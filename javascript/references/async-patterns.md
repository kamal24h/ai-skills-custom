# Async Patterns

Promise combinators, `async`/`await` correctness, cancellation, and concurrency control.

## When to Load

- Running several async operations and deciding how failures should combine
- Reviewing a loop that awaits inside it
- Handling timeouts, cancellation, or retries
- Diagnosing unhandled rejections, race conditions, or a process that exits early

## Rule Categories by Priority

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | Promise combinators | CRITICAL | `async-` |
| 2 | `async`/`await` correctness | CRITICAL | `async-` |

## Rule Index

- [`async-promise-combinators`](../rules/async-promise-combinators.md) — `all` / `allSettled` / `race` / `any`
- [`async-await-patterns`](../rules/async-await-patterns.md) — Sequential vs parallel, error propagation, cleanup

## Key Principles

### Choosing a combinator

| Combinator | Resolves when | Rejects when | Use for |
|---|---|---|---|
| `Promise.all` | All fulfil | **First** rejection | Independent work where any failure fails the whole operation |
| `Promise.allSettled` | All settle | Never | Batch work where partial success is meaningful |
| `Promise.race` | First settles | First settles with a rejection | Timeouts, first-response-wins |
| `Promise.any` | First fulfils | All reject (`AggregateError`) | Redundant sources, fallbacks |

The trap in `Promise.all` is that it **rejects early but does not cancel**. The other promises keep running; their results are discarded, and if one of them rejects afterwards it becomes an unhandled rejection. When the operations have side effects, either use `allSettled` and decide explicitly, or pass an `AbortSignal` so the rest actually stop.

```ts
// ❌ one bad row fails the batch and hides which rows succeeded
await Promise.all(rows.map(importRow))

// ✅ partial success is visible and actionable
const results = await Promise.allSettled(rows.map(importRow))
const failed = results.flatMap((r, i) => r.status === 'rejected' ? [{ row: rows[i], reason: r.reason }] : [])
```

### Sequential vs parallel is a correctness decision, not just speed

```ts
// ❌ 3 sequential round trips for independent data
const user = await getUser(id)
const orders = await getOrders(id)
const prefs = await getPrefs(id)

// ✅ one round trip's worth of latency
const [user, orders, prefs] = await Promise.all([getUser(id), getOrders(id), getPrefs(id)])
```

But keep it sequential when a later call depends on an earlier result, or when parallelism would exceed a rate limit or a connection-pool size. Unbounded `Promise.all` over a large array is a common outage cause: 10,000 concurrent queries against a 20-connection pool.

```ts
// bounded concurrency
async function mapLimit<T, R>(items: T[], limit: number, fn: (t: T) => Promise<R>): Promise<R[]> {
  const out: R[] = new Array(items.length)
  let i = 0
  await Promise.all(Array.from({ length: Math.min(limit, items.length) }, async () => {
    while (i < items.length) {
      const idx = i++
      out[idx] = await fn(items[idx])
    }
  }))
  return out
}
```

`for await...of` over an async iterable, or a library like `p-limit`, solve the same problem.

### `await` in a loop: usually wrong, sometimes right

Right when each iteration depends on the previous one, when you are deliberately throttling, or when you are streaming and must not buffer. Wrong when the iterations are independent — that is `Promise.all` with a concurrency bound.

`forEach` never awaits:

```ts
// ❌ returns immediately; rejections become unhandled
items.forEach(async (item) => { await save(item) })

// ✅
await Promise.all(items.map(save))
```

### Cancellation is explicit in JavaScript

Promises cannot be cancelled. `AbortSignal` is the convention every modern API accepts:

```ts
const controller = new AbortController()
const timeout = setTimeout(() => controller.abort(), 5_000)
try {
  const res = await fetch(url, { signal: controller.signal })
  return await res.json()
} finally {
  clearTimeout(timeout)
}
```

`AbortSignal.timeout(ms)` does this in one call, and `AbortSignal.any([...])` combines a user cancellation with a deadline. Thread the signal all the way down — a helper that ignores it silently keeps working after the caller has given up, which is how a "cancelled" request still writes to the database.

### Errors and the missing `await`

```ts
// ❌ the try/catch never fires: the promise is returned, not awaited
try { return doWork() } catch { … }

// ❌ fire-and-forget with no rejection handler → unhandledRejection
void auditLog.write(entry)

// ✅
try { return await doWork() } catch { … }
auditLog.write(entry).catch(err => logger.error({ err }, 'audit write failed'))
```

`return await` inside a `try` is not redundant — without it the frame is popped before the rejection arrives and the `catch` is bypassed. Outside a `try`, `return promise` is fine.

Always register the process-level guard in a service:

```ts
process.on('unhandledRejection', (reason) => { logger.fatal({ reason }); process.exit(1) })
```

A process that has already lost an error should be replaced, not continued in an unknown state.

### Retries need backoff, jitter, and a predicate

```ts
async function retry<T>(fn: () => Promise<T>, { attempts = 3, base = 200 } = {}): Promise<T> {
  for (let i = 0; ; i++) {
    try { return await fn() }
    catch (err) {
      if (i >= attempts - 1 || !isRetryable(err)) throw err
      const delay = base * 2 ** i * (0.5 + Math.random())   // exponential + jitter
      await new Promise(r => setTimeout(r, delay))
    }
  }
}
```

Only retry idempotent operations, and only on transient failures — retrying a 400 or a validation error just multiplies the load. Fixed-interval retries across many clients produce a synchronised thundering herd; the jitter term is what prevents it.

### Sync-looking hazards

- `async` functions always return a promise — an `async` function passed where a sync callback is expected (`Array.sort`, `JSON.stringify` replacer) silently returns a pending promise.
- A rejected promise created but awaited later still counts as unhandled in that tick under some runtimes; create and await in the same expression where possible.
- `await` in a top-level module body is allowed in ESM and blocks the module graph — fine for config, wrong for anything slow.

## Sources

- [MDN — Using promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises)
- [MDN — Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [MDN — AbortController](https://developer.mozilla.org/en-US/docs/Web/API/AbortController)
- [Node.js — Asynchronous work](https://nodejs.org/en/learn/asynchronous-work/javascript-asynchronous-programming-and-callbacks)
- [Node.js — Event loop, timers, and nextTick](https://nodejs.org/en/learn/asynchronous-work/event-loop-timers-and-nexttick)
