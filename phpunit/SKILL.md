---
name: phpunit
description: Expert guidance for writing, running, and maintaining PHPUnit tests. Use this skill when creating new tests, refactoring existing ones, or troubleshooting test failures in PHP projects. Triggers on "PHPUnit", "PHP test", "unit test", "data provider", "createMock", "assertSame", "test double", "flaky test", "phpunit.xml".
model: inherit
---

# PHPUnit Best Practices

Procedural knowledge and patterns for effective PHP testing with **PHPUnit 12.x** (PHP 8.3+). Emphasises strict comparison, the AAA pattern, deterministic isolation, and attribute-based metadata. 19 rules across 6 categories with bad / good examples in `rules/`; per-category guides in `references/`.

## Specialized Agents

Specialized personas for PHP testing. Load these from `agents/` to provide expert context.

| Agent | Role | Focus |
|-------|------|-------|
| **phpunit-pro** | Testing Expert | AAA pattern, test doubles, isolation, data providers, AI testing. |

## When to Use

- Creating new unit, integration, or feature tests
- Refactoring existing test suites for better performance or isolation
- Troubleshooting failing, flaky, or order-dependent tests
- Designing test doubles for a collaborator
- Configuring `phpunit.xml` or wiring the suite into CI
- Upgrading a suite from PHPUnit 9/10/11 to 12
- Testing AI-driven or probabilistic outputs

## Step 1: Detect the PHPUnit Version

**Check before recommending any API — the metadata system changed twice in recent majors.**

```json
// composer.json
{ "require-dev": { "phpunit/phpunit": "^12.0" } }
```

| PHPUnit | PHP | Metadata | Data providers |
|---------|-----|----------|----------------|
| **12.x** | 8.3+ | Attributes **only** — annotations removed | Must be `static` |
| 11.x | 8.2+ | Attributes; annotations deprecated | Must be `static` |
| 10.x | 8.1+ | Attributes introduced; annotations still read | Must be `static` |
| 9.x | 7.3+ | Annotations | May be non-static |

On 12.x a leftover `@dataProvider` or `@test` is inert text — the test either runs with no arguments or silently disappears from the suite. See [`ci-attributes-only`](rules/ci-attributes-only.md).

## Core Workflow

1. **Analyse** — identify the system under test and which collaborators are inputs versus outputs.
2. **Arrange** — build fixtures with named factory methods; keep `setUp()` for wiring only.
3. **Double** — `createStub()` for value sources, `createMock()` only where the call *is* the behaviour, a hand-written fake for stateful collaborators.
4. **Act** — one statement.
5. **Assert** — the most specific assertion available, with hard-coded expected values.
6. **Verify** — run with `--order-by=random` and the strictness flags enabled.

## Core Directives

### MUST DO

- Follow the **AAA (Arrange, Act, Assert)** pattern, with a single act statement
- Use `assertSame()` for scalar equality; `assertEquals()` only for value-object comparison
- Use the most specific assertion available (`assertCount`, `assertStringContainsString`, …)
- Name tests after the scenario and the expected outcome
- Use attributes for all metadata (`#[Test]`, `#[DataProvider]`, `#[CoversClass]`)
- Declare data providers `public static` and have them return scalars
- Name every data set with a string key
- Inject the clock, randomness, and every external collaborator
- Isolate database state per test (transaction rollback or truncation)
- Declare `void` return types on test methods and `declare(strict_types=1)` in test files
- Run the suite with `executionOrder="random"` and `failOnRisky`/`failOnWarning`/`failOnDeprecation`

### MUST NOT DO

- Use `assertEquals()` where `assertSame()` applies, or `assertTrue()` on a computed comparison
- Double the system under test (`createPartialMock` on the SUT) or test private methods
- Set `expects($this->once())` on collaborators whose call is not the behaviour under test
- Put `expectException()` before the arrange block
- Put conditionals or loops in a test body
- Rely on static properties, singletons, superglobals, or another test's leftovers
- Call `new DateTimeImmutable()`, `random_int()`, or `uniqid()` inside code under test
- Call live external APIs or model endpoints in the default suite
- Gate the build on a coverage percentage

## Category Index — When to Load Which Reference

| # | Category | Impact | Load when… | Reference | Prefix | Rules |
|--:|----------|:------:|------------|-----------|--------|:-----:|
| 1 | Test Structure | CRITICAL | Organising a test class, naming, fixtures, suite layout | [`references/test-structure.md`](references/test-structure.md) | `struct-` | 4 |
| 2 | Assertions | CRITICAL | Choosing an assertion, comparing floats/collections/exceptions | [`references/assertions.md`](references/assertions.md) | `assert-` | 4 |
| 3 | Test Doubles | HIGH | Stub vs mock vs fake, doubling a hard-to-double dependency | [`references/test-doubles.md`](references/test-doubles.md) | `double-` | 4 |
| 4 | Data Providers | HIGH | Parameterising a test, boundary matrices, provider errors | [`references/data-providers.md`](references/data-providers.md) | `data-` | 2 |
| 5 | Isolation & State | CRITICAL | Flaky or order-dependent tests, database/clock/filesystem state | [`references/isolation.md`](references/isolation.md) | `iso-` | 3 |
| 6 | Configuration & CI | HIGH | `phpunit.xml`, CI wiring, coverage, upgrading to 12 | [`references/configuration-ci.md`](references/configuration-ci.md) | `ci-` | 2 |
| 7 | Best Practices | HIGH | What to test, reviewing tests, introducing tests to legacy code | [`references/best-practices.md`](references/best-practices.md) | — | — |
| 8 | AI & Probabilistic | MEDIUM | Testing LLM-backed features or non-deterministic output | [`references/ai-testing.md`](references/ai-testing.md) | — | — |

## Rule Index

### 1. Test Structure (`struct-`) — CRITICAL
`struct-aaa` · `struct-one-behaviour` · `struct-descriptive-names` · `struct-factory-over-setup`

### 2. Assertions (`assert-`) — CRITICAL
`assert-same-over-equals` · `assert-specific-over-generic` · `assert-exception-scope` · `assert-no-conditional-logic`

### 3. Test Doubles (`double-`) — HIGH
`double-stub-vs-mock` · `double-no-mock-sut` · `double-interface-not-concrete` · `double-fake-over-chain`

### 4. Data Providers (`data-`) — HIGH
`data-provider-static` · `data-provider-named-sets`

### 5. Isolation & State (`iso-`) — CRITICAL
`iso-no-shared-state` · `iso-inject-time-randomness` · `iso-database-per-test`

### 6. Configuration & CI (`ci-`) — HIGH
`ci-attributes-only` · `ci-strict-config`

## Validation Checklist

- [ ] Every test follows AAA with exactly one act statement
- [ ] `assertSame()` used for scalars; `assertEquals()` only for value objects
- [ ] The most specific assertion is used — no `assertTrue()` on a comparison
- [ ] Test names state the scenario and the expected outcome
- [ ] All metadata uses attributes; no `@test`/`@dataProvider`/`@covers` remain
- [ ] Data providers are `public static`, return scalars, and every set is named
- [ ] `expectException()` sits immediately before the throwing call, which is last
- [ ] No test doubles the system under test; no private methods tested directly
- [ ] Mock expectations exist only where the interaction is the behaviour
- [ ] No static properties, singletons, or superglobals shared between tests
- [ ] Clock and randomness are injected, not called inside the code under test
- [ ] Database state is rolled back or truncated per test
- [ ] Suite passes with `--order-by=random` at any seed
- [ ] `failOnRisky`, `failOnWarning`, `failOnDeprecation` enabled and green
- [ ] Live external calls are excluded from the default suite

## External References

- [PHPUnit Documentation (12.0)](https://docs.phpunit.de/en/12.0/)
- [PHPUnit — Attributes](https://docs.phpunit.de/en/12.0/attributes.html)
- [PHPUnit — XML configuration](https://docs.phpunit.de/en/12.0/configuration.html)
- [PHPUnit — ChangeLog 12.0](https://github.com/sebastianbergmann/phpunit/blob/main/ChangeLog-12.0.md)
- [Martin Fowler — Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html)
- [Martin Fowler — Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
- [PSR-20: Clock](https://www.php-fig.org/psr/psr-20/)
- [Testing in Laravel](https://laravel.com/docs/testing)
- [Pest PHP (alternative runner)](https://pestphp.com)
- [Mockery (alternative doubles)](http://docs.mockery.io)
- [Infection (mutation testing)](https://infection.github.io/)
