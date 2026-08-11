# Styling

Scoped CSS semantics, `:deep()`/`:slotted()`/`:global()`, CSS Modules, reactive `v-bind()`, design tokens, and Tailwind in Vue.

## 1. Scoped Styles

```vue
<style scoped>
.card { padding: 1rem; border-radius: 8px; }
</style>
```

The compiler adds a `data-v-<hash>` attribute to the component's elements and rewrites selectors to `.card[data-v-hash]`.

### Performance: prefer class selectors

Attribute-scoped element selectors are markedly slower than class selectors because of how browsers match them.

```css
/* ❌ */
div span a { color: red; }

/* ✅ */
.card__link { color: red; }
```

### What scoped styles reach

| Target | Reached? |
|---|---|
| The component's own elements | ✅ |
| A child component's **root** element | ✅ (both parent and child hashes apply) |
| A child component's inner elements | ❌ — need `:deep()` |
| Slot content passed into this component | ❌ — need `:slotted()` |
| `v-html` content | ❌ — need `:deep()` or a global rule |
| Teleported content | ❌ in practice — use a global class |

```vue
<style scoped>
.wrapper :deep(.vendor-icon) { color: var(--accent); }  /* into a child */
:slotted(.item) { margin: 0; }                          /* slot content, from the child */
:global(.body--locked) { overflow: hidden; }            /* escape scoping */
</style>
```

`:deep()` is a deliberate escape hatch. Overusing it recreates the global-leakage problem scoping was meant to solve. Prefer exposing a prop or a CSS custom property from the child:

```vue
<!-- Child publishes a hook instead of being reached into -->
<style scoped>
.icon { color: var(--icon-color, currentColor); }
</style>
```

```vue
<!-- Parent -->
<ChildIcon style="--icon-color: red" />
```

## 2. Reactive Styles with `v-bind()`

```vue
<script setup lang="ts">
const props = defineProps<{ progress: number; accent?: string }>()
const width = computed(() => `${props.progress}%`)
</script>

<template>
  <div class="bar"><div class="bar__fill" /></div>
</template>

<style scoped>
.bar__fill {
  width: v-bind(width);
  background: v-bind('accent ?? "#3b82f6"');
}
</style>
```

`v-bind()` in `<style>` compiles to a CSS custom property updated on the component's root element. It is cheaper than a large inline `:style` object recomputed each render, and it keeps styling in the style block.

Expressions containing anything but a plain identifier must be quoted.

## 3. CSS Modules

```vue
<script setup lang="ts">
import { useCssModule } from 'vue'
const styles = useCssModule()
const cls = computed(() => [styles.btn, isPrimary.value ? styles.primary : styles.ghost])
</script>

<template>
  <button :class="cls"><slot /></button>
</template>

<style module>
.btn { padding: 0.5rem 1rem; }
.primary { background: var(--color-primary); }
.ghost { background: transparent; }
</style>
```

Use `<style module>` when class names must be **values in JavaScript** (dynamic composition, variant maps). Use `<style scoped>` otherwise — it is simpler and keeps the template readable.

Named modules: `<style module="classes">` exposes `$style` as `classes`.

## 4. Design Tokens

Define tokens once, globally, and consume them everywhere.

```css
/* src/styles/tokens.css */
:root {
  --color-bg: #ffffff;
  --color-fg: #111827;
  --color-primary: #3b82f6;
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-4: 1rem;
  --radius-md: 8px;
  --font-sans: system-ui, sans-serif;
}

:root[data-theme='dark'] {
  --color-bg: #0b0f19;
  --color-fg: #e5e7eb;
}
```

```vue
<style scoped>
.card {
  background: var(--color-bg);
  color: var(--color-fg);
  padding: var(--space-4);
  border-radius: var(--radius-md);
}
</style>
```

Custom properties cross component and scoping boundaries, which makes them the correct mechanism for theming — unlike Sass variables, which are compiled away.

### Dark mode

```ts
import { useDark, useToggle } from '@vueuse/core'
const isDark = useDark({ attribute: 'data-theme', valueDark: 'dark', valueLight: 'light' })
const toggleDark = useToggle(isDark)
```

Apply the theme attribute on the server (or in an inline head script) to avoid a flash of the wrong theme.

## 5. Tailwind in Vue

### Never build class names dynamically

Tailwind scans source files statically for complete class strings.

```vue
<!-- ❌ the class is never generated -->
<div :class="`text-${color}-500 p-${size}`" />

<!-- ✅ full class names in a lookup map -->
<script setup lang="ts">
const TONE = {
  danger: 'bg-red-500 text-white',
  success: 'bg-green-500 text-white',
  neutral: 'bg-gray-100 text-gray-900',
} as const
const props = defineProps<{ tone?: keyof typeof TONE }>()
const toneClass = computed(() => TONE[props.tone ?? 'neutral'])
</script>

<template><span :class="toneClass"><slot /></span></template>
```

### Merging with fallthrough classes

Vue merges a fallthrough `class` with the component's own. With Tailwind this can produce conflicting utilities (`p-2 p-4`). Resolve with `tailwind-merge`:

```ts
import { twMerge } from 'tailwind-merge'
const attrs = useAttrs()
const cls = computed(() => twMerge('rounded-md p-2', attrs.class as string))
```

### Tailwind and scoped styles

`@apply` inside `<style scoped>` works, but the utility classes it generates are scoped, so they cannot be overridden from a parent. Prefer utilities in the template and reserve `@apply` for genuinely repeated patterns.

## 6. Transitions and Animation

Keep transition classes **unscoped or global** when they live in a reusable wrapper component — scoped styles from the wrapper do not apply to slot content.

```vue
<!-- FadeTransition.vue -->
<template>
  <Transition name="fade" mode="out-in"><slot /></Transition>
</template>

<style>            <!-- deliberately not scoped -->
.fade-enter-active, .fade-leave-active { transition: opacity 0.2s ease; }
.fade-enter-from,   .fade-leave-to     { opacity: 0; }
</style>
```

Respect motion preferences:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

Animate `transform` and `opacity`; avoid animating `width`, `height`, `top`, and `left` (layout thrash).

## 7. Style Organization

```
src/styles/
  tokens.css        # custom properties
  reset.css         # normalize / preflight
  base.css          # element defaults, typography
  utilities.css     # a handful of app-wide helpers
```

- Global styles are imported once in `main.ts`.
- Everything else is scoped to a component.
- Use BEM-ish class names inside components (`.card`, `.card__title`, `.card--compact`) so `:deep()` targets stay readable when unavoidable.
- Keep `<style>` blocks under roughly 100 lines — beyond that the component is usually doing too much.

## Anti-Patterns

| Anti-pattern | Consequence | Fix |
|---|---|---|
| Unscoped component styles | Global leakage | `<style scoped>` |
| Element selectors in scoped CSS | Slow selector matching | Class selectors |
| `:deep()` everywhere | Scoping benefits lost | Expose props / CSS variables |
| Concatenated Tailwind classes | Class never generated | Complete strings in a map |
| Sass variables for theming | Compiled away, no runtime theming | CSS custom properties |
| Scoped transition classes in a wrapper | Animation silently absent | Unscoped/global transition CSS |
| Large inline `:style` objects | Recomputed each render | `v-bind()` in `<style>` |
| Animating `width`/`top` | Layout thrash, jank | `transform` / `opacity` |
| No `prefers-reduced-motion` handling | Accessibility failure | Media query override |
| Styling `v-html` with scoped CSS | Rules do not apply | `:deep()` or a global rule |

## Sources

- [Vue — SFC CSS features](https://vuejs.org/api/sfc-css-features.html)
- [Vue — Class and style bindings](https://vuejs.org/guide/essentials/class-and-style.html)
