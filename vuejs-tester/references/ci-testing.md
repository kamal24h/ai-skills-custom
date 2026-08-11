# CI Testing

Running Vue test suites in a pipeline: staging, sharding, artifacts, and flake control.

## 1. Pipeline Stages

Order gates by speed so failures surface fast:

```
lint  →  type-check  →  unit + component  →  build  →  E2E
(sec)     (~10s)          (~30s)              (~30s)    (minutes)
```

A type error should never wait behind a five-minute E2E run.

## 2. GitHub Actions

```yaml
name: CI
on:
  push: { branches: [main] }
  pull_request:

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  static:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: pnpm }
      - run: pnpm install --frozen-lockfile
      - run: pnpm lint
      - run: pnpm type-check          # vue-tsc --noEmit

  unit:
    runs-on: ubuntu-latest
    needs: static
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: pnpm }
      - run: pnpm install --frozen-lockfile
      - run: pnpm vitest run --coverage
      - uses: actions/upload-artifact@v4
        if: always()
        with: { name: coverage, path: coverage/ }

  e2e:
    runs-on: ubuntu-latest
    needs: unit
    strategy:
      fail-fast: false
      matrix:
        shard: [1, 2, 3, 4]
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: pnpm }
      - run: pnpm install --frozen-lockfile
      - run: pnpm exec playwright install --with-deps chromium
      - run: pnpm exec playwright test --shard=${{ matrix.shard }}/4
        env:
          E2E_USER: ${{ secrets.E2E_USER }}
          E2E_PASSWORD: ${{ secrets.E2E_PASSWORD }}
      - uses: actions/upload-artifact@v4
        if: ${{ !cancelled() }}
        with:
          name: playwright-report-${{ matrix.shard }}
          path: playwright-report/
          retention-days: 7
```

Key details:

- `concurrency` + `cancel-in-progress` avoids queueing runs for superseded commits.
- `--frozen-lockfile` fails on lockfile drift instead of silently resolving different versions.
- `fail-fast: false` on the shard matrix so one shard's failure does not hide the others'.
- `if: always()` / `if: !cancelled()` on artifact upload — you need artifacts most when the job failed.

## 3. Sharding

```bash
pnpm vitest run --shard=1/4
pnpm exec playwright test --shard=1/4
```

Shard once a suite exceeds a few minutes. Four shards is a reasonable starting point; more shards mean more fixed startup cost per job, so measure rather than guessing.

Merge coverage across Vitest shards before enforcing thresholds, or enforce them in a single unsharded job.

## 4. Browser Binary Caching

```yaml
- name: Cache Playwright browsers
  uses: actions/cache@v4
  with:
    path: ~/.cache/ms-playwright
    key: playwright-${{ runner.os }}-${{ hashFiles('pnpm-lock.yaml') }}

- run: pnpm exec playwright install --with-deps chromium
```

Keying on the lockfile invalidates the cache exactly when the Playwright version changes.

## 5. Flake Control

A test that passes on retry is a bug, not a result.

```ts
// playwright.config.ts
retries: process.env.CI ? 2 : 0,
use: { trace: 'on-first-retry' },
```

Retries exist to keep the pipeline usable **while you fix the root cause**, not as a permanent policy.

### Diagnosing a flaky test

1. Reproduce locally: `vitest run --sequence.shuffle --repeat=20 path/to/test`
2. Run it in isolation — if it passes alone, another test is leaking state.
3. Search for `setTimeout` waits, missing `await`s, and unrestored fake timers.
4. Check for shared module state, shared stores, or a shared router.
5. Check for time or timezone dependence (`vi.setSystemTime`, `TZ=UTC` in CI).
6. For E2E: open the trace and look at what the page actually showed at the failure point.

```yaml
env:
  TZ: UTC
  LANG: en_US.UTF-8
```

Pinning timezone and locale in CI eliminates a whole class of date-formatting flake.

### Quarantine, don't ignore

```ts
it.fails('reorders on drag', async () => { … })    // documented, still reported
// or
it.skip('reorders on drag — flaky, see #482', async () => { … })
```

Always link an issue. A `skip` without a reference becomes permanent.

## 6. Failing on Warnings

```ts
// src/test/setup.ts
const originalWarn = console.warn
console.warn = (...args: unknown[]) => {
  if (typeof args[0] === 'string' && args[0].includes('[Vue warn]')) {
    throw new Error(args.join(' '))
  }
  originalWarn(...args)
}

process.on('unhandledRejection', (reason) => { throw reason })
```

This turns missing `:key`s, mutated props, undeclared emits, and failed injections from log noise into CI failures — where they get fixed.

## 7. Required Checks and PR Feedback

- Make `lint`, `type-check`, and `unit` required status checks on the default branch.
- Post coverage **diff** on the PR (Codecov, or a small script) so new untested code is visible at review time.
- Publish the Playwright HTML report as an artifact and link it from the failure summary.

## 8. Performance

| Technique | Effect |
|---|---|
| `node` environment for pure-logic tests | Skips jsdom startup |
| Vitest projects (unit / browser split) | Only pay for a browser where needed |
| `pool: 'threads'` (default) | Parallel workers |
| Dependency + browser caching | Removes install time |
| Sharding | Linear wall-clock reduction |
| E2E limited to critical journeys | The biggest lever by far |

Measure before optimizing: `vitest run --reporter=verbose` shows per-file duration, and Playwright's HTML report ranks slowest specs.

## 9. Nightly / Extended Runs

Keep the PR pipeline fast; run the expensive matrix on a schedule.

```yaml
on:
  schedule: [{ cron: '0 3 * * *' }]
```

Nightly is the right home for: cross-browser E2E (firefox, webkit), mobile viewports, visual regression, and `--repeat` flake hunting.

## Anti-Patterns

| Anti-pattern | Consequence | Fix |
|---|---|---|
| E2E before type-check | Slow feedback on trivial errors | Order gates by speed |
| No `--frozen-lockfile` | CI resolves different versions than local | Add the flag |
| Artifacts uploaded only on success | Nothing to debug when it fails | `if: always()` |
| Retries as permanent policy | Real races ship | Fix the root cause; track retry counts |
| Un-pinned timezone/locale | Date-format flake | `TZ=UTC` in CI env |
| Vue warnings only logged | Contract violations invisible | Throw on `[Vue warn]` |
| Browsers reinstalled every run | Minutes wasted per job | Cache `~/.cache/ms-playwright` |
| One serial 20-minute job | Developers stop waiting | Shard the suite |
| `skip` without an issue link | Permanently dead test | Reference a ticket |
| Coverage reported but not enforced | Silent decline | Thresholds + PR diff |
