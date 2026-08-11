# PHP Type System

Strict typing, declaration coverage, and the variance rules that make static analysis useful.

## When to Load

- Adding or reviewing type declarations on parameters, returns, or properties
- Deciding between a union, an intersection, a nullable type, or `mixed`
- Introducing `declare(strict_types=1)` into an existing codebase
- Raising a PHPStan/Psalm level and dealing with the resulting errors

## Rule Categories by Priority

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | Strict mode & declaration coverage | CRITICAL | `type-` |
| 2 | Composite types (union, intersection, nullable) | HIGH | `type-` |
| 3 | Bottom and escape types (`void`, `never`, `mixed`) | HIGH | `type-` |

## Rule Index

- [`type-strict-mode`](../rules/type-strict-mode.md) — `declare(strict_types=1)` in every file
- [`type-parameter-types`](../rules/type-parameter-types.md) — Declare a type on every parameter
- [`type-return-types`](../rules/type-return-types.md) — Declare a return type on every function and method
- [`type-property-types`](../rules/type-property-types.md) — Type every property; prefer non-nullable + constructor init
- [`type-union-types`](../rules/type-union-types.md) — `A|B` when a value genuinely has two shapes
- [`type-intersection-types`](../rules/type-intersection-types.md) — `A&B` to require several interfaces at once
- [`type-nullable-types`](../rules/type-nullable-types.md) — `?T` deliberately, not as a default
- [`type-void-never`](../rules/type-void-never.md) — `void` returns nothing; `never` never returns
- [`type-mixed-avoid`](../rules/type-mixed-avoid.md) — `mixed` is an unresolved design decision

## Key Principles

### Coercive vs strict mode

Without `declare(strict_types=1)`, PHP coerces scalars at the call boundary:

```php
function withDiscount(int $priceInCents): int { … }

withDiscount("100");   // coercive mode: becomes int(100)
withDiscount(9.99);    // coercive mode: becomes int(9) — silent data loss
```

With strict types both calls throw `TypeError`. The second case is the reason this matters: coercion turns a bug into a rounded number that flows into an invoice.

Strict mode is **per-file and applies to calls made from that file**, not to the file being called. Adding it incrementally is safe: each converted file tightens its own outgoing calls.

### Declaration coverage is what static analysis runs on

PHPStan and Psalm infer from declarations. An untyped parameter is an implicit `mixed`, and every operation on it becomes unverifiable:

```php
// no declaration → analyzer knows nothing
function total($items) { return array_sum($items); }

// declared → analyzer verifies callers and the sum's type
/** @param list<int> $items */
function total(array $items): int { return array_sum($items); }
```

Array shapes are still invisible to the engine — PHP has no generics. Docblock generics (`list<int>`, `array<string, User>`) are the supported way to close that gap, and both major analyzers read them.

### Choosing between composite types

| Situation | Type | Note |
|---|---|---|
| Value is legitimately one of several shapes | `int\|string` | Every consumer must branch — keep the arity small |
| Parameter needs several capabilities | `Countable&Traversable` | Prefer one purpose-built interface if you own both |
| Absence is a meaningful state | `?User` | Callers must handle null; make that explicit in the name |
| Absence means "not loaded yet" | uninitialised typed property | Accessing it throws instead of returning a misleading null |
| You do not know yet | `mixed` | Not a type — a deferred decision. Resolve it. |

`?T` and `T|null` are identical to the engine. `?T` is conventional for a single type; `T|U|null` is required once there are two or more.

### `never` is not `void`

```php
function fail(string $message): never { throw new RuntimeException($message); }
```

`never` tells the analyzer that control does not continue past the call, which removes false "possibly undefined" and "missing return" reports at call sites. `void` means the function returns normally with no value. Marking a throwing helper `void` loses that information.

### Typed properties and uninitialised state

```php
final class Invoice
{
    private DateTimeImmutable $issuedAt;   // no default, not nullable
}
```

Reading `$issuedAt` before assignment throws `Error: Typed property must not be accessed before initialization`. This is preferable to `?DateTimeImmutable $issuedAt = null`, which pushes a null check into every consumer forever to model a state that only exists during construction. Prefer constructor promotion and make the object valid from birth.

### Variance

PHP supports covariant returns and contravariant parameters:

```php
class Repository { public function find(int $id): ?Model { … } }
class UserRepository extends Repository {
    public function find(int $id): ?User { … }     // ✅ narrower return — allowed
}
```

Widening a parameter type in a child is allowed; narrowing it is not. This is what makes Liskov substitution enforceable by the engine rather than by review — see [`solid-lsp`](../rules/solid-lsp.md).

## Migration Order for Legacy Code

1. Add return types (lowest risk — no caller behavior changes)
2. Add parameter types file by file, running tests between files
3. Add `declare(strict_types=1)` per file, starting with leaf files that call nothing
4. Add property types last (they surface uninitialised-state bugs, which take longest to fix)
5. Raise the analyzer level one step at a time; never jump to max on a legacy codebase

## Sources

- [PHP Manual — Type declarations](https://www.php.net/manual/en/language.types.declarations.php)
- [PHP Manual — Union types](https://www.php.net/manual/en/language.types.type-system.php)
- [PHP Manual — Typed properties](https://www.php.net/manual/en/language.oop5.properties.php)
- [PHPStan — Rule levels](https://phpstan.org/user-guide/rule-levels)
- [Psalm — Typing in Psalm](https://psalm.dev/docs/annotating_code/typing_in_psalm/)
