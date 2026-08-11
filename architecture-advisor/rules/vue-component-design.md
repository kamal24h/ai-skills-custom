---
title: Vue Component Design Analysis
impact: HIGH
impactDescription: "Oversized SFCs, mutated props, and store-aware presentational components make the component tree untestable and unsafe to refactor"
tags: vue, component-design, sfc, props, emits, v-model, slots, provide-inject, route-views
---

## Vue Component Design Analysis

**Impact: HIGH (Oversized SFCs, mutated props, and store-aware presentational components make the component tree untestable and unsafe to refactor)**

A Vue component's architecture is its contract: what it accepts (props, slots, injected context), what it announces (emits, exposed methods), and what it knows about the outside world (stores, router, HTTP). Components that keep the contract narrow can be reused, tested in isolation, and moved between features. Components that reach outward — importing a store, reading route params, fetching data — are welded to one position in one app.

Analyze four things: **layer placement**, **size and responsibility**, **contract quality**, and **data flow direction**.

## Component Layers

```
Layer                  │ May know about                    │ Example
───────────────────────────────────────────────────────────────────────────
UI / presentational    │ props, emits, slots only          │ BaseButton, PriceTag
Feature component      │ feature composables / store       │ CartItemList, CartSummary
View / route component │ router, stores, feature components│ CartView
Layout                 │ slots, router outlet              │ DefaultLayout
```

A component that skips a layer — a `BaseButton` reading `useCartStore()` — is a finding regardless of its size.

## Incorrect

```vue
<!-- ❌ God view: fetching, mapping, validation, and markup in one file (300+ lines) -->
<script setup lang="ts">
const route = useRoute()
const items = ref([])
const loading = ref(false)
const error = ref(null)
const filter = ref('all')
const sortBy = ref('date')
const page = ref(1)
const showModal = ref(false)
const form = reactive({ name: '', email: '', address: '' })

onMounted(async () => {
    loading.value = true
    const res = await fetch(`/api/orders?user=${route.params.id}`)   // ❌ transport in a view
    items.value = (await res.json()).map(o => ({ ...o, total: o.unit * o.qty }))  // ❌ mapping in a view
    loading.value = false
})

function validate() { /* 40 lines of form validation */ }            // ❌ domain logic in a view
</script>

<template>
    <!-- 180 lines of markup covering list, filters, modal, and form -->
</template>
```

```vue
<!-- ❌ Prop mutation — the parent overwrites this on its next render -->
<script setup lang="ts">
const props = defineProps<{ modelValue: string }>()

function onInput(e: Event) {
    props.modelValue = (e.target as HTMLInputElement).value   // ❌ silently broken data flow
}
</script>
```

```vue
<!-- ❌ Presentational component reaching into a store — not reusable, not testable -->
<script setup lang="ts">
const cart = useCartStore()
</script>
<template><span class="price">{{ cart.total }}</span></template>
```

```vue
<!-- ❌ Untyped contract and undeclared events -->
<script setup>
defineProps(['item', 'config', 'options', 'mode', 'variant', 'size', 'theme', 'locale'])
// 8 loose props, no types; emitted events never declared, so the contract is invisible
function select() { emit('row-select', item.id) }
</script>
```

```vue
<!-- ❌ Props drilled four levels because no boundary was chosen -->
<!-- OrdersView → OrderList → OrderRow → OrderActions → OrderDeleteButton -->
<OrderList :user="user" :permissions="permissions" :locale="locale" />
```

```vue
<!-- ❌ Stored XSS -->
<template><article v-html="post.body" /></template>
```

## Correct

```vue
<!-- ✅ Thin route view: composition surface only -->
<script setup lang="ts">
import { useOrders } from '@/features/orders'
import OrderFilters from '../components/OrderFilters.vue'
import OrderList from '../components/OrderList.vue'

const route = useRoute()
const { orders, status, error } = useOrders(() => route.params.id as string)
</script>

<template>
    <OrderFilters v-model:filter="filter" />
    <OrderList v-if="status === 'success'" :orders="orders" @select="open" />
    <OrderListSkeleton v-else-if="status === 'loading'" />
    <ErrorState v-else-if="status === 'error'" :error="error" @retry="refresh" />
</template>
```

```vue
<!-- ✅ Two-way contract via defineModel (Vue 3.4+) — no prop mutation -->
<script setup lang="ts">
const model = defineModel<string>({ required: true })
</script>
<template><input v-model="model" /></template>
```

```vue
<!-- ✅ Presentational component: props in, events out, reusable anywhere -->
<script setup lang="ts">
defineProps<{ amount: number; currency?: string }>()
defineEmits<{ select: [id: string] }>()
</script>
<template><span class="price">{{ formatMoney(amount, currency) }}</span></template>
```

```ts
// ✅ Typed context instead of drilling through four levels
// shared/types/session.ts
export const sessionKey: InjectionKey<Readonly<Ref<Session>>> = Symbol('session')

// app/providers.ts
provide(sessionKey, readonly(session))

// any descendant, at any depth
const session = inject(sessionKey)!
```

## Component Design Assessment Questions

```
1. Does a *View.vue exceed 300 lines, or own fetching + mapping + markup?
   → HIGH issue: extract a composable for state, child components for UI sections

2. Is any prop assigned to inside the child?
   → HIGH issue: use defineModel or emit an event; the parent owns the value

3. Does a component in shared/ui or a purely presentational component import a store or useRoute?
   → HIGH issue: replace with props/emits so it can be reused and tested

4. Is the same prop passed through 4 or more components untouched?
   → HIGH issue: provide/inject with a typed InjectionKey, or a store for genuinely global state

5. Are props declared as an array/runtime object rather than defineProps<T>()?
   → MEDIUM issue: the contract is untyped; vue-tsc cannot verify call sites

6. Are emitted events undeclared (no defineEmits)?
   → MEDIUM issue: the outgoing contract is invisible to consumers and to type-checking

7. Does a component take more than 8 props, several of them booleans?
   → MEDIUM issue: likely two components fused; split by responsibility or group into an object prop

8. Is v-html bound to anything not provably sanitized?
   → CRITICAL issue: stored XSS

9. Are v-memo / v-once / virtualization present without any profiling evidence?
   → LOW issue: premature optimization; remove or justify with a measurement

10. Do child components reach into parent internals via ref + exposed state instead of props?
    → MEDIUM issue: inverted data flow; use props down / events up
```

## Size and Contract Metrics

```
SFC total lines          <150 healthy   │ 150–300 warning │ >300 critical
<template> lines         <60  healthy   │ 60–120 warning  │ >120 critical
Props count              ≤5   healthy   │ 6–8 warning     │ >8 critical
Source refs in setup     ≤5   healthy   │ 6–10 warning    │ >10 critical
watch/watchEffect        ≤2   healthy   │ 3–4 warning     │ >4 critical
Props drilling depth     1–2  healthy   │ 3 warning       │ >3 critical
Route view lines         <120 healthy   │ 120–250 warning │ >250 critical
```

Use the metrics to locate candidates, then judge by responsibility — a long but single-purpose form is healthier than a short component doing three jobs.

## Why

- **Testability**: A component whose only inputs are props and slots is testable by mounting it with fixtures. One that calls `useCartStore()` requires a Pinia instance, a router, and network stubs before it renders at all.
- **Reusability**: Layer discipline is what makes `shared/ui` genuinely shared. A single store import inside it ties every consumer to one feature.
- **Predictable data flow**: Props down / events up means the owner of a value is always findable. Prop mutation makes the value's source unknowable, and the mutation is silently reverted on the parent's next render.
- **Refactor safety**: Typed `defineProps<T>()` and `defineEmits<T>()` let `vue-tsc` find every call site when a contract changes. Untyped contracts push that discovery to runtime.
- **Depth cost**: Each drilling level is another file to edit for an unrelated change, and another place for the chain to break during a refactor.
- **Security**: `v-html` bypasses Vue's escaping entirely — it is the one template feature that turns API content into executable script.
