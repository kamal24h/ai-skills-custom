# Vitest Setup for Vue

Configuring Vitest so tests share the app's Vite resolution, and so failures are loud rather than silent.

## 1. Install

```bash
pnpm add -D vitest @vitejs/plugin-vue @vue/test-utils jsdom
pnpm add -D @testing-library/vue @testing-library/user-event @testing-library/jest-dom   # optional but recommended
pnpm add -D msw
pnpm add -D @vitest/coverage-v8
```

Vitest is the default for Vue because it reuses the project's Vite config — aliases, plugins, env vars, and SFC compilation behave exactly as in the app. Jest requires a parallel transform pipeline that drifts from production.

## 2. Configuration

```ts
// vitest.config.ts
import { fileURLToPath, URL } from 'node:url'
import { defineConfig, mergeConfig } from 'vitest/config'
import viteConfig from './vite.config'

export default mergeConfig(viteConfig, defineConfig({
  test: {
    globals: true,                      // describe/it/expect without imports
    environment: 'jsdom',
    setupFiles: ['./src/test/setup.ts'],
    include: ['src/**/*.{test,spec}.{ts,tsx}'],
    exclude: ['**/node_modules/**', '**/e2e/**'],
    clearMocks: true,
    restoreMocks: true,
    css: false,                         // true only if a test asserts on styles
    coverage: {
      provider: 'v8',
      reporter: ['text', 'lcov', 'html'],
      exclude: ['src/main.ts', '**/*.d.ts', 'src/test/**', '**/types.ts'],
      thresholds: { lines: 80, functions: 80, branches: 70, statements: 80 },
    },
  },
  resolve: {
    alias: { '@': fileURLToPath(new URL('./src', import.meta.url)) },
  },
}))
```

`mergeConfig(viteConfig, …)` is the important line — without it, aliases and plugins silently diverge from the app build.

### Multiple environments in one repo

```ts
// vitest.config.ts — Vitest projects
export default defineConfig({
  test: {
    projects: [
      {
        extends: true,
        test: { name: 'unit', environment: 'node', include: ['src/**/*.spec.ts'] },
      },
      {
        extends: true,
        test: { name: 'component', environment: 'jsdom', include: ['src/**/*.test.ts'], setupFiles: ['./src/test/setup.ts'] },
      },
    ],
  },
})
```

Pure logic runs faster in `node`; only component tests pay the jsdom cost.

## 3. Setup File

```ts
// src/test/setup.ts
import { afterAll, afterEach, beforeAll, expect, vi } from 'vitest'
import { cleanup } from '@testing-library/vue'
import * as matchers from '@testing-library/jest-dom/matchers'
import { config } from '@vue/test-utils'
import { server } from './msw/server'

expect.extend(matchers)

// --- MSW ---
beforeAll(() => server.listen({ onUnhandledRequest: 'error' }))
afterEach(() => server.resetHandlers())
afterAll(() => server.close())

// --- DOM cleanup ---
afterEach(() => {
  cleanup()
  document.body.innerHTML = ''
})

// --- Global VTU config ---
config.global.stubs = {
  // Only genuinely global, genuinely heavy things belong here
}

// --- Fail loudly on Vue warnings ---
const originalWarn = console.warn
console.warn = (...args: unknown[]) => {
  if (typeof args[0] === 'string' && args[0].includes('[Vue warn]')) {
    throw new Error(args.join(' '))
  }
  originalWarn(...args)
}

// --- jsdom gaps ---
Object.defineProperty(window, 'matchMedia', {
  writable: true,
  value: vi.fn().mockImplementation((query: string) => ({
    matches: false, media: query, onchange: null,
    addEventListener: vi.fn(), removeEventListener: vi.fn(), dispatchEvent: vi.fn(),
    addListener: vi.fn(), removeListener: vi.fn(),
  })),
})

globalThis.ResizeObserver = class {
  observe() {} unobserve() {} disconnect() {}
} as unknown as typeof ResizeObserver

globalThis.IntersectionObserver = class {
  observe() {} unobserve() {} disconnect() {} takeRecords() { return [] }
  root = null; rootMargin = ''; thresholds = []
} as unknown as typeof IntersectionObserver
```

**Failing on `[Vue warn]`** is the highest-value line in this file. It turns silent contract violations (missing keys, mutated props, undeclared emits, failed injections) into red tests.

## 4. jsdom Limits

jsdom implements the DOM API but **not** a layout or rendering engine:

| Not available in jsdom | Consequence |
|---|---|
| Layout / box model | `offsetWidth`, `getBoundingClientRect()` return 0 |
| Computed styles from stylesheets | `getComputedStyle` reflects inline styles only |
| Real scrolling | `scrollTo`, `scrollIntoView` are no-ops |
| `IntersectionObserver`, `ResizeObserver` | Must be polyfilled or stubbed |
| `matchMedia` | Must be stubbed |
| Canvas / WebGL | Needs `canvas` package or stubbing |
| Real focus semantics in a detached tree | Focus assertions need `attachTo: document.body` |

If a test needs any of these for real, that is the signal to move it to Vitest Browser Mode — not to write elaborate mocks.

## 5. Scripts

```jsonc
{
  "scripts": {
    "test": "vitest",
    "test:run": "vitest run",
    "test:ui": "vitest --ui",
    "test:coverage": "vitest run --coverage",
    "test:e2e": "playwright test"
  }
}
```

## 6. Directory Layout

```
src/
  components/
    UserCard.vue
    UserCard.test.ts          # colocated with the unit
  composables/
    useCart.ts
    useCart.test.ts
  test/
    setup.ts
    render.ts                 # shared render helpers
    factories.ts              # test data builders
    msw/
      server.ts
      handlers.ts
e2e/
  checkout.spec.ts            # Playwright, excluded from Vitest
```

Colocation keeps tests visible during refactors. Shared infrastructure lives in `src/test/`.

## 7. Test Data Factories

```ts
// src/test/factories.ts
import type { User, CartItem } from '@/types'

export function makeUser(overrides: Partial<User> = {}): User {
  return { id: 'u1', name: 'Ada Lovelace', email: 'ada@example.com', role: 'member', ...overrides }
}

export function makeCartItem(overrides: Partial<CartItem> = {}): CartItem {
  return { id: 'i1', name: 'Widget', price: 1000, qty: 1, ...overrides }
}
```

Factories keep tests focused on the one field that matters:

```ts
const admin = makeUser({ role: 'admin' })   // intent is obvious
```

## 8. Shared Render Helper

```ts
// src/test/render.ts
import { render, type RenderOptions } from '@testing-library/vue'
import { createTestingPinia } from '@pinia/testing'
import { createRouter, createMemoryHistory } from 'vue-router'
import { routes } from '@/router/routes'
import { vi } from 'vitest'

export function renderWithApp(
  component: unknown,
  options: RenderOptions<never> & { initialState?: Record<string, unknown>; route?: string } = {},
) {
  const { initialState, route = '/', ...rest } = options
  const router = createRouter({ history: createMemoryHistory(), routes })
  router.push(route)

  return {
    router,
    ...render(component as never, {
      ...rest,
      global: {
        plugins: [
          createTestingPinia({ initialState, createSpy: vi.fn }),
          router,
        ],
        ...rest.global,
      },
    }),
  }
}
```

A fresh router and a fresh Pinia per call — never module-level singletons.

## 9. Debugging Tests

```ts
screen.debug()                  // print the current DOM
screen.debug(element)           // print one element
console.log(wrapper.html())     // VTU equivalent

// Run a subset
it.only('…')
describe.skip('…')

// Verify order independence
// vitest --sequence.shuffle
```

`vitest --ui` gives a browser view of results, module graph, and per-test DOM.

## Anti-Patterns

| Anti-pattern | Consequence | Fix |
|---|---|---|
| Vitest config not merged with Vite config | Aliases/plugins diverge from the app | `mergeConfig(viteConfig, …)` |
| Vue warnings only logged | Silent contract violations | Throw on `[Vue warn]` |
| No `restoreMocks` | Mocks leak between tests | `restoreMocks: true` |
| MSW without `onUnhandledRequest: 'error'` | Real requests slip through | Set it to `error` |
| Elaborate layout mocks in jsdom | Tests assert the mock, not the app | Move to Browser Mode |
| Shared router/Pinia instance | Cross-test state leakage | Fresh instances per render |
| jsdom for every test including pure logic | Slow suite | Vitest projects with a `node` project |
| E2E specs matched by `include` | Playwright specs run under Vitest | Exclude `e2e/**` |

## Sources

- [Vitest — Getting started](https://vitest.dev/guide/)
- [Vitest — Configuration](https://vitest.dev/config/)
