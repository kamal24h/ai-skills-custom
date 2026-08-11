# Composition API & `<script setup>`

Expert guidance for authoring Vue 3.5 SFCs with `<script setup lang="ts">`, compiler macros, and lifecycle hooks.

## 1. Canonical Component Shape

```vue
<script setup lang="ts">
import { computed, onMounted, shallowRef, watch } from 'vue'
import UserAvatar from './UserAvatar.vue'
import type { User } from '@/features/users/types'

const props = defineProps<{
  user: User
  compact?: boolean
}>()

const emit = defineEmits<{
  select: [id: string]
  dismiss: []
}>()

const expanded = shallowRef(false)
const displayName = computed(() => props.user.nickname ?? props.user.fullName)

watch(() => props.user.id, () => { expanded.value = false })

onMounted(() => { /* DOM-safe work */ })

defineExpose({ collapse: () => { expanded.value = false } })
</script>

<template>
  <article :class="{ 'is-compact': compact }">
    <UserAvatar :user="user" />
    <h3>{{ displayName }}</h3>
    <button type="button" @click="emit('select', user.id)">Select</button>
  </article>
</template>

<style scoped>
.is-compact { padding: 0.25rem; }
</style>
```

**Block order is always `<script>` → `<template>` → `<style>`.**

## 2. Compiler Macros

Macros are compile-time only. They are not imported, not runtime functions, and must appear at the **top level** of `<script setup>` — never inside a function, condition, or loop.

| Macro | Since | Purpose |
|-------|:-----:|---------|
| `defineProps<T>()` | 3.0 | Declare props |
| `defineEmits<T>()` | 3.0 | Declare emitted events |
| `defineExpose({})` | 3.0 | Publish an imperative API to parent template refs |
| `withDefaults()` | 3.0 | Provide defaults for type-declared props |
| `defineOptions({})` | 3.3 | Set component options (`name`, `inheritAttrs`) |
| `defineSlots<T>()` | 3.3 | Type slot props |
| `defineModel<T>()` | 3.4 | Two-way `v-model` prop |

### defineProps

```ts
// Type-based (required in TS projects)
const props = defineProps<{
  title: string
  count?: number
  items: readonly string[]
}>()

// Defaults, Vue 3.4 and below
const props = withDefaults(defineProps<{
  title: string
  items?: string[]
}>(), {
  items: () => [],          // factory — never a shared literal
})

// Defaults, Vue 3.5+ (reactive props destructure)
const { title, count = 0, items = [] } = defineProps<{
  title: string
  count?: number
  items?: string[]
}>()
```

**Reactive props destructure caveats (3.5+):**
- Destructured bindings stay reactive in the template and in effects — the compiler rewrites them to `props.x`.
- Passing a destructured binding to a function or watcher loses reactivity: use `watch(() => count, ...)` or `toRef(() => count)`.
- Some teams disable it for explicitness. Follow the project's existing convention.

**Compiler limitation:** `defineProps` types must be resolvable by the SFC compiler. Locally declared interfaces and simple imported interfaces work; deeply generic, mapped, or conditional imported types may fail. Declare a flat local interface in that case.

### defineEmits

```ts
// Named tuple syntax (recommended)
const emit = defineEmits<{
  update: [value: string]
  change: [id: number, name: string]
  close: []
}>()

emit('change', 1, 'name')
```

Never combine the type argument with a runtime array — it is a compile error. Declaring events matters beyond types: an **undeclared** event name also stays in `$attrs` as a native listener, which produces double-firing when the parent binds `@close` and the root element also emits a native `close`.

### defineModel

```ts
// Default model — prop "modelValue", event "update:modelValue"
const model = defineModel<string>()

// Named model — <Child v-model:count="total" />
const count = defineModel<number>('count', { default: 0 })

// Required / typed options
const value = defineModel<string>({ required: true })

// Modifiers and transformers — <Child v-model.trim="text" />
const [text, modifiers] = defineModel<string>({
  set: (v) => (modifiers.trim ? v.trim() : v),
})
```

Mutating a property of an object model does **not** emit. Replace the value:

```ts
const form = defineModel<{ name: string }>()
// ❌ form.value.name = 'Ada'
// ✅
form.value = { ...form.value!, name: 'Ada' }
```

### defineExpose

Components using `<script setup>` are **closed by default**. Parents see nothing on a template ref unless you expose it.

```ts
const inputEl = useTemplateRef<HTMLInputElement>('input')
defineExpose({
  focus: () => inputEl.value?.focus(),
})
```

Parent side, fully typed:

```ts
import type SearchBox from './SearchBox.vue'
const box = useTemplateRef<InstanceType<typeof SearchBox>>('box')
box.value?.focus()
```

### defineOptions & defineSlots

```ts
defineOptions({ name: 'UserList', inheritAttrs: false })

const slots = defineSlots<{
  default(props: { item: User; index: number }): any
  header?(props: { total: number }): any
}>()
```

`name` matters for `<KeepAlive :include>`, recursive self-reference, and devtools labels.

### Generic Components

```vue
<script setup lang="ts" generic="T extends { id: string }">
defineProps<{
  items: T[]
  selected?: T
}>()

const emit = defineEmits<{ select: [item: T] }>()

defineSlots<{ row(props: { item: T }): any }>()
</script>
```

Use this for lists, tables, selects, and any component parameterized over item type. It keeps slot props and emit payloads typed at every call site.

## 3. Lifecycle Hooks

| Hook | Runs | Typical use |
|------|------|-------------|
| `onBeforeMount` | Before first render | Rare |
| `onMounted` | After DOM insert | DOM measurement, third-party init, listeners |
| `onBeforeUpdate` | Before re-render patch | Capture pre-update DOM state |
| `onUpdated` | After DOM patch | **Avoid** — no state mutation here |
| `onBeforeUnmount` | Before teardown | Save state, flush |
| `onUnmounted` | After teardown | Remove listeners, clear timers |
| `onActivated` / `onDeactivated` | `<KeepAlive>` resume/pause | Restart polling, pause video |
| `onErrorCaptured` | Descendant error | Error boundaries |
| `onServerPrefetch` | SSR only, before render | Await data on the server |

**All hooks must be registered synchronously during setup.** After an `await`, the current-instance context is gone:

```ts
// ❌ silently never runs
const data = await fetchData()
onMounted(() => init(data))

// ✅
onMounted(async () => {
  const data = await fetchData()
  init(data)
})
```

Same rule applies to `provide`, `inject`, `defineExpose`, and composables that register hooks.

## 4. Top-level `await` and `<Suspense>`

```vue
<script setup lang="ts">
// Component becomes async; must be rendered inside <Suspense>
const user = await api.users.get(route.params.id as string)
</script>
```

- Call `defineExpose()` and register lifecycle hooks **before** the first `await`.
- `<Suspense>` has no built-in error handling — pair with `onErrorCaptured` in the parent.
- Prefer explicit loading state in most apps; reserve top-level `await` for SSR data flows and framework-managed boundaries (Nuxt).

## 5. Module-scope Code in an SFC

`<script setup>` cannot have named exports. When you need module-scope code (constants, types, a `defineComponent` for a render helper), add a second plain `<script>` block:

```vue
<script lang="ts">
export type Variant = 'primary' | 'ghost'
export const VARIANTS: Variant[] = ['primary', 'ghost']
</script>

<script setup lang="ts">
defineProps<{ variant?: Variant }>()
</script>
```

Prefer moving shared types/constants into a sibling `.ts` file. Use `defineOptions` rather than a second `<script>` when all you need is `name` or `inheritAttrs`.

## 6. Options API Interop

Only relevant in projects that already use Options API.

- Wrap components in `defineComponent()` so `this` is typed.
- `methods` and lifecycle hooks must be regular functions — arrow functions have no `this` binding to the instance.
- Prop validators and complex prop types use `PropType<T>`:
  ```ts
  props: { user: { type: Object as PropType<User>, required: true } }
  ```
- Stateful helpers (debounced handlers) must be created per instance in `created()`, not shared in `methods`.
- Do not introduce `mixins` in new code; migrate shared logic to composables, which can be consumed from Options API via `setup()`.

## 7. App Configuration

```ts
import { createApp } from 'vue'
import App from './App.vue'

const app = createApp(App)

app.use(router)
app.use(pinia)
app.config.errorHandler = (err, instance, info) => report(err, info)
app.provide(configKey, appConfig)

app.mount('#app')   // mount() returns the root component instance, not the app
```

- All `app.use`, `app.provide`, `app.component`, and `app.config` calls must happen **before** `mount()`.
- `app.mount()` returns the root component instance — do not chain app configuration off it.
- Prefer `app.provide()` + `inject()` over `app.config.globalProperties`, which is invisible in `<script setup>` and untyped without module augmentation.
- Global component registration in Vite uses `import.meta.glob()`, not `require.context()`.

## Anti-Patterns

| Anti-pattern | Why it fails | Fix |
|---|---|---|
| Macro inside a function/condition | Compile error | Move to top level |
| `defineExpose` after `await` | Parent ref sees nothing | Call before the first `await` |
| Lifecycle hook after `await` | Silently never runs | Register synchronously |
| `export const X` in `<script setup>` | Not allowed | Second `<script>` block or sibling `.ts` |
| Runtime + type args to `defineEmits` | Compile error | Pick one |
| `mixins` for shared logic | Implicit collisions | Composables |
| `app.config.globalProperties` for services | Untyped, invisible in setup | `provide`/`inject` with `InjectionKey` |
