---
title: Vue Project Structure Analysis
impact: HIGH
impactDescription: "Flat layouts, cross-feature coupling, and scattered configuration make Vue codebases resist refactoring and hide their real dependency graph"
tags: vue, project-structure, feature-folders, layering, nuxt, configuration, code-splitting
---

## Vue Project Structure Analysis

**Impact: HIGH (Flat layouts, cross-feature coupling, and scattered configuration make Vue codebases resist refactoring and hide their real dependency graph)**

Vue imposes almost no structure of its own — `createApp` works with any folder layout, and Nuxt's auto-import hides where things come from. That freedom means the architecture lives entirely in convention. Projects that never make the convention explicit end up with a 40-file `components/` folder, features importing each other's internals, and `import.meta.env` read in twenty places.

Structure analysis answers three questions: **where does code live**, **which direction do dependencies point**, and **what is the public surface of each unit**.

## Incorrect

```
// ❌ Flat type-based layout at scale — nothing indicates feature boundaries

src/
├── components/           → 47 .vue files, alphabetical, no grouping
│   ├── CartItem.vue
│   ├── CheckoutForm.vue
│   ├── OrderRow.vue
│   ├── ProductCard.vue
│   └── … 43 more
├── views/                → 18 route components, several over 300 lines
├── composables/          → useCart.ts, useOrders.ts, useAuth.ts, useUtils.ts
├── stores/               → one store per view, plus a god useAppStore
└── main.ts               → fetch() calls and env reads inline

// Nothing here tells you which files belong to "checkout".
// Deleting a feature means grepping for its name across five folders.
```

```ts
// ❌ Cross-feature deep import — bypasses any public surface
import { normalizeCartItem } from '@/features/cart/composables/internal/mapping'
//                                                    ^ internal helper, now a de-facto public API

// ❌ shared/ importing a feature — inverted dependency, circular risk
// src/shared/ui/PriceTag.vue
import { useCartStore } from '@/features/cart/store'
```

```ts
// ❌ Environment access scattered across the codebase
// api/user.ts
fetch(`${import.meta.env.VITE_API_URL}/users`)
// api/orders.ts
fetch(`${import.meta.env.VITE_API}/orders`)   // typo, undefined at runtime
// components/Analytics.vue
const key = import.meta.env.VITE_ANALYTICS_KEY ?? ''   // silently empty in prod
```

```ts
// ❌ Every route statically imported — one bundle for the whole app
import CartView from '@/views/CartView.vue'
import CheckoutView from '@/views/CheckoutView.vue'
import AdminDashboardView from '@/views/AdminDashboardView.vue'   // 400 KB of charts

const routes = [
    { path: '/cart', component: CartView },
    { path: '/checkout', component: CheckoutView },
    { path: '/admin', component: AdminDashboardView },
]
```

## Correct

```
// ✅ Feature-based layout with explicit boundaries

src/
├── app/
│   ├── App.vue
│   ├── main.ts
│   └── providers.ts          → app.provide / plugin wiring in one place
├── router/
│   ├── index.ts              → lazy route definitions
│   ├── guards.ts             → global beforeEach logic
│   └── types.d.ts            → RouteMeta augmentation
├── shared/                   → cross-feature only; MUST NOT import features/
│   ├── ui/                   → BaseButton.vue, BaseInput.vue, BaseModal.vue
│   ├── composables/          → useBreakpoints.ts, useClipboard.ts
│   ├── utils/                → pure functions
│   └── types/
├── lib/
│   ├── http.ts               → configured client + ApiError
│   └── config.ts             → the single typed import.meta.env reader
└── features/
    ├── cart/
    │   ├── index.ts          → public surface — the only legal import path
    │   ├── api.ts
    │   ├── types.ts
    │   ├── store.ts
    │   ├── composables/
    │   ├── components/
    │   └── views/
    └── checkout/
```

```ts
// ✅ Feature public surface — internals stay internal
// features/cart/index.ts
export { useCart } from './composables/useCart'
export { default as CartSummary } from './components/CartSummary.vue'
export type { CartItem } from './types'

// consumer
import { useCart, type CartItem } from '@/features/cart'
```

```ts
// ✅ One typed, validated configuration module
// lib/config.ts
export const config = {
    apiUrl: import.meta.env.VITE_API_URL,
    sentryDsn: import.meta.env.VITE_SENTRY_DSN,
    isProd: import.meta.env.PROD,
} as const

if (!config.apiUrl) throw new Error('VITE_API_URL is not set')
// Fails at boot with a clear message instead of producing "undefined/users" requests.
```

```ts
// ✅ Route-level code splitting
const routes = [
    { path: '/cart', component: () => import('@/features/cart/views/CartView.vue') },
    { path: '/admin', component: () => import('@/features/admin/views/DashboardView.vue') },
]
```

## Structure Compliance Assessment

```
CRITICAL violations:
├── secrets present in client env vars (VITE_*, runtimeConfig.public) — every client env value ships in the bundle
├── circular imports between features (a → b → a), or shared/ ↔ features/ cycles
└── SSR/Nuxt app with secret-bearing logic outside server/ (server routes or private runtimeConfig)

HIGH violations:
├── shared/ or lib/ importing from features/ — inverted dependency direction
├── cross-feature deep imports bypassing the feature's index.ts public surface
├── no API/service layer — HTTP calls issued directly from SFCs (see vue-data-flow)
└── >20 components in a flat components/ folder with no feature grouping

MEDIUM violations:
├── every route statically imported — no route-level code splitting
├── Options API and Composition API mixed in the same component, or mixins in new code
├── import.meta.env read in more than one module instead of a typed config module
├── vue-tsc --noEmit missing from CI in a TypeScript project
└── path aliases undefined — deep relative chains (../../../shared/ui) throughout

LOW violations:
├── inconsistent component file naming (kebab-case and PascalCase mixed)
├── route view components not distinguishable from presentational ones (no views/ folder or *View suffix)
└── no index.ts barrel for shared/ui, forcing per-file deep imports
```

## Directory Signals

```
✅ Healthy Vue project structure:
features/*/index.ts        → each feature declares its own public API
shared/ui/                 → imports nothing from features/
lib/http.ts                → knows transport, not domain
lib/config.ts              → single, validated env reader
router/index.ts            → all route components dynamically imported

❌ Warning signals:
components/ with 40+ flat files      → no feature boundary exists
stores/ with one store per view      → stores mirror screens, not domains
views/*.vue over 300 lines           → route views are god components
utils/index.ts as a catch-all        → unrelated helpers with no owner
import '../../../features/x/y'       → no aliases and no public surface
```

## Nuxt-Specific Notes

Nuxt supplies the top-level layout (`pages/`, `layouts/`, `composables/`, `server/`), so evaluate the layers Nuxt does **not** enforce:

```
✅ Expected in a healthy Nuxt project:
server/api/                → the only place with DB access or secrets
composables/<feature>/      → feature grouping inside the auto-import root
nuxt.config.ts runtimeConfig → private keys server-side, public keys explicitly public

❌ Findings:
components/ flat with 60+ auto-imported files   → name collisions, unclear ownership
secrets in runtimeConfig.public or NUXT_PUBLIC_* → exposed in the client bundle
business logic in pages/ instead of composables/ → pages become god components
server/ absent while the app holds API keys      → keys shipped to the browser
```

## Why

- **Deletability**: A feature folder with a public `index.ts` can be removed or replaced by deleting one directory; a feature spread across five type-based folders cannot.
- **Dependency direction**: When `shared/` never imports `features/`, the dependency graph stays acyclic — build tools can tree-shake, and refactors stay local.
- **Public surfaces**: An `index.ts` boundary lets internals be renamed freely. Deep imports promote every internal file to public API by accident.
- **Configuration auditing**: One `config.ts` makes it possible to answer "what does this app read from the environment, and is any of it secret" in a single file read.
- **Bundle economics**: Route-level dynamic imports keep an admin dashboard's charting library out of the first paint of a public landing page.
- **Consistency**: A single API style means one mental model. Mixed Options/Composition code doubles the reading cost of every component and blocks systematic refactoring.
