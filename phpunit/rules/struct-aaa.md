---
title: Structure Every Test as Arrange, Act, Assert
impact: CRITICAL
impactDescription: A test without a visible act step forces the reader to reverse-engineer what is being tested from the assertions
tags: phpunit, structure, aaa, readability
---

## Structure Every Test as Arrange, Act, Assert

**Impact: CRITICAL — When arrange and act are interleaved, a failure tells you a value was wrong but not which call produced it**

Three blocks, separated by blank lines, in order: build the world, perform the one operation under test, verify the outcome.

## Bad Example

```php
public function test_order_total(): void
{
    $calculator = new TaxCalculator(0.20);
    $order = new Order();
    $order->addItem(new Item('SKU-1', 1_000, 2));
    $this->assertSame(2_000, $order->subtotal());          // assertion in the middle
    $order->addItem(new Item('SKU-2', 500, 1));
    $order->applyTax($calculator);
    $this->assertSame(3_000, $order->subtotal());
    $this->assertSame(3_600, $order->total());             // which call is under test?
}
```

Three operations and three assertions interleaved. When `total()` returns the wrong number, the failure could originate in any of the three mutations above it.

## Good Example

```php
public function test_it_applies_tax_to_the_order_subtotal(): void
{
    // Arrange
    $order = $this->anOrderWith(
        new Item('SKU-1', 1_000, 2),
        new Item('SKU-2', 500, 1),
    );

    // Act
    $order->applyTax(new TaxCalculator(0.20));

    // Assert
    $this->assertSame(3_600, $order->total());
}
```

One call between arrange and assert. If this fails, `applyTax` is the suspect.

## Notes

- The comments are optional; the blank lines are not. Many teams drop the labels once the shape is habitual.
- **Act must be a single statement.** If it takes three calls to reach the state you want to assert on, those calls are arrange — or the test is covering more than one behaviour ([`struct-one-behaviour`](struct-one-behaviour.md)).
- Assertions on the arrange step (`assertSame(2_000, $order->subtotal())` above) mean you do not trust the fixture. Either that setup deserves its own test, or use a factory that cannot produce an invalid object.
- For exception tests, `expectException()` belongs in the arrange block, immediately before the act call — see [`assert-exception-scope`](assert-exception-scope.md).

## Why

- **Localised blame**: A single act statement means a failure names one operation.
- **Readable diffs**: Reviewers can see what changed about the scenario versus what changed about the expectation.
- **Refactor resistance**: Tests structured this way survive internal refactors, because they touch the object only through the public entry point.
