# JavaScript & TypeScript Testing

Vitest/Jest patterns for unit, integration, and component tests — and where mocking stops helping.

## When to Load

- Setting up a test suite or choosing a test runner
- Deciding what to mock and what to run for real
- Writing tests for async code, HTTP handlers, or database access (React component tests live in the `react` skill)
- A suite is slow, flaky, or passes while production breaks

## Rule Categories by Priority

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | Unit tests & async correctness | HIGH | `test-` |
| 2 | Test doubles and injection | HIGH | `test-` |
| 3 | Integration (HTTP, database) | HIGH | `test-` |
| 4 | Fixtures and data setup | HIGH | `test-` |

## Rule Index

- [`test-unit-pure`](../rules/test-unit-pure.md) — Pure logic tested without infrastructure
- [`test-async-functions`](../rules/test-async-functions.md) — Await assertions; assert on rejections
- [`test-di-mocking`](../rules/test-di-mocking.md) — Inject fakes instead of mocking modules
- [`test-mocking-modules`](../rules/test-mocking-modules.md) — When module mocking is unavoidable
- [`test-spying-fakes`](../rules/test-spying-fakes.md) — Spy on interactions, fake collaborators
- [`test-integration-api`](../rules/test-integration-api.md) — Exercise the real HTTP stack
- [`test-integration-database`](../rules/test-integration-database.md) — Real database, isolated per test
- [`test-fixtures-factories`](../rules/test-fixtures-factories.md) — Factories with overrides, not shared fixtures

> React component/hook testing rules moved to the `react` skill (`react/rules/`).

## The Shape of a Healthy Suite

```
Many    unit tests        pure functions, services with injected fakes    milliseconds
Some    integration tests real HTTP stack, real DB, faked third parties   seconds
Few     E2E tests         critical user journeys only                     minutes
```

The failure mode to avoid is a suite that is entirely unit tests with everything mocked: it stays green while the wiring between layers is broken, because no test ever exercises two real components together.

## Key Principles

### Test behavior through the public surface

```ts
// ❌ asserts on how the work is done — breaks on every refactor
expect(service['calculateSubtotal']).toHaveBeenCalledWith(items)

// ✅ asserts on what the caller observes
expect(await service.createOrder(userId, input)).toMatchObject({ total: 4_500, status: 'pending' })
```

A test that knows about private methods, call counts of internal helpers, or the order of internal steps will fail on refactors that change nothing observable. Those failures train people to update tests reflexively, which is how a suite stops catching real regressions.

### Mock at the boundary, not in the middle

Mock what you do not own and cannot run: third-party HTTP APIs, payment providers, email senders, the clock. Do not mock your own repositories, services, or database when running them is cheap.

```ts
// ✅ inject a fake — no module mocking, no framework magic
const orderRepository = { create: vi.fn().mockResolvedValue(anOrder), findById: vi.fn() }
const service = createOrderService({ orderRepository, mailer: fakeMailer, clock: fixedClock })
```

Module mocking (`vi.mock`, `jest.mock`) is the fallback for code you cannot inject into — a legacy module with a top-level singleton. It is hoisted above imports, applies to the whole file, and silently keeps passing when the real module's signature changes. Treat every `vi.mock` of first-party code as a design signal: something should have been a parameter.

For HTTP, prefer intercepting at the network layer with MSW over stubbing `fetch`. It exercises your real client code — headers, serialisation, error mapping — instead of replacing it.

### Async assertions must be awaited

```ts
// ❌ passes whatever happens: the rejection is unhandled, the assertion never runs
expect(service.load('missing')).rejects.toThrow(NotFound)

// ✅
await expect(service.load('missing')).rejects.toThrow(NotFound)
```

The missing `await` is the single most common silent-pass bug in JS test suites. Enable `eslint-plugin-vitest`/`jest`'s `valid-expect` and `no-floating-promises` from `@typescript-eslint` to catch it mechanically.

Related: assert on the error *type and code*, not on the message string. Messages are copy; codes are contract.

### Fake timers for time, not `setTimeout` in tests

```ts
vi.useFakeTimers()
const promise = retryWithBackoff(fn)
await vi.advanceTimersByTimeAsync(30_000)
await promise
vi.useRealTimers()
```

Any test containing a real `sleep()` is trading wall-clock time for flakiness. Use the async timer-advancing APIs so pending promise callbacks flush between ticks.

### Database tests: real database, per-test isolation

```ts
beforeEach(async () => { await db.transaction(async tx => { … }) })   // rollback after each test
```

Two workable strategies: wrap each test in a transaction and roll back, or truncate the affected tables between tests. Both beat a shared seeded database, where test order becomes significant and one failure cascades.

Run against the same engine and version as production — Testcontainers makes this cheap. SQLite standing in for PostgreSQL hides exactly the behaviors worth testing: constraint semantics, concurrency, JSON operators, migration correctness.

### Component tests: query the way a user perceives the UI

```tsx
render(<LoginForm onSubmit={onSubmit} />)
await userEvent.type(screen.getByLabelText(/email/i), 'a@b.co')
await userEvent.click(screen.getByRole('button', { name: /sign in/i }))
expect(onSubmit).toHaveBeenCalledWith({ email: 'a@b.co' })
```

Prefer `getByRole` and `getByLabelText` over `data-testid`: they fail when the component becomes inaccessible, so the test doubles as an accessibility check. Use `userEvent` over `fireEvent` — it dispatches the full event sequence a real interaction produces.

Never assert on class names or DOM structure; those are implementation. `findBy*` (async) over `waitFor` wrappers where possible, and never assert on a snapshot as the only assertion — a snapshot records what the code does, including its bugs.

### Factories over shared fixtures

```ts
const makeUser = (overrides: Partial<User> = {}): User => ({
  id: 'u_1', email: 'a@b.co', role: 'member', createdAt: new Date('2024-01-01'), ...overrides,
})

const admin = makeUser({ role: 'admin' })
```

Each test states only what it cares about, and the relevant difference is visible in the test body. A shared `beforeEach` fixture forces readers to scroll elsewhere to understand why a test passes, and coupling every test to one object shape makes it unchangeable.

### Coverage is a signal, not a goal

Line coverage says code ran, not that it was verified. A suite with 95% coverage and no assertions on error paths is worse than 70% with the critical branches genuinely exercised. Track coverage to find untested areas; do not set a percentage gate that gets satisfied with tests nobody reads.

## Vitest vs Jest

| | Vitest | Jest |
|---|---|---|
| ESM / TS | Native via Vite | Needs transform config |
| Speed | Faster (Vite transform, worker threads) | Slower on large TS suites |
| API | Jest-compatible (`describe`/`it`/`expect`) | The original |
| Browser mode | Yes | No (jsdom only) |

For a new project on Vite or plain TypeScript, Vitest is the default. Migrating an existing Jest suite is mostly a config change plus `jest.` → `vi.`, so the choice is not costly to revisit.

## Sources

- [Vitest — Documentation](https://vitest.dev/guide/)
- [Jest — Documentation](https://jestjs.io/docs/getting-started)
- [Testing Library — Guiding Principles](https://testing-library.com/docs/guiding-principles)
- [Testing Library — About queries](https://testing-library.com/docs/queries/about)
- [MSW — Mock Service Worker](https://mswjs.io/docs/)
- [Testcontainers for Node.js](https://node.testcontainers.org/)
