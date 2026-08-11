# TDD Workflow for Vue

RED → GREEN → REFACTOR applied to Vue components, composables, and stores.

## The Cycle

| Phase | Goal | Rule |
|---|---|---|
| **RED** | Write a failing test that describes the desired behavior | Run it and **watch it fail for the right reason** |
| **GREEN** | Write the minimum code to pass | No extra features, no speculative abstraction |
| **REFACTOR** | Improve structure with the test as a safety net | No behavior change; tests stay green |

Never skip RED. A test that has never failed proves nothing — it may be asserting something that is trivially true.

## 1. Start From the Contract

Before writing a test, state the component's contract in one sentence per line:

```
CartSummary
- renders the formatted total from the cart store
- shows an empty state when the cart has no items
- disables Checkout while the cart is empty
- emits nothing; it calls the store's checkout action
- shows an error message when checkout fails
```

Each line becomes an `it(...)`. This is design work, and doing it before implementation is where most of TDD's value comes from.

## 2. Worked Example — A Composable

### RED

```ts
// useCart.test.ts
import { describe, expect, it } from 'vitest'
import { useCart } from './useCart'
import { makeCartItem } from '@/test/factories'

describe('useCart', () => {
  it('starts empty', () => {
    const { items, total, isEmpty } = useCart()

    expect(items.value).toEqual([])
    expect(total.value).toBe(0)
    expect(isEmpty.value).toBe(true)
  })
})
```

```
FAIL  src/composables/useCart.test.ts
  Failed to resolve import "./useCart"
```

Failing for the right reason: the module does not exist yet.

### GREEN

```ts
// useCart.ts
import { computed, ref } from 'vue'
import type { CartItem } from '@/types'

export function useCart() {
  const items = ref<CartItem[]>([])
  const total = computed(() => items.value.reduce((n, i) => n + i.price * i.qty, 0))
  const isEmpty = computed(() => items.value.length === 0)

  return { items, total, isEmpty }
}
```

Green. Nothing more — no `add`, no `remove`, no persistence yet.

### RED again — next behavior

```ts
it('increases the quantity when the same product is added twice', () => {
  const { items, add } = useCart()
  const widget = makeCartItem({ id: 'p1', qty: 1 })

  add(widget)
  add(widget)

  expect(items.value).toHaveLength(1)
  expect(items.value[0].qty).toBe(2)
})
```

### GREEN

```ts
function add(item: CartItem) {
  const existing = items.value.find(i => i.id === item.id)
  if (existing) existing.qty += item.qty
  else items.value.push({ ...item })
}
```

### REFACTOR

Once several behaviors are green, improve structure — extract a lookup map, switch to immutable updates, split a large composable — running the tests after every step.

## 3. Worked Example — A Component

### RED

```ts
// CartSummary.test.ts
import { render, screen } from '@testing-library/vue'
import { createTestingPinia } from '@pinia/testing'
import { vi } from 'vitest'
import CartSummary from './CartSummary.vue'
import { makeCartItem } from '@/test/factories'

it('renders the formatted total from the cart store', () => {
  render(CartSummary, {
    global: {
      plugins: [createTestingPinia({
        createSpy: vi.fn,
        initialState: { cart: { items: [makeCartItem({ price: 1500, qty: 2 })] } },
      })],
    },
  })

  expect(screen.getByTestId('total')).toHaveTextContent('₺30,00')
})
```

### GREEN

```vue
<script setup lang="ts">
import { storeToRefs } from 'pinia'
import { useCartStore } from '@/stores/cart'
import { formatMoney } from '@/utils/format'

const cart = useCartStore()
const { total } = storeToRefs(cart)
</script>

<template>
  <p data-testid="total">{{ formatMoney(total) }}</p>
</template>
```

### RED — the next behavior

```ts
it('disables Checkout when the cart is empty', () => {
  render(CartSummary, {
    global: { plugins: [createTestingPinia({ createSpy: vi.fn, initialState: { cart: { items: [] } } })] },
  })

  expect(screen.getByRole('button', { name: 'Checkout' })).toBeDisabled()
})
```

Continue one behavior at a time. Each cycle is small enough that when a test goes red you know exactly which change caused it.

## 4. Order of Behaviors

1. **Happy path** — the core value of the unit
2. **Empty / zero state** — often the most-shipped bug
3. **Error path** — network failure, validation failure, permission denial
4. **Boundaries** — 0, 1, max, exactly-at-limit
5. **Interaction details** — disabled while pending, focus management, keyboard access

Writing the happy path first keeps the design honest; writing the error path immediately after keeps it realistic.

## 5. Bug-Driven TDD

When a bug is reported:

1. Write a test that **reproduces** it. Watch it fail — this proves you understood the bug.
2. Fix the code until the test passes.
3. Keep the test forever as a regression guard, named after the behavior:
   ```ts
   it('keeps the newest search results when an earlier request resolves late', async () => { … })
   ```

Never fix a bug without a failing test first. Without it, you cannot know whether the fix addressed the actual cause.

## 6. What Not to Test-Drive

- Framework behavior (`v-if` hides things, reactivity works)
- Trivial pass-through props with no logic
- Third-party library internals
- Exact markup structure (test behavior, not DOM shape)
- Styling that is not behavior (colors, spacing) — unless it encodes state

## 7. TDD and Refactoring Vue Components

Because the tests assert the **contract** (rendered output, emits, side effects), you can restructure freely with the suite as a net:

- Split one component into several
- Extract state and effects into a composable
- Replace a manual `modelValue` prop with `defineModel`
- Move from `ref` to `shallowRef`
- Switch from a local store to Pinia

If a refactor breaks tests without changing behavior, the tests were coupled to implementation — fix the tests first, then continue.

## 8. Practical Rhythm

```bash
pnpm vitest --watch          # keep it running for the whole session
pnpm vitest CartSummary      # narrow to the file you are working on
```

- Cycles of 1–5 minutes. If a cycle takes longer, the step was too big.
- Commit at every green.
- Never refactor while red.
- If you cannot write the test, the design is unclear — that is the real signal, and it is worth acting on before writing code.

## Anti-Patterns

| Anti-pattern | Consequence | Fix |
|---|---|---|
| Skipping RED | Test may assert nothing | Always watch it fail first |
| Writing tests after the code | Tests shaped by the implementation | Test first |
| Test fails for the wrong reason | False confidence | Read the failure message |
| Implementing beyond the test | Untested speculative code | Minimum to pass |
| Refactoring while red | Two problems at once | Green first |
| Testing implementation details | Refactors break tests | Assert the contract |
| Bug fixed without a test | No regression guard | Reproduce, then fix |
| Huge cycles | Hard to locate failures | One behavior at a time |
| Only happy paths | Errors and edges ship broken | Order in §4 |
