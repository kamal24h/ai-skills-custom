---
name: php
description: PHP 8.x modern patterns, PSR standards, and SOLID principles. Use when reviewing PHP code, checking type safety, auditing code quality, or ensuring PHP best practices. Triggers on "review PHP", "check PHP code", "audit PHP", or "PHP best practices".
model: inherit
---

# PHP Best Practices

Modern PHP 8.x patterns, PSR standards, type system best practices, and SOLID principles. Contains 51 rules for writing clean, maintainable PHP code.

## Specialized Agents

Specialized personas for PHP development. Load these from `agents/` to provide expert context.

| Agent | Role | Focus |
|-------|------|-------|
| **php-pro** | PHP Expert | Modern PHP 8.x features, enums, types, performance. |

## When to Use

Reference these guidelines when:
- Writing or reviewing PHP code
- Implementing classes and interfaces
- Using PHP 8.x modern features
- Ensuring type safety
- Following PSR standards
- Applying design patterns (SOLID)

## Step 1: Detect PHP Version

**Always check the project's PHP version before giving any advice.**

```bash
php -v
```
Check `composer.json` for the required PHP version:
```json
{ "require": { "php": "^8.3" } }
```

### Feature Availability by Version

| Feature | Version | Rule Prefix |
|---------|---------|-------------|
| Union types, match, nullsafe, named args, constructor promotion | 8.0+ | `modern-`, `type-` |
| Enums, readonly properties, intersection types, first-class callables | 8.1+ | `modern-` |
| Readonly classes, DNF types | 8.2+ | `modern-` |
| Typed class constants, `#[\Override]` | 8.3+ | `modern-` |
| Property hooks, asymmetric visibility | 8.4+ | `modern-` |
| Pipe operator `|>` | 8.5+ | `modern-` |

## Core Directives

### MUST DO

- Declare `strict_types=1` in every PHP file
- Use PHP 8.x features (Constructor Promotion, Match, Enums) wherever possible
- Always declare parameter and return types explicitly
- Implement specific Exception classes for different error scenarios
- Follow PSR-12 coding style and PSR-4 autoloading
- Use `#[Override]` (PHP 8.3+) when overriding parent methods
- Leverage Readonly properties/classes for immutable data structures

### MUST NOT DO

- Use the `@` error suppression operator
- Use `mixed` type when more specific types (union/intersection) are possible
- Concatenate user input into SQL strings (use prepared statements)
- Put multiple classes in a single file
- Rely on global variables (use Dependency Injection)
- Use MD5 or SHA1 for passwords (use `password_hash`)

## Category Index — When to Load Which Reference

| # | Category | Impact | Load when… | Reference | Prefix | Rules |
|--:|----------|:------:|------------|-----------|--------|:-----:|
| 1 | Type System | CRITICAL | Adding type declarations, choosing union/intersection/nullable, raising analyzer level | [`references/type-system.md`](references/type-system.md) | `type-` | 9 |
| 2 | Modern PHP Features | CRITICAL | Using 8.x syntax, enums, readonly, property hooks — check the version floor first | [`references/modern-php.md`](references/modern-php.md) | `modern-` | 16 |
| 3 | PSR Standards | HIGH | Autoload config, code style tooling, naming, choosing PSR interfaces | [`references/psr-standards.md`](references/psr-standards.md) | `psr-` | 6 |
| 4 | SOLID Principles | HIGH | Designing or splitting a class, reviewing an interface or hierarchy | [`references/solid-principles.md`](references/solid-principles.md) | `solid-` | 5 |
| 5 | Error Handling | HIGH | Designing exceptions, reviewing try/catch, resource and transaction cleanup | [`references/error-handling.md`](references/error-handling.md) | `error-` | 5 |
| 6 | Security | CRITICAL | Any external input, SQL, output, passwords, file uploads, security audit | [`references/security.md`](references/security.md) | `sec-` | 5 |
| 7 | Performance | MEDIUM | Large collections, memory ceilings, profiling a slow script | [`references/performance.md`](references/performance.md) | `perf-` | 5 |

## Rule Index

### 1. Type System (`type-`) — CRITICAL
`type-strict-mode` · `type-return-types` · `type-parameter-types` · `type-property-types` · `type-union-types` · `type-intersection-types` · `type-nullable-types` · `type-void-never` · `type-mixed-avoid`

### 2. Modern PHP Features (`modern-`) — CRITICAL
**8.0+**: `modern-constructor-promotion` · `modern-match-expression` · `modern-named-arguments` · `modern-nullsafe-operator` · `modern-attributes`
**8.1+**: `modern-enums` · `modern-enums-methods` · `modern-readonly-properties` · `modern-first-class-callables` · `modern-arrow-functions`
**8.2+**: `modern-readonly-classes`
**8.3+**: `modern-typed-constants` · `modern-override-attribute`
**8.4+**: `modern-property-hooks` · `modern-asymmetric-visibility`
**8.5+**: `modern-pipe-operator`

### 3. PSR Standards (`psr-`) — HIGH
`psr-4-autoloading` · `psr-12-coding-style` · `psr-namespace-usage` · `psr-file-structure` · `psr-naming-classes` · `psr-naming-methods`

### 4. SOLID Principles (`solid-`) — HIGH
`solid-srp` · `solid-ocp` · `solid-lsp` · `solid-isp` · `solid-dip`

### 5. Error Handling (`error-`) — HIGH
`error-custom-exceptions` · `error-exception-hierarchy` · `error-try-catch-specific` · `error-finally-cleanup` · `error-never-suppress`

### 6. Security (`sec-`) — CRITICAL
`sec-input-validation` · `sec-output-escaping` · `sec-sql-prepared` · `sec-password-hashing` · `sec-file-uploads`

### 7. Performance (`perf-`) — MEDIUM
`perf-array-functions` · `perf-string-functions` · `perf-generators` · `perf-lazy-loading` · `perf-avoid-globals`

## Validation Checklist

- [ ] `declare(strict_types=1)` is present at the top of all files
- [ ] All method parameters and return types are explicitly hinted
- [ ] Modern PHP features (e.g., Match, Enums) are used instead of legacy patterns
- [ ] Code follows PSR-12 formatting and PSR-4 directory structure
- [ ] SOLID principles are respected (especially SRP)
- [ ] Sensitive operations are protected against common vulnerabilities (SQLi, XSS)
- [ ] No global state is used; dependencies are injected
- [ ] Custom exceptions are thrown instead of generic ones

## External References

- [PHP Documentation](https://www.php.net/docs.php)
- [PHP The Right Way](https://phptherightway.com)
- [PHP FIG (PSR Standards)](https://www.php-fig.org/psr/)
- [PHPStan Static Analysis](https://phpstan.org)
