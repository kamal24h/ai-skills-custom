# Project Architecture

Folder layout, layer boundaries, the API/service layer, and dependency direction for Vue applications.

## 1. Feature-Based Layout

Start simple; move to feature folders as soon as a feature owns more than one component.

```
src/
  app/                        # bootstrap
    App.vue
    main.ts
    providers.ts              # app.provide / plugin wiring
  router/
    index.ts
    guards.ts
    types.d.ts                # RouteMeta augmentation
  shared/                     # cross-feature, no feature imports allowed
    ui/                       # BaseButton.vue, BaseInput.vue, BaseModal.vue
    composables/              # useBreakpoints.ts, useClipboard.ts
    utils/                    # pure functions
    types/                    # cross-cutting domain types
  lib/
    http.ts                   # configured fetch/axios instance
    config.ts                 # typed import.meta.env access
  features/
    cart/
      index.ts                # public entry point of the feature
      api.ts                  # cart HTTP calls → domain models
      types.ts
      store.ts                # Pinia store (only if needed)
      composables/
        useCart.ts
      components/
        CartItemList.vue
        CartItemRow.vue
        CartSummary.vue
      views/
        CartView.vue          # route component
    checkout/
      ...
```

Small app? `src/{components,composables,views,api,stores}` is fine. Migrate to features when a flat `components/` folder passes roughly 20 files or when two features start colliding on names.

## 2. Dependency Direction

```
views  →  feature components  →  shared/ui
  ↓             ↓
feature composables / store
  ↓
feature api  →  lib/http  →  network
```

Rules:

- `shared/` must **never** import from `features/`.
- Features must never import each other's internals. Cross-feature use goes through the feature's `index.ts` public entry, a shared store, or an event/route.
- `lib/http` knows nothing about domain models; feature `api.ts` maps DTOs to domain types.
- Route views are composition surfaces — layout, wiring, composition. They are the only place that may know about both a store and the router.

```ts
// features/cart/index.ts — the feature's public surface
export { useCart } from './composables/useCart'
export { default as CartSummary } from './components/CartSummary.vue'
export type { CartItem } from './types'
```

## 3. The API Layer

Never call `fetch` from an SFC.

```ts
// lib/http.ts
import { config } from './config'

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
  if (!res.ok) {
    throw new ApiError(res.status, `${init.method ?? 'GET'} ${path} failed`, await res.json().catch(() => null))
  }
  return res.status === 204 ? (undefined as T) : res.json()
}
```

```ts
// features/cart/api.ts
import { z } from 'zod'
import { request } from '@/lib/http'
import type { CartItem } from './types'

const cartItemDto = z.object({
  id: z.string(),
  product_name: z.string(),
  unit_price: z.number(),
  qty: z.number().int(),
})

function toDomain(dto: z.infer<typeof cartItemDto>): CartItem {
  return { id: dto.id, name: dto.product_name, price: dto.unit_price, qty: dto.qty }
}

export async function fetchCart(): Promise<CartItem[]> {
  const raw = await request<unknown[]>('/cart')
  return z.array(cartItemDto).parse(raw).map(toDomain)
}
```

Why map DTOs to domain models:

- Backend field renames stop at the API layer instead of rippling through 30 components.
- Templates use domain language (`item.name`), not transport language (`item.product_name`).
- Validation at the boundary turns "undefined is not an object" deep in a template into a clear parse error.

## 4. Component Layers

| Layer | Knows about | Example |
|---|---|---|
| **UI / presentational** | Props, emits, slots only | `BaseButton`, `PriceTag`, `CartItemRow` |
| **Feature component** | Feature composables/store | `CartItemList`, `CartSummary` |
| **View / route** | Router, stores, feature components | `CartView` |
| **Layout** | Slots, router outlet | `DefaultLayout`, `AuthLayout` |

```vue
<!-- ❌ presentational component reaching into a store — no longer reusable or testable -->
<script setup lang="ts">
const cart = useCartStore()
</script>
<template><span>{{ cart.total }}</span></template>

<!-- ✅ -->
<script setup lang="ts">
defineProps<{ amount: number; currency?: string }>()
</script>
<template><span>{{ formatMoney(amount, currency) }}</span></template>
```

## 5. Domain Types

```ts
// features/cart/types.ts
export interface CartItem {
  id: string
  name: string
  price: number      // minor units
  qty: number
}

export type CartStatus = 'idle' | 'loading' | 'error'
```

- Domain types are defined by the app, not copied from the API schema.
- Model async state as a discriminated union rather than parallel booleans:
  ```ts
  type Async<T> =
    | { status: 'idle' }
    | { status: 'loading' }
    | { status: 'success'; data: T }
    | { status: 'error'; error: ApiError }
  ```
  Three independent booleans permit `loading && error && data` — an impossible state that will eventually render.

## 6. Configuration

```ts
// lib/config.ts
export const config = {
  apiUrl: import.meta.env.VITE_API_URL,
  sentryDsn: import.meta.env.VITE_SENTRY_DSN,
  isProd: import.meta.env.PROD,
} as const

if (!config.apiUrl) throw new Error('VITE_API_URL is not set')
```

- Read `import.meta.env` in exactly one place and import `config` everywhere else.
- Type the vars in `env.d.ts` (`ImportMetaEnv`).
- **Every client env value is public** — it is inlined into the bundle. Secrets belong on a server.

## 7. Cross-Cutting Concerns

### Error handling

```ts
// app/main.ts
app.config.errorHandler = (err, instance, info) => {
  reportError(err, { component: instance?.$options.name, info })
}
```

Plus `onErrorCaptured` boundaries around risky subtrees (async components, third-party widgets), and explicit error state in the async union above.

### Dependency injection for services

```ts
// shared/types/services.ts
export const analyticsKey: InjectionKey<AnalyticsClient> = Symbol('analytics')

// app/providers.ts
app.provide(analyticsKey, createAnalytics(config))

// any component/composable
const analytics = inject(analyticsKey)!
```

This makes services swappable in tests without module mocking, unlike importing a singleton directly.

### Auth

Keep session credentials in httpOnly cookies. If tokens must live in JS, keep them in memory (a store) — never `localStorage`, which is XSS-readable. Route protection lives in a global `beforeEach` guard, not in individual components.

## 8. Naming Conventions

| Thing | Convention | Example |
|---|---|---|
| Component file | PascalCase, multi-word | `UserProfileCard.vue` |
| Base/design-system component | Shared prefix | `BaseButton.vue`, `AppInput.vue` |
| Tightly coupled child | Parent prefix | `TodoListItem.vue` |
| View / route component | `*View.vue` or `views/` folder | `CartView.vue` |
| Composable | `useXxx.ts` | `useCart.ts` |
| Store | `useXxxStore` in `store.ts` | `useCartStore` |
| Pure util | camelCase function in `utils/` | `formatMoney` |
| Type/interface | PascalCase, no `I` prefix | `CartItem` |
| Injection key | `xxxKey` | `analyticsKey` |
| Event name | kebab-case in templates, camelCase in `defineEmits` | `@row-select` / `rowSelect` |

## 9. Monorepo Notes

When Vue apps share a design system:

- Ship the UI package as source `.vue` + types, and let the consuming app compile it (avoids duplicate Vue instances and lets tree-shaking work).
- Mark `vue` as a peer dependency and dedupe it in `vite.config.ts` (`resolve.dedupe: ['vue']`) — two Vue copies break `provide`/`inject` and reactivity across the boundary.
- Keep the design system free of app-specific stores, router imports, and API calls.

## Anti-Patterns

| Anti-pattern | Consequence | Fix |
|---|---|---|
| `fetch()` inside an SFC | Untestable, duplicated error handling | API layer module |
| Raw DTOs through the component tree | Backend renames ripple everywhere | Map to domain models |
| Store used in a presentational component | Not reusable, not testable | Props/emits |
| `shared/` importing a feature | Circular dependency | Invert or move the code |
| Cross-feature deep imports | Tangled coupling | Public `index.ts` entry |
| `import.meta.env` scattered everywhere | Untyped, unvalidated config | Single `config.ts` |
| Parallel `loading`/`error`/`data` booleans | Impossible states render | Discriminated union |
| Singleton service imported directly | Hard to fake in tests | `provide`/`inject` with `InjectionKey` |
| Tokens in `localStorage` | XSS-exfiltratable | httpOnly cookie or in-memory |
| Two Vue copies in a monorepo | Broken inject/reactivity | Peer dep + `resolve.dedupe` |
