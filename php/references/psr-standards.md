# PSR Standards

PHP-FIG interoperability standards: autoloading, coding style, and naming.

## When to Load

- Setting up `composer.json` autoload configuration
- Configuring PHP-CS-Fixer or PHP_CodeSniffer for a project
- Reviewing file, namespace, or class naming
- Deciding which interface a library should type-hint against (PSR-3, PSR-7, PSR-11…)

## Rule Categories by Priority

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | Autoloading (PSR-4) | HIGH | `psr-` |
| 2 | Coding style (PSR-12) | HIGH | `psr-` |
| 3 | Naming and file structure | HIGH | `psr-` |

## Rule Index

- [`psr-4-autoloading`](../rules/psr-4-autoloading.md) — Namespace prefix maps to a base directory
- [`psr-12-coding-style`](../rules/psr-12-coding-style.md) — Braces, spacing, imports, line length
- [`psr-namespace-usage`](../rules/psr-namespace-usage.md) — One namespace per file, `use` over FQCN in code
- [`psr-file-structure`](../rules/psr-file-structure.md) — Declarations or side effects, never both
- [`psr-naming-classes`](../rules/psr-naming-classes.md) — `StudlyCaps`, one class per file, filename matches
- [`psr-naming-methods`](../rules/psr-naming-methods.md) — `camelCase` methods, `UPPER_CASE` constants

## Key Principles

### PSR-4 is a mapping, not a convention

```json
{
  "autoload": {
    "psr-4": { "App\\": "src/" }
  },
  "autoload-dev": {
    "psr-4": { "App\\Tests\\": "tests/" }
  }
}
```

`App\Service\InvoiceBuilder` must live at `src/Service/InvoiceBuilder.php`. The mapping is case-sensitive on Linux even when it works on Windows and macOS — the single most common cause of "works locally, class not found in CI".

After changing autoload config, `composer dump-autoload` is required. In production use `composer dump-autoload --optimize --classmap-authoritative` to convert lookups to a static classmap and stop filesystem probing.

### PSR-12 supersedes PSR-2

PSR-2 is deprecated. PSR-12 extends it with rules for the parts PSR-2 predated: `declare` statements, return types, nullable type spacing, multi-line arguments, and trait `use` imports.

```php
<?php

declare(strict_types=1);

namespace App\Service;

use App\Contract\Mailer;
use Psr\Log\LoggerInterface;

final class InvoiceMailer implements Mailer
{
    public function __construct(
        private readonly LoggerInterface $logger,
    ) {
    }
}
```

Enforce rather than review: PHP-CS-Fixer with `@PSR12` (or the newer `@PER-CS` ruleset, which is where PHP-FIG's evolving style now lives) in a pre-commit hook and in CI. Style comments in code review are wasted reviewer attention.

### The side-effect rule is the one that actually bites

A file must **either** declare things (classes, functions, constants) **or** cause side effects (emit output, change ini settings, connect to something) — never both.

```php
<?php
// ❌ both declaration and side effect
ini_set('display_errors', '1');
session_start();

final class UserController { … }
```

Autoloading a class must not start a session. When it does, behavior depends on which class happened to be loaded first, and the bug appears only under certain request paths. Entry points (`public/index.php`, `bin/console`) are the place for side effects.

### Which PSR interfaces to depend on

| PSR | Interface | Use for |
|---|---|---|
| PSR-3 | `LoggerInterface` | Any logging dependency — never type-hint Monolog directly |
| PSR-4 | — | Autoloading |
| PSR-6 / PSR-16 | `CacheItemPoolInterface` / `CacheInterface` | Cache abstraction (PSR-16 for the simple key/value case) |
| PSR-7 / PSR-17 | `RequestInterface`, `ResponseInterface`, factories | HTTP messages |
| PSR-11 | `ContainerInterface` | Reading from a DI container at framework boundaries |
| PSR-14 | `EventDispatcherInterface` | Event dispatch |
| PSR-15 | `MiddlewareInterface`, `RequestHandlerInterface` | HTTP middleware pipelines |
| PSR-18 | `ClientInterface` | HTTP client — lets consumers swap Guzzle for anything |

Depending on the interface instead of the implementation is [`solid-dip`](../rules/solid-dip.md) applied at the ecosystem level: it is what allows a library to be used in Laravel, Symfony, and Slim without adapters.

**Do not** inject `ContainerInterface` into application services to fetch dependencies on demand — that is the service locator anti-pattern wearing a PSR badge. Inject the dependencies themselves.

### Naming rules worth stating explicitly

- Classes, interfaces, traits, enums: `StudlyCaps` — `InvoiceBuilder`, not `invoice_builder`
- Methods and properties: `camelCase`
- Class constants: `UPPER_SNAKE_CASE`
- No `I` prefix on interfaces (`Mailer`, not `IMailer`) and no `Abstract`/`Interface` suffix requirement — PSR does not mandate them, and most modern codebases drop them
- One class per file, filename identical to the class name

## Sources

- [PSR-4: Autoloader](https://www.php-fig.org/psr/psr-4/)
- [PSR-12: Extended Coding Style](https://www.php-fig.org/psr/psr-12/)
- [PER Coding Style](https://www.php-fig.org/per/coding-style/)
- [PHP-FIG — All PSRs](https://www.php-fig.org/psr/)
- [PHP-CS-Fixer](https://cs.symfony.com/)
- [Composer — Autoloading](https://getcomposer.org/doc/04-schema.md#autoload)
