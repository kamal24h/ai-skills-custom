# Composables

Designing `useXxx()` functions that are reusable, adaptable, and safe to compose. Covers naming, call-site rules, input normalization, return shape, and cleanup.

## 1. When to Extract a Composable

Extract when logic is **stateful**, **reused**, or **side-effect heavy**:

- Shared across two or more components
- Owns refs/computeds and lifecycle-bound effects
- Wraps a browser API, subscription, timer, or network resource

**Do not** extract pure functions with no reactive state — those are `utils/`, not `composables/`.

```ts
// ❌ composables/useFormatCurrency.ts
export function useFormatCurrency(n: number) { return new Intl.NumberFormat().format(n) }

// ✅ utils/format.ts
export function formatCurrency(n: number, locale = 'en-US') { /* ... */ }
```

## 2. Call-site Rules

A composable that registers lifecycle hooks or `inject()` **must** be called:
- synchronously, at the top level of `<script setup>` / `setup()`, or
- synchronously inside another composable, or
- inside an active `effectScope().run()`.

```ts
// ❌ after await — no active instance, hooks silently never fire
const data = await load()
const { x } = useThing()

// ❌ conditionally — inconsistent effect registration
if (props.enabled) { useThing() }

// ❌ inside a handler — no instance to bind to
function onClick() { useThing() }

// ✅
const { x } = useThing()
```

For conditional behavior, pass a reactive flag into the composable and branch **inside** its effects instead of branching at the call site.

## 3. Adaptable Inputs — `MaybeRef` vs `MaybeRefOrGetter`

Library-grade composables accept plain values, refs, or getters so callers never have to adapt.

```ts
type MaybeRef<T> = T | Ref<T> | ShallowRef<T> | WritableComputedRef<T>
type MaybeRefOrGetter<T> = MaybeRef<T> | ComputedRef<T> | (() => T)
```

### Policy

| Input kind | Type | Resolve with |
|---|---|---|
| Read-only, may be derived | `MaybeRefOrGetter<T>` | `toValue()` inside the effect, or `toRef()` as a watcher source |
| Must be writable (two-way) | `MaybeRef<T>` | `toRef()` → writable ref |
| May itself be a function (callback, predicate, comparator) | **plain type**, never `MaybeRefOrGetter` | — (it would be invoked as a getter) |
| DOM/element target that may be derived | `MaybeRefOrGetter<HTMLElement \| null>` | `toValue()` inside `watchEffect` |

### Read-only input

```ts
import { toRef, watch } from 'vue'
import type { MaybeRefOrGetter } from 'vue'

export function useDocumentTitle(title: MaybeRefOrGetter<string>) {
  watch(toRef(title), (t) => { document.title = t }, { immediate: true })
}

// All three call styles work:
useDocumentTitle('Dashboard')
useDocumentTitle(pageTitle)                       // ref
useDocumentTitle(() => `${user.value.name} — App`) // getter
```

### Writable input

```ts
import { toRef } from 'vue'
import type { MaybeRef } from 'vue'

export function useCounter(count: MaybeRef<number>, step = 1) {
  const countRef = toRef(count)
  return {
    count: countRef,
    inc: () => { countRef.value += step },
    dec: () => { countRef.value -= step },
  }
}
```

### `toValue()` must be called **inside** the effect

```ts
// ❌ snapshots once; never updates
export function useDouble(input: MaybeRefOrGetter<number>) {
  const v = toValue(input)
  return computed(() => v * 2)
}

// ✅ tracked on every evaluation
export function useDouble(input: MaybeRefOrGetter<number>) {
  return computed(() => toValue(input) * 2)
}
```

Same rule inside `watchEffect`:

```ts
export function useFetch(url: MaybeRefOrGetter<string>) {
  const data = shallowRef<unknown>(null)
  watchEffect(async (onCleanup) => {
    const controller = new AbortController()
    onCleanup(() => controller.abort())
    const res = await fetch(toValue(url), { signal: controller.signal }) // ✅ tracked
    data.value = await res.json()
  })
  return { data }
}
```

## 4. Return Shape — Plain Refs, Not `reactive()`

Return a plain object of refs/computeds/functions so callers can destructure freely.

```ts
// ❌ destructuring at the call site kills reactivity
return reactive({ count, double, inc })

// ✅
return { count, double, inc }
```

If a caller wants an object-style API, they can wrap it themselves with `reactive(useCounter())`.

### Expose readonly state + explicit actions

```ts
export function useSelection<T>(items: MaybeRefOrGetter<readonly T[]>) {
  const selected = shallowRef<Set<T>>(new Set())

  function toggle(item: T) {
    const next = new Set(selected.value)
    next.has(item) ? next.delete(item) : next.add(item)
    selected.value = next
  }
  function clear() { selected.value = new Set() }

  return {
    selected: readonly(selected),          // consumers cannot mutate directly
    count: computed(() => selected.value.size),
    toggle,
    clear,
  }
}
```

## 5. Options Object for Optional Parameters

```ts
export interface UseFetchOptions {
  immediate?: boolean
  retries?: number
  timeoutMs?: number
  onError?: (e: unknown) => void
}

export function useFetch<T>(
  url: MaybeRefOrGetter<string>,
  options: UseFetchOptions = {},
) {
  const { immediate = true, retries = 0, timeoutMs = 10_000, onError } = options
  // ...
}
```

Required inputs are positional; everything else goes in a single options object. This keeps the API extensible without breaking existing callers and eliminates boolean-trap arguments.

## 6. Cleanup

Every listener, timer, observer, and subscription must be released.

```ts
import { onScopeDispose, watchEffect } from 'vue'
import type { MaybeRefOrGetter } from 'vue'

export function useResizeObserver(
  target: MaybeRefOrGetter<HTMLElement | null>,
  cb: ResizeObserverCallback,   // plain type — a callback must not be a getter
) {
  let observer: ResizeObserver | null = null

  const stop = () => { observer?.disconnect(); observer = null }

  watchEffect((onCleanup) => {
    const el = toValue(target)
    if (!el) return
    observer = new ResizeObserver(cb)
    observer.observe(el)
    onCleanup(stop)
  })

  onScopeDispose(stop)          // works in components and manual effectScope
  return { stop }
}
```

`onScopeDispose()` is preferred over `onUnmounted()` in composables: it also fires when the composable runs inside a manually created `effectScope` (stores, singletons, tests).

## 7. Compose from Smaller Primitives

Build big composables out of small ones rather than one monolith.

```ts
export function useUserProfile(userId: MaybeRefOrGetter<string>) {
  const { data: user, loading, error, refresh } = useFetch<User>(
    () => `/api/users/${toValue(userId)}`,
  )
  const { isOnline } = usePresence(userId)
  const displayName = computed(() => user.value?.nickname ?? user.value?.fullName ?? '')

  return { user, displayName, isOnline, loading, error, refresh }
}
```

Each primitive stays independently testable, and the aggregate stays readable.

## 8. No Hidden Side Effects

A composable mutates only its own state, plus effects it documents (DOM, storage, network).

```ts
// ❌ silently reorders the caller's array
export function useSorted<T>(items: T[], cmp: (a: T, b: T) => number) {
  items.sort(cmp)
  return items
}

// ✅
export function useSorted<T>(
  items: MaybeRefOrGetter<readonly T[]>,
  cmp: (a: T, b: T) => number,
) {
  return computed(() => [...toValue(items)].sort(cmp))
}
```

## 9. Shared vs Per-Caller State

By default each call creates independent state. When state must be shared:

```ts
// VueUse: one instance for the whole app
export const useTheme = createSharedComposable(() => {
  const dark = useDark()
  return { dark, toggle: () => { dark.value = !dark.value } }
})

// VueUse: provide/inject-scoped shared state (SSR-safe, per subtree)
const [provideCartState, useCartState] = createInjectionState((initial: CartItem[]) => {
  const items = ref(initial)
  return { items, add: (i: CartItem) => items.value.push(i) }
})
```

**In SSR, never use a module-level singleton for per-user state.** `createSharedComposable`/`createGlobalState` are safe only for client-only or genuinely global-immutable data; otherwise use `createInjectionState` or a per-request Pinia store.

## 10. File Organization

```
src/
  composables/            # cross-feature, app-wide
    useBreakpoints.ts
    useFetch.ts
  features/
    cart/
      composables/
        useCart.ts        # feature-scoped
        useCartTotals.ts
  utils/
    format.ts             # pure functions, no reactivity
```

One composable per file, named exactly after the exported function.

## Anti-Patterns

| Anti-pattern | Consequence | Fix |
|---|---|---|
| Called after `await` / conditionally | Hooks never fire, effects leak | Call synchronously at setup top level |
| `toValue()` at composable top | Input frozen at first value | Call inside the effect |
| Returning `reactive({...})` | Destructuring breaks reactivity | Return plain refs |
| `MaybeRefOrGetter` for a callback param | Callback invoked as a getter | Use the plain function type |
| No `onScopeDispose` | Listener/timer leak, duplicate handlers | Register cleanup |
| Many positional booleans | Unreadable call sites | Options object |
| Mutating an argument | Surprising caller-side bugs | Copy and derive |
| Module singleton state in SSR | Cross-request data leak | `createInjectionState` / per-request store |
| Pure helper in `composables/` | Misleading contract | Move to `utils/` |
