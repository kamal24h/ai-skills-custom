# Testing Pinia Stores

Two distinct jobs: testing a store's own logic, and testing a component that consumes a store.

```bash
pnpm add -D @pinia/testing
```

## 1. Store Unit Tests — Real Pinia

```ts
import { createPinia, setActivePinia } from 'pinia'
import { useCartStore } from './cart'
import { makeCartItem } from '@/test/factories'

describe('cart store', () => {
  beforeEach(() => {
    setActivePinia(createPinia())     // fresh, isolated store per test
  })

  it('starts empty', () => {
    const cart = useCartStore()
    expect(cart.items).toEqual([])
    expect(cart.total).toBe(0)
    expect(cart.isEmpty).toBe(true)
  })

  it('increases the quantity when the same product is added twice', () => {
    const cart = useCartStore()
    const widget = makeCartItem({ id: 'p1', qty: 1 })

    cart.add(widget)
    cart.add(widget)

    expect(cart.items).toHaveLength(1)
    expect(cart.items[0].qty).toBe(2)
    expect(cart.count).toBe(2)
  })

  it('removes an item by id', () => {
    const cart = useCartStore()
    cart.add(makeCartItem({ id: 'p1' }))
    cart.add(makeCartItem({ id: 'p2' }))

    cart.remove('p1')

    expect(cart.items.map(i => i.id)).toEqual(['p2'])
  })
})
```

Without `setActivePinia(createPinia())` you get **"getActivePinia() was called but there was no active Pinia"** — that error always means this line is missing (or the store was used at module scope).

## 2. Async Actions

Mock the network beneath the action; run the real action.

```ts
import { http, HttpResponse } from 'msw'
import { server } from '@/test/msw/server'

it('clears the cart after a successful checkout', async () => {
  server.use(http.post('/api/checkout', () => HttpResponse.json({ orderId: 'o1' })))
  const cart = useCartStore()
  cart.add(makeCartItem())

  await cart.checkout()

  expect(cart.items).toEqual([])
  expect(cart.status).toBe('idle')
})

it('keeps the cart and records an error when checkout fails', async () => {
  server.use(http.post('/api/checkout', () => HttpResponse.json({ message: 'Payment declined' }, { status: 402 })))
  const cart = useCartStore()
  cart.add(makeCartItem())

  await expect(cart.checkout()).rejects.toThrow()

  expect(cart.items).toHaveLength(1)
  expect(cart.status).toBe('error')
})
```

## 3. Stores That Use Other Stores

```ts
it('blocks checkout when the user is not authenticated', () => {
  setActivePinia(createPinia())
  const auth = useAuthStore()
  const cart = useCartStore()
  const checkout = useCheckoutStore()

  cart.add(makeCartItem())
  auth.user = null

  expect(checkout.canCheckout).toBe(false)
})
```

Because all stores share the active Pinia, the real dependency graph is exercised — no mocking needed.

## 4. Component Tests — `createTestingPinia`

```ts
import { createTestingPinia } from '@pinia/testing'
import { render, screen } from '@testing-library/vue'
import { vi } from 'vitest'
import CartSummary from './CartSummary.vue'

it('renders the formatted total from the store', () => {
  render(CartSummary, {
    global: {
      plugins: [createTestingPinia({
        createSpy: vi.fn,
        initialState: {
          cart: { items: [makeCartItem({ price: 1500, qty: 2 })] },
        },
      })],
    },
  })

  expect(screen.getByTestId('total')).toHaveTextContent('30.00')
})
```

`createTestingPinia` seeds state via `initialState` (keyed by store id) and **stubs all actions by default**, replacing them with spies.

### Asserting that an action was called

```ts
it('calls checkout when the button is clicked', async () => {
  render(CartSummary, {
    global: { plugins: [createTestingPinia({ createSpy: vi.fn, initialState: { cart: { items: [makeCartItem()] } } })] },
  })
  const cart = useCartStore()      // returns the testing store

  await userEvent.click(screen.getByRole('button', { name: 'Checkout' }))

  expect(cart.checkout).toHaveBeenCalledOnce()
})
```

### When you need the real action to run

```ts
render(CartPage, {
  global: {
    plugins: [createTestingPinia({ createSpy: vi.fn, stubActions: false })],
  },
})
```

With `stubActions: false` the real action executes (still spied, so you can assert calls) — pair it with MSW for the network layer.

**This is the most common Pinia testing mistake:** stubbing actions and then asserting that state changed. Stubbed actions do nothing, so the state never changes and the test fails for a confusing reason.

| Goal | Setting |
|---|---|
| Assert the component *calls* the action | default (`stubActions: true`) |
| Assert what the action *does* to state/UI | `stubActions: false` + MSW |

### Overriding a getter

Getters are computed from state, so seed the state instead. When a getter must be forced (complex derivation not under test):

```ts
const cart = useCartStore()
// @ts-expect-error — testing-only getter override
cart.total = 9999
```

Prefer seeding state; a forced getter means the test no longer reflects reality.

## 5. Isolation

```ts
// ❌ leaks into the next test
const cart = useCartStore()
cart.items.push(makeCartItem())

// ✅ seed per mount
createTestingPinia({ initialState: { cart: { items: [makeCartItem()] } } })
```

`createTestingPinia` creates a fresh Pinia per call, so a per-test `render` gives isolation automatically. Store unit tests need `setActivePinia(createPinia())` in `beforeEach`.

## 6. Setup Stores and Returned State

`initialState` can only seed state the store **returns**. A setup store that keeps a ref private is unreachable from tests, DevTools, SSR, and plugins.

```ts
// ❌ `status` cannot be seeded or inspected
return { items, add, remove }

// ✅
return { items, status, count, total, add, remove, checkout }
```

If a test needs to seed state that the store does not return, the fix is in the store, not the test.

## 7. Subscriptions and Plugins

```ts
it('persists the cart on every change', () => {
  setActivePinia(createPinia())
  const cart = useCartStore()
  const spy = vi.fn()
  cart.$subscribe(spy)

  cart.add(makeCartItem())

  expect(spy).toHaveBeenCalled()
})

it('logs each action', () => {
  const log = vi.fn()
  const pinia = createPinia()
  pinia.use(({ store }) => { store.$onAction(({ name }) => log(name)) })
  setActivePinia(pinia)

  useCartStore().add(makeCartItem())

  expect(log).toHaveBeenCalledWith('add')
})
```

## 8. Coverage Checklist

- [ ] Initial state of every returned ref
- [ ] Every getter, including edge cases (empty, boundary)
- [ ] Every action's effect on state
- [ ] Async actions: loading, success, and failure transitions
- [ ] Cross-store interactions
- [ ] Reset behavior (if the store exposes `$reset` or an equivalent)
- [ ] Components: renders store state, calls the right actions

## Anti-Patterns

| Anti-pattern | Consequence | Fix |
|---|---|---|
| Missing `setActivePinia` | "no active Pinia" error | `setActivePinia(createPinia())` in `beforeEach` |
| `vi.mock('@/stores/cart')` | Store contract untested, brittle | `createTestingPinia` |
| Stubbed actions + state assertions | State never changes; confusing failure | `stubActions: false` |
| Mutating a shared store between tests | Order-dependent suite | `initialState` per mount |
| Store state not returned from a setup store | Unseedable, invisible in DevTools | Return everything |
| Asserting on `$state` internals a component never shows | Implementation coupling | Assert getters/rendered output |
| Mocking the API module instead of the network | Real client code untested | MSW |
| One store instance shared at module scope | Cross-test leakage | Fresh Pinia per test |
