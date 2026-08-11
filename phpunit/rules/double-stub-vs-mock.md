---
title: Stub for State, Mock for Interaction
impact: HIGH
impactDescription: Setting expectations on every collaborator call couples the test to the implementation's call sequence
tags: phpunit, test-doubles, mock, stub, coupling
---

## Stub for State, Mock for Interaction

**Impact: HIGH — A mock with expectations is an assertion about *how* the code works; use it only where the interaction itself is the behaviour**

`createStub()` provides canned answers and verifies nothing. `createMock()` can additionally assert that calls happened, with what arguments, how many times.

Default to stubs. Reach for a mock when the observable effect **is** the call — an email sent, an event published, a payment charged.

## Bad Example

```php
public function test_it_calculates_the_total(): void
{
    $rates = $this->createMock(TaxRateProvider::class);
    $rates->expects($this->once())                       // ❌ why must it be called exactly once?
          ->method('forCountry')
          ->with('DE')                                    // ❌ locks in the argument shape
          ->willReturn(0.19);

    $repository = $this->createMock(OrderRepository::class);
    $repository->expects($this->once())->method('find')->with('o_1')->willReturn($this->anOrder());
    $logger = $this->createMock(LoggerInterface::class);
    $logger->expects($this->once())->method('debug');     // ❌ now a log line is part of the contract

    $total = (new PricingService($rates, $repository, $logger))->total('o_1');

    $this->assertSame(11_900, $total);
}
```

Caching the rate lookup, reordering calls, or removing a debug log all break this test without changing behaviour. The one real assertion is the last line.

## Good Example

```php
public function test_it_applies_the_country_tax_rate_to_the_total(): void
{
    $rates = $this->createStub(TaxRateProvider::class);
    $rates->method('forCountry')->willReturn(0.19);       // just a value source

    $service = new PricingService($rates, $this->repositoryReturning($this->anOrder()), new NullLogger());

    $this->assertSame(11_900, $service->total('o_1'));
}
```

```php
public function test_it_sends_a_receipt_when_the_payment_succeeds(): void
{
    $mailer = $this->createMock(Mailer::class);
    $mailer->expects($this->once())                        // ✅ the call IS the behaviour
           ->method('send')
           ->with(
               $this->equalTo('a@b.co'),
               $this->callback(fn(Receipt $r) => $r->orderId() === 'o_1'),
           );

    (new CheckoutService($this->successfulGateway(), $mailer))->pay('o_1');
}
```

## Notes

- `createStub()` cannot be given expectations at all — using it documents "this is a value source" and prevents accidental over-specification.
- Prefer `$this->any()` or no expectation for incidental calls. `expects($this->once())` on every method turns refactors into test rewrites.
- Loggers, clocks, and caches are almost never worth mocking with expectations. Use a null implementation or an in-memory fake.
- `createMock()` on a class with a constructor does not call it — the double is a subclass with all methods replaced. That is why doubling **interfaces** is safer ([`double-interface-not-concrete`](double-interface-not-concrete.md)).
- PHPUnit 12 removed `getMockBuilder()`'s deprecated configuration methods; `createMock()`, `createStub()`, `createConfiguredMock()`, and `createMockForIntersectionOfInterfaces()` cover the useful cases.

## Why

- **Refactor tolerance**: Stubs let the implementation change how it obtains a value without breaking the test.
- **Meaningful failures**: A mock expectation that fails should mean a real contract was broken, not that a call order changed.
- **Readable intent**: Stub versus mock tells the next reader whether the collaborator is an input or an output.
