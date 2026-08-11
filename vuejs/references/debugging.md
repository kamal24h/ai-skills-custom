# Debugging Vue 3

A symptom-first index for diagnosing Vue runtime warnings, silent reactivity loss, and rendering bugs.

## 1. Tools

| Tool | Use |
|---|---|
| **Vue DevTools** (browser extension or `vite-plugin-vue-devtools`) | Component tree, props/state inspection, timeline, Pinia state, router state |
| `onRenderTracked(e)` | Which dependency was *tracked* during render |
| `onRenderTriggered(e)` | Which dependency *caused* this re-render — the fastest answer to "why did this update?" |
| `app.config.performance = true` | Component init/render/patch marks in the Performance panel |
| `app.config.errorHandler` | Central capture of uncaught errors |
| `app.config.warnHandler` | Central capture of Vue warnings (dev only) |
| `debug` option on `watch`/`computed` | Per-effect `onTrack`/`onTrigger` hooks (dev only) |

```ts
onRenderTriggered((e) => {
  console.log('re-render:', e.type, e.key, e.target)
})

watch(source, cb, {
  onTrigger(e) { debugger },
})
```

## 2. Symptom Index — Reactivity

| Symptom | Likely cause | Fix |
|---|---|---|
| Value shows as `[object Object]` in the template | Nested ref (not top-level) — no auto-unwrap | `{{ obj.nested.value }}` or restructure |
| Ref changes but UI never updates | `.value` not written, or the ref was destructured out of `reactive()` | Write `.value`; use `toRefs()` |
| State stops updating after destructuring | `const { x } = reactive(...)` | `toRefs()` |
| Value in an array/`Map`/`Set` doesn't unwrap | Refs only unwrap in `reactive` objects and top-level template | Explicit `.value` |
| `a === b` false for the same object | Proxy vs raw identity | Compare by id, or `toRaw()` |
| Third-party instance behaves strangely | Vue proxied its internals | `markRaw()` / `shallowRef` |
| Watcher fires once for many changes | Same-tick batching (intended) | Use `flush: 'sync'` only if truly required |
| `shallowRef` mutation ignored | Only replacement is tracked | Replace `.value`, or use `ref` |
| Computed never updates | Dependency not read on the taken branch | Read all deps unconditionally, or restructure |
| Computed result mutation vanishes | Computed return is readonly by contract | Copy into an editable ref |
| Sorting a list corrupts source order | `sort()`/`reverse()` mutate in place | `[...items].sort()` |
| Watcher never fires | Source is a plain value, not a ref/getter | `watch(() => state.x, cb)` |
| `watchEffect` misses a dependency | Dep read after `await` | Read deps before the first `await`, or use `watch` |
| Stale search results overwrite new ones | No async cleanup | `onCleanup` + `AbortController` |
| Deep watcher old/new identical | Same object reference | Snapshot, or watch a derived primitive |
| DOM read is stale in a watcher | Default `pre` flush | `{ flush: 'post' }` |

## 3. Symptom Index — Components & Props

| Symptom | Likely cause | Fix |
|---|---|---|
| "Component not found" / renders as unknown element | Locally registered components are not inherited by descendants | Import in the component that uses it, or register globally |
| Wrong component renders | Name collision with another component or an HTML element | Multi-word PascalCase names |
| `@click` on a component does nothing | The component declares `click` as an emit but never emits it, or the root isn't clickable | Emit it, or use `@click` fallthrough on a single-root component |
| Event fires twice | Undeclared emit also bound as a native listener via `$attrs` | Declare it in `defineEmits` |
| Parent's `ref` to a child is empty | `<script setup>` is closed by default | `defineExpose({...})` |
| `defineExpose` has no effect | Called after `await` | Call before the first `await` |
| Parent styles don't apply | Multi-root component — no automatic attr inheritance | Bind `v-bind="$attrs"` on the intended root |
| Attributes land on the wrong element | Wrapper without `inheritAttrs: false` | `inheritAttrs: false` + `v-bind="$attrs"` |
| `defineProps` throws on a referenced variable | Macro is hoisted; it cannot reference `<script setup>` locals | Use literals/types only inside the macro |
| Prop change doesn't reach a child | Prop mutated locally instead of via the parent | Emit and let the parent update |
| Recursive component doesn't render | No resolvable name | `defineOptions({ name: 'TreeNode' })` |

## 4. Symptom Index — Templates & Refs

| Symptom | Likely cause | Fix |
|---|---|---|
| "Cannot read property of undefined" | Deep access before data loads | `v-if` on the wrapper + optional chaining |
| List items swap state / lose input | Index keys | Stable id keys |
| `v-if` + `v-for` error or wrong result | `v-if` evaluates first | Filter in `computed` |
| `v-else` renders unconditionally | Not an immediate sibling of `v-if` | Move it adjacent |
| `v-show` does nothing on `<template>` | Unsupported | `v-if` |
| Off-by-one in `v-for="n in 5"` | Range starts at 1 | Adjust |
| Template ref is `null` | Read before mount, or element is behind `v-if` | `onMounted` / `flush: 'post'` / `?.` |
| `v-for` refs in the wrong order | Array order is not guaranteed | Function ref keyed by id |
| Renaming a `ref` attribute silently breaks | Implicit variable-name matching | `useTemplateRef('name')` |
| Template compilation error on a statement | Templates take expressions only | Move logic to script |
| Dynamic argument not working | Must be a lowercase string or `null` | Normalize the value |
| `<textarea>` content ignored | No interpolation in textarea | `v-model` |

## 5. Symptom Index — Lifecycle & Async

| Symptom | Likely cause | Fix |
|---|---|---|
| `onMounted` never runs | Registered after `await` | Register synchronously |
| `inject()` returns `undefined` | Called after `await`, outside setup, or no provider above | Call synchronously; verify the provider |
| Injected value never updates | A snapshot was provided, not a ref | `provide(key, refOrComputed)` |
| All consumers share one default object | `inject(key, {})` | Factory + `true` |
| DOM read after a state change is stale | Updates are batched | `await nextTick()` |
| Listener still firing after navigation | No `onUnmounted` cleanup | Pair cleanup, or use VueUse |
| Memory grows over time | Unremoved listeners/observers/timers, or unbounded `<KeepAlive>` | Cleanup + `:max` |
| Composable's hooks silently don't fire | Called conditionally/asynchronously | Call at setup top level |

## 6. Symptom Index — Router, Store, SSR

| Symptom | Likely cause | Fix |
|---|---|---|
| Data stale after `/users/1` → `/users/2` | Component reused; `onMounted` doesn't re-run | Watch `route.params` / `onBeforeRouteUpdate` |
| "getActivePinia was called…" | Store used before `app.use(pinia)` | Instantiate inside setup/guard |
| Store values don't update in the template | Store destructured directly | `storeToRefs()` |
| Store state missing in DevTools | Setup store didn't return it | Return every ref/computed |
| Guard redirect loop | No terminating condition | Check `to.name` before redirecting |
| Navigation happens before an auth check | Unawaited async in a guard | `async` guard + `await` |
| "Hydration node/text mismatch" | Nondeterministic render | See `ssr-hydration.md` |
| One user sees another's data (SSR) | Module-scope mutable state | Per-request store / injection state |
| `window is not defined` | Browser API during SSR | `onMounted` / SSR guard |

## 7. Symptom Index — Built-ins & Styling

| Symptom | Likely cause | Fix |
|---|---|---|
| Transition doesn't animate | Multiple roots, or same key on swap | One child + unique `:key` |
| Transition hangs | JS hook without `done()` | Call `done()`, `:css="false"` |
| List items jump instead of sliding | Leaving item still in layout flow | `position: absolute` on `-leave-active` |
| FLIP move animation missing on inline elements | `display: inline` cannot be transformed | `inline-block` / flex child |
| "Teleport target not found" | Target not yet in the DOM | `defer` (3.5+) or move the target |
| Scoped styles don't reach a child's internals | Scoping boundary | `:deep()` or a CSS variable hook |
| Scoped styles don't apply to slot content | Slot content is parent-scoped | `:slotted()` |
| Scoped styles don't apply to `v-html` | Dynamic nodes carry no scope attribute | `:deep()` / global rule |
| Tailwind class missing at runtime | Class name built by concatenation | Full class strings in a map |
| Suspense fallback never resolves | Async setup rejected, no error handling | `onErrorCaptured` |

## 8. A Repeatable Debugging Procedure

1. **Read the warning literally.** Vue's dev warnings name the component and usually the exact rule.
2. **Confirm the value is reactive.** In DevTools, does the state change when you expect? If not, the bug is upstream of rendering.
3. **Confirm the render is triggered.** Add `onRenderTriggered` — if it never fires, the dependency is not tracked.
4. **Isolate.** Reproduce in a minimal SFC. Most Vue bugs collapse to under 20 lines.
5. **Check the boundary.** Props/emits, provide/inject, store, router — most "impossible" bugs live where two layers meet.
6. **Check async ordering.** Was a hook, macro, `provide`, or composable called after an `await`?
7. **Check cleanup.** Does the symptom appear only after navigating away and back? That is a missing teardown.

## 9. Production Error Reporting

```ts
app.config.errorHandler = (err, instance, info) => {
  reportError(err, { component: instance?.$options.name, hook: info })
}

// Warnings are dev-only, but useful to fail loudly in CI/e2e
if (import.meta.env.DEV) {
  app.config.warnHandler = (msg, _instance, trace) => {
    throw new Error(`[vue warn] ${msg}\n${trace}`)
  }
}
```

Add `onErrorCaptured` boundaries around async components and third-party widgets so a single failure does not blank the page. Ship sourcemaps to the error reporter (not to the public bundle) so stack traces are readable.
