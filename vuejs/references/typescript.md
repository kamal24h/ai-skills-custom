# TypeScript with Vue 3

Typed component contracts, refs, injection keys, generic components, JSX, and `vue-tsc`.

## 1. Project Setup

```jsonc
// tsconfig.json
{
  "compilerOptions": {
    "target": "ESNext",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "strict": true,
    "jsx": "preserve",
    "jsxImportSource": "vue",        // only for JSX/TSX projects
    "isolatedModules": true,
    "verbatimModuleSyntax": true,
    "noUncheckedIndexedAccess": true,
    "types": ["vite/client"],
    "paths": { "@/*": ["./src/*"] }
  },
  "include": ["src/**/*.ts", "src/**/*.vue", "env.d.ts"]
}
```

```jsonc
// package.json
{
  "scripts": {
    "build": "vue-tsc --noEmit && vite build",
    "typecheck": "vue-tsc --noEmit"
  }
}
```

**`vite build` does not type-check templates.** `vue-tsc --noEmit` must be a CI gate.

## 2. Typing Props

```ts
interface Column { key: string; label: string; width?: number }

const props = defineProps<{
  columns: readonly Column[]
  density?: 'comfortable' | 'compact'
  onRetry?: () => void
}>()
```

### Defaults

```ts
// 3.4 and below
const props = withDefaults(defineProps<{
  columns?: Column[]
  density?: 'comfortable' | 'compact'
}>(), {
  columns: () => [],            // ✅ factory
  density: 'comfortable',
})

// 3.5+ reactive props destructure
const { columns = [], density = 'comfortable' } = defineProps<{
  columns?: Column[]
  density?: 'comfortable' | 'compact'
}>()
```

**Object/array defaults must be factories.** A literal `{ columns: [] }` shares one array across every instance — mutating it in one component changes all of them.

### Boolean props

Vue casts an absent boolean prop to `false`. If you need to distinguish "not provided":

```ts
const props = defineProps({
  dense: { type: Boolean, default: undefined },
})
// props.dense: boolean | undefined
```

With pure type declarations, `dense?: boolean` still arrives as `false` when omitted, because of Boolean casting.

### Compiler resolution limits

The SFC compiler resolves prop types at compile time, without the full type checker.

```ts
// ✅ local interface
interface Props { id: string }
defineProps<Props>()

// ✅ simple imported interface/type alias
import type { Props } from './types'
defineProps<Props>()

// ⚠️ may fail: deeply generic / mapped / conditional imported types
defineProps<Pick<DeepMapped<Api['user']>, 'id' | 'name'>>()
```

When resolution fails, flatten to a local interface.

## 3. Typing Emits

```ts
const emit = defineEmits<{
  select: [row: Row]
  'update:page': [page: number]
  close: []
}>()
```

Older call-signature syntax also works but is more verbose:

```ts
const emit = defineEmits<{
  (e: 'select', row: Row): void
  (e: 'close'): void
}>()
```

## 4. Typing Refs

```ts
import { ref, shallowRef, computed, useTemplateRef } from 'vue'
import type { Ref, ShallowRef, ComputedRef } from 'vue'

const count: ShallowRef<number> = shallowRef(0)
const user = ref<User | null>(null)               // explicit union
const items = ref<Row[]>([])
const total: ComputedRef<number> = computed(() => items.value.length)

// DOM ref (Vue 3.5+)
const inputEl = useTemplateRef<HTMLInputElement>('search')
onMounted(() => inputEl.value?.focus())

// Component ref
import SearchBox from './SearchBox.vue'
const box = useTemplateRef<InstanceType<typeof SearchBox>>('box')
```

### `reactive()` — never pass a type argument

```ts
// ❌ reactive unwraps nested refs, so the explicit generic mismatches reality
const state = reactive<State>({ ... })

// ✅ let it infer
const state = reactive({ count: 0, user: ref<User | null>(null) })
```

### Ref null handling

Template refs are `HTMLElement | null`. Use optional chaining, or a non-null assertion only inside `onMounted` where the element is guaranteed to exist and cannot be inside a `v-if`.

```ts
// ✅
onMounted(() => { inputEl.value?.focus() })

// ⚠️ only when the element is unconditionally rendered
onMounted(() => { inputEl.value!.focus() })
```

## 5. Generic Components

```vue
<script setup lang="ts" generic="T extends { id: string }">
const props = defineProps<{
  items: readonly T[]
  selected?: T
}>()

const emit = defineEmits<{ select: [item: T] }>()

defineSlots<{
  row(props: { item: T; index: number }): any
  empty?(): any
}>()
</script>

<template>
  <ul>
    <li v-for="(item, i) in items" :key="item.id" @click="emit('select', item)">
      <slot name="row" :item="item" :index="i">{{ item.id }}</slot>
    </li>
    <slot v-if="!items.length" name="empty" />
  </ul>
</template>
```

Multiple parameters and imported constraints:

```vue
<script setup lang="ts" generic="T, K extends keyof T">
import type { Item } from './types'
defineProps<{ data: T[]; sortKey: K }>()
</script>
```

Use generics for every reusable list, table, select, autocomplete, or data-grid component.

## 6. Typing provide/inject

```ts
// context/theme.ts
import type { InjectionKey, Ref } from 'vue'

export interface ThemeContext {
  mode: Readonly<Ref<'light' | 'dark'>>
  toggle: () => void
}
export const themeKey: InjectionKey<ThemeContext> = Symbol('theme')
```

```ts
// provider
provide(themeKey, { mode: readonly(mode), toggle })

// consumer — inferred as ThemeContext | undefined
const theme = inject(themeKey)
if (!theme) throw new Error('useTheme must be used under <ThemeProvider>')

// with default (object defaults need a factory + true)
const theme = inject(themeKey, () => defaultTheme, true)
```

## 7. Typing Event Handlers

Under `strict`, inline template handlers with untyped parameters are unsafe.

```ts
function onInput(e: Event) {
  const target = e.target as HTMLInputElement
  query.value = target.value
}

function onKey(e: KeyboardEvent) {
  if (e.key === 'Enter') search()
}
```

```vue
<input @input="onInput" @keydown="onKey">
```

For component events, the payload type comes from `defineEmits` automatically.

## 8. Module Augmentation

### Route meta

```ts
// router/types.d.ts
export {}
declare module 'vue-router' {
  interface RouteMeta {
    requiresAuth?: boolean
    title?: string
    roles?: readonly string[]
  }
}
```

### Global properties (Options API / plugins)

```ts
declare module 'vue' {
  interface ComponentCustomProperties {
    $formatDate: (d: Date) => string
  }
}
export {}
```

The augmentation file must be included by `tsconfig` and must contain a top-level `export {}` to be treated as a module.

### Env vars

```ts
// env.d.ts
/// <reference types="vite/client" />
interface ImportMetaEnv {
  readonly VITE_API_URL: string
  readonly VITE_SENTRY_DSN?: string
}
interface ImportMeta { readonly env: ImportMetaEnv }
```

## 9. Dynamic Components

```ts
import { shallowRef, markRaw } from 'vue'
import type { Component } from 'vue'

const view = shallowRef<Component>(markRaw(ListView))
```

Component definitions must **not** be deeply reactive — `ref(SomeComponent)` triggers a Vue performance warning and wastes work proxying the definition. Use `shallowRef` and/or `markRaw`.

Resolve `<component :is>` targets from a fixed map, never from user input:

```ts
const VIEWS = { list: ListView, grid: GridView } as const
const current = computed(() => VIEWS[mode.value] ?? ListView)
```

## 10. Narrowing in Templates

The template compiler narrows on `v-if` in most cases, but union payloads sometimes need help:

```vue
<template>
  <ErrorBanner v-if="state.status === 'error'" :message="state.error" />
  <DataTable v-else-if="state.status === 'success'" :rows="state.rows" />
</template>
```

Model async state as a discriminated union so narrowing works:

```ts
type AsyncState<T> =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'success'; rows: T[] }
  | { status: 'error'; error: string }
```

This is preferable to three independent booleans (`loading`, `error`, `data`) which permit impossible combinations.

## 11. JSX / TSX in Vue

Only if the project uses `@vitejs/plugin-vue-jsx`.

```tsx
import { defineComponent, ref } from 'vue'

export default defineComponent({
  props: { title: { type: String, required: true } },
  setup(props, { slots, emit }) {
    const count = ref(0)
    return () => (
      <div class="card">                    {/* class, NOT className */}
        <h3>{props.title}</h3>
        <button onClick={() => count.value++}>{count.value}</button>
        {slots.default?.()}
      </div>
    )
  },
})
```

Differences from React JSX:

| React | Vue JSX |
|---|---|
| `className` | `class` |
| `htmlFor` | `for` |
| `onChange` (synthetic) | `onChange` (native) — use `onInput` for live typing |
| `style={{ marginTop: 8 }}` | `style={{ marginTop: '8px' }}` (units required for strings) |
| Refs auto-read | Refs need `.value` in JSX — no template unwrapping |
| Children as props | Slots as functions: `{{ default: () => <p/> }}` |
| Re-renders whole subtree | `setup()` runs once; the returned render fn re-runs |

`v-model` in JSX: `<input v-model={text.value} />` (with the JSX plugin) or wire `value` + `onInput` manually.

## Anti-Patterns

| Anti-pattern | Consequence | Fix |
|---|---|---|
| No `vue-tsc` in CI | Template type errors ship | `vue-tsc --noEmit` |
| `withDefaults` with a literal array/object | Shared reference across instances | Factory function |
| `reactive<T>({...})` | Type/runtime mismatch on nested refs | Let it infer |
| `ref(SomeComponent)` | Vue perf warning, wasted proxying | `shallowRef` + `markRaw` |
| String inject keys | `unknown` type, collisions | `InjectionKey<T>` |
| `any` in a public prop | Contract lost at every call site | Real type or generic |
| Three booleans for async state | Impossible states representable | Discriminated union |
| Complex imported type in `defineProps` | Opaque compiler error | Flatten to a local interface |
| `@ts-ignore` on a template error | Hides a real bug | Fix the type or narrow properly |
