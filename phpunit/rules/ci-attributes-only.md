---
title: Use Attributes for All Metadata
impact: CRITICAL
impactDescription: PHPUnit 12 removed doc-comment annotations; a leftover @dataProvider or @test is ignored silently, not reported as an error
tags: phpunit, attributes, annotations, phpunit12, migration
---

## Use Attributes for All Metadata

**Impact: CRITICAL — Annotations are no longer read, and a test whose metadata is ignored either stops running or runs with the wrong arguments**

Attributes were introduced in PHPUnit 10, annotations deprecated in 11, and removed in 12. Metadata in doc-comments is now inert text.

## Bad Example

```php
/**
 * @test
 * @dataProvider quantityProvider
 * @covers \App\Pricing\PricingService
 * @group slow
 */
public function it_prices_an_order(int $quantity, int $expected): void { … }
```

Under PHPUnit 12 every line here is a comment. The method does not start with `test`, so without `#[Test]` it is not collected at all — the test silently disappears from the run and coverage drops with no failure to explain it. If the method *were* named `test_…`, it would run once with no arguments and error on the missing parameters.

## Good Example

```php
use PHPUnit\Framework\Attributes\CoversClass;
use PHPUnit\Framework\Attributes\DataProvider;
use PHPUnit\Framework\Attributes\Group;
use PHPUnit\Framework\Attributes\Test;

#[CoversClass(PricingService::class)]
final class PricingServiceTest extends TestCase
{
    #[Test]
    #[DataProvider('quantityProvider')]
    #[Group('pricing')]
    public function it_prices_an_order(int $quantity, int $expected): void { … }
}
```

Attributes are parsed by the engine: a typo in the class name is a resolution error, and an IDE can navigate and refactor them.

## Migration Map

| Annotation | Attribute |
|---|---|
| `@test` | `#[Test]` |
| `@dataProvider m` | `#[DataProvider('m')]` |
| — | `#[DataProviderExternal(Other::class, 'm')]` |
| `@covers \A\B` | `#[CoversClass(B::class)]`, `#[CoversMethod(B::class, 'm')]`, `#[CoversFunction('f')]` |
| `@uses \A\B` | `#[UsesClass(B::class)]` |
| `@group x` | `#[Group('x')]` |
| `@depends m` | `#[Depends('m')]` |
| `@testWith` | `#[TestWith([1, 2])]` |
| `@requires PHP 8.3` | `#[RequiresPhp('>=8.3')]` |
| `@requires extension redis` | `#[RequiresPhpExtension('redis')]` |
| `@doesNotPerformAssertions` | `#[DoesNotPerformAssertions]` |
| `@backupGlobals` | `#[BackupGlobals(true)]` |
| `@runInSeparateProcess` | `#[RunInSeparateProcess]` |
| `@small` / `@medium` / `@large` | `#[Small]` / `#[Medium]` / `#[Large]` |
| `@ticket` / `@testdox` | `#[Ticket('…')]` / `#[TestDox('…')]` |

## Notes

- Attributes are imported like classes: `use PHPUnit\Framework\Attributes\DataProvider;`. Forgetting the import is a fatal error, not a silent skip — which is itself an improvement over annotations.
- Class-level attributes apply to every method in the class; method-level ones apply to that method. `#[CoversClass]` is normally class-level.
- Rector's `PHPUnit` set converts an existing suite mechanically:
  ```bash
  vendor/bin/rector process tests --config rector-phpunit.php
  ```
- After migrating, grep for leftovers so nothing is silently inert:
  ```bash
  grep -rnE '@(test|dataProvider|covers|uses|group|depends|requires)\b' tests/
  ```
- PHPUnit 12 requires PHP 8.3 or later. Check the platform floor before upgrading the runner.
- `#[CoversClass]` combined with `requireCoverageMetadata="true"` makes untargeted coverage an error rather than a quiet inflation of the coverage number ([`ci-strict-config`](ci-strict-config.md)).

## Why

- **Silent disappearance is the worst failure mode**: An ignored `@test` removes a test without turning CI red.
- **Verified by the engine**: Class references in attributes are resolved; strings in doc-comments are not.
- **Tooling**: IDEs, static analysers, and refactoring tools understand attributes and can rename through them.
