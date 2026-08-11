# Sections

This file defines all sections, their ordering, impact levels, and descriptions.
The section ID (in parentheses) is the filename prefix used to group rules.

Target: **PHPUnit 12.x** (PHP 8.3+). Metadata is attribute-only — doc-comment annotations were removed.

---

## 1. Test Structure (struct)

**Impact:** CRITICAL
**Description:** How a test is organised determines whether a failure is diagnosable. Covers the Arrange/Act/Assert shape, one behaviour per test, names that state the scenario and expectation, and building fixtures with factory methods instead of accumulating shared `setUp()` state.

## 2. Assertions (assert)

**Impact:** CRITICAL
**Description:** The assertion decides what a failure message tells you. Covers `assertSame` over `assertEquals`, specific assertions over generic truthiness, narrowing exception expectations to the call that should throw, and keeping conditionals out of test bodies.

## 3. Test Doubles (double)

**Impact:** HIGH
**Description:** Stub for state, mock for interaction, fake when a chain of `willReturn` becomes unreadable. Covers never doubling the system under test, doubling interfaces rather than concrete classes, and recognising when mocking is compensating for a design problem.

## 4. Data Providers (data)

**Impact:** HIGH
**Description:** Data providers turn one test into many. Covers the static requirement in PHPUnit 10+, named data sets so failures identify themselves, and keeping provider methods free of logic and I/O.

## 5. Isolation & State (iso)

**Impact:** CRITICAL
**Description:** A test that depends on another test, on the clock, on randomness, or on leftover database rows is a future intermittent failure. Covers shared state, injected time and randomness, and per-test database isolation.

## 6. Configuration & CI (ci)

**Impact:** HIGH
**Description:** PHPUnit's defaults are permissive; strictness is opt-in. Covers attribute-only metadata, the strict XML configuration, failing on deprecations and risky tests, random execution order, and using coverage as a signal rather than a gate.
