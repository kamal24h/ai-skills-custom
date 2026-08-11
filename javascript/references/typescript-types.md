# TypeScript Type System

Generics, conditional and mapped types, narrowing, and the type-level patterns that make an API self-enforcing.

## When to Load

- Designing a public API signature that callers should not be able to misuse
- Writing a generic function, class, or utility type
- Replacing runtime checks with compile-time guarantees
- Fighting an inference problem or an unhelpful error message

## Rule Categories by Priority

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | Generics & inference | CRITICAL | `ts-` |
| 2 | Narrowing & unions | CRITICAL | `ts-` |
| 3 | Type-level composition | HIGH | `ts-` |
| 4 | Architectural type patterns | HIGH | `ts-pattern-` |

## Rule Index

- [`ts-generics`](../rules/ts-generics.md) — Constrained type parameters, inference sites
- [`ts-discriminated-unions`](../rules/ts-discriminated-unions.md) — A literal tag makes states exhaustively checkable
- [`ts-type-guards`](../rules/ts-type-guards.md) — `x is T` predicates and `asserts` signatures
- [`ts-conditional-types`](../rules/ts-conditional-types.md) — `T extends U ? A : B`, `infer`
- [`ts-mapped-types`](../rules/ts-mapped-types.md) — Transform every key of a type
- [`ts-template-literal-types`](../rules/ts-template-literal-types.md) — String shapes as types
- [`ts-utility-types`](../rules/ts-utility-types.md) — `Pick`, `Omit`, `Partial`, `Record`, `Awaited`
- [`ts-pattern-api-client`](../rules/ts-pattern-api-client.md) — Endpoint map → typed client
- [`ts-pattern-builder`](../rules/ts-pattern-builder.md) — Builder that tracks required fields in the type
- [`ts-pattern-event-emitter`](../rules/ts-pattern-event-emitter.md) — Event name → payload map

## Compiler Configuration Comes First

None of these patterns work under a loose config. The baseline:

```jsonc
{
  "compilerOptions": {
    "strict": true,                            // the eight strict flags as one
    "noUncheckedIndexedAccess": true,          // arr[0] is T | undefined
    "exactOptionalPropertyTypes": true,        // { a?: string } ≠ { a: string | undefined }
    "noImplicitOverride": true,
    "noFallthroughCasesInSwitch": true,
    "verbatimModuleSyntax": true,
    "isolatedModules": true
  }
}
```

`noUncheckedIndexedAccess` is the highest-value flag beyond `strict` and the one most often missing: without it, every array index and record lookup silently claims a value exists.

## Key Principles

### Discriminated unions make impossible states unrepresentable

```ts
// ❌ 8 representable combinations, 4 of them nonsense
interface State { loading: boolean; data?: User[]; error?: Error }

// ✅ exactly 4 states, each with only the fields it can have
type State =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'success'; data: User[] }
  | { status: 'error'; error: Error }
```

The payoff is exhaustiveness. Add a `'refreshing'` member and every `switch` that does not handle it becomes a compile error — provided you use the `never` check:

```ts
function assertNever(x: never): never {
  throw new Error(`Unhandled: ${JSON.stringify(x)}`)
}

switch (state.status) {
  case 'idle':    return null
  case 'loading': return <Spinner />
  case 'success': return <List items={state.data} />
  case 'error':   return <Err e={state.error} />
  default:        return assertNever(state)
}
```

The discriminant must be a **literal** type. `status: string` discriminates nothing.

### Constrain type parameters; do not over-parameterise

```ts
// ❌ T is unconstrained — nothing can be done with it inside
function pluck<T, K>(items: T[], key: K) { … }

// ✅ the constraint is what makes the body type-check and the call site safe
function pluck<T, K extends keyof T>(items: T[], key: K): T[K][] {
  return items.map(item => item[key])
}
```

Rules of thumb: a type parameter used in exactly one place is usually not needed; a parameter you find yourself asserting away inside the function was the wrong abstraction; and a generic whose constraint you cannot state is a sign the signature is doing two jobs.

### `infer` and conditional types are for library boundaries

```ts
type ElementOf<T> = T extends readonly (infer U)[] ? U : never
type Unwrap<T> = T extends Promise<infer U> ? Unwrap<U> : T
```

These are the right tool when you must derive a type from a shape you do not control (a schema, a route table, a third-party return type). They are the wrong tool for expressing something you could simply declare. Deeply nested conditional types produce error messages that no one can read; when a type becomes hard to name, that is the signal to name it.

### `unknown` over `any`, always

`any` disables checking for everything it touches and propagates silently. `unknown` accepts anything but permits nothing until narrowed — which is exactly the behavior you want at a boundary:

```ts
function parse(raw: unknown): Config {
  if (typeof raw !== 'object' || raw === null) throw new TypeError('not an object')
  // narrowing continues, or hand off to a schema validator
}
```

For real boundaries (HTTP responses, `JSON.parse`, `localStorage`, message payloads) prefer a runtime validator — Zod, Valibot, ArkType — and derive the static type from the schema with `z.infer<typeof schema>`. A hand-written `interface` over network data is an assertion, not a guarantee: it describes what you hope arrived.

### Type guards vs assertion functions

```ts
function isUser(v: unknown): v is User { … }          // returns boolean, narrows in the branch
function assertUser(v: unknown): asserts v is User { … }  // throws, narrows for the rest of the scope
```

Both are unchecked promises — TypeScript trusts the predicate body without verifying it. Keep them small and, where the shape matters, back them with a schema. An assertion function must have an explicit return type annotation; inference does not produce `asserts`.

### Mapped and template literal types

```ts
type Getters<T> = { [K in keyof T & string as `get${Capitalize<K>}`]: () => T[K] }
type Route = `/api/${string}`
type Handlers<E> = { [K in keyof E]: (payload: E[K]) => void }
```

Key remapping (`as`) is what turns a mapped type from "transform the values" into "restructure the object". Combined with a template literal it produces API surfaces that cannot be called with a typo — the `ts-pattern-event-emitter` and `ts-pattern-api-client` rules are both applications of this.

### Prefer `interface` for object contracts, `type` for everything else

`interface` supports declaration merging and gives better error messages on object shapes; `type` is required for unions, tuples, conditional and mapped types. Both are structurally typed — there is no behavioral difference for a plain object shape, so this is a consistency choice, not a correctness one.

### Nominal typing when structure is not enough

```ts
type UserId = string & { readonly __brand: 'UserId' }
const toUserId = (s: string): UserId => s as UserId
```

Two `string` IDs are interchangeable to the type system, which is how a `postId` ends up in a `getUser()` call. Branding costs one cast at the boundary and eliminates that class of bug entirely.

## Sources

- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
- [TypeScript Handbook — Narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html)
- [TypeScript Handbook — Conditional types](https://www.typescriptlang.org/docs/handbook/2/conditional-types.html)
- [TypeScript Handbook — Mapped types](https://www.typescriptlang.org/docs/handbook/2/mapped-types.html)
- [TypeScript — tsconfig reference](https://www.typescriptlang.org/tsconfig)
- [Zod](https://zod.dev/)
