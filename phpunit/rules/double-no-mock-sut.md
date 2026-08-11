---
title: Never Double the System Under Test
impact: CRITICAL
impactDescription: A partial mock of the class being tested verifies the double, not the code, and can pass with the real method deleted
tags: phpunit, test-doubles, partial-mock, sut, false-positive
---

## Never Double the System Under Test

**Impact: CRITICAL — Replacing part of the class under test means the suite no longer verifies that class**

`createPartialMock()` and `onlyMethods()` applied to the SUT replace real behaviour with canned answers. Whatever they replace is no longer tested — and often the replaced method is the interesting one.

## Bad Example

```php
public function test_it_calculates_the_total(): void
{
    $service = $this->createPartialMock(PricingService::class, ['taxRate', 'discountFor']);
    $service->method('taxRate')->willReturn(0.19);
    $service->method('discountFor')->willReturn(0.10);

    $this->assertSame(10_710, $service->total($this->anOrder()));
}
```

`taxRate()` and `discountFor()` are never executed. Delete their bodies entirely and this test still passes. The only thing verified is the arithmetic in `total()` — and the moment someone inlines the tax logic into `total()`, the test breaks for no behavioural reason.

The instinct to reach for this almost always signals a design problem: `PricingService` is doing too much, and the private methods you want to stub are a collaborator waiting to be extracted.

## Good Example

```php
// The hidden collaborators become explicit
final class PricingService
{
    public function __construct(
        private readonly TaxRateProvider $rates,
        private readonly DiscountPolicy $discounts,
    ) {}

    public function total(Order $order): int { … }
}
```

```php
public function test_it_applies_tax_and_discount_to_the_total(): void
{
    $rates = $this->createStub(TaxRateProvider::class);
    $rates->method('forCountry')->willReturn(0.19);

    $discounts = $this->createStub(DiscountPolicy::class);
    $discounts->method('rateFor')->willReturn(0.10);

    $service = new PricingService($rates, $discounts);       // the real class, fully executed

    $this->assertSame(10_710, $service->total($this->anOrder()));
}
```

Now the tax and discount rules have their own tests, and `PricingService` is tested end to end through its public API.

## Notes

- The same applies to `getMockBuilder(SUT::class)->onlyMethods([...])` and to subclassing the SUT in the test file to override a method.
- **Do not test private methods.** They are reached through the public API; if a private method is complex enough to need direct testing, it is a class that has not been extracted yet. Reflection-based access to privates couples the test to the implementation permanently.
- Legitimate uses of partial doubles exist and are all about code you do not own: an abstract third-party base class, or a legacy class whose constructor performs I/O and cannot be changed yet. Mark those as debt.
- Static calls and `new` inside a method create the same untestable coupling. Inject a factory or the collaborator itself.

## Why

- **The test verifies the real thing**: Every line of the SUT actually runs.
- **Design feedback**: The urge to stub a private method is accurate information — it names a missing collaborator.
- **No false positives**: A partial mock can keep passing after the real implementation is deleted; the injected-collaborator form cannot.
