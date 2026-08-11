---
title: Build Fixtures with Named Factories, Not Accumulated setUp()
impact: HIGH
impactDescription: A shared setUp() couples every test to one object graph and hides the inputs that actually matter for each case
tags: phpunit, fixtures, setup, factories, readability
---

## Build Fixtures with Named Factories, Not Accumulated setUp()

**Impact: HIGH — When the relevant input lives in setUp(), a reader cannot tell from the test body why it passes**

`setUp()` is for wiring the system under test and its collaborators. Scenario data belongs in named factory methods called from the test that needs it.

## Bad Example

```php
protected function setUp(): void
{
    $this->customer = new Customer('c_1', 'a@b.co', tier: Tier::Gold);   // why Gold?
    $this->order = new Order($this->customer);
    $this->order->addItem(new Item('SKU-1', 1_000, 12));                 // why 12?
    $this->order->applyCoupon(new Coupon('SUMMER', 0.10));
    $this->service = new PricingService(new TaxCalculator(0.20));
}

public function test_it_applies_the_bulk_discount(): void
{
    $this->assertSame(10_800, $this->service->total($this->order));      // where does 12 come from?
}
```

The quantity `12` is the whole point of the test and it is 30 lines away. Changing it for a new test breaks the others; adding a field for one test adds it for all.

## Good Example

```php
protected function setUp(): void
{
    $this->service = new PricingService(new TaxCalculator(0.20));        // SUT wiring only
}

private function anOrder(int $quantity, Tier $tier = Tier::Standard): Order
{
    $order = new Order(new Customer('c_1', 'a@b.co', $tier));
    $order->addItem(new Item('SKU-1', 1_000, $quantity));

    return $order;
}

public function test_it_applies_the_bulk_discount_above_ten_units(): void
{
    $order = $this->anOrder(quantity: 12);

    $this->assertSame(10_800, $this->service->total($order));
}

public function test_it_charges_full_price_at_ten_units(): void
{
    $order = $this->anOrder(quantity: 10);

    $this->assertSame(12_000, $this->service->total($order));
}
```

Each test states the one value that makes it different. The factory absorbs everything irrelevant.

## Notes

- Factories take **defaults plus overrides**, so a test names only what it cares about. Named arguments make the call site self-documenting.
- Object mothers (`anOrder()`, `aGoldCustomer()`) belong in the test class when local, or in a shared `Tests\Support` namespace when reused. Do not put them in `setUp()`.
- `setUpBeforeClass()` runs once per class and its state persists across the tests in that class — a direct route to order-dependent failures ([`iso-no-shared-state`](iso-no-shared-state.md)). Use it only for genuinely immutable, expensive resources.
- `tearDown()` should be unnecessary for anything created inside a test. If you need it to undo global state, the state should not be global.
- PHPUnit 12 runs `setUp()` before every test method and creates a fresh test-case instance per test — properties do not leak between methods, but static properties and external systems still do.

## Why

- **Locality**: The value that determines the expected result is visible in the same three lines as the assertion.
- **Independence**: Adding a scenario means adding a factory argument, not editing a fixture every other test depends on.
- **Cheap deletion**: Removing a test removes its data. A shared fixture accumulates fields nobody dares delete.
