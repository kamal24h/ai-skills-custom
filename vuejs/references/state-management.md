# State Management

Choosing where state lives, Pinia setup stores, lightweight alternatives, and SSR-safe state.

## 1. Choose the Lightest Approach

Escalate only when the current level stops working:

| Level | Mechanism | Use when |
|---|---|---|
| 1 | `ref`/`reactive` in the component | State used by one component |
| 2 | Lift to the nearest common parent, pass props | Two or three nearby components |
| 3 | Composable (`useXxx`) instance per caller | Reusable logic, independent state |
| 4 | URL query params | Filters, sort, page, tab — must survive refresh and be shareable |
| 5 | `provide`/`inject` with `InjectionKey` | Deep-tree context scoped to a subtree (form, theme, table config) |
| 6 | `createInjectionState` (VueUse) | Shared state scoped to a subtree, SSR-safe |
| 7 | Pinia store | Cross-feature state, needs DevTools/persistence/plugins |

Do not reach for Pinia because "the app is big". Reach for it when state genuinely crosses feature boundaries or needs store-level tooling.

## 2. URL as State

Ephemeral, shareable UI state belongs in the URL — it survives refresh, supports the back button, and is linkable.

```ts
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

const page = computed({
  get: () => Number(route.query.page ?? 1),
  set: (v) => router.replace({ query: { ...route.query, page: String(v) } }),
})

const status = computed({
  get: () => (route.query.status as string) ?? 'all',
  set: (v) => router.replace({ query: { ...route.query, status: v || undefined } }),
})
```

Use `replace` for filter changes (no history spam) and `push` for navigations the user should be able to go back from.

## 3. Pinia Setup Stores

```ts
// stores/cart.ts
import { defineStore } from 'pinia'

export const useCartStore = defineStore('cart', () => {
  // state
  const items = ref<CartItem[]>([])
  const status = ref<'idle' | 'loading' | 'error'>('idle')

  // getters
  const count = computed(() => items.value.reduce((n, i) => n + i.qty, 0))
  const total = computed(() => items.value.reduce((n, i) => n + i.qty * i.price, 0))
  const isEmpty = computed(() => items.value.length === 0)

  // actions
  function add(product: Product, qty = 1) {
    const existing = items.value.find(i => i.id === product.id)
    if (existing) existing.qty += qty
    else items.value.push({ ...product, qty })
  }

  function remove(id: string) {
    items.value = items.value.filter(i => i.id !== id)
  }

  async function checkout() {
    status.value = 'loading'
    try {
      await api.cart.checkout(items.value)
      items.value = []
      status.value = 'idle'
    } catch (e) {
      status.value = 'error'
      throw e
    }
  }

  // ⚠️ MUST return every ref/computed the store owns
  return { items, status, count, total, isEmpty, add, remove, checkout }
})
```

**Everything must be returned.** State not returned from a setup store is invisible to DevTools, is not serialized during SSR, is not reset by `$reset`, and is unreachable by plugins (persistence, undo).

If you need a genuinely private value, keep it outside the store or accept that it is untracked — do not assume Pinia "handles" unreturned refs.

## 4. Consuming a Store

```ts
import { storeToRefs } from 'pinia'

const cart = useCartStore()

// ❌ reactivity lost — these are plain snapshots
const { items, total } = cart

// ✅ state and getters
const { items, total, isEmpty } = storeToRefs(cart)

// ✅ actions are plain functions; destructure them or call off the store
const { add, remove } = cart
```

In templates, calling through the store object is clearest:

```vue
<button @click="cart.remove(item.id)">Remove</button>
```

### `getActivePinia` errors

```ts
// ❌ module top level — Pinia is not installed yet
const auth = useAuthStore()
router.beforeEach(() => { if (!auth.user) ... })

// ✅ call inside the guard
router.beforeEach(() => {
  const auth = useAuthStore()
  if (!auth.user) return { name: 'login' }
})
```

Call `useXStore()` inside setup, a component method, a guard/handler callback, or anywhere after `app.use(pinia)`.

## 5. Store Composition & Granularity

```ts
export const useCheckoutStore = defineStore('checkout', () => {
  const cart = useCartStore()          // stores can use other stores
  const auth = useAuthStore()

  const canCheckout = computed(() => !cart.isEmpty && auth.isAuthenticated)
  return { canCheckout }
})
```

- One store per domain concept: `auth`, `cart`, `catalog`, `notifications`.
- Not one god `mainStore`, and not one store per component.
- Watch for circular store dependencies — extract shared logic into a composable both stores use.

### Other store APIs

```ts
cart.$patch({ status: 'idle' })                 // batched update
cart.$patch(s => { s.items.push(item) })        // function form for collections
cart.$reset()                                   // option stores only; setup stores need a manual reset action
cart.$subscribe((mutation, state) => persist(state))
cart.$onAction(({ name, after, onError }) => { /* logging, analytics */ })
```

Setup stores have no automatic `$reset` — expose your own:

```ts
function $reset() { items.value = []; status.value = 'idle' }
return { items, status, /* ... */ $reset }
```

## 6. Lightweight Global State Without Pinia

### Client-only global singleton

```ts
// VueUse
import { createGlobalState } from '@vueuse/core'

export const useThemeState = createGlobalState(() => {
  const dark = ref(false)
  return { dark, toggle: () => { dark.value = !dark.value } }
})
```

Simple and dependency-light, but it is a **module singleton** — unsafe for SSR per-user data.

### Subtree-scoped shared state (SSR-safe)

```ts
import { createInjectionState } from '@vueuse/core'

const [provideCounter, useCounter] = createInjectionState((initial: number) => {
  const count = ref(initial)
  return { count, inc: () => count.value++ }
})

export { provideCounter, useCounter }
```

The provider component calls `provideCounter(0)`; descendants call `useCounter()`. State lives on the component tree, so each SSR request gets its own.

## 7. Never Export Mutable Module State

```ts
// ❌ shared by every request on a server; leaks user data across users
export const currentUser = ref<User | null>(null)
export const cart = reactive<CartItem[]>([])
```

Even in a pure SPA this is worth avoiding: it is untestable in isolation, invisible in DevTools, and has no defined reset point. In SSR/Nuxt it is a security bug.

```ts
// ✅ factory + provide, or a Pinia store created per request
export function createUserState() {
  const user = ref<User | null>(null)
  return { user, set: (u: User) => { user.value = u } }
}
```

## 8. SSR State

```ts
// server entry — one Pinia per request
export async function render(url: string) {
  const app = createSSRApp(App)
  const pinia = createPinia()
  app.use(pinia)
  app.use(createRouter(/* per-request router too */))

  const html = await renderToString(app)
  const state = JSON.stringify(pinia.state.value)   // serialize
  return { html, state }
}
```

```ts
// client entry — hydrate
const pinia = createPinia()
if (window.__PINIA__) pinia.state.value = window.__PINIA__
app.use(pinia)
```

Serialize with a safe stringifier (`devalue`) rather than raw `JSON.stringify` interpolated into HTML — otherwise `</script>` in data breaks the page and enables injection.

In Nuxt, `useState()` and Pinia via `@pinia/nuxt` handle this for you; the rule that survives is: **no module-level mutable state**.

## 9. Persistence

```ts
// Simple, explicit
const items = useLocalStorage<CartItem[]>('cart:items', [])  // VueUse, SSR-aware

// Or a Pinia plugin
pinia.use(({ store }) => {
  const saved = localStorage.getItem(`pinia:${store.$id}`)
  if (saved) store.$patch(JSON.parse(saved))
  store.$subscribe((_m, state) => {
    localStorage.setItem(`pinia:${store.$id}`, JSON.stringify(state))
  })
})
```

Never persist tokens or PII to `localStorage` in a browser app — use httpOnly cookies for session credentials.

## Anti-Patterns

| Anti-pattern | Consequence | Fix |
|---|---|---|
| Pinia for state used by one component | Indirection with no benefit | Local `ref` |
| Setup store not returning all state | Broken DevTools/SSR/plugins | Return everything |
| `const { x } = useStore()` | Reactivity lost | `storeToRefs()` |
| `useStore()` at module top level | "no active Pinia" error | Call inside setup/handler |
| One god `mainStore` | Untestable, coupled | One store per domain |
| Exported mutable module state | Cross-request leak in SSR | Factory / store / injection state |
| Shared `pinia` across SSR requests | User data leak | `createPinia()` per request |
| Filters in a store | Lost on refresh, unshareable | URL query params |
| Raw `JSON.stringify` for SSR payload | XSS via `</script>` | `devalue` |
| Tokens in `localStorage` | XSS-exfiltratable | httpOnly cookies |
