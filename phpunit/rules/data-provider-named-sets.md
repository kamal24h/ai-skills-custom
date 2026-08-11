---
title: Name Every Data Set
impact: MEDIUM
impactDescription: "with data set #3" forces the reader to count array entries to find out what failed
tags: phpunit, data-provider, naming, diagnostics
---

## Name Every Data Set

**Impact: MEDIUM — The data-set label is the only thing distinguishing one generated test from another in the failure report**

Use string keys in the provider's return value. They become part of the test name.

## Bad Example

```php
public static function emailProvider(): array
{
    return [
        ['a@b.co', true],
        ['a@b', false],
        ['@b.co', false],
        ['a b@c.co', false],
        ['a@b..co', false],
    ];
}
```

```
✗ test_it_validates_email with data set #4
  Failed asserting that true is false.
```

To learn what broke you must open the file and count to the fifth entry, remembering that PHPUnit indexes from zero.

## Good Example

```php
/** @return array<string, array{string, bool}> */
public static function emailProvider(): array
{
    return [
        'valid address'            => ['a@b.co',    true],
        'missing tld'              => ['a@b',       false],
        'missing local part'       => ['@b.co',     false],
        'space in local part'      => ['a b@c.co',  false],
        'consecutive dots in host' => ['a@b..co',   false],
    ];
}
```

```
✗ test_it_validates_email with data set "consecutive dots in host"
  Failed asserting that true is false.
```

The report now states the rule that regressed.

## Notes

- Names also make targeted reruns possible:
  ```bash
  vendor/bin/phpunit --filter 'test_it_validates_email.*consecutive dots'
  ```
- With a generator, yield with a key: `yield 'missing tld' => ['a@b', false];`
- Name the **case**, not the data: `'missing tld'` beats `'a@b'`. The point is to say why the case exists.
- Add a docblock `@return` shape (`array<string, array{string, bool}>`). PHPStan and Psalm use it to verify that provider tuples match the test method's signature — a mismatch is otherwise only found at runtime.
- Keep data sets to the boundaries and representative cases. Twenty near-identical rows slow the suite and obscure which distinctions actually matter.

## Why

- **Self-describing failures**: CI output reads as a list of broken rules.
- **Targeted reruns**: A named set can be filtered without counting indices.
- **Intentional coverage**: Naming each case forces you to articulate why it exists, which surfaces duplicates and gaps.
