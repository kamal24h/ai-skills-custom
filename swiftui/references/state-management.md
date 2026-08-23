# State Management in SwiftUI

Comprehensive guide for data flow in modern SwiftUI (iOS 15–26+), focusing on the Observation framework and property wrappers.

## 1. The Observation Framework (iOS 17+)

The `@Observable` macro is the modern standard for state management, replacing `ObservableObject`.

### Core Directives
- **Use `@Observable`:** For classes that own data shared across multiple views.
- **No `@Published`:** Properties inside an `@Observable` class are automatically tracked.
- **Inject via `@State` or Environment:**
    - Use `@State var viewModel = ViewModel()` for view-owned objects.
    - Use `@Bindable` when you need to pass a binding to a property of an `@Observable` object.
    - Use `.environment(viewModel)` to inject into the view hierarchy.

### Migration Path
- `ObservableObject` → `@Observable`
- `@Published` → (Delete, it's automatic)
- `@StateObject` → `@State`
- `@ObservedObject` → `@Bindable` (if bindings needed) or just pass as a parameter.
- `@EnvironmentObject` → `@Environment`

## 2. Property Wrappers Cheat Sheet

| Wrapper | Ownership | Use Case |
|---------|-----------|----------|
| `@State` | Owned | Private, simple values or `@Observable` instances. |
| `@Binding` | Shared | Two-way connection to a value owned elsewhere. |
| `@Bindable` | Shared | Create bindings to properties of an `@Observable` object. |
| `@Environment` | Shared | Global state, system settings, or DI. |
| `@Query` | Persistence | Fetching data from SwiftData. |

## 3. Best Practices
- **Single Source of Truth:** Ensure every piece of data has exactly one owner.
- **Minimal Invalidation:** Extract subviews to ensure only the necessary parts of the UI re-render when state changes.
- **Private State:** Mark `@State` properties as `private` to encapsulate view logic.
- **Avoid Global Singletons:** Prefer `@Environment` or Dependency Injection for testability.
- **Observation Pitfall:** Remember that `@Observable` tracks access in `body`. If you access a property outside of `body` (e.g., in a helper method), it might not trigger a re-render unless called from `body`.

## 4. Environment Injection Patterns

| Scenario | Pattern |
|---|---|
| Provide an `@Observable` instance app-wide | `.environment(store)` on the root, read with `@Environment(Store.self) private var store` |
| Read a system value | `@Environment(\.dismiss)`, `@Environment(\.scenePhase)` |
| Pass a *binding* to an `@Observable` property | `@Bindable var vm` → `$vm.name` |
| Custom environment key | `EnvironmentKey` + computed `EnvironmentValues` extension (value types only) |

```swift
// Custom key - value types only; objects go through .environment(obj)
private struct ThemeKey: EnvironmentKey {
    static let defaultValue: Theme = .system
}
extension EnvironmentValues {
    var theme: Theme {
        get { self[ThemeKey.self] }
        set { self[ThemeKey.self] = newValue }
    }
}
```

## 5. Observation Pitfalls and Scoping

- **Track-by-access:** `@Observable` records which properties `body` reads. Reading `user.profile.avatar` tracks only that path — unrelated mutations of `user.settings` do not invalidate the view.
- **Escape hatches break tracking:** accessing state inside closures stored away from `body`, or in `DispatchQueue`-style legacy callbacks, bypasses observation. Do all reads inside `body` or via `withObservationTracking`.
- **Value semantics still matter:** `@Observable` classes are reference types — two views sharing one instance share state deliberately; copy into structs at boundaries when isolation is needed.
- **Do not mix systems:** a class cannot be both `@Observable` and `ObservableObject`; pick per type.

## 6. Example: Modern MVVM

```swift
@Observable
class UserViewModel {
    var name: String = ""
    var age: Int = 0
}

struct UserView: View {
    @State private var viewModel = UserViewModel()
    
    var body: some View {
        Form {
            TextField("Name", text: $viewModel.name)
            Stepper("Age: \(viewModel.age)", value: $viewModel.age)
        }
    }
}
```

## Cross References

- Related rules: `swiftui-state-observable`, `conc-actor-isolation`, `layout-focus-state`
- Related references: [`architecture.md`](architecture.md), [`concurrency.md`](concurrency.md), [`view-structure.md`](view-structure.md), [`swiftdata.md`](swiftdata.md)

## Sources

- [SwiftUI — State and data flow](https://developer.apple.com/documentation/swiftui/state-and-data-flow)
- [Observation framework](https://developer.apple.com/documentation/observation)
