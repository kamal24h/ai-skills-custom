# Rules for Vue 3 Development

Actionable directives for modern Vue 3 — Composition API, reactivity, composables, component contracts, Pinia, Vue Router, and SSR.

## 1. Composition API (`vue-`)

### `vue-script-setup-ts`
- **Context:** Component authoring.
- **Rule:** Author every new component as `<script setup lang="ts">`. Keep block order `<script>` → `<template>` → `<style>`.
- **Avoid:** `export default { setup() {} }`, `defineComponent` wrappers in SFCs, or Options API in a Composition-API project.

### `vue-type-based-macros`
- **Context:** Compiler macros.
- **Rule:** Declare props and emits with type arguments: `defineProps<{ id: string }>()`, `defineEmits<{ save: [id: string] }>()`.
- **Avoid:** Runtime object declarations (`defineProps({ id: String })`) in TypeScript components.

### `vue-macros-top-level`
- **Context:** Compiler macros.
- **Rule:** Call `defineProps`, `defineEmits`, `defineModel`, `defineSlots`, `defineOptions`, and `defineExpose` at the top level of `<script setup>` only.
- **Avoid:** Calling a macro inside a function, conditional, loop, or callback — it will not compile.

### `vue-no-runtime-and-type-emits`
- **Context:** Emits declaration.
- **Rule:** Use either the type argument or the runtime argument for `defineEmits`, never both.
- **Avoid:** `defineEmits<{ save: [] }>(['save'])` — compilation error.

### `vue-define-expose-before-await`
- **Context:** Async `<script setup>`.
- **Rule:** Call `defineExpose()` before the first `await`. After an `await`, the setup context is gone and the parent's template ref sees nothing.
- **Avoid:** `const data = await load(); defineExpose({ data })`.

### `vue-lifecycle-sync-registration`
- **Context:** Lifecycle hooks.
- **Rule:** Register `onMounted`, `onUnmounted`, `provide`, `inject`, and watchers synchronously during setup, before any `await`.
- **Avoid:** `await load(); onMounted(() => ...)` — the hook silently never runs.

### `vue-no-named-exports-in-setup`
- **Context:** SFC structure.
- **Rule:** `<script setup>` cannot have named exports. Put shared helpers/types in a sibling `.ts` file, or use a separate plain `<script>` block for module-scope code.
- **Avoid:** `export const FOO = 1` inside `<script setup>`.

### `vue-define-options-over-second-script`
- **Context:** Component options.
- **Rule:** Use `defineOptions({ name, inheritAttrs })` (Vue 3.3+) instead of adding a second `<script>` block just to set options.
- **Avoid:** `<script>export default { inheritAttrs: false }</script>` alongside `<script setup>`.

### `vue-no-mixins`
- **Context:** Code reuse.
- **Rule:** Use composables for shared logic. Mixins have implicit name collisions and untraceable property origins.
- **Avoid:** `mixins: [...]` in any new code.

### `vue-no-options-composition-mix`
- **Context:** API style consistency.
- **Rule:** One API style per component. If a project is Options API, follow it consistently; do not sprinkle `setup()` into Options components without a migration plan.
- **Avoid:** `data()` + `setup()` in the same component for convenience.

### `vue-use-id-for-ssr-ids`
- **Context:** Unique DOM ids (Vue 3.5+).
- **Rule:** Use `useId()` to generate ids for label/input associations and ARIA references. It is stable across server and client.
- **Avoid:** `Math.random()`, incrementing module counters, or `crypto.randomUUID()` for render-time ids — they cause hydration mismatches.

## 2. Reactivity (`rx-`)

### `rx-shallow-ref-primitives`
- **Context:** State declaration.
- **Rule:** Use `shallowRef()` for primitive values (string, number, boolean, null) — deep tracking is pure overhead.
- **Avoid:** `ref(0)` when the value is always a primitive.

### `rx-no-reactive-destructure`
- **Context:** Reactivity loss.
- **Rule:** Never destructure a `reactive()` object. Use `toRefs(state)` to get refs, or access via `state.x`.
- **Avoid:** `const { count } = reactive({ count: 0 })` — `count` is a disconnected snapshot.

### `rx-computed-over-watch`
- **Context:** Derived state.
- **Rule:** Derive values with `computed`. A watcher that only assigns to another ref should be a `computed`.
- **Avoid:** `watchEffect(() => { total.value = items.value.reduce(...) })`.

### `rx-computed-pure`
- **Context:** Computed purity.
- **Rule:** A computed getter only derives a value — no mutation, no fetch, no storage write, no `emit`, no logging side effects.
- **Avoid:** `computed(() => { if (n.value > 10) notify(); return n.value * 2 })`.

### `rx-computed-no-params`
- **Context:** Computed API.
- **Rule:** Computed refs take no parameters. For parameterized derivation, return a function from `computed`, or use a plain method, or build a lookup `Map` in the computed.
- **Avoid:** `computed((id) => items.value.find(i => i.id === id))`.

### `rx-computed-no-array-mutation`
- **Context:** Array derivation.
- **Rule:** Copy before `sort()`/`reverse()` inside a computed: `[...items.value].sort(...)`. These methods mutate in place.
- **Avoid:** `computed(() => items.value.sort(fn))` — corrupts source order and can loop.

### `rx-watch-getter-source`
- **Context:** Watcher sources.
- **Rule:** Pass a ref, a getter (`() => state.count`), a reactive object, or an array of these. Wrap reactive property access in a getter.
- **Avoid:** `watch(state.count, cb)` — passes a plain value; the watcher never fires.

### `rx-watch-immediate`
- **Context:** Initial execution.
- **Rule:** Use `{ immediate: true }` instead of duplicating the callback in `onMounted`.
- **Avoid:** `onMounted(() => load(id.value)); watch(id, load)`.

### `rx-watch-async-cleanup`
- **Context:** Async watchers.
- **Rule:** Cancel superseded async work. Use the third `onCleanup` argument (or `onWatcherCleanup()` in 3.5+) with an `AbortController`.
- **Avoid:** Unguarded `await fetch(...)` in a watcher — a slow earlier response overwrites a newer one.

### `rx-watch-flush-post-for-dom`
- **Context:** Flush timing.
- **Rule:** Use `{ flush: 'post' }` (or `watchPostEffect`) when the callback reads the DOM or a template ref. The default `pre` flush runs before the DOM updates.
- **Avoid:** Reading `el.value.offsetHeight` in a default-flush watcher and getting stale values.

### `rx-no-async-watcher-creation`
- **Context:** Watcher lifetime.
- **Rule:** Create watchers synchronously in setup. A watcher created inside an async callback is not bound to the component and leaks.
- **Avoid:** `onMounted(async () => { await x(); watch(a, cb) })`.

### `rx-markraw-external-instances`
- **Context:** Third-party objects.
- **Rule:** Wrap external instances (map SDKs, chart objects, class instances, WebGL contexts) in `markRaw()` or store them in `shallowRef` so Vue does not proxy their internals.
- **Avoid:** `reactive({ map: new mapboxgl.Map(...) })` — proxying breaks identity checks and private fields.

### `rx-deep-watch-clone-old-value`
- **Context:** Deep watchers.
- **Rule:** With `{ deep: true }` on an object source, `oldValue` and `newValue` are the same reference. Snapshot with `structuredClone`/a getter returning a derived primitive if you need the previous value.
- **Avoid:** Comparing `newVal !== oldVal` in a deep watcher and expecting a difference.

### `rx-effect-scope-manual-effects`
- **Context:** Effects outside components.
- **Rule:** Wrap effects created outside a component (stores, singletons, manually managed lifetimes) in `effectScope()` and dispose with `scope.stop()`. Use `onScopeDispose()` for cleanup inside composables.
- **Avoid:** Creating watchers in module scope with no disposal path.

### `rx-refs-in-collections-need-value`
- **Context:** Ref unwrapping.
- **Rule:** Refs are only auto-unwrapped as properties of a `reactive` object and at the top level of templates. Inside arrays, `Map`, and `Set`, access `.value` explicitly.
- **Avoid:** `const list = reactive([ref(1)]); list[0] + 1`.

### `rx-next-tick-for-dom-reads`
- **Context:** DOM timing.
- **Rule:** `await nextTick()` before reading the DOM after a state change. Vue batches DOM updates.
- **Avoid:** `open.value = true; modal.value.focus()` — `modal.value` is still `null`.

## 3. Composables (`comp-`)

### `comp-use-prefix`
- **Context:** Naming.
- **Rule:** Name composables `useSomething` in camelCase; file `composables/useSomething.ts`. The name signals setup-context requirements to both humans and lint rules.
- **Avoid:** `getUser()`, `userHelper()` for functions that create refs or register effects.

### `comp-sync-call-in-setup`
- **Context:** Call location.
- **Rule:** Call composables synchronously at the top level of `<script setup>` (or in another composable, or inside an active `effectScope`).
- **Avoid:** Calling a composable after `await`, in a conditional, in a loop, or inside an event handler.

### `comp-return-refs-not-reactive`
- **Context:** Return shape.
- **Rule:** Return a plain object of refs/computeds/functions so callers can destructure without losing reactivity.
- **Avoid:** `return reactive({ count, inc })` — destructuring at the call site breaks reactivity.

### `comp-maybe-ref-or-getter-input`
- **Context:** Adaptable inputs.
- **Rule:** Type read-only reactive inputs as `MaybeRefOrGetter<T>` so callers may pass a value, ref, or getter. Use `MaybeRef<T>` when the input must be writable (two-way).
- **Avoid:** Forcing callers to `unref()` or to always pass a ref. Also avoid `MaybeRefOrGetter` for parameters that may legitimately be functions (callbacks, predicates, comparators) — they would be invoked as getters.

### `comp-tovalue-inside-effect`
- **Context:** Input normalization.
- **Rule:** Resolve `MaybeRefOrGetter` inputs with `toValue()` **inside** the reactive effect (`watch`/`watchEffect`/`computed`), or convert once with `toRef()` for use as a watcher source.
- **Avoid:** `const v = toValue(input)` at the top of the composable — it snapshots the value and never updates.

### `comp-options-object-params`
- **Context:** Composable signature.
- **Rule:** Take required inputs positionally and everything else as a single `options` object with defaults. Keeps the API extensible without breaking callers.
- **Avoid:** `useFetch(url, immediate, retries, timeout, onError)` — boolean-trap positional parameters.

### `comp-readonly-state-explicit-actions`
- **Context:** Encapsulation.
- **Rule:** Expose state as `readonly(...)` / computed and provide explicit action functions for mutation.
- **Avoid:** Returning a writable internal ref and relying on convention for who mutates it.

### `comp-no-hidden-side-effects`
- **Context:** Predictability.
- **Rule:** A composable mutates only its own state, plus effects it clearly documents (DOM, storage, network). Do not silently mutate arguments or external module state.
- **Avoid:** `useSelection(items)` that reorders the caller's `items` array.

### `comp-cleanup-on-scope-dispose`
- **Context:** Teardown.
- **Rule:** Every listener, timer, observer, or subscription created by a composable must be released in `onScopeDispose()` (works in components and in manual scopes).
- **Avoid:** Registering `window.addEventListener` with no removal — memory leak plus duplicate handlers on remount.

### `comp-plain-utils-stay-utils`
- **Context:** Scope discipline.
- **Rule:** Pure functions with no reactive state and no lifecycle needs belong in `utils/`, not `composables/`.
- **Avoid:** `useFormatCurrency(n)` that just wraps `Intl.NumberFormat`.

## 4. Component Design (`cmp-`)

### `cmp-no-prop-mutation`
- **Context:** One-way data flow.
- **Rule:** Props are read-only. Emit an event, use `defineModel`, or copy into local state.
- **Avoid:** `props.items.push(x)` or `props.value = 1`.

### `cmp-declare-emits`
- **Context:** Component contract.
- **Rule:** Declare every emitted event with `defineEmits<T>()`. Undeclared events fall through as native listeners, causing double-firing and silent contract drift.
- **Avoid:** Calling `emit('close')` without declaring `close`.

### `cmp-props-down-events-up`
- **Context:** Data flow.
- **Rule:** Parent owns state and passes it down; child reports intent upward via events. Use this as the default for all component communication.
- **Avoid:** Children reaching into parents, or shared mutable objects passed as props and mutated in place.

### `cmp-define-model-for-two-way`
- **Context:** Two-way binding.
- **Rule:** Use `defineModel<T>()` (Vue 3.4+) for `v-model` contracts instead of manual `modelValue` prop + `update:modelValue` emit.
- **Avoid:** Hand-writing the prop/emit pair, which drifts from `v-model` modifier semantics.

### `cmp-define-model-object-emit`
- **Context:** `defineModel` with objects.
- **Rule:** Mutating a property of an object held in `defineModel` does not emit an update. Assign a new object: `model.value = { ...model.value, name }`.
- **Avoid:** `model.value.name = 'x'` and expecting the parent to be notified.

### `cmp-no-ref-over-props`
- **Context:** Component access.
- **Rule:** Communicate via props/emits. Reach for a component template ref only for genuinely imperative APIs (`focus()`, `play()`, `validate()`).
- **Avoid:** Reading a child's internal state through `childRef.value.someState`.

### `cmp-expose-explicitly`
- **Context:** Imperative API.
- **Rule:** `<script setup>` components are closed by default. Publish an intentional imperative surface with `defineExpose({ focus, reset })` and type it for the parent.
- **Avoid:** Exposing the whole internal state object.

### `cmp-inject-key-typed`
- **Context:** provide/inject.
- **Rule:** Use a typed `InjectionKey<T>` symbol exported from a shared module, so `inject()` infers the type and collisions are impossible.
- **Avoid:** String keys like `inject('user')` typed as `unknown`.

### `cmp-provide-reactive-wrapper`
- **Context:** provide/inject reactivity.
- **Rule:** Provide a ref/computed/reactive object (or a `readonly()` view of one) if consumers must react to changes. Provide mutator functions alongside, and keep mutations in the provider.
- **Avoid:** `provide(key, user.value)` — injects a snapshot.

### `cmp-inject-default-factory`
- **Context:** Inject defaults.
- **Rule:** For object/array defaults, pass a factory and `true` as the third argument: `inject(key, () => ({}), true)`.
- **Avoid:** `inject(key, {})` — every consumer shares one object instance.

### `cmp-inherit-attrs-false-wrappers`
- **Context:** Fallthrough attributes.
- **Rule:** For wrapper components whose root is not the target element, set `inheritAttrs: false` and bind `v-bind="$attrs"` on the intended element.
- **Avoid:** Letting `class`/`id`/listeners land on an outer `<div>` wrapper. Note: in Vue 3, fallthrough `class`/`style` merge, but other attributes overwrite the component's own bindings.

### `cmp-slot-forwarding`
- **Context:** Wrapper components.
- **Rule:** Forward slots explicitly when wrapping a component: `<template v-for="(_, name) in $slots" #[name]="slotProps"><slot :name="name" v-bind="slotProps ?? {}" /></template>`.
- **Avoid:** Wrapper components that silently swallow the wrapped component's slots.

### `cmp-single-responsibility`
- **Context:** Component size.
- **Rule:** Split when a component owns both orchestration/state and substantial markup, has 3+ distinct UI sections, or repeats a template block. Move UI into children, state/effects into composables.
- **Avoid:** A 400-line SFC that fetches, filters, renders a form, a list, and a footer.

### `cmp-thin-route-views`
- **Context:** Route-level components.
- **Rule:** Keep `App.vue` and route views as composition surfaces — layout, provider wiring, feature composition. For CRUD/list features, split into container, form/input, list/item, and filter/status components.
- **Avoid:** Implementing an entire feature inside a route view.

## 5. SFC & Templates (`tpl-`)

### `tpl-stable-key`
- **Context:** List rendering.
- **Rule:** Every `v-for` needs a stable, unique `:key` tied to item identity.
- **Avoid:** `:key="index"` for lists that reorder, filter, or splice — component state binds to the wrong row.

### `tpl-no-vif-with-vfor`
- **Context:** Directive precedence.
- **Rule:** Never use `v-if` and `v-for` on the same element. Filter in a `computed`, or move `v-if` to a wrapping `<template>`.
- **Avoid:** `<li v-for="u in users" v-if="u.active">` — in Vue 3 `v-if` evaluates first and cannot see `u`.

### `tpl-no-side-effects-in-template`
- **Context:** Template purity.
- **Rule:** Template expressions and called functions must be pure. Render-time mutation causes unpredictable re-render loops.
- **Avoid:** `{{ incrementCounter() }}` or a method that pushes to an array while rendering.

### `tpl-no-expensive-expressions`
- **Context:** Template cost.
- **Rule:** Move filtering, sorting, mapping, and formatting into `computed`. Template expressions re-run on every render.
- **Avoid:** `v-for="i in items.filter(x => x.active).sort(fn)"`.

### `tpl-vif-null-check-order`
- **Context:** Null safety.
- **Rule:** Guard with `v-if="user"` on the wrapper, or use optional chaining `user?.profile?.name`. Sibling `v-if` does not protect an expression on the same element.
- **Avoid:** `<span v-if="user">{{ user.profile.name }}</span>` where `profile` may be missing.

### `tpl-v-show-vs-v-if`
- **Context:** Conditional rendering.
- **Rule:** `v-if` for rarely-toggled or expensive subtrees (it unmounts and destroys state); `v-show` for frequent toggles (CSS `display` only). `v-show` does not work on `<template>` and has no `v-else`.
- **Avoid:** `v-if` on a tab panel toggled many times per session, or `v-show` on a heavy subtree that is usually hidden.

### `tpl-use-template-ref`
- **Context:** Template refs (Vue 3.5+).
- **Rule:** Use `const el = useTemplateRef<HTMLInputElement>('input')` — the string is checked against the template and refactors are visible.
- **Avoid:** `const input = ref(null)` matched implicitly by variable name (silently breaks on rename).

### `tpl-template-ref-null-guard`
- **Context:** Ref lifetime.
- **Rule:** Template refs are `null` before mount and after a `v-if` unmounts the element. Always guard with `?.` or check inside `onMounted`/`watch` with `flush: 'post'`.
- **Avoid:** Accessing `el.value.focus()` in setup body or in a `pre`-flush watcher.

### `tpl-pascal-case-components`
- **Context:** Naming.
- **Rule:** Use PascalCase for component filenames and in-template usage (`<UserCard />`). Use multi-word names to avoid clashing with HTML elements.
- **Avoid:** `<user-card>` in SFC templates, or a component named `Item`/`Table`.

### `tpl-no-v-html-untrusted`
- **Context:** XSS.
- **Rule:** Do not use `v-html` for any value that is not sanitized server-side or by a vetted sanitizer (DOMPurify) and provably trusted. Prefer `{{ }}` interpolation or slots.
- **Avoid:** `v-html="comment.body"`.

### `tpl-camel-case-style-bindings`
- **Context:** Style bindings.
- **Rule:** Use camelCase keys in `:style` object bindings (`{ backgroundColor: c }`); kebab-case requires quoting.
- **Avoid:** `{ background-color: c }` — invalid JS.

### `tpl-self-closing-components`
- **Context:** Template style.
- **Rule:** Self-close components with no slot content: `<UserCard :user="u" />`.
- **Avoid:** `<UserCard :user="u"></UserCard>`.

## 6. TypeScript (`ts-`)

### `ts-with-defaults-factory`
- **Context:** Prop defaults.
- **Rule:** Object and array defaults must be factory functions: `withDefaults(defineProps<T>(), { items: () => [] })`. Same applies to reactive props destructure defaults.
- **Avoid:** `{ items: [] }` — one array shared across all instances.

### `ts-no-reactive-generic-arg`
- **Context:** `reactive()` typing.
- **Rule:** Do not pass a type argument to `reactive()`; let it infer, because `reactive` unwraps nested refs and the explicit generic mismatches the actual type.
- **Avoid:** `reactive<State>({ ... })`.

### `ts-template-ref-null-handling`
- **Context:** Ref types.
- **Rule:** Type template refs as `T | null` (`useTemplateRef<HTMLInputElement>('input')` already does) and use non-null assertion only inside `onMounted` where the element is guaranteed.
- **Avoid:** `ref<HTMLInputElement>()` then `el.value.focus()` without a guard.

### `ts-boolean-prop-undefined`
- **Context:** Boolean props.
- **Rule:** Vue casts absent boolean props to `false` by default. If you need tri-state, type it `boolean | undefined` and disable the cast (`defineProps({ flag: { type: Boolean, default: undefined } })`).
- **Avoid:** Assuming `props.flag === undefined` means "not provided" with a plain `flag?: boolean`.

### `ts-event-handler-typing`
- **Context:** DOM events.
- **Rule:** Type handler parameters explicitly and narrow the target: `(e: Event) => { const t = e.target as HTMLInputElement }`. Under `strict`, inline template handlers are `any`-unsafe.
- **Avoid:** `@input="e => value = e.target.value"` with no typing.

### `ts-generic-components`
- **Context:** Reusable components.
- **Rule:** Use `<script setup lang="ts" generic="T">` for components parameterized over item type (lists, selects, tables) so slot props and emits stay typed.
- **Avoid:** `items: any[]` in a generic list component.

### `ts-shallow-ref-dynamic-component`
- **Context:** Dynamic components.
- **Rule:** Hold component definitions in `shallowRef`/`markRaw`, not `ref`/`reactive` — proxying a component definition triggers a Vue warning and wastes work.
- **Avoid:** `const view = ref(SomeComponent)`.

### `ts-vue-tsc-in-ci`
- **Context:** Type checking.
- **Rule:** Run `vue-tsc --noEmit` as a CI gate. `vite build` does not type-check templates.
- **Avoid:** Relying on editor diagnostics alone.

### `ts-defineprops-local-types`
- **Context:** Compiler limitations.
- **Rule:** Prefer types declared in the same file or in a simple imported interface for `defineProps`. Deeply generic, mapped, or conditional imported types can fail SFC compiler resolution.
- **Avoid:** `defineProps<DeepMapped<Api['user']>>()` and then debugging an opaque compile error.

## 7. State Management (`store-`)

### `store-setup-store-style`
- **Context:** Pinia store authoring.
- **Rule:** Use setup stores: `defineStore('id', () => { ... return { ... } })`. They compose with other composables and type better than option stores.
- **Avoid:** Option stores in new code unless the project already standardizes on them.

### `store-return-all-state`
- **Context:** Setup stores.
- **Rule:** Return **every** ref and computed the store owns. Unreturned state is invisible to DevTools, SSR serialization, `$reset`, and plugins.
- **Avoid:** Keeping a "private" ref out of the returned object.

### `store-use-storetorefs`
- **Context:** Store consumption.
- **Rule:** `const { items, total } = storeToRefs(store)` for state and getters; call actions directly (`store.load()`).
- **Avoid:** `const { items } = useCartStore()` — reactivity is lost.

### `store-action-binding`
- **Context:** Template usage.
- **Rule:** Call store actions through the store object (`@click="store.remove(id)"`), or destructure the action (actions are safe to destructure) — but never pass a bare method reference that relies on `this`.
- **Avoid:** Detaching an option-store method from its store and losing context.

### `store-no-module-mutable-state`
- **Context:** SSR safety.
- **Rule:** Do not export mutable module-scope state (`export const user = ref(null)`) in code that runs on a server — it is shared by every request.
- **Avoid:** Module-level singletons for per-user data. Use a store created per request, or `createInjectionState`.

### `store-pinia-instance-per-request`
- **Context:** SSR.
- **Rule:** In SSR, `createPinia()` per request and install it on that request's app instance; serialize `pinia.state.value` into the payload and hydrate on the client.
- **Avoid:** A single shared `pinia` instance across requests.

### `store-url-for-ephemeral-state`
- **Context:** State location.
- **Rule:** Filters, sort order, pagination, and open-tab state that should survive refresh and be shareable belong in the URL query, not a store.
- **Avoid:** A `filtersStore` whose contents are lost on reload and cannot be linked to.

### `store-no-active-pinia-outside-setup`
- **Context:** Store initialization.
- **Rule:** Call `useXStore()` inside setup, a component method, a guard callback, or after `app.use(pinia)`. At module top level, no active Pinia exists yet.
- **Avoid:** `const store = useAuthStore()` at the top of a router or plugin module — throws "getActivePinia was called with no active Pinia".

### `store-colocate-by-domain`
- **Context:** Store granularity.
- **Rule:** One store per domain concept (`auth`, `cart`, `catalog`), not one global store and not one store per component.
- **Avoid:** A `mainStore` that accumulates every piece of app state.

## 8. Routing (`router-`)

### `router-no-next-callback`
- **Context:** Navigation guards.
- **Rule:** Return a value from guards: `return true`, `return false`, or `return { name: 'login' }`. The `next()` callback style is legacy and easy to call twice.
- **Avoid:** Mixing `return` and `next()` in one guard.

### `router-guard-await-async`
- **Context:** Async guards.
- **Rule:** Make the guard `async` and `await` all async work before returning. An unawaited promise lets navigation complete first.
- **Avoid:** `beforeEach((to) => { checkAuth().then(...) ; return true })`.

### `router-no-guard-redirect-loop`
- **Context:** Redirects.
- **Rule:** Always check the destination before redirecting: `if (!auth && to.name !== 'login') return { name: 'login' }`.
- **Avoid:** Unconditional redirects that also match the redirect target.

### `router-watch-params-not-lifecycle`
- **Context:** Route param changes.
- **Rule:** The component is reused when only params change — `onMounted` does not re-run. Use `watch(() => route.params.id, load, { immediate: true })` or `onBeforeRouteUpdate`.
- **Avoid:** Fetching only in `onMounted` for `/user/:id`, leaving stale data on navigation between users.

### `router-beforerouteenter-no-this`
- **Context:** In-component guards.
- **Rule:** `beforeRouteEnter` runs before the component instance exists — there is no `this`/setup scope. Fetch there and pass data through, or fetch in setup after navigation.
- **Avoid:** Accessing component state inside `beforeRouteEnter`.

### `router-lazy-route-components`
- **Context:** Bundle size.
- **Rule:** Define route components as `() => import('../views/Foo.vue')` so each route becomes its own chunk.
- **Avoid:** Static imports of every view in the router file.

### `router-typed-meta`
- **Context:** Route metadata.
- **Rule:** Augment `RouteMeta` in a `.d.ts` (`declare module 'vue-router' { interface RouteMeta { requiresAuth?: boolean } }`) so guards are type-safe.
- **Avoid:** `to.meta.requiresAuth as boolean` casts scattered through guards.

### `router-cleanup-on-unmount`
- **Context:** Leaks.
- **Rule:** Listeners, intervals, and subscriptions registered by a route component must be removed in `onUnmounted` — route navigation unmounts components silently.
- **Avoid:** `window.addEventListener('scroll', ...)` in a view with no teardown.

## 9. Performance (`perf-`)

### `perf-virtualize-large-lists`
- **Context:** Long lists.
- **Rule:** Virtualize beyond a few hundred rows (`vue-virtual-scroller`, `@tanstack/vue-virtual`, VueUse `useVirtualList`). Rendering thousands of DOM nodes is the bottleneck, not Vue.
- **Avoid:** `v-for` over 10,000 items with per-row components.

### `perf-stable-props`
- **Context:** Child updates.
- **Rule:** Pass stable references. Object/array literals and inline arrow functions in templates create a new identity every render and force child updates.
- **Avoid:** `<Row :config="{ dense: true }" @click="() => select(row)" />` inside a hot list.

### `perf-computed-object-stability`
- **Context:** Computed identity.
- **Rule:** A computed returning a new object/array on every evaluation retriggers downstream effects even when the content is equal. Return primitives, memoize, or compare structurally before replacing.
- **Avoid:** `computed(() => ({ ...defaults, ...props.opts }))` feeding a deep watcher.

### `perf-v-memo-hot-lists`
- **Context:** `v-memo`.
- **Rule:** Use `v-memo="[a, b]"` only on measured hot paths — typically large `v-for` rows where most rows are unchanged. Combine with `:key`.
- **Avoid:** Sprinkling `v-memo` preemptively; a wrong dependency array causes stale UI.

### `perf-v-once-static-subtrees`
- **Context:** `v-once`.
- **Rule:** Use `v-once` for genuinely static subtrees rendered many times (headers, legal text in list rows).
- **Avoid:** `v-once` on anything that can change — it will never update.

### `perf-no-abstraction-in-hot-lists`
- **Context:** Component overhead.
- **Rule:** In very hot list paths, inline simple markup instead of creating a component per cell — each component instance carries setup and patch cost.
- **Avoid:** A `<Cell>` component wrapping a single `<span>` inside a 50-column × 1,000-row table.

### `perf-shallow-for-large-data`
- **Context:** Deep reactivity cost.
- **Rule:** Use `shallowRef`/`shallowReactive` for large immutable payloads updated by replacement.
- **Avoid:** `ref(hugeNestedApiResponse)` — Vue walks and proxies the whole tree.

### `perf-lazy-async-components`
- **Context:** Initial load.
- **Rule:** `defineAsyncComponent` for heavy, rarely-used UI (modals, editors, charts). In Vue 3.5+, add a hydration strategy (`hydrateOnVisible()`, `hydrateOnIdle()`) for SSR apps.
- **Avoid:** Bundling a rich text editor into the initial chunk.

### `perf-no-updated-hook-work`
- **Context:** `onUpdated`.
- **Rule:** Keep `onUpdated` free of state mutation and expensive work — it runs after every re-render and mutation there causes infinite update loops.
- **Avoid:** Recomputing layout measurements in `onUpdated`; use a targeted `watch` with `flush: 'post'` or a `ResizeObserver`.

## 10. Architecture (`arch-`)

### `arch-feature-folders`
- **Context:** Project layout.
- **Rule:** Group by feature (`src/features/cart/{components,composables,api,types}`) once a feature has more than one component. Keep truly shared primitives in `src/shared` or `src/components/ui`.
- **Avoid:** A flat `components/` folder with 80 unrelated SFCs.

### `arch-api-layer-isolated`
- **Context:** Data access.
- **Rule:** Put HTTP calls behind a typed API module (`api/users.ts`) that returns domain models. Components and stores call the API layer, never `fetch` directly.
- **Avoid:** `fetch('/api/users')` inline in an SFC.

### `arch-no-store-in-dumb-components`
- **Context:** Reusability.
- **Rule:** Presentational components take props and emit events. Only container/view components read stores or call the API layer.
- **Avoid:** `useCartStore()` inside a generic `<PriceTag>`.

### `arch-typed-domain-models`
- **Context:** Boundaries.
- **Rule:** Define domain types independently of API DTOs and map at the API layer. Validate untrusted payloads (e.g. Zod) at the boundary.
- **Avoid:** Passing raw API response shapes down through the component tree.

### `arch-no-cross-feature-imports`
- **Context:** Coupling.
- **Rule:** Features must not import each other's internals. Share through `shared/`, a store, or explicit public entry points (`features/cart/index.ts`).
- **Avoid:** `import { useCartRow } from '../../cart/composables/useCartRow'` from inside the checkout feature.

### `arch-env-config-centralized`
- **Context:** Configuration.
- **Rule:** Read `import.meta.env` once in a typed `config.ts` and import from there. Type env vars via `vite-env.d.ts` `ImportMetaEnv`.
- **Avoid:** `import.meta.env.VITE_API_URL` scattered across 30 files.

## 11. Built-in Components (`builtin-`)

### `builtin-transition-single-element`
- **Context:** `<Transition>`.
- **Rule:** `<Transition>` accepts exactly one element/component child. For a swap between two elements, give each a unique `:key` and use `mode="out-in"`.
- **Avoid:** Multiple sibling roots inside `<Transition>` — no animation runs.

### `builtin-transition-js-done-callback`
- **Context:** JS transition hooks.
- **Rule:** When using JavaScript hooks, call `done()` in `enter`/`leave` and set `:css="false"`, otherwise the transition hangs or ends early.
- **Avoid:** `@enter="el => animate(el)"` with no `done`.

### `builtin-transition-group-key`
- **Context:** `<TransitionGroup>`.
- **Rule:** Every child needs a stable `:key`, and the move transition needs a `.<name>-move` class. `<TransitionGroup>` renders no wrapper element by default in Vue 3 — pass `tag="ul"` if you need one.
- **Avoid:** Index keys, or assuming a `<span>` wrapper like Vue 2.

### `builtin-teleport-target-exists`
- **Context:** `<Teleport>`.
- **Rule:** The `to` target must exist in the DOM when the Teleport mounts. Use `disabled` or `defer` (Vue 3.5+) when the target is rendered by the same app.
- **Avoid:** `to="#modal-root"` when `#modal-root` is created later in the same render pass.

### `builtin-suspense-error-boundary`
- **Context:** `<Suspense>`.
- **Rule:** `<Suspense>` has no built-in error handling. Pair it with `onErrorCaptured` in a parent (or `app.config.errorHandler`) to surface failed async setup.
- **Avoid:** An async component that rejects and leaves the fallback rendered forever.

### `builtin-keepalive-include-by-name`
- **Context:** `<KeepAlive>`.
- **Rule:** Use `:include`/`:exclude`/`:max` and give cached components a resolvable name (`defineOptions({ name: 'UserList' })`). Use `onActivated`/`onDeactivated` for resume/pause logic.
- **Avoid:** Wrapping the whole router view in `<KeepAlive>` with no `:max` — unbounded memory growth, especially combined with `<Transition>`.

### `builtin-async-component-error-ui`
- **Context:** `defineAsyncComponent`.
- **Rule:** Supply `errorComponent`, `loadingComponent`, `delay`, and `timeout` for network-loaded components. Note that under `<Suspense>`, the async component's own loading/error UI is bypassed.
- **Avoid:** A blank screen when a chunk fails to load on a flaky connection.

## 12. Forms (`form-`)

### `form-v-model-over-value-input`
- **Context:** Form bindings.
- **Rule:** Use `v-model` on native inputs; it handles the correct event per input type (`input`, `change`, `checked`, multi-select).
- **Avoid:** Hand-wiring `:value` + `@input` unless you need custom transformation.

### `form-no-html-value-attribute`
- **Context:** Initial values.
- **Rule:** `v-model` ignores `value`, `checked`, and `selected` attributes in the template. Set the initial value in the reactive state.
- **Avoid:** `<input v-model="name" value="Ada">` and expecting "Ada" to show.

### `form-number-modifier-guard`
- **Context:** `v-model.number`.
- **Rule:** `.number` yields the original string when parsing fails, and an empty input yields `''` — not `0`. Validate and coerce explicitly before arithmetic.
- **Avoid:** `total = qty * price` where `qty` is `''`.

### `form-ime-composition-aware`
- **Context:** IME input.
- **Rule:** `v-model` does not update during IME composition (Chinese/Japanese/Korean). For live search/validation, listen to `input` directly or handle `compositionstart`/`compositionend`.
- **Avoid:** Debounced search bound only to `v-model` and appearing broken for CJK users.

### `form-checkbox-true-false-value`
- **Context:** Checkboxes.
- **Rule:** `true-value`/`false-value` are Vue-only bindings and are not submitted by a native form POST. Submit via JS, or use a hidden input for native submissions.
- **Avoid:** Relying on `true-value="yes"` to reach a server-side form handler.

### `form-label-association`
- **Context:** Accessibility.
- **Rule:** Associate every control with a `<label for>` (use `useId()` for the id) or wrap the input in the label. Surface validation errors via `aria-describedby` and `aria-invalid`.
- **Avoid:** Placeholder-only labels.

## 13. Styling (`css-`)

### `css-scoped-by-default`
- **Context:** Style isolation.
- **Rule:** Use `<style scoped>` in components by default. Put global resets and tokens in one global stylesheet.
- **Avoid:** Unscoped component styles that leak selectors app-wide.

### `css-class-selectors-in-scoped`
- **Context:** Scoped CSS performance.
- **Rule:** Prefer class selectors in scoped styles. Element selectors combined with attribute scoping are markedly slower.
- **Avoid:** `div span a { }` inside `<style scoped>`.

### `css-deep-selector-explicit`
- **Context:** Child component styling.
- **Rule:** Scoped styles do not reach a child component's internals. Use `:deep(.child-class)` deliberately, or better, expose a prop/CSS variable from the child.
- **Avoid:** Broad `:deep(*)` rules that recreate global leakage.

### `css-modules-for-shared`
- **Context:** CSS Modules.
- **Rule:** Use `<style module>` when you need class names as JS values (dynamic composition, conditional class maps).
- **Avoid:** String-concatenating scoped class names in script.

### `css-v-bind-for-dynamic`
- **Context:** Reactive styles.
- **Rule:** Use `v-bind()` in `<style>` for reactive CSS values (`color: v-bind(themeColor)`) — it compiles to CSS custom properties.
- **Avoid:** Large inline `:style` objects recomputed on every render.

### `css-no-dynamic-tailwind-classes`
- **Context:** Tailwind.
- **Rule:** Tailwind scans source statically. Write full class names and select between them; do not build them by concatenation.
- **Avoid:** `` :class="`text-${color}-500`" `` — the class is never generated. Use a lookup map of complete class strings.

## 14. SSR (`ssr-`)

### `ssr-no-cross-request-state`
- **Context:** State isolation.
- **Rule:** All app state must be created per request (app factory, Pinia per request). Module-scope refs are shared across every user.
- **Avoid:** `export const currentUser = ref(null)` in an SSR app.

### `ssr-guard-browser-apis`
- **Context:** Universal code.
- **Rule:** Access `window`, `document`, `localStorage`, `navigator`, and `IntersectionObserver` only inside `onMounted` or behind an `import.meta.env.SSR` / `typeof window !== 'undefined'` guard.
- **Avoid:** Reading `localStorage` at module scope or in `setup()`.

### `ssr-deterministic-render`
- **Context:** Hydration.
- **Rule:** Server and client must produce identical markup. Avoid `Date.now()`, `Math.random()`, locale/timezone-dependent formatting, and invalid HTML nesting (`<div>` inside `<p>`) in SSR output.
- **Avoid:** Rendering "3 minutes ago" during SSR; render an absolute timestamp and localize after mount.

### `ssr-client-only-for-nondeterministic`
- **Context:** Escape hatches.
- **Rule:** Wrap genuinely client-only widgets in `<ClientOnly>` (Nuxt) or render them after mount. For known-acceptable text differences, use `data-allow-mismatch` (Vue 3.5+) narrowly.
- **Avoid:** Suppressing hydration warnings globally instead of fixing determinism.

### `ssr-teleport-target-ssr-safe`
- **Context:** Teleport + SSR.
- **Rule:** Teleported content is serialized separately; the target must exist in the server-rendered HTML or the Teleport must be client-only.
- **Avoid:** Teleporting to `document.body` during SSR without handling the hydration path.

## 15. Security & Accessibility (`sec-`, `a11y-`)

### `sec-no-untrusted-v-html`
- **Context:** XSS.
- **Rule:** Never bind user-controlled content to `v-html`. If rich content is required, sanitize with a vetted library and constrain the allowed tag/attribute set.
- **Avoid:** `v-html="markdownRenderedUserInput"` with no sanitizer.

### `sec-no-dynamic-component-from-input`
- **Context:** Dynamic rendering.
- **Rule:** Resolve `<component :is>` targets from a fixed allow-list map. Never let user input select an arbitrary component or HTML tag.
- **Avoid:** `<component :is="route.query.widget" />`.

### `sec-no-secrets-in-client-env`
- **Context:** Configuration.
- **Rule:** Anything reachable from `import.meta.env` in client code ships in the bundle. Keep API secrets server-side; use a backend proxy.
- **Avoid:** `VITE_STRIPE_SECRET_KEY`.

### `a11y-semantic-elements`
- **Context:** Markup.
- **Rule:** Use `<button>`, `<a href>`, `<nav>`, `<main>`, and real headings. Interactive elements must be keyboard-reachable and have an accessible name.
- **Avoid:** `<div @click="...">` acting as a button.

### `a11y-focus-management`
- **Context:** Overlays and routing.
- **Rule:** Move focus into modals/drawers on open, trap it while open, restore it on close, and move focus to the main heading on route change.
- **Avoid:** Modals that leave focus behind the overlay.

### `a11y-aria-live-for-async`
- **Context:** Async feedback.
- **Rule:** Announce loading, success, and error state changes through an `aria-live="polite"` (or `assertive` for errors) region.
- **Avoid:** Spinners and toasts that are invisible to screen readers.
