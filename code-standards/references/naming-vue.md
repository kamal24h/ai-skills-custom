# Vue Naming Conventions

From the official Vue.js Style Guide (Priority A = essential, B = strongly recommended) plus Pinia and composable conventions.

## Element table

| Element | Convention | Example |
|---|---|---|
| Component name | **multi-word mandatory** (Priority A) — never single-word | `TodoItem`, never `Todo` |
| SFC filename | PascalCase, matches component (Priority B strong) | `UserCard.vue` |
| Component usage in SFC templates | PascalCase (Priority B strong) | `<UserCard />` |
| Component usage in DOM templates | kebab-case (HTML is case-insensitive) | `<user-card>` |
| Prop declaration | camelCase; kebab-case attribute when used in-DOM | `props: { greetingText }` → `greeting-text="hi"` |
| Emits declaration | camelCase; template listener kebab-case for DOM compatibility | `emit('update:modelValue')` → `@update:model-value` |
| Composable | `use` + camelCase noun, one concern per composable | `useMouse()`, `useFetch()` |
| Composable file | same name as composable *(documented pattern)* | `composables/useMouse.js` |
| Pinia store id / hook | string id snake or camel; hook `use` + PascalCase + `Store` | `defineStore('cart', …)` → `useCartStore()` |
| Directive name | lowercase word(s), registered with prefix usage `v-focus` | `directives: { focus: {...} }` |
| Event payload type names | PascalCase | `interface CartChangedPayload {}` |

## Rules worth remembering

- Multi-word component names prevent collisions with existing/future HTML elements (`<item>` vs `<todo-item>`) — this is a Priority A rule, not a preference.
- Never use `data` as a prop/component name (reserved conflict patterns with HTML `data-*`).
- Self-closing components (`<UserCard />`) in SFCs signal no-content intent (Priority B).

## Sources

- [Vue Official Style Guide](https://vuejs.org/style-guide/)
- [Vue — Component Events (naming)](https://vuejs.org/guide/components/events.html)
- [Vue — Composables conventions](https://vuejs.org/guide/reusability/composables.html#conventions-and-best-practices)
- [Pinia — Define Stores](https://pinia.vuejs.org/core-concepts/define-stores.html)
