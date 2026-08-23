# Testing React Components & Hooks

Testing Library + Vitest/Jest guidance; the concrete rules live in `rules/`.

## When to Load

- Writing component or hook tests
- Deciding what to assert (behavior vs internals)
- Migrating off enzyme/shallow rendering

## Rule Index

- [`test-react-components`](../rules/test-react-components.md) — Query by role/label, simulate real interactions, assert on behavior
- [`test-react-hooks`](../rules/test-react-hooks.md) — `renderHook` + `act`, direct `result.current` access, async updates

## The Testing Pyramid for React UIs

```
Many    unit tests      pure helpers, reducers, custom hooks via renderHook
Some    component tests user-visible behavior with Testing Library
Few     E2E tests       critical journeys in Playwright (browser mode)
```

## Practices That Keep Suites Green

- Wrap renders that need providers once: a `renderWithProviders(ui)` helper beats per-test boilerplate.
- Prefer `userEvent` over `fireEvent` when interaction realism matters (focus, keyboard, pointer sequences).
- Assert with `findBy*` for anything async — never `waitFor` around arbitrary sleeps.
- Mock the network at the boundary (MSW), not components' internals.

## Sources

- [Testing Library — React](https://testing-library.com/docs/react-testing-library/intro/)
- [Testing Library — Queries priority](https://testing-library.com/docs/queries/about/#priority)
- [React — Testing Recipes](https://react.dev/learn/testing)
