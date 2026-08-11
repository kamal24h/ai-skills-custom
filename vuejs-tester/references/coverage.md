# Coverage

Configuring, enforcing, and correctly interpreting test coverage in a Vue project.

## 1. Setup

```bash
pnpm add -D @vitest/coverage-v8
```

```ts
// vitest.config.ts
test: {
  coverage: {
    provider: 'v8',                       // fast, native; use 'istanbul' if you need finer branch data
    reporter: ['text', 'text-summary', 'lcov', 'html'],
    reportsDirectory: './coverage',
    all: true,                            // include files with zero tests
    include: ['src/**/*.{ts,vue}'],
    exclude: [
      'src/main.ts',
      'src/router/index.ts',
      'src/**/*.d.ts',
      'src/**/types.ts',
      'src/test/**',
      'src/**/__mocks__/**',
      '**/*.config.*',
    ],
    thresholds: {
      lines: 80,
      functions: 80,
      branches: 70,
      statements: 80,
    },
  },
}
```

**`all: true` matters.** Without it, a file with no tests at all is simply absent from the report, and coverage looks great while whole modules are untested.

```bash
pnpm vitest run --coverage
```

## 2. Thresholds

| Code | Target | Reasoning |
|---|---|---|
| Business logic, composables, stores | 90%+ | Highest defect cost |
| Utilities, formatters, validators | 95%+ | Pure, trivial to test |
| Components | 70–85% | Behavior matters more than every branch |
| API/service layer | 80%+ | Error mapping must be covered |
| `main.ts`, plugin registration, config | excluded | Nothing meaningful to assert |
| Generated code, `.d.ts` | excluded | Not authored |

Per-file thresholds prevent one well-tested module from masking an untested one:

```ts
thresholds: {
  lines: 80, functions: 80, branches: 70, statements: 80,
  'src/composables/**': { lines: 90, functions: 90, branches: 85 },
  'src/lib/**': { lines: 95, functions: 95 },
}
```

### Ratcheting into a legacy codebase

Set thresholds at the current level and raise them as coverage improves:

```ts
thresholds: { lines: 45, functions: 40, branches: 35, statements: 45, autoUpdate: true }
```

`autoUpdate` rewrites the thresholds upward as coverage improves, locking in gains without blocking work.

## 3. Coverage of `.vue` Files

The v8 provider maps coverage back through the SFC compiler, so `<script setup>` code is attributed to the `.vue` file. Two caveats:

- **Template branches** (`v-if`, `v-else`, ternaries in the template) are reported inconsistently across providers. Do not tune thresholds around them.
- Vue macros compile away; do not expect `defineProps` lines to appear.

If branch attribution in SFCs matters to you, switch to `provider: 'istanbul'` — it is slower but produces more faithful branch data.

## 4. Reading a Report

Prioritize by **branch** coverage, not line coverage. Uncovered branches are untested decisions — the places bugs live.

```
File                    | % Stmts | % Branch | % Funcs | % Lines | Uncovered Lines
------------------------|---------|----------|---------|---------|----------------
src/composables/        |         |          |         |         |
  useCart.ts            |   95.2  |   62.5   |  100.0  |   95.2  | 48-52, 71
  useCheckout.ts        |   88.0  |   40.0   |   85.7  |   88.0  | 30-45
```

`useCheckout.ts` at 40% branches means more than half its decision paths — most likely the error and edge cases — are never exercised, despite 88% of lines running.

`reporter: ['html']` plus `open coverage/index.html` shows exactly which branch was never taken.

## 5. Coverage Is Not Test Quality

```ts
// 100% coverage, zero value
it('renders', () => {
  render(UserCard, { props: { user: makeUser() } })
  expect(true).toBe(true)
})
```

Every line executes; nothing is verified. Coverage answers "was this line run?", never "does this behave correctly?".

Use coverage as a **gap finder**, not a goal:

- 0% on a file → nobody tested it
- High lines, low branches → only the happy path is tested
- 100% everywhere with few assertions → the metric is being gamed

The signals that actually correlate with quality: are error paths tested? empty states? boundary values? Does each test have meaningful assertions?

## 6. Exclusions

```ts
/* v8 ignore next */
if (import.meta.env.DEV) { setupDevtools() }

/* v8 ignore start */
function unreachableFallback() { throw new Error('unreachable') }
/* v8 ignore stop */
```

Use exclusion comments sparingly and only for genuinely unreachable or environment-specific code. Every ignore comment should have a reason next to it — an untracked `ignore` is how coverage silently rots.

## 7. CI Integration

```yaml
- run: pnpm vitest run --coverage
- uses: codecov/codecov-action@v5
  with:
    files: ./coverage/lcov.info
    fail_ci_if_error: true
- uses: actions/upload-artifact@v4
  if: always()
  with:
    name: coverage-html
    path: coverage/
```

Fail the build on threshold violations (Vitest does this automatically when `thresholds` are set). Surface the diff coverage on pull requests so new untested code is visible at review time — that is where coverage pays off, not in the absolute number.

## 8. Merging Coverage Across Projects

With Vitest projects (unit + browser), or with a separate E2E coverage run, merge before reporting:

```bash
pnpm vitest run --coverage --coverage.reporter=json
# then merge with nyc / c8 if combining with E2E instrumentation
```

Do not report unit and E2E coverage separately and average them — the numbers are not comparable.

## Anti-Patterns

| Anti-pattern | Consequence | Fix |
|---|---|---|
| No `all: true` | Untested files vanish from the report | Enable it |
| Coverage measured but not enforced | Silent decline over time | `thresholds` |
| Chasing 100% | Meaningless tests, wasted effort | Target branches and risk |
| Ignoring branch coverage | Happy-path-only suite passes the gate | Prioritize branch % |
| Tests written to touch lines | Green metric, no verification | Assert behavior |
| `main.ts`/config in the report | Diluted, misleading percentage | Exclude them |
| Broad `v8 ignore` blocks | Real gaps hidden | Narrow, justified ignores |
| Threshold set far below reality | Ratchet never engages | Set at current level + `autoUpdate` |
| Comparing unit and E2E coverage | Incomparable numbers | Merge or report separately with context |
