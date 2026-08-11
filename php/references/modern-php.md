# Modern PHP Features (8.0 – 8.5)

Version-gated language features, what each one replaces, and when the older form is still correct.

## When to Load

- Before suggesting any 8.x-only syntax — check the project's minimum version first
- Refactoring boilerplate constructors, getters, or `switch` chains
- Replacing class constants or magic strings with enums
- Deciding whether a value object should be `readonly`

## Version Gate

Read `composer.json` before recommending anything:

```json
{ "require": { "php": "^8.3" } }
```

`^8.3` means 8.3 is the floor — 8.4 features will fail on a developer running 8.3. Match the floor, not the newest release. Check `platform.php` in the `config` block too; it overrides the runtime for dependency resolution.

## Rule Index

### PHP 8.0
- [`modern-constructor-promotion`](../rules/modern-constructor-promotion.md) — Declare and assign in the signature
- [`modern-match-expression`](../rules/modern-match-expression.md) — Strict, exhaustive, expression-valued branching
- [`modern-named-arguments`](../rules/modern-named-arguments.md) — Name the arguments that are not self-evident
- [`modern-nullsafe-operator`](../rules/modern-nullsafe-operator.md) — `?->` instead of nested null checks
- [`modern-attributes`](../rules/modern-attributes.md) — Structured metadata instead of docblock parsing

### PHP 8.1
- [`modern-enums`](../rules/modern-enums.md) — Closed sets of values as a type
- [`modern-enums-methods`](../rules/modern-enums-methods.md) — Behavior belongs on the enum, not in a `match` at every call site
- [`modern-readonly-properties`](../rules/modern-readonly-properties.md) — Write-once properties
- [`modern-first-class-callables`](../rules/modern-first-class-callables.md) — `$fn = $obj->method(...)`
- [`modern-arrow-functions`](../rules/modern-arrow-functions.md) — `fn() =>` with implicit capture

### PHP 8.2
- [`modern-readonly-classes`](../rules/modern-readonly-classes.md) — Every property readonly, declared once

### PHP 8.3
- [`modern-typed-constants`](../rules/modern-typed-constants.md) — Types on class constants
- [`modern-override-attribute`](../rules/modern-override-attribute.md) — `#[\Override]` catches renamed parents

### PHP 8.4
- [`modern-property-hooks`](../rules/modern-property-hooks.md) — Computed/validated properties without getter boilerplate
- [`modern-asymmetric-visibility`](../rules/modern-asymmetric-visibility.md) — `public private(set)` — read anywhere, write inside

### PHP 8.5
- [`modern-pipe-operator`](../rules/modern-pipe-operator.md) — `|>` for left-to-right transformation chains

## Key Principles

### `match` is not a `switch` replacement in every case

```php
$label = match ($status) {
    Status::Draft, Status::Pending => 'In progress',
    Status::Published              => 'Live',
};
```

`match` compares with `===`, returns a value, does not fall through, and throws `\UnhandledMatchError` on an unmatched subject. That last property is a feature: an unhandled enum case fails loudly instead of silently skipping.

Keep `switch` when you deliberately want fall-through across several cases executing shared statements, or when the arms are long statement blocks rather than expressions.

### Enums replace three older patterns

| Old pattern | Problem | Enum equivalent |
|---|---|---|
| Class constants (`const DRAFT = 'draft'`) | Any string passes the type check | `enum Status: string` |
| Magic strings | Typos are runtime bugs | Backed enum + `from()`/`tryFrom()` |
| Static factory + validation | Validation must be called everywhere | Invalid values cannot be constructed |

`from()` throws on an unknown value; `tryFrom()` returns null. Use `from()` at trusted boundaries (your own database) and `tryFrom()` on user input.

Pure enums have no scalar value and cannot be persisted directly. Use a backed enum for anything that crosses a storage or API boundary.

### `readonly` semantics people get wrong

```php
final class Money
{
    public function __construct(
        public readonly int $amount,
        public readonly Currency $currency,
    ) {}
}
```

- Readonly is **shallow**: a readonly property holding an object still permits mutating that object's own properties.
- Readonly properties can only be initialised from **inside the declaring class scope** — a parent cannot initialise a child's readonly property.
- Cloning: before PHP 8.3 a readonly property could not be modified in `__clone()`, which made `withX()` wither-methods awkward. Since 8.3, reinitialising readonly properties inside `__clone()` is allowed.
- `readonly class` (8.2) applies readonly to every property and forbids dynamic properties — the right default for value objects and DTOs.

### `#[\Override]` is cheap insurance

```php
final class JsonLogger extends AbstractLogger
{
    #[\Override]
    public function log(string $message): void { … }
}
```

If the parent method is renamed or removed, this becomes a compile-time error instead of a method that silently stops being called. Add it to every intentional override in a codebase on 8.3+.

### Property hooks change what a "property" means (8.4)

```php
final class Temperature
{
    public float $celsius = 0.0;

    public float $fahrenheit {
        get => $this->celsius * 9 / 5 + 32;
        set => $this->celsius = ($value - 32) * 5 / 9;
    }
}
```

This removes the classic `getX()`/`setX()` pair while keeping the validation point. It also means a public property is no longer a guarantee of direct field access — a hook may run arbitrary code, so treat property reads in hot loops with the same care as method calls.

### Asymmetric visibility vs readonly (8.4)

```php
public private(set) array $items = [];   // read anywhere, write only inside the class
```

Use `readonly` for values fixed at construction. Use `private(set)` for state that changes over the object's lifetime but only through its own methods — a mutable aggregate with a safe public read surface.

### Attributes are metadata, not behavior

Attributes are inert until something reflects over them. They are the right tool when a framework or your own container reads them (routing, validation, DI, ORM mapping). They are the wrong tool for logic that should simply be a method call — reflection is slower and the indirection is invisible in a stack trace.

## Sources

- [PHP Manual — Migrating from 7.4 to 8.0](https://www.php.net/manual/en/migration80.php)
- [PHP Manual — Enumerations](https://www.php.net/manual/en/language.enumerations.php)
- [PHP Manual — Readonly properties](https://www.php.net/manual/en/language.oop5.properties.php)
- [PHP Manual — Property hooks](https://www.php.net/manual/en/language.oop5.property-hooks.php)
- [PHP Manual — Attributes](https://www.php.net/manual/en/language.attributes.php)
- [PHP Manual — Supported versions](https://www.php.net/supported-versions.php)
