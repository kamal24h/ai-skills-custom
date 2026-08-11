# PHP Performance

Memory-bounded iteration, native functions, lazy construction, and the global state that blocks all of it.

## When to Load

- Processing collections large enough to approach `memory_limit`
- A script is slow or exhausting memory and the cause is not yet known
- Reviewing loops that call functions PHP already implements natively
- Deciding whether an expensive dependency should be constructed eagerly

## Rule Categories by Priority

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | Memory-bounded iteration | MEDIUM | `perf-` |
| 2 | Native array/string functions | MEDIUM | `perf-` |
| 3 | Lazy construction and global state | MEDIUM | `perf-` |

## Rule Index

- [`perf-generators`](../rules/perf-generators.md) — `yield` instead of building the whole array
- [`perf-lazy-loading`](../rules/perf-lazy-loading.md) — Construct expensive things on first use
- [`perf-array-functions`](../rules/perf-array-functions.md) — Native array functions over hand-written loops
- [`perf-string-functions`](../rules/perf-string-functions.md) — `str_*` over regex for literal work
- [`perf-avoid-globals`](../rules/perf-avoid-globals.md) — Global state defeats caching, testing, and reasoning

## Measure First

Nothing in this file should be applied speculatively. The ordering that actually matters in a PHP request is almost always:

```
1. N+1 queries / missing indexes      ← usually 10–1000× the cost of everything below
2. Uncached remote calls
3. Unbounded memory growth (OOM, swap)
4. Missing OPcache / preloading in production
5. Algorithmic complexity in application code
6. Native-vs-userland function choice  ← the smallest item on this list
```

Tools: Xdebug profiler or Blackfire for call graphs, `memory_get_peak_usage(true)` for memory ceilings, the framework's query logger for (1). A rewrite justified by intuition rather than a profile is a refactor with extra risk.

## Key Principles

### Generators bound memory, not time

```php
// ❌ entire file in memory before the first row is processed
function readRows(string $path): array
{
    return array_map('str_getcsv', file($path));
}

// ✅ one row in memory at a time
function readRows(string $path): \Generator
{
    $handle = fopen($path, 'rb');
    try {
        while (($row = fgetcsv($handle)) !== false) {
            yield $row;
        }
    } finally {
        fclose($handle);
    }
}
```

A 2 GB CSV becomes processable in constant memory. The trade-offs are real and worth stating: a generator can only be iterated once, `count()` does not work on it, and you cannot index into it. Return an array when the caller genuinely needs random access to a small collection.

`yield from` delegates to another generator without buffering, which is how a pipeline of transformations stays lazy end to end.

### Native functions win on volume, not on principle

`array_map`, `array_filter`, `array_column`, `array_sum`, `in_array` with `strict: true`, `array_key_exists` — these run in C and avoid per-iteration userland overhead. For a 10-element array the difference is unmeasurable; for a million-element array it is the difference between a request and a timeout.

The more important reason to prefer them is that they state intent: `array_column($rows, 'id')` is one obvious operation, while the equivalent `foreach` requires reading three lines to confirm it does nothing else.

Two performance traps in this area:

```php
// ❌ O(n·m): in_array scans the whole list every iteration
foreach ($ids as $id) { if (in_array($id, $blocked, true)) { … } }

// ✅ O(n): hash lookup
$blockedSet = array_flip($blocked);
foreach ($ids as $id) { if (isset($blockedSet[$id])) { … } }
```

```php
// ❌ rebuilds the array on every append in older engines and copies on write
$result = array_merge($result, $chunk);   // inside a loop

// ✅
foreach ($chunk as $item) { $result[] = $item; }
// or: array_push($result, ...$chunk);
```

### Strings: regex only when the pattern is genuinely a pattern

`str_contains`, `str_starts_with`, `str_ends_with` (8.0+), `str_replace`, `explode`, and `substr` are faster and clearer than the `preg_*` equivalents for literal work. Reach for `preg_*` when there is real alternation, quantification, or capture.

When you do use `preg_*`: hoist the pattern to a constant so the compiled-pattern cache is hit, avoid catastrophic backtracking on nested quantifiers over untrusted input, and prefer `preg_quote()` for any literal interpolated into a pattern.

For building large strings, append to an array and `implode()` once rather than repeatedly concatenating in a loop.

### Lazy construction

```php
final class ReportService
{
    private ?PdfRenderer $renderer = null;

    private function renderer(): PdfRenderer
    {
        return $this->renderer ??= new PdfRenderer($this->config);
    }
}
```

Useful when the dependency is expensive (opens a connection, loads fonts, parses a large config) and only some code paths need it. Not useful — and harmful to clarity — for cheap objects.

Prefer the container's own lazy services where the framework provides them (Symfony lazy services, Laravel deferred providers): they keep constructor injection intact and stay visible to static analysis, while a hand-rolled `??=` hides the dependency from the constructor signature.

### Global state costs more than performance

```php
// ❌
function currentUser(): User { global $user; return $user; }
```

Globals (and their disguises: `static` mutable properties, singletons, `$GLOBALS`) prevent parallel test execution, make call order significant, and turn a function's real inputs into something you must grep for. Under long-running runtimes — Swoole, RoadRunner, FrankenPHP, Octane — mutable global state survives between requests and leaks data across users, which is the same class of bug as SSR module-scope state.

Pass dependencies explicitly. If a value is genuinely request-scoped, put it in a request-scoped container binding, not in a global.

### Production runtime settings

Application-level micro-optimisation is dominated by configuration:

- **OPcache enabled** with a sufficient `opcache.memory_consumption` and `opcache.max_accelerated_files`; `opcache.validate_timestamps=0` in production with a deploy-time cache clear.
- **Preloading** (`opcache.preload`) for framework classes on PHP 7.4+.
- **JIT** helps CPU-bound numeric work and does close to nothing for typical I/O-bound web requests — measure before enabling.
- **Persistent connections** and a properly sized `pm.max_children` for FPM.

## Sources

- [PHP Manual — Generators](https://www.php.net/manual/en/language.generators.php)
- [PHP Manual — Array functions](https://www.php.net/manual/en/ref.array.php)
- [PHP Manual — String functions](https://www.php.net/manual/en/ref.strings.php)
- [PHP Manual — OPcache configuration](https://www.php.net/manual/en/opcache.configuration.php)
- [PHP Manual — Performance considerations (PCRE)](https://www.php.net/manual/en/regexp.reference.performance.php)
- [Blackfire — Profiling PHP](https://www.blackfire.io/docs/introduction)
