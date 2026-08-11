# AI Skills & Agents

A collection of specialized expert skills designed for AI coding agents. Includes structured rules, hook references, and best practices across multiple domains.

**Contents:** 20 expert skills · 38 specialized agent personas.

## Expert Skills

### Analysis Skills

| Skill | Description | Personas |
| :--- | :--- | :--- |
| **Architecture Advisor** | Analyzes project architecture, detects tech stack, reports strengths and gaps. | `arch-php-pro`, `arch-node-pro`, `arch-react-pro`, `arch-javascript-pro`, `arch-golang-pro`, `arch-kotlin-pro`, `arch-swift-pro`, `arch-swiftui-pro` |
| **Code Standards** | Universal code design and clean code principles. | SOLID, KISS, YAGNI, DRY, TDA, Testability, Complexity, Naming conventions. |

### Language & Framework Skills

Each implementation skill is paired with a dedicated testing skill where one exists.

| Skill | Tester Skill | Description | Key Focus Areas |
| :--- | :--- | :--- | :--- |
| **Go / Golang** | **Go Tester** | Modern Go development practices and idioms. | Package design, concurrency, error handling, performance, observability, toolchain conventions. |
| **JavaScript / TypeScript** | *(built-in `js-test-pro`)* | Modern JS/TS for backend and advanced logic. | Node.js, Type systems, TS migration/interop, Runtime validation (Zod/io-ts), Backend architecture. |
| **Kotlin** | **Kotlin Tester** | Kotlin for Android and Kotlin Multiplatform. | Coroutines/Flow, Clean Architecture, Jetpack Compose, Material Design 3, Hilt/Koin, Room, Gradle version catalogs. |
| **Laravel** | *(built-in Pest/PHPUnit)* | Comprehensive Laravel 13 development. | Eloquent, Database optimization, Caching, OWASP security, Inertia.js. |
| **PHP** | **PHPUnit** | Modern PHP 8.x patterns and PSR standards. | Type safety, PHP 8.4+ features, Enums, `declare(strict_types=1)`, Readonly, PSR-12, SOLID. |
| **SwiftUI** | **SwiftUI Tester** | SwiftUI for iOS/macOS with Swift 6.3+ concurrency. | View composition, state management, `@Observable`, actors/Sendable, SwiftData, HIG compliance, Figma → SwiftUI. |
| **Vue.js** | **Vue.js Tester** | Modern Vue 3 application development. | Composition API, `<script setup>`, reactivity, composables, Pinia, Vue Router, VueUse, SSR/hydration, Vite. |

### Testing Skills

| Skill | Description | Key Focus Areas |
| :--- | :--- | :--- |
| **Go Tester** | Expert guidance for Go testing. | Table-driven tests, parallelism, mocking boundaries, goleak, integration tags, fuzzing, benchmarks. |
| **Kotlin Tester** | Kotlin/Android/KMP testing. | JUnit 5, Kotest, MockK, Coroutines Test, Turbine, Espresso, Compose Testing, UIAutomator, Kover. |
| **PHPUnit** | Expert guidance for PHP testing. | AAA pattern, Framework-aware testing, Snapshot testing, CI/CD, Test isolation. |
| **SwiftUI Tester** | Swift Testing and XCTest for SwiftUI apps. | `#expect`/`#require`, `@Test`/`@Suite`, async testing, mocking, XCTest migration. |
| **Vue.js Tester** | Expert guidance for Vue 3 testing. | Vitest, Vue Test Utils, Testing Library, MSW, Pinia/router testing, Browser Mode, Playwright, coverage. |

### Platform & Infrastructure Skills

| Skill | Description | Key Focus Areas |
| :--- | :--- | :--- |
| **API Design Patterns** | RESTful API design and best practices. | Resource design, Error handling (RFC 7807), Security, Pagination, gRPC, Versioning. |
| **Docker** | Unified Docker and Docker Compose skill. | Dockerfiles, BuildKit, multi-stage builds, Compose services, networking, storage, security hardening, CI/CD, troubleshooting. |
| **Microservices** | Distributed systems patterns (PHP & TS). | Service boundaries, Data consistency (Saga/CQRS), Resilience, Observability, Idempotency. |
| **SQL Expert** | Database design, queries, and optimization. | PostgreSQL/MySQL/SQLite/SQL Server, JSON/Full-text, Connection pooling, CTEs, Window functions. |

### Domain Skills

| Skill | Description | Key Focus Areas |
| :--- | :--- | :--- |
| **WordPress** | WordPress plugin/theme/backend development. | Block editor, Plugin architecture, REST API, Performance, WP-CLI, Theme dev, Hook reference (2672 hooks). |
| **WooCommerce** | WooCommerce development extending WordPress. | Products, Orders, Cart/Checkout, Payments, Shipping, Emails, REST API, Admin, Hook reference (2723 hooks). |

## Agent Index

All agents defined in this repository:

| Agent | Skill | Role |
| :--- | :--- | :--- |
| `arch-php-pro` | Architecture Advisor | PHP/Laravel/Symfony/WordPress architecture analysis |
| `arch-node-pro` | Architecture Advisor | Node.js backend architecture analysis |
| `arch-react-pro` | Architecture Advisor | React/Next.js/Remix architecture analysis |
| `arch-javascript-pro` | Architecture Advisor | Vanilla JS / browser JS architecture analysis |
| `arch-golang-pro` | Architecture Advisor | Go service and package architecture analysis |
| `arch-kotlin-pro` | Architecture Advisor | Kotlin/Android/KMP architecture analysis |
| `arch-swift-pro` | Architecture Advisor | Swift/iOS/macOS architecture analysis |
| `arch-swiftui-pro` | Architecture Advisor | SwiftUI app architecture analysis |
| `api-design-pro` | API Design Patterns | REST/GraphQL/gRPC API design |
| `code-standards-pro` | Code Standards | SOLID, Clean Code, refactoring guidance |
| `docker-pro` | Docker | Dockerfile/Compose authoring, hardening, troubleshooting, CI/CD |
| `golang-pro` | Go / Golang | Idiomatic Go, concurrency, performance, package/API design |
| `golang-tester-pro` | Go Tester | Go testing, table-driven suites, mocks, benchmarks, fuzzing |
| `javascript-pro` | JavaScript | Modern JS, Node.js, async patterns |
| `typescript-pro` | JavaScript | Advanced TypeScript, type systems |
| `js-test-pro` | JavaScript | Vitest/Jest testing for JS/TS code |
| `kotlin-pro` | Kotlin | Compose UI, Material Design 3, state management, accessibility |
| `kotlin-coroutines-pro` | Kotlin | Structured concurrency, Flow, StateFlow, error handling |
| `kotlin-conventions-pro` | Kotlin | Idiomatic Kotlin, null safety, DSL builders, collections |
| `kotlin-build-pro` | Kotlin | Gradle Kotlin DSL, Version Catalogs, Convention Plugins, CI/CD |
| `kotlin-tester-pro` | Kotlin Tester | JUnit/Kotest, MockK, Coroutines Test, Espresso, Compose Testing |
| `laravel-pro` | Laravel | Laravel 13 implementation |
| `microservices-pro` | Microservices | Distributed systems design |
| `php-pro` | PHP | Modern PHP 8.x implementation |
| `phpunit-pro` | PHPUnit | PHP testing (PHPUnit, Pest) |
| `sql-pro` | SQL Expert | Query design and optimization |
| `swiftui-pro` | SwiftUI | View composition, state, animations, layout, HIG compliance |
| `concurrency-pro` | SwiftUI | Actor isolation, task structure, cancellation, Sendable correctness |
| `swiftdata-pro` | SwiftUI | Model design, relationships, predicates, migration safety |
| `figma-swiftui` | SwiftUI | Figma design → production SwiftUI views (Figma MCP) |
| `swiftui-tester-pro` | SwiftUI Tester | Swift Testing, XCTest, async testing, mocking, migration |
| `vue-pro` | Vue.js | SFC structure, component design, templates, built-ins, accessibility |
| `vue-reactivity-pro` | Vue.js | Reactivity primitives, watchers, effect scope, composable API design |
| `vue-state-pro` | Vue.js | Pinia stores, state boundaries, Vue Router 4, SSR-safe state |
| `vue-build-pro` | Vue.js | Vite, vue-tsc, TypeScript contracts, ESLint, SSR/Nuxt config |
| `vue-tester-pro` | Vue.js Tester | Vitest, VTU, MSW, Pinia/router tests, Browser Mode, Playwright |
| `wordpress-pro` | WordPress | WordPress development |
| `woocommerce-pro` | WooCommerce | WooCommerce development |

## How It Works

### Skill Structure

Each skill directory follows a consistent structure:
- **`SKILL.md`**: Entry point with core directives, a category index mapping tasks to references, a rule index, and a validation checklist.
- **`rules/`**: Actionable rules in `Context` / `Rule` / `Avoid` form, each with a stable rule id (e.g. `rx-computed-pure`). Two layouts are in use — one file per rule (`php`, `laravel`, `golang`, `javascript`, `wordpress`, …) or a single consolidated directives file (`kotlin`, `swiftui`, `vuejs` and their testers).
- **`references/`**: Detailed documentation, deep-dives, and hook references.
- **`agents/`**: Specialized system prompts for different roles within the skill.

`rules/` and `references/` are optional — `code-standards`, `phpunit`, and `sql-expert` carry no `rules/`; `javascript` and `php` keep everything in `rules/`.

Rule ids are stable identifiers — cite them in reviews (`rx-computed-pure`, `coro-no-globalscope`, `test-no-snapshot-only`) so feedback is traceable back to the source rule.

### Skill Inventory

| Skill | Agents | Rules | References |
| :--- | ---: | ---: | ---: |
| `api-design-patterns` | 1 | 40 | 7 |
| `architecture-advisor` | 8 | 27 | 10 |
| `code-standards` | 1 | — | 5 |
| `docker` | 1 | 15 | 86 |
| `golang` | 1 | 33 | 20 |
| `golang-tester` | 1 | 8 | 7 |
| `javascript` | 3 | 45 | — |
| `kotlin` | 4 | consolidated | 16 |
| `kotlin-tester` | 1 | consolidated | 11 |
| `laravel` | 1 | 98 | 9 |
| `microservices` | 1 | 29 | 7 |
| `php` | 1 | 53 | — |
| `phpunit` | 1 | — | 3 |
| `sql-expert` | 1 | — | 5 |
| `swiftui` | 4 | consolidated | 15 |
| `swiftui-tester` | 1 | consolidated | 3 |
| `vuejs` | 4 | consolidated | 17 |
| `vuejs-tester` | 1 | consolidated | 12 |
| `wordpress` | 1 | 28 | 24 |
| `woocommerce` | 1 | 14 | 23 |

### Hook References (WordPress & WooCommerce)

Hook references are organized by domain in `references/hooks/`:
- **WordPress**: 20 files (10 action + 10 filter categories, 2672 non-deprecated hooks)
- **WooCommerce**: 22 files (11 action + 11 filter categories, 2723 hooks)
- **Variable hooks**: Dynamic hook patterns documented in `references/variable-hooks.md`

## Usage

### For Users
- Ask for an **architecture analysis** (e.g., "Review this project's architecture using the Architecture Advisor").
- Ask for a **code review** based on a specific skill (e.g., "Review this PHP code using the PHP skill").
- Request a **new feature** following specific standards (e.g., "Design a REST API endpoint following the API Design Patterns skill").
- Use for **debugging** (e.g., "Explain why this SQL query is slow using the SQL Expert skill").

### For AI Agents
- Proactively load the relevant `SKILL.md` when a task matches its description.
- Load only the references named by the skill's category index — do not read the whole `references/` directory.
- **Separation of Concerns (Mandatory):** Implementation agents (e.g., `golang-pro`, `typescript-pro`, `laravel-pro`, `kotlin-pro`, `swiftui-pro`, `vue-pro`) MUST NOT write tests. Delegate to the matching tester agent.
- Reference specific rules in `rules/*.md` for concrete, example-backed feedback.
- Use `references/*.md` for deeper understanding of patterns or hook lookups.

## Agent Delegation Flow

To maintain high specialization and context efficiency, follow this delegation pattern:

1. **Architecture Analysis:** Use `architecture-advisor` (routes to the correct language persona automatically).
2. **Implementation:** Use the specific `<domain>-pro` agent (e.g., `laravel-pro`, `typescript-pro`, `vue-pro`).
3. **Testing:** Never combine implementation and testing in a single agent call. Route to the matching tester:

| Stack | Implementation | Testing |
| :--- | :--- | :--- |
| Go | `golang-pro` | `golang-tester-pro` |
| JavaScript / TypeScript | `javascript-pro`, `typescript-pro` | `js-test-pro` |
| Kotlin / Android / KMP | `kotlin-pro` (+ specialists) | `kotlin-tester-pro` |
| PHP / Laravel | `php-pro`, `laravel-pro` | `phpunit-pro` |
| SwiftUI / iOS | `swiftui-pro` (+ specialists) | `swiftui-tester-pro` |
| Vue.js | `vue-pro` (+ specialists) | `vue-tester-pro` |

## Scope

- **Covered**: Best practices, modern syntax (Go 1.21+, PHP 8.4+, TS 5.x, Kotlin 2.x, Swift 6.3+, Vue 3.5, Laravel 13, WordPress 6.9+, WooCommerce 9.6+), containerization (Docker / Compose), industry-standard design patterns, comprehensive hook references.
- **Not Covered**: Project-specific business logic, legacy framework versions, or non-technical project management.
