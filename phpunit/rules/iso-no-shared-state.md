---
title: No Shared State Between Tests
impact: CRITICAL
impactDescription: Order-dependent tests pass locally, fail in CI under a different order, and get "fixed" by disabling randomisation
tags: phpunit, isolation, static-state, global, flaky
---

## No Shared State Between Tests

**Impact: CRITICAL — A test that depends on another test's leftovers is an intermittent failure waiting for a parallel runner or a filter flag**

PHPUnit creates a fresh test-case instance per test method, so `$this` properties are safe. Everything outside the instance is not: static properties, singletons, superglobals, the filesystem, the database, and any long-lived container.

## Bad Example

```php
final class OrderServiceTest extends TestCase
{
    private static array $created = [];              // ❌ survives every test in the class

    public function test_it_creates_an_order(): void
    {
        self::$created[] = $this->service->create($this->anOrder());

        $this->assertCount(1, self::$created);       // passes only if this runs first
    }

    public function test_it_lists_orders(): void
    {
        $this->assertCount(1, $this->service->all()); // depends on the previous test's INSERT
    }
}
```

```php
// ❌ global state mutated and never restored
public function test_it_formats_dates_for_the_locale(): void
{
    date_default_timezone_set('Asia/Istanbul');       // every later test now runs in +03
    Config::set('app.locale', 'tr');                  // static config, never reset
}
```

Both pass in file order and fail under `--order-by=random`, under `--filter`, and when a colleague adds a test above them.

## Good Example

```php
final class OrderServiceTest extends TestCase
{
    private OrderService $service;
    private InMemoryOrderRepository $repository;

    protected function setUp(): void
    {
        $this->repository = new InMemoryOrderRepository();     // rebuilt per test
        $this->service = new OrderService($this->repository);
    }

    public function test_it_creates_an_order(): void
    {
        $this->service->create($this->anOrder());

        $this->assertCount(1, $this->repository->all());
    }

    public function test_it_lists_orders(): void
    {
        $this->repository->save($this->anOrder());             // this test arranges its own world

        $this->assertCount(1, $this->service->all());
    }
}
```

```php
// Environment changes restored explicitly
protected function setUp(): void
{
    $this->originalTimezone = date_default_timezone_get();
    date_default_timezone_set('UTC');
}

protected function tearDown(): void
{
    date_default_timezone_set($this->originalTimezone);
}
```

## Notes

- **Verify by randomising.** `--order-by=random` in CI is what turns a hidden dependency into a visible failure. Record the seed so the order is reproducible ([`ci-strict-config`](ci-strict-config.md)).
- Databases: wrap each test in a transaction and roll back, or truncate the touched tables in `tearDown()`. A shared seeded database makes order significant by construction.
- `setUpBeforeClass()` state persists for the whole class. Use it only for immutable, expensive resources — a compiled schema, not a repository.
- `#[BackupStaticProperties]` and `#[BackupGlobals]` exist, and `#[RunInSeparateProcess]` isolates a test entirely. All three are slow; treat them as containment for legacy code, not as a design.
- Filesystem: write to a unique temp directory per test and remove it in `tearDown()`. Never a fixed path under the project.
- `$_SERVER`, `$_ENV`, `putenv()`, `ini_set()`, and static registries are the usual leak sources — grep for them when a suite starts failing intermittently.

## Why

- **Order independence**: Any test can run alone, first, last, or in parallel.
- **Real failure signals**: An intermittent failure means a bug, not a leaked fixture.
- **Filter usability**: `--filter` on one test gives a trustworthy result.
