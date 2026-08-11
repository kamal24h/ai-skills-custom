---
name: vue-architecture-guide
description: Vue 3, Vue 2, and Nuxt architecture patterns, state management benchmarks, component quality metrics, and anti-pattern catalogue for architectural analysis.
type: reference
---

# Vue.js Architecture Guide

Reference for analyzing Vue 3, Vue 2, and Nuxt projects.

## Maturity Levels

| Level | Signals |
|-------|---------|
| **Level 1** | Vue 2 Options API, `mixins`, global event bus, jQuery or direct DOM manipulation mixed in |
| **Level 2** | Vue 3 but Options API dominant, Vuex modules, `fetch` inside components, flat `components/` folder |
| **Level 3** | `<script setup>` everywhere, composables extracted, Pinia setup stores, an API module exists |
| **Level 4** | Feature-based folders with public `index.ts`, typed contracts (`defineProps<T>`), lazy routes, `vue-tsc` in CI |
| **Level 5** | DTO→domain mapping with runtime validation, async state as discriminated unions, SSR-safe state, measured performance work, >60% component/composable test coverage |

Report the level with the evidence that placed it there — not as a score alone.

---

## Folder Structure Patterns

### Feature-Based (recommended once a feature owns more than one component)

```
src/
├── app/                    → App.vue, main.ts, providers.ts (plugin/provide wiring)
├── router/                 → index.ts, guards.ts, RouteMeta augmentation
├── shared/                 → cross-feature only; MUST NOT import from features/
│   ├── ui/                 → BaseButton.vue, BaseInput.vue, BaseModal.vue
│   ├── composables/        → useBreakpoints.ts, useClipboard.ts
│   ├── utils/              → pure functions
│   └── types/
├── lib/
│   ├── http.ts             → configured fetch/axios instance, ApiError
│   └── config.ts           → the single typed import.meta.env reader
└── features/
    └── cart/
        ├── index.ts        → public surface of the feature
        ├── api.ts          → HTTP calls + DTO→domain mapping
        ├── types.ts        → domain models
        ├── store.ts        → Pinia store (only if state is genuinely shared)
        ├── composables/    → useCart.ts
        ├── components/     → CartItemList.vue, CartSummary.vue
        └── views/          → CartView.vue (route component)
```

### Type-Based (acceptable below ~20 components, degrades after)

```
src/{components,composables,views,api,stores,router}
```

Migration trigger: a flat `components/` folder passing roughly 20 files, or two features colliding on component names.

### Nuxt Convention-Based

```
app.vue · pages/ · layouts/ · components/ · composables/ · middleware/
plugins/ · server/api/ · server/middleware/ · nuxt.config.ts
```

Nuxt's auto-import replaces explicit imports, not layering. A Nuxt project still needs feature grouping inside `components/` and `composables/` once it grows — and `server/` must stay the only place holding secrets.

### Dependency Direction

```
views  →  feature components  →  shared/ui
  ↓             ↓
feature composables / store
  ↓
feature api  →  lib/http  →  network
```

Any arrow pointing back up the chain is a finding: `shared/` importing a feature, a presentational component importing a store, `lib/http` importing domain models.

---

## Component Quality Metrics

| Metric | Healthy | Warning | Critical |
|--------|---------|---------|---------|
| SFC total lines | <150 | 150–300 | >300 |
| `<template>` lines | <60 | 60–120 | >120 |
| Props count | ≤5 | 6–8 | >8 |
| Source refs in one `setup` | ≤5 | 6–10 | >10 |
| `watch` / `watchEffect` per component | ≤2 | 3–4 | >4 |
| Props drilling depth | 1–2 | 3 | >3 |
| Route view (`*View.vue`) lines | <120 | 120–250 | >250 |
| Composable public return size | ≤6 entries | 7–10 | >10 |
| Store count for a 20-route app | 4–10 | 1–3 or 11–20 | 1 god store or >20 |

Metrics are conversation starters, not verdicts — a 200-line SFC that is one flat form may be fine; a 90-line one mixing fetching, mapping, and markup is not.

---

## State Management Selection Guide

### Match the solution to the scale

| App Scale | Recommended State Approach |
|-----------|---------------------------|
| <5 routes, no cross-route state | `ref`/`computed` in components + a shared composable |
| 5–20 routes, auth/theme/cart shared | Pinia setup stores, 1 store per domain |
| 20+ routes, heavy server data | Pinia for client state + a dedicated server-cache layer (TanStack Query / Nuxt `useAsyncData`) |
| Nuxt / SSR | Pinia with per-request instance + `useState`/`useAsyncData`; never module-scope mutables |
| Deep-tree context (theme, i18n, form context) | `provide`/`inject` with typed `InjectionKey` — not a store |

### State Type → Correct Tool Mapping

```
Server data (API responses)      → API layer + TanStack Query / useAsyncData
                                   (NOT a hand-rolled Pinia cache)
Global client state (auth/theme) → Pinia setup store
Deep-tree context                → provide/inject with InjectionKey
URL-reflected state (filters,    → route query params
page, tab, sort)
Local UI state (modal, hover)    → ref / reactive in the component
Form state                       → v-model / defineModel + a validation lib
Non-reactive instances (map,     → shallowRef / markRaw
chart, socket)
```

### Pinia Health Checks

```
1. Is any store holding fetched server data with hand-written loading/error flags?
   → HIGH: no invalidation, no dedup, no background refresh

2. Is a store destructured directly (const { items } = useCartStore())?
   → HIGH: reactivity lost — storeToRefs() required for state/getters

3. Is there a single useAppStore holding unrelated domains?
   → MEDIUM: split by domain; store boundaries should match feature boundaries

4. Is a store used for state only one component reads?
   → MEDIUM: over-centralization; keep it local

5. Are filters/pagination in a store instead of the URL?
   → MEDIUM: refresh loses state, links are not shareable

6. In SSR: is a store or reactive object created at module scope?
   → CRITICAL: state leaks across requests and users
```

---

## Data Fetching Pattern Matrix

| Pattern | Use When | Avoid When |
|---------|----------|------------|
| Feature `api.ts` + composable | Any SPA with more than a handful of endpoints | Never — this is the baseline |
| TanStack Query (`@tanstack/vue-query`) | Client-rendered, cached, refetched, deduped data | Trivial one-shot fetch on a single page |
| Nuxt `useAsyncData` / `useFetch` | Nuxt pages needing SSR-rendered data | Client-only interactive widgets |
| Nuxt `server/api/` route | Anything needing a secret, or DB access | Public data already safe to fetch client-side |
| `watch` + manual fetch | Reacting to a param change with explicit cancellation | Initial load (use the composable's own entry path) |
| `fetch` inline in an SFC | Prototype only | Any production component |

---

## Nuxt / SSR Specific Benchmarks

```ts
// ❌ Module-scope mutable state — shared by every request on the server
export const session = reactive({ user: null })

// ✅ Per-request state
export const useSession = () => useState('session', () => ({ user: null }))
```

```ts
// ❌ Non-deterministic render → hydration mismatch
<span>{{ new Date().toLocaleTimeString() }}</span>

// ✅ Render deterministically, fill in on the client
<ClientOnly><LiveClock /></ClientOnly>
```

Checklist for any SSR/Nuxt project:
- No `window`/`document`/`localStorage` access outside `onMounted` or a client guard
- `provide`/`inject`, lifecycle hooks and `defineExpose` registered synchronously before any `await`
- Secrets only in `runtimeConfig` private keys or `server/`, never in `runtimeConfig.public` or `NUXT_PUBLIC_*`
- One Pinia instance per request, not a module singleton

---

## Common Anti-Patterns

| Anti-Pattern | Signs | Impact |
|-------------|-------|--------|
| **God View** | `*View.vue` >300 lines fetching, mapping, validating and rendering | Untestable, every change is high risk |
| **Fetch in SFC** | `fetch()`/`axios` inside `<script setup>` | Duplicated error handling, untestable, no cancellation |
| **Raw DTOs everywhere** | `item.product_name` in templates | One backend rename ripples through dozens of files |
| **Store as server cache** | Pinia store with `items`, `loading`, `error` and a `fetchAll()` | Stale data, no dedup, manual invalidation bugs |
| **Store destructuring** | `const { items } = useStore()` | Silent reactivity loss — the UI simply stops updating |
| **`reactive()` destructuring** | `const { x } = reactive(obj)` | Same silent reactivity loss |
| **Prop mutation** | `props.value = …` inside a child | Overwritten on parent re-render; data flow becomes untraceable |
| **Props drilling >3 levels** | Same prop threaded through 4+ components | Fragile, resists refactoring |
| **Store in presentational component** | `BaseCard.vue` calling `useCartStore()` | Not reusable, not testable in isolation |
| **Watcher chains** | `watch(a, () => b.value = …)` cascades | Derivation expressed as imperative sequence; ordering bugs |
| **Side effects in `computed`** | API call or store write inside a getter | Runs unpredictably, re-runs on every dependency change |
| **Global mutable module state (SSR)** | Exported `reactive()` at module scope | Cross-request data leakage between users |
| **Mixed API styles** | Options API and `<script setup>` in one component; `mixins` | Two mental models, implicit name collisions |
| **Env sprawl** | `import.meta.env` read in 20 files | Untyped, unvalidated, impossible to audit |
| **Eager routes** | Every route statically imported in `router/index.ts` | Single large bundle, slow first paint |
| **Premature `v-memo`** | Memo directives with no profiling evidence | Stale renders and complexity for no measured gain |
| **`v-html` with API content** | `v-html="post.body"` | Stored XSS |

---

## Vue 2 → Vue 3 Migration Debt

When `vue@^2` or `@vue/composition-api` is present, flag these as migration blockers and rate them:

| Signal | Severity | Note |
|---|---|---|
| Vue 2 with no migration plan | HIGH | Vue 2 reached end of life; no security patches |
| `mixins` used for shared logic | HIGH | Implicit name collisions; composables are the replacement |
| Global event bus (`new Vue()` as bus) | HIGH | Untraceable data flow; no removal path for listeners |
| `Vue.filter` usage | MEDIUM | Removed in Vue 3 — must become computed/method |
| Vuex modules with heavy boilerplate | MEDIUM | Pinia setup stores are the Vue 3 path |
| `vue-class-component` decorators | MEDIUM | No Vue 3 successor; requires a rewrite per component |

## Sources

- [Vue — Scaling up](https://vuejs.org/guide/scaling-up/sfc.html)
- [Vue Style Guide](https://vuejs.org/style-guide/)
- [Pinia](https://pinia.vuejs.org/)
- [Nuxt — Directory structure](https://nuxt.com/docs/guide/directory-structure/app)
