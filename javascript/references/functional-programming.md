# Functional Programming in JavaScript

Array methods, composition, purity, and immutability — applied pragmatically, not dogmatically.

## When to Load

- Reviewing a chain of array transformations, or a loop that could be one
- Extracting reusable transformation logic
- Diagnosing a bug caused by shared mutable state
- Deciding whether a value should be copied or mutated

## Rule Categories by Priority

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | Purity & immutability | HIGH | `func-` |
| 2 | Array transformations | HIGH | `func-` |
| 3 | Composition | HIGH | `func-` |

## Rule Index

- [`func-pure-immutability`](../rules/func-pure-immutability.md) — Same input, same output, no side effects
- [`func-array-methods`](../rules/func-array-methods.md) — `map`/`filter`/`reduce`/`flatMap` over manual loops
- [`func-composition`](../rules/func-composition.md) — Small functions combined, currying, memoisation

## Key Principles

### Purity is a testability property

```ts
// ❌ impure: reads global state, mutates its input, depends on the clock
function applyDiscount(cart) {
  cart.total = cart.total * (1 - CURRENT_CAMPAIGN.rate)
  cart.appliedAt = Date.now()
  return cart
}

// ✅ pure: everything it needs is a parameter, nothing outside changes
function applyDiscount(cart: Cart, rate: number, now: Date): Cart {
  return { ...cart, total: cart.total * (1 - rate), appliedAt: now }
}
```

The pure version needs no setup, no mocks, and no cleanup to test — that is the whole return on the discipline. It is also safe to call twice, to call in parallel, and to memoise.

Side effects have to happen somewhere. The goal is to concentrate them at the edges (I/O, persistence, logging) and keep the decision-making core pure, not to eliminate them.

### Which array method

| Intent | Method |
|---|---|
| Same length, transformed values | `map` |
| Fewer items, same shape | `filter` |
| Many items → one value | `reduce` |
| Map then flatten one level | `flatMap` |
| Does any / do all match | `some` / `every` |
| First match | `find` / `findIndex` |
| Side effect only | `for...of` (not `forEach`) |

`map` used for side effects and `forEach` used to build an array are both misuse — they mislead the reader about what the block does. `for...of` is the honest choice for genuine side effects, and it supports `await`, `break`, and `continue`, which `forEach` does not.

### `reduce` has a readability ceiling

```ts
// ✅ clear
const total = items.reduce((sum, i) => sum + i.price * i.qty, 0)

// ❌ a reduce building a nested object with conditionals inside — write the loop
const grouped = items.reduce((acc, i) => { … 12 lines … }, {} as Record<string, Item[]>)
```

For grouping specifically, `Object.groupBy` / `Map.groupBy` express the intent directly where available. Beyond simple accumulation, an explicit `for...of` with a named accumulator is usually easier to read and to debug than a dense `reduce`.

Chaining `.filter().map().filter()` over a large array iterates it repeatedly. That is irrelevant for hundreds of items and matters for hundreds of thousands — measure before collapsing a readable chain into one pass.

### Immutability, and its cost

```ts
const next = { ...state, user: { ...state.user, name } }     // shallow copies at each level
const list = [...items.slice(0, i), updated, ...items.slice(i + 1)]
```

Spread is shallow: `{...state}` copies the top level and shares every nested object. For deep updates either spread each level explicitly (as above), use `structuredClone` for a genuine deep copy, or use a library like Immer that produces the copy from mutable-looking code.

Newer non-mutating array methods remove a category of accidental mutation: `toSorted`, `toReversed`, `toSpliced`, and `with` return new arrays where `sort`, `reverse`, `splice` mutate in place. `sort()` mutating the original is a classic source of "why did the props array change".

Immutability is not free. Copying a large structure on every keystroke is a real cost; local mutation inside a function that owns the value and returns a fresh result is perfectly fine:

```ts
function buildIndex(rows: Row[]): Map<string, Row> {
  const index = new Map<string, Row>()      // local mutation, no external visibility
  for (const row of rows) index.set(row.id, row)
  return index
}
```

### Composition and currying

```ts
const pipe = <T>(...fns: Array<(x: T) => T>) => (x: T) => fns.reduce((v, f) => f(v), x)

const normaliseEmail = pipe<string>(s => s.trim(), s => s.toLowerCase())
```

Composition pays off when the steps are genuinely reusable and each has a name worth reading. A `pipe` of three anonymous arrow functions used once is harder to read than three sequential statements — and worse in a stack trace, since the frames are unnamed.

Currying is useful where the language pushes you toward it — partially applying a config to get a reusable handler:

```ts
const withRetry = (attempts: number) => <T>(fn: () => Promise<T>) => retry(fn, { attempts })
const retryTwice = withRetry(2)
```

Point-free style (`items.map(toUser)` rather than `items.map(x => toUser(x))`) is good until it hides an arity mismatch: `['1','2','3'].map(parseInt)` returns `[1, NaN, NaN]` because `map` passes the index as the radix. When in doubt, write the arrow.

### Memoisation

```ts
function memoise<A, R>(fn: (a: A) => R): (a: A) => R {
  const cache = new Map<A, R>()
  return (a) => cache.has(a) ? cache.get(a)! : (cache.set(a, fn(a)), cache.get(a)!)
}
```

Only correct for pure functions — memoising anything that reads mutable state or the clock caches a stale answer forever. An unbounded `Map` keyed on user input is a memory leak; bound the size or use a `WeakMap` when the key is an object whose lifetime should govern the entry.

## Sources

- [MDN — Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [MDN — Array.prototype.reduce](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)
- [MDN — structuredClone](https://developer.mozilla.org/en-US/docs/Web/API/Window/structuredClone)
- [MDN — Object.groupBy](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/groupBy)
- [Immer](https://immerjs.github.io/immer/)
