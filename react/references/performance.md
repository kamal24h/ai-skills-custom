# React Performance

Official react.dev guidance for avoiding wasted renders and shipping less JavaScript.

## 1. Reduce Re-render Scope First

- Lift state down / push components up: move `useState` into the smallest subtree that needs it; extract static sections above the stateful part so they don't re-execute.
- Pass components as `children`/props — element identity stays stable and the parent's re-render skips them.
- Memoize only measured hotspots: `memo(Component)` + stable props (`useCallback`/`useMemo`) is a pair; memoizing a component while passing fresh object/function props does nothing.

```tsx
// ✅ children escape the counter's re-renders
function Page() {
  return (
    <Counter />
  );
}

function Counter() {
  const [n, setN] = useState(0);
  return (
    <>
      <button onClick={() => setN(n + 1)}>{n}</button>
      <HeavyTree />   {/* defined outside — same element reference */}
    </>
  );
}
```

## 2. Referential Stability

| Problem | Fix |
|---|---|
| New object/array prop each render | `useMemo(() => build(), [deps])` or hoist the constant |
| New callback prop each render | `useCallback` at the source, or pass through context with split values |
| Expensive computation per render | `useMemo` — but measure first; most computations are cheap |

## 3. Bundle and Load

- Code-split routes and heavy widgets with `React.lazy` + `<Suspense fallback>` (client-side trees).
- Virtualize very long lists (`List`/windowing) instead of rendering thousands of rows.
- Images: explicit dimensions, lazy loading below the fold, modern formats.

## 4. Measure Before Optimizing

- React DevTools **Profiler**: record an interaction, sort by "why did this render", look for commits where props didn't change.
- StrictMode double-invocations are dev-only noise, not production costs.

## Sources

- [React — Escape Hatches / Performance Overview](https://react.dev/learn/render-and-commit)
- [React — memo](https://react.dev/reference/react/memo)
- [React — useMemo](https://react.dev/reference/react/useMemo)
- [React — lazy](https://react.dev/reference/react/lazy)
