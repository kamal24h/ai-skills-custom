---
name: vuejs-tester
description: Vue 3 testing patterns — Vitest, Vue Test Utils, Testing Library, component/composable/store/router testing, mocking with MSW, browser mode, Playwright E2E, and coverage. Use when authoring, refactoring, or debugging Vue tests. Triggers on "Vue test", "Vitest", "Vue Test Utils", "mount", "shallowMount", "flushPromises", "createTestingPinia", "Playwright", "component test", "test composable".
model: inherit
---

# Vue.js Testing Best Practices

Modern testing for Vue 3 applications — Vitest, Vue Test Utils, Testing Library, MSW, Vitest Browser Mode, and Playwright. Focused on tests that survive refactors, never flake, and fail for the right reason.

## Specialized Agents

| Agent | Role | Focus |
|-------|------|-------|
| **vue-tester-pro** | Test Expert | Vitest, VTU, Testing Library, composables, Pinia, router, MSW, Playwright, coverage. |

## When to Use

Reference these guidelines when:
- Setting up a Vitest + Vue Test Utils environment
- Writing component tests that assert behavior instead of internals
- Testing composables that use lifecycle hooks, `inject`, or effects
- Testing Pinia stores and components that consume them
- Testing router-dependent components and navigation guards
- Mocking HTTP with MSW, or modules with `vi.mock`
- Testing async components, `<Suspense>`, and `<Teleport>`
- Deciding between jsdom, Vitest Browser Mode, and Playwright
- Setting up coverage thresholds and CI test pipelines
- Diagnosing flaky or intermittently failing Vue tests
- Following a TDD (RED/GREEN/REFACTOR) workflow

## Step 1: Choose the Test Surface

| Question | Runner |
|---|---|
| Pure logic, composables, stores, utils | **Vitest** (node environment) |
| Component behavior, props/emits/slots, user interaction | **Vitest + jsdom + VTU / Testing Library** |
| Real layout, computed styles, native events, focus, scroll | **Vitest Browser Mode** (Playwright provider) |
| Full user journeys across pages, real backend or MSW | **Playwright** |

Default to jsdom component tests. Escalate to Browser Mode only when jsdom cannot express the assertion (measured sizes, CSS-driven visibility, real pointer/focus behavior).

## Step 2: Choose the Guidance Set

- Load `references/vitest-setup.md` before configuring or fixing the test environment.
- Load `references/component-testing.md` before writing or reviewing component tests.
- Load `references/async-testing.md` when a test involves promises, timers, or `nextTick`.
- Load `references/composables-testing.md` before testing a `useXxx()` function.
- Load `references/pinia-testing.md` before testing a store or a store-consuming component.
- Load `references/router-testing.md` before testing route components or guards.
- Load `references/mocking.md` before mocking HTTP, modules, or child components.
- Load `references/browser-mode.md` when jsdom cannot express the assertion.
- Load `references/e2e-playwright.md` for cross-page user journeys.
- Load `references/coverage.md` when configuring coverage or thresholds.
- Load `references/tdd-workflow.md` when driving new code from tests.
- Load `references/ci-testing.md` when wiring tests into a pipeline.
- Load the `vuejs` skill for the implementation patterns these tests target.

## Core Directives

### MUST DO

- **Runner:** Use Vitest for unit and component tests. It shares the Vite config, so aliases, plugins, and env vars match production.
- **Black box:** Test the public contract — rendered output, emitted events, and observable side effects. Not internal refs, methods, or `wrapper.vm`.
- **Naming:** `describe('ComponentName')` + `it('emits submit with the form values when the form is submitted')`. Describe the behavior, not the method.
- **Structure:** Arrange / Act / Assert, visually separated in every test.
- **Queries:** Query by accessible role, label, or text (Testing Library), or by `data-testid`. Never by CSS class or DOM position.
- **Async:** `await` every interaction and use `flushPromises()` after promise-based work. Vue's DOM updates are asynchronous.
- **Isolation:** Fresh mounts, fresh stores, fresh mocks per test. `restoreMocks: true` in the Vitest config.
- **HTTP:** Intercept at the network boundary with MSW so the real client code (headers, error mapping, retries) runs.
- **Pinia:** `createTestingPinia()` for components; a real `createPinia()` + `setActivePinia()` for store unit tests.
- **Composables:** Wrap lifecycle-dependent composables in a host component or a `withSetup()` helper.
- **Errors:** Test error paths, empty states, and boundaries — not just the happy path.
- **Cleanup:** Unmount, reset timers, and reset handlers in `afterEach`.

### MUST NOT DO

- **Snapshot-only tests:** Never let a snapshot be a component's only test — it passes while the feature is broken.
- **`wrapper.vm` assertions:** Never assert on internal state or call internal methods.
- **`setTimeout` waits:** Never `await new Promise(r => setTimeout(r, 100))` to "let things settle".
- **Real network:** Never hit a live API from a unit or component test.
- **Class/position selectors:** Never `find('.btn-primary')` or `findAll('div')[2]`.
- **Shallow by default:** Never reach for `shallowMount` reflexively — it stubs the children whose integration you are trying to verify.
- **Shared mutable state:** No module-level state carried between tests.
- **Order dependence:** Never rely on tests running in declaration order.
- **Mocking what you own:** Do not mock your own composables/stores when the real thing works — mock the network boundary instead.
- **Testing the framework:** Do not assert that `v-if` hides an element or that Vue reactivity works.

## Category Index — When to Load Which Reference

| # | Category | Impact | Load when… | Reference |
|--:|----------|:------:|------------|-----------|
| 1 | Vitest Setup | CRITICAL | Config, environment, aliases, globals, setup files | [`references/vitest-setup.md`](references/vitest-setup.md) |
| 2 | Component Testing | CRITICAL | mount, props/emits/slots, queries, interactions | [`references/component-testing.md`](references/component-testing.md) |
| 3 | Async Testing | CRITICAL | nextTick, flushPromises, fake timers, Suspense | [`references/async-testing.md`](references/async-testing.md) |
| 4 | Composables Testing | HIGH | withSetup helper, lifecycle, inject, effect scope | [`references/composables-testing.md`](references/composables-testing.md) |
| 5 | Pinia Testing | HIGH | createTestingPinia, store units, actions, getters | [`references/pinia-testing.md`](references/pinia-testing.md) |
| 6 | Router Testing | HIGH | Route components, guards, memory history | [`references/router-testing.md`](references/router-testing.md) |
| 7 | Mocking | CRITICAL | MSW, vi.mock, stubs, global mocks, timers | [`references/mocking.md`](references/mocking.md) |
| 8 | Browser Mode | MEDIUM | Real layout, styles, focus, pointer events | [`references/browser-mode.md`](references/browser-mode.md) |
| 9 | E2E (Playwright) | HIGH | User journeys, auth flows, cross-page state | [`references/e2e-playwright.md`](references/e2e-playwright.md) |
| 10 | Coverage | MEDIUM | v8/istanbul config, thresholds, exclusions | [`references/coverage.md`](references/coverage.md) |
| 11 | TDD Workflow | HIGH | RED/GREEN/REFACTOR for Vue features | [`references/tdd-workflow.md`](references/tdd-workflow.md) |
| 12 | CI Testing | MEDIUM | Pipelines, sharding, artifacts, flake control | [`references/ci-testing.md`](references/ci-testing.md) |

## Rule Index

### 1. Core Testing (`test-`) — CRITICAL
`test-behavior-names` · `test-arrange-act-assert` · `test-blackbox-contract` · `test-no-vm-assertions` · `test-no-snapshot-only` · `test-fresh-mount-per-test` · `test-no-shared-state` · `test-no-order-dependence` · `test-error-paths` · `test-no-framework-testing` · `test-one-behavior-per-test` · `test-descriptive-failure`

### 2. Queries & Interaction (`query-`) — CRITICAL
`query-by-role-or-label` · `query-testid-fallback` · `query-no-class-selectors` · `query-no-index-selection` · `query-await-interactions` · `query-user-event-over-trigger` · `query-assert-visible-text`

### 3. Async (`async-`) — CRITICAL
`async-flush-promises` · `async-await-next-tick` · `async-no-arbitrary-sleep` · `async-fake-timers-cleanup` · `async-suspense-wrapper` · `async-vi-wait-for` · `async-unhandled-rejection-fails`

### 4. Mounting (`mount-`) — HIGH
`mount-over-shallow` · `mount-stub-heavy-children-only` · `mount-global-plugins-per-test` · `mount-attach-to-document-for-focus` · `mount-teleport-stub-or-target` · `mount-unmount-in-cleanup`

### 5. Composables (`ctest-`) — HIGH
`ctest-with-setup-helper` · `ctest-plain-call-when-no-lifecycle` · `ctest-effect-scope-dispose` · `ctest-assert-returned-refs` · `ctest-provide-in-host`

### 6. Stores (`store-test-`) — HIGH
`store-test-set-active-pinia` · `store-test-testing-pinia-for-components` · `store-test-real-actions-by-default` · `store-test-initial-state-per-test` · `store-test-no-store-internals`

### 7. Mocking (`mock-`) — CRITICAL
`mock-msw-for-http` · `mock-no-live-network` · `mock-boundary-not-internals` · `mock-vi-mock-hoisted` · `mock-restore-between-tests` · `mock-typed-mocks` · `mock-reset-msw-handlers`

### 8. E2E (`e2e-`) — HIGH
`e2e-user-visible-selectors` · `e2e-web-first-assertions` · `e2e-no-hard-waits` · `e2e-independent-tests` · `e2e-auth-via-storage-state` · `e2e-critical-paths-only` · `e2e-trace-on-retry`

### 9. Coverage & CI (`cov-`, `ci-`) — MEDIUM
`cov-threshold-enforcement` · `cov-exclude-generated` · `cov-behavior-over-percentage` · `ci-fail-on-flake` · `ci-shard-large-suites` · `ci-upload-artifacts`

## Validation Checklist

- [ ] Test names describe observable behavior, not method names
- [ ] Arrange / Act / Assert visually separated
- [ ] Assertions target rendered output, emitted events, or side effects — never `wrapper.vm`
- [ ] No snapshot-only test files
- [ ] Elements queried by role/label/text or `data-testid`, never by class or index
- [ ] Every interaction and promise-based step is `await`ed (`flushPromises()` where needed)
- [ ] No arbitrary `setTimeout` waits anywhere
- [ ] Fake timers restored in `afterEach`
- [ ] Fresh mount, fresh store, and fresh mocks per test
- [ ] HTTP intercepted with MSW; handlers reset between tests
- [ ] No live network calls in unit or component tests
- [ ] `createTestingPinia()` used for component tests; real Pinia for store unit tests
- [ ] Composables with lifecycle hooks tested through a host component or `withSetup()`
- [ ] Error paths, empty states, and boundary values covered
- [ ] `mount` used by default; `shallowMount`/stubs justified case by case
- [ ] Async components tested inside `<Suspense>` or with `flushPromises()`
- [ ] Coverage thresholds enforced in CI
- [ ] E2E limited to critical user journeys, with web-first assertions and no hard waits

## External References

- [Vue Testing Guide](https://vuejs.org/guide/scaling-up/testing.html)
- [Vue Test Utils](https://test-utils.vuejs.org/)
- [Vitest](https://vitest.dev/)
- [Vitest Browser Mode](https://vitest.dev/guide/browser/)
- [Testing Library — Vue](https://testing-library.com/docs/vue-testing-library/intro/)
- [Playwright](https://playwright.dev/)
- [MSW](https://mswjs.io/)
- [Pinia Testing](https://pinia.vuejs.org/cookbook/testing.html)
- [Vue Router Testing](https://router.vuejs.org/guide/advanced/testing.html)
