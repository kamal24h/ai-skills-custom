# SSR & Hydration

Server-side rendering correctness: per-request state, deterministic markup, browser-API guards, and hydration mismatch diagnosis. Applies to hand-rolled Vue SSR and to Nuxt.

## 1. The Two Rules That Prevent Most SSR Bugs

1. **No mutable module-scope state.** Anything at module scope is shared by every request on the server.
2. **Server and client must render identical markup.** Any nondeterminism becomes a hydration mismatch.

## 2. Per-Request Everything

```ts
// entry-server.ts
import { createSSRApp } from 'vue'
import { renderToString } from 'vue/server-renderer'
import { createPinia } from 'pinia'
import { createMemoryHistory, createRouter } from 'vue-router'
import { routes } from './router/routes'
import App from './App.vue'

export async function render(url: string) {
  const app = createSSRApp(App)                            // new app per request
  const pinia = createPinia()                              // new store per request
  const router = createRouter({ history: createMemoryHistory(), routes })

  app.use(pinia).use(router)
  await router.push(url)
  await router.isReady()

  const html = await renderToString(app)
  return { html, state: pinia.state.value }
}
```

```ts
// entry-client.ts
const app = createApp(App)          // createSSRApp for hydration in a real setup
const pinia = createPinia()
if (window.__INITIAL_STATE__) pinia.state.value = window.__INITIAL_STATE__
app.use(pinia).use(router)
router.isReady().then(() => app.mount('#app'))
```

Serialize the payload with `devalue`, not raw `JSON.stringify` interpolated into HTML — a `</script>` inside data would break the page and enable injection.

### The singleton trap

```ts
// ❌ every user shares this on the server
export const currentUser = ref<User | null>(null)
export const cache = new Map<string, Data>()

// ❌ VueUse createGlobalState / createSharedComposable are module singletons too
export const useSession = createGlobalState(() => ({ user: ref<User | null>(null) }))
```

```ts
// ✅ tied to the component tree — one instance per request
import { createInjectionState } from '@vueuse/core'
const [provideSession, useSession] = createInjectionState(() => ({ user: ref<User | null>(null) }))
export { provideSession, useSession }

// ✅ or a Pinia store, created per request
```

A read-only module constant (config, lookup table) is fine. Anything a request can **write** is not.

## 3. Browser APIs

`window`, `document`, `localStorage`, `navigator`, `matchMedia`, `IntersectionObserver`, and `ResizeObserver` do not exist on the server.

```ts
// ❌ crashes during SSR
const width = ref(window.innerWidth)

// ✅ access after mount
const width = ref(0)
onMounted(() => { width.value = window.innerWidth })

// ✅ or guard explicitly
if (!import.meta.env.SSR) { /* client-only */ }
if (typeof window !== 'undefined') { /* client-only */ }
```

`onMounted` and `onUpdated` never run on the server. `setup()`, `computed`, and `onServerPrefetch` do.

Most VueUse composables are SSR-safe by design (they no-op on the server and initialize on mount) — prefer them over hand-rolled browser-API code.

## 4. Hydration Mismatches

Vue logs `Hydration node mismatch` / `Hydration text mismatch` and then discards the server markup for that subtree, re-rendering it on the client. That means a visible flash plus lost SSR benefit.

### Common causes

| Cause | Example | Fix |
|---|---|---|
| Time/date | `{{ formatRelative(post.date) }}` → "3 minutes ago" | Render absolute on the server, localize in `onMounted` |
| Randomness | `Math.random()`, `crypto.randomUUID()` for ids | `useId()` (Vue 3.5+) |
| Locale/timezone | `toLocaleDateString()` with server locale ≠ client locale | Format with an explicit locale/timezone |
| Browser-only state | `window.innerWidth`, `localStorage` read during setup | Read in `onMounted` |
| Invalid HTML nesting | `<div>` inside `<p>`, `<tr>` outside `<tbody>` | Fix the markup — the browser silently reparses it |
| Third-party DOM mutation | Extensions, analytics injecting nodes | Usually ignorable; scope your markup |
| Conditional on `import.meta.env.SSR` in the template | Different tree per environment | Render the same tree; toggle after mount |

### The `isMounted` pattern

```ts
const isMounted = ref(false)
onMounted(() => { isMounted.value = true })
```

```vue
<span>{{ isMounted ? relativeTime : absoluteTime }}</span>
```

Server and first client render both produce `absoluteTime`; the swap happens after hydration. This is the standard fix for time-ago, theme-dependent, and viewport-dependent content.

### Escape hatches

```vue
<!-- Nuxt -->
<ClientOnly><ThirdPartyWidget /><template #fallback><Skeleton /></template></ClientOnly>

<!-- Vue 3.5+: allow a known, acceptable mismatch narrowly -->
<span data-allow-mismatch="text">{{ localFormattedDate }}</span>
```

`data-allow-mismatch` accepts `text`, `children`, `class`, `style`, or `attribute`. Use it for one specific known difference — never as a global way to silence warnings.

## 5. Data Fetching on the Server

```ts
// Plain Vue SSR
onServerPrefetch(async () => {
  await store.loadDashboard()     // runs on the server, state is serialized
})
onMounted(() => {
  if (!store.loaded) store.loadDashboard()   // client-side navigation
})
```

In Nuxt, use `useAsyncData`/`useFetch`, which handle server execution, payload serialization, and deduplication in one call:

```ts
const { data, error, pending } = await useAsyncData('dashboard', () => $fetch('/api/dashboard'))
```

Do not fetch the same data twice (once on the server, once on hydration) — that is the most common SSR performance regression.

## 6. Teleport and SSR

Teleported content is serialized into a separate chunk of the payload and re-attached at hydration.

- The target element must exist in the server-rendered HTML, or the Teleport must be client-only.
- `<Teleport to="body">` works in Nuxt but needs care in custom SSR setups.
- Teleport + `<Suspense>` combinations have known hydration edge cases; test them explicitly.

## 7. `<Suspense>` and SSR

`<Suspense>` is still experimental and its SSR behavior has known rough edges (fallback content and hydration order). For SSR apps prefer explicit loading state or the framework's data-fetching primitives over `<Suspense>` boundaries in app code.

## 8. CSS and Fonts

- Inline critical CSS or ensure the stylesheet is in the SSR-rendered `<head>` — otherwise the first paint is unstyled.
- Set the theme attribute (`data-theme`) server-side or via an inline head script to avoid a flash of the wrong theme.
- Preload the primary font weight; use `font-display: swap`.

## 9. SSR Checklist

- [ ] App, router, and Pinia are created per request
- [ ] No mutable module-scope state anywhere in universal code
- [ ] No `createGlobalState`/`createSharedComposable` holding per-user data
- [ ] Browser APIs only in `onMounted` or behind `import.meta.env.SSR` guards
- [ ] No `Date.now()`, `Math.random()`, or locale-dependent formatting in render output
- [ ] Unique ids come from `useId()`
- [ ] HTML nesting is valid (no `<div>` in `<p>`, no bare `<tr>`)
- [ ] Payload serialized with `devalue` (or equivalent), not raw `JSON.stringify`
- [ ] Data fetched once — server prefetch state is hydrated, not refetched
- [ ] Client-only widgets wrapped in `<ClientOnly>` or mounted post-hydration
- [ ] `data-allow-mismatch` used narrowly, if at all
- [ ] No hydration warnings in the console on any route

## Anti-Patterns

| Anti-pattern | Consequence | Fix |
|---|---|---|
| `export const user = ref(null)` | Cross-request data leak | Per-request store / injection state |
| Shared `pinia` across requests | User data leak | `createPinia()` per request |
| `window.x` in `setup()` | Server crash | `onMounted` / SSR guard |
| Relative time rendered during SSR | Hydration text mismatch | `isMounted` swap |
| `Math.random()` for ids | Guaranteed mismatch | `useId()` |
| Invalid HTML nesting | Node mismatch, silent reparse | Fix the markup |
| Raw `JSON.stringify` for payload | XSS via `</script>` | `devalue` |
| Fetch on server + refetch on mount | Doubled load, flicker | Hydrate the serialized state |
| Global `data-allow-mismatch` | Real bugs hidden | Narrow, per-element use |
| Suppressing hydration warnings | Debt accumulates invisibly | Fix determinism |
