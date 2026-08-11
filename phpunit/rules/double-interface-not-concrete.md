---
title: Double Interfaces, Not Concrete Classes
impact: HIGH
impactDescription: A double of a concrete class silently keeps passing after the real class changes its constructor, return types, or method set
tags: phpunit, test-doubles, interfaces, coupling, design
---

## Double Interfaces, Not Concrete Classes

**Impact: HIGH — Doubling a concrete class ties the test to that class's shape while bypassing every guarantee it makes**

`createMock(ConcreteClass::class)` builds a subclass with all methods overridden and the constructor skipped. The double has the class's method names but none of its behaviour, and none of its invariants.

## Bad Example

```php
public function test_it_charges_the_customer(): void
{
    // Doubling the vendor's concrete client
    $stripe = $this->createMock(\Stripe\StripeClient::class);
    $stripe->method('charge')->willReturn(new \Stripe\Charge());   // constructing a vendor value object

    $service = new CheckoutService($stripe);

    $this->assertTrue($service->pay('o_1')->isSuccessful());
}
```

Problems this creates:

- The vendor renames `charge()` to `createCharge()` in a minor release — the double happily provides `charge()`, the test passes, production breaks.
- The double's `charge()` returns a `Charge` built without its constructor, so its properties are null in ways the real object never is.
- `CheckoutService` is now typed against a vendor class; swapping providers means editing the service, not just the wiring.

## Good Example

```php
// Your boundary, your contract
interface PaymentGateway
{
    public function charge(string $orderId, Money $amount): PaymentResult;
}

final class StripeGateway implements PaymentGateway { … }   // adapter, covered by an integration test
```

```php
public function test_it_reports_success_when_the_gateway_accepts_the_charge(): void
{
    $gateway = $this->createStub(PaymentGateway::class);
    $gateway->method('charge')->willReturn(PaymentResult::accepted('ch_1'));

    $service = new CheckoutService($gateway);

    $this->assertTrue($service->pay('o_1')->isSuccessful());
}
```

The interface is small, owned by you, and expressed in your domain types. The vendor's shape is confined to `StripeGateway`, which is verified once against the real API in an integration test.

## Notes

- Doubling a **final** class is impossible without extensions — a signal to introduce an interface rather than to install `dg/bypass-finals`.
- `createMockForIntersectionOfInterfaces([A::class, B::class])` handles a dependency requiring several narrow interfaces without inventing a combined one.
- A hand-written fake often beats a generated double when the collaborator has state: an `InMemoryOrderRepository` implementing the interface is more readable than five `willReturn` chains and can be reused across the suite ([`double-fake-over-chain`](double-fake-over-chain.md)).
- If a class has no interface and you do not own it, wrap it in an adapter you do own. That adapter is the only place the vendor's API appears.
- Contract tests are the counterweight: run one shared test suite against both the real adapter and the fake so they cannot drift.

## Why

- **Upstream changes surface**: A renamed method on your own interface is a compile-time break everywhere, including the adapter.
- **Domain types at the boundary**: Tests read in your language, not the vendor's.
- **Substitutability**: A second provider is a new adapter, not a change to the service.
