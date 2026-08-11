# JavaScript Performance

Rate-limiting user-driven work, lazy evaluation, and the measurements that should precede any of it.

## When to Load

- A handler fires far more often than the work it triggers needs to run
- Diagnosing a slow interaction, a janky UI, or an overloaded endpoint
- Deciding whether to cache, defer, or batch an expensive computation

## Rule Categories by Priority

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | Rate limiting: debounce & throttle | MEDIUM | `perf-` |

## Rule Index

- [`perf-debounce-throttle`](../rules/perf-debounce-throttle.md) — Collapse bursts of events into the work you actually need

## Measure First

The ordering of real costs in a JavaScript application is stable and rarely matches intuition:

```
Backend:   N+1 queries → missing indexes → uncached remote calls → serialization → app CPU
Frontend:  bundle size / render blocking → excessive re-renders → layout thrash → JS execution
```

Micro-optimising a loop while a route ships 900 KB of JavaScript or issues 40 queries is effort spent in the wrong place. Tools: Node's `--cpu-prof` and `node --inspect`, Chrome DevTools Performance panel, `performance.mark`/`measure` for named spans, and a bundle analyzer for shipped weight.

Establish the number before and after. "It feels faster" is not a result.

## Key Principles

### Debounce vs throttle

They solve different problems and are routinely swapped:

| | Debounce | Throttle |
|---|---|---|
| Runs | Once, after the burst stops | At most once per interval, during the burst |
| Use for | Search-as-you-type, autosave, resize-settled, validation | Scroll position, mousemove, progress updates, rate-limited API calls |
| Risk | Never runs while input continues | Drops intermediate values |

```ts
function debounce<A extends unknown[]>(fn: (...a: A) => void, ms: number) {
  let t: ReturnType<typeof setTimeout> | undefined
  return (...args: A) => {
    clearTimeout(t)
    t = setTimeout(() => fn(...args), ms)
  }
}

function throttle<A extends unknown[]>(fn: (...a: A) => void, ms: number) {
  let last = 0
  return (...args: A) => {
    const now = Date.now()
    if (now - last >= ms) { last = now; fn(...args) }
  }
}
```

Two things production versions need that the sketches above lack:

1. **Cancellation on unmount/teardown.** A pending debounced callback firing after a component unmounts writes to dead state. Return a `cancel()` and call it in cleanup.
2. **Cancellation of the in-flight request.** Debouncing a search input still lets an earlier response land after a later one. Pair the debounce with an `AbortController` per invocation, or discard responses whose query no longer matches the current input.

For scroll and resize specifically, prefer the platform: `IntersectionObserver` and `ResizeObserver` deliver batched, off-main-thread-scheduled callbacks and make manual throttling unnecessary.

### Lazy evaluation

Do the work when the result is needed, not when the module loads:

```ts
// module-level: runs on import, on every process start
const rules = compileRules(loadRuleFile())

// lazy: runs on first use, once
let rules: Rules | undefined
const getRules = () => (rules ??= compileRules(loadRuleFile()))
```

At the module level this matters most for cold-start time in serverless and for CLI startup. In the browser the equivalent is dynamic `import()` for route-level and feature-level code splitting — the largest single lever on frontend performance, and the one that requires no algorithmic work.

Generators are the streaming form of the same idea: they compute each element on demand, so a pipeline over a large source never materialises the whole collection ([`es-generators`](../rules/es-generators.md)).

### Batching

Collapse many small operations into one round trip:

- **Database**: one `WHERE id IN (…)` instead of N lookups — the single highest-impact change in most Node services
- **DOM**: read all measurements, then write all mutations; interleaving forces synchronous layout on every switch
- **Network**: request coalescing / DataLoader-style batching per tick
- **Logs and metrics**: buffer and flush on an interval rather than per event

### Caching, briefly

Cache when the computation is expensive **and** the inputs repeat **and** staleness is acceptable. Always answer the invalidation question before adding the cache — an entry with no TTL and no invalidation path is a bug with a delay on it. See [`backend-redis-caching`](../rules/backend-redis-caching.md) for the server-side shape.

Memoisation is the in-process case and applies only to pure functions ([`func-composition`](../rules/func-composition.md)). Keyed on unbounded user input, it is a memory leak.

### Costs that are usually not the problem

Choosing between `for` and `forEach`, `Map` vs object literal for a ten-key lookup, or shaving allocations in code that runs once per request — these are measurable only in microbenchmarks. Modern engines optimise the common shapes aggressively, and readability is worth more than the difference. Optimise the loop that runs a million times, not the one that runs three.

## Sources

- [MDN — Performance API](https://developer.mozilla.org/en-US/docs/Web/API/Performance_API)
- [MDN — IntersectionObserver](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)
- [MDN — ResizeObserver](https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver)
- [Node.js — Profiling](https://nodejs.org/en/learn/getting-started/profiling)
- [web.dev — Core Web Vitals](https://web.dev/articles/vitals)
