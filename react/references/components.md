# React Component Patterns

Official react.dev guidance for component structure, props, and composition.

## 1. Component Design

- **Pure render:** a component renders the same output given the same inputs — no side effects in `body` (JSX function), mutations of module state, or writes during render.
- **One concern per component:** extract when JSX nests past ~2 levels of layout logic or when a chunk has its own state.
- **Never define components inside components** — the inner identity changes every parent render, remounting children and losing their state.

```tsx
// ❌ Remounts on every Parent render
function Parent() {
  function Row() { return <li>…</li>; }
  return <ul>{items.map(i => <Row key={i.id} />)}</ul>;
}

// ✅ Sibling definition, stable identity
function Row({ item }: { item: Item }) { return <li>{item.label}</li>; }
```

## 2. Props

- Read-only by contract: never mutate `props`, never mirror them into state (`useState(props.value)` freezes the initial value).
- Children composition beats prop drilling: `<Card><Card.Title/><CardBody>` passes elements instead of config flags.
- Booleans read as predicates; callbacks as `on*`; keep prop names domain-meaningful (`isSubmittable`, not `flag1`).

## 3. Conditional Rendering and Lists

- Prefer early returns and `{cond && <X/>}` / ternaries over hiding with CSS when content must not mount.
- Keys are identities: stable DB ids; index keys only for static, never-reordered lists. Index keys on dynamic lists cause state bleed between rows.

## 4. State Placement

| State kind | Home |
|---|---|
| Local UI (input value, toggle) | `useState` in the leaf component |
| Shared by siblings | Lift to closest common parent |
| Cross-tree theme/session/user | Context provider or external store |
| Server data | Framework cache layer (React Query/SWR/RSC) |

## 5. Rendering Models (awareness)

- **Client Components** (`'use client'`): interactivity, browser APIs.
- **Server Components** (default under RSC frameworks): zero-bundle data rendering, no state/effects; pass serializable props down to client islands.
- Choose per component, not per app — interactive leaves stay client-side.

## Sources

- [React — Your First Component](https://react.dev/learn/your-first-component)
- [React — Keeping Components Pure](https://react.dev/learn/keeping-components-pure)
- [React — Passing Props](https://react.dev/learn/passing-props-to-a-component)
- [React — Rendering Lists](https://react.dev/learn/rendering-lists)
- [React Server Components](https://react.dev/reference/rsc/server-components)
