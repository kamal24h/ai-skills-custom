---
name: code-standards
description: Expert in code design standards including SOLID principles, Clean Code patterns (KISS, YAGNI, DRY, TDA), pragmatic software design, AND per-language default naming conventions (WordPress, Laravel, Symfony, PHP/PSR, Go, Kotlin, Swift/SwiftUI, React, Vue, JS/TS, Python) collected from official style guides. **ALWAYS use when designing ANY classes/modules, implementing features, fixing bugs, refactoring code, writing functions, or choosing names.** Use proactively to ensure proper design, separation of concerns, simplicity, and maintainability. Examples - "create class", "design module", "implement feature", "refactor code", "fix bug", "is this too complex", "apply SOLID", "keep it simple", "avoid over-engineering", "naming convention", "how should I name".
model: inherit
---

# Code Standards & Design Principles

Universal code design and clean code principles for building maintainable, scalable, and simple software. Covers SOLID, KISS, YAGNI, DRY, and TDA patterns — plus the official per-stack naming conventions.

## Specialized Agents

Specialized personas for code design. Load these from `agents/` to provide expert context.

| Agent | Role | Focus |
|-------|------|-------|
| **code-standards-pro** | Design Expert | SOLID, Clean Code, KISS/YAGNI, complexity reduction. |
| **naming-conventions-pro** | Naming Expert | Per-stack naming defaults, prefix/suffix rules, file naming. |

## When to Use

Proactively assist when:
- Designing new classes or modules
- Implementing features without over-abstraction
- Refactoring to remove unnecessary complexity
- Fixing bugs without adding abstractions
- Code reviews focused on simplicity
- User asks "is this too complex?"
- Detecting/preventing over-engineering
- Choosing duplication over coupling

**For per-language naming conventions (files, folders, functions, variables), load the matching `references/naming-*.md` file from the Naming Conventions category below — it collects the official defaults for WordPress, Laravel, Symfony, PHP (PSR), Go, Kotlin, Swift/SwiftUI, React, Vue, JavaScript/TypeScript, and Python.**

## Core Philosophy

1. **"Duplication Over Coupling"** — Prefer duplicating code between contexts over creating shared abstractions.
2. **"Start Ugly, Refactor Later"** — Don't create abstractions until you have 3+ real use cases.
3. **KISS Over DRY** — Simplicity beats premature abstraction every time.
4. **YAGNI Always** — Never add features or abstractions "just in case".

```typescript
// ✅ GOOD: Each entity is independent
export class User { /* Only what User needs */ }
export class Product { /* Only what Product needs */ }
```

## Core Directives

### MUST DO

- Keep functions focused on **one task at one level of abstraction** (length is a symptom, not the target)
- Use meaningful names that explain **WHY**, not **WHAT**
- Apply the **Rule of Three**: only abstract after the 3rd occurrence
- Favor **Composition** over Inheritance
- Implement **Early Returns** to reduce nesting and improve readability
- Practice **Tell, Don't Ask (TDA)**: behavior should live with the data it operates on
- Ensure every class has a **Single Responsibility (SRP)**

### MUST NOT DO

- Create "God Classes" that handle multiple unrelated responsibilities
- Abstract code "just in case" it might be reused later (YAGNI violation)
- Use deep inheritance hierarchies (prefer shallow or flat structures)
- Suppress or ignore linter/compiler warnings without a very strong reason
- Add complex design patterns (e.g., Factory, Strategy) to simple problems
- Hardcode "magic numbers" or strings (use constants or enums)

## Category Index — When to Load Which Reference

| # | Category | Impact | Load when… | Reference | Prefix | Rules |
|--:|----------|:------:|------------|-----------|--------|:-----:|
| 1 | SOLID Principles | CRITICAL | Designing OOP systems, ensuring extensibility and maintainability | [`references/solid-principles.md`](references/solid-principles.md) | `solid-` | 5 |
| 2 | Clean Code Patterns | CRITICAL | Writing daily code, choosing between simplicity and abstraction | [`references/clean-code-principles.md`](references/clean-code-principles.md) | `clean-` | 4 |
| 3 | Function Design | HIGH | Designing methods, organizing logic, reducing complexity | [`references/function-design.md`](references/function-design.md) | `fn-` | 4 |
| 4 | Anti-Patterns | MEDIUM | Identifying common design mistakes and refactoring code | [`references/anti-patterns-and-examples.md`](references/anti-patterns-and-examples.md) | — | — |
| 5 | Pragmatic Software Design | HIGH | Enhancing readability, input safety, early returns, and cognitive simplicity | [`references/pragmatic-software-design.md`](references/pragmatic-software-design.md) | `prag-` | 5 |
| 6 | Universal Naming | HIGH | Naming any identifier; boolean predicates, prefixes, type-encoding smells | (rules only, see Rule Index) | `name-` | 4 |

## Naming Conventions — Per-Stack Defaults

Load exactly the stack(s) in play. When stacks disagree, each layer follows its own documented standard.

| # | Stack | Load when… | Reference | Base standard |
|--:|-------|------------|-----------|---------------|
| N1 | PHP (PSR) | Plain PHP, or as base for Laravel/Symfony | [`references/naming-php.md`](references/naming-php.md) | PSR-1, PSR-12 |
| N2 | WordPress | Plugins, themes, hooks, options, DB tables | [`references/naming-wordpress.md`](references/naming-wordpress.md) | WP Coding Standards |
| N3 | Laravel | Models, tables, controllers, jobs, migrations | [`references/naming-laravel.md`](references/naming-laravel.md) | PHP (PSR) |
| N4 | Symfony | Services, bundles, entities, Twig templates | [`references/naming-symfony.md`](references/naming-symfony.md) | PHP (PSR) |
| N5 | Go | Packages, exports, interfaces, errors | [`references/naming-go.md`](references/naming-go.md) | Effective Go + Go Style Guide |
| N6 | Kotlin | Packages, classes, coroutines, Compose | [`references/naming-kotlin.md`](references/naming-kotlin.md) | Kotlin Coding Conventions |
| N7 | Swift / SwiftUI | Types, protocols, factories, Views | [`references/naming-swift.md`](references/naming-swift.md) | Swift API Design Guidelines |
| N8 | React | Components, hooks, props, contexts | [`references/naming-react.md`](references/naming-react.md) | React docs + lint defaults |
| N9 | Vue | SFCs, props, emits, stores, composables | [`references/naming-vue.md`](references/naming-vue.md) | Vue Official Style Guide |
| N10 | JavaScript / TypeScript | Files, interfaces, enums, constants | [`references/naming-javascript-typescript.md`](references/naming-javascript-typescript.md) | Google JS Style + TS Do's/Dont's |
| N11 | Python | Modules, classes, dunder/protected names | [`references/naming-python.md`](references/naming-python.md) | PEP 8 |

## Rule Index

All rules live in [`rules/core-directives.md`](rules/core-directives.md) in `Context` / `Rule` / `Avoid` form. Cite the ids in reviews.

### 1. SOLID Principles (`solid-`) — CRITICAL
`solid-srp` · `solid-ocp` · `solid-lsp` · `solid-isp` · `solid-dip`

### 2. Clean Code Patterns (`clean-`) — CRITICAL
`clean-kiss` · `clean-yagni` · `clean-dry` · `clean-tda`

### 3. Function Design (`fn-`) — HIGH
`fn-small-functions` · `fn-meaningful-names` · `fn-single-abstraction-level` · `fn-early-returns`

### 4. Pragmatic Software Design (`prag-`) — HIGH
`prag-guard-clauses` · `prag-no-exceptions-for-flow` · `prag-no-flag-arguments` · `prag-explaining-variables` · `prag-dop-vs-oop-boundary`

### 5. Universal Naming (`name-`) — HIGH
`name-intent-over-mechanism` · `name-boolean-predicate` · `name-prefix-escaping` · `name-no-type-encoding`

## Validation Checklist

- [ ] Each class/function has a single, well-defined responsibility (SRP)
- [ ] Code is as simple as possible; no premature abstractions (KISS/YAGNI)
- [ ] Duplication is only abstracted after the 3rd occurrence (DRY)
- [ ] Each function does one thing at one abstraction level; no internal section comments needed
- [ ] Early returns are used to minimize nesting
- [ ] Names are meaningful and self-documenting
- [ ] Behavior lives with the data (TDA)
- [ ] Dependencies point toward abstractions, not concretions (DIP)
- [ ] Complexity is justified by the requirements, not "dogma"
- [ ] Guard clauses are used to validate inputs immediately and fail-fast
- [ ] Exceptions are not used for normal business control flow
- [ ] Methods do not use boolean flag parameters to steer execution paths
- [ ] Complex conditionals are broken down into well-named explaining variables
- [ ] Every name matches the loaded stack's naming table (`references/naming-*.md`)
- [ ] Booleans read as predicates; escaping identifiers carry the agreed prefix; no type-encoded names

## External References

- [Clean Code, Robert C. Martin](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
- [Refactoring, Martin Fowler](https://refactoring.com)
- [SOLID Principles](https://en.wikipedia.org/wiki/SOLID)
- [KISS Principle](https://en.wikipedia.org/wiki/KISS_principle)
