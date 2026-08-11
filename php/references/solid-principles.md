# SOLID Principles in PHP

The five principles as they apply to PHP's type system, with the failure mode each one prevents.

## When to Load

- Designing a new class or deciding whether to split an existing one
- A class has grown past a few hundred lines or gained a second reason to change
- Adding a new case to something that already required editing a `match`/`switch`
- Reviewing an inheritance hierarchy or an interface with many methods

## Rule Categories by Priority

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | Single Responsibility | HIGH | `solid-` |
| 2 | Dependency Inversion | HIGH | `solid-` |
| 3 | Open/Closed, Liskov, Interface Segregation | HIGH | `solid-` |

## Rule Index

- [`solid-srp`](../rules/solid-srp.md) — One reason to change per class
- [`solid-ocp`](../rules/solid-ocp.md) — Extend without editing existing code
- [`solid-lsp`](../rules/solid-lsp.md) — Subtypes must be usable through the parent's contract
- [`solid-isp`](../rules/solid-isp.md) — Narrow interfaces over one wide one
- [`solid-dip`](../rules/solid-dip.md) — Depend on abstractions, inject them

## Key Principles

### SRP — "reason to change" means a stakeholder, not a topic

A class has a single responsibility when only one kind of request would force it to change.

```php
// ❌ three reasons to change: report layout, tax law, storage engine
final class Invoice
{
    public function calculateTax(): Money { … }      // finance changes
    public function renderHtml(): string { … }       // design changes
    public function save(): void { … }               // infrastructure changes
}
```

Splitting into `TaxCalculator`, `InvoiceRenderer`, and `InvoiceRepository` means a tax-rate change touches one file and cannot break rendering. The signal to look for is not line count — it is a class that appears in commits for unrelated reasons.

Counter-signal: splitting a class into three that are always changed together produces the same coupling with extra indirection. SRP is about change frequency, not about aesthetic separation.

### OCP — the enum + `match` tension

The classic OCP violation in PHP:

```php
// ❌ every new payment method edits this method
public function fee(PaymentMethod $method): Money
{
    return match ($method) {
        PaymentMethod::Card   => …,
        PaymentMethod::Sepa   => …,
        PaymentMethod::Wallet => …,
    };
}
```

Two legitimate resolutions:

1. **Strategy objects** — one class per method implementing a `FeeStrategy` interface, resolved from a map or a tagged DI service. New method = new class, no edit.
2. **Behavior on the enum** — a method on the enum itself ([`modern-enums-methods`](../rules/modern-enums-methods.md)). New case = new arm, but the compiler and `\UnhandledMatchError` guarantee you cannot forget one.

Choose (2) when the set is genuinely closed and small (order status, currency). Choose (1) when third parties or plugins must add cases without touching your code. Applying (1) to a three-case enum is over-engineering.

### LSP — PHP enforces the signature, not the contract

PHP's variance rules catch signature violations at compile time. They do not catch behavioral ones:

```php
final class ReadOnlyCollection extends Collection
{
    public function add(Item $item): void
    {
        throw new LogicException('immutable');   // ❌ signature is fine, contract is broken
    }
}
```

Any code written against `Collection` now breaks when handed this subtype. The fix is compositional: `ReadOnlyCollection` should not extend `Collection`; both should implement a narrower `Countable`/`IteratorAggregate` surface, and only the mutable one should implement an `AddsItems` interface.

Practical LSP checks: a subtype must not strengthen preconditions (reject inputs the parent accepted), weaken postconditions (return less than promised), or throw exception types the parent's contract does not mention.

### ISP — measured by what implementers are forced to stub

```php
// ❌ every implementer must supply all six, and most throw on half
interface Repository
{
    public function find(int $id): ?Model;
    public function findAll(): array;
    public function save(Model $m): void;
    public function delete(int $id): void;
    public function truncate(): void;
    public function restore(int $id): void;
}
```

The tell is a class implementing the interface with `throw new BadMethodCallException()` bodies. Split into `Finder`, `Writer`, `SoftDeletes` and let a class implement the ones it actually supports. Intersection types then express the requirement precisely at the consumption point:

```php
public function __construct(private readonly Finder&Writer $repository) {}
```

### DIP — inject the abstraction, and let the container own construction

```php
// ❌ high-level policy depends on a concrete infrastructure detail
final class OrderService
{
    private MySqlOrderRepository $repository;
    public function __construct() { $this->repository = new MySqlOrderRepository(); }
}

// ✅ depends on an interface it declares itself
final class OrderService
{
    public function __construct(private readonly OrderRepository $repository) {}
}
```

The ownership detail matters: `OrderRepository` should be defined by the **domain layer that consumes it**, not by the infrastructure layer that implements it. That is what makes the dependency arrow point inward and lets infrastructure be replaced without touching domain code.

DIP is also what makes tests fast — a fake `OrderRepository` needs no database. If a class cannot be unit-tested without infrastructure, that is a DIP violation reporting itself.

## Applying SOLID Without Over-Engineering

| Symptom | Likely principle | Fix |
|---|---|---|
| Class changes for unrelated reasons | SRP | Split by stakeholder |
| Adding a case means editing a `match` in several files | OCP | Strategy or enum method |
| `instanceof` checks before calling a method | LSP | Wrong hierarchy — use composition |
| Implementers throwing on half the interface | ISP | Split the interface |
| Cannot unit test without a DB/HTTP call | DIP | Inject an interface |

SOLID describes forces, not a checklist to apply pre-emptively. Five classes and three interfaces for behavior with one implementation and no known second case is a YAGNI violation — see the `code-standards` skill for the counterweight.

## Sources

- [Robert C. Martin — The Principles of OOD](http://butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod)
- [Martin Fowler — Inversion of Control Containers and the Dependency Injection pattern](https://martinfowler.com/articles/injection.html)
- [Martin Fowler — Refactoring catalog](https://refactoring.com/catalog/)
- [PHP Manual — Object interfaces](https://www.php.net/manual/en/language.oop5.interfaces.php)
- [PHP Manual — Covariance and contravariance](https://www.php.net/manual/en/language.oop5.variance.php)
