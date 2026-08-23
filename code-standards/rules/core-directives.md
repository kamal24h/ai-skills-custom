# Rules for Code Design & Clean Code

Actionable directives for SOLID, Clean Code (KISS, YAGNI, DRY, TDA), function design, and pragmatic simplicity. Language-agnostic — apply alongside the language skill in use.

Cite these ids in reviews (`solid-srp`, `clean-yagni`, `fn-early-returns`) so feedback is traceable back to the source rule.

## 1. SOLID Principles (`solid-`)

### `solid-srp`
- **Context:** Class and module design.
- **Rule:** Give each class one reason to change. The test is behavioural, not visual: would two different stakeholders ever request changes to this class for unrelated reasons?
- **Avoid:** A class that calculates, renders, and persists. Splitting is also wrong when the parts always change together — that is indirection without benefit.

### `solid-ocp`
- **Context:** Adding a new case to existing behaviour.
- **Rule:** Prefer designs where a new case is a new file. Use strategy objects when third parties or plugins must extend; use an exhaustive `switch`/`match` on a closed enum when you own every case and the compiler can enforce completeness.
- **Avoid:** Editing the same conditional in five files for every new type. Equally, avoid a strategy hierarchy for three cases that will never grow.

### `solid-lsp`
- **Context:** Inheritance and interface implementation.
- **Rule:** A subtype must be usable anywhere the supertype is, without the caller knowing. Do not strengthen preconditions, weaken postconditions, or throw exception types the contract does not mention.
- **Avoid:** An override that throws `UnsupportedOperation`. `instanceof`/type checks before calling a method are the symptom — the hierarchy is wrong, use composition.

### `solid-isp`
- **Context:** Interface design.
- **Rule:** Prefer several narrow interfaces to one wide one. Consumers depend only on what they call.
- **Avoid:** An interface whose implementers stub half the methods with "not supported". That stub is the measurement that the interface is too wide.

### `solid-dip`
- **Context:** Dependencies between layers.
- **Rule:** Depend on abstractions, injected through the constructor. The abstraction is defined by the **consuming** layer, not the implementing one, so the dependency arrow points inward.
- **Avoid:** `new ConcreteRepository()` inside a service, static/global access to infrastructure, or a domain interface living in the infrastructure package. If a class cannot be unit-tested without infrastructure, this rule is being broken.

## 2. Clean Code Patterns (`clean-`)

### `clean-kiss`
- **Context:** Choosing an approach.
- **Rule:** Pick the simplest solution that satisfies the current requirement and is honest about it. Simple means fewer moving parts and fewer things a reader must hold in mind — not fewer characters.
- **Avoid:** Clever one-liners, nested ternaries, metaprogramming, and configuration-driven indirection where a straightforward function would do.

### `clean-yagni`
- **Context:** Anticipating future requirements.
- **Rule:** Build what is needed now. Speculative generality costs immediately and pays only if the guess was right.
- **Avoid:** Interfaces with one implementation "for testing" (inject the concrete type or use a real seam), plugin systems with one plugin, config options nobody sets, and abstract base classes with one subclass.

### `clean-dry`
- **Context:** Repeated code.
- **Rule:** Deduplicate repeated **knowledge** — a business rule, a validation, a format that must stay consistent. Two pieces of code that merely look alike are not duplication.
- **Avoid:** Coupling unrelated call sites into a shared helper with a boolean parameter. Premature deduplication is harder to undo than duplication; wait for the third occurrence.

### `clean-tda`
- **Context:** Object interaction (Tell, Don't Ask).
- **Rule:** Tell an object what to do; let it decide how. Keep behaviour with the data it operates on.
- **Avoid:** `if (order.getStatus() == PAID && order.getItems().size() > 0) { order.setStatus(SHIPPED) }` — the rule belongs in `order.ship()`. Chains of getters reaching through several objects (`a.getB().getC().getD()`) are the tell.

## 3. Function Design (`fn-`)

### `fn-small-functions`
- **Context:** Function length.
- **Rule:** A function should do one thing at one level of abstraction. Length is a symptom, not the rule — a 40-line flat switch can be fine, while a 12-line function mixing parsing, validation, and I/O is not.
- **Avoid:** Functions requiring section comments (`// validate`, `// then save`). Each comment names the function you should have extracted.

### `fn-meaningful-names`
- **Context:** Naming.
- **Rule:** Name for intent and domain language. Length should scale with scope: a loop index may be `i`; a class field may not be `d`. Booleans read as predicates (`isExpired`, `hasAccess`); functions with side effects read as verbs.
- **Avoid:** `data`, `info`, `manager`, `helper`, `process()`, `handle()`, encoded types (`strName`), and names that lie after a refactor.

### `fn-single-abstraction-level`
- **Context:** Function body composition.
- **Rule:** Keep all statements in a function at the same conceptual level. High-level orchestration calls named steps; low-level detail lives inside those steps.
- **Avoid:** A function that calls `validateOrder()` and then, three lines later, does raw string manipulation on a postcode.

### `fn-early-returns`
- **Context:** Conditional structure.
- **Rule:** Return early for invalid or trivial cases so the main path stays at the lowest indentation. Aim for at most two levels of nesting.
- **Avoid:** Arrow-shaped code — nested `if` blocks with the real work at the bottom and a chain of closing braces. Invert the condition and return.

## 4. Pragmatic Software Design (`prag-`)

### `prag-guard-clauses`
- **Context:** Preconditions (fail fast).
- **Rule:** Validate inputs and invariants at the top of the function and reject immediately. Fail at the boundary where the bad value entered, not three layers deeper.
- **Avoid:** Letting an invalid value travel until it produces an unrelated error somewhere else. Silent defaulting (`?? 0`) that hides a missing value is the same defect with a delay.

### `prag-no-exceptions-for-flow`
- **Context:** Expected versus exceptional conditions.
- **Rule:** Exceptions signal conditions the caller could not reasonably prevent. Expected outcomes — not found, validation failed, insufficient funds — are return values: an optional, a result type, or a violations list.
- **Avoid:** `try { find() } catch (NotFound) { … }` as the normal path. It is slower, hides real errors in the same `catch`, and makes the happy path unreadable.

### `prag-no-flag-arguments`
- **Context:** Function parameters.
- **Rule:** A boolean parameter that selects between two behaviours means the function does two things. Split it into two named functions.
- **Avoid:** `render(true)` at the call site — unreadable without opening the definition. If the flag must stay (a public API you cannot break), take a named enum instead of a boolean.

### `prag-explaining-variables`
- **Context:** Complex expressions.
- **Rule:** Name intermediate results to explain conditions and calculations. A well-named variable replaces a comment and survives refactoring.
- **Avoid:** Multi-clause boolean conditions inline in an `if`. Extract `isEligibleForDiscount` and the condition documents itself.

### `prag-dop-vs-oop-boundary`
- **Context:** Choosing between data-oriented and object-oriented modelling.
- **Rule:** Use plain data structures (DTOs, records, dictionaries) for transport and transformation pipelines. Use objects with behaviour where invariants must be enforced and cannot be allowed to break.
- **Avoid:** Anaemic classes that are structs with getters and setters (use a record), and equally, "smart" data structures that acquire business logic while crossing a serialization boundary.

## 5. Universal Naming (`name-`)

Language-agnostic naming directives. Per-stack default conventions live in `references/naming-*.md`.

### `name-intent-over-mechanism`
- **Context:** Any identifier that will outlive the current task.
- **Rule:** Name for *why* it exists in domain language, not for how it is implemented. Length scales with scope: loop index may be `i`; a class field may not be `d`.
- **Avoid:** `data`, `info`, `manager`, `helper`, `process()`, `handle()` — names that survive refactors of their own meaning are lies waiting to happen. (Shared rule: [`fn-meaningful-names`](#fn-meaningful-names))

### `name-boolean-predicate`
- **Context:** Booleans, flags, validation functions.
- **Rule:** Booleans read as predicates — `isEnabled`, `hasAccess`, `canEdit`, `isEmpty`. Functions returning booleans read as questions; functions with side effects read as verbs.
- **Avoid:** Boolean names that are nouns (`status: true`) or verbs without auxiliaries (`send: false`).

### `name-prefix-escaping`
- **Context:** Ecosystems where identifiers share one global namespace (WordPress hooks/options/functions, CLI command signatures, environment variables, event names across services).
- **Rule:** Prefix every escaping identifier with the unique project prefix agreed at kickoff (`myplugin_`, `wc_`). The prefix is part of the contract once published.
- **Avoid:** Shipping a hook or option without a prefix because "the project is small" — collisions surface months later as unexplainable bugs.

### `name-no-type-encoding`
- **Context:** Typed languages and modern PHP/Python/TS codebases.
- **Rule:** The type system already documents types; names document intent. Do not encode type or scope in the name (`strName`, `$arrUsers`, `IUserService`, `m_count`).
- **Avoid:** Hungarian notation, `I`-prefixed interfaces (TypeScript's documented anti-recommendation), underscore scope markers in languages with real access modifiers. Framework suffixes (`-Controller`, `-Repository`) are conventions, not type encoding — those stay.
