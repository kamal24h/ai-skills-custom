# AI Skills & Agents

A collection of specialized expert skills for AI coding agents. Each skill bundles rules, deep-dive references, and agent personas for a specific technology domain.

**22 skills · 42+ agent personas.**

## Skills

### Analysis & Standards

| Skill | What it can do | What it does NOT do |
|-------|----------------|---------------------|
| **architecture-advisor** | Detects the tech stack, routes to a language persona (`arch-php-pro`, `arch-node-pro`, …), and produces an evidence-based architecture report with prioritized recommendations. | Does not refactor code or make changes — it reports only. |
| **code-standards** | Applies SOLID, KISS, YAGNI, DRY, TDA and pragmatic design principles to any code review or design task; includes the official default **naming conventions per stack** (WordPress, Laravel, Symfony, PHP/PSR, Go, Kotlin, Swift/SwiftUI, React, Vue, JS/TS, Python) sourced from each stack's style guide. | Not language-specific beyond naming tables; pair it with the relevant language skill for implementation guidance. |
| **ui-ux** | Framework-agnostic UI/UX design, modern CSS, semantic HTML, typography, 3-tier design tokens (OKLCH), motion, surfaces/elevation, WCAG 2.2 accessibility, 5-dimension technical audits, UX copywriting clarity, the Craft Floor, Core Web Vitals, real content design, interface affordances, and modern CSS architecture (@layer). Routes to `ui-designer-pro` and `ux-designer-pro`. | Not tied to specific frameworks or utility libraries (Bootstrap, Tailwind, React, etc.); focused on native web standards and design fundamentals. |

### Language & Framework Implementation

| Skill | Purpose |
|-------|---------|
| **golang** | Idiomatic modern Go: concurrency, error handling, performance, toolchain (Go 1.21→1.26 features). |
| **javascript** | Node.js backends, advanced TypeScript type systems, ES6+ patterns, JS/TS testing (Vitest/Jest). React components live in the `react` skill. |
| **kotlin** | Kotlin 2.x for Android and KMP: coroutines/Flow, Clean Architecture, Compose, Material 3, Hilt/Koin, Room. |
| **laravel** | Laravel 13 development: Eloquent, queues, validation, security, testing with Pest/PHPUnit, Inertia.js. |
| **php** | Modern PHP 8.x patterns and PSR standards — type safety, enums, readonly, property hooks (8.0–8.5), security. |
| **react** | React component/hook development and Testing Library tests, based on official react.dev guidance. |
| **swiftui** | SwiftUI for iOS/macOS: `@Observable`, Swift 6.x concurrency, SwiftData, navigation, HIG-compliant design. |
| **vuejs** | Vue 3.5+ applications: Composition API, reactivity, Pinia, Router, composables, SSR/hydration, Vite. |

### Testing (pairs with implementation skills)

| Skill | Pairs with | Purpose |
|-------|-----------|---------|
| **golang-tester** | golang | Table-driven tests, mocking, goleak, integration tags, benchmarks, fuzzing. |
| **kotlin-tester** | kotlin | JUnit 5, Kotest, MockK, Turbine, Compose Testing, Espresso, coverage/Kover. |
| **phpunit** | php | PHPUnit 12 on PHP 8.3+: attributes-only metadata, test doubles, isolation, strict config. |
| **swiftui-tester** | swiftui | Swift Testing + XCTest: `#expect`/`@Test`, mocking via protocol DI, coverage & CI. |
| **vuejs-tester** | vuejs | Vitest, Vue Test Utils, Testing Library, MSW, Browser Mode, Playwright E2E. |

> **Separation of concerns:** implementation agents do not write tests; route test work to the matching tester skill/agent.

### Platform & Infrastructure

| Skill | Can help with | Out of scope |
|-------|--------------|--------------|
| **api-design-patterns** | REST resource design, error envelopes (RFC 9457-aware), versioning/deprecation, pagination, API security, OpenAPI docs; GraphQL/gRPC selection guidance. | Protocol client libraries' internals. |
| **docker** | Dockerfiles, BuildKit mounts/caches, multi-stage builds, Compose services/networks/volumes/secrets, hardening, CI/CD, troubleshooting. Engine 29.x baseline. | Kubernetes orchestration beyond deployment concerns. |
| **microservices** | Service boundaries, saga/CQRS/event sourcing, transactional outbox, schema evolution, resilience patterns, observability, gateways/mesh — in PHP and TypeScript. | Single-service application design. |
| **sql-expert** | Query writing and optimization (CTEs, window functions), indexing, schema design, safe migrations across PostgreSQL 17 / MySQL 8.4 / SQL Server 2022 / SQLite (engine specifics included). | ORM-specific API questions (see language skills). |

### WordPress Ecosystem

| Skill | Purpose |
|-------|---------|
| **wordpress** | Plugin/theme/backend development: block editor, plugin architecture, REST API, WP-CLI, coding standards, plus hook references extracted from core source (params, since versions). |
| **woocommerce** | Extends `wordpress` with WooCommerce-specific patterns: products, orders, checkout, payments, shipping, emails, REST API, HPOS awareness, plus 2,600+ core hooks sourced from the WooCommerce plugin. |

## How It Works

Each skill directory follows the same shape:

```
<skill>/
├── SKILL.md          # Entry point: triggers, category index, rule index, validation checklist
├── rules/            # Actionable directives (bad/good examples), one file per topic or one consolidated file
├── references/       # Deep dives; every file ends with ## Sources linking canonical documentation
└── agents/           # Specialized personas (e.g. golang-pro, kotlin-tester-pro)
```

- Agents load only the `SKILL.md`, then only the references named by its category index.
- Rules are cited by heading/id in review feedback so comments trace back to their source.

## Usage

**For users** — ask naturally:
- "Review this project's architecture" → architecture-advisor
- "Review this Go test suite" → golang-tester
- "Design a REST endpoint for orders" → api-design-patterns
- "Audit this form's accessibility and contrast" → ui-ux
- "Why is this query slow?" → sql-expert

**For AI agents:**
1. Proactively load the matching `SKILL.md` when a task matches its description triggers.
2. Load only the references named by the category index — never the whole `references/` tree.
3. Never combine implementation and testing in one pass; delegate to the tester counterpart.

## Scope

- **Covered:** best practices, current major versions of the listed technologies, industry-standard design patterns, official naming standards, curated hook references.
- **Not covered:** project-specific business logic, legacy framework versions, non-technical project management.

Version baselines are stated inside each skill's `SKILL.md`; always detect the project's actual versions first.
