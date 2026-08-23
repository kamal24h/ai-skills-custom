# React Hooks & State

Official react.dev guidance on the hook set, state placement, and effect discipline.

## 1. The Hook Set at a Glance

| Hook | Use for |
|---|---|
| `useState` | Local interactive state |
| `useReducer` | Multi-field transitions with a state machine shape |
| `useContext` | Reading ambient values (theme, session) without prop drilling |
| `useRef` / `useImperativeHandle` | Non-reactive mutable values and DOM handles |
| `useEffect` | Synchronizing with external systems only |
| `useLayoutEffect` | Measure/mutate DOM before paint (rare) |
| `useMemo` / `useCallback` / `memo` | Referential stability for expensive work or memoized children |
| `useSyncExternalStore` | Bridging external stores (Zustand, browser APIs) |

## 2. Rules of Hooks (hard rules)

- Call only at the top level of a component or custom hook — never in conditions, loops, nested functions, or after early returns.
- Lint enforcement: `eslint-plugin-react-hooks` (`rules-of-hooks`, `exhaustive-deps`) is non-optional in review.

## 3. Effect Discipline — You Might Not Need an Effect

Replace the three classic effect abuses:

```tsx
// ❌ Derived state via effect
const [full, setFull] = useState('');
useEffect(() => { setFull(first + ' ' + last); }, [first, last]);

// ✅ Derive during render
const full = first + ' ' + last;

// ❌ Event logic via effect
useEffect(() => { if (submitted) analytics.track(); }, [submitted]);

// ✅ Track in the event handler
function handleSubmit() { analytics.track(); }

// ❌ Fetch-in-effect with race conditions
useEffect(() => { fetch(url).then(setData); }, [url]);
```

Effects remain correct for: subscribing to external stores/websockets, imperative DOM integrations, analytics page views, and syncing React state to non-React widgets. Always return cleanup for subscriptions; make effects idempotent under double-invocation (StrictMode).

## 4. Custom Hooks

- Extract when two components share stateful *logic*; name `use*`; they compose hooks, not markup.
- Keep one concern per hook (`useLocalStorage(key)`), return tuples for paired APIs or objects past 3 values.

```tsx
function useDebounced<T>(value: T, ms: number): T {
  const [debounced, setDebounced] = useState(value);
  useEffect(() => {
    const id = setTimeout(() => setDebounced(value), ms);
    return () => clearTimeout(id);   // cleanup is part of the contract
  }, [value, ms]);
  return debounced;
}
```

## Sources

- [React — Rules of Hooks](https://react.dev/reference/rules/rules-of-hooks)
- [React — You Might Not Need an Effect](https://react.dev/learn/you-might-not-need-an-effect)
- [React — Reusing Logic with Custom Hooks](https://react.dev/learn/reusing-logic-with-custom-hooks)
- [React — Managing State](https://react.dev/learn/managing-state)
