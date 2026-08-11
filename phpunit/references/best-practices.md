# PHPUnit Best Practices

The working principles behind the rules, plus the decisions that come before writing any test.

## When to Load

- Starting a test suite on a project that has none
- Deciding what deserves a test and what does not
- A suite exists but nobody trusts it, or nobody runs it
- Reviewing someone else's tests

## Core Principles

1. **Test behaviour, not implementation.** A test should survive any refactor that preserves observable behaviour. If renaming a private method breaks tests, the tests are coupled to the wrong thing.
2. **A failing test must name the problem.** The method name plus the assertion message should be enough to know what regressed, without opening the file.
3. **Tests are read far more often than written.** Optimise the body for the next reader, not for line count.
4. **Determinism is non-negotiable.** A test that fails 1% of the time is worse than no test — it trains people to rerun CI instead of investigating.
5. **The suite must be fast enough to run before every commit.** A suite people skip provides no feedback regardless of its coverage.
6. **Test code is production code.** It gets reviewed, refactored, and deleted when obsolete. It does not get a lower standard.

## What to Test

| Test it | Do not test it |
|---|---|
| Business rules, calculations, state transitions | Getters/setters with no logic |
| Validation and its boundaries | Framework internals |
| Error paths and edge cases | Third-party library behaviour |
| Public API of each class | Private methods directly |
| Bugs, as a regression test written first | Configuration constants |
| Contracts between layers | Generated code |

The highest-value tests are the ones covering **branches** — conditionals, boundaries, error handling. A suite that only exercises the happy path has high coverage and low value.

Write the regression test **before** the fix. A test that fails, then passes after the change, has proven it detects the bug. A test written afterwards has proven nothing.

## Naming and Structure

- Directory mirrors `src/`, namespace prefixed `App\Tests\`, class suffixed `Test`
- One test class per production class, `final`
- Test names state scenario and expectation: `it_rejects_a_negative_quantity`
- `#[Test]` frees the name from the `test` prefix
- AAA with one act statement; blank lines between the blocks
- Factories at the bottom, `setUp()` for wiring only

See [`test-structure.md`](test-structure.md) for the full anatomy.

## Practices That Pay Off

**Write the assertion first.** Start from the expected value and work backwards to the arrangement. This tends to produce one clear claim per test instead of a walkthrough of the code.

**Hard-code expected values.** Computing the expectation with the same formula the implementation uses tests that the formula equals itself.

**Assert on absence.** `$mock->expects($this->never())->method('send')` — "no email is sent when validation fails" is a real requirement and is otherwise untested.

**Cover the boundaries, not the middle.** Quantity 9, 10, and 11 around a threshold of 10 catches off-by-one errors. Quantity 5 and 50 do not.

**Let the test drive the design.** A class that is hard to test is hard to use: six constructor doubles means too many responsibilities; needing to stub a private method means a collaborator has not been extracted; needing the database for a pricing rule means domain logic leaked into persistence.

**Delete obsolete tests.** A test for removed behaviour is noise that will eventually be "fixed" back into relevance by someone who does not know it should be gone.

## Practices to Avoid

| Anti-pattern | Consequence |
|---|---|
| Mocking everything | Suite passes while the wiring is broken |
| Testing private methods via reflection | Permanent coupling to implementation |
| One test asserting six behaviours | One problem reported per run |
| `assertTrue($a === $b)` | Failure message contains no values |
| Shared `setUp()` fixture for all tests | The deciding input is invisible in the test |
| Sleeping to wait for something | Slow and flaky at the same time |
| Snapshot as the only assertion | Records current behaviour including its bugs |
| Coverage percentage as a build gate | Produces tests written to satisfy the gate |
| Skipping a flaky test | The bug remains, the signal is gone |

## Reviewing Tests

Questions worth asking in a code review:

- Does the test name state a behaviour? Would a failure be self-explanatory in CI?
- Is there exactly one act statement?
- Would this test still pass if the bug it targets were reintroduced elsewhere?
- Are the expected values hard-coded, or computed the same way the code computes them?
- Would this break on a pure refactor?
- Are error paths and boundaries covered, or only the happy path?
- Does anything here depend on the clock, randomness, order, or leftover state?

`vendor/bin/phpunit --testdox` renders the suite as a sentence list — an efficient way to review whether the tests describe behaviour or implementation.

## Introducing Tests to an Untested Codebase

1. Turn the next bug report into a failing test, then fix it. Repeat.
2. Add characterisation tests around the area you are about to change — they record current behaviour so a refactor can be verified even if that behaviour is imperfect.
3. Extract collaborators as you go; each extraction makes the next test easier.
4. Enable strictness flags one at a time ([`ci-strict-config`](../rules/ci-strict-config.md)), fixing the fallout before the next.
5. Do not attempt a coverage push. Chasing a percentage on legacy code produces tests that assert nothing and cement the existing design.

## Sources

- [PHPUnit — Documentation](https://docs.phpunit.de/en/12.0/)
- [Martin Fowler — Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
- [Martin Fowler — Unit Test](https://martinfowler.com/bliki/UnitTest.html)
- [Martin Fowler — Self Testing Code](https://martinfowler.com/bliki/SelfTestingCode.html)
- [Martin Fowler — Refactoring catalog](https://refactoring.com/catalog/)
- [PHP The Right Way — Testing](https://phptherightway.com/#testing)
