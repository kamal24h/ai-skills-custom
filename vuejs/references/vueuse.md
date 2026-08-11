# VueUse

A decision guide for [VueUse](https://vueuse.org/) composables. Check whether a VueUse function already solves the requirement **before** writing a custom composable — they are SSR-aware, auto-cleaning, and accept `MaybeRefOrGetter` inputs.

```bash
pnpm add @vueuse/core
```

## Invocation Policy

| Level | Meaning |
|---|---|
| **AUTO** | Use whenever it fits the requirement — part of `@vueuse/core`, no extra dependency. |
| **EXTERNAL** | Requires a peer dependency (`@vueuse/integrations`, `@vueuse/motion`, firebase, rxjs…). Use only if already installed; ask before adding. |
| **EXPLICIT_ONLY** | Use only when the user asks for it — non-obvious behavior or heavy trade-offs. |

Project instructions in `AGENTS.md`/`CLAUDE.md` override these defaults.

## Why Prefer VueUse Over Hand-Rolled Code

- Listeners, observers, and timers are disposed automatically via `tryOnScopeDispose`.
- SSR-safe: they no-op on the server and initialize on mount.
- Inputs accept value / ref / getter (`MaybeRefOrGetter`), so call sites stay flexible.
- Consistent return shapes (`{ x, isSupported, stop }`) across the library.

A hand-rolled `useWindowSize` that forgets `removeEventListener` or crashes during SSR is the default outcome; VueUse's does not.

## Function Catalog by Category

### State (AUTO)
`useStorage` · `useLocalStorage` · `useSessionStorage` · `useStorageAsync` · `useRefHistory` · `useManualRefHistory` · `useDebouncedRefHistory` · `useThrottledRefHistory` · `useLastChanged` · `useAsyncState` · `createGlobalState` · `createSharedComposable` · `createInjectionState` · `provideLocal` / `injectLocal`

> **SSR caution:** `createGlobalState` and `createSharedComposable` are module singletons. Never use them for per-user data in an SSR app — use `createInjectionState` or a per-request Pinia store.

### Elements (AUTO)
`useElementSize` · `useElementBounding` · `useElementVisibility` · `useIntersectionObserver` · `useResizeObserver` · `useMutationObserver` · `useWindowSize` · `useWindowScroll` · `useWindowFocus` · `useDocumentVisibility` · `useActiveElement` · `useMouseInElement` · `useDraggable` · `useDropZone` · `useParentElement`

### Browser (AUTO)
`useEventListener` · `useMediaQuery` · `useBreakpoints` · `useDark` · `useColorMode` · `usePreferredDark` · `usePreferredColorScheme` · `usePreferredReducedMotion` · `usePreferredLanguages` · `useClipboard` · `useClipboardItems` · `useFullscreen` · `useTitle` · `useFavicon` · `useUrlSearchParams` · `useCssVar` · `useStyleTag` · `useScriptTag` · `useFileDialog` · `useShare` · `useObjectUrl` · `useTextareaAutosize` · `usePermission` · `useWebNotification` · `useWebWorker` · `useVibrate` · `useWakeLock` · `useScreenOrientation` · `useScreenSafeArea` · `useSSRWidth`

### Sensors (AUTO)
`onClickOutside` · `onKeyStroke` · `onLongPress` · `onStartTyping` · `onElementRemoval` · `useMagicKeys` · `useKeyModifier` · `useMouse` · `useMousePressed` · `usePointer` · `usePointerSwipe` · `useSwipe` · `useScroll` · `useScrollLock` · `useInfiniteScroll` · `useFocus` · `useFocusWithin` · `useElementHover` · `useIdle` · `usePageLeave` · `useTextSelection` · `useGeolocation` · `useNetwork` · `useOnline` · `useBattery` · `useDevicesList` · `useUserMedia` · `useDisplayMedia` · `useSpeechRecognition` · `useSpeechSynthesis` · `useDeviceMotion` · `useDeviceOrientation` · `useDevicePixelRatio` · `useFps`

### Network (AUTO)
`useFetch` · `useWebSocket` · `useEventSource`

> `useFetch` is convenient for prototypes and simple cases. For a real app, prefer a typed API layer (see `architecture.md`) or a data-fetching library with caching and retries.

### Animation & Time (AUTO)
`useTransition` · `useAnimate` · `useRafFn` · `useInterval` · `useIntervalFn` · `useTimeout` · `useTimeoutFn` · `useTimestamp` · `useNow` · `useCountdown` · `useDateFormat` · `useTimeAgo` · `useTimeAgoIntl`

> `useTimeAgo` in SSR causes hydration mismatches — render an absolute date on the server and swap after mount.

### Component Utilities (AUTO)
`useVModel` · `useVModels` · `useVirtualList` · `useMounted` · `useCurrentElement` · `unrefElement` · `useTemplateRefsList` · `createReusableTemplate` · `createTemplatePromise` · `tryOnMounted` · `tryOnUnmounted` · `tryOnBeforeUnmount` · `tryOnScopeDispose` · `computedInject`

> `useVModel`/`useVModels` predate `defineModel`. In Vue 3.4+ prefer `defineModel`.

### Watch (AUTO)
`watchDebounced` · `watchThrottled` · `watchPausable` · `watchIgnorable` · `watchOnce` · `watchImmediate` · `watchDeep` · `watchArray` · `watchAtMost` · `watchTriggerable` · `watchWithFilter` · `whenever` · `until`

### Reactivity (AUTO)
`computedAsync` · `computedEager` · `computedWithControl` · `reactiveComputed` · `reactivePick` · `reactiveOmit` · `refDebounced` · `refThrottled` · `refAutoReset` · `refDefault` · `refManualReset` · `refWithControl` · `syncRef` · `syncRefs` · `extendRef` · `toReactive` · `reactify` · `createRef`

### Array (AUTO)
`useArrayFilter` · `useArrayMap` · `useArrayFind` · `useArrayFindLast` · `useArrayFindIndex` · `useArrayIncludes` · `useArraySome` · `useArrayEvery` · `useArrayReduce` · `useArrayUnique` · `useArrayDifference` · `useArrayJoin` · `useSorted`

> These are thin `computed` wrappers. A plain `computed(() => items.value.filter(...))` is equally good and has zero indirection — use the array helpers only when the extra `MaybeRefOrGetter` flexibility helps.

### Utilities (AUTO)
`useToggle` · `useCounter` · `useCycleList` · `useStepper` · `useDebounceFn` · `useThrottleFn` · `useMemoize` · `useCloned` · `usePrevious` · `useCached` · `useEventBus` · `useConfirmDialog` · `useOffsetPagination` · `useAsyncQueue` · `useTimeoutPoll` · `useSupported` · `useToNumber` · `useToString` · `isDefined` · `get` · `set` · `createEventHook` · `makeDestructurable`

### Add-on Packages (EXTERNAL — requires an extra dependency)
| Package | Provides |
|---|---|
| `@vueuse/integrations` | `useAxios`, `useCookies`, `useIDBKeyval`, `useFocusTrap`, `useQRCode`, `useJwt`, `useNProgress`, `useSortable`, `useDrauu`, `useChangeCase` |
| `@vueuse/router` | `useRouteParams`, `useRouteQuery`, `useRouteHash` |
| `@vueuse/math` | `useClamp`, `useSum`, `useAvg`, `useMin`, `useMax`, `useRound`, `useProjection`, `usePrecision`, `logicAnd`, `logicOr`, `logicNot` |
| `@vueuse/motion` | `useMotion`, `useSpring`, `useMotionTransitions` |
| `@vueuse/sound` | `useSound` |
| `@vueuse/head` | Document head management (superseded by `unhead` in most stacks) |
| `@vueuse/rxjs`, `@vueuse/firebase`, `@vueuse/electron`, `@vueuse/schema-org` | Domain integrations |

## Common Patterns

### Replace hand-rolled listeners

```ts
// ❌ manual, leak-prone, SSR-unsafe
onMounted(() => window.addEventListener('resize', onResize))
onUnmounted(() => window.removeEventListener('resize', onResize))

// ✅
useEventListener(window, 'resize', onResize)   // auto-cleanup, SSR-safe
const { width, height } = useWindowSize()
```

### Persistent, reactive storage

```ts
const settings = useLocalStorage('app:settings', { density: 'comfortable', locale: 'tr' })
settings.value.density = 'compact'   // written through automatically
```

Never store tokens or PII here — `localStorage` is readable by any injected script.

### Responsive breakpoints

```ts
import { breakpointsTailwind, useBreakpoints } from '@vueuse/core'

const bp = useBreakpoints(breakpointsTailwind)
const isMobile = bp.smaller('md')
const isDesktop = bp.greaterOrEqual('lg')
```

Pass `useSSRWidth` (or Nuxt's SSR width option) so the server render matches the expected viewport class.

### Debounce and throttle

```ts
const search = useDebounceFn(runSearch, 300)
const onScroll = useThrottleFn(updateHeader, 100)
const debouncedQuery = refDebounced(query, 300)   // debounce the value itself

watchDebounced(query, runSearch, { debounce: 300, maxWait: 1000 })
```

### Dismissible overlays

```ts
const panel = useTemplateRef<HTMLElement>('panel')
onClickOutside(panel, () => { isOpen.value = false })
onKeyStroke('Escape', () => { isOpen.value = false })
useScrollLock(document.body, isOpen)   // prevent background scroll while open
```

### Async state

```ts
const { state: user, isLoading, error, execute } = useAsyncState(
  () => api.users.get(id.value),
  null,
  { immediate: false, resetOnExecute: true },
)
```

### Virtual list

```ts
const { list, containerProps, wrapperProps } = useVirtualList(rows, { itemHeight: 44, overscan: 10 })
```

## Selection Rules

1. Search the VueUse catalog before writing a composable that touches a browser API, a timer, or an observer.
2. Import from `@vueuse/core` — it tree-shakes; do not worry about the library's total size.
3. Do not add an add-on package (`EXTERNAL`) without asking.
4. Skip a VueUse helper when a two-line `computed` is clearer (most of the Array category).
5. In SSR, avoid `createGlobalState`/`createSharedComposable` for per-user data.
6. Prefer `defineModel` over `useVModel` on Vue 3.4+.
7. Prefer a typed API layer over `useFetch` for production data fetching.

## Anti-Patterns

| Anti-pattern | Consequence | Fix |
|---|---|---|
| Hand-rolled listener/observer composables | Leaks, SSR crashes | VueUse equivalent |
| `createGlobalState` for user data in SSR | Cross-request leak | `createInjectionState` / per-request store |
| `useTimeAgo` in SSR output | Hydration mismatch | Absolute date + post-mount swap |
| `useLocalStorage` for tokens | XSS-exfiltratable | httpOnly cookie |
| `useVModel` on Vue 3.4+ | Redundant indirection | `defineModel` |
| Array helpers for trivial derivations | Indirection with no gain | Plain `computed` |
| Adding `@vueuse/integrations` unprompted | Unrequested dependency | Ask first |
