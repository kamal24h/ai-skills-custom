---
title: Data Providers Must Be Static and Free of Fixtures
impact: HIGH
impactDescription: PHPUnit 10+ requires static providers; a provider touching $this or the container fails or silently runs before setUp()
tags: phpunit, data-provider, static, attributes, phpunit12
---

## Data Providers Must Be Static and Free of Fixtures

**Impact: HIGH — Providers run before the test object is prepared, so anything they touch from the instance is unavailable or stale**

PHPUnit resolves every data provider up front, ahead of `setUp()`, to build the list of tests. In PHPUnit 10 and later the provider method must be `public static`, and it cannot depend on instance state.

## Bad Example

```php
// ❌ not static — an error in PHPUnit 10+
public function orderProvider(): array
{
    return [
        [$this->anOrder(quantity: 5), 5_000],       // ❌ instance method, and setUp() has not run
        [$this->repository->find('o_1'), 9_900],    // ❌ database access while collecting tests
    ];
}

/** @dataProvider orderProvider */                   // ❌ annotations removed in PHPUnit 12
public function test_it_prices_orders(Order $order, int $expected): void { … }
```

Three separate failures: the method is not static, it builds objects that should be created per test, and it uses the doc-comment annotation that PHPUnit 12 no longer reads — so the test silently runs once with no arguments and errors on the missing parameters.

## Good Example

```php
/** @return array<string, array{int, int}> */
public static function quantityProvider(): array
{
    return [
        'single unit'        => [1,  1_000],
        'below bulk cutoff'  => [9,  9_000],
        'at bulk cutoff'     => [10, 10_000],
        'above bulk cutoff'  => [11, 9_900],
    ];
}

#[DataProvider('quantityProvider')]
public function test_it_prices_an_order_by_quantity(int $quantity, int $expectedTotal): void
{
    $order = $this->anOrder($quantity);            // objects built inside the test, after setUp()

    $this->assertSame($expectedTotal, $this->service->total($order));
}
```

The provider supplies **scalars**; the test turns them into objects. Each case is independent and named.

## Notes

- Pass primitives and enums, not built objects. Objects created in a provider are shared across data sets and constructed before any fixture exists.
- String keys become data-set names in the output: `test_it_prices_an_order_by_quantity with data set "at bulk cutoff"`. Numeric keys give you `with data set #2`, which tells you nothing ([`data-provider-named-sets`](data-provider-named-sets.md)).
- A provider may `yield` instead of returning an array — useful for large sets, and it keeps memory flat.
- Use `#[DataProviderExternal(OtherClass::class, 'method')]` to share a provider across test classes rather than inheriting from a base test case.
- Providers must not perform I/O. Reading a fixture file or querying a database at collection time makes `--list-tests` require a database.
- Under a strict configuration, a provider returning an empty array is reported rather than silently skipped.

## Why

- **Correct lifecycle**: Providers run during test collection; instance state does not exist yet.
- **Independent cases**: Scalar inputs guarantee each data set builds its own objects.
- **Fast collection**: `--list-tests`, filtering, and IDE integration stay usable when providers are pure.
