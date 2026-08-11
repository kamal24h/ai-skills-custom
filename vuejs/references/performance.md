# Performance

**Run this pass only after behavior is correct and verified.** Measure first — Vue's reactivity is rarely the bottleneck; DOM node count, network waterfalls, and bundle size usually are.

## 1. Measurement Before Optimization

| Tool | Finds |
|---|---|
| Vue DevTools → Timeline / Component render tracking | Which components re-render and why |
| Chrome Performance panel | Long tasks, layout thrash, scripting vs rendering split |
| `onRenderTracked` / `onRenderTriggered` | Exactly which dependency triggered a re-render |
| `rollup-plugin-visualizer` / `vite build --report` | Bundle composition |
| Lighthouse / Web Vitals | LCP, INP, CLS regressions |

```ts
onRenderTriggered((e) => {
  console.log('re-render because', e.type, e.key, e.target)
})
```

Both hooks are dev-only and are the fastest way to answer "why did this re-render?".

## 2. Bundle & Load

### Route-level splitting

```ts
{ path: '/reports', component: () => import('@/views/ReportsView.vue') }
```

Every route becomes its own chunk. This is the single highest-leverage change in most Vue apps.

### Component-level splitting

```ts
const ChartPanel = defineAsyncComponent(() => import('./ChartPanel.vue'))
```

For modals, editors, charts, maps, and anything below the fold. Define at module scope, not inside `setup()`.

### Lazy hydration (Vue 3.5+, SSR only)

```ts
import { defineAsyncComponent, hydrateOnVisible, hydrateOnIdle, hydrateOnInteraction } from 'vue'

const Comments = defineAsyncComponent({
  loader: () => import('./Comments.vue'),
  hydrate: hydrateOnVisible(),
})
```

Server-rendered markup appears immediately; the JS cost is deferred until the component is visible/idle/interacted with.

### Dependency hygiene

- Prefer per-function imports over whole libraries (`import { debounce } from 'lodash-es'`, or VueUse's `useDebounceFn`).
- Check for duplicate date/i18n/icon libraries in the bundle report.
- Move heavy, rarely-needed parsing (markdown, syntax highlighting, PDF) behind a dynamic import.

## 3. Reactivity Cost

### Shallow for large or opaque data

```ts
// ❌ Vue walks and proxies the entire tree
const data = ref(hugeNestedApiResponse)

// ✅ replacement-based updates only
const data = shallowRef(hugeNestedApiResponse)
data.value = nextResponse

// ✅ external instance never proxied
const chart = shallowRef(markRaw(new Chart(el, cfg)))
```

Deep reactivity on a 10k-node object costs on every read and every write. If updates are replacement-based, `shallowRef` is strictly better.

### Primitives

`shallowRef` for every string/number/boolean — deep tracking has no purpose there.

### Computed object stability

A computed that returns a **new** object/array each evaluation retriggers every downstream effect, even when the content is identical.

```ts
// ❌ new object identity every time `opts` or `defaults` change at all
const config = computed(() => ({ ...defaults, ...props.opts }))
watch(config, applyConfig, { deep: true })   // fires constantly

// ✅ derive primitives
const density = computed(() => props.opts.density ?? defaults.density)

// ✅ or gate on structural equality
const config = shallowRef(build())
watchEffect(() => {
  const next = build()
  if (!isEqual(next, config.value)) config.value = next
})
```

### Narrow watcher sources

```ts
// ❌ traverses the whole object on every change anywhere
watch(user, save, { deep: true })

// ✅
watch(() => user.value.email, save)
```

Vue 3.5+ supports `deep: <number>` to bound traversal depth when a deep watch is unavoidable.

## 4. Rendering Cost

### Virtualize long lists

Beyond a few hundred rows the bottleneck is DOM node count, not Vue.

```vue
<script setup lang="ts">
import { useVirtualList } from '@vueuse/core'
const { list, containerProps, wrapperProps } = useVirtualList(rows, { itemHeight: 44 })
</script>

<template>
  <div v-bind="containerProps" style="height: 600px">
    <div v-bind="wrapperProps">
      <div v-for="{ data, index } in list" :key="data.id">{{ data.name }}</div>
    </div>
  </div>
</template>
```

Alternatives: `vue-virtual-scroller`, `@tanstack/vue-virtual`. Or paginate — often the better product answer.

### Stable props

Object/array literals and inline arrows in templates create a new identity on every render, forcing child updates.

```vue
<!-- ❌ new object + new function per row per render -->
<Row v-for="r in rows" :key="r.id" :config="{ dense: true }" @click="() => select(r)" />

<!-- ✅ -->
<Row v-for="r in rows" :key="r.id" :config="rowConfig" :row="r" @click="select" />
```

```ts
const rowConfig = { dense: true }        // hoisted, stable identity
function select(row: Row) { /* ... */ }  // stable reference
```

The compiler hoists static props automatically; it cannot hoist expressions that close over render-scope variables.

### Avoid over-abstraction in hot paths

Each component instance carries setup, props resolution, and patch cost. In a 1,000-row × 20-column table, a `<Cell>` component wrapping a single `<span>` multiplies that by 20,000.

```vue
<!-- ✅ inline the trivial markup in the hot path; keep components at the row level -->
<tr v-for="row in rows" :key="row.id">
  <td v-for="col in columns" :key="col.key">{{ row[col.key] }}</td>
</tr>
```

This is a targeted exception, not general advice — component abstraction is correct nearly everywhere else.

### `v-memo` for measured hot lists

```vue
<div v-for="row in rows" :key="row.id" v-memo="[row.id === selectedId, row.version]">
  <ExpensiveRow :row="row" />
</div>
```

The subtree re-renders only when a listed dependency changes. A missing dependency produces stale UI — measure, then apply, then verify.

### `v-once` for static subtrees

```vue
<footer v-once>{{ legalText }}</footer>
```

Never updates again. Only for genuinely immutable content.

### `v-show` vs `v-if`

`v-if` unmounts and remounts (full setup cost); `v-show` toggles `display`. For a panel toggled dozens of times per session, `v-show` is much cheaper. For a heavy subtree that is usually hidden, `v-if` avoids the initial mount entirely.

## 5. Update Loops and `onUpdated`

```ts
// ❌ runs after every re-render; mutating state here loops forever
onUpdated(() => { height.value = el.value!.offsetHeight })

// ✅ targeted
watch(content, async () => {
  await nextTick()
  height.value = el.value?.offsetHeight ?? 0
}, { flush: 'post' })

// ✅ or observe the DOM directly
useResizeObserver(el, ([entry]) => { height.value = entry.contentRect.height })
```

## 6. Event and Effect Throttling

```ts
import { useDebounceFn, useThrottleFn, refDebounced } from '@vueuse/core'

const search = useDebounceFn(runSearch, 300)              // trailing input
const onScroll = useThrottleFn(updateHeader, 100)         // continuous events
const debouncedQuery = refDebounced(query, 300)           // debounce the value itself
```

Debounce user input; throttle scroll/resize/pointermove. Pair with an `AbortController` in the watcher so superseded requests are cancelled, not just delayed.

## 7. Images and Assets

- Explicit `width`/`height` (or `aspect-ratio`) on every image to prevent CLS.
- `loading="lazy"` + `decoding="async"` for below-the-fold images.
- Modern formats (AVIF/WebP) with `<picture>` fallbacks.
- `<link rel="preload">` for the LCP image only.
- Self-host fonts with `font-display: swap` and preload the primary weight.

## 8. Optimization Order

1. Ship less JavaScript — route splitting, async components, dependency pruning.
2. Render fewer DOM nodes — pagination or virtualization.
3. Reduce reactivity surface — `shallowRef`, narrow watchers, stable computed outputs.
4. Reduce re-render triggers — stable props, hoisted objects, `computed` over template expressions.
5. Only then micro-optimize — `v-memo`, `v-once`, inlining in hot paths.

## Anti-Patterns

| Anti-pattern | Consequence | Fix |
|---|---|---|
| Optimizing before measuring | Wasted effort, added risk | DevTools + `onRenderTriggered` first |
| `ref(hugeObject)` | Deep proxy over the whole tree | `shallowRef` |
| Deep watch on a large object | Traversal cost on every change | Narrow getter, or `deep: <number>` |
| Computed returning a fresh object | Downstream effects fire constantly | Derive primitives / structural gate |
| Inline object/arrow props in a list | New identity every render | Hoist config, use named handlers |
| 10k `v-for` rows | Frozen scroll, huge memory | Virtualize or paginate |
| Per-cell components in a big grid | Multiplied instance overhead | Inline the trivial markup |
| `v-memo` with wrong deps | Stale UI | Measure, list every dep, verify |
| Work in `onUpdated` | Runs constantly, can loop | `watch` + `flush: 'post'` / observers |
| Static imports of every view | Huge initial bundle | `() => import()` |

## Sources

- [Vue — Performance](https://vuejs.org/guide/best-practices/performance.html)
- [Vue — Rendering mechanism](https://vuejs.org/guide/extras/rendering-mechanism.html)
