---
title: Isolate Database State Per Test
impact: HIGH
impactDescription: Rows left behind by one test make the next test's assertions depend on execution order
tags: phpunit, isolation, database, transactions, integration
---

## Isolate Database State Per Test

**Impact: HIGH — A shared, accumulating database turns a suite into a sequence that only works in one order**

Every test starts from a known state and leaves nothing behind. Two mechanisms achieve this; pick one and apply it consistently.

## Bad Example

```php
final class OrderRepositoryTest extends TestCase
{
    public function test_it_saves_an_order(): void
    {
        $this->repository->save($this->anOrder(id: 'o_1'));

        $this->assertCount(1, $this->repository->all());   // only true on a clean database
    }

    public function test_it_finds_orders_by_customer(): void
    {
        // relies on o_1 from the previous test still existing
        $this->assertCount(1, $this->repository->forCustomer('c_1'));
    }
}
```

Run the second test alone and it fails. Run the suite twice without resetting and the first fails. Both get "fixed" by seeding more data, which deepens the coupling.

## Good Example — transaction rollback (fastest)

```php
abstract class DatabaseTestCase extends TestCase
{
    protected PDO $pdo;

    protected function setUp(): void
    {
        $this->pdo = TestDatabase::connection();
        $this->pdo->beginTransaction();
    }

    protected function tearDown(): void
    {
        $this->pdo->rollBack();          // everything the test wrote disappears
    }
}
```

```php
final class OrderRepositoryTest extends DatabaseTestCase
{
    public function test_it_finds_orders_by_customer(): void
    {
        $this->repository->save($this->anOrder(id: 'o_1', customerId: 'c_1'));

        $this->assertCount(1, $this->repository->forCustomer('c_1'));
    }
}
```

## Good Example — truncation (when the code under test commits)

```php
protected function setUp(): void
{
    $this->pdo->exec('TRUNCATE orders, order_items RESTART IDENTITY CASCADE');
}
```

Use this when the system under test manages its own transactions — a service calling `commit()` inside a wrapping test transaction either fails or, with nested-transaction emulation, commits for real.

## Notes

- **Match production.** Run against the same engine and version you deploy: Testcontainers makes a per-run PostgreSQL or MySQL container cheap. SQLite standing in for PostgreSQL hides exactly what integration tests exist to catch — constraint behaviour, JSON operators, isolation levels, and migration correctness.
- Frameworks provide this: Laravel's `RefreshDatabase`, Doctrine's `dbunit`-style fixtures, Symfony's `DAMADoctrineTestBundle` (transaction rollback). Prefer the framework mechanism over a hand-rolled one.
- Do not test against a shared development or staging database. Parallel runs will interleave, and a truncation will eventually run somewhere it should not.
- Create data through factories, not raw SQL, so schema changes break the factory once instead of every test.
- Keep database tests in a separate suite (`<testsuite name="integration">`) so the unit suite stays fast and runnable without infrastructure.
- Auto-increment ids continue climbing after a rollback. Never assert on a literal id — assert on the value you inserted.

## Why

- **Order independence**: Any test can run alone or in any position.
- **Repeatability**: The suite produces the same result on the second run without a manual reset.
- **Parallel safety**: Isolated state is what makes running the suite across workers possible at all.
