# Component Testing

Testing Vue components through their public contract: rendered output, props, emits, slots, and user interaction.

## 1. What a Component Test Asserts

The component's contract is:

| Input | Output |
|---|---|
| Props | Rendered DOM |
| Slots | Emitted events |
| User interaction | Calls to injected/provided dependencies |
| Injected values | Observable side effects (HTTP, storage, navigation) |

Everything else — refs, computed values, method names, internal structure — is implementation and must not appear in assertions.

```ts
// ❌ implementation-coupled: breaks on any refactor, passes when the UI is broken
expect(wrapper.vm.isOpen).toBe(true)
wrapper.vm.submit()

// ✅ contract-coupled
await userEvent.click(screen.getByRole('button', { name: 'Open' }))
expect(screen.getByRole('dialog')).toBeVisible()
```

## 2. Two Libraries, One Philosophy

**Vue Test Utils** is the official low-level mounting library. **Testing Library** wraps it with accessibility-first queries and user-centric interaction. Both are fine; Testing Library pushes harder toward black-box tests.

### Testing Library

```ts
import { render, screen } from '@testing-library/vue'
import userEvent from '@testing-library/user-event'
import UserCard from './UserCard.vue'
import { makeUser } from '@/test/factories'

it('emits select with the user id when the card is activated', async () => {
  // Arrange
  const user = makeUser({ id: 'u42', name: 'Ada Lovelace' })
  const { emitted } = render(UserCard, { props: { user } })

  // Act
  await userEvent.click(screen.getByRole('button', { name: /select ada lovelace/i }))

  // Assert
  expect(emitted().select).toEqual([['u42']])
})
```

### Vue Test Utils

```ts
import { mount } from '@vue/test-utils'
import UserCard from './UserCard.vue'

it('emits select with the user id when the card is activated', async () => {
  const wrapper = mount(UserCard, { props: { user: makeUser({ id: 'u42' }) } })

  await wrapper.get('[data-testid="select"]').trigger('click')

  expect(wrapper.emitted('select')).toEqual([['u42']])
})
```

## 3. Query Priority

1. `getByRole('button', { name: 'Save' })` — matches how assistive tech and users find things
2. `getByLabelText('Email')` — form controls
3. `getByPlaceholderText`, `getByText`, `getByDisplayValue`
4. `getByTestId('cart-total')` — last resort for non-semantic elements

```ts
// ❌ breaks on restyle; passes even if the button is unreachable
wrapper.find('.btn.btn-primary')
wrapper.findAll('li')[2]

// ✅
screen.getByRole('button', { name: 'Save' })
screen.getByRole('listitem', { name: /widget/i })
```

Query variants:

| Prefix | Returns | Use |
|---|---|---|
| `getBy*` | Element, throws if absent | Element should exist now |
| `queryBy*` | Element or `null` | Assert absence |
| `findBy*` | Promise, retries | Element appears asynchronously |
| `*AllBy*` | Array | Multiple matches |

```ts
expect(screen.queryByRole('alert')).not.toBeInTheDocument()   // absence
expect(await screen.findByRole('alert')).toHaveTextContent('Failed')  // eventual
```

## 4. Props

```ts
it('renders the compact layout when compact is true', () => {
  render(UserCard, { props: { user: makeUser(), compact: true } })
  expect(screen.getByTestId('card')).toHaveClass('is-compact')
})

it('re-renders when the user prop changes', async () => {
  const { rerender } = render(UserCard, { props: { user: makeUser({ name: 'Ada' }) } })
  expect(screen.getByText('Ada')).toBeInTheDocument()

  await rerender({ user: makeUser({ name: 'Grace' }) })
  expect(screen.getByText('Grace')).toBeInTheDocument()
})
```

VTU equivalent: `await wrapper.setProps({ user: … })`.

Test prop **effects**, not prop **assignment** — asserting that a prop equals what you passed tests Vue, not your component.

## 5. Emitted Events

```ts
// Testing Library
expect(emitted().submit).toHaveLength(1)
expect(emitted().submit[0]).toEqual([{ email: 'ada@example.com' }])

// VTU
expect(wrapper.emitted('submit')).toBeTruthy()
expect(wrapper.emitted('submit')![0]).toEqual([{ email: 'ada@example.com' }])
expect(wrapper.emitted('close')).toBeUndefined()   // not emitted
```

## 6. `v-model`

```ts
it('supports v-model', async () => {
  const wrapper = mount(BaseInput, { props: { modelValue: 'a', 'onUpdate:modelValue': (v: string) => wrapper.setProps({ modelValue: v }) } })

  await wrapper.get('input').setValue('ab')

  expect(wrapper.props('modelValue')).toBe('ab')
})
```

Or assert the emit directly, which is simpler and equally valid:

```ts
await wrapper.get('input').setValue('ab')
expect(wrapper.emitted('update:modelValue')).toEqual([['ab']])
```

## 7. Slots

```ts
it('renders default and named slot content', () => {
  render(Card, {
    props: { title: 'Report' },
    slots: {
      default: '<p>Body text</p>',
      footer: '<button>Export</button>',
    },
  })

  expect(screen.getByText('Body text')).toBeInTheDocument()
  expect(screen.getByRole('button', { name: 'Export' })).toBeInTheDocument()
})

it('exposes scoped slot props', () => {
  render(DataList, {
    props: { items: [makeUser({ name: 'Ada' })] },
    slots: { row: `<template #row="{ item }"><span>{{ item.name }}</span></template>` },
  })
  expect(screen.getByText('Ada')).toBeInTheDocument()
})
```

Also assert the **fallback** content when the slot is not provided.

## 8. User Interaction

Prefer `userEvent` — it fires the realistic event sequence (pointerdown, focus, keydown, input, keyup, click) rather than a single synthetic event.

```ts
const user = userEvent.setup()

await user.click(screen.getByRole('button', { name: 'Add' }))
await user.type(screen.getByLabelText('Email'), 'ada@example.com')
await user.clear(screen.getByLabelText('Email'))
await user.selectOptions(screen.getByLabelText('Country'), 'tr')
await user.keyboard('{Escape}')
await user.tab()
await user.hover(screen.getByTestId('tooltip-trigger'))
```

VTU triggers when you need a specific low-level event:

```ts
await wrapper.get('input').setValue('text')
await wrapper.get('form').trigger('submit.prevent')
await wrapper.get('div').trigger('keydown', { key: 'Escape' })
```

**Always `await`.** Vue's DOM updates are asynchronous; assertions in the same tick see the old DOM.

## 9. Mounting Options

```ts
const wrapper = mount(Component, {
  props: { … },
  slots: { default: '…' },
  attachTo: document.body,             // needed for focus/scroll assertions
  global: {
    plugins: [createTestingPinia({ initialState }), router],
    provide: { [themeKey as symbol]: { mode: ref('dark'), toggle: vi.fn() } },
    stubs: { HeavyChart: true },
    directives: { tooltip: () => {} },
    mocks: { $t: (k: string) => k },    // last resort — prefer real plugins
  },
})
```

### `mount` vs `shallowMount`

Default to `mount`. Full rendering catches the parent/child integration bugs that matter.

`shallowMount` (or targeted `stubs`) is justified when a child is genuinely heavy (map, chart, rich editor), depends on unavailable browser APIs, or is thoroughly tested on its own. State the reason in a comment — a reviewer should not have to guess.

```ts
// Chart pulls in a canvas renderer; its rendering is covered by its own test
const wrapper = mount(Dashboard, { global: { stubs: { RevenueChart: true } } })
```

## 10. Teleport

Teleported content is **not** inside `wrapper`.

```ts
// Option A: create the target and query the document
beforeEach(() => {
  const el = document.createElement('div')
  el.id = 'modal-root'
  document.body.appendChild(el)
})

it('renders the dialog into the teleport target', async () => {
  render(App)
  await userEvent.click(screen.getByRole('button', { name: 'Open' }))
  expect(screen.getByRole('dialog')).toBeVisible()   // screen queries document.body
})

// Option B: stub the Teleport so content stays inline
mount(App, { global: { stubs: { teleport: true } } })
```

## 11. Focus, Scroll, and Layout

```ts
it('focuses the input on open', async () => {
  render(SearchPanel, { attachTo: document.body })   // required for focus
  await userEvent.click(screen.getByRole('button', { name: 'Search' }))
  expect(screen.getByLabelText('Query')).toHaveFocus()
})
```

Layout measurements (`offsetWidth`, `getBoundingClientRect`) are always 0 in jsdom. Do not mock them into plausibility — move the test to Browser Mode.

## 12. Accessibility Assertions

Accessible queries already enforce a baseline. Add explicit ARIA assertions where state matters:

```ts
expect(screen.getByRole('button', { name: 'Menu' })).toHaveAttribute('aria-expanded', 'false')
expect(screen.getByLabelText('Email')).toHaveAttribute('aria-invalid', 'true')
expect(screen.getByRole('alert')).toHaveTextContent('Email is required')
```

## 13. A Complete Example

```ts
import { render, screen } from '@testing-library/vue'
import userEvent from '@testing-library/user-event'
import { http, HttpResponse } from 'msw'
import { server } from '@/test/msw/server'
import LoginForm from './LoginForm.vue'

describe('LoginForm', () => {
  it('shows a validation error when the email is empty on submit', async () => {
    // Arrange
    const user = userEvent.setup()
    render(LoginForm)

    // Act
    await user.click(screen.getByRole('button', { name: 'Sign in' }))

    // Assert
    expect(await screen.findByRole('alert')).toHaveTextContent('Email is required')
    expect(screen.getByLabelText('Email')).toHaveAttribute('aria-invalid', 'true')
  })

  it('emits authenticated with the user when credentials are valid', async () => {
    const user = userEvent.setup()
    const { emitted } = render(LoginForm)

    await user.type(screen.getByLabelText('Email'), 'ada@example.com')
    await user.type(screen.getByLabelText('Password'), 'correct-horse')
    await user.click(screen.getByRole('button', { name: 'Sign in' }))

    expect(await screen.findByText('Welcome back')).toBeInTheDocument()
    expect(emitted().authenticated?.[0]).toEqual([{ id: 'u1', email: 'ada@example.com' }])
  })

  it('shows a server error message when the API rejects the credentials', async () => {
    server.use(http.post('/api/login', () => HttpResponse.json({ message: 'Invalid credentials' }, { status: 401 })))
    const user = userEvent.setup()
    render(LoginForm)

    await user.type(screen.getByLabelText('Email'), 'ada@example.com')
    await user.type(screen.getByLabelText('Password'), 'wrong')
    await user.click(screen.getByRole('button', { name: 'Sign in' }))

    expect(await screen.findByRole('alert')).toHaveTextContent('Invalid credentials')
  })

  it('disables the submit button while the request is in flight', async () => {
    const user = userEvent.setup()
    render(LoginForm)

    await user.type(screen.getByLabelText('Email'), 'ada@example.com')
    await user.type(screen.getByLabelText('Password'), 'correct-horse')
    await user.click(screen.getByRole('button', { name: 'Sign in' }))

    expect(screen.getByRole('button', { name: /signing in/i })).toBeDisabled()
  })
})
```

## Anti-Patterns

| Anti-pattern | Consequence | Fix |
|---|---|---|
| `wrapper.vm.x` assertions | Breaks on refactor, passes when UI is broken | Assert on DOM/emits |
| `find('.class')` | Breaks on restyle | Role/label/testid queries |
| `findAll(...)[2]` | Breaks on reorder | Query by accessible name |
| Missing `await` on interaction | Asserts the pre-update DOM | `await` every interaction |
| Snapshot as the only test | Green while broken | Behavioral assertions |
| Reflexive `shallowMount` | Stubs the integration under test | `mount`, stub deliberately |
| Mocking layout APIs in jsdom | Tests the mock | Browser Mode |
| Focus assertions without `attachTo` | Silently never matches | `attachTo: document.body` |
| `wrapper.find` for teleported content | "Not found" false negative | Query `document.body` or stub teleport |
| Asserting a prop equals what you passed | Tests Vue, not your code | Assert the rendered effect |

## Sources

- [Vue Test Utils](https://test-utils.vuejs.org/guide/)
- [Testing Library — Vue](https://testing-library.com/docs/vue-testing-library/intro)
- [Vue — Testing](https://vuejs.org/guide/scaling-up/testing.html)
