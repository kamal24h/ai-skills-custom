# Vue Router 4

Route definitions, lazy loading, navigation guards, param reactivity, and typed metadata.

## 1. Router Setup

```ts
// router/index.ts
import { createRouter, createWebHistory } from 'vue-router'

export const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('@/views/HomeView.vue'),   // lazy → its own chunk
    },
    {
      path: '/users/:id',
      name: 'user-detail',
      component: () => import('@/views/UserDetailView.vue'),
      props: true,                                       // params become props
      meta: { requiresAuth: true, title: 'User' },
      children: [
        { path: 'posts', name: 'user-posts', component: () => import('@/views/UserPosts.vue') },
      ],
    },
    { path: '/:pathMatch(.*)*', name: 'not-found', component: () => import('@/views/NotFound.vue') },
  ],
  scrollBehavior(to, from, saved) {
    if (saved) return saved
    if (to.hash) return { el: to.hash, behavior: 'smooth' }
    return { top: 0 }
  },
})
```

- **Always lazy-load route components** with dynamic `import()`.
- Use **named routes** and `router.push({ name, params })` — path strings break on refactors.
- Always define a catch-all 404 route.
- `props: true` decouples the view from `useRoute()` and makes it trivially testable. `props: route => ({ id: route.params.id, page: Number(route.query.page ?? 1) })` for the function form.

### Typed meta

```ts
// router/types.d.ts
export {}
declare module 'vue-router' {
  interface RouteMeta {
    requiresAuth?: boolean
    roles?: readonly string[]
    title?: string
  }
}
```

## 2. Navigation Guards — Return, Don't Call `next()`

The `next()` callback is legacy and easy to call twice or forget on one branch. Return a value instead.

```ts
router.beforeEach(async (to) => {
  const auth = useAuthStore()          // inside the guard, not at module scope

  if (!auth.initialized) await auth.restoreSession()   // ✅ awaited

  if (to.meta.requiresAuth && !auth.isAuthenticated) {
    if (to.name === 'login') return true               // ✅ terminating condition
    return { name: 'login', query: { redirect: to.fullPath } }
  }

  if (to.meta.roles && !to.meta.roles.some(r => auth.roles.includes(r))) {
    return { name: 'forbidden' }
  }

  return true
})
```

Return values:

| Return | Effect |
|---|---|
| `true` / `undefined` | Continue |
| `false` | Abort, stay on the current route |
| `{ name: 'x' }` / `'/x'` | Redirect |
| `throw` | Abort and trigger `router.onError` |

### Async guards must be awaited

```ts
// ❌ navigation completes before the check resolves
router.beforeEach((to) => {
  checkAuth().then(ok => { if (!ok) router.push('/login') })
  return true
})

// ✅
router.beforeEach(async (to) => {
  const ok = await checkAuth()
  return ok ? true : { name: 'login' }
})
```

### Infinite redirect loops

Every redirect needs a terminating condition — check the destination before redirecting:

```ts
// ❌ /login also lacks auth → infinite loop
if (!auth.isAuthenticated) return { name: 'login' }

// ✅
if (!auth.isAuthenticated && to.name !== 'login') return { name: 'login' }
```

Vue Router aborts after too many redirects and logs an error — treat that as a guard bug, not a router bug.

### Guard execution order

1. `beforeRouteLeave` (leaving components)
2. Global `beforeEach`
3. `beforeRouteUpdate` (reused components)
4. Route-level `beforeEnter`
5. `beforeRouteEnter` (entering components)
6. Global `beforeResolve`
7. Navigation confirmed → global `afterEach`

Notes:

- `beforeEnter` **does not fire** when only params change on the same route (`/users/1` → `/users/2`). Put such logic in `beforeEach`, `beforeRouteUpdate`, or a param watcher. Passing an array of guards to `beforeEnter` is supported for composition.
- `beforeRouteEnter` runs **before** the component instance exists — there is no `this`, no setup scope. Fetch there and stash the result, or (better) fetch inside the component after navigation.
- `afterEach` cannot cancel navigation — use it for analytics and `document.title`.

## 3. Reacting to Param Changes

The component is **reused** when only params change. `onMounted` does not re-run.

```ts
// ❌ stale data when navigating /users/1 → /users/2
onMounted(() => loadUser(route.params.id as string))

// ✅ watcher with immediate
const route = useRoute()
watch(
  () => route.params.id,
  (id) => loadUser(id as string),
  { immediate: true },
)

// ✅ or the in-component guard
onBeforeRouteUpdate(async (to) => { await loadUser(to.params.id as string) })

// ✅ best: props: true and watch the prop
const props = defineProps<{ id: string }>()
watch(() => props.id, loadUser, { immediate: true })
```

Alternatively, force a fresh instance with `<RouterView :key="route.fullPath" />` — simple, but it discards all component state and re-runs every mount effect, so use it deliberately.

## 4. In-Component Guards

```ts
import { onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'

onBeforeRouteLeave(() => {
  if (form.isDirty) return window.confirm('Discard unsaved changes?')
})

onBeforeRouteUpdate(async (to, from) => {
  if (to.params.id !== from.params.id) await load(to.params.id as string)
})
```

These are composables — call them synchronously in setup.

## 5. Cleanup on Navigation

Route navigation unmounts components silently. Anything registered manually must be released:

```ts
onMounted(() => window.addEventListener('scroll', onScroll))
onUnmounted(() => window.removeEventListener('scroll', onScroll))

// or, no bookkeeping needed:
useEventListener(window, 'scroll', onScroll)   // VueUse — auto-cleanup
```

Same for intervals, WebSockets, `IntersectionObserver`, and third-party widget instances.

## 6. Programmatic Navigation

```ts
const router = useRouter()

router.push({ name: 'user-detail', params: { id } })
router.replace({ query: { ...route.query, page: '2' } })   // no history entry
router.back()

// Detect failures (aborted by a guard, duplicated navigation)
const failure = await router.push({ name: 'checkout' })
if (failure) reportNavigationFailure(failure)
```

`router.push` resolves even when a guard cancels — check the returned `NavigationFailure` when the next step depends on the navigation succeeding.

## 7. Named Views and Nested Layouts

```ts
{
  path: '/settings',
  components: {
    default: () => import('@/views/SettingsView.vue'),
    sidebar: () => import('@/components/SettingsNav.vue'),
  },
}
```

```vue
<RouterView name="sidebar" />
<RouterView />
```

For layouts, prefer a parent route with a layout component and a nested `<RouterView />` over per-view layout imports.

## 8. Transitions and KeepAlive with RouterView

```vue
<RouterView v-slot="{ Component, route }">
  <Transition :name="route.meta.transition ?? 'fade'" mode="out-in">
    <KeepAlive :include="['UserList']" :max="5">
      <component :is="Component" :key="route.path" />
    </KeepAlive>
  </Transition>
</RouterView>
```

- Add `appear` only if you want the first render animated.
- `<KeepAlive :include>` matches component **names** — set `defineOptions({ name: 'UserList' })`.
- Always bound `:max` — unbounded caching plus `<Transition>` is a known memory-growth pattern.
- With nested routes, wrapping the wrong `<RouterView>` in `<KeepAlive>` can cause children to mount twice; keep the caching at one level.

## 9. Data Fetching Strategy

| Strategy | Where | Trade-off |
|---|---|---|
| Fetch after navigation | In the component (`watch` + `immediate`) | Instant navigation, loading UI needed |
| Fetch before navigation | `beforeEnter` / `beforeRouteEnter` | No loading flash, navigation feels slow |
| Prefetch on intent | `@mouseenter` on the link | Best perceived speed, extra requests |

Default to fetching after navigation with explicit loading/error states — it is simpler and keeps guards fast. Use before-navigation fetching only when a blank state is unacceptable.

## Anti-Patterns

| Anti-pattern | Consequence | Fix |
|---|---|---|
| Static imports of all views | One huge bundle | `() => import(...)` |
| `next()` callbacks | Double-call / missed branch bugs | Return values |
| Unawaited async in a guard | Navigation races the check | `async` guard + `await` |
| Redirect without checking the target | Infinite loop | Guard the destination |
| Fetch only in `onMounted` | Stale data on param change | Watch params / `onBeforeRouteUpdate` |
| Store instantiated at router module scope | "no active Pinia" | Instantiate inside the guard |
| `to.meta.x as boolean` casts | Untyped metadata | Augment `RouteMeta` |
| Listeners without `onUnmounted` | Leaks across navigations | Pair cleanup / VueUse |
| Path strings in `push` | Breaks on route refactors | Named routes |
| Unbounded `<KeepAlive>` | Memory growth | `:include` + `:max` |
