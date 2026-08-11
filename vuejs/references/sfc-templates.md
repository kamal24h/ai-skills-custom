# SFC Structure & Template Correctness

Single-File Component layout, template syntax rules, directives, template refs, and scoped styles.

## 1. SFC Layout

```vue
<script setup lang="ts">
// 1. imports
// 2. macros (defineProps / defineEmits / defineModel / defineSlots / defineOptions)
// 3. state
// 4. computed
// 5. watchers & lifecycle
// 6. functions
// 7. defineExpose (last)
</script>

<template>
  <!-- declarative markup only -->
</template>

<style scoped>
/* component-local styles */
</style>
```

Always `<script>` → `<template>` → `<style>`. Keep one component per file.

### Naming

- Component files use **PascalCase**: `UserCard.vue`, `BaseButton.vue`.
- Use them in templates as `<UserCard />` (PascalCase distinguishes components from native elements and enables self-closing).
- **Multi-word names** always — `Item.vue` and `Table.vue` risk colliding with current or future HTML elements.
- Prefix tightly coupled children with the parent name: `TodoList.vue`, `TodoListItem.vue`.
- Base/design-system components share a prefix: `BaseButton`, `BaseInput`, or `AppButton`, `AppInput`.
- Recursive components need a resolvable name — `defineOptions({ name: 'TreeNode' })` or rely on the filename.

## 2. Template Expression Rules

Templates support **expressions**, not statements.

```vue
<!-- ❌ statements / declarations -->
{{ const x = 1 }}
{{ if (ok) { ... } }}

<!-- ✅ expressions -->
{{ ok ? 'Yes' : 'No' }}
{{ items.length }}
```

Templates access only: top-level `<script setup>` bindings, globals allow-listed by `app.config.globalProperties`, and a small built-in whitelist (`Math`, `Date`, …). Other globals need explicit exposure.

### No side effects in templates

Every render evaluates template expressions. A function called from the template must be pure.

```vue
<!-- ❌ mutates during render → unpredictable re-render loops -->
<span>{{ incrementAndFormat(value) }}</span>

<!-- ✅ -->
<span>{{ formatted }}</span>
```

### No expensive work in templates

Template expressions are not cached. Filtering, sorting, mapping, and formatting belong in `computed`.

```vue
<!-- ❌ -->
<li v-for="i in items.filter(x => x.active).sort(byName)" :key="i.id">

<!-- ✅ -->
<li v-for="i in visibleItems" :key="i.id">
```

## 3. `v-for`

### Stable keys are mandatory

```vue
<!-- ❌ index key: component state binds to position, not identity -->
<TodoItem v-for="(todo, i) in todos" :key="i" :todo="todo" />

<!-- ✅ -->
<TodoItem v-for="todo in todos" :key="todo.id" :todo="todo" />
```

Index keys are only acceptable for lists that never reorder, filter, insert, or remove — which is rare enough that a stable id is always the safer default.

### Never combine `v-if` and `v-for`

In Vue 3, `v-if` has **higher** priority and cannot access the `v-for` alias.

```vue
<!-- ❌ compile/runtime error: `todo` is not defined -->
<li v-for="todo in todos" v-if="!todo.done" :key="todo.id">

<!-- ✅ filter in a computed (preferred) -->
<li v-for="todo in pendingTodos" :key="todo.id">

<!-- ✅ or move v-if to a wrapping template -->
<template v-for="todo in todos" :key="todo.id">
  <li v-if="!todo.done">{{ todo.title }}</li>
</template>
```

### Other `v-for` facts

- `v-for="n in 5"` yields `1..5`, not `0..4`.
- Iterating an object gives `(value, key, index)`.
- Sorting/reversing must happen in a `computed` over a copy — never mutate the source array in the template.
- When passing to a child, pass the item explicitly: `<Row v-for="r in rows" :key="r.id" :row="r" />`.

## 4. `v-if`, `v-else`, `v-show`

```vue
<div v-if="state === 'loading'">…</div>
<div v-else-if="state === 'error'">…</div>
<div v-else>…</div>
```

- `v-else`/`v-else-if` must be the **immediate sibling** of `v-if` — a comment or whitespace node in between is fine, but any other element breaks the chain.
- `v-if` unmounts: child state and DOM are destroyed and recreated.
- `v-show` only toggles `display`. It does **not** work on `<template>` and has no `v-else`.

| Use | Directive |
|---|---|
| Rarely toggled, expensive subtree | `v-if` |
| Frequently toggled, cheap subtree | `v-show` |
| Must preserve child state while hidden | `v-show` (or `<KeepAlive>` + `v-if`) |
| Must run mount logic each time it appears | `v-if` |

### Null-check ordering

`v-if` on the same element does not protect other bindings on that element from evaluating too early in every case, and it never protects deeper chains:

```vue
<!-- ❌ throws when profile is undefined -->
<span v-if="user">{{ user.profile.name }}</span>

<!-- ✅ -->
<span v-if="user?.profile">{{ user.profile.name }}</span>
<!-- ✅ or -->
<span>{{ user?.profile?.name ?? '—' }}</span>
```

## 5. Bindings, Class & Style

```vue
<div
  :class="['card', { 'card--active': isActive, 'card--dense': dense }]"
  :style="{ backgroundColor: bg, marginTop: `${gap}px` }"
/>
```

- `:style` object keys use **camelCase** (`backgroundColor`), kebab-case requires quoting.
- Move non-trivial class logic into a `computed` returning an object or array.
- Dynamic directive arguments (`:[attrName]="v"`, `@[eventName]="fn"`) must evaluate to a lowercase string or `null`; in in-DOM templates they are lowercased by the browser.
- `v-bind="objectOfAttrs"` spreads an object of attributes.

## 6. Event Handling

```vue
<button @click="submit" />
<button @click="remove(id)" />
<button @click.stop.prevent="save" />
<input @keyup.enter="search" @keyup.esc="reset">
```

- **Modifier order matters.** `@click.prevent.self` prevents on the element and all children; `@click.self.prevent` only when the target is the element itself.
- `.passive` and `.prevent` are contradictory — the browser ignores `preventDefault()` on passive listeners.
- `.exact` restricts to precisely the listed system modifiers: `@click.ctrl` fires on Ctrl+Alt+Click; `@click.ctrl.exact` does not.
- Key modifiers on `keyup` fire on release; system modifier keys (`ctrl`, `alt`, `shift`, `meta`) with `keyup` require the modifier still held when the other key is released — use `keydown` for shortcuts.
- On a **component**, `@click` binds the *custom* event `click` if it is declared in `defineEmits`, otherwise it falls through as a native listener. Use `@click.native`-free Vue 3 semantics deliberately: declare the emit or rely on fallthrough, not both.

## 7. Template Refs

```vue
<script setup lang="ts">
import { useTemplateRef, onMounted } from 'vue'

const inputEl = useTemplateRef<HTMLInputElement>('search')  // Vue 3.5+
onMounted(() => inputEl.value?.focus())
</script>

<template>
  <input ref="search">
</template>
```

- `useTemplateRef('name')` ties the ref to the string in the template — renaming the template attribute without updating the string is now visible, unlike the implicit variable-name matching of `ref(null)`.
- Refs are `null` before mount and after a `v-if` removes the element. Always guard with `?.`.
- Reading a ref in a watcher requires `{ flush: 'post' }` — the default `pre` flush runs before the DOM updates.
- `ref` inside `v-for` produces an array **whose order is not guaranteed** to match the source array. Key by id and use a function ref if order matters:
  ```vue
  <li v-for="item in items" :key="item.id" :ref="el => rowEls[item.id] = el as HTMLElement">
  ```
- To reach a child component's API, the child must `defineExpose`.

## 8. `v-html` and Rendering Safety

```vue
<!-- ❌ XSS -->
<div v-html="comment.body" />

<!-- ✅ sanitized at the boundary, and only if rich content is truly required -->
<div v-html="sanitizedBody" />
```

- Never bind user-controlled content to `v-html` without a vetted sanitizer (DOMPurify) and a constrained tag/attribute allow-list.
- Scoped styles do **not** apply to `v-html` content — style it via a global rule or `:deep()`.
- Prefer `{{ }}` interpolation, slots, or a markdown renderer that outputs a vnode tree.
- `<component :is>` must resolve from a fixed allow-list map — never from user input or a query parameter.

## 9. Scoped Styles

```vue
<style scoped>
.card { padding: 1rem; }              /* prefer class selectors */
.card :deep(.icon) { color: red; }     /* explicit reach into a child */
:slotted(.item) { margin: 0; }         /* style slot content from the child */
:global(.body-locked) { overflow: hidden; }
</style>
```

- Scoped CSS adds a `[data-v-xxxx]` attribute selector. **Class selectors are markedly faster** than element selectors under this scheme — avoid `div span a { }`.
- Scoped styles reach a child's **root element** but not its internals; use `:deep()` deliberately or, better, expose a prop/CSS variable from the child.
- Slot content is compiled in the parent scope, so the child needs `:slotted()` to style it.
- Dynamic values belong in `v-bind()`:
  ```vue
  <style scoped>
  .bar { width: v-bind(widthPercent); background: v-bind('theme.accent'); }
  </style>
  ```
- Use `<style module>` when you need class names as JS values.

## 10. In-DOM Template Caveats

If a template lives in the page HTML rather than an SFC (rare, but happens in CDN/legacy setups):

- Tag and attribute names are case-insensitive → use kebab-case (`<user-card my-prop="…">`).
- Self-closing custom tags are invalid → `<my-comp></my-comp>`.
- Content-model restrictions apply: `<li>` only inside `<ul>/<ol>`, `<tr>` only inside `<tbody>`, etc. Use `is="vue:my-comp"` to work around it.
- `<textarea>` ignores `{{ }}` interpolation — use `v-model` or `:value`.

SFCs are not subject to these rules. Prefer SFCs.

## Anti-Patterns

| Anti-pattern | Consequence | Fix |
|---|---|---|
| `:key="index"` on a mutable list | State attaches to the wrong row | Stable id key |
| `v-if` + `v-for` on one element | Error / precedence bug | Filter in `computed` |
| Filter/sort in the template | Recomputed every render | `computed` |
| Impure function in the template | Unpredictable re-renders | Move the effect out |
| `v-show` on `<template>` | Silently does nothing | `v-if` |
| `ref(null)` matched by variable name | Silent break on rename | `useTemplateRef('name')` |
| Template ref read in setup body | `null` | `onMounted` / `flush: 'post'` |
| `v-html` with user content | XSS | Sanitize or don't use it |
| Element selectors in scoped CSS | Slow selector matching | Class selectors |
| Single-word component name | HTML collision risk | Multi-word PascalCase |
