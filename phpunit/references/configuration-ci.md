# Configuration & CI

PHPUnit 12 configuration, the CLI worth knowing, coverage, and what to gate a build on.

## When to Load

- Setting up `phpunit.xml` for a new project or tightening an existing one
- Wiring the suite into CI
- Upgrading from PHPUnit 9/10/11 to 12
- Deciding what should fail a build

## Rule Index

- [`ci-attributes-only`](../rules/ci-attributes-only.md) — Attributes; annotations are removed in 12
- [`ci-strict-config`](../rules/ci-strict-config.md) — Strictness flags and suite separation

## Version Requirements

| PHPUnit | PHP | Metadata |
|---|---|---|
| 12.x | 8.3+ | Attributes only |
| 11.x | 8.2+ | Attributes; annotations deprecated |
| 10.x | 8.1+ | Attributes introduced; annotations still read |
| 9.x | 7.3+ | Annotations |

Check the floor before upgrading — PHPUnit 12 on a PHP 8.2 deployment target will not install.

## Reference Configuration

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
        <testsuite name="feature">
            <directory>tests/Feature</directory>
        </testsuite>
    </testsuites>

    <source restrictDeprecations="true" restrictNotices="true" restrictWarnings="true">
        <include>
            <directory>src</directory>
        </include>
        <exclude>
            <directory>src/Migrations</directory>
        </exclude>
    </source>

    <coverage includeUncoveredFiles="true">
        <report>
            <html outputDirectory="build/coverage"/>
            <clover outputFile="build/clover.xml"/>
            <text outputFile="php://stdout" showOnlySummary="true"/>
        </report>
    </coverage>

    <php>
        <ini name="error_reporting" value="-1"/>
        <env name="APP_ENV" value="testing"/>
    </php>
</phpunit>
```

Note the PHPUnit 10+ shape: `<source>` replaced the old `<filter>`/`<coverage><include>` element, and the strictness attributes moved onto the root element.

## CLI Worth Knowing

```bash
vendor/bin/phpunit --testsuite unit                 # one suite
vendor/bin/phpunit --filter 'PricingServiceTest'    # one class
vendor/bin/phpunit --filter 'it_prices.*bulk'       # regex over test names
vendor/bin/phpunit --group slow --exclude-group db  # by #[Group]

vendor/bin/phpunit --order-by=defects               # previously failing first (needs cacheDirectory)
vendor/bin/phpunit --order-by=random --random-order-seed=12345
vendor/bin/phpunit --stop-on-failure                # fast local loop

vendor/bin/phpunit --testdox                        # human-readable behaviour list
vendor/bin/phpunit --list-tests                     # what would run
vendor/bin/phpunit --coverage-text
```

`--testdox` output is worth checking in review: it renders test names as sentences, which immediately exposes names that describe implementation rather than behaviour.

## CI Pipeline Shape

```yaml
- run: composer install --prefer-dist --no-progress
- run: vendor/bin/phpunit --testsuite unit                    # fast, fails first
- run: vendor/bin/phpunit --testsuite integration --testsuite feature
- run: vendor/bin/phpunit --coverage-clover build/clover.xml  # separate: coverage is slow
```

Split the fast suite from the infrastructure suites so a broken unit test fails in seconds rather than after the containers boot. Run coverage as its own step — instrumentation roughly doubles runtime, so it should not be in the loop developers wait on.

Matrix over the PHP versions you actually support, and include the lowest as well as the highest.

## Coverage

Drivers: **PCOV** is much faster for line coverage; **Xdebug** is required for branch and path coverage.

```bash
php -d pcov.enabled=1 vendor/bin/phpunit --coverage-text
XDEBUG_MODE=coverage vendor/bin/phpunit --coverage-html build/coverage
```

`requireCoverageMetadata="true"` makes `#[CoversClass]` mandatory. Without it, a feature test incidentally executing half the codebase inflates the number until it stops meaning anything.

**Do not gate the build on a coverage percentage.** Line coverage records that a line executed, not that its behaviour was verified — a test with no assertions produces coverage. A percentage gate reliably produces tests written to satisfy the gate. Track the trend, review uncovered diffs in PRs, and gate on the strictness flags instead: `failOnRisky`, `failOnWarning`, `failOnDeprecation` detect actual defects.

Mutation testing (Infection) answers the question coverage cannot — whether the tests would notice if the code were wrong:

```bash
vendor/bin/infection --min-msi=70 --threads=4
```

## Upgrading to PHPUnit 12

1. **Move to attributes.** Rector's PHPUnit set converts mechanically:
   ```bash
   vendor/bin/rector process tests --config rector-phpunit.php
   ```
2. **Grep for leftovers** — an ignored annotation is silent:
   ```bash
   grep -rnE '@(test|dataProvider|covers|uses|group|depends|requires|testWith)\b' tests/
   ```
3. **Make data providers static** — required since 10.
4. **Update the XML** — migrate the config, then validate it:
   ```bash
   vendor/bin/phpunit --migrate-configuration
   ```
5. **Replace removed APIs** — `expectExceptionMessageRegExp()` → `expectExceptionMessageMatches()`; `assertContains()` on strings → `assertStringContainsString()`; the deprecated `getMockBuilder()` configuration methods → `createMock()`/`createStub()`.
6. **Run with `--display-deprecations`** and fix what the runner itself reports.

Between 12.0 and later 12.x point releases the surface continues to move; check the release ChangeLog before assuming an API is still present.

## Sources

- [PHPUnit — Documentation](https://docs.phpunit.de/en/12.0/)
- [PHPUnit — The XML configuration file](https://docs.phpunit.de/en/12.0/configuration.html)
- [PHPUnit — Command-line test runner](https://docs.phpunit.de/en/12.0/textui.html)
- [PHPUnit — Code coverage](https://docs.phpunit.de/en/12.0/code-coverage.html)
- [PHPUnit — ChangeLog](https://github.com/sebastianbergmann/phpunit/blob/main/ChangeLog-12.0.md)
- [Rector — PHPUnit rules](https://github.com/rectorphp/rector-phpunit)
- [Infection — Mutation testing](https://infection.github.io/)
