---
title: Choose the Most Specific Assertion Available
impact: HIGH
impactDescription: assertTrue() on a computed expression discards the actual value, leaving a failure message that says only "false is not true"
tags: phpunit, assertions, diagnostics, failure-messages
---

## Choose the Most Specific Assertion Available

**Impact: HIGH — The assertion you pick decides whether a failure shows you the data or shows you nothing**

PHPUnit builds its failure message from the assertion's own knowledge of what it compared. Collapsing a comparison into a boolean throws that away before PHPUnit ever sees it.

## Bad Example

```php
$this->assertTrue($order->total() === 3_600);
// Failed asserting that false is true.          ← what was the total?

$this->assertTrue(count($cart->items()) === 3);
// Failed asserting that false is true.          ← how many were there?

$this->assertTrue(in_array('admin', $user->roles(), true));
// Failed asserting that false is true.          ← which roles did they have?

$this->assertTrue(str_contains($body, 'Invoice #42'));
// Failed asserting that false is true.          ← what did the body contain?
```

Every one of these requires adding a `var_dump` and re-running to learn anything.

## Good Example

```php
$this->assertSame(3_600, $order->total());
// Failed asserting that 3400 is identical to 3600.

$this->assertCount(3, $cart->items());
// Failed asserting that actual size 2 matches expected size 3.

$this->assertContains('admin', $user->roles());
// Failed asserting that Array (0 => 'editor', 1 => 'viewer') contains 'admin'.

$this->assertStringContainsString('Invoice #42', $body);
// Failed asserting that '<html>…' contains "Invoice #42".
```

Each failure names the actual value. Most are diagnosable without opening the file.

## Assertion Selection

| Checking | Use |
|---|---|
| Scalar equality | `assertSame` |
| Object is value-equal | `assertEquals` |
| Object identity | `assertSame` |
| Float within tolerance | `assertEqualsWithDelta` |
| Collection size | `assertCount` |
| Membership | `assertContains` / `assertContainsOnly` |
| Array shape ignoring order | `assertEqualsCanonicalizing` |
| Substring | `assertStringContainsString` |
| Prefix/suffix | `assertStringStartsWith` / `assertStringEndsWith` |
| Emptiness | `assertEmpty` (careful: `'0'` is empty) or `assertSame([], …)` |
| Null | `assertNull` |
| Type | `assertInstanceOf` |
| JSON | `assertJsonStringEqualsJsonString` |
| Array key | `assertArrayHasKey` |
| Nothing was thrown | `expectNotToPerformAssertions` is **not** this — see notes |

## Notes

- `assertEmpty()` is true for `0`, `'0'`, `''`, `[]`, `null`, and `false`. When you mean "the list is empty", write `assertSame([], $items)` or `assertCount(0, $items)`.
- `assertContains()` on strings was removed in favour of `assertStringContainsString()` — the split exists because the array and string semantics were genuinely different.
- A test with no assertions is marked risky, not passing, under a strict configuration ([`ci-strict-config`](ci-strict-config.md)). If a test's claim is "this does not throw", assert on the returned value instead, or state the intent with `expectNotToPerformAssertions()`.
- Custom assertions are worth writing when the same three-line check appears in many tests. Put them in a trait and have them delegate to the specific built-ins so failure messages stay useful.

## Why

- **Diagnosis without re-running**: The message contains the actual value, which is usually enough to identify the bug.
- **Intent is explicit**: `assertCount(3, …)` states what is being verified; `assertTrue(count(…) === 3)` states how.
- **Better diffs**: PHPUnit renders structured diffs for arrays and objects only when the assertion knows their types.
