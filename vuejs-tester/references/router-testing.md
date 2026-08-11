# Testing with Vue Router

Route components, navigation guards, and route-driven behavior — with a real router on memory history.

## 1. Use a Real Router, Not a Mock

Mocking `useRoute`/`useRouter` skips exactly the wiring most likely to be wrong (param names, guard order, redirect targets). A real router on `createMemoryHistory()` is fast and has no DOM dependency.

```ts
import { createMemoryHistory, createRouter, type Router } from 'vue-router'
import { routes } from '@/router/routes'

export function makeRouter(initial = '/'): Router {
  const router = createRouter({ history: createMemoryHistory(), routes })
  router.push(initial)
  return router
}
```

A fresh router per test — a shared one carries navigation history and guard state between tests.

## 2. Testing a Route Component

```ts
import { render, screen } from '@testing-library/vue'
import { makeRouter } from '@/test/router'
import UserDetailView from './UserDetailView.vue'

it('loads the user for the route param', async () => {
  const router = makeRouter('/users/u1')
  await router.isReady()

  render(UserDetailView, { global: { plugins: [router] } })

  expect(await screen.findByRole('heading', { name: 'Ada Lovelace' })).toBeInTheDocument()
})
```

**`await router.isReady()`** before rendering — otherwise the initial navigation may not have resolved and `route.params` is empty.

### Prefer `props: true` routes

A route component that receives params as props needs no router at all in its own tests:

```ts
// Route: { path: '/users/:id', component: UserDetailView, props: true }
render(UserDetailView, { props: { id: 'u1' } })   // no router plugin needed
```

This is the strongest argument for `props: true` — it makes route components trivially testable.

## 3. Param Changes

The most common route bug: the component is reused when only params change, so `onMounted` does not re-run.

```ts
it('reloads when the route param changes', async () => {
  const calls: string[] = []
  server.use(http.get('/api/users/:id', ({ params }) => {
    calls.push(params.id as string)
    return HttpResponse.json({ id: params.id, name: `User ${params.id}` })
  }))

  const router = makeRouter('/users/u1')
  await router.isReady()
  render(App, { global: { plugins: [router] } })
  await flushPromises()

  await router.push('/users/u2')
  await flushPromises()

  expect(calls).toEqual(['u1', 'u2'])
  expect(screen.getByRole('heading', { name: 'User u2' })).toBeInTheDocument()
})
```

If this test fails with `['u1']`, the component fetches only in `onMounted` — the fix is a param watcher or `onBeforeRouteUpdate`.

## 4. Asserting Navigation

```ts
it('navigates to the detail page when a row is clicked', async () => {
  const router = makeRouter('/users')
  await router.isReady()
  const push = vi.spyOn(router, 'push')

  render(UserListView, { global: { plugins: [router] } })
  await userEvent.click(await screen.findByRole('link', { name: 'Ada Lovelace' }))

  expect(push).toHaveBeenCalledWith(expect.objectContaining({ name: 'user-detail', params: { id: 'u1' } }))
})
```

Or assert the resulting location, which is less coupled to the call shape:

```ts
await userEvent.click(screen.getByRole('link', { name: 'Ada Lovelace' }))
await flushPromises()
expect(router.currentRoute.value.name).toBe('user-detail')
expect(router.currentRoute.value.params.id).toBe('u1')
```

## 5. Testing Guards

Guards are plain functions — test them directly, without mounting anything.

```ts
import { setActivePinia, createPinia } from 'pinia'
import { authGuard } from '@/router/guards'
import { useAuthStore } from '@/stores/auth'

describe('authGuard', () => {
  beforeEach(() => { setActivePinia(createPinia()) })

  it('redirects to login with a redirect query for a protected route', async () => {
    const to = { name: 'settings', fullPath: '/settings', meta: { requiresAuth: true } } as never

    const result = await authGuard(to)

    expect(result).toEqual({ name: 'login', query: { redirect: '/settings' } })
  })

  it('allows a protected route for an authenticated user', async () => {
    useAuthStore().user = makeUser()
    const to = { name: 'settings', fullPath: '/settings', meta: { requiresAuth: true } } as never

    await expect(authGuard(to)).resolves.toBe(true)
  })

  it('does not redirect when already on the login route', async () => {
    const to = { name: 'login', fullPath: '/login', meta: { requiresAuth: true } } as never

    await expect(authGuard(to)).resolves.toBe(true)   // no infinite loop
  })
})
```

That last test is the redirect-loop regression guard. Write it for every guard that redirects.

### End-to-end through the router

```ts
it('blocks navigation to a protected route when unauthenticated', async () => {
  const router = makeRouter('/')
  router.beforeEach(authGuard)
  await router.isReady()

  await router.push('/settings')

  expect(router.currentRoute.value.name).toBe('login')
  expect(router.currentRoute.value.query.redirect).toBe('/settings')
})
```

## 6. In-Component Guards

```ts
it('warns before leaving with unsaved changes', async () => {
  const confirmSpy = vi.spyOn(window, 'confirm').mockReturnValue(false)
  const router = makeRouter('/posts/new')
  await router.isReady()
  render(App, { global: { plugins: [router] } })

  await userEvent.type(screen.getByLabelText('Title'), 'Draft')
  await router.push('/posts')

  expect(confirmSpy).toHaveBeenCalled()
  expect(router.currentRoute.value.path).toBe('/posts/new')   // navigation blocked
})
```

## 7. `RouterLink` and `RouterView` in Isolated Tests

If a component renders `<RouterLink>` but the test has no router plugin, Vue warns about an unresolved component. Options, in order of preference:

1. Install the real router (`global.plugins: [router]`) — preferred.
2. Stub it when routing is irrelevant to the assertion:
   ```ts
   global: { stubs: { RouterLink: { template: '<a><slot /></a>' } } }
   ```

Avoid `global.mocks: { $route, $router }` — it does not work with `useRoute()`/`useRouter()` in `<script setup>`, which is what modern components use.

## 8. Route Meta

```ts
it('marks the settings route as requiring auth', () => {
  const router = makeRouter()
  const route = router.resolve({ name: 'settings' })
  expect(route.meta.requiresAuth).toBe(true)
})

it('defines a catch-all 404 route', () => {
  const router = makeRouter()
  expect(router.resolve('/definitely-not-a-route').name).toBe('not-found')
})
```

`router.resolve()` needs no navigation and is the fastest way to assert route configuration.

## 9. URL-Backed State

```ts
it('reads the page from the query string', async () => {
  const router = makeRouter('/users?page=3')
  await router.isReady()

  render(UserListView, { global: { plugins: [router] } })

  expect(await screen.findByTestId('page')).toHaveTextContent('3')
})

it('writes the filter to the query string', async () => {
  const router = makeRouter('/users')
  await router.isReady()
  render(UserListView, { global: { plugins: [router] } })

  await userEvent.selectOptions(screen.getByLabelText('Status'), 'active')
  await flushPromises()

  expect(router.currentRoute.value.query.status).toBe('active')
})
```

## 10. Async Route Components

```ts
it('resolves the lazily loaded view', async () => {
  const router = makeRouter('/reports')
  await router.isReady()          // resolves the dynamic import for the initial route

  render(App, { global: { plugins: [router] } })
  await flushPromises()

  expect(screen.getByRole('heading', { name: 'Reports' })).toBeInTheDocument()
})
```

`router.isReady()` waits for the initial route's component to load; subsequent navigations need `await router.push(...)` plus `flushPromises()`.

## Anti-Patterns

| Anti-pattern | Consequence | Fix |
|---|---|---|
| `vi.mock('vue-router')` | Real wiring untested, brittle mocks | Real router + memory history |
| `global.mocks: { $route }` | Ignored by `useRoute()` in `<script setup>` | Install the router plugin |
| Missing `await router.isReady()` | Empty params on first render | Await it before rendering |
| Shared router across tests | Navigation history leaks | Fresh router per test |
| Only testing the happy path of a guard | Redirect loops ship | Test the already-on-target case |
| No param-change test | Stale-data bug ships | Assert refetch on `push` to a sibling param |
| `RouterLink` unresolved warning ignored | Noise hides real warnings | Install router or stub deliberately |
| Asserting only `push` was called | Passes while the guard cancels | Assert `currentRoute` |

## Sources

- [Vue Test Utils — Testing Vue Router](https://test-utils.vuejs.org/guide/advanced/vue-router.html)
- [Vue Router](https://router.vuejs.org/)
