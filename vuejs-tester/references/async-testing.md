# Async Testing

Vue's DOM updates are asynchronous, and most real components await something. Every flaky Vue test traces back to this reference.

## 1. The Three Waiting Primitives

| Primitive | Waits for | Use when |
|---|---|---|
| `await nextTick()` | Vue's render queue to flush | Purely synchronous state change |
| `await flushPromises()` | All pending microtasks **and** the render queue | Anything involving promises (fetch, dynamic import, async setup) |
| `await vi.waitFor(fn)` | `fn` to stop throwing, with retries | Unknown number of ticks / polling |

```ts
import { nextTick } from 'vue'
import { flushPromises } from '@vue/test-utils'
import { vi } from 'vitest'
```

## 2. `nextTick` — Synchronous State Changes

```ts
it('shows the panel after toggling', async () => {
  const wrapper = mount(Panel)

  await wrapper.get('button').trigger('click')   // trigger returns nextTick
  expect(wrapper.get('[data-testid="panel"]').isVisible()).toBe(true)
})
```

VTU's `trigger`, `setValue`, `setProps`, and Testing Library's `userEvent`/`fireEvent` already return a promise that resolves after `nextTick`. `await` them and you rarely need an explicit `nextTick()`.

```ts
// Explicit case: state changed outside an interaction helper
store.items = [makeCartItem()]
await nextTick()
expect(screen.getByText('Widget')).toBeInTheDocument()
```

## 3. `flushPromises` — Promise Chains

One `nextTick()` flushes **one** microtask checkpoint. A `fetch().then().then()` chain needs more.

```ts
it('renders the fetched users', async () => {
  render(UserList)

  await flushPromises()          // resolves the fetch chain + re-render

  expect(screen.getByText('Ada Lovelace')).toBeInTheDocument()
})
```

`flushPromises` drains the microtask queue repeatedly, so it covers `await` chains of arbitrary depth. It does **not** advance timers.

Testing Library's `findBy*` queries are often cleaner — they retry until the element appears:

```ts
expect(await screen.findByText('Ada Lovelace')).toBeInTheDocument()
```

## 4. `vi.waitFor` — Eventual Conditions

```ts
await vi.waitFor(() => {
  expect(screen.getByRole('status')).toHaveTextContent('Saved')
}, { timeout: 2000, interval: 20 })
```

Use for conditions that resolve after an unpredictable number of ticks (retry logic, polling, debounced effects with real timers). Prefer `findBy*` when you are simply waiting for an element.

## 5. Never Sleep

```ts
// ❌ flaky on a loaded CI machine, and slow when it passes
await new Promise(r => setTimeout(r, 100))

// ✅ wait for the actual condition
await flushPromises()
await vi.waitFor(() => expect(spy).toHaveBeenCalled())
expect(await screen.findByRole('alert')).toBeVisible()
```

A fixed sleep encodes a guess about machine speed. On CI it is either too short (flake) or too long (slow suite) — usually both across different tests.

## 6. Fake Timers

```ts
describe('AutoSaveEditor', () => {
  beforeEach(() => { vi.useFakeTimers() })
  afterEach(() => { vi.useRealTimers() })   // ⚠️ mandatory — leaking fake timers hangs later tests

  it('saves 2 seconds after the last keystroke', async () => {
    const save = vi.fn()
    render(AutoSaveEditor, { props: { onSave: save } })

    await fireEvent.update(screen.getByRole('textbox'), 'hello')

    await vi.advanceTimersByTimeAsync(1999)
    expect(save).not.toHaveBeenCalled()

    await vi.advanceTimersByTimeAsync(1)
    expect(save).toHaveBeenCalledOnce()
  })
})
```

Rules:

- Use the **async** advancers (`advanceTimersByTimeAsync`, `runAllTimersAsync`) so pending microtasks between timer callbacks also flush.
- Always restore real timers in `afterEach`.
- `userEvent` schedules its own delays; with fake timers use `userEvent.setup({ advanceTimers: vi.advanceTimersByTime })`.
- Freeze the clock for date-dependent output: `vi.setSystemTime(new Date('2026-01-01T00:00:00Z'))`.

## 7. Async Components and `<Suspense>`

A component with top-level `await` in `<script setup>` renders nothing until resolved, and must be mounted inside `<Suspense>`.

```ts
import { defineComponent, h, Suspense } from 'vue'

function mountSuspended(Component: unknown, props: Record<string, unknown> = {}) {
  return mount(defineComponent({
    render: () => h(Suspense, null, {
      default: () => h(Component as never, props),
      fallback: () => h('div', { 'data-testid': 'fallback' }, 'Loading'),
    }),
  }))
}

it('renders the dashboard after async setup resolves', async () => {
  const wrapper = mountSuspended(AsyncDashboard)

  expect(wrapper.get('[data-testid="fallback"]').text()).toBe('Loading')

  await flushPromises()

  expect(wrapper.text()).toContain('Revenue')
})
```

For `defineAsyncComponent`, `flushPromises()` alone usually suffices because the dynamic import resolves as a microtask:

```ts
it('renders the lazily loaded chart', async () => {
  const wrapper = mount(Parent)
  await flushPromises()
  expect(wrapper.findComponent({ name: 'RevenueChart' }).exists()).toBe(true)
})
```

Nuxt projects can use `mountSuspended` from `@nuxt/test-utils` instead of hand-rolling the wrapper.

## 8. Loading / Success / Error Sequences

Assert the **whole** sequence, not just the end state — a component that skips its loading state is a real bug.

```ts
it('shows loading, then the results', async () => {
  render(SearchResults, { props: { query: 'vue' } })

  expect(screen.getByRole('status')).toHaveTextContent('Loading')

  await flushPromises()

  expect(screen.queryByRole('status')).not.toBeInTheDocument()
  expect(screen.getByRole('list')).toBeInTheDocument()
})

it('shows an error message when the request fails', async () => {
  server.use(http.get('/api/search', () => HttpResponse.error()))
  render(SearchResults, { props: { query: 'vue' } })

  expect(await screen.findByRole('alert')).toHaveTextContent(/could not load/i)
})
```

## 9. Debounced Input

```ts
it('searches once after the user stops typing', async () => {
  vi.useFakeTimers()
  const user = userEvent.setup({ advanceTimers: vi.advanceTimersByTime })
  const onSearch = vi.fn()
  render(SearchBox, { props: { onSearch } })

  await user.type(screen.getByRole('searchbox'), 'vue')
  expect(onSearch).not.toHaveBeenCalled()

  await vi.advanceTimersByTimeAsync(300)
  expect(onSearch).toHaveBeenCalledExactlyOnceWith('vue')

  vi.useRealTimers()
})
```

## 10. Race Conditions and Cleanup

Verify that a superseded request does not overwrite fresh data — this is the bug `AbortController` cleanup exists to prevent.

```ts
it('ignores the response of a superseded request', async () => {
  let resolveFirst!: (v: unknown) => void
  server.use(
    http.get('/api/search', ({ request }) => {
      const q = new URL(request.url).searchParams.get('q')
      if (q === 'a') return new Promise(r => { resolveFirst = r as never })
      return HttpResponse.json([{ id: '2', title: 'B result' }])
    }),
  )

  const { rerender } = render(SearchResults, { props: { query: 'a' } })
  await rerender({ query: 'b' })
  await flushPromises()

  resolveFirst(HttpResponse.json([{ id: '1', title: 'A result' }]))
  await flushPromises()

  expect(screen.getByText('B result')).toBeInTheDocument()
  expect(screen.queryByText('A result')).not.toBeInTheDocument()
})
```

## 11. Unhandled Rejections Must Fail

```ts
// src/test/setup.ts
process.on('unhandledRejection', (reason) => { throw reason })
```

Without this, a rejected promise inside a component logs a warning and the test still passes.

## Diagnosing a Flaky Async Test

1. Is every interaction `await`ed?
2. Is there a promise chain that needs `flushPromises()` rather than one `nextTick()`?
3. Is there a `setTimeout` sleep anywhere? Replace it.
4. Are fake timers restored in `afterEach`?
5. Does the test depend on data created by another test?
6. Does it pass with `vitest --sequence.shuffle`?
7. Does it pass with `--no-threads` (concurrency issue) or in isolation (state leak)?

## Anti-Patterns

| Anti-pattern | Consequence | Fix |
|---|---|---|
| `setTimeout` sleep | Flake on CI, slow suite | `flushPromises` / `vi.waitFor` / `findBy*` |
| One `nextTick()` after a fetch | Assertion runs before data arrives | `flushPromises()` |
| Missing `await` on `trigger`/`userEvent` | Asserts the pre-update DOM | `await` it |
| Fake timers not restored | Later tests hang | `vi.useRealTimers()` in `afterEach` |
| Sync timer advancers with async code | Microtasks never flush | `advanceTimersByTimeAsync` |
| Async-setup component mounted directly | Renders nothing | Wrap in `<Suspense>` |
| Only the final state asserted | Skipped loading state goes unnoticed | Assert the sequence |
| Unhandled rejection ignored | Green test hiding a real error | Fail on `unhandledRejection` |
| Chained `flushPromises()` calls | Guessing at tick counts | `vi.waitFor` / `findBy*` |
