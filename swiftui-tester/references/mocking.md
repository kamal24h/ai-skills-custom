# Mocking & Test Doubles for SwiftUI Apps

Apple platforms ship no mocking framework — the documented pattern is **protocol-oriented dependency injection** plus hand-rolled fakes/stubs. This file shows how to structure doubles that stay compatible with `@Observable` models, Swift Testing, and strict concurrency.

## 1. Protocol Boundaries at the Seam

Define protocols where your app talks to the outside world (network, persistence, auth, clocks). Production injects the real implementation; tests inject a fake.

```swift
protocol UserServiceProtocol: Sendable {
    func fetchUser(id: UUID) async throws -> User
}

// Production
final class UserService: UserServiceProtocol { /* real network */ }

// Test double — records calls, returns scripted results
@MainActor
final class MockUserService: UserServiceProtocol {
    private(set) var fetchCalls: [UUID] = []
    var result: Result<User, Error> = .success(.preview)

    func fetchUser(id: UUID) async throws -> User {
        fetchCalls.append(id)
        return try result.get()
    }
}
```

## 2. Doubles Vocabulary

| Double | Purpose | Use when |
|---|---|---|
| Stub | Hard-coded return values | The collaborator's data shape is all that matters |
| Fake | Working lightweight implementation | In-memory store standing in for SwiftData/network |
| Spy | Records interactions | Asserting "this was called with X" |
| Mock (strict) | Pre-programmed expectations | Avoid hand-rolling; prefer spies + explicit assertions |

Prefer **state verification** (assert on returned/observed state) over interaction verification; use spies only when the side effect *is* the behavior (analytics, logging).

## 3. Injecting into @Observable ViewModels

```swift
@Observable
@MainActor
final class ProfileViewModel {
    private let userService: any UserServiceProtocol

    init(userService: any UserServiceProtocol = UserService()) {
        self.userService = userService
    }
}

// Test
@Test @MainActor func loadsUser() async throws {
    let service = MockUserService()
    let vm = ProfileViewModel(userService: service)
    await vm.load(id: userID)
    #expect(service.fetchCalls == [userID])
}
```

Defaults in production initializers keep SwiftUI previews working without test scaffolding.

## 4. Time, Networking, and Side Effects

- Inject `Clock`/`ContinuousClock` (Swift ClockAPI) so deadline logic is testable with `TestClock`-style fakes or short durations.
- Replace URL loading with protocol seams (`URLSessionProtocol`) or stub via `URLProtocol` when a seam is impossible — `URLProtocol` is Apple's sanctioned interception point.
- For notification/location delegates, bridge through an `AsyncStream` you can yield scripted events into from tests.

## 5. Strict Concurrency Rules for Doubles

- Mark doubles `Sendable` or confine them to one actor; shared mutable recording arrays must live behind `@MainActor` or a lock.
- Do not share one mock instance across parallel tests — Swift Testing runs in parallel by default ([`.serialized`](swift-testing.md) only for genuinely shared fixtures).

## Related Rules

- `test-no-shared-state`, `test-async-confirmation`, `test-mainactor-isolation` (see SKILL.md Rule Index)
- Persistence fakes: [`persistence-testing.md`](persistence-testing.md) (in-memory `ModelContainer` is itself the canonical SwiftData fake)

## Sources

- [Swift Testing Documentation](https://developer.apple.com/documentation/testing)
- [Dependency Injection and Testing (Apple sample practices)](https://developer.apple.com/documentation/swiftui/model-data)
- [URLProtocol — URL Loading System](https://developer.apple.com/documentation/foundation/urlprotocol)
- [Swift Clock API](https://developer.apple.com/documentation/swift/clock)
