---
title: One Behaviour Per Test Method
impact: CRITICAL
impactDescription: A test covering several behaviours stops at the first failure, hiding every later problem until the first is fixed
tags: phpunit, structure, granularity, feedback
---

## One Behaviour Per Test Method

**Impact: CRITICAL — PHPUnit stops a test at the first failed assertion, so a multi-behaviour test reports one problem per run**

A test method verifies one claim. Several assertions are fine when they describe facets of that single claim; several unrelated claims are not.

## Bad Example

```php
public function test_user_registration(): void
{
    $result = $this->service->register('a@b.co', 'hunter2');

    $this->assertTrue($result->isSuccessful());
    $this->assertSame('a@b.co', $result->user()->email());
    $this->assertTrue(password_verify('hunter2', $result->user()->passwordHash()));
    $this->assertCount(1, $this->mailer->sent());              // notification behaviour
    $this->assertSame('welcome', $this->mailer->sent()[0]->template());
    $this->assertTrue($this->auditLog->has('user.registered')); // audit behaviour
    $this->assertFalse($this->service->register('a@b.co', 'x')->isSuccessful()); // duplicate behaviour
}
```

If hashing breaks, you learn nothing about the mailer, the audit log, or duplicate handling until it is fixed — three more edit-run cycles.

## Good Example

```php
public function test_it_creates_the_user_with_a_hashed_password(): void
{
    $result = $this->service->register('a@b.co', 'hunter2');

    $this->assertSame('a@b.co', $result->user()->email());
    $this->assertTrue(password_verify('hunter2', $result->user()->passwordHash()));
}

public function test_it_sends_a_welcome_email_on_registration(): void
{
    $this->service->register('a@b.co', 'hunter2');

    $this->assertSame(['welcome'], $this->mailer->sentTemplates());
}

public function test_it_rejects_an_email_that_is_already_registered(): void
{
    $this->service->register('a@b.co', 'hunter2');

    $result = $this->service->register('a@b.co', 'other');

    $this->assertFalse($result->isSuccessful());
}
```

One run now reports every broken behaviour at once, and each failing method name states what regressed.

## Notes

- Multiple assertions describing **one** outcome are correct: asserting on three fields of the same returned value is one claim about that value.
- The word "and" in a test name is the reliable smell — `test_it_saves_and_notifies` is two tests.
- Repeated arrange code across the split tests is not duplication worth removing with `setUp()`; extract a named factory method instead ([`struct-factory-over-setup`](struct-factory-over-setup.md)).
- Long assertion lists over the same object are often better expressed as one comparison against an expected value object.

## Why

- **Parallel feedback**: All independent regressions surface in a single run.
- **Naming as documentation**: The failing test's name is the bug report.
- **Change isolation**: When a behaviour is removed, one test is deleted rather than surgically edited out of a large one.
