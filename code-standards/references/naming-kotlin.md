# Kotlin Naming Conventions

From the official Kotlin Coding Conventions, plus the AndroidX Compose API Guidelines for Compose naming. 

## Element table

| Element | Convention | Example |
|---|---|---|
| Package | lowerCamelCase, no underscores | `org.example.project` |
| Class / object / interface | PascalCase noun | `InvoiceRepository` |
| Function | camelCase verb or verb phrase | `calculateTotal()` |
| Property / variable | camelCase | `invoiceTotal` |
| Constant (top-level `const val` or object `val`) | SCREAMING_SNAKE_CASE | `const val MAX_RETRIES = 5` |
| Other top-level/object vals | camelCase (they are not constants) | `val defaultTimeout = 30` |
| Backing property | underscore prefix | `_state: StateFlow<UiState>` |
| Enum class / entries | PascalCase class; PascalCase entries (SCREAMING_SNAKE acceptable for C-style) | `enum class InvoiceStatus { Paid, Overdue }` |
| Type parameter | short UpperCamel or single capital | `<T>`, `<RequestData>` |
| Test function names | backticked sentences allowed | `` fun `empty cart throws on checkout`() `` |

## Rules worth remembering

- Factory functions that create instances of an abstract type may share the abstract return type's name (`interface Foo { … }`, `fun Foo(): Foo`).
- Don't prefix interfaces with `I`; don't suffix implementations with `Impl` unless forced by name collision.
- Extension functions live in a package named after what they extend where practical (`kotlin.time.Duration.Companion`).

## Compose specifics (AndroidX API Guidelines)

| Element | Convention | Example |
|---|---|---|
| Composable emitting UI (returns Unit) | PascalCase **noun**, no UI-type suffix unless needed to disambiguate | `ProfileCard(...)` — `ProfileCardContent` only when required |
| Composable returning a value | camelCase, reads as noun | `rememberScrollState()` |
| Modifier parameter | first optional parameter named `modifier: Modifier = Modifier` | — |
| Slot parameters | named by role, trailing lambda | `content: @Composable () -> Unit` |
| State holder | PascalCase + `State`/`StateHolder` | `ScrollState` |
| Effect helper | camelCase effect-named | `LaunchedEffect`, `DisposableEffectEffect` pattern: `rememberX`/`XEffect` |

## Sources

- [Kotlin Coding Conventions](https://kotlinlang.org/docs/coding-conventions.html)
- [AndroidX Compose API Guidelines](https://github.com/androidx/androidx/blob/androidx-main/compose/docs/compose-api-guidelines.md)
