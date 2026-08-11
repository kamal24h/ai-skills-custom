---
title: Vue Data Flow & Composable Layer Analysis
impact: HIGH
impactDescription: "HTTP calls inside SFCs, raw DTOs in templates, watcher chains, and impossible async states turn data flow into an untraceable, untestable web"
tags: vue, data-flow, composables, api-layer, reactivity, computed, watchers, ssr, async-state
---

## Vue Data Flow & Composable Layer Analysis

**Impact: HIGH (HTTP calls inside SFCs, raw DTOs in templates, watcher chains, and impossible async states turn data flow into an untraceable, untestable web)**

Data flow is the path a value takes from the network to the screen and back. In a healthy Vue app that path is explicit and layered: an API module owns transport and maps DTOs to domain models, a composable owns the reactive logic, and a component renders. In an unhealthy one, `fetch` lives in `onMounted`, DTO field names leak into templates, and derived values are produced by watchers writing into other refs — so no single place explains where a value came from.

Analyze three axes: **where transport lives**, **whether composables are the logic layer**, and **how derivation is expressed**.

## The Data Flow Chain

```
component  →  composable  →  feature api.ts  →  lib/http  →  network
   ↑              ↑                ↑
 renders      owns reactive     owns transport +
              logic & lifecycle DTO→domain mapping
```

Every skipped link is a finding: a component calling `lib/http` directly, or an `api.ts` importing a store.

## Incorrect

```vue
<!-- ❌ Transport, mapping, and error handling inside the SFC -->
<script setup lang="ts">
const orders = ref([])
const loading = ref(false)
const error = ref(null)

onMounted(async () => {
    loading.value = true
    try {
        const res = await fetch(`${import.meta.env.VITE_API_URL}/orders`)
        if (!res.ok) throw new Error('failed')
        // ❌ raw DTO shape flows straight into the template
        orders.value = await res.json()
    } catch (e) {
        error.value = e
    } finally {
        loading.value = false
    }
})
</script>

<template>
    <!-- ❌ template speaks transport language, not domain language -->
    <div v-for="o in orders" :key="o.id">{{ o.customer_full_name }} — {{ o.total_amount_cents }}</div>
</template>
<!-- The same 15 lines are duplicated in six other components, each with slightly
     different error handling, and none of them cancel on unmount. -->
```

```ts
// ❌ Watcher chain expressing a derivation as an imperative sequence
const items = ref<Item[]>([])
const filtered = ref<Item[]>([])
const sorted = ref<Item[]>([])
const total = ref(0)

watch(items, v => { filtered.value = v.filter(i => i.active) })
watch(filtered, v => { sorted.value = [...v].sort(byDate) })
watch(sorted, v => { total.value = v.reduce((s, i) => s + i.price, 0) })
// Four sources of truth, three ticks of lag, and ordering bugs when any of them
// is written from elsewhere.
```

```ts
// ❌ Side effect inside a computed getter
const summary = computed(() => {
    analytics.track('summary_viewed')      // ❌ fires on every dependency change
    store.lastViewed = Date.now()          // ❌ mutation inside a getter
    return items.value.length
})
```

```ts
// ❌ Reactivity lost by destructuring a reactive object
const state = reactive({ query: '', page: 1 })
const { query, page } = state              // plain strings/numbers from here on
watch(query, …)                            // never fires
```

```ts
// ❌ Composable that is really a component in disguise
export function useOrders() {
    const route = useRoute()               // ❌ hard dependency on router position
    const store = useCartStore()           // ❌ hidden coupling to an unrelated domain
    const toast = useToast()               // ❌ side effect on UI from a data composable
    // Cannot be tested without a router, a Pinia instance, and a toast plugin.
}
```

```ts
// ❌ Parallel booleans permitting impossible states
const data = ref<Order[] | null>(null)
const loading = ref(false)
const error = ref<Error | null>(null)
// loading && error && data is representable — and will eventually render
```

```ts
// ❌ Async work with no cancellation — a stale response overwrites a newer one
watch(() => route.params.id, async id => {
    results.value = await search(id)       // requests can resolve out of order
})
```

## Correct

```ts
// ✅ Transport isolated in lib/http — knows the wire, not the domain
export class ApiError extends Error {
    constructor(readonly status: number, message: string, readonly body?: unknown) {
        super(message)
    }
}

export async function request<T>(path: string, init: RequestInit = {}): Promise<T> {
    const res = await fetch(`${config.apiUrl}${path}`, {
        ...init,
        headers: { 'Content-Type': 'application/json', ...init.headers },
        credentials: 'include',
    })
    if (!res.ok) throw new ApiError(res.status, `${init.method ?? 'GET'} ${path} failed`, await res.json().catch(() => null))
    return res.status === 204 ? (undefined as T) : res.json()
}
```

```ts
// ✅ Feature api.ts — validates at the boundary and maps DTO → domain
const orderDto = z.object({
    id: z.string(),
    customer_full_name: z.string(),
    total_amount_cents: z.number().int(),
})

function toDomain(dto: z.infer<typeof orderDto>): Order {
    return { id: dto.id, customer: dto.customer_full_name, total: dto.total_amount_cents }
}

export async function fetchOrders(): Promise<Order[]> {
    const raw = await request<unknown[]>('/orders')
    return z.array(orderDto).parse(raw).map(toDomain)
}
// A backend rename now breaks one file with a clear parse error,
// instead of rendering "undefined" in thirty templates.
```

```ts
// ✅ Composable owns reactive logic and lifecycle; inputs are refs or getters
export function useOrders(customerId: MaybeRefOrGetter<string>) {
    const state = ref<Async<Order[]>>({ status: 'idle' })

    watch(
        () => toValue(customerId),
        async (id, _old, onCleanup) => {
            const controller = new AbortController()
            onCleanup(() => controller.abort())     // ✅ stale requests cancelled
            state.value = { status: 'loading' }
            try {
                state.value = { status: 'success', data: await fetchOrders(id, controller.signal) }
            } catch (error) {
                if (!controller.signal.aborted) state.value = { status: 'error', error: error as ApiError }
            }
        },
        { immediate: true },
    )

    return { state }
}
```

```ts
// ✅ Derivation expressed as computed — one source of truth, no lag
const items = ref<Item[]>([])
const filtered = computed(() => items.value.filter(i => i.active))
const sorted = computed(() => [...filtered.value].sort(byDate))
const total = computed(() => sorted.value.reduce((s, i) => s + i.price, 0))
```

```ts
// ✅ Async state as a discriminated union — impossible states are unrepresentable
type Async<T> =
    | { status: 'idle' }
    | { status: 'loading' }
    | { status: 'success'; data: T }
    | { status: 'error'; error: ApiError }
```

```ts
// ✅ Reactivity preserved
const state = reactive({ query: '', page: 1 })
const { query, page } = toRefs(state)
```

## Data Flow Assessment Questions

```
1. Is fetch/axios called from inside any .vue file?
   → HIGH issue: no shared error handling, no cancellation, untestable

2. Do templates reference transport field names (snake_case, *_cents, *_id_fk)?
   → HIGH issue: no DTO→domain mapping; backend renames ripple across the app

3. Does any computed getter mutate state, call an API, write storage, or emit?
   → HIGH issue: getters must be pure; they re-run on every dependency change

4. Is a chain of watchers writing into other refs where computed would express it?
   → MEDIUM issue: multiple sources of truth, propagation lag, ordering bugs

5. Is a reactive() object destructured anywhere?
   → HIGH issue: silent reactivity loss — use toRefs()

6. Do async watchers/composables cancel in-flight work (onCleanup/AbortController)?
   → MEDIUM issue: out-of-order responses overwrite newer data

7. Are loading/error/data modeled as parallel booleans instead of a union?
   → MEDIUM issue: impossible states are representable and eventually render

8. Does a composable call useRoute/useStore/UI plugins internally?
   → MEDIUM issue: hidden coupling; pass values in as parameters instead

9. Are composables called conditionally, in loops, or after an await?
   → HIGH issue: lifecycle binding is lost; effects never clean up

10. Are listeners, timers, observers, and subscriptions torn down on unmount?
    → HIGH issue: memory leaks and callbacks firing into dead components

11. In SSR: are browser APIs touched outside onMounted or a client guard?
    → HIGH issue: server render crashes or hydration mismatch

12. Is the same endpoint fetched independently by several components?
    → MEDIUM issue: duplicate requests; centralize in one composable or query layer
```

## Layer Signals

```
✅ Healthy data flow:
lib/http.ts                  → single configured client, one ApiError type
features/*/api.ts            → endpoint functions returning domain models
features/*/composables/      → reactive logic, lifecycle, cancellation
components                   → render props, emit events

❌ Warning signals:
onMounted(async () => fetch(…))     → transport in the view layer
o.customer_full_name in a template  → DTO leaked to the UI
watch(a, () => b.value = …)         → derivation written as a side effect
const { x } = reactive(obj)         → reactivity dropped
useXxx() called inside if/for/await → lifecycle binding lost
no AbortController in param watchers→ race conditions on fast navigation
```

## Why

- **Single point of change**: With transport in `lib/http` and mapping in `api.ts`, an auth-header change or a field rename is a one-file edit. Spread across components, the same change is a grep-and-pray refactor.
- **Boundary validation**: Parsing responses at the API boundary converts "undefined is not an object" deep inside a template into a precise, early error naming the field that changed.
- **Domain language**: Templates that read `order.customer` instead of `order.customer_full_name` remain readable and stop coupling the UI to the backend's serialization choices.
- **Derivation vs effect**: `computed` declares *what a value is*; watchers describe *what to do when something changes*. Expressing derivation with watchers creates duplicate state that can disagree with its source for at least one tick.
- **Purity**: Computed getters may run at any time and any number of times. Side effects inside them fire unpredictably — duplicate analytics events, surprise writes, and non-reproducible bugs.
- **Cancellation**: Without `onCleanup`/`AbortController`, fast navigation lets an older response land after a newer one, and the user sees data for a record they already left.
- **Testability**: A composable that takes its inputs as parameters can be tested with plain refs. One that reaches for `useRoute()` and `useToast()` needs the whole app assembled first.
