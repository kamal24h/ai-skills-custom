# ES6+ Features

Modern syntax, module semantics, optional chaining, and generators — with the sharp edges each one has.

## When to Load

- Modernising legacy JavaScript (`var`, `require`, callback style)
- Configuring or debugging module resolution (ESM vs CommonJS)
- Reviewing destructuring, spread, or optional-chaining usage
- Implementing lazy or streaming iteration

## Rule Categories by Priority

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | Module system | MEDIUM | `es-` |
| 2 | Modern syntax | MEDIUM | `es-` |
| 3 | Optional chaining & nullish | MEDIUM | `es-` |
| 4 | Generators & iteration | MEDIUM | `es-` |

## Rule Index

- [`es-modules`](../rules/es-modules.md) — ESM imports/exports, resolution, interop
- [`es-modern-syntax`](../rules/es-modern-syntax.md) — `const`/`let`, destructuring, spread, template literals
- [`es-optional-chaining`](../rules/es-optional-chaining.md) — `?.` and `??` with their precise semantics
- [`es-generators`](../rules/es-generators.md) — `function*`, `yield`, async iteration

## Key Principles

### `??` is not `||`

```ts
const port = config.port ?? 3000        // only null/undefined fall through
const port = config.port || 3000        // 0 also falls through — a real bug
```

`||` treats every falsy value as absent: `0`, `''`, `false`, `NaN`. That is almost never what a config default means. Use `??` for "not provided" and `||` only when you genuinely want "falsy". `??=`, `||=`, and `&&=` follow the same distinction.

`??` cannot be mixed with `||`/`&&` without parentheses — a deliberate syntax error, because the precedence would be ambiguous.

### `?.` short-circuits the whole chain

```ts
user?.profile.avatar.url      // if user is null → undefined, no error on the rest
user?.save?.()                // calls only if both exist
list?.[0]                     // optional index access
```

Two failure modes to watch for:

1. **Silencing a real invariant.** `order?.total` where `order` must exist turns a loud bug into `undefined` flowing downstream. Optional chaining is for values that are genuinely optional, not for suppressing errors you have not understood.
2. **Assignment.** `a?.b = c` is invalid — optional chaining cannot be an assignment target.

### `const` by default, `let` when reassigned, never `var`

`var` is function-scoped and hoisted, which produces the classic closure-in-a-loop bug and lets a variable be used before its declaration line. `const` does not make the value immutable — it prevents rebinding. `const arr = []` still permits `arr.push()`.

### Destructuring: defaults apply to `undefined` only

```ts
const { retries = 3 } = options          // null does NOT trigger the default
const { a: { b } = {} } = input          // guard nested destructuring or it throws on undefined
const [first, ...rest] = items
function f({ id, name = 'anon' }: Args) {}
```

Destructuring a `null` throws `TypeError`. Nested destructuring of possibly-absent objects needs a default at each level, which gets unreadable quickly — beyond one level, prefer explicit access with `?.`.

Rest in object destructuring is the clean way to omit a field: `const { password, ...safe } = user`.

### ESM vs CommonJS

| | ESM | CommonJS |
|---|---|---|
| Syntax | `import` / `export` | `require` / `module.exports` |
| Resolution | Static, at parse time | Dynamic, at call time |
| Extensions | Required in relative paths (`./x.js`) | Optional |
| `__dirname` | Not defined — use `import.meta.dirname` | Defined |
| Top-level `await` | Allowed | Not allowed |
| Loading CJS | `import` a CJS module works (default export) | `require()` of ESM works in current Node; historically did not |

Enable ESM with `"type": "module"` in `package.json`, or use the `.mjs` extension. The most common migration errors: forgetting the file extension in relative imports (ESM does not resolve `./utils` to `./utils.js`), and named imports from a CommonJS package — CJS interop exposes the module as a default export, and named bindings are only detected heuristically.

In TypeScript, set `"verbatimModuleSyntax": true` so emitted imports match what you wrote, and use `import type { X }` for type-only imports to guarantee erasure.

Prefer static imports. `import()` is for genuine lazy loading (route-level code splitting, optional heavy dependencies) — using it to break a circular dependency hides a design problem rather than fixing it.

### Generators: lazy sequences and streaming

```ts
function* chunk<T>(items: Iterable<T>, size: number): Generator<T[]> {
  let buf: T[] = []
  for (const item of items) {
    buf.push(item)
    if (buf.length === size) { yield buf; buf = [] }
  }
  if (buf.length) yield buf
}
```

Generators produce values on demand, so an infinite or very large sequence costs constant memory. They are consumed once — after iteration the generator is done, and it has no `length` and no random access.

Async generators are the idiomatic way to consume paginated APIs and streams:

```ts
async function* allPages(url: string) {
  let next: string | null = url
  while (next) {
    const page = await fetch(next).then(r => r.json())
    yield* page.items
    next = page.nextUrl
  }
}

for await (const item of allPages('/api/orders')) { … }
```

`yield*` delegates without buffering, which keeps a pipeline of generators lazy end to end. Node streams are async-iterable, so `for await...of` works directly on a file or socket read stream.

### Other modern syntax worth defaulting to

- Template literals over concatenation; tagged templates for escaping-sensitive interpolation
- `Object.entries`/`fromEntries` for object↔array conversion
- `Array.from({ length: n }, (_, i) => …)` over `new Array(n).fill()` gymnastics
- `at(-1)` for the last element
- Class fields and `#private` members over closure-based privacy in classes
- `structuredClone` over `JSON.parse(JSON.stringify(x))`, which loses `Date`, `Map`, `Set`, `undefined`, and throws on cycles

## Sources

- [MDN — JavaScript reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference)
- [MDN — JavaScript modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
- [MDN — Optional chaining](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining)
- [MDN — Iterators and generators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators)
- [Node.js — Modules: ECMAScript modules](https://nodejs.org/api/esm.html)
- [TypeScript — Modules reference](https://www.typescriptlang.org/docs/handbook/modules/reference.html)
