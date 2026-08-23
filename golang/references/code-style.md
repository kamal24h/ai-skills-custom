# Go Code Style

Style rules that require human judgment — linters handle formatting, this reference handles clarity. Covers control flow, variable declarations, function design, string handling, and code organisation.

## When to Load

- Reviewing code clarity or structure
- Writing new functions or packages
- Deciding between variable declaration forms
- Choosing between if-else chains and switch
- Designing function signatures

## Rule Categories by Priority

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | Control Flow | HIGH | `style-early-return`, `style-no-else`, `style-switch-over-if`, `style-complex-conditions` |
| 2 | Variable Declarations | HIGH | `idiomatic-var-declarations`, `idiomatic-slice-map-init`, `idiomatic-struct-init` |
| 3 | Function Design | HIGH | `style-function-design`, `style-value-vs-pointer` |
| 4 | String & Type Handling | MEDIUM | `style-string-handling`, `style-line-breaking` |
| 5 | File Organisation | MEDIUM | `idiomatic-file-organization`, `idiomatic-blank-imports` |

## Rule Index

### 1. Control Flow (HIGH)

- [`style-early-return`](../rules/style-early-return.md) — Handle errors and edge cases first; keep happy path at minimal indentation
- [`style-no-else`](../rules/style-no-else.md) — Drop `else` when the `if` body ends with `return`/`break`/`continue`
- [`style-switch-over-if`](../rules/style-switch-over-if.md) — Prefer `switch` when comparing the same variable multiple times
- [`style-complex-conditions`](../rules/style-complex-conditions.md) — Extract 3+ operand conditions into named booleans

### 2. Variable Declarations (HIGH)

- [`idiomatic-var-declarations`](../rules/idiomatic-var-declarations.md) — Use `:=` for non-zero values, `var` for zero-value initialization; the form signals intent
- [`idiomatic-slice-map-init`](../rules/idiomatic-slice-map-init.md) — Always initialise slices/maps explicitly; nil maps panic on write, nil slices serialize to JSON `null`
- [`idiomatic-struct-init`](../rules/idiomatic-struct-init.md) — Always use named fields in composite literals

### 3. Function Design (HIGH)

- [`style-function-design`](../rules/style-function-design.md) — Short focused functions; ≤4 params; `context.Context` first
- [`style-value-vs-pointer`](../rules/style-value-vs-pointer.md) — Pass small types by value; use pointers for mutation, large structs, or when nil is meaningful

### 4. String & Type Handling (MEDIUM)

- [`style-string-handling`](../rules/style-string-handling.md) — `strconv` for simple conversions, `fmt.Sprintf` for formatting, `strings.Builder` in loops
- [`style-line-breaking`](../rules/style-line-breaking.md) — Break lines at semantic boundaries; 4+ arguments → one per line

### 5. File Organisation (MEDIUM)

- [`idiomatic-file-organization`](../rules/idiomatic-file-organization.md) — Group related declarations; one primary type per file
- [`idiomatic-blank-imports`](../rules/idiomatic-blank-imports.md) — Restrict `_` imports to `main` and test packages

## Philosophy

- **"A little copying is better than a little dependency"** — don't add a package for one utility function
- **"Reflection is never clear"** — avoid `reflect` unless truly necessary
- **Don't abstract prematurely** — extract when the pattern is stable, not on first use
- **Minimise public surface** — every exported name is a commitment; unexport aggressively
- **Use `slices` and `maps` standard packages** (Go 1.21+) for collection operations

## Enforce with Linters

Many rules here are enforceable automatically:

| Tool | What it catches |
|------|----------------|
| `gofmt` / `gofumpt` | Formatting |
| `goimports` | Import organisation |
| `gocritic` | Style issues, unnecessary else |
| `revive` | Naming, exported docs, blank imports |
| `wsl` | Whitespace lint |
| `golangci-lint` | Aggregates all of the above |

```bash
golangci-lint run ./...
```
\
## Sources\
\
- [Effective Go](https://go.dev/doc/effective_go)\
- [Google Go Style Guide](https://google.github.io/styleguide/go/)\
- [Go Code Review Comments](https://go.dev/wiki/CodeReviewComments)
