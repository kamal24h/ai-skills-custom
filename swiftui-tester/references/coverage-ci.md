# Coverage & CI for SwiftUI Projects

Code coverage measurement with Xcode tooling, sensible gates, and CI hygiene for Swift Testing/XCTest suites.

## 1. Enabling and Reading Coverage

- Enable per scheme: **Scheme → Test → Options → Code Coverage** (App targets only; exclude test targets).
- After a run, Xcode shows line coverage in the editor gutter; the report navigator lists per-file/per-class percentages.
- Export machine-readable data with `xccov`:

```bash
xcodebuild test -project MyApp.xcodeproj \
  -scheme MyApp -destination 'platform=iOS Simulator,name=iPhone 16' \
  -resultBundlePath results.xcresult

xccov view --report results.xcresult          # human-readable
xccov view --report --json results.xcresult   # parse in CI
```

## 2. Sensible Gates

| Layer | Expectation | Rationale |
|---|---|---|
| Domain/business logic | High (80–90%+) | Cheap to test, highest defect cost |
| ViewModels / @Observable state | High on logic branches | Behavior lives here |
| Views / SwiftUI layout | Low or excluded | Preview + UI tests cover rendering |
| App entry, generated code | Excluded | No behavior to verify |

Coverage is a *diagnostic*, not a goal: a gate at 100% rewards assertion-free tests. Gate the delta on changed files, or gate specific modules, rather than demanding a global number.

## 3. CI Wiring (GitHub Actions example)

```yaml
- name: Run tests
  run: |
    xcodebuild test \
      -project MyApp.xcodeproj -scheme MyApp \
      -destination 'platform=iOS Simulator,name=iPhone 16' \
      -resultBundlePath results.xcresult \
      | xcbeautify

- name: Coverage report
  run: xccov view --report results.xcresult
```

- Use `-parallel-testing-enabled YES` where suites are independent; keep `.serialized` traits out of shared-state-free code.
- Fail fast on flakiness: rerun-once policies hide real races — investigate instead (`--repeat` on `xcodebuild`, or Swift Testing's `.repetitionBehavior`).

## 4. Hygiene Checklist

- [ ] Coverage enabled on app schemes; test targets excluded from measurement
- [ ] `xccov` JSON parsed in CI; regression comment posted per PR (or threshold job)
- [ ] New modules carry their own coverage expectation, documented in the module README
- [ ] No `@testable import` of app entry points; generated code excluded via target membership
- [ ] Flaky tests quarantined with `withKnownIssue` + tracking link, fixed within an agreed window

## Related Rules

- `test-known-issue` for tracked flaky tests; `ui-test-page-objects` for stable UI flows.

## Sources

- [Xcode Help — Code coverage](https://help.apple.com/xcode/mac/current/#/itde0-19279)
- [xccov — man page](https://keith.github.io/xcode-man-pages/xccov.1.html)
- [Swift Testing Documentation](https://developer.apple.com/documentation/testing)
