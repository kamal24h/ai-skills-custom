# Reactivity Core Patterns

Choosing the right reactive primitive, deriving with `computed`, and using watchers for side effects only. Based on Vue 3.5.

## 1. Choosing a Reactive Primitive

| Primitive | Tracks | Use when |
|-----------|--------|----------|
| `shallowRef(v)` | Replacement of `.value` only | Primitives; opaque/external objects; large payloads replaced wholesale |
| `ref(v)` | Deep, through `.value` | Objects/arrays that are both replaced *and* mutated internally |
| `reactive(obj)` | Deep, property mutation | "Single state object" patterns (forms, local stores) where you mutate in place |
| `shallowReactive(obj)` | Top-level properties only | Containers whose nested payloads should stay unproxied |
| `readonly(x)` | — | Public views of state that consumers must not mutate |
| `markRaw(x)` | Never | Third-party instances, class instances, component definitions |

```ts
import { markRaw, reactive, ref, shallowReactive, shallowRef } from 'vue'

// Primitives → shallowRef (deep tracking is pure overhead)
const count = shallowRef(0)
const isOpen = shallowRef(false)

// Replaced wholesale AND mutated inside → ref
const user = ref<User | null>(null)
user.value = await api.users.me()
user.value.name = 'Ada'            // still reactive

// Mutated in place, rarely replaced → reactive
const form = reactive({ email: '', password: '', remember: false })
form.email = 'a@b.c'
// ❌ never reassign the reactive root: form = reactive({...})

// Opaque external instance → shallowRef + markRaw
const map = shallowRef<maplibregl.Map | null>(null)
onMounted(() => { map.value = markRaw(new maplibregl.Map(opts)) })

// Only top-level keys matter → shallowReactive
const cache = shallowReactive<Record<string, HugePayload>>({})
```

## 2. Reactivity Loss — The Four Classic Traps

### Trap 1 — Destructuring `reactive()`

```ts
const state = reactive({ count: 0 })
const { count } = state          // ❌ plain number, frozen in time

const { count } = toRefs(state)  // ✅ ref
```

### Trap 2 — Passing a value where a source is expected

```ts
const state = reactive({ count: 0 })

watch(state.count, cb)             // ❌ passes 0; never fires
watch(() => state.count, cb)       // ✅ getter
watch(toRef(state, 'count'), cb)   // ✅ ref
```

### Trap 3 — Refs inside collections

Refs auto-unwrap only as properties of a `reactive` object and at the top level of templates.

```ts
const list = reactive([ref(1)])
list[0] + 1        // ❌ "[object Object]1"
list[0].value + 1  // ✅

const map = reactive(new Map([['a', ref(1)]]))
map.get('a')!.value // ✅ explicit .value required
```

Nested refs in the template also do not unwrap:

```vue
{{ obj.nested }}         <!-- ❌ [object Object] if nested is a ref -->
{{ obj.nested.value }}   <!-- ✅ -->
```

### Trap 4 — Proxy identity

```ts
const raw = { id: 1 }
const proxied = reactive(raw)
proxied === raw            // false
list.includes(raw)         // false if list holds the proxy
toRaw(proxied) === raw     // true
```

Compare by id, or normalize with `toRaw()` before identity checks. External library instances should be `markRaw`'d so they are never proxied at all.

## 3. `computed` — Derive, Never Mutate

### Prefer computed over watcher-assigned refs

```ts
// ❌
const total = ref(0)
watchEffect(() => { total.value = items.value.reduce((s, i) => s + i.price, 0) })

// ✅
const total = computed(() => items.value.reduce((s, i) => s + i.price, 0))
```

### Keep getters pure

No mutation, no fetch, no storage writes, no `emit`, no logging with side effects.

```ts
// ❌
const doubled = computed(() => {
  if (count.value > 10) notify()   // side effect
  return count.value * 2
})

// ✅
const doubled = computed(() => count.value * 2)
watch(count, v => { if (v > 10) notify() })
```

### Never mutate arrays in a computed

`sort()` and `reverse()` mutate in place, corrupting the source and risking loops.

```ts
// ❌
const sorted = computed(() => items.value.sort(byName))
// ✅
const sorted = computed(() => [...items.value].sort(byName))
```

### Computed takes no parameters

```ts
// ❌
const byId = computed((id: string) => items.value.find(i => i.id === id))

// ✅ return a lookup structure
const byId = computed(() => new Map(items.value.map(i => [i.id, i])))
// usage: byId.value.get(id)

// ✅ or return a function (not memoized — fine for cheap lookups)
const findById = computed(() => (id: string) => items.value.find(i => i.id === id))
```

### Move derivation out of templates

```vue
<!-- ❌ recomputed on every render, no caching -->
<li v-for="i in items.filter(x => x.active).sort(byName)" :key="i.id">

<!-- ✅ -->
<li v-for="i in visibleItems" :key="i.id">
```

### Writable computed

```ts
const fullName = computed({
  get: () => `${first.value} ${last.value}`,
  set: (v) => { [first.value, last.value] = v.split(' ') },
})
```

### Computed return value is readonly

Mutating the result of a computed is silently discarded on the next re-evaluation. If you need to edit derived data, copy it into its own ref.

## 4. Watchers — Side Effects Only

### `watch` vs `watchEffect`

| | `watch` | `watchEffect` |
|---|---|---|
| Dependencies | Explicit source | Auto-tracked from the body |
| Old value | Available | Not available |
| Initial run | Only with `immediate: true` | Always |
| Best for | Reacting to a specific value | Effects with several implicit deps |

`watchEffect` only tracks dependencies accessed **before the first `await`**. Read every reactive dependency synchronously at the top of the callback, or use `watch` with an explicit source.

### Flush timing

```ts
watch(src, cb)                       // 'pre'  — before component re-render (default)
watch(src, cb, { flush: 'post' })    // after DOM update — use for DOM/template-ref reads
watch(src, cb, { flush: 'sync' })    // synchronous — rarely correct
watchPostEffect(cb)                  // shorthand for watchEffect + post
```

Reading a template ref or measuring the DOM in a default-flush watcher gives stale values.

### `immediate` instead of duplicated init

```ts
// ❌
onMounted(() => loadUser(userId.value))
watch(userId, loadUser)

// ✅
watch(userId, loadUser, { immediate: true })
```

### Async cleanup — cancel superseded work

```ts
const query = shallowRef('')
const results = shallowRef<Result[]>([])

watch(query, async (q, _old, onCleanup) => {
  const controller = new AbortController()
  onCleanup(() => controller.abort())

  const res = await fetch(`/api/search?q=${encodeURIComponent(q)}`, {
    signal: controller.signal,
  })
  results.value = await res.json()
})
```

Vue 3.5+ offers `onWatcherCleanup()`, usable anywhere in the synchronous part of the callback:

```ts
import { onWatcherCleanup } from 'vue'

watch(id, async (value) => {
  const controller = new AbortController()
  onWatcherCleanup(() => controller.abort())
  data.value = await load(value, controller.signal)
})
```

Without cleanup, a slow earlier request can resolve after a newer one and overwrite fresh data.

### Deep watch caveats

```ts
watch(obj, (newVal, oldVal) => {
  // newVal === oldVal — same object reference
}, { deep: true })
```

If you need the previous value, watch a derived primitive or snapshot explicitly:

```ts
watch(() => structuredClone(toRaw(obj.value)), (a, b) => { /* real diff */ }, { deep: true })
```

Deep watching large structures is expensive. Vue 3.5+ supports `deep: <number>` to limit traversal depth.

### Never create watchers asynchronously

```ts
// ❌ not bound to the component — leaks
onMounted(async () => {
  await ready()
  watch(source, cb)
})

// ✅ create it synchronously; gate the body instead
watch(source, async (v) => { await ready(); cb(v) })
```

## 5. Effect Scope

For effects created outside a component (stores, singletons, manually managed lifetimes):

```ts
import { effectScope, onScopeDispose } from 'vue'

const scope = effectScope()
scope.run(() => {
  watch(a, cb)
  watchEffect(() => { /* ... */ })
})
// later
scope.stop()   // stops every effect created inside
```

Inside a composable, `onScopeDispose()` is the general-purpose teardown hook — it works both inside components (fires on unmount) and inside manual scopes.

## 6. DOM Timing

Vue batches DOM updates. After changing state, `await nextTick()` before reading the DOM.

```ts
isOpen.value = true
await nextTick()
dialogEl.value?.focus()
```

Same-tick batching also means a watcher fires once for multiple synchronous mutations — that is intended, not a bug.

## Reactivity Decision Flow

```
Is the value a primitive?                     → shallowRef
Is it an external/class instance?              → shallowRef + markRaw
Is it derived from other state?                → computed
Do you mutate properties in place, rarely replace? → reactive
Do you replace the whole value and mutate inside?  → ref
Do only top-level keys matter?                 → shallowReactive
Is it a side effect (I/O, DOM, storage)?       → watch / watchEffect
Does it live outside a component?              → effectScope
```

## Anti-Patterns

| Anti-pattern | Consequence | Fix |
|---|---|---|
| `ref(0)` for a primitive | Needless deep-tracking overhead | `shallowRef(0)` |
| `const { x } = reactive(s)` | Reactivity lost | `toRefs(s)` |
| `watch(state.x, cb)` | Never fires | `watch(() => state.x, cb)` |
| Side effects in `computed` | Unpredictable runs, loops | Move to `watch` |
| `items.sort()` in computed | Source mutated, possible loop | `[...items].sort()` |
| Deep watch on a large tree | Traversal cost every change | Watch a narrow getter |
| Async watcher without cleanup | Stale response overwrites fresh | `onCleanup` + `AbortController` |
| `reactive()` on an SDK instance | Broken identity/private fields | `markRaw` / `shallowRef` |
| DOM read without `nextTick` | Stale or `null` | `await nextTick()` or `flush: 'post'` |

## Sources

- [Vue — Reactivity fundamentals](https://vuejs.org/guide/essentials/reactivity-fundamentals.html)
- [Vue — Reactivity in depth](https://vuejs.org/guide/extras/reactivity-in-depth.html)
- [Vue — Reactivity API](https://vuejs.org/api/reactivity-core.html)
