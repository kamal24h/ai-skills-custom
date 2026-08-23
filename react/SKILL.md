---
name: react
description: React component and hook development — component composition, state placement, custom hooks, performance (memo/lazy), Server Components awareness, and Testing Library patterns. Use when building or reviewing React components, writing custom hooks, or testing React UIs. Triggers on "React", "component", "useEffect", "custom hook", "JSX", "renderHook", "Testing Library".
model: inherit
---

# React Best Practices

Component and hook guidance for modern React (19+), based on the official react.dev documentation. Backend JS/TS patterns live in the `javascript` skill.

## Specialized Agents

| Agent | Role | Focus |
|-------|------|-------|
| **react-pro** | React Expert | Component design, hooks, state placement, rendering behavior. |

## When to Use

- Designing component structure, props, and composition
- Deciding where state lives (local vs lifted vs context vs store)
- Writing or reviewing custom hooks
- Fixing effect misuse (`useEffect` for data fetching, derived state, event logic)
- Testing components and hooks with Testing Library + Vitest/Jest

## Core Directives

### MUST DO

- Components are functions returning JSX in PascalCase; one concern per component
- Derive values during render instead of syncing state with effects
- Custom hooks are the reuse mechanism — `use*` prefix mandatory
- Keys are stable identities (`item.id`), never array indices in dynamic lists
- Test user-visible behavior via semantic queries (`getByRole`) — see [`rules/test-react-components`](rules/test-react-components.md)

### MUST NOT DO

- Call hooks conditionally or outside components/custom hooks (Rules of Hooks)
- Use effects for transformations that belong in render or event handlers
- Mutate props or read refs for rendering decisions (`ref.current` is not reactive)
- Define components inside other components (identity churn on every render)
- Shallow-render in tests — assert on what users see

## Category Index

| # | Category | Impact | Load when… | Reference | Rules |
|--:|----------|:------:|------------|-----------|:-----:|
| 1 | Component Patterns | HIGH | Composition, props design, conditional rendering, lists | [`references/components.md`](references/components.md) | — |
| 2 | Hooks & State | CRITICAL | useState/useReducer/useContext placement, custom hooks, effect rules | [`references/hooks.md`](references/hooks.md) | — |
| 3 | Performance | MEDIUM | Re-render storms, memoization boundaries, code splitting | [`references/performance.md`](references/performance.md) | — |
| 4 | Testing | HIGH | Component and hook tests with Testing Library | [`references/testing-react.md`](references/testing-react.md) | 2 |

## Rule Index

### Testing (`test-`) — HIGH
[`test-react-components`](rules/test-react-components.md) · [`test-react-hooks`](rules/test-react-hooks.md)

## Validation Checklist

- [ ] Every hook call is unconditional and top-level
- [ ] Derived data computed during render, not stored in extra state
- [ ] Effects only synchronize with external systems — no fetch-in-effect without an abstraction layer
- [ ] List keys stable and unique; no index keys on reorderable/dynamic rows
- [ ] State lives at the lowest common owner; context used for genuinely global values
- [ ] Custom hooks extracted when logic is reused across components
- [ ] Tests query by role/label and assert on behavior, not internals

## External References

- [React Documentation](https://react.dev/learn)
- [Rules of Hooks](https://react.dev/reference/rules/rules-of-hooks)
- [You Might Not Need an Effect](https://react.dev/learn/you-might-not-need-an-effect)
- [Testing Library — React](https://testing-library.com/docs/react-testing-library/intro/)
