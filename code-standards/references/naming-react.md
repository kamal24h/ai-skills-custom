# React Naming Conventions

From the official React documentation rules plus ecosystem-wide lint defaults (eslint-plugin-react / react-hooks). Items marked *(de-facto)* are dominant community practice rather than documented React requirements.

## Element table

| Element | Convention | Example |
|---|---|---|
| Component | PascalCase function identifier | `function ProfileCard() {}` |
| Hook | `use` prefix, **mandatory** (Rules of Hooks — enforced by lint) | `useLocalStorage()` |
| Props | camelCase | `<UserCard userName={…} />` |
| Boolean prop | predicate reading | `isEnabled`, `showHeader` |
| Event handler prop | `on` prefix | `onSelect`, `onChange` |
| Internal handler function | `handle` prefix | `const handleSelect = …` |
| Context object / hook | PascalCase + `Context` suffix / `use` + noun | `ThemeContext`, `useTheme()` |
| State + setter pair | noun / `set` + capitalized noun | `[count, setCount] = useState(0)` |
| Custom hook file | matches hook name *(de-facto)* | `use-local-storage.ts` or `useLocalStorage.ts` |
| Component file | matches component in PascalCase, or `index.tsx` barrel *(de-facto; pick one per repo)* | `ProfileCard.tsx` |
| HOC (legacy) | `with` prefix *(de-facto)* | `withAuth(Component)` |
| Constants | SCREAMING_SNAKE at module scope *(JS base convention)* | `const MAX_RETRIES = 3` |

## Rules worth remembering

- Hooks are only callable from components/other hooks — the `use` prefix is how the linter tells them apart; a stateful function without it is a bug waiting to happen.
- Components must start uppercase: `<profileCard />` compiles as an HTML tag and silently renders nothing.
- Render-prop children and slot props follow the same camelCase rules as props.

## Sources

- [React — Your First Component](https://react.dev/learn/your-first-component)
- [React — Rules of Hooks](https://react.dev/reference/rules/rules-of-hooks)
- [React — Sharing Logic with Custom Hooks](https://react.dev/learn/reusing-logic-with-custom-hooks)
- [React — State: setter naming](https://react.dev/reference/react/useState)
