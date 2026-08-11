---
title: Keep Conditionals and Loops Out of Test Bodies
impact: HIGH
impactDescription: A branch inside a test means one of its paths is never exercised and nobody notices
tags: phpunit, assertions, complexity, data-provider
---

## Keep Conditionals and Loops Out of Test Bodies

**Impact: HIGH — Test code is not itself tested; every `if` in a test is untested logic guarding your verification**

A test should be a straight line. Branching in the test means the assertion that runs depends on the code under test, which is circular.

## Bad Example

```php
public function test_discount(): void
{
    foreach ([5, 10, 15, 20] as $quantity) {
        $total = $this->service->total($this->anOrder($quantity));

        if ($quantity > 10) {
            $this->assertLessThan($quantity * 1_000, $total);   // vague, and only for 2 of 4 cases
        } else {
            $this->assertSame($quantity * 1_000, $total);
        }
    }
}
```

Three problems: the first failure aborts the remaining iterations, the failure message does not say which quantity broke, and the `> 10` branch duplicates the business rule — so if the rule is wrong in both places, the test agrees with the bug.

## Good Example

```php
public static function quantityProvider(): array
{
    return [
        'below threshold'   => [5,  5_000],
        'at threshold'      => [10, 10_000],
        'above threshold'   => [12, 10_800],
        'well above'        => [20, 18_000],
    ];
}

#[DataProvider('quantityProvider')]
public function test_it_prices_an_order_by_quantity(int $quantity, int $expectedTotal): void
{
    $this->assertSame($expectedTotal, $this->service->total($this->anOrder($quantity)));
}
```

Four independent cases with hard-coded expectations. All four run, and a failure reports `test_it_prices_an_order_by_quantity with data set "above threshold"`.

## Notes

- **Hard-code expected values.** Computing the expectation with the same formula the code uses (`$quantity * 1_000 * 0.9`) tests that the formula equals itself. Write `10_800`.
- Loops over a collection to assert on each element are usually one assertion in disguise: `assertSame($expected, array_map(fn($i) => $i->sku(), $items))`.
- `try`/`catch` in a test is acceptable only in the exception form with `$this->fail()` ([`assert-exception-scope`](assert-exception-scope.md)).
- Conditional skipping is different and legitimate: `markTestSkipped()` when an extension is missing, or `#[RequiresPhpExtension('redis')]`. That is environment gating, not verification branching.
- If a test needs a switch to decide what to assert, it is covering multiple behaviours ([`struct-one-behaviour`](struct-one-behaviour.md)).

## Why

- **Every case runs**: A data provider produces independent tests; a loop stops at the first failure.
- **Failures identify themselves**: The data-set name appears in the report.
- **No duplicated business rules**: Hard-coded expectations cannot silently agree with a bug in the implementation.
