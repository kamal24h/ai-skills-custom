---
name: vuejs
description: Vue 3 modern patterns — Composition API, `<script setup>`, reactivity, composables, Pinia, Vue Router, VueUse, TypeScript, SSR, and Vite. Use when building, reviewing, or auditing Vue/Nuxt apps. Triggers on "Vue", "Vue 3", ".vue", "script setup", "Composition API", "ref", "computed", "composable", "Pinia", "Vue Router", "VueUse", "Nuxt", "Vite".
model: inherit
---

# Vue.js Best Practices

Modern Vue 3 patterns — Composition API with `<script setup lang="ts">`, the reactivity system, composables, component contracts, Pinia state, Vue Router, and SSR/hydration. Focused on predictable state, explicit data flow, testability, and performance.

## Specialized Agents

| Agent | Role | Focus |
|-------|------|-------|
| **vue-pro** | Vue Expert | SFC structure, component design, templates, built-ins, accessibility. |
| **vue-reactivity-pro** | Reactivity Expert | ref/shallowRef, computed, watchers, effect scope, composables. |
| **vue-state-pro** | State & Routing Expert | Pinia stores, provide/inject, Vue Router 4, SSR-safe state. |
| **vue-build-pro** | Build & Types Expert | Vite, vue-tsc, TypeScript contracts, ESLint, SSR/Nuxt config. |

## When to Use

Reference these guidelines when:
- Building or refactoring Vue 3 / Nuxt 3+ applications
- Writing SFCs with `<script setup>` and compiler macros
- Choosing reactive primitives (`ref`, `shallowRef`, `reactive`, `computed`, `watch`)
- Extracting logic into composables or designing library-grade composable APIs
- Defining component contracts (props, emits, `v-model`, slots, provide/inject)
- Managing shared state with Pinia or lightweight global state
- Implementing routing, navigation guards, and lazy route components
- Using built-in components (`Transition`, `Teleport`, `Suspense`, `KeepAlive`)
- Diagnosing reactivity loss, hydration mismatches, or unexpected re-renders
- Optimizing large lists, unstable props, or expensive computed values
- Applying VueUse composables instead of bespoke browser-API code

## Step 1: Detect Target Environment

**Always check the Vue version, API style, build tool, and TypeScript setup before recommending anything.**

Check `package.json`, `vite.config.ts`, and `tsconfig.json`:
```jsonc
// package.json
{
  "dependencies": { "vue": "^3.5.13", "pinia": "^3.0.0", "vue-router": "^4.5.0" },
  "devDependencies": { "vite": "^7.0.0", "vue-tsc": "^2.2.0" }
}
```

### Feature Availability by Version

| Feature | Version |
|---------|---------|
| `<script setup>` (stable) | Vue 3.2+ |
| `defineOptions`, `defineSlots`, generic components | Vue 3.3+ |
| `defineModel` (stable) | Vue 3.4+ |
| `useTemplateRef()` | Vue 3.5+ |
| Reactive props destructure with defaults | Vue 3.5+ |
| `onWatcherCleanup()` | Vue 3.5+ |
| `useId()` (SSR-safe unique ids) | Vue 3.5+ |
| Lazy hydration for async components | Vue 3.5+ |
| `defineAsyncComponent` hydration strategies | Vue 3.5+ |
| Pinia setup stores | Pinia 2+ |
| `data-allow-mismatch` hydration escape hatch | Vue 3.5+ |

### API Style Detection

- **Default:** Composition API + `<script setup lang="ts">`. Use this unless the project explicitly says otherwise.
- **Options API project:** Only follow existing style; see `references/composition-api.md` § Options API interop.
- **JSX/TSX project:** See `references/typescript.md` § JSX in Vue — `class` not `className`, no auto-unwrapping of refs in JSX.

## Step 2: Choose the Right Guidance Set

- Load `references/composition-api.md` before writing any SFC or compiler macro.
- Load `references/reactivity.md` before choosing a reactive primitive, computed, or watcher.
- Load `references/composables.md` before extracting or designing a `useXxx()` function.
- Load `references/component-design.md` before defining props/emits/slots/provide-inject contracts.
- Load `references/sfc-templates.md` before writing templates, directives, or scoped styles.
- Load `references/typescript.md` before typing props, refs, events, or generic components.
- Load `references/state-management.md` before adding Pinia or any app-wide shared state.
- Load `references/routing.md` before touching routes or navigation guards.
- Load `references/builtin-components.md` before using Transition/Teleport/Suspense/KeepAlive.
- Load `references/performance.md` **only after** behavior is correct and verified.
- Load `references/architecture.md` before creating folder structure or an API/service layer.
- Load `references/forms-validation.md` before building forms or `v-model` bindings.
- Load `references/styling.md` before writing scoped CSS, CSS Modules, or Tailwind classes.
- Load `references/ssr-hydration.md` before working on SSR, Nuxt, or hydration bugs.
- Load `references/vueuse.md` before hand-rolling browser-API or utility composables.
- Load `references/tooling-build.md` before changing Vite, vue-tsc, or ESLint config.
- Load `references/debugging.md` when diagnosing a runtime warning, silent reactivity loss, or flaky render.
- Load `vuejs-tester` before authoring tests so implementation and test guidance stay aligned.

## Step 3: Plan Component Boundaries Before Coding

For any non-trivial feature, write a short component map first.

- Give each component a **single responsibility** stated in one sentence.
- Keep `App.vue` and route-level views as **composition surfaces** — layout, provider wiring, feature composition.
- **Split** a component when any of these is true: it owns both orchestration/state and substantial markup; it has 3+ distinct UI sections; a template block repeats or could be reused.
- Move state and side effects into composables (`useXxx()`); move UI sections into child components (props in, events out).
- Define the props/emits contract for each child in the map before implementing.

## Core Directives

### MUST DO

- **API Style:** Use Composition API with `<script setup lang="ts">`. Keep SFC block order `<script>` → `<template>` → `<style>`.
- **Reactivity:** Keep source state minimal; derive everything possible with `computed`. Use `shallowRef` for primitives and opaque/external objects.
- **Watchers:** Use watchers for side effects only. Pass a getter (`() => state.x`) as the source. Clean up async work with `onCleanup` / `onWatcherCleanup`.
- **Data Flow:** Props down, events up. `v-model` only for genuine two-way contracts. `provide`/`inject` only for deep-tree context, always with a typed `InjectionKey`.
- **Contracts:** Declare all props with `defineProps<T>()` and all events with `defineEmits<T>()`. Type-based declarations, not runtime objects.
- **Composables:** Name them `useXxx`. Return plain refs (destructurable). Accept `MaybeRefOrGetter<T>` for read-only inputs and normalize with `toValue()`/`toRef()`.
- **Lists:** Always provide a stable, unique `:key` on `v-for`. Never use array index as key for mutable lists.
- **Cleanup:** Every listener, timer, observer, and subscription registered in `setup` must be torn down in `onUnmounted` (or via VueUse, which does it for you).
- **Templates:** Keep templates declarative. Move branching, filtering, and sorting into `computed`.
- **Pinia:** Use setup stores. Destructure state/getters with `storeToRefs()`; call actions directly off the store.
- **SSR:** Register `provide`/`inject`, lifecycle hooks, and `defineExpose` **synchronously**, before any `await`.
- **TypeScript:** Run `vue-tsc --noEmit` in CI. Use `useTemplateRef<T>()` (3.5+) for DOM/component refs.
- **Security:** Treat `v-html` as forbidden for any value that is not sanitized and provably trusted.

### MUST NOT DO

- **Mutating props:** Never assign to a prop. Emit an event or use `defineModel`.
- **Destructuring `reactive()`:** Never destructure a `reactive()` object — reactivity is lost. Use `toRefs()`.
- **Destructuring a store:** Never destructure a Pinia store directly — use `storeToRefs()`.
- **Side effects in `computed`:** Never mutate state, call APIs, write storage, or emit from a computed getter.
- **`v-if` with `v-for`:** Never put both on the same element — filter in a `computed` instead.
- **Async composable calls:** Never call a composable after `await` or inside a conditional/loop/callback — lifecycle binding is lost.
- **Module-level mutable state:** Never export mutable module-scope state in an SSR/Nuxt app — it leaks across requests.
- **Index as key:** Never use `:key="index"` for lists that reorder, filter, or splice.
- **Untyped `any` props:** Never fall back to `any` in a public component contract.
- **`v-html` with user input:** Never render untrusted HTML — XSS.
- **Premature optimization:** Never add `v-memo`, `v-once`, or virtualization before functionality is complete and a real bottleneck is measured.
- **Options API in a Composition project:** Never mix styles in the same component; never use `mixins` in new code.

## Category Index — When to Load Which Reference

| # | Category | Impact | Load when… | Reference |
|--:|----------|:------:|------------|-----------|
| 1 | Composition API | CRITICAL | `<script setup>`, macros, lifecycle, generics | [`references/composition-api.md`](references/composition-api.md) |
| 2 | Reactivity | CRITICAL | ref/shallowRef/reactive, computed, watchers | [`references/reactivity.md`](references/reactivity.md) |
| 3 | Composables | CRITICAL | Extracting logic, adaptable/reusable `useXxx()` | [`references/composables.md`](references/composables.md) |
| 4 | Component Design | CRITICAL | Props, emits, v-model, slots, provide/inject | [`references/component-design.md`](references/component-design.md) |
| 5 | SFC & Templates | CRITICAL | Template syntax, directives, refs, scoped CSS | [`references/sfc-templates.md`](references/sfc-templates.md) |
| 6 | TypeScript | HIGH | Typing props/emits/refs, generics, JSX, vue-tsc | [`references/typescript.md`](references/typescript.md) |
| 7 | State Management | HIGH | Pinia stores, global state, SSR-safe state | [`references/state-management.md`](references/state-management.md) |
| 8 | Routing | HIGH | Vue Router 4, guards, params, lazy routes | [`references/routing.md`](references/routing.md) |
| 9 | Built-in Components | HIGH | Transition, Teleport, Suspense, KeepAlive, async | [`references/builtin-components.md`](references/builtin-components.md) |
| 10 | Performance | HIGH | Large lists, re-renders, v-memo, stability | [`references/performance.md`](references/performance.md) |
| 11 | Architecture | HIGH | Folder layout, layers, API/service boundary | [`references/architecture.md`](references/architecture.md) |
| 12 | Forms & Validation | MEDIUM | v-model on inputs, modifiers, IME, validation | [`references/forms-validation.md`](references/forms-validation.md) |
| 13 | Styling | MEDIUM | Scoped CSS, CSS Modules, `v-bind()` in CSS, Tailwind | [`references/styling.md`](references/styling.md) |
| 14 | SSR & Hydration | MEDIUM | Nuxt, hydration mismatch, cross-request leaks | [`references/ssr-hydration.md`](references/ssr-hydration.md) |
| 15 | VueUse | MEDIUM | Browser APIs, sensors, utilities, shared state | [`references/vueuse.md`](references/vueuse.md) |
| 16 | Tooling & Build | MEDIUM | Vite, vue-tsc, ESLint, aliases, env vars | [`references/tooling-build.md`](references/tooling-build.md) |
| 17 | Debugging | MEDIUM | Warnings, silent reactivity loss, devtools | [`references/debugging.md`](references/debugging.md) |

## Rule Index

### 1. Composition API (`vue-`) — CRITICAL
`vue-script-setup-ts` · `vue-type-based-macros` · `vue-macros-top-level` · `vue-no-runtime-and-type-emits` · `vue-define-expose-before-await` · `vue-lifecycle-sync-registration` · `vue-no-named-exports-in-setup` · `vue-define-options-over-second-script` · `vue-no-mixins` · `vue-no-options-composition-mix` · `vue-use-id-for-ssr-ids`

### 2. Reactivity (`rx-`) — CRITICAL
`rx-shallow-ref-primitives` · `rx-no-reactive-destructure` · `rx-computed-over-watch` · `rx-computed-pure` · `rx-computed-no-params` · `rx-computed-no-array-mutation` · `rx-watch-getter-source` · `rx-watch-immediate` · `rx-watch-async-cleanup` · `rx-watch-flush-post-for-dom` · `rx-no-async-watcher-creation` · `rx-markraw-external-instances` · `rx-deep-watch-clone-old-value` · `rx-effect-scope-manual-effects` · `rx-refs-in-collections-need-value` · `rx-next-tick-for-dom-reads`

### 3. Composables (`comp-`) — CRITICAL
`comp-use-prefix` · `comp-sync-call-in-setup` · `comp-return-refs-not-reactive` · `comp-maybe-ref-or-getter-input` · `comp-tovalue-inside-effect` · `comp-options-object-params` · `comp-readonly-state-explicit-actions` · `comp-no-hidden-side-effects` · `comp-cleanup-on-scope-dispose` · `comp-plain-utils-stay-utils`

### 4. Component Design (`cmp-`) — CRITICAL
`cmp-no-prop-mutation` · `cmp-declare-emits` · `cmp-props-down-events-up` · `cmp-define-model-for-two-way` · `cmp-define-model-object-emit` · `cmp-no-ref-over-props` · `cmp-expose-explicitly` · `cmp-inject-key-typed` · `cmp-provide-reactive-wrapper` · `cmp-inject-default-factory` · `cmp-inherit-attrs-false-wrappers` · `cmp-slot-forwarding` · `cmp-single-responsibility` · `cmp-thin-route-views`

### 5. SFC & Templates (`tpl-`) — CRITICAL
`tpl-stable-key` · `tpl-no-vif-with-vfor` · `tpl-no-side-effects-in-template` · `tpl-no-expensive-expressions` · `tpl-vif-null-check-order` · `tpl-v-show-vs-v-if` · `tpl-use-template-ref` · `tpl-template-ref-null-guard` · `tpl-pascal-case-components` · `tpl-no-v-html-untrusted` · `tpl-camel-case-style-bindings` · `tpl-self-closing-components`

### 6. TypeScript (`ts-`) — HIGH
`ts-with-defaults-factory` · `ts-no-reactive-generic-arg` · `ts-template-ref-null-handling` · `ts-boolean-prop-undefined` · `ts-event-handler-typing` · `ts-generic-components` · `ts-shallow-ref-dynamic-component` · `ts-vue-tsc-in-ci` · `ts-defineprops-local-types`

### 7. State Management (`store-`) — HIGH
`store-setup-store-style` · `store-return-all-state` · `store-use-storetorefs` · `store-action-binding` · `store-no-module-mutable-state` · `store-pinia-instance-per-request` · `store-url-for-ephemeral-state` · `store-no-active-pinia-outside-setup` · `store-colocate-by-domain`

### 8. Routing (`router-`) — HIGH
`router-no-next-callback` · `router-guard-await-async` · `router-no-guard-redirect-loop` · `router-watch-params-not-lifecycle` · `router-beforerouteenter-no-this` · `router-lazy-route-components` · `router-typed-meta` · `router-cleanup-on-unmount`

### 9. Performance (`perf-`) — HIGH
`perf-virtualize-large-lists` · `perf-stable-props` · `perf-computed-object-stability` · `perf-v-memo-hot-lists` · `perf-v-once-static-subtrees` · `perf-no-abstraction-in-hot-lists` · `perf-shallow-for-large-data` · `perf-lazy-async-components` · `perf-no-updated-hook-work`

### 10. Architecture (`arch-`) — HIGH
`arch-feature-folders` · `arch-api-layer-isolated` · `arch-no-store-in-dumb-components` · `arch-typed-domain-models` · `arch-no-cross-feature-imports` · `arch-env-config-centralized`

### 11. Built-ins (`builtin-`) — MEDIUM
`builtin-transition-single-element` · `builtin-transition-js-done-callback` · `builtin-transition-group-key` · `builtin-teleport-target-exists` · `builtin-suspense-error-boundary` · `builtin-keepalive-include-by-name` · `builtin-async-component-error-ui`

### 12. Forms (`form-`) — MEDIUM
`form-v-model-over-value-input` · `form-no-html-value-attribute` · `form-number-modifier-guard` · `form-ime-composition-aware` · `form-checkbox-true-false-value` · `form-label-association`

### 13. Styling (`css-`) — MEDIUM
`css-scoped-by-default` · `css-class-selectors-in-scoped` · `css-deep-selector-explicit` · `css-modules-for-shared` · `css-v-bind-for-dynamic` · `css-no-dynamic-tailwind-classes`

### 14. SSR (`ssr-`) — MEDIUM
`ssr-no-cross-request-state` · `ssr-guard-browser-apis` · `ssr-deterministic-render` · `ssr-client-only-for-nondeterministic` · `ssr-teleport-target-ssr-safe`

### 15. Security & Accessibility (`sec-`, `a11y-`) — HIGH
`sec-no-untrusted-v-html` · `sec-no-dynamic-component-from-input` · `sec-no-secrets-in-client-env` · `a11y-semantic-elements` · `a11y-focus-management` · `a11y-aria-live-for-async`

## Validation Checklist

- [ ] `<script setup lang="ts">` used; SFC blocks ordered script → template → style
- [ ] All props declared via type-based `defineProps<T>()`; no prop mutation
- [ ] All emitted events declared via `defineEmits<T>()`
- [ ] `defineModel` used for two-way contracts instead of manual `modelValue` + `update:modelValue`
- [ ] Macros, lifecycle hooks, `provide`/`inject`, and `defineExpose` are called synchronously before any `await`
- [ ] `shallowRef` used for primitives and opaque/external objects
- [ ] No destructuring of `reactive()` objects or Pinia stores (`toRefs` / `storeToRefs` used)
- [ ] Derived values use `computed`; computed getters are pure
- [ ] Watcher sources are refs or getters; async watchers clean up with `onCleanup`
- [ ] Every `v-for` has a stable, unique `:key`; no `v-if` on the same element
- [ ] No expensive filtering/sorting or function calls with side effects in templates
- [ ] Composables named `useXxx`, called at setup top level, returning plain refs
- [ ] Reactive composable inputs typed `MaybeRefOrGetter<T>` and read with `toValue()`
- [ ] All listeners/timers/observers cleaned up on unmount
- [ ] `provide`/`inject` uses a typed `InjectionKey`; object defaults use a factory
- [ ] Pinia setup stores return all state; `storeToRefs()` used at call sites
- [ ] No mutable module-scope state in SSR/Nuxt code paths
- [ ] Route components lazy-loaded; guards `await` async work and cannot loop
- [ ] `v-html` absent, or provably sanitized and trusted
- [ ] Scoped styles used; no dynamically concatenated Tailwind class names
- [ ] `vue-tsc --noEmit` passes with no errors
- [ ] Performance directives (`v-memo`, `v-once`, virtualization) added only after a measured bottleneck
- [ ] Interactive elements are semantic, labelled, and keyboard-reachable

## External References

- [Vue 3 Documentation](https://vuejs.org/guide/introduction.html)
- [Vue 3 API Reference](https://vuejs.org/api/)
- [Vue Style Guide](https://vuejs.org/style-guide/)
- [Vue Router 4](https://router.vuejs.org/)
- [Pinia](https://pinia.vuejs.org/)
- [VueUse](https://vueuse.org/)
- [Vite](https://vite.dev/)
- [Nuxt](https://nuxt.com/docs)
- [Vue TypeScript Guide](https://vuejs.org/guide/typescript/overview.html)
- [Vue SSR Guide](https://vuejs.org/guide/scaling-up/ssr.html)
