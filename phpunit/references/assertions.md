# Assertions

Choosing the assertion that produces a useful failure message, and the comparison semantics behind each one.

## When to Load

- Deciding between `assertSame`, `assertEquals`, and the specific assertions
- A failure message says only "false is not true"
- Asserting on floats, collections, JSON, exceptions, or object graphs
- Writing a custom assertion

## Rule Index

- [`assert-same-over-equals`](../rules/assert-same-over-equals.md) — `===` unless loose comparison is intended
- [`assert-specific-over-generic`](../rules/assert-specific-over-generic.md) — The most specific assertion available
- [`assert-exception-scope`](../rules/assert-exception-scope.md) — Arm the expectation immediately before the throwing call
- [`assert-no-conditional-logic`](../rules/assert-no-conditional-logic.md) — No branching in test bodies

## Comparison Semantics

| Assertion | Comparison | Notes |
|---|---|---|
| `assertSame` | `===` | Scalars: type + value. Objects: identity |
| `assertEquals` | Comparator chain | Coerces scalars; objects compared attribute by attribute |
| `assertEqualsCanonicalizing` | `==` after sorting | Arrays where order is irrelevant |
| `assertEqualsIgnoringCase` | `==` case-insensitive | Strings only |
| `assertEqualsWithDelta` | `abs(a-b) <= delta` | The only correct float comparison |
| `assertObjectEquals` | Calls the object's own `equals()` | Value objects that define equality themselves |

The `assertEquals` object comparison is recursive and ignores identity, which is what makes it right for value objects and wrong for asserting "this is the exact instance I registered".

## Selection Table

| Verifying | Assertion |
|---|---|
| Scalar equality | `assertSame($expected, $actual)` |
| Float equality | `assertEqualsWithDelta($e, $a, 0.0001)` |
| Value-object equality | `assertEquals($expected, $actual)` or `assertObjectEquals` |
| Same instance | `assertSame($instance, $actual)` |
| Type | `assertInstanceOf(Foo::class, $actual)` |
| Null / not null | `assertNull` / `assertNotNull` |
| Booleans | `assertTrue` / `assertFalse` (never `assertSame(true, …)`) |
| Collection size | `assertCount($n, $collection)` |
| Emptiness | `assertSame([], $items)` — clearer than `assertEmpty` |
| Membership | `assertContains($needle, $haystack)` |
| Element types | `assertContainsOnlyInstancesOf(Item::class, $items)` |
| Key present | `assertArrayHasKey('id', $row)` |
| Array equality ignoring order | `assertEqualsCanonicalizing($e, $a)` |
| Substring | `assertStringContainsString($needle, $haystack)` |
| Prefix / suffix | `assertStringStartsWith` / `assertStringEndsWith` |
| Pattern | `assertMatchesRegularExpression($pattern, $string)` |
| JSON equality | `assertJsonStringEqualsJsonString($e, $a)` |
| File contents | `assertStringEqualsFile($path, $string)` |
| Exception | `expectException` + `expectExceptionMessage` |

## Type, File, and Directory Assertions

```php
// Types — prefer these over assertTrue(is_array($x))
assertIsArray  · assertIsBool   · assertIsFloat  · assertIsInt
assertIsString · assertIsObject · assertIsNumeric · assertIsCallable
assertIsIterable · assertInstanceOf(Foo::class, $x) · assertNull

// Filesystem
assertFileExists($path)          · assertFileDoesNotExist($path)
assertDirectoryExists($path)     · assertIsReadable($path) · assertIsWritable($path)
assertFileEquals($expected, $actual)
assertStringEqualsFile($path, $string)

// Exceptions
$this->expectException(Foo::class)
$this->expectExceptionMessage('substring')
$this->expectExceptionMessageMatches('/regex/')
$this->expectExceptionCode(123)
```

In a codebase with `declare(strict_types=1)` and full type declarations, the type assertions are mostly redundant — the signature already guarantees the type. They earn their place at boundaries: decoded JSON, database rows, and anything typed `mixed` or `array`.

## Floats

```php
// ❌ 0.1 + 0.2 !== 0.3 in IEEE-754
$this->assertSame(0.3, $a + $b);

// ✅
$this->assertEqualsWithDelta(0.3, $a + $b, 0.0001);
```

The better fix is upstream: represent money as integer minor units (`1_050` for €10.50) and the comparison becomes exact. Floats for currency produce rounding discrepancies that no test tolerance can hide indefinitely.

## Collections

```php
// Order matters
$this->assertSame(['a', 'b', 'c'], $result);

// Order does not matter — do not downgrade to assertEquals
$this->assertEqualsCanonicalizing(['c', 'a', 'b'], $result);

// Asserting on a projection reads better than looping
$this->assertSame(['SKU-1', 'SKU-2'], array_map(fn(Item $i) => $i->sku(), $order->items()));
```

`assertSame` on arrays checks key types too: `[0 => 'a']` is not identical to `['0' => 'a']`. That strictness is usually what you want after `array_filter`, which preserves keys and produces gaps.

## Exceptions

```php
// Arrange first, then arm, then act — nothing after the act call
$order = $this->anOrder();

$this->expectException(InvalidArgumentException::class);
$this->expectExceptionMessage('Quantity must be positive');

$order->add($this->aProduct(), -1);
```

To assert on state after the throw, catch explicitly and fail if nothing was thrown:

```php
try {
    $order->add($this->aProduct(), -1);
    $this->fail('Expected InvalidArgumentException');
} catch (InvalidArgumentException $e) {
    $this->assertSame(ErrorCode::InvalidQuantity, $e->code);
}

$this->assertCount(0, $order->items());
```

Prefer asserting on an error **code** over the message. Messages are user-facing copy and get reworded; codes are contract.

## Custom Assertions

When the same multi-line check appears across many tests, extract it — and delegate to the specific built-ins so the failure message stays useful:

```php
trait AssertsMoney
{
    private function assertMoneyEquals(int $expectedMinor, Currency $currency, Money $actual): void
    {
        $this->assertSame($expectedMinor, $actual->minorUnits(), 'amount mismatch');
        $this->assertSame($currency, $actual->currency(), 'currency mismatch');
    }
}
```

The optional third argument to most assertions is a message **prefix** — it is added to PHPUnit's own message, not a replacement for it, so use it to add context rather than to restate the comparison.

## Assertions That Are Usually a Mistake

- `assertTrue($a === $b)` — discards both values from the message
- `assertEquals()` on scalars — passes on type changes
- `assertEmpty()` when you mean "empty array" — also true for `0`, `'0'`, `''`, `false`, `null`
- `assertNotEmpty()` as a stand-in for a real expectation — it passes for almost anything
- Snapshot assertions as the only check — they record current behaviour including its bugs
- No assertion at all — marked risky under a strict configuration; state the intent with `expectNotToPerformAssertions()` if that is genuinely the claim

## Sources

- [PHPUnit — Assertions](https://docs.phpunit.de/en/12.0/assertions.html)
- [PHPUnit — Testing exceptions](https://docs.phpunit.de/en/12.0/writing-tests-for-phpunit.html#testing-exceptions)
- [PHP Manual — Comparison operators](https://www.php.net/manual/en/language.operators.comparison.php)
- [PHP Manual — Floating point precision](https://www.php.net/manual/en/language.types.float.php)
