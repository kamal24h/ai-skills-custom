# Component Design & Data Flow

Explicit, typed contracts between components: props down, events up, `v-model`, slots, provide/inject, fallthrough attrs, and component splitting.

## 1. The Default Model — Props Down, Events Up

```vue
<!-- Parent owns the state -->
<script setup lang="ts">
const todos = ref<Todo[]>([])
function remove(id: string) { todos.value = todos.value.filter(t => t.id !== id) }
</script>

<template>
  <TodoList :todos="todos" @remove="remove" />
</template>
```

```vue
<!-- Child reports intent, never mutates -->
<script setup lang="ts">
defineProps<{ todos: readonly Todo[] }>()
const emit = defineEmits<{ remove: [id: string] }>()
</script>

<template>
  <li v-for="todo in todos" :key="todo.id">
    {{ todo.title }}
    <button type="button" @click="emit('remove', todo.id)">×</button>
  </li>
</template>
```

**Props are read-only.** Mutating an object prop's contents technically "works" and is exactly why it is dangerous: the parent's state changes with no traceable cause.

```ts
// ❌
props.todos.push(newTodo)
props.user.name = 'Ada'

// ✅ emit and let the owner update
emit('add', newTodo)
```

Typing array/object props as `readonly` (`readonly Todo[]`) makes accidental mutation a type error.

### Local state derived from a prop

```ts
const props = defineProps<{ initialQuery: string }>()
const query = ref(props.initialQuery)                  // one-time seed
watch(() => props.initialQuery, v => { query.value = v }) // resync if needed
```

Name such props `initialX`/`defaultX` so the one-way relationship is obvious.

## 2. Emits — Declare Everything

```ts
const emit = defineEmits<{
  submit: [payload: FormValues]
  'update:step': [step: number]
  cancel: []
}>()
```

Declaring events is not only about types:

- An **undeclared** event name remains in `$attrs` and is bound as a native listener on the root element. If the root element also fires that native event, the parent handler runs **twice**.
- Declared events are removed from `$attrs`, so wrapper components forwarding `v-bind="$attrs"` do not double-bind them.
- Events that collide with native DOM events (`click`, `focus`, `input`, `change`) must be declared, or you get both the native and the custom firing.

Prefer domain-specific names (`@confirm`, `@row-select`) over re-emitting native names.

### Validation in emits

```ts
const emit = defineEmits({
  submit: (payload: FormValues) => payload.email.includes('@'),
})
```

Use the runtime form only in JS projects; in TS use the type form and validate before emitting.

## 3. `v-model` — Genuine Two-Way Contracts Only

```ts
// Child
const model = defineModel<string>()                       // v-model
const page  = defineModel<number>('page', { default: 1 }) // v-model:page
const [text, mods] = defineModel<string>({                // v-model.trim
  set: v => (mods.trim ? v.trim() : v),
})
```

```vue
<!-- Parent -->
<SearchInput v-model="query" v-model:page="page" />
```

### Object models do not emit on property mutation

```ts
const form = defineModel<FormValues>()

// ❌ parent never notified
form.value.email = 'a@b.c'

// ✅
form.value = { ...form.value!, email: 'a@b.c' }
```

For deeply nested form objects, prefer separate named models or a store — `v-model` on a large object couples parent and child tightly.

### When *not* to use `v-model`

- The child only reports an event (use `@change`).
- Three or more independent values (use props + explicit events, or a store).
- The parent must validate/transform before accepting (use `@update:x` explicitly so you can reject a value).

## 4. Slots

```vue
<!-- Card.vue -->
<script setup lang="ts">
defineSlots<{
  header?(props: { title: string }): any
  default(props: { expanded: boolean }): any
  footer?(): any
}>()

const props = defineProps<{ title: string }>()
const expanded = ref(false)
</script>

<template>
  <section>
    <header>
      <slot name="header" :title="props.title">
        <h3>{{ props.title }}</h3>   <!-- fallback content -->
      </slot>
    </header>

    <slot :expanded="expanded" />

    <footer v-if="$slots.footer"><slot name="footer" /></footer>
  </section>
</template>
```

Rules:

- Slot content is compiled in the **parent's** scope — it cannot access the child's internal state except through scoped slot props.
- `v-slot` is only valid on `<template>` or on a component tag, never on a plain HTML element.
- Once you use any named `<template #name>`, put default content in `<template #default>` explicitly — mixing bare content with named templates is ambiguous and errors in some cases.
- `name` is a reserved slot prop; do not pass `:name` as slot data.
- Use `v-if="$slots.footer"` to avoid rendering empty wrappers.

### Forwarding slots through a wrapper

```vue
<template>
  <BaseTable v-bind="$attrs">
    <template v-for="(_, name) in $slots" #[name]="slotProps">
      <slot :name="name" v-bind="slotProps ?? {}" />
    </template>
  </BaseTable>
</template>
```

Without this, a wrapper silently swallows every slot the wrapped component supports.

## 5. Provide / Inject

Use for **deep-tree context** (theme, i18n, form context, design-system config) — not as a substitute for props between a parent and its direct child.

```ts
// keys.ts
import type { InjectionKey, Ref } from 'vue'

export interface FormContext {
  values: Readonly<Ref<FormValues>>
  setField: (k: keyof FormValues, v: string) => void
}
export const formKey: InjectionKey<FormContext> = Symbol('form')
```

```ts
// Provider — must run synchronously in setup
const values = ref<FormValues>(initial)
provide(formKey, {
  values: readonly(values),
  setField: (k, v) => { values.value = { ...values.value, [k]: v } },
})
```

```ts
// Consumer
const form = inject(formKey)
if (!form) throw new Error('FormField must be used inside <Form>')
```

Rules:

- Always use a typed `InjectionKey<T>` symbol — string keys are untyped and collide.
- Provide **reactive** values (ref/computed/reactive) if consumers must react; `provide(key, user.value)` injects a dead snapshot.
- Keep mutations in the provider: expose `readonly` state plus mutator functions.
- Object/array defaults need a factory and `true` as the third argument:
  ```ts
  const cfg = inject(configKey, () => ({ dense: false }), true)
  ```
  `inject(key, {})` shares one object across every consumer.
- `provide`/`inject` must be called synchronously during setup, before any `await`.
- Provide/inject is hard to trace. Document the provider in the key file and fail loudly when the injection is missing.

## 6. Fallthrough Attributes

Attributes and listeners not declared as props or emits land on the component's single root element.

- `class` and `style` **merge** with the root element's own values.
- Other attributes (`id`, `type`, `aria-*`, `data-*`) **overwrite** the component's own binding.
- Multi-root components do not auto-inherit — Vue warns and you must bind `v-bind="$attrs"` explicitly on the intended root.

```vue
<!-- BaseInput.vue — wrapper whose root is not the target -->
<script setup lang="ts">
defineOptions({ inheritAttrs: false })
const model = defineModel<string>()
const id = useId()
</script>

<template>
  <div class="field">
    <label :for="id"><slot /></label>
    <input :id="id" v-model="model" v-bind="$attrs">
  </div>
</template>
```

In script, `useAttrs()` gives access to `$attrs`; note it is not reactive per-property in the way props are — read it inside a computed if you need to react.

## 7. Component Template Refs — Last Resort

Prefer props/emits. Use a template ref only for genuinely imperative APIs.

```vue
<script setup lang="ts">
import SearchBox from './SearchBox.vue'
const box = useTemplateRef<InstanceType<typeof SearchBox>>('box')

onMounted(() => box.value?.focus())
</script>

<template>
  <SearchBox ref="box" />
</template>
```

The child must publish its API explicitly — `<script setup>` components are closed:

```ts
// SearchBox.vue
const inputEl = useTemplateRef<HTMLInputElement>('input')
defineExpose({
  focus: () => inputEl.value?.focus(),
  clear: () => { model.value = '' },
})
```

Expose an intentional surface (`focus`, `reset`, `validate`) — never the whole internal state object.

## 8. Component Splitting

Split when **any** of these is true:

- The component owns both orchestration/state and substantial presentational markup.
- It has 3+ distinct UI sections (form, filters, list, footer/status).
- A template block repeats or is reusable (row, card, list entry).
- The `<script setup>` block mixes unrelated concerns (fetching + drag/drop + formatting).

Move **UI sections** into child components (props in, events out). Move **state and side effects** into composables.

### Route views stay thin

```vue
<!-- views/CartView.vue — a composition surface -->
<script setup lang="ts">
const { items, total, remove, checkout } = useCart()
</script>

<template>
  <PageLayout title="Cart">
    <CartItemList :items="items" @remove="remove" />
    <CartSummary :total="total" @checkout="checkout" />
  </PageLayout>
</template>
```

For a CRUD/list feature, split at minimum into: feature container, input/form, list (and item), and filter/status components.

A single-file implementation is acceptable only for a very small throwaway demo — and should be justified explicitly.

## 9. Public Component API Checklist

```ts
// Every public component states its contract in one place
const props = defineProps<{
  /** Rows to render. Treated as immutable. */
  items: readonly Row[]
  /** Currently highlighted row id. */
  selectedId?: string
  density?: 'comfortable' | 'compact'
}>()

const emit = defineEmits<{
  select: [row: Row]
  'update:selectedId': [id: string]
}>()

defineSlots<{
  cell(props: { row: Row; column: Column }): any
  empty?(): any
}>()
```

- Every prop typed, no `any`.
- Every event declared with a typed payload.
- Every slot declared with its props.
- Imperative surface (if any) declared via `defineExpose`.

## Anti-Patterns

| Anti-pattern | Consequence | Fix |
|---|---|---|
| Mutating a prop | Untraceable parent state changes | Emit / `defineModel` |
| Undeclared emit | Double-firing via `$attrs` | `defineEmits<T>()` |
| `v-model` on a big nested object | Tight coupling, missed updates | Named models, store, or explicit events |
| Reading child internals via ref | Brittle coupling | Props/emits, or `defineExpose` a narrow API |
| String inject keys | Untyped, collision-prone | `InjectionKey<T>` symbol |
| `inject(key, {})` | Shared object across consumers | Factory + `true` |
| `provide(key, ref.value)` | Dead snapshot | Provide the ref/computed |
| Wrapper without `inheritAttrs: false` | Attributes on the wrong element | `inheritAttrs: false` + `v-bind="$attrs"` |
| Wrapper that drops slots | Lost functionality | Forward `$slots` |
| 400-line route view | Untestable, unreusable | Split into container + sections + composables |

## Sources

- [Vue — Props](https://vuejs.org/guide/components/props.html)
- [Vue — Events](https://vuejs.org/guide/components/events.html)
- [Vue — Provide / Inject](https://vuejs.org/guide/components/provide-inject.html)
