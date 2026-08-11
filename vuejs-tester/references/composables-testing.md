# Testing Composables

Composables split into two kinds, and each has its own testing strategy.

| Kind | Uses lifecycle hooks / `inject` / `getCurrentInstance`? | Strategy |
|---|---|---|
| **Independent** | No — only refs, computeds, plain functions | Call directly in the test |
| **Instance-dependent** | Yes | Run inside a component context (`withSetup()` helper or a host component) |

## 1. Independent Composables — Call Directly

```ts
import { nextTick } from 'vue'
import { useCounter } from './useCounter'

describe('useCounter', () => {
  it('increments by the configured step', async () => {
    const { count, inc } = useCounter(0, { step: 5 })

    inc()
    await nextTick()

    expect(count.value).toBe(5)
  })

  it('clamps at the maximum', () => {
    const { count, inc } = useCounter(9, { step: 5, max: 10 })
    inc()
    expect(count.value).toBe(10)
  })
})
```

Assert on the returned refs' `.value` and on observable side effects. Do not reach into the closure.

### Adaptable inputs

A composable taking `MaybeRefOrGetter` must work with all three call styles — test them:

```ts
it.each([
  ['plain value', 3],
  ['ref', ref(3)],
  ['getter', () => 3],
])('accepts a %s input', (_label, input) => {
  const { double } = useDouble(input as never)
  expect(double.value).toBe(6)
})

it('tracks changes when the input is a ref', async () => {
  const n = ref(3)
  const { double } = useDouble(n)

  n.value = 5
  await nextTick()

  expect(double.value).toBe(10)   // fails if toValue() was called outside the effect
})
```

That second test is the one that catches the most common composable bug: `toValue()` snapshotting the input at call time.

## 2. Instance-Dependent Composables — `withSetup()`

```ts
// src/test/withSetup.ts
import { createApp, type App } from 'vue'

export function withSetup<T>(composable: () => T): [T, App] {
  let result!: T
  const app = createApp({
    setup() {
      result = composable()
      return () => {}          // render nothing
    },
  })
  app.mount(document.createElement('div'))
  return [result, app]         // app.unmount() triggers onUnmounted / onScopeDispose
}
```

```ts
import { withSetup } from '@/test/withSetup'
import { useWindowSize } from './useWindowSize'

describe('useWindowSize', () => {
  it('registers and removes the resize listener', () => {
    const add = vi.spyOn(window, 'addEventListener')
    const remove = vi.spyOn(window, 'removeEventListener')

    const [{ width }, app] = withSetup(() => useWindowSize())
    expect(add).toHaveBeenCalledWith('resize', expect.any(Function), expect.anything())
    expect(width.value).toBe(window.innerWidth)

    app.unmount()
    expect(remove).toHaveBeenCalledWith('resize', expect.any(Function), expect.anything())
  })
})
```

`app.unmount()` is what makes teardown testable — without it you can never verify cleanup.

### Providing injected dependencies

```ts
export function withSetup<T>(
  composable: () => T,
  provides: Record<string | symbol, unknown> = {},
): [T, App] {
  let result!: T
  const app = createApp({ setup() { result = composable(); return () => {} } })
  for (const [key, value] of Object.entries(provides)) app.provide(key, value)
  for (const sym of Object.getOwnPropertySymbols(provides)) app.provide(sym, provides[sym])
  app.mount(document.createElement('div'))
  return [result, app]
}
```

```ts
const analytics = { track: vi.fn() }
const [{ report }] = withSetup(() => useReporting(), { [analyticsKey]: analytics })

report('checkout')
expect(analytics.track).toHaveBeenCalledWith('checkout')
```

Provide the real `InjectionKey` — do not module-mock the provider to sidestep injection.

## 3. Host Component Approach

When the composable's behavior is best observed through rendering, a tiny host component is clearer than `withSetup`:

```ts
import { defineComponent } from 'vue'
import { render, screen } from '@testing-library/vue'
import { useBreakpoints } from './useBreakpoints'

const Host = defineComponent({
  setup() {
    const { isMobile } = useBreakpoints()
    return () => h('div', isMobile.value ? 'mobile' : 'desktop')
  },
})

it('reports mobile below the md breakpoint', async () => {
  setViewport(500)
  render(Host)
  expect(await screen.findByText('mobile')).toBeInTheDocument()
})
```

## 4. Testing Cleanup with `effectScope`

For composables intended to run outside components (stores, singletons):

```ts
import { effectScope } from 'vue'

it('disposes its interval when the scope stops', () => {
  vi.useFakeTimers()
  const tick = vi.fn()

  const scope = effectScope()
  scope.run(() => usePolling(tick, 1000))

  vi.advanceTimersByTime(3000)
  expect(tick).toHaveBeenCalledTimes(3)

  scope.stop()
  vi.advanceTimersByTime(3000)
  expect(tick).toHaveBeenCalledTimes(3)   // no further calls

  vi.useRealTimers()
})
```

This is the canonical test for `onScopeDispose` correctness.

## 5. Composables That Fetch

Mock at the network boundary, not the composable's internals:

```ts
import { http, HttpResponse } from 'msw'
import { server } from '@/test/msw/server'

describe('useUser', () => {
  it('exposes the loaded user', async () => {
    server.use(http.get('/api/users/u1', () => HttpResponse.json({ id: 'u1', name: 'Ada' })))

    const [{ user, isLoading }] = withSetup(() => useUser(ref('u1')))
    expect(isLoading.value).toBe(true)

    await flushPromises()

    expect(isLoading.value).toBe(false)
    expect(user.value).toEqual({ id: 'u1', name: 'Ada' })
  })

  it('exposes an error when the request fails', async () => {
    server.use(http.get('/api/users/u1', () => HttpResponse.json({ message: 'Not found' }, { status: 404 })))

    const [{ user, error }] = withSetup(() => useUser(ref('u1')))
    await flushPromises()

    expect(user.value).toBeNull()
    expect(error.value).toBeInstanceOf(ApiError)
  })

  it('refetches when the id changes', async () => {
    const calls: string[] = []
    server.use(http.get('/api/users/:id', ({ params }) => {
      calls.push(params.id as string)
      return HttpResponse.json({ id: params.id, name: 'X' })
    }))

    const id = ref('u1')
    withSetup(() => useUser(id))
    await flushPromises()

    id.value = 'u2'
    await flushPromises()

    expect(calls).toEqual(['u1', 'u2'])
  })
})
```

## 6. What to Cover

- [ ] Initial state of every returned ref
- [ ] Each returned action's effect on state
- [ ] Reactivity to changing inputs (ref and getter forms)
- [ ] Loading / success / error transitions for async composables
- [ ] Cleanup on unmount / scope stop
- [ ] Edge cases: empty input, `null`, rapid successive calls, superseded requests
- [ ] Injected dependency wiring, where applicable

## Anti-Patterns

| Anti-pattern | Consequence | Fix |
|---|---|---|
| Calling a lifecycle composable directly | "must be called inside setup" or dead hooks | `withSetup()` / host component |
| Never unmounting in the test | Cleanup bugs go undetected | `app.unmount()` / `scope.stop()` |
| Mocking the composable's own internals | Tests the mock | Mock the network boundary |
| Only testing the plain-value input | `toValue()` snapshot bug missed | Test ref and getter inputs too |
| Module-mocking the provider | Injection contract untested | `app.provide(realKey, fake)` |
| Reading closure state via mocks | Couples to implementation | Assert returned refs |
| Assertion without `await nextTick()` | Reads pre-update value | `await nextTick()` |
| `withSetup` ceremony for pure composables | Noise | Call directly |

## Sources

- [Vue — Testing composables](https://vuejs.org/guide/scaling-up/testing.html)
- [Vue — Composables](https://vuejs.org/guide/reusability/composables.html)
