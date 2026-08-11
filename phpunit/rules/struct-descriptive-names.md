---
title: Name Tests After the Scenario and the Expectation
impact: HIGH
impactDescription: The test name is what a CI failure shows first; a name like test_calculate forces every reader to open the file
tags: phpunit, naming, readability, ci
---

## Name Tests After the Scenario and the Expectation

**Impact: HIGH — A failing test's name is the entire message most people ever read**

Name the condition and the expected outcome, not the method being called.

## Bad Example

```php
public function testCalculate(): void { … }
public function testCalculate2(): void { … }
public function testTotalWorks(): void { … }
public function testException(): void { … }
```

`testCalculate2 failed` in CI communicates nothing. The reader must open the file, read the body, and reconstruct the intent before they can judge whether the test or the code is wrong.

## Good Example

```php
public function test_it_applies_the_bulk_discount_above_ten_units(): void { … }
public function test_it_does_not_apply_the_bulk_discount_at_exactly_ten_units(): void { … }
public function test_it_throws_when_the_quantity_is_negative(): void { … }
```

Each name is a sentence about behaviour. A failure report reads as a list of broken requirements.

## Notes

- Two conventions are common and both work; pick one per project and enforce it:
  - `test_it_<expected>_when_<condition>` (snake_case, reads as prose)
  - `<method>_<condition>_<expected>` (e.g. `total_withNegativeQuantity_throws`)
- With PHPUnit 12 the `test` prefix is optional if you mark methods with `#[Test]`. Using the attribute frees the name entirely:
  ```php
  #[Test]
  public function it_applies_the_bulk_discount_above_ten_units(): void { … }
  ```
- Name boundaries explicitly. `above_ten` and `at_exactly_ten` as separate tests document the boundary better than any comment.
- Avoid naming the implementation (`test_it_uses_array_filter`) — that name becomes wrong the moment the implementation improves.
- For data-provider cases, the data-set name carries this burden instead; name the sets ([`data-provider-named-sets`](data-provider-named-sets.md)).

## Why

- **CI legibility**: The failure list becomes a readable specification of what broke.
- **Review speed**: A reviewer can judge coverage from the method list without reading bodies.
- **Intent preservation**: A name stating the rule survives refactors that change how the rule is implemented.
