# Test Structure

How a test class is organised, named, and built — the layer that decides whether a failure is diagnosable.

## When to Load

- Writing a new test class or reorganising an existing one
- Deciding what belongs in `setUp()` versus a factory method
- Naming tests, or reviewing a suite whose names carry no information
- A test failure did not tell you what broke

## Rule Index

- [`struct-aaa`](../rules/struct-aaa.md) — Arrange, act, assert, with one act statement
- [`struct-one-behaviour`](../rules/struct-one-behaviour.md) — One claim per test method
- [`struct-descriptive-names`](../rules/struct-descriptive-names.md) — Name the scenario and expectation
- [`struct-factory-over-setup`](../rules/struct-factory-over-setup.md) — Named factories over accumulated fixtures

## Anatomy of a Test Class

```php
<?php

declare(strict_types=1);

namespace App\Tests\Unit\Pricing;

use App\Pricing\PricingService;
use PHPUnit\Framework\Attributes\CoversClass;
use PHPUnit\Framework\Attributes\DataProvider;
use PHPUnit\Framework\Attributes\Test;
use PHPUnit\Framework\TestCase;

#[CoversClass(PricingService::class)]
final class PricingServiceTest extends TestCase
{
    private PricingService $service;                    // 1. SUT and collaborators as typed properties

    protected function setUp(): void                    // 2. wiring only — no scenario data
    {
        $this->service = new PricingService(
            new FixedTaxRateProvider(0.20),
            new InMemoryDiscountPolicy(),
        );
    }

    #[Test]                                             // 3. tests: one behaviour each
    public function it_applies_tax_to_the_subtotal(): void
    {
        $order = $this->anOrder(quantity: 2);

        $total = $this->service->total($order);

        $this->assertSame(2_400, $total);
    }

    private function anOrder(int $quantity): Order      // 4. factories last, defaults + overrides
    {
        return new Order(new Customer('c_1'), [new Item('SKU-1', 1_000, $quantity)]);
    }
}
```

Four zones, always in this order: state, setup, tests, factories. A reader scanning the file finds the behaviours in the middle without wading through fixture construction.

## Directory and Suite Layout

```
tests/
├── Unit/                 → no I/O, no database, no network. Milliseconds.
│   └── Pricing/PricingServiceTest.php
├── Integration/          → real database, real framework container, faked third parties
│   └── Repository/OrderRepositoryTest.php
├── Feature/              → HTTP entry point through to persistence
│   └── Checkout/PlaceOrderTest.php
└── Support/              → factories, fakes, base test cases (not tests)
    ├── InMemoryOrderRepository.php
    └── OrderFactory.php
```

Mirror the `src/` namespace under each suite so the test for a class is findable by path. Register the suites separately in `phpunit.xml` so the fast one can run alone:

```xml
<testsuite name="unit"><directory>tests/Unit</directory></testsuite>
<testsuite name="integration"><directory>tests/Integration</directory></testsuite>
```

`tests/Support` must not be picked up by any suite — it contains no test classes.

## What to Test, and at Which Level

| Level | Covers | Doubles | Speed |
|---|---|---|---|
| Unit | Domain rules, calculations, state machines, validators | Everything external | ms |
| Integration | Repositories, queries, framework wiring, serialisation | Third-party HTTP only | 10s–100s of ms |
| Feature/E2E | Critical user journeys end to end | Nothing internal | seconds |

The distribution matters more than the labels. A suite that is 100% unit tests with everything doubled stays green while the wiring between layers is broken, because nothing ever exercises two real components together. A suite that is mostly feature tests is slow enough that people stop running it.

**Do not test**: framework internals, third-party library behaviour, getters and setters with no logic, or configuration constants. Each of those costs maintenance and verifies nothing you own.

## Base Test Cases

A shared base class is justified for infrastructure, not for convenience helpers:

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
        $this->pdo->rollBack();
    }
}
```

Prefer **traits** for reusable helpers and **factories in `Support/`** for data. A deep base-class hierarchy where every test inherits ten unused helpers reproduces the shared-fixture problem at class level.

## Assertion Density

One behaviour per test does not mean one assertion per test. These are all one claim:

```php
$this->assertSame('a@b.co', $user->email());
$this->assertSame(Role::Member, $user->role());
$this->assertFalse($user->isVerified());
```

Better still when the type allows it:

```php
$this->assertEquals(new User('a@b.co', Role::Member, verified: false), $user);
```

The split point is topical, not numeric: assertions about the returned user belong together; an assertion about a sent email is a different behaviour.

## Sources

- [PHPUnit — Writing tests for PHPUnit](https://docs.phpunit.de/en/12.0/writing-tests-for-phpunit.html)
- [PHPUnit — Organizing tests](https://docs.phpunit.de/en/12.0/organizing-tests.html)
- [PHPUnit — Fixtures](https://docs.phpunit.de/en/12.0/fixtures.html)
- [Martin Fowler — Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
- [Martin Fowler — Object Mother](https://martinfowler.com/bliki/ObjectMother.html)
