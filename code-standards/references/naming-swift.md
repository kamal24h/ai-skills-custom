# Swift / SwiftUI Naming Conventions

From the official Swift API Design Guidelines. Core principle: names must **read like English phrases** at the call site — clarity beats brevity.

## Element table

| Element | Convention | Example |
|---|---|---|
| Type (struct/class/enum/actor/protocol) | UpperCamelCase noun | `InvoiceParser`, `NetworkSession` |
| Function / method / property / variable / parameter | lowerCamelCase | `parseInvoice(_:)`, `isValid` |
| Protocol describing *what something is* | noun | `Collection`, `View` |
| Protocol describing a *capability* | `-able` / `-ible` / `-ing` | `Equatable`, `ProgressReporting` |
| Delegate / data source protocol | role noun suffix | `UITableViewDelegate`, `SceneDataSource` |
| Boolean | assertion reading as fact | `isEmpty`, `hasNextLine` |
| Imperative (mutating) methods | verb, imperative mood | `list.sort()` |
| Non-mutating counterpart | `-ed` / `-ing` participle | `sorted()`, `appending(_:)` |
| Factory method | `make` prefix | `makeIterator()` |
| Acronyms | uniformly upper- or lowercase in code | `userID`, `url`, `httpBody` (never `userId`, `URL`) |
| Enum cases | lowerCamelCase (Swift 3+ convention) | `.automatic`, `.byName` |

## Rules worth remembering

- **Omit needless words**: the type already carries context — `invoice.remove()` not `invoice.removeInvoice()`. Keep words that disambiguate: `remove(_ element:)` vs `remove(at: index)`.
- Side-effect-free methods read as noun phrases (`distance(to:)`); side-effectful ones read as commands (`print(_:)`).
- Prefer first-parameter labels omitted when the function name carries the meaning (`move(from:to:)`).

## SwiftUI specifics

| Element | Convention | Example |
|---|---|---|
| View struct | PascalCase noun; no `View` suffix required unless it aids clarity | `ProfileHeader` / `ProfileHeaderView` both acceptable — pick one per project |
| Modifier chain | reads as transformation verbs | `.font(.headline).padding()` |
| State properties | camelCase noun | `@State private var isEditing = false` |
| Environment/model objects | camelCase noun | `@Environment(UserStore.self) private var userStore` |
| Action closures | named by interaction | `onSubmit`, `onDelete` |

## Sources

- [Swift API Design Guidelines](https://www.swift.org/documentation/api-design-guidelines/)
- [The Swift Programming Language — Naming](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/naming/)
