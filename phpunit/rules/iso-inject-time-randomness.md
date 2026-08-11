---
title: Inject Time and Randomness
impact: CRITICAL
impactDescription: Tests reading the system clock fail at midnight, on the last day of a month, and across DST — always on someone else's branch
tags: phpunit, isolation, clock, randomness, flaky, determinism
---

## Inject Time and Randomness

**Impact: CRITICAL — `new DateTimeImmutable()` and `random_int()` inside production code make deterministic tests impossible**

Time and randomness are dependencies. Code that reaches for them directly cannot be verified, only observed.

## Bad Example

```php
final class SubscriptionService
{
    public function renew(Subscription $s): Subscription
    {
        $now = new DateTimeImmutable();                     // ❌ hidden dependency on the clock
        return $s->withExpiry($now->modify('+1 month'))
                 ->withReference(bin2hex(random_bytes(8))); // ❌ hidden dependency on randomness
    }
}
```

```php
public function test_it_extends_the_subscription_by_a_month(): void
{
    $renewed = $this->service->renew($this->aSubscription());

    // Reimplements the production logic; cannot assert on the reference at all
    $this->assertSame(
        (new DateTimeImmutable())->modify('+1 month')->format('Y-m-d'),
        $renewed->expiresAt()->format('Y-m-d'),
    );
}
```

Run this on 31 January and `+1 month` lands on 3 March — the test and the code agree on the same surprising behaviour, so the bug is invisible. Run it at 23:59:59.9 and the two `new DateTimeImmutable()` calls straddle midnight.

## Good Example

```php
interface Clock { public function now(): DateTimeImmutable; }

final class SystemClock implements Clock
{
    public function now(): DateTimeImmutable { return new DateTimeImmutable(); }
}

final class FrozenClock implements Clock
{
    public function __construct(private DateTimeImmutable $now) {}
    public function now(): DateTimeImmutable { return $this->now; }
    public function advance(string $interval): void { $this->now = $this->now->modify($interval); }
}
```

```php
final class SubscriptionService
{
    public function __construct(
        private readonly Clock $clock,
        private readonly ReferenceGenerator $references,
    ) {}

    public function renew(Subscription $s): Subscription
    {
        return $s->withExpiry($this->clock->now()->modify('+1 month'))
                 ->withReference($this->references->next());
    }
}
```

```php
public function test_it_extends_a_january_subscription_to_the_end_of_february(): void
{
    $clock = new FrozenClock(new DateTimeImmutable('2025-01-31 12:00:00'));
    $service = new SubscriptionService($clock, new FixedReferenceGenerator('ref_1'));

    $renewed = $service->renew($this->aSubscription());

    $this->assertSame('2025-02-28', $renewed->expiresAt()->format('Y-m-d'));  // the rule, stated
    $this->assertSame('ref_1', $renewed->reference());
}
```

The month-end rule is now an explicit, hard-coded expectation — and the test asserts the same thing every day of the year.

## Notes

- PSR-20 defines `Psr\Clock\ClockInterface` with a single `now(): DateTimeImmutable`. Use it rather than inventing an interface, so libraries interoperate.
- `Symfony\Component\Clock\MockClock` and `lcobucci/clock` provide ready-made test clocks; `slope-it/clock-mock` and the `uopz`/`ClockMock` approaches patch the global clock instead — workable for legacy code, but they leave the hidden dependency in place.
- The same applies to: `uniqid()`, `random_int()`, `shuffle()`, `array_rand()`, `session_id()`, `php_uname()`, `getenv()`, and anything reading the filesystem's current state.
- Always use `DateTimeImmutable`. `DateTime::modify()` mutates in place, so passing one to a collaborator that modifies it changes the caller's value.
- Store and compare timestamps in UTC; convert only at the presentation edge. Most "flaky at 02:00" failures are DST transitions in a local timezone.
- Test the boundaries explicitly: month ends, leap days, DST changes, and year rollovers. Those are the cases a frozen clock makes cheap to write.

## Why

- **Deterministic**: The same input produces the same result on every machine and at every hour.
- **Boundary coverage**: Leap days and month-end arithmetic become ordinary tests instead of production incidents.
- **Honest signatures**: A constructor that takes a `Clock` tells the reader this class depends on time.
