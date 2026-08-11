# Isolation & State

Why tests become intermittent, and the state boundaries that keep them deterministic.

## When to Load

- A test passes locally and fails in CI, or fails only when run with others
- Introducing `--order-by=random` to an existing suite
- Writing tests that touch the database, filesystem, clock, or environment
- A suite cannot be run in parallel

## Rule Index

- [`iso-no-shared-state`](../rules/iso-no-shared-state.md) — Nothing survives between tests
- [`iso-inject-time-randomness`](../rules/iso-inject-time-randomness.md) — Clock and randomness as dependencies
- [`iso-database-per-test`](../rules/iso-database-per-test.md) — Transaction rollback or truncation per test

## What PHPUnit Isolates For You, and What It Does Not

| | Isolated per test | Notes |
|---|---|---|
| `$this` properties | ✅ | A fresh test-case instance is created per method |
| `setUp()` / `tearDown()` | ✅ | Run around every method |
| `static` properties | ❌ | Persist for the whole process |
| `setUpBeforeClass()` state | ❌ | Persists for the class |
| Singletons / service locators | ❌ | Persist for the process |
| `$_SERVER`, `$_ENV`, `putenv`, `ini_set` | ❌ | Process-global |
| Database rows | ❌ | You must roll back or truncate |
| Filesystem | ❌ | You must clean up |
| The clock, randomness | ❌ | Inject them |

Everything in the second group is a potential order dependency. The list is short enough to grep for.

## The Diagnostic Procedure

When a suite starts failing intermittently:

```bash
# 1. Confirm it is an order dependency
vendor/bin/phpunit --order-by=random --random-order-seed=12345

# 2. Reproduce deterministically with the same seed
vendor/bin/phpunit --random-order-seed=12345

# 3. Does the failing test pass alone?
vendor/bin/phpunit --filter test_it_lists_orders
#    passes alone + fails in suite = shared state
#    fails alone                    = a real bug

# 4. Bisect: run the suspect with progressively fewer neighbours
vendor/bin/phpunit --filter 'OrderServiceTest|PricingServiceTest'
```

Then grep the implicated files for the second-group items above. The culprit is almost always a `static` property, a container that was not rebuilt, or an uncommitted database write.

## Time and Randomness

The two most common sources of "fails at 02:00" and "fails on the 31st":

```php
// PSR-20
interface ClockInterface { public function now(): DateTimeImmutable; }
```

```php
$clock = new FrozenClock(new DateTimeImmutable('2025-01-31 12:00:00'));
$service = new SubscriptionService($clock);

$this->assertSame('2025-02-28', $service->renew($sub)->expiresAt()->format('Y-m-d'));
```

The same treatment applies to `uniqid()`, `random_int()`, `shuffle()`, `array_rand()`, and `session_id()`. Any of these called inside production code makes the outcome unassertable.

Store timestamps in UTC and convert at the presentation edge — most DST-related flakiness is a local timezone leaking into domain logic.

## Database

Two strategies, both acceptable:

```php
// A. transaction rollback — fastest, but the SUT must not commit
protected function setUp(): void    { $this->pdo->beginTransaction(); }
protected function tearDown(): void { $this->pdo->rollBack(); }

// B. truncation — required when the code under test manages transactions
protected function setUp(): void
{
    $this->pdo->exec('TRUNCATE orders, order_items RESTART IDENTITY CASCADE');
}
```

Run against the production engine and version — Testcontainers makes a per-run container cheap:

```php
$container = (new PostgreSqlContainer('postgres:17'))->start();
```

SQLite substituting for PostgreSQL hides constraint semantics, JSON operators, isolation-level behaviour, and migration correctness — which is most of what an integration test is for.

Never assert on a literal auto-increment id; sequences keep climbing across rollbacks.

## Filesystem

```php
protected function setUp(): void
{
    $this->tmp = sys_get_temp_dir() . '/test_' . bin2hex(random_bytes(8));
    mkdir($this->tmp);
}

protected function tearDown(): void
{
    // recursive delete
}
```

A fixed path under the project directory collides between parallel workers and leaves artefacts that make the next run pass for the wrong reason. Better still, use an in-memory filesystem abstraction (`league/flysystem` with an in-memory adapter) and skip the disk entirely.

## Containment for Legacy Code

PHPUnit provides escape hatches. They are slow and should be treated as debt markers, not design:

```php
#[BackupGlobals(true)]           // save/restore superglobals around the test
#[BackupStaticProperties(true)]  // save/restore static properties
#[RunInSeparateProcess]          // fork a process for this test
#[RunTestsInSeparateProcesses]   // …for every test in the class
```

`RunInSeparateProcess` costs a full bootstrap per test. Use it to unblock a legacy class today and record the underlying static state as something to remove.

## Parallelism

Isolation is the precondition for parallel execution. Once tests are order-independent, `paratest` distributes them across workers:

```bash
vendor/bin/paratest --processes=8
```

Each worker needs its own database — usually `APP_DB_NAME=test_$TEST_TOKEN` in the bootstrap. Any remaining shared resource surfaces immediately as a failure, which makes parallel runs a useful isolation check in themselves.

## Sources

- [PHPUnit — Fixtures](https://docs.phpunit.de/en/12.0/fixtures.html)
- [PHPUnit — Test dependencies and execution order](https://docs.phpunit.de/en/12.0/writing-tests-for-phpunit.html#test-dependencies)
- [PSR-20: Clock](https://www.php-fig.org/psr/psr-20/)
- [Testcontainers for PHP](https://testcontainers.com/)
- [ParaTest](https://github.com/paratestphp/paratest)
