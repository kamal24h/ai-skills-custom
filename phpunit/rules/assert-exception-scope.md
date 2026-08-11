---
title: Scope Exception Expectations to the Call That Should Throw
impact: HIGH
impactDescription: expectException() at the top of a test passes if any line throws, including the fixture setup that was supposed to succeed
tags: phpunit, assertions, exceptions, false-positive
---

## Scope Exception Expectations to the Call That Should Throw

**Impact: HIGH — A test that passes because the wrong line threw is a false positive that hides a broken fixture**

`expectException()` arms an expectation for the whole remaining test method. Anything after it that throws the right class satisfies it.

## Bad Example

```php
public function test_it_rejects_a_negative_quantity(): void
{
    $this->expectException(InvalidArgumentException::class);

    $catalog = new Catalog($this->repository);      // if THIS throws, the test still passes
    $product = $catalog->find('SKU-1');             // …or this
    $order   = new Order($this->customer);
    $order->add($product, -1);                      // the line actually under test
}
```

Delete the `$order->add()` line entirely and this test still passes as long as anything above it throws an `InvalidArgumentException` — including a typo in the repository fixture.

Worse, nothing after the throwing call executes, so any assertion placed below it never runs:

```php
$this->expectException(InvalidArgumentException::class);
$order->add($product, -1);
$this->assertCount(0, $order->items());             // never reached, silently
```

## Good Example

```php
public function test_it_rejects_a_negative_quantity(): void
{
    // Arrange — must not be inside the expectation window
    $order = $this->anOrder();
    $product = $this->aProduct();

    // Act + Assert
    $this->expectException(InvalidArgumentException::class);
    $this->expectExceptionMessage('Quantity must be positive');

    $order->add($product, -1);
}
```

Arrange first, arm the expectation immediately before the act, and make the act the last statement.

When you need to assert on state after the throw, catch explicitly:

```php
public function test_it_leaves_the_order_unchanged_when_the_quantity_is_invalid(): void
{
    $order = $this->anOrderWith($this->anItem());

    try {
        $order->add($this->aProduct(), -1);
        $this->fail('Expected InvalidArgumentException');
    } catch (InvalidArgumentException $e) {
        $this->assertSame('Quantity must be positive', $e->getMessage());
    }

    $this->assertCount(1, $order->items());          // now reachable
}
```

## Notes

- `$this->fail()` after the call is what makes the `try`/`catch` form safe — without it, a non-throwing implementation passes silently.
- Narrow the expectation: `expectException(InvalidArgumentException::class)` also matches subclasses. When the specific type matters, assert on `get_class($e)` in the catch form.
- `expectExceptionMessage()` does a substring match; `expectExceptionMessageMatches()` takes a regex. Prefer asserting on a stable error **code** where one exists — messages are copy and get reworded.
- Do not assert only on the message. A test that passes because the wording matched, while the wrong exception class was thrown, is another false positive.
- PHPUnit 12 removed `expectExceptionMessageRegExp()`; use `expectExceptionMessageMatches()`.

## Why

- **No false positives**: The expectation covers exactly the call it is meant to cover.
- **Post-throw assertions become possible**: The catch form lets you verify the object was left in a valid state.
- **Fixture failures stay visible**: A broken arrange step fails as an error instead of masquerading as a pass.
