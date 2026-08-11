---
title: Configure PHPUnit Strictly and Fail the Build on Warnings
impact: HIGH
impactDescription: PHPUnit's defaults tolerate risky tests, deprecations, and tests that assert nothing — all of which hide real problems
tags: phpunit, configuration, ci, strictness, deprecations
---

## Configure PHPUnit Strictly and Fail the Build on Warnings

**Impact: HIGH — A green suite under permissive settings can contain tests that assert nothing and code that is already deprecated**

Strictness is opt-in. The default configuration reports these as notices nobody reads.

## Bad Example

```xml
<?xml version="1.0"?>
<phpunit bootstrap="vendor/autoload.php">
    <testsuites>
        <testsuite name="all">
            <directory>tests</directory>
        </testsuite>
    </testsuites>
</phpunit>
```

```bash
vendor/bin/phpunit          # exits 0 with 14 deprecations and 3 risky tests
```

A test with no assertions passes. Code calling a method deprecated in the next major version passes. Output accidentally echoed from production code passes. None of it turns CI red.

## Good Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<phpunit xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:noNamespaceSchemaLocation="vendor/phpunit/phpunit/phpunit.xsd"
         bootstrap="vendor/autoload.php"
         cacheDirectory=".phpunit.cache"
         executionOrder="random"
         resolveDependencies="true"
         requireCoverageMetadata="true"
         beStrictAboutCoverageMetadata="true"
         beStrictAboutOutputDuringTests="true"
         failOnRisky="true"
         failOnWarning="true"
         failOnDeprecation="true"
         failOnNotice="true"
         displayDetailsOnTestsThatTriggerDeprecations="true"
         displayDetailsOnTestsThatTriggerErrors="true"
         displayDetailsOnPhpunitDeprecations="true"
         colors="true">

    <testsuites>
        <testsuite name="unit">
            <directory>tests/Unit</directory>
        </testsuite>
        <testsuite name="integration">
            <directory>tests/Integration</directory>
        </testsuite>
    </testsuites>

    <source restrictDeprecations="true" restrictNotices="true" restrictWarnings="true">
        <include>
            <directory>src</directory>
        </include>
    </source>

    <php>
        <ini name="error_reporting" value="-1"/>
        <env name="APP_ENV" value="testing"/>
    </php>
</phpunit>
```

```bash
vendor/bin/phpunit --testsuite unit          # fast, no infrastructure
vendor/bin/phpunit --testsuite integration   # database, containers
```

## What Each Setting Buys

| Setting | Catches |
|---|---|
| `executionOrder="random"` | Hidden order dependencies ([`iso-no-shared-state`](iso-no-shared-state.md)) |
| `failOnRisky` | Tests that assert nothing, or leave output behind |
| `failOnWarning` / `failOnNotice` | PHP warnings and notices raised by the code under test |
| `failOnDeprecation` | Deprecated calls, before the next major release breaks the build |
| `requireCoverageMetadata` | Tests without `#[CoversClass]` inflating the coverage number |
| `beStrictAboutOutputDuringTests` | Stray `echo`/`var_dump` left in production code |
| `<source restrictDeprecations>` | Limits the above to **your** code, so vendor deprecations do not block you |
| `cacheDirectory` | Result cache for `--order-by=defects` |

## Notes

- Adopt incrementally on an existing suite: enable one flag, fix the fallout, commit, repeat. Turning all of them on at once on a legacy suite produces hundreds of failures and gets reverted.
- `executionOrder="random"` prints the seed. Record it in CI so a failure can be reproduced with `--random-order-seed=<seed>`.
- `--order-by=defects` reruns previously failing tests first — a large feedback-loop win locally, and it needs `cacheDirectory` to work.
- Add `.phpunit.cache` and `.phpunit.result.cache` to `.gitignore`.
- Coverage requires Xdebug or PCOV. PCOV is substantially faster for line coverage; Xdebug is needed for branch and path coverage.
- **Do not gate the build on a coverage percentage.** Line coverage records that code ran, not that it was verified; a percentage gate is satisfied by tests nobody reads. Track the trend, and gate on the strictness flags above instead — they detect real defects.
- Run with `--fail-on-skipped` in CI if skipped tests should not accumulate silently.

## Why

- **Deprecations surface early**: The upgrade becomes a series of small fixes instead of one blocked release.
- **Empty tests cannot hide**: `failOnRisky` turns a test that verifies nothing into a build failure.
- **Order dependencies become visible**: Randomisation is the only reliable way to find them.
