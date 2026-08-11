# Vitest Browser Mode

Running component tests in a real browser when jsdom cannot express the assertion.

## 1. When to Escalate from jsdom

Stay in jsdom for most component tests — it is faster and simpler. Move a test to Browser Mode when it depends on something jsdom does not implement:

| Need | jsdom | Browser Mode |
|---|---|---|
| Layout / box model (`offsetWidth`, `getBoundingClientRect`) | Always 0 | Real |
| Computed styles from stylesheets | Inline only | Real |
| CSS-driven visibility (`display`, `visibility`, `opacity`) | Unreliable | Real |
| Scroll behavior, sticky/fixed positioning | No-op | Real |
| `IntersectionObserver`, `ResizeObserver` | Must be stubbed | Native |
| Real focus order, `:focus-visible`, tab traversal | Approximate | Real |
| Pointer/drag/touch gestures | Synthetic | Real (CDP-driven) |
| Canvas / WebGL | Needs polyfill | Real |
| Transitions/animations with real timing | Not run | Real |
| Speed | Fast | Slower (real browser startup) |

If you find yourself writing elaborate mocks for layout or styles, that is the signal — the test belongs in Browser Mode, not in a more clever jsdom mock.

## 2. Setup

```bash
pnpm add -D @vitest/browser playwright
pnpm exec playwright install chromium
```

```ts
// vitest.config.ts
import { defineConfig, mergeConfig } from 'vitest/config'
import viteConfig from './vite.config'

export default mergeConfig(viteConfig, defineConfig({
  test: {
    projects: [
      {
        extends: true,
        test: {
          name: 'unit',
          environment: 'jsdom',
          include: ['src/**/*.test.ts'],
          setupFiles: ['./src/test/setup.ts'],
        },
      },
      {
        extends: true,
        test: {
          name: 'browser',
          include: ['src/**/*.browser.test.ts'],
          setupFiles: ['./src/test/setup.browser.ts'],
          browser: {
            enabled: true,
            provider: 'playwright',
            headless: true,
            instances: [{ browser: 'chromium' }],
          },
        },
      },
    ],
  },
}))
```

Two projects, one command. Name browser tests `*.browser.test.ts` so the split is visible in the filename.

## 3. Writing a Browser Test

```ts
import { render } from 'vitest-browser-vue'
import { expect, it } from 'vitest'
import { page, userEvent } from '@vitest/browser/context'
import DataTable from './DataTable.vue'

it('keeps the header sticky while the body scrolls', async () => {
  const screen = render(DataTable, { props: { rows: makeRows(200) } })

  const container = screen.getByTestId('table-scroll')
  await container.element().scrollTo({ top: 500 })

  const header = screen.getByRole('rowgroup', { name: 'Header' })
  expect(header.element().getBoundingClientRect().top).toBe(0)   // real layout
})
```

Key differences from jsdom tests:

- `render` comes from `vitest-browser-vue`, not `@testing-library/vue`.
- Locators are **retriable** — `screen.getByRole(...)` returns a locator, and assertions retry until timeout, like Playwright.
- `userEvent` comes from `@vitest/browser/context` and drives the real browser.
- `element()` unwraps to a real DOM node when you need direct measurement.

## 4. What Browser Mode Tests Well

### Real focus and keyboard traversal

```ts
it('traps focus inside the open dialog', async () => {
  const screen = render(App)
  await userEvent.click(screen.getByRole('button', { name: 'Open' }))

  await userEvent.keyboard('{Tab}{Tab}{Tab}')

  const dialog = screen.getByRole('dialog').element()
  expect(dialog.contains(document.activeElement)).toBe(true)
})
```

### Computed styles

```ts
it('applies the danger token to the error state', async () => {
  const screen = render(Alert, { props: { tone: 'danger' } })
  const el = screen.getByRole('alert').element()

  expect(getComputedStyle(el).color).toBe('rgb(220, 38, 38)')
})
```

### Intersection-driven behavior

```ts
it('loads the next page when the sentinel scrolls into view', async () => {
  const screen = render(InfiniteList)

  await screen.getByTestId('sentinel').element().scrollIntoView()

  await expect.element(screen.getByText('Item 51')).toBeVisible()   // real IntersectionObserver
})
```

### Drag and drop

```ts
it('reorders items by dragging', async () => {
  const screen = render(SortableList, { props: { items: ['a', 'b', 'c'] } })

  await userEvent.dragAndDrop(screen.getByText('c'), screen.getByText('a'))

  await expect.element(screen.getByRole('list')).toHaveTextContent('c a b')
})
```

## 5. Visual Assertions

```ts
await expect(page).toMatchScreenshot('empty-state')
```

Screenshot testing catches regressions that DOM assertions cannot, but it is fragile across OS and browser versions. If you adopt it: pin the browser version, run screenshots only in CI on a fixed container image, and keep the set small (a handful of key states, not every component).

## 6. Browser Mode vs Playwright E2E

| | Vitest Browser Mode | Playwright E2E |
|---|---|---|
| Unit under test | A component, mounted directly | The whole app, through the UI |
| Server needed | No | Yes (dev/preview server) |
| Speed | Seconds | Tens of seconds to minutes |
| Mocking | MSW, `vi.mock`, props, provides | Route interception, real or seeded backend |
| Best for | Component behavior needing real rendering | User journeys across pages |

They are complementary. Browser Mode does not replace E2E, and E2E is the wrong tool for a single component's focus behavior.

## 7. Trade-offs

- **Slower**: real browser startup per run. Keep the browser project small and targeted.
- **CI cost**: requires installing browser binaries; cache them.
- **Debugging**: run with `headless: false` to watch, or use the Vitest UI.
- **Module mocking**: `vi.mock` works, but MSW must run in the browser (`setupWorker`) rather than the Node server.

```ts
// src/test/setup.browser.ts
import { setupWorker } from 'msw/browser'
import { handlers } from './msw/handlers'

const worker = setupWorker(...handlers)
beforeAll(() => worker.start({ onUnhandledRequest: 'error', quiet: true }))
afterEach(() => worker.resetHandlers())
afterAll(() => worker.stop())
```

## 8. Selection Rule

> Write the test in jsdom first. Move it to Browser Mode only when the assertion you need is impossible there — and prefer moving the test over mocking the browser.

## Anti-Patterns

| Anti-pattern | Consequence | Fix |
|---|---|---|
| Every component test in Browser Mode | Slow suite, expensive CI | jsdom by default |
| Mocking `getBoundingClientRect` in jsdom | Asserts the mock, not the layout | Browser Mode |
| Browser Mode used for user journeys | Wrong granularity, awkward setup | Playwright E2E |
| Screenshot tests for every component | Constant false failures | A few key states, pinned environment |
| MSW Node server in Browser Mode | Requests are not intercepted | `setupWorker` from `msw/browser` |
| Browser binaries not cached in CI | Minutes added per run | Cache the Playwright browser path |
| Non-retrying assertions on locators | Flake on timing | `await expect.element(...)` |
