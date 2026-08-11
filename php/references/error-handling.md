# Error Handling

Exception hierarchy design, catch granularity, resource cleanup, and the failure modes of suppression.

## When to Load

- Designing exceptions for a new module or package
- Reviewing `try`/`catch` blocks, especially broad ones
- Handling resources that must be released (files, locks, connections, transactions)
- Deciding whether a condition should be an exception, a null return, or a result object

## Rule Categories by Priority

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | Never suppress | HIGH | `error-` |
| 2 | Hierarchy and custom types | HIGH | `error-` |
| 3 | Catch granularity and cleanup | HIGH | `error-` |

## Rule Index

- [`error-never-suppress`](../rules/error-never-suppress.md) — No `@`, no empty `catch`
- [`error-custom-exceptions`](../rules/error-custom-exceptions.md) — Domain exceptions carrying context
- [`error-exception-hierarchy`](../rules/error-exception-hierarchy.md) — A per-package base interface
- [`error-try-catch-specific`](../rules/error-try-catch-specific.md) — Catch what you can handle
- [`error-finally-cleanup`](../rules/error-finally-cleanup.md) — Release resources on every path

## Key Principles

### `Throwable`, `Error`, `Exception`

```
Throwable (interface)
├── Error                  → engine-level faults
│   ├── TypeError          → strict-type violation
│   ├── ValueError         → argument out of range (8.0+)
│   ├── ArithmeticError    → DivisionByZeroError
│   └── AssertionError
└── Exception              → application-level conditions
    ├── LogicException     → a bug: fix the code
    │   ├── InvalidArgumentException
    │   ├── DomainException
    │   └── BadMethodCallException
    └── RuntimeException   → environmental: handle it
        ├── OutOfBoundsException
        └── UnexpectedValueException
```

The `LogicException` / `RuntimeException` split is the useful one:

- **LogicException** means the caller has a bug. Do not catch it in application code — let it fail loudly in development and be reported in production.
- **RuntimeException** means the world misbehaved (network down, disk full, row missing). This is what deserves a `catch`.

`catch (Exception)` does not catch `Error`. Catching `Throwable` catches both and is appropriate in exactly one place: the top-level handler that converts anything into a 500 response and a log entry.

### Per-package marker interface

```php
namespace App\Billing\Exception;

interface BillingException extends \Throwable {}

final class PaymentDeclined extends \RuntimeException implements BillingException {}
final class InvoiceNotFound extends \RuntimeException implements BillingException {}
```

Consumers can catch everything from your module with one `catch (BillingException)` without you forcing a common base class on them — the exceptions still extend the correct SPL parent, so generic handlers keep working. This is the pattern used by most modern PHP libraries.

### Exceptions should carry structured context

```php
final class PaymentDeclined extends \RuntimeException implements BillingException
{
    public function __construct(
        public readonly string $orderId,
        public readonly string $declineCode,
        ?\Throwable $previous = null,
    ) {
        parent::__construct("Payment declined for order {$orderId}: {$declineCode}", 0, $previous);
    }
}
```

A message string forces the handler to parse English to decide what to do. Typed properties let it branch on `$e->declineCode` and let the logger attach fields instead of a blob.

Always pass `$previous` when re-throwing. Losing the original exception discards the stack frame where the problem actually occurred, which is usually the only useful part.

### Catch granularity

```php
// ❌ hides bugs: a TypeError inside the handler becomes "could not save"
try {
    $repository->save($order);
} catch (\Throwable $e) {
    $this->logger->error('could not save');
}

// ✅ catch what this code can genuinely do something about
try {
    $repository->save($order);
} catch (UniqueConstraintViolation $e) {
    return $this->mergeWithExisting($order);
} catch (ConnectionLost $e) {
    $this->queue->retryLater($order);
}
```

Two questions decide whether a `catch` belongs: *can this code do something meaningful other than logging?* and *does swallowing it leave the system in a valid state?* If both answers are no, let it propagate to the boundary handler.

### `finally` and resource cleanup

```php
$lock = $this->locks->acquire($key);
try {
    return $this->process($payload);
} finally {
    $lock->release();          // runs on return, on throw, and on early return
}
```

`finally` runs even when the `try` block returns. A `return` inside `finally` overrides the one in `try` — including overriding an in-flight exception, which silently discards it. Never return from `finally`.

Transactions follow the same shape, with an explicit rollback:

```php
$this->db->beginTransaction();
try {
    $this->db->commit();
} catch (\Throwable $e) {
    $this->db->rollBack();
    throw $e;                  // rethrow — do not convert a failure into a silent no-op
}
```

### Suppression is never the answer

```php
$data = @file_get_contents($path);        // ❌ hides permission errors, typos, missing mounts
```

`@` suppresses diagnostics but the failure still happens — the function returns `false` and the next line operates on a boolean. Since PHP 8, `@` no longer silences fatal errors, so its only remaining effect is to hide the warning that would have told you what was wrong.

Use the checked form instead, or configure the library to throw:

```php
// PDO
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);   // default since PHP 8
// json
json_decode($raw, flags: JSON_THROW_ON_ERROR);
// intdiv, DateTime, etc. already throw
```

An empty `catch {}` is the same failure with more syntax. If a failure is genuinely expected and ignorable, say so in a comment and log at debug level — never leave the block empty.

### Exceptions vs null vs result objects

| Situation | Return |
|---|---|
| Lookup where absence is normal (`findByEmail`) | `?User` |
| Lookup where absence is a broken invariant (`getById` after validation) | Throw |
| Validation with many possible failures the caller must show a user | Result/violation list, not exceptions |
| Anything crossing an infrastructure boundary | Exception |

Exceptions are for exceptional conditions. Using them for ordinary control flow (an expected empty search result) makes the happy path slower to read and hides the real errors in the same `catch`.

## Sources

- [PHP Manual — Exceptions](https://www.php.net/manual/en/language.exceptions.php)
- [PHP Manual — Predefined exceptions](https://www.php.net/manual/en/reserved.exceptions.php)
- [PHP Manual — SPL exceptions](https://www.php.net/manual/en/spl.exceptions.php)
- [PHP Manual — Errors in PHP 7+](https://www.php.net/manual/en/language.errors.php7.php)
- [PSR-3: Logger Interface](https://www.php-fig.org/psr/psr-3/)
