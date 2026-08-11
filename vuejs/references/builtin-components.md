# Built-in Components & Directives

`<Transition>`, `<TransitionGroup>`, `<Teleport>`, `<Suspense>`, `<KeepAlive>`, async components, and custom directives.

## 1. `<Transition>`

Animates the enter/leave of **a single** element or component.

```vue
<Transition name="fade" mode="out-in">
  <component :is="current" :key="current.name" />
</Transition>

<style scoped>
.fade-enter-active, .fade-leave-active { transition: opacity 0.2s ease; }
.fade-enter-from,   .fade-leave-to     { opacity: 0; }
</style>
```

### Classes

| Class | Phase |
|---|---|
| `v-enter-from` | Start of enter (one frame) |
| `v-enter-active` | Whole enter — put `transition`/`animation` here |
| `v-enter-to` | End of enter |
| `v-leave-from` / `v-leave-active` / `v-leave-to` | Same for leave |

`v-` is replaced by `name`. Custom class names (`enter-active-class`) let you use Animate.css or Tailwind utilities.

### Rules

- Exactly **one** child element. Multiple sibling roots → no animation runs.
- Swapping between two elements requires a unique `:key` on each; `mode="out-in"` avoids overlap.
- `appear` animates the initial render (off by default) — relevant for `<RouterView>` transitions.
- Mixing CSS `transition` and `animation` requires `type="transition"` or `type="animation"` so Vue knows which end event to wait for.
- Nested transitions need explicit `:duration="{ enter: 500, leave: 300 }"` — Vue only observes the root element's end event.
- Reusable transition wrapper components must define their transition classes **globally or unscoped**; scoped styles from the wrapper do not apply to content passed in via slots (or use `:slotted()`).

### JavaScript hooks

```vue
<Transition
  :css="false"
  @enter="(el, done) => animate(el, { opacity: [0, 1] }).finished.then(done)"
  @leave="(el, done) => animate(el, { opacity: [1, 0] }).finished.then(done)"
/>
```

- **Always call `done()`**, or the element never finishes entering/leaving.
- Set `:css="false"` so Vue skips class detection and relies solely on your hooks.
- During rapid toggles, `@after-leave` may be skipped in favour of `@leave-cancelled` — put critical cleanup in both, or in `onUnmounted`.

## 2. `<TransitionGroup>`

For list insertions, removals, and reordering.

```vue
<TransitionGroup name="list" tag="ul">
  <li v-for="item in items" :key="item.id">{{ item.title }}</li>
</TransitionGroup>

<style scoped>
.list-move,
.list-enter-active,
.list-leave-active { transition: all 0.3s ease; }
.list-enter-from, .list-leave-to { opacity: 0; transform: translateY(-8px); }
.list-leave-active { position: absolute; }   /* remove from flow so siblings can FLIP */
</style>
```

- Vue 3 renders **no wrapper element** by default (Vue 2 rendered a `<span>`). Pass `tag="ul"` if you need one.
- Every child needs a stable, unique `:key` — index keys break FLIP animations.
- The `.<name>-move` class enables the move (FLIP) transition.
- Leaving items must be taken out of layout flow (`position: absolute`) or the remaining items jump instead of sliding.
- FLIP does not work on `display: inline` elements — use `inline-block` or a flex/grid child.
- For long lists, TransitionGroup gets expensive: limit animated items or virtualize.

## 3. `<Teleport>`

Renders a subtree elsewhere in the DOM while keeping it in the component's logical tree (props, provide/inject, events all still work).

```vue
<Teleport to="#modal-root" :disabled="isInline">
  <div class="modal" role="dialog" aria-modal="true">…</div>
</Teleport>
```

- The target must **exist in the DOM when the Teleport mounts**. If the target is rendered by the same Vue app, use `defer` (Vue 3.5+) so the Teleport resolves after the current render pass:
  ```vue
  <Teleport defer to="#late-target">…</Teleport>
  ```
- Scoped styles from the origin component do **not** apply to teleported content — the `data-v-` attribute travels but the scoped selector context often does not match expectations. Use a global class, CSS Modules, or `:deep()` from a global stylesheet.
- Multiple Teleports to the same target append in mount order.
- Under SSR, the target must exist in the server-rendered HTML, or make the Teleport client-only.

## 4. `<Suspense>`

Coordinates async setup in a subtree.

```vue
<Suspense timeout="0">
  <template #default>
    <AsyncDashboard />
  </template>
  <template #fallback>
    <DashboardSkeleton />
  </template>
</Suspense>
```

- Triggers on components with top-level `await` in `<script setup>` and on `defineAsyncComponent`.
- **No built-in error handling.** Pair with `onErrorCaptured` in a parent or `app.config.errorHandler`:
  ```ts
  onErrorCaptured((err) => { error.value = err; return false })
  ```
  Without it, a rejected async setup leaves the fallback rendered forever.
- Under `<Suspense>`, an async component's own `loadingComponent`/`errorComponent` are bypassed — the Suspense fallback wins.
- Events: `@pending`, `@resolve`, `@fallback`.
- `<Suspense>` is still marked experimental in the Vue docs; its API may change. Explicit loading state in the component is often the safer default for app code.
- SSR + Suspense has known hydration edge cases; in Nuxt, use the framework's data-fetching primitives instead.

## 5. `<KeepAlive>`

Caches component instances instead of destroying them.

```vue
<KeepAlive :include="['UserList', 'SearchResults']" :max="5">
  <component :is="current" />
</KeepAlive>
```

- `:include`/`:exclude` match the component **name** — set it via `defineOptions({ name: 'UserList' })` or rely on the filename in SFCs.
- **Always set `:max`.** Unbounded caching grows memory indefinitely; combining `<KeepAlive>` with `<Transition>` and no `:max` is a common leak.
- Cached components fire `onActivated`/`onDeactivated` instead of mount/unmount. Restart polling in `onActivated`, pause it in `onDeactivated`.
- Template refs inside a cached async component can be stale after reactivation — re-resolve them in `onActivated`.
- With nested routes, wrapping more than one `<RouterView>` level in `<KeepAlive>` can cause children to mount twice. Keep the caching at a single level.

## 6. Async Components

```ts
import { defineAsyncComponent, hydrateOnVisible, hydrateOnIdle } from 'vue'

const RichEditor = defineAsyncComponent({
  loader: () => import('./RichEditor.vue'),
  loadingComponent: EditorSkeleton,
  errorComponent: LoadFailed,
  delay: 200,        // ms before showing loadingComponent
  timeout: 10_000,   // ms before failing
  onError(error, retry, fail, attempts) {
    if (attempts <= 3) retry()
    else fail()
  },
})

// Vue 3.5+ lazy hydration (SSR apps)
const Comments = defineAsyncComponent({
  loader: () => import('./Comments.vue'),
  hydrate: hydrateOnVisible(),
})
```

- Use for heavy, rarely-used UI: modals, editors, charts, maps.
- **Do not** wrap route components in `defineAsyncComponent` — Vue Router already handles `() => import()` lazily. Wrap only if you need loading/error UI at the route level.
- Always supply `errorComponent` for network-loaded chunks; a failed chunk on a flaky connection otherwise renders nothing.
- Define the async component **outside** `setup()` (module scope or a `shallowRef`), otherwise it is recreated on every render and reloads.

## 7. `v-memo` and `v-once`

```vue
<!-- Skip re-render unless valueA/valueB change -->
<div v-for="row in rows" :key="row.id" v-memo="[row.id === selectedId, row.updatedAt]">
  <ExpensiveCell :row="row" />
</div>

<!-- Render once, never update -->
<footer v-once>{{ legalText }}</footer>
```

- `v-memo` is a **micro-optimization for measured hot paths**, typically huge `v-for` lists where most rows are unchanged. A wrong dependency array silently produces stale UI.
- `v-once` freezes the subtree forever — only for genuinely static content.
- Neither should be added before a bottleneck is measured.

## 8. Custom Directives

Use a directive only when the behavior is **DOM-specific** and does not fit a composable or component.

```vue
<script setup lang="ts">
import type { Directive } from 'vue'

// Local directive: the `vName` convention registers it as `v-name`
const vFocus: Directive<HTMLElement, boolean> = {
  mounted(el, binding) { if (binding.value !== false) el.focus() },
}

const vClickOutside: Directive<HTMLElement, () => void> = {
  mounted(el, binding) {
    el._handler = (e: MouseEvent) => {
      if (!el.contains(e.target as Node)) binding.value()
    }
    document.addEventListener('click', el._handler)
  },
  unmounted(el) { document.removeEventListener('click', el._handler) },
}
</script>

<template>
  <input v-focus>
  <div v-click-outside="close">…</div>
</template>
```

Hooks: `created`, `beforeMount`, `mounted`, `beforeUpdate`, `updated`, `beforeUnmount`, `unmounted`.

- Always clean up in `unmounted` — directives are a common leak source.
- `binding.arg` and `binding.modifiers` carry `v-dir:arg.mod="value"`.
- Global registration: `app.directive('focus', vFocus)`.
- On a **multi-root component**, a directive cannot resolve a single target element and Vue warns.
- Directives run on every update — keep the `updated` hook cheap.

## Anti-Patterns

| Anti-pattern | Consequence | Fix |
|---|---|---|
| Multiple roots in `<Transition>` | No animation | Single element/component child |
| JS hooks without `done()` | Transition hangs | Call `done()`, set `:css="false"` |
| Index keys in `<TransitionGroup>` | Broken FLIP | Stable id keys |
| Leaving item left in flow | Items jump | `position: absolute` on `-leave-active` |
| Teleport target rendered later | "Target not found" warning | `defer` (3.5+) or move the target |
| `<Suspense>` without an error boundary | Permanent fallback | `onErrorCaptured` |
| `<KeepAlive>` with no `:max` | Memory growth | `:include` + `:max` |
| `defineAsyncComponent` inside `setup()` | Re-created and re-loaded each render | Define at module scope |
| Async route component double-wrapped | Redundant indirection | `() => import()` in the route |
| `v-memo` added preemptively | Stale UI | Measure first |
| Directive without `unmounted` cleanup | Listener leak | Remove in `unmounted` |
