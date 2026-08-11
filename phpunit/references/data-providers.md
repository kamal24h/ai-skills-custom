# Data Providers

Turning one test into many, and the PHPUnit 10+ rules that govern how providers run.

## When to Load

- The same test body repeats with different inputs
- Covering boundary values or a validation matrix
- Migrating `@dataProvider` annotations to attributes
- A provider fails with "must be static" or silently supplies no arguments

## Rule Index

- [`data-provider-static`](../rules/data-provider-static.md) — Static, scalar, no fixtures or I/O
- [`data-provider-named-sets`](../rules/data-provider-named-sets.md) — String keys become test names

## Lifecycle

Providers are resolved **during test collection**, before any test object exists:

```
1. PHPUnit discovers test classes
2. For each #[DataProvider], calls the static provider method   ← setUp() has NOT run
3. Builds one test per data set
4. For each test: new test-case instance → setUp() → test method → tearDown()
```

This is the whole reason for the constraints. At step 2 there is no `$this`, no fixture, and no container — and anything slow there slows `--list-tests`, IDE discovery, and filtering.

## Basic Form

```php
use PHPUnit\Framework\Attributes\DataProvider;

/** @return array<string, array{int, int}> */
public static function quantityProvider(): array
{
    return [
        'single unit'       => [1,  1_000],
        'below bulk cutoff' => [9,  9_000],
        'at bulk cutoff'    => [10, 10_000],
        'above bulk cutoff' => [11, 9_900],
    ];
}

#[DataProvider('quantityProvider')]
public function test_it_prices_an_order_by_quantity(int $quantity, int $expectedTotal): void
{
    $this->assertSame($expectedTotal, $this->service->total($this->anOrder($quantity)));
}
```

Each tuple element maps positionally to a test-method parameter. The array key names the data set in the output.

## Variants

```php
// Generator — constant memory for large sets
public static function rowProvider(): \Generator
{
    foreach (range(1, 1_000) as $i) {
        yield "row {$i}" => [$i, $i * 100];
    }
}

// Shared across test classes
#[DataProviderExternal(ValidationData::class, 'emails')]
public function test_it_validates_email(string $input, bool $valid): void { … }

// Inline, for two or three cases where a method is overkill
#[TestWith(['a@b.co', true])]
#[TestWith(['a@b', false])]
public function test_it_validates_email(string $input, bool $valid): void { … }

// Multiple providers on one test — the sets are concatenated
#[DataProvider('validEmails')]
#[DataProvider('validAliases')]
public function test_it_accepts_the_address(string $input): void { … }
```

## Static Analysis of Provider Shapes

Annotate the return type so PHPStan and Psalm can verify the tuples match the method signature:

```php
/** @return iterable<string, array{0: string, 1: bool}> */
```

Without it, a provider yielding three values into a two-parameter test only fails at runtime — and only for the affected data sets. PHPStan's `phpstan-phpunit` extension checks this specifically.

## What Belongs in a Provider

**Yes**: scalars, enums, arrays of scalars, `DateTimeImmutable` constructed from a fixed string.

**No**:
- Objects built from the container or a factory — they are constructed once and shared across data sets
- Database queries or file reads — collection time becomes infrastructure-dependent
- Randomised values — a failure that cannot be reproduced is not a test
- Values computed with the same formula as the code under test — the test then agrees with any bug

```php
// ❌ objects shared across every data set; created before setUp()
return [[new Order(quantity: 5), 5_000]];

// ✅ scalars in, objects built inside the test
return ['five units' => [5, 5_000]];
```

## When Not to Use One

A data provider is the right tool when the **test body is identical** and only inputs differ. It is the wrong tool when:

- Each case needs different arrange steps → separate test methods
- The expected value must be computed from the input → the computation duplicates the implementation
- Cases need different assertions → that is more than one behaviour
- There are two cases → two named test methods usually read better and name themselves

## Boundary Coverage

Providers make boundary testing cheap, which is where most defects are:

```php
public static function bulkDiscountProvider(): array
{
    return [
        'one below threshold' => [9,  9_000],
        'exactly at threshold'=> [10, 10_000],
        'one above threshold' => [11, 9_900],
        'zero quantity'       => [0,  0],
        'maximum order size'  => [999, 899_100],
    ];
}
```

Off-by-one errors at the threshold are the failure this catches, and it is invisible to a test that only checks quantity 5 and quantity 50.

## Migration from Annotations

```php
/** @dataProvider quantityProvider */   →   #[DataProvider('quantityProvider')]
/** @testWith [1, 2] */                 →   #[TestWith([1, 2])]
```

PHPUnit 12 does not read the annotation form. A leftover `@dataProvider` means the test runs once with no arguments and errors on missing parameters — or, if the method is not `test`-prefixed and has no `#[Test]`, it disappears from the suite entirely. Grep after migrating:

```bash
grep -rn '@dataProvider\|@testWith' tests/
```

## Sources

- [PHPUnit — Data providers](https://docs.phpunit.de/en/12.0/writing-tests-for-phpunit.html#data-providers)
- [PHPUnit — Attributes](https://docs.phpunit.de/en/12.0/attributes.html)
- [phpstan-phpunit extension](https://github.com/phpstan/phpstan-phpunit)
