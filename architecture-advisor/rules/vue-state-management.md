---
title: Vue State Management Pattern Analysis
impact: HIGH
impactDescription: "Server data cached by hand in stores, lost reactivity from destructuring, and module-scope state in SSR produce stale UIs and cross-request data leaks"
tags: vue, state-management, pinia, vuex, storetorefs, provide-inject, url-state, ssr
---

## Vue State Management Pattern Analysis

**Impact: HIGH (Server data cached by hand in stores, lost reactivity from destructuring, and module-scope state in SSR produce stale UIs and cross-request data leaks)**

Vue makes global state trivially easy — any module can export a `reactive()` object and every importer shares it. That convenience is exactly why state architecture goes wrong: state that should be local ends up global, state that belongs in the URL ends up in memory, and server data ends up hand-cached in a store with three flags and no invalidation. In SSR, the same convenience becomes a security bug, because a module-scope object is shared by every request the server handles.

## The State Classification Framework

```
State Type                      │ Right Tool
──────────────────────────────────────────────────────────────────
Server data (API responses)     │ API layer + TanStack Query /
                                │ Nuxt useAsyncData
                                │ (NOT a hand-rolled Pinia cache)
──────────────────────────────────────────────────────────────────
Global client state             │ Pinia setup store, one per domain
(auth, theme, cart)             │
──────────────────────────────────────────────────────────────────
Deep-tree context               │ provide/inject with typed
(i18n, form context, services)  │ InjectionKey — not a store
──────────────────────────────────────────────────────────────────
URL-reflected state             │ route query params
(filters, page, tab, sort)      │
──────────────────────────────────────────────────────────────────
Local UI state                  │ ref / reactive inside the component
(modal, hover, expanded)        │
──────────────────────────────────────────────────────────────────
Shared-but-not-global logic     │ a composable — not every shared
                                │ value needs a store
──────────────────────────────────────────────────────────────────
Non-reactive instances          │ shallowRef / markRaw
(chart, map, socket)            │
```

## Incorrect

```ts
// ❌ Pinia store used as a hand-written server cache
export const useProductStore = defineStore('products', () => {
    const items = ref<Product[]>([])
    const loading = ref(false)
    const error = ref<Error | null>(null)

    // ❌ no deduplication — three components mounting together fire three requests
    // ❌ no staleness policy — data is whatever the last fetch left behind
    // ❌ no invalidation — after a mutation elsewhere, this store is silently wrong
    // ❌ parallel booleans permit loading && error && items simultaneously
    async function fetchAll() {
        loading.value = true
        try {
            items.value = await (await fetch('/api/products')).json()
        } catch (e) {
            error.value = e as Error
        } finally {
            loading.value = false
        }
    }

    return { items, loading, error, fetchAll }
})
```

```ts
// ❌ Destructuring a store — reactivity is lost, the UI stops updating
const { items, total } = useCartStore()
// items and total are now plain snapshots taken at setup time
```

```ts
// ❌ Module-scope mutable state in an SSR/Nuxt app
// stores/session.ts
export const session = reactive({ user: null, token: null })
// On the server this object is created once per process.
// Request A's login writes user data that Request B renders. Cross-user leak.
```

```ts
// ❌ One god store holding unrelated domains
export const useAppStore = defineStore('app', () => {
    const user = ref(null)
    const cart = ref([])
    const products = ref([])
    const notifications = ref([])
    const sidebarOpen = ref(false)     // ❌ purely local UI state
    const currentPage = ref(1)         // ❌ belongs in the URL
    const searchFilters = ref({})      // ❌ belongs in the URL
    // 400 lines; every feature imports it; nothing can be deleted
})
```

```ts
// ❌ Filters and pagination in memory — refresh loses them, links are not shareable
const filters = ref({ category: 'all', page: 1 })
```

```ts
// ❌ A store for state exactly one component reads
export const useModalStore = defineStore('modal', () => ({ isOpen: ref(false) }))
```

## Correct

```ts
// ✅ Setup store, one domain, all state returned, actions co-located
export const useCartStore = defineStore('cart', () => {
    const items = ref<CartItem[]>([])

    const total = computed(() =>
        items.value.reduce((sum, i) => sum + i.price * i.qty, 0),
    )

    function add(item: CartItem) {
        const existing = items.value.find(i => i.id === item.id)
        if (existing) existing.qty += item.qty
        else items.value.push(item)
    }

    return { items, total, add }
})
```

```ts
// ✅ storeToRefs for state and getters; actions come off the store directly
const cartStore = useCartStore()
const { items, total } = storeToRefs(cartStore)   // stay reactive
const { add } = cartStore                          // actions are bound, safe to destructure
```

```ts
// ✅ Server data through a query layer — dedup, staleness, invalidation handled
const { data: products, isPending, error } = useQuery({
    queryKey: ['products'],
    queryFn: fetchProducts,          // from features/products/api.ts
    staleTime: 5 * 60 * 1000,
})
```

```ts
// ✅ SSR-safe per-request state (Nuxt)
export const useSession = () => useState<Session | null>('session', () => null)

// ✅ SSR-safe Pinia — one instance per request, created in the app factory
export function createApp() {
    const app = createSSRApp(App)
    app.use(createPinia())    // per request, never a module singleton
    return app
}
```

```ts
// ✅ URL as the source of truth for filters and pagination
const route = useRoute()
const router = useRouter()

const page = computed(() => Number(route.query.page ?? 1))
const category = computed(() => (route.query.category as string) ?? 'all')

function setCategory(value: string) {
    router.replace({ query: { ...route.query, category: value, page: 1 } })
}
// Survives refresh, supports the back button, and links are shareable.
```

```ts
// ✅ provide/inject for deep-tree context — no global store needed
export const themeKey: InjectionKey<Readonly<Ref<Theme>>> = Symbol('theme')
provide(themeKey, readonly(theme))
```

## State Management Assessment Questions

```
1. Is any store created at module scope in an SSR/Nuxt app (exported reactive/ref)?
   → CRITICAL issue: state leaks across requests and users

2. Does a store hold fetched server data with hand-written loading/error flags?
   → HIGH issue: no dedup, no staleness policy, no invalidation — move to a query layer

3. Is any store destructured without storeToRefs()?
   → HIGH issue: silent reactivity loss; the UI stops reflecting state changes

4. Is there a single god store holding unrelated domains?
   → MEDIUM issue: split by domain so store boundaries match feature boundaries

5. Are filters, pagination, tabs, or sort order kept in a store or component state?
   → MEDIUM issue: move to route query params

6. Does a store exist for state only one component reads?
   → MEDIUM issue: keep it local; a store is a coupling decision, not a default

7. Is deep-tree context (theme, i18n, form context) implemented as a global store?
   → MEDIUM issue: provide/inject with a typed InjectionKey scopes it correctly

8. Is Vuex still in use in a Vue 3 project?
   → MEDIUM issue: migration debt — Pinia setup stores are the supported path

9. Do actions mutate state belonging to another store directly?
   → MEDIUM issue: cross-store writes; call the owning store's action instead

10. Are auth tokens kept in localStorage?
    → HIGH issue: XSS-readable; use httpOnly cookies or in-memory store state
```

## Store Health Signals

```
✅ Healthy state architecture:
features/cart/store.ts        → one store, one domain, colocated with the feature
storeToRefs(store)            → at every destructuring call site
computed getters              → derived values are never stored twice
route.query                   → filters, page, sort live in the URL
createPinia() per request     → SSR-safe instance lifecycle

❌ Warning signals:
stores/index.ts exporting 1 store per view   → stores mirror screens, not domains
store.items = await fetch(...)               → server cache built by hand
export const state = reactive({})            → module-scope mutable state
const { x } = useStore()                     → reactivity dropped on the floor
localStorage.setItem('token', …)             → XSS-exfiltratable credentials
```

## Why

- **Cache correctness**: A query layer handles deduplication, staleness, background refresh, and invalidation. A store with `items`/`loading`/`error` reimplements a fraction of that and gets the rest wrong — usually as stale data after a mutation elsewhere in the app.
- **Reactivity is not free**: `storeToRefs` exists because destructuring reads `.value` once. The failure mode is silent — no error, no warning, just a UI that stops updating, which is expensive to diagnose later.
- **Request isolation**: On a server, a module is evaluated once per process while requests arrive concurrently. Module-scope state therefore belongs to every user at once — a data-leak class of bug, not a style issue.
- **Scope discipline**: State placed globally is state every feature may now depend on. Keeping local state local and context in `provide`/`inject` preserves the option to delete or move a feature.
- **URL as state**: Filters and pagination in the URL make pages refreshable, bookmarkable, shareable, and back-button correct — for free, by using a store that already exists in the browser.
- **Domain boundaries**: Stores split by domain can be deleted with their feature. A god store outlives every feature it serves and accumulates state nobody dares remove.
