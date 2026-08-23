# JavaScript / TypeScript Naming Conventions

From the Google JavaScript Style Guide and the official TypeScript Handbook Do's and Don'ts. Where the two ecosystems differ, both are listed.

## Element table

| Element | Convention | Example |
|---|---|---|
| Local variable / function | camelCase | `parseChunk()` |
| Module-level constant | SCREAMING_SNAKE_CASE (Google: CONSTANT_CASE) | `const MAX_RETRIES = 3` |
| Class | PascalCase | `EventBus` |
| Interface / type alias | PascalCase — **no `I` prefix** (official TS recommendation) | `interface UserRecord {}`, not `IUserRecord` |
| Enum | PascalCase type, PascalCase members (TS docs style) | `enum InvoiceStatus { Paid }` |
| Type parameter | single uppercase letter or UpperCamelCase | `<T>`, `<Key>` |
| File name | all lowercase, hyphens allowed, no underscores (Google); kebab-case dominant in Node *(de-facto)* | `invoice-service.ts` |
| Private field | `#` native private over `_` prefix (modern) | `#cache = new Map()` |
| Exported symbol | named exports preferred; re-exported API stays stable | `export function parse() {}` |
| Boolean variable/function | predicate reading | `isReady`, `hasPendingFlush()` |
| Event constant / custom event | camelCase string or SCREAMING_SNAKE for module constants | `'order:updated'`, `const EVENT_ORDER_UPDATED` |
| Test file | subject + `.test.` / `.spec.` *(framework convention)* | `invoice-service.test.ts` |

## Rules worth remembering

- The TypeScript team explicitly recommends **against** `I`-prefixed interfaces and `_`-prefixed private members in modern code.
- Acronyms stay uniformly cased within a word (`loadHTTPResponse`, not `loadHttpResponse`) per Google style.
- Default exports hide names at import sites — prefer named exports so the declared name is the contract.

## Sources

- [Google JavaScript Style Guide — Naming](https://google.github.io/styleguide/jsguide.html#5-naming)
- [TypeScript Do's and Don'ts](https://www.typescriptlang.org/docs/handbook/declaration-files/do-s-and-don-ts.html)
- [TypeScript Handbook — Enums](https://www.typescriptlang.org/docs/handbook/enums.html)
