# End-to-End Testing with Playwright

Playwright is the recommended E2E runner for Vue apps: cross-browser, auto-waiting, first-class tracing, and no framework coupling.

## 1. Scope

E2E is expensive. Cover a small set of **critical user journeys** end to end:

- Sign up / sign in / sign out
- The primary conversion path (checkout, submit application, publish)
- One representative CRUD lifecycle
- Any flow where a failure is business-critical

Everything else — field validation, empty states, error copy, component variants — belongs in component tests, which are an order of magnitude faster and easier to debug.

## 2. Setup

```bash
pnpm create playwright
```

```ts
// playwright.config.ts
import { defineConfig, devices } from '@playwright/test'

export default defineConfig({
  testDir: './e2e',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 2 : undefined,
  reporter: process.env.CI ? [['html'], ['github']] : 'list',

  use: {
    baseURL: 'http://localhost:4173',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },

  projects: [
    { name: 'setup', testMatch: /global\.setup\.ts/ },
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'], storageState: 'e2e/.auth/user.json' },
      dependencies: ['setup'],
    },
    {
      name: 'mobile',
      use: { ...devices['Pixel 7'], storageState: 'e2e/.auth/user.json' },
      dependencies: ['setup'],
    },
  ],

  webServer: {
    command: 'pnpm build && pnpm preview',
    url: 'http://localhost:4173',
    reuseExistingServer: !process.env.CI,
    timeout: 120_000,
  },
})
```

Test the **preview build**, not the dev server — dev-only behavior (HMR, unminified code, different chunking) hides real production bugs.

## 3. Selectors

```ts
// ✅ user-visible, survives refactors
page.getByRole('button', { name: 'Add to cart' })
page.getByLabel('Email')
page.getByPlaceholder('Search products')
page.getByText('Order confirmed')
page.getByTestId('cart-total')

// ❌ structural, breaks on any markup change
page.locator('.btn-primary')
page.locator('div > ul > li:nth-child(3)')
page.locator('//div[@class="card"]/button')
```

Configure the test-id attribute if your project uses a different name:

```ts
use: { testIdAttribute: 'data-test' }
```

## 4. Web-First Assertions

```ts
// ✅ retries until the timeout
await expect(page.getByRole('alert')).toBeVisible()
await expect(page.getByTestId('total')).toHaveText('₺300,00')
await expect(page).toHaveURL(/\/orders\/\d+/)
await expect(page.getByRole('listitem')).toHaveCount(3)
await expect(page.getByRole('button', { name: 'Pay' })).toBeEnabled()

// ❌ samples once — flaky
expect(await page.getByTestId('total').textContent()).toBe('₺300,00')
```

Never use `page.waitForTimeout()`. Wait for a state instead:

```ts
await page.waitForURL('**/checkout/success')
await page.waitForResponse(r => r.url().includes('/api/orders') && r.ok())
await expect(page.getByRole('progressbar')).toBeHidden()
```

## 5. Authentication via `storageState`

```ts
// e2e/global.setup.ts
import { test as setup, expect } from '@playwright/test'

const authFile = 'e2e/.auth/user.json'

setup('authenticate', async ({ page }) => {
  await page.goto('/login')
  await page.getByLabel('Email').fill(process.env.E2E_USER!)
  await page.getByLabel('Password').fill(process.env.E2E_PASSWORD!)
  await page.getByRole('button', { name: 'Sign in' }).click()

  await expect(page.getByRole('heading', { name: 'Dashboard' })).toBeVisible()
  await page.context().storageState({ path: authFile })
})
```

Every other spec starts authenticated. Test the login **flow itself** in exactly one spec, with `storageState: { cookies: [], origins: [] }` to opt out.

Add `e2e/.auth/` to `.gitignore`.

## 6. Page Objects

```ts
// e2e/pages/CheckoutPage.ts
import type { Page, Locator } from '@playwright/test'

export class CheckoutPage {
  readonly total: Locator
  readonly payButton: Locator

  constructor(private readonly page: Page) {
    this.total = page.getByTestId('order-total')
    this.payButton = page.getByRole('button', { name: 'Pay now' })
  }

  async goto() { await this.page.goto('/checkout') }

  async fillCard(number: string, expiry: string, cvc: string) {
    await this.page.getByLabel('Card number').fill(number)
    await this.page.getByLabel('Expiry').fill(expiry)
    await this.page.getByLabel('CVC').fill(cvc)
  }

  async pay() { await this.payButton.click() }
}
```

Page objects expose **locators and actions**, never assertions — assertions stay in the test so failures point at the spec.

## 7. A Complete Journey

```ts
import { expect, test } from '@playwright/test'
import { CheckoutPage } from './pages/CheckoutPage'

test.describe('checkout', () => {
  test('completes a purchase and shows the order confirmation', async ({ page }) => {
    // Arrange
    await page.goto('/products/widget')

    // Act
    await page.getByRole('button', { name: 'Add to cart' }).click()
    await expect(page.getByTestId('cart-count')).toHaveText('1')

    const checkout = new CheckoutPage(page)
    await checkout.goto()
    await checkout.fillCard('4242424242424242', '12/30', '123')
    await checkout.pay()

    // Assert
    await expect(page).toHaveURL(/\/orders\/[\w-]+/)
    await expect(page.getByRole('heading', { name: 'Order confirmed' })).toBeVisible()
    await expect(page.getByTestId('order-total')).toHaveText('₺300,00')
  })

  test('shows a decline message when the payment fails', async ({ page }) => {
    await page.route('**/api/payments', route =>
      route.fulfill({ status: 402, json: { message: 'Card declined' } }))

    await page.goto('/checkout')
    await new CheckoutPage(page).pay()

    await expect(page.getByRole('alert')).toHaveText('Card declined')
    await expect(page).toHaveURL(/\/checkout/)   // stays put
  })
})
```

## 8. Network Control

```ts
// Stub a specific endpoint
await page.route('**/api/products', route =>
  route.fulfill({ json: [{ id: 'p1', name: 'Widget', price: 15000 }] }))

// Simulate an outage
await page.route('**/api/**', route => route.abort())

// Inspect without changing behavior
page.on('request', r => console.log(r.method(), r.url()))
```

Decide deliberately whether a journey runs against a **seeded real backend** (highest fidelity, needs data management) or against **stubbed routes** (fast and deterministic, but no longer end-to-end). Mixed suites are fine — document which specs are which.

## 9. Test Independence

```ts
test.beforeEach(async ({ request }) => {
  await request.post('/api/test/reset')          // reset to a known state
})

test('creates a product', async ({ page }) => {
  const name = `Widget ${Date.now()}`            // unique data per test
  // ...
})
```

Each test creates its own data. `fullyParallel: true` means shared fixtures will collide.

## 10. Debugging

```bash
pnpm exec playwright test --ui           # time-travel UI runner
pnpm exec playwright test --debug        # step through with Inspector
pnpm exec playwright test --headed
pnpm exec playwright show-trace trace.zip
pnpm exec playwright codegen localhost:4173
```

`trace: 'on-first-retry'` gives a full DOM/network/console recording of exactly the run that failed — the single most valuable setting for CI debugging.

## 11. CI

```yaml
- run: pnpm exec playwright install --with-deps chromium
- run: pnpm exec playwright test --shard=${{ matrix.shard }}/4
- uses: actions/upload-artifact@v4
  if: ${{ !cancelled() }}
  with:
    name: playwright-report-${{ matrix.shard }}
    path: playwright-report/
    retention-days: 7
```

Cache the browser binaries; keep `retries: 2` on CI but treat a test that only passes on retry as a bug to fix, not a result to accept.

## Anti-Patterns

| Anti-pattern | Consequence | Fix |
|---|---|---|
| E2E for field-level validation | Slow, flaky, expensive | Component tests |
| CSS/XPath selectors | Break on any markup change | Role/label/testid |
| `waitForTimeout` | Flake and wasted time | Web-first assertions |
| `expect(await locator.textContent())` | Samples once | `await expect(locator).toHaveText()` |
| UI login in every spec | Minutes of wasted runtime | `storageState` |
| Tests sharing data | Parallel collisions | Per-test data + reset |
| Assertions inside page objects | Failures point at the wrong file | Assertions in the spec |
| Testing the dev server | Dev-only behavior masks bugs | `build` + `preview` |
| Retries without investigation | Real races ship | Fix the root cause |
| No trace/artifacts | CI failures undiagnosable | `trace: 'on-first-retry'` + upload |
