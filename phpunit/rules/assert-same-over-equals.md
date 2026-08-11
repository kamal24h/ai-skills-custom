---
title: Use assertSame() Unless Loose Comparison Is Intended
impact: CRITICAL
impactDescription: assertEquals() passes on type mismatches, so a function returning "0" instead of 0 ships green
tags: phpunit, assertions, type-safety, strict
---

## Use assertSame() Unless Loose Comparison Is Intended

**Impact: CRITICAL — `assertEquals()` compares with type juggling, which is precisely the class of bug a typed codebase is trying to eliminate**

`assertSame()` uses `===`. `assertEquals()` uses a comparator chain that coerces scalars and compares objects by value.

## Bad Example

```php
$this->assertEquals(100, $order->total());        // passes for 100, "100", 100.0, "100.00"
$this->assertEquals(true, $result->isValid());    // passes for true, 1, "1", "yes"
$this->assertEquals([1, 2], $ids);                // passes for ["1", "2"]
```

A repository that starts returning `"100"` from a database driver instead of `100` breaks JSON output and strict comparisons downstream — and this suite stays green.

## Good Example

```php
$this->assertSame(100, $order->total());
$this->assertTrue($result->isValid());            // specific, and cannot pass for 1
$this->assertSame([1, 2], $ids);                  // types and order both checked
```

```php
// Value objects: assertEquals is correct here — compare by value, not identity
$this->assertEquals(new Money(100, Currency::EUR), $order->total());

// …unless identity is the claim
$this->assertSame($expectedInstance, $registry->get('mailer'));
```

## Notes

- `assertSame()` on objects compares **identity**, not value. For value objects use `assertEquals()` deliberately, or better, assert on the primitives: `assertSame(100, $total->amount())`.
- Arrays: `assertSame()` requires identical order and key types. When order genuinely does not matter, sort first or use `assertEqualsCanonicalizing()` — do not downgrade to `assertEquals()`.
- Floats: neither is appropriate. Use `assertEqualsWithDelta($expected, $actual, 0.0001)`, or avoid floats entirely by storing money in minor units as integers.
- `assertNotSame()` follows the same rule for negative assertions.
- Enable `strict_types=1` in test files too — it catches the same class of problem at the call boundary.

## Why

- **Type regressions are silent**: Loose comparison is exactly the mechanism that lets a type change pass through a test suite unnoticed.
- **Better failure messages**: `assertSame` reports `100` vs `'100'` distinctly; a coerced comparison never gets the chance to.
- **Consistency with the language**: A codebase using `declare(strict_types=1)` and typed properties should not verify itself with loose rules.
