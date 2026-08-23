# Go Naming Conventions

From Effective Go and the official Go Style Guidelines (Google). Go's central rule: **MixedCaps — never underscores** for multi-word names.

## Element table

| Element | Convention | Example |
|---|---|---|
| Multi-word identifier | MixedCaps; no snake_case, ever | `parseRequest` / `ParseRequest` |
| Exported (= public) | UpperCamelCase | `func NewServer()` |
| Unexported (= package-private) | lowerCamelCase | `func normalizePath()` |
| Package name | short, all lowercase, one word, **no** under_scores or mixedCaps, usually singular | `strconv`, `http`, not `util`, `common`, `types` |
| Interface (single method) | method name + `-er` suffix | `Reader`, `Writer`, `Formatter` |
| Getter | NO `Get` prefix — noun matches field | `obj.Owner()`, setter `obj.SetOwner()` |
| Error variable | `err` | `if err != nil { … }` |
| Error strings | lowercase, no trailing punctuation, wrap with `%w` | `fmt.Errorf("cache expired: %w", err)` |
| Constant | MixedCaps (NOT SCREAMING_SNAKE) | `const MaxRetries = 5` |
| Receiver name | short, consistent across all methods of the type | `(c *Client)` in every Client method |
| Test file / function | `_test.go`; `TestXxx`, benchmark `BenchmarkXxx`, example `ExampleXxx` | `server_test.go` |
| Initialisms | uniform case, no mixed casing | `userID`, `ServeHTTP`, `xmlHTTP` (not `userId`, `serveHttp`) |

## Rules worth remembering

- Capitalisation IS the visibility modifier — there is no `public`/`private` keyword. Rename to export.
- Name length scales with scope: short loop names fine; package-level names carry more weight ("the package name is the default name for all its identifiers" — prefer `http.Get`, not `http.GetRequest`).
- Avoid stutter: type `Server`, constructor `New()` inside package `server`, so callers write `server.New()` — not `server.NewServer()`.
- Don't reuse built-in names (`len`, `cap`, `copy`, `new`, `make`, `min`, `max`) as identifiers.

## Sources

- [Effective Go — Names](https://go.dev/doc/effective_go#names)
- [Google Go Style Guide — Naming](https://google.github.io/styleguide/go/decisions#naming)
- [Go Code Review Comments](https://go.dev/wiki/CodeReviewComments)
