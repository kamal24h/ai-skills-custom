# Mocking

Where to place a test double, and which tool to use.

## 1. Mock the Boundary, Not Your Own Code

| Mock it | Do not mock it |
|---|---|
| Network (HTTP, WebSocket, SSE) | Your composables |
| `Date`, `crypto`, `Math.random` | Your Pinia stores |
| Browser APIs jsdom lacks | Your utils |
| Third-party SDKs (analytics, payments, maps) | Vue itself |
| Heavy child components (charts, editors, maps) | The component under test |

Mocking your own modules produces tests that pass while the real integration is broken. Mock at the edge of your system so the maximum amount of real code executes.

## 2. HTTP with MSW

MSW intercepts at the network layer, so your real client (headers, status handling, error mapping, retries, response parsing) runs.

```ts
// src/test/msw/handlers.ts
import { http, HttpResponse } from 'msw'
import { makeUser } from '../factories'

export const handlers = [
  http.get('/api/users', () => HttpResponse.json([makeUser()])),

  http.get('/api/users/:id', ({ params }) =>
    HttpResponse.json(makeUser({ id: params.id as string }))),

  http.post('/api/users', async ({ request }) => {
    const body = await request.json() as { name: string }
    return HttpResponse.json(makeUser({ name: body.name }), { status: 201 })
  }),
]
```

```ts
// src/test/msw/server.ts
import { setupServer } from 'msw/node'
import { handlers } from './handlers'

export const server = setupServer(...handlers)
```

```ts
// src/test/setup.ts
beforeAll(() => server.listen({ onUnhandledRequest: 'error' }))
afterEach(() => server.resetHandlers())
afterAll(() => server.close())
```

`onUnhandledRequest: 'error'` makes a forgotten handler a loud failure instead of a real network call.

### Per-test overrides

```ts
it('shows an error banner when the API returns 500', async () => {
  server.use(http.get('/api/users', () => HttpResponse.json({ message: 'Boom' }, { status: 500 })))

  render(UserList)

  expect(await screen.findByRole('alert')).toHaveTextContent(/could not load users/i)
})

it('shows an offline message on a network failure', async () => {
  server.use(http.get('/api/users', () => HttpResponse.error()))
  render(UserList)
  expect(await screen.findByRole('alert')).toHaveTextContent(/check your connection/i)
})
```

`server.resetHandlers()` in `afterEach` guarantees overrides do not leak into later tests.

### Asserting the request

```ts
it('sends the search query as a parameter', async () => {
  const seen: string[] = []
  server.use(http.get('/api/search', ({ request }) => {
    seen.push(new URL(request.url).searchParams.get('q') ?? '')
    return HttpResponse.json([])
  }))

  render(SearchPage)
  await userEvent.type(screen.getByRole('searchbox'), 'vue{Enter}')
  await flushPromises()

  expect(seen).toEqual(['vue'])
})
```

### Delayed responses

```ts
import { delay } from 'msw'

server.use(http.get('/api/users', async () => {
  await delay(100)
  return HttpResponse.json([makeUser()])
}))
```

Useful for asserting that a loading state actually renders.

## 3. Module Mocks with `vi.mock`

Reserve for modules that cannot be intercepted at the network layer — third-party SDKs, native modules, environment-specific code.

```ts
vi.mock('@/lib/analytics', () => ({
  track: vi.fn(),
  identify: vi.fn(),
}))

import { track } from '@/lib/analytics'

it('tracks the checkout event', async () => {
  render(CheckoutButton)
  await userEvent.click(screen.getByRole('button', { name: 'Checkout' }))
  expect(vi.mocked(track)).toHaveBeenCalledWith('checkout_started')
})
```

### Hoisting

`vi.mock` is hoisted above imports. Referencing a top-level `const` inside the factory throws "Cannot access before initialization".

```ts
// ❌
const trackSpy = vi.fn()
vi.mock('@/lib/analytics', () => ({ track: trackSpy }))

// ✅
const { trackSpy } = vi.hoisted(() => ({ trackSpy: vi.fn() }))
vi.mock('@/lib/analytics', () => ({ track: trackSpy }))
```

### Partial mocks

```ts
vi.mock('@/lib/format', async (importOriginal) => {
  const actual = await importOriginal<typeof import('@/lib/format')>()
  return { ...actual, formatDate: vi.fn(() => '2026-01-01') }
})
```

### Typed mocks

```ts
import { vi } from 'vitest'
import { fetchUser } from '@/api/users'

vi.mock('@/api/users')

it('renders the user', async () => {
  vi.mocked(fetchUser).mockResolvedValue(makeUser({ name: 'Ada' }))
  // ...
})
```

`vi.mocked()` keeps the mock's signature tied to the real function — an `as any` cast lets the two drift silently.

## 4. Spies

```ts
const onSave = vi.fn()
const spy = vi.spyOn(console, 'error').mockImplementation(() => {})
const storage = vi.spyOn(Storage.prototype, 'setItem')

expect(onSave).toHaveBeenCalledOnce()
expect(onSave).toHaveBeenCalledWith({ id: 'u1' })
expect(onSave).toHaveBeenCalledExactlyOnceWith({ id: 'u1' })
expect(onSave.mock.calls[0][0]).toMatchObject({ id: 'u1' })
expect(onSave).toHaveBeenLastCalledWith(expect.objectContaining({ id: 'u1' }))
```

Set `restoreMocks: true` in the Vitest config (or `vi.restoreAllMocks()` in `afterEach`) so spies do not leak between tests.

## 5. Component Stubs

```ts
mount(Dashboard, {
  global: {
    stubs: {
      RevenueChart: true,                                      // renders <revenue-chart-stub>
      MapView: { template: '<div data-testid="map-stub" />' },  // custom stub
      transition: false,                                       // render transitions for real
      teleport: true,                                          // keep teleported content inline
    },
  },
})
```

Stub only when the child is genuinely heavy (canvas/WebGL/editor), depends on unavailable APIs, or is fully covered by its own tests — and say why in a comment.

```ts
// RevenueChart mounts a canvas renderer unavailable in jsdom; covered by its own test
```

## 6. Browser APIs and Globals

```ts
// Frozen clock
vi.setSystemTime(new Date('2026-01-01T12:00:00Z'))
afterEach(() => vi.useRealTimers())

// Deterministic ids
vi.spyOn(crypto, 'randomUUID').mockReturnValue('00000000-0000-4000-8000-000000000000')

// Geolocation
Object.defineProperty(navigator, 'geolocation', {
  value: { getCurrentPosition: vi.fn(cb => cb({ coords: { latitude: 41, longitude: 29 } })) },
  configurable: true,
})

// Clipboard
Object.assign(navigator, { clipboard: { writeText: vi.fn().mockResolvedValue(undefined) } })

// matchMedia, ResizeObserver, IntersectionObserver → see vitest-setup.md
```

## 7. Injected Dependencies

Because provide/inject is a real seam, injected services are the easiest things to fake — no module mocking required.

```ts
render(Checkout, {
  global: {
    provide: {
      [paymentsKey as symbol]: { charge: vi.fn().mockResolvedValue({ ok: true }) },
    },
  },
})
```

This is a strong argument for injecting services rather than importing singletons directly.

## 8. Decision Table

| Need | Tool |
|---|---|
| HTTP request/response | MSW |
| WebSocket / SSE | MSW (WebSocket handlers) or a fake transport |
| Third-party SDK | `vi.mock` |
| Time / dates | `vi.useFakeTimers()` + `vi.setSystemTime()` |
| Randomness / UUIDs | `vi.spyOn` |
| Missing browser API | Global stub in `setup.ts` |
| Heavy child component | `global.stubs` |
| Application service | `global.provide` with a fake |
| Callback prop | `vi.fn()` |
| Your own composable/store | **Do not mock** — use the real one |

## Anti-Patterns

| Anti-pattern | Consequence | Fix |
|---|---|---|
| `vi.mock('@/lib/http')` | Skips headers/status/error mapping | MSW |
| Mocking your own composables | Tests the mock | Use the real one |
| No `onUnhandledRequest: 'error'` | Real requests silently pass | Set it |
| Handlers not reset | One test's override breaks the next | `server.resetHandlers()` |
| Outer variable in a `vi.mock` factory | "Cannot access before initialization" | `vi.hoisted()` |
| `as any` on mocks | Signature drift goes unnoticed | `vi.mocked()` |
| Mocks not restored | Leaked implementations | `restoreMocks: true` |
| Stubbing every child | Integration untested | Stub deliberately, explain why |
| Mocking `Date` globally in `setup.ts` | Surprising failures everywhere | Per-test `setSystemTime` |
| Real network in a component test | CI flake, slow suite | MSW |

## Sources

- [Vitest — Mocking](https://vitest.dev/guide/mocking.html)
- [MSW — Mock Service Worker](https://mswjs.io/docs/)
