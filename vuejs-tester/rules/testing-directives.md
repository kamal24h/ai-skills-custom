# Rules for Vue 3 Testing

Actionable directives for authoring, reviewing, and debugging Vue tests with Vitest, Vue Test Utils, MSW, and Playwright.

## 1. Core Testing Rules (`test-`)

### `test-behavior-names`
- **Context:** Test naming.
- **Rule:** `describe('<Unit>')` + `it('<observable behavior> when <trigger>')`. The name must be readable as a sentence describing what a user or caller observes.
- **Avoid:** `it('test handleSubmit')`, `it('works')`, `it('renders correctly')`.

### `test-arrange-act-assert`
- **Context:** Test structure.
- **Rule:** Every test has visually separated Arrange, Act, and Assert sections (blank lines, optionally comments).
- **Avoid:** A flat block where setup, interaction, and assertions are interleaved.

### `test-blackbox-contract`
- **Context:** What to assert.
- **Rule:** Assert on rendered output, emitted events, and observable side effects (HTTP calls, storage writes, navigation). These are the contract.
- **Avoid:** Asserting on internal refs, computed values, or private methods.

### `test-no-vm-assertions`
- **Context:** Implementation coupling.
- **Rule:** Never read or write `wrapper.vm.*` in an assertion or as a way to trigger behavior. Interact through the DOM.
- **Avoid:** `expect(wrapper.vm.isOpen).toBe(true)`, `wrapper.vm.submit()`.

### `test-no-snapshot-only`
- **Context:** Snapshot testing.
- **Rule:** A snapshot may supplement behavioral assertions; it must never be the only test for a component. Snapshots pass while functionality is broken and get blindly `-u`'d.
- **Avoid:** A test file containing only `expect(wrapper.html()).toMatchSnapshot()`.

### `test-fresh-mount-per-test`
- **Context:** Isolation.
- **Rule:** Mount the component inside each test (or in `beforeEach`), never once at module scope. Use a `renderComponent(overrides)` factory for shared setup.
- **Avoid:** `const wrapper = mount(Comp)` at the top of the file, shared by every test.

### `test-no-shared-state`
- **Context:** Isolation.
- **Rule:** No module-level mutable state between tests. Reset stores, mocks, timers, and MSW handlers in `afterEach`.
- **Avoid:** `let items = []` at file scope, mutated by several tests.

### `test-no-order-dependence`
- **Context:** Determinism.
- **Rule:** Every test must pass in isolation and in any order. Verify with `vitest --sequence.shuffle`.
- **Avoid:** A test that relies on data created by an earlier test.

### `test-error-paths`
- **Context:** Coverage completeness.
- **Rule:** Cover failure responses, validation errors, empty lists, and boundary values alongside the happy path.
- **Avoid:** Only asserting the 200-response case.

### `test-no-framework-testing`
- **Context:** Test value.
- **Rule:** Test your logic, not Vue's. Reactivity, `v-if`, and `v-for` are the framework's responsibility.
- **Avoid:** `it('hides the element when show is false')` on a bare `v-if`.

### `test-one-behavior-per-test`
- **Context:** Diagnosability.
- **Rule:** One behavior per `it`. Multiple `expect`s are fine when they describe the same behavior.
- **Avoid:** A 60-line test asserting loading, success, error, and navigation at once.

### `test-descriptive-failure`
- **Context:** Debuggability.
- **Rule:** Assertions should fail with a message that identifies the problem. Prefer `toHaveTextContent`/`toBeVisible` over `toBe(true)` on a derived boolean.
- **Avoid:** `expect(found).toBe(true)` — the failure says nothing.

## 2. Queries & Interaction (`query-`)

### `query-by-role-or-label`
- **Context:** Element lookup.
- **Rule:** Prefer accessible queries: `getByRole('button', { name: 'Save' })`, `getByLabelText('Email')`, `getByText(...)`. They assert accessibility as a side effect.
- **Avoid:** Structural selectors that pass even when the element is unreachable to users.

### `query-testid-fallback`
- **Context:** Non-semantic elements.
- **Rule:** When no accessible query fits, use `data-testid`. Treat the attribute as part of the component's contract.
- **Avoid:** Removing `data-testid` in a "cleanup" refactor without updating tests.

### `query-no-class-selectors`
- **Context:** Selector stability.
- **Rule:** Never select by CSS class — classes are styling, and they change with restyles and Tailwind refactors.
- **Avoid:** `wrapper.find('.btn-primary')`.

### `query-no-index-selection`
- **Context:** Selector stability.
- **Rule:** Never select by position.
- **Avoid:** `wrapper.findAll('div')[2]`, `rows.at(0)`, `nth-child` selectors.

### `query-await-interactions`
- **Context:** Async DOM.
- **Rule:** `await` every `trigger`/`setValue`/`userEvent` call. Vue applies DOM updates asynchronously.
- **Avoid:** `wrapper.find('button').trigger('click')` without `await`, then asserting.

### `query-user-event-over-trigger`
- **Context:** Fidelity.
- **Rule:** Prefer Testing Library's `userEvent` (or Browser Mode's `userEvent`) for typing, clicking, and tabbing — it fires the full realistic event sequence including focus and keyboard events.
- **Avoid:** `trigger('click')` when the behavior under test depends on focus, hover, or key sequences.

### `query-assert-visible-text`
- **Context:** Assertion target.
- **Rule:** Assert on what the user sees: visible text, accessible names, ARIA state.
- **Avoid:** Asserting on raw HTML strings or attribute soup.

## 3. Async (`async-`)

### `async-flush-promises`
- **Context:** Promise-based updates.
- **Rule:** After code that awaits promises (fetch, dynamic import, async setup), call `await flushPromises()` before asserting.
- **Avoid:** A single `await nextTick()` after a network call — one microtask tick is usually not enough.

### `async-await-next-tick`
- **Context:** DOM updates.
- **Rule:** After a purely synchronous state change, `await nextTick()` (or `await wrapper.vm.$nextTick()`) before reading the DOM.
- **Avoid:** Asserting on the DOM in the same tick as the state change.

### `async-no-arbitrary-sleep`
- **Context:** Determinism.
- **Rule:** Never wait a fixed duration. Use `flushPromises()`, `vi.waitFor(...)`, `findBy*` queries, or fake timers with explicit advancement.
- **Avoid:** `await new Promise(r => setTimeout(r, 100))`.

### `async-fake-timers-cleanup`
- **Context:** Timer isolation.
- **Rule:** `vi.useFakeTimers()` in `beforeEach` and `vi.useRealTimers()` in `afterEach`. Advance explicitly with `vi.advanceTimersByTimeAsync()`.
- **Avoid:** Leaking fake timers into subsequent tests — they hang or fail mysteriously.

### `async-suspense-wrapper`
- **Context:** Async setup components.
- **Rule:** Components with top-level `await` must be mounted inside a `<Suspense>` wrapper, then resolved with `flushPromises()`.
- **Avoid:** Mounting an async-setup component directly and asserting on empty output.

### `async-vi-wait-for`
- **Context:** Eventual conditions.
- **Rule:** Use `await vi.waitFor(() => expect(...).toBe(...))` for conditions that become true after an unknown number of ticks.
- **Avoid:** Chaining several `flushPromises()` calls hoping one is enough.

### `async-unhandled-rejection-fails`
- **Context:** Silent failures.
- **Rule:** Configure the suite so unhandled rejections and `console.error` from Vue warnings fail the test.
- **Avoid:** Tests that pass while logging "Unhandled error during execution".

## 4. Mounting (`mount-`)

### `mount-over-shallow`
- **Context:** Mount strategy.
- **Rule:** Default to `mount`. Full rendering catches integration bugs between parent and child.
- **Avoid:** Reflexive `shallowMount`, which stubs exactly the interactions under test.

### `mount-stub-heavy-children-only`
- **Context:** Stubbing.
- **Rule:** Stub a child only when it is genuinely heavy (maps, charts, editors) or irrelevant, and state the reason. Use `global.stubs: { HeavyChart: true }`.
- **Avoid:** Stubbing everything by default.

### `mount-global-plugins-per-test`
- **Context:** Plugin wiring.
- **Rule:** Install router/Pinia/i18n through `global.plugins` **per mount**, from a fresh instance each time.
- **Avoid:** A shared plugin instance carrying state between tests.

### `mount-attach-to-document-for-focus`
- **Context:** Focus and layout.
- **Rule:** For focus, `document.activeElement`, or scroll assertions, mount with `attachTo: document.body` and unmount in `afterEach`.
- **Avoid:** Focus assertions on a detached tree — they silently never match.

### `mount-teleport-stub-or-target`
- **Context:** Teleport.
- **Rule:** Teleported content is not inside `wrapper`. Either create the target element in the test DOM and query `document.body`, or stub the Teleport (`global.stubs: { teleport: true }`).
- **Avoid:** `wrapper.find('.modal')` for teleported content and concluding the modal is broken.

### `mount-unmount-in-cleanup`
- **Context:** Leak prevention.
- **Rule:** `wrapper.unmount()` in `afterEach` (Testing Library's `cleanup` does this automatically) so global listeners and timers are released.
- **Avoid:** Accumulating mounted components across a suite.

## 5. Composables (`ctest-`)

### `ctest-with-setup-helper`
- **Context:** Lifecycle-bound composables.
- **Rule:** Composables using lifecycle hooks, `inject`, or `getCurrentInstance` must run inside a component context — use a `withSetup()` helper or a minimal host component.
- **Avoid:** Calling them directly and getting "must be called inside setup" warnings or silently dead hooks.

### `ctest-plain-call-when-no-lifecycle`
- **Context:** Pure composables.
- **Rule:** A composable that only creates refs/computeds can be called directly in a test — no host needed.
- **Avoid:** Ceremony for composables that do not need it.

### `ctest-effect-scope-dispose`
- **Context:** Cleanup verification.
- **Rule:** Run the composable inside an `effectScope`, call `scope.stop()`, and assert that listeners/timers/observers were released.
- **Avoid:** Never testing teardown — leaks are the most common composable bug.

### `ctest-assert-returned-refs`
- **Context:** Contract.
- **Rule:** Assert on the returned refs' `.value` and on observable side effects, after `await nextTick()` where reactivity is involved.
- **Avoid:** Reaching into the composable's closure via mocks.

### `ctest-provide-in-host`
- **Context:** Injection.
- **Rule:** Supply injected dependencies through the host component's `provide` (or `global.provide` on the mount), keyed by the real `InjectionKey`.
- **Avoid:** Module-mocking the provider to work around missing injection.

## 6. Stores (`store-test-`)

### `store-test-set-active-pinia`
- **Context:** Store unit tests.
- **Rule:** `setActivePinia(createPinia())` in `beforeEach`, then use the store directly.
- **Avoid:** "getActivePinia was called with no active Pinia" from a missing setup.

### `store-test-testing-pinia-for-components`
- **Context:** Component tests.
- **Rule:** Use `createTestingPinia({ initialState })` in `global.plugins` so state is seeded and actions are spied.
- **Avoid:** Hand-mocking the store module with `vi.mock`.

### `store-test-real-actions-by-default`
- **Context:** Fidelity.
- **Rule:** Pass `stubActions: false` when the test depends on what the action actually does; mock the network beneath it with MSW instead.
- **Avoid:** Stubbed actions plus assertions about resulting state — the state never changes.

### `store-test-initial-state-per-test`
- **Context:** Isolation.
- **Rule:** Seed state through `initialState` per mount, not by mutating a shared store between tests.
- **Avoid:** `store.items = [...]` leaking into the next test.

### `store-test-no-store-internals`
- **Context:** Contract.
- **Rule:** Assert on getters and on what the component renders; treat unreturned internals as nonexistent.
- **Avoid:** Reaching into `store.$state` for values the component never exposes.

## 7. Mocking (`mock-`)

### `mock-msw-for-http`
- **Context:** HTTP.
- **Rule:** Intercept at the network boundary with MSW so the real client code (headers, status handling, error mapping, retries) executes.
- **Avoid:** `vi.mock('@/lib/http')`, which skips the code most likely to be wrong.

### `mock-no-live-network`
- **Context:** Determinism.
- **Rule:** No unit or component test may reach a real server. Configure MSW with `onUnhandledRequest: 'error'`.
- **Avoid:** Tests that pass locally and fail in CI because of network access.

### `mock-boundary-not-internals`
- **Context:** Mock placement.
- **Rule:** Mock what you do not own: network, `Date`, `crypto`, browser APIs, third-party SDKs. Use the real thing for your own composables and stores.
- **Avoid:** Mocking `useCart()` in a test whose purpose is verifying cart behavior.

### `mock-vi-mock-hoisted`
- **Context:** `vi.mock` semantics.
- **Rule:** `vi.mock` is hoisted above imports. Reference outer variables only through `vi.hoisted()`.
- **Avoid:** "Cannot access before initialization" from referencing a top-level `const` inside the factory.

### `mock-restore-between-tests`
- **Context:** Isolation.
- **Rule:** Set `restoreMocks: true` (or call `vi.restoreAllMocks()` in `afterEach`) so spies and implementations do not leak.
- **Avoid:** A mocked return value from test 1 silently satisfying test 5.

### `mock-typed-mocks`
- **Context:** Type safety.
- **Rule:** Use `vi.mocked(fn)` / `Mock<typeof fn>` so mock signatures track the real ones.
- **Avoid:** `as any` casts that let a mock drift from its real signature.

### `mock-reset-msw-handlers`
- **Context:** Handler leakage.
- **Rule:** `server.resetHandlers()` in `afterEach`; use `server.use(...)` for per-test overrides.
- **Avoid:** An error-response override from one test breaking the next.

## 8. E2E (`e2e-`)

### `e2e-user-visible-selectors`
- **Context:** Selector stability.
- **Rule:** `getByRole`, `getByLabel`, `getByText`, or `getByTestId`. Never CSS or XPath structure.
- **Avoid:** `page.locator('div > .card:nth-child(2) button')`.

### `e2e-web-first-assertions`
- **Context:** Auto-waiting.
- **Rule:** Use `await expect(locator).toBeVisible()` / `toHaveText()` — Playwright retries these until timeout.
- **Avoid:** `expect(await locator.textContent()).toBe('x')`, which samples once.

### `e2e-no-hard-waits`
- **Context:** Flake.
- **Rule:** Never `page.waitForTimeout()`. Wait for a state: a visible element, a response, a URL.
- **Avoid:** Fixed sleeps to "let the animation finish".

### `e2e-independent-tests`
- **Context:** Parallelism.
- **Rule:** Each test creates its own data and can run in isolation and in parallel.
- **Avoid:** Test B depending on the record created by test A.

### `e2e-auth-via-storage-state`
- **Context:** Speed.
- **Rule:** Log in once in a setup project, save `storageState`, and reuse it. Test the login flow itself in exactly one test.
- **Avoid:** UI login in `beforeEach` of every spec.

### `e2e-critical-paths-only`
- **Context:** Suite economics.
- **Rule:** E2E covers a small number of high-value journeys (signup, checkout, primary CRUD). Everything cheaper belongs in component tests.
- **Avoid:** Field-level validation coverage in E2E.

### `e2e-trace-on-retry`
- **Context:** Diagnosability.
- **Rule:** Enable `trace: 'on-first-retry'`, screenshots on failure, and video retention on failure; upload as CI artifacts.
- **Avoid:** A red CI run with no evidence of what happened.

## 9. Coverage & CI (`cov-`, `ci-`)

### `cov-threshold-enforcement`
- **Context:** Regression guard.
- **Rule:** Enforce thresholds in the Vitest config (e.g. 80% lines/functions, 70% branches) so coverage cannot silently decline.
- **Avoid:** Reporting coverage without failing on regression.

### `cov-exclude-generated`
- **Context:** Signal quality.
- **Rule:** Exclude `main.ts`, generated `*.d.ts`, config files, mocks, and type-only modules from coverage.
- **Avoid:** Chasing a percentage inflated or deflated by unreachable code.

### `cov-behavior-over-percentage`
- **Context:** Test quality.
- **Rule:** Coverage measures executed lines, not verified behavior. Prioritize covering branches, error paths, and boundaries over raising the number.
- **Avoid:** Tests written solely to touch lines, with weak or no assertions.

### `ci-fail-on-flake`
- **Context:** Trust.
- **Rule:** Treat a flaky test as a bug: quarantine it and fix the root cause (usually a missing `await` or a hard wait). Track retry counts.
- **Avoid:** Blanket retries that hide real race conditions.

### `ci-shard-large-suites`
- **Context:** Feedback speed.
- **Rule:** Shard with `vitest --shard` / `playwright --shard` across CI jobs once the suite exceeds a few minutes.
- **Avoid:** A 20-minute serial job that developers stop waiting for.

### `ci-upload-artifacts`
- **Context:** Debugging CI failures.
- **Rule:** Upload coverage reports, Playwright traces, screenshots, and videos on failure.
- **Avoid:** Debugging a CI-only failure from the log text alone.
