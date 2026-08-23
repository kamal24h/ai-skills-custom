# Kotlin Multiplatform (KMP) Patterns

Expert guidance for sharing code across Android, iOS, Desktop, and Web using Kotlin Multiplatform.

## 1. Project Structure

A typical KMP project structure:

```
common/
├── src/
│   ├── commonMain/             (Shared logic: domain, data, network)
│   ├── androidMain/            (Android-specific implementations)
│   ├── iosMain/                (iOS-specific implementations)
│   ├── desktopMain/            (Desktop-specific implementations)
│   └── wasmJsMain/             (Web-specific implementations)
└── build.gradle.kts
```

### Source sets and hierarchy

- Every target contributes a **compilation**; each compilation consumes `commonMain` plus its platform source set.
- The **hierarchical structure is on by default**: you can create *intermediate* source sets shared by a subset of targets (for example `appleMain` shared by `iosMain` and `macosMain`) and the toolchain resolves `expect`/`actual` across the graph.
- Default source sets provided by the plugin: `commonTest`, plus `<target>Main`/`<target>Test` per target. Intermediate sets are declared with `applyDefaultHierarchyTemplate()` customization or manually via `dependsOn()`.

```kotlin
kotlin {
    androidTarget()
    iosArm64()
    iosSimulatorArm64()

    sourceSets {
        commonMain.dependencies { implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.10.1") }
    }
}
```

- Declare dependencies for the **widest** source set that needs them (`commonMain` first); add platform artifacts only in leaf sets.
- Platform-specific dependencies (OkHttp, Room) never appear in `commonMain` — the dependency check fails the build, which is the point.

### Targets DSL essentials

| Target | Declaration |
|---|---|
| Android | `androidTarget()` + AGP `library` config |
| iOS device/simulator | `iosArm64()`, `iosSimulatorArm64()`, `iosX64()` |
| Desktop JVM | `jvm()` |
| Browser | `wasmJs { browser() }` or `js(IR) { browser() }` |

For Apple frameworks consumed from Swift, configure the Gradle-MacOS plugin:

```kotlin
listOf(iosArm64(), iosSimulatorArm64()).forEach { target ->
    target.binaries.framework {
        baseName = "Shared"
        isStatic = true
    }
}
```

Prefer **direct integration** (Xcode build phases calling Gradle) over checked-in frameworks so Swift builds always consume fresh binaries.

## 2. expect / actual Pattern

Use `expect`/`actual` when you need to access platform-specific APIs.

### Example: Platform Name
```kotlin
// commonMain
expect fun getPlatformName(): String

// androidMain
actual fun getPlatformName(): String = "Android ${android.os.Build.VERSION.SDK_INT}"

// iosMain
actual fun getPlatformName(): String = "iOS ${UIDevice.currentDevice.systemVersion}"
```

### Example: Platform-specific Class
```kotlin
// commonMain
expect class PlatformLogger() {
    fun log(message: String)
}

// androidMain
actual class PlatformLogger actual constructor() {
    actual fun log(message: String) {
        android.util.Log.d("KMP", message)
    }
}
```

## 3. Interface-based Abstraction (Recommended)

Prefer interfaces and Dependency Injection over `expect`/`actual` for better testability and cleaner separation.

```kotlin
// commonMain
interface FileSystem {
    fun readText(path: String): String
}

class DataRepository(private val fileSystem: FileSystem) {
    fun loadConfig() = fileSystem.readText("config.json")
}

// androidMain
class AndroidFileSystem : FileSystem {
    override fun readText(path: String): String = // Android impl
}

// iosMain
class IosFileSystem : FileSystem {
    override fun readText(path: String): String = // iOS impl
}
```

## 4. KMP Networking with Ktor

Ktor is the standard networking library for KMP.

```kotlin
// commonMain
val client = HttpClient {
    install(ContentNegotiation) {
        json(Json {
            ignoreUnknownKeys = true
            explicitNulls = false
        })
    }
}

suspend fun fetchUsers(): List<User> = client.get("https://api.example.com/users").body()
```

### KMP HttpClient Engines

| Platform | Engine |
|----------|--------|
| Android | `OkHttp` |
| iOS | `Darwin` |
| Desktop | `CIO` / `Java` |
| JS/WASM | `Js` |

## 5. KMP Persistence with SQLDelight

SQLDelight generates type-safe Kotlin APIs from SQL.

```kotlin
// commonMain
val database = MyDatabase(driver)

// androidMain
val driver = AndroidSqliteDriver(MyDatabase.Schema, context, "test.db")

// iosMain
val driver = NativeSqliteDriver(MyDatabase.Schema, "test.db")
```

## 6. Compose Multiplatform

Compose Multiplatform allows sharing UI across Android, iOS, Desktop, and Web.

```kotlin
// commonMain
@Composable
fun App() {
    MaterialTheme {
        var text by remember { mutableStateOf("Hello, World!") }
        Button(onClick = { text = "Hello, KMP!" }) {
            Text(text)
        }
    }
}
```

## 7. KMP Dispatchers

`Dispatchers.IO` is NOT available in `commonMain` for all targets.

### Abstraction Pattern
```kotlin
// commonMain
expect val ioDispatcher: CoroutineDispatcher

// androidMain
actual val ioDispatcher = Dispatchers.IO

// iosMain
actual val ioDispatcher = Dispatchers.Default // iOS uses Default for IO
```

## 8. Testing Across Targets

- Shared business logic tests live in `commonTest` and run once **per target** — the same test class executes on JVM, iOS simulator, etc.
- Platform behaviors (permissions, file systems) get `expect`/`actual` fakes or run in `<target>Test` sets (`androidUnitTest`, `iosSimulatorArm64Test`).
- Run all targets locally: `./gradlew allTests`; CI aggregates via the `kotlin-multiplatform` plugin's combined reports.

```kotlin
// commonMain test
class UserRepositoryTest {
    @Test
    fun parsesUser() = runTest {
        val repo = UserRepository(FakeFileSystem())
        assertEquals("Ada", repo.loadName("user.json"))
    }
}
```

## 9. Best Practices

| Rule | Description |
|------|-------------|
| Keep `commonMain` pure | Avoid platform-specific imports in shared code |
| Prefer interfaces | Use interfaces for platform-specific capabilities; reserve `expect`/`actual` for what interfaces cannot express (top-level functions, companion objects) |
| Use `kotlinx.serialization` | The standard for KMP serialization (`@Serializable`, JSON plugin) |
| Use `kotlinx.datetime` / `kotlinx-io` | Official multiplatform libraries before reaching for platform APIs |
| Use `Napier` or `Kermit` | Multiplatform logging libraries |
| Use `Koin` or KotlinInject | Popular DI options that compile in common code |
| Gate API surface per source set | Anything exported to Swift is public API forever — keep the ObjC-exported surface small |

## 10. Common Pitfalls

- **Memory Management on iOS:** The new (default since Kotlin 1.7.20) memory manager removed freezing requirements, but shared global mutable state still needs synchronization — prefer state confined inside coroutines/actors.
- **ObjC export limits:** Generics are erased to star-projections in Swift; sealed classes, inline value classes, and suspend functions with complex signatures do not translate cleanly — wrap them behind simple facades.
- **Platform-specific Dependencies:** Ensure every library version supports *all* your targets; a single Android-only transitive dependency breaks iOS compilation.
- **Resources:** Use Compose Multiplatform resources for sharing strings, images, and fonts across targets instead of duplicating per-platform assets.
- **Binary compatibility churn:** Framework rebuild ordering causes stale binaries in Xcode — script Gradle invocation inside Xcode build phases rather than committing frameworks.

## Cross References

- Related rules: `kt-kmp-expect-actual`, `coro-inject-dispatchers`
- Related references: [`coroutines.md`](coroutines.md), [`architecture.md`](architecture.md), [`compose-ui.md`](compose-ui.md)

## Sources

- [Kotlin Multiplatform documentation](https://www.jetbrains.com/help/kotlin-multiplatform-dev/get-started.html)
- [Multiplatform libraries and expect/actual](https://kotlinlang.org/docs/multiplatform-connect-to-apis-on-specific-platforms.html)
- [Hierarchical project structure](https://kotlinlang.org/docs/multiplatform-dsl-reference.html)
- [Compose Multiplatform](https://www.jetbrains.com/lifecycle/compose-multiplatform/)
