# UI Resilience, Boundary Conditions & Edge Cases

**Impact:** CRITICAL · **Prefix:** `resilience-` · **Production Hardening & Defensive CSS**

A web interface is only as good as its behavior under hostile, degraded, or unexpected real-world conditions. Defensive frontend design hardens the interface against extreme string lengths, network latency, multi-language expansion, boundary data quantities, and interrupted pointer interactions.

## Load When

- Designing or reviewing data tables, user profile cards, comment threads, and list items
- Implementing asynchronous forms, mutation requests, and optimistic UI updates
- Building interactive drag surfaces, custom sliders, and gesture controls
- Auditing layouts for internationalization (i18n), RTL scripts, and long non-English copy
- Handling network disconnections, API timeouts, and error states

## Rules

| Rule | Summary |
|------|---------|
| [`resilience-text-overflow-wrap`](../rules/resilience-text-overflow-wrap.md) | Prevent container blowout from long strings using `overflow-wrap: break-word` and `min-width: 0` |

---

## Defensive Typography & Extreme Text

Real user names, localized phrases, URLs, and German compound words break rigid fixed-width designs.

### 1. The Container Blowout Prevention Rule
Flex and Grid children have a default `min-width: auto`, which prevents them from shrinking smaller than their longest unbroken text child:

```css
/* ✅ Essential defensive CSS for flex and grid children */
.flex-child,
.grid-cell {
  min-width: 0;                    /* Allows container to shrink below content size */
  overflow-wrap: break-word;       /* Breaks long URLs and words safely */
  hyphens: auto;                   /* Hyphenates gracefully when supported */
}

/* For single-line truncated text (e.g., breadcrumbs, table cells) */
.truncate-single-line {
  min-width: 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
```

### 2. Localization Expansion (i18n)
- Text strings in German, French, or Spanish expand by **20% to 35%** compared to English.
- Avoid hardcoded container widths (`width: 120px` on buttons or tabs). Use fluid sizing and responsive auto-wrapping:
```css
.button-row {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-3);
}
```

### 3. Bi-directional (RTL) Readiness with CSS Logical Properties
Never use physical directional properties (`left`, `right`) when building interfaces intended for global audiences:

| Physical (Legacy) | Modern Logical Property (Bidirectional) |
|---|---|
| `margin-left: 1rem;` | `margin-inline-start: 1rem;` |
| `padding-right: 1.5rem;` | `padding-inline-end: 1.5rem;` |
| `border-left: 2px solid;` | `border-inline-start: 2px solid;` |
| `text-align: left;` | `text-align: start;` |

---

## Boundary Data Conditions

Always test components against the extremes of data volume:

1. **Zero Items (Empty State)**: Never render a blank screen or raw empty table header. Render a dedicated empty state with explanation and call-to-action.
2. **Single Item**: Does the layout look lopsided or stretched when only 1 card or row exists? Ensure maximum column widths (`max-width: 24rem` on cards) prevent bizarre stretching.
3. **Tens of Thousands of Items**: Never render 10,000 DOM nodes at once. Use virtual scrolling (`content-visibility: auto`, virtualized lists) or server-side pagination.
4. **Extreme Numeric Values**: Billions, negative balances, and recurring decimals (`$1,942,000,000.00` or `-0.000004%`) must not overlap adjacent columns. Apply `font-variant-numeric: tabular-nums;` and right-align numeric table headers and cells.

---

## Asynchronous Mutation Resilience

### Double-Submission Prevention
Rapidly clicking a primary button must never send duplicate API requests, create duplicate orders, or charge payment twice:

```javascript
async function handleSubmit(event) {
  event.preventDefault();
  const submitButton = form.querySelector('button[type="submit"]');
  
  // 1. Guard against concurrent triggers
  if (submitButton.disabled) return;
  
  try {
    submitButton.disabled = true;
    submitButton.setAttribute('aria-busy', 'true');
    await submitApiPayload();
  } catch (err) {
    // 2. Re-enable on failure so user can retry
    submitButton.disabled = false;
    submitButton.removeAttribute('aria-busy');
    showInlineError(err.message);
  }
}
```

### Optimistic UI with Rollback
When updating UI optimistically (e.g. toggling a favorite bookmark or like counter):
1. Immediately render the desired target state for instant perceived responsiveness.
2. Dispatch network mutation in the background.
3. If the request fails, cleanly revert the visual state to previous value and announce an alert: *"Couldn't save favorite. Tap to retry."*

---

## Interrupted Pointer Gestures

When implementing custom interactive drag surfaces, sliders, or scroll scrubbers, real user interactions are frequently interrupted by browser scrolling, incoming phone alerts, or multi-touch collisions.

Always bind to modern Pointer Events and listen for interruption signals:

```javascript
function attachDragController(sliderElement) {
  let isDragging = false;

  function onPointerDown(e) {
    isDragging = true;
    // Capture pointer so move events continue outside boundary
    sliderElement.setPointerCapture(e.pointerId);
  }

  function onPointerMove(e) {
    if (!isDragging) return;
    updateSliderPosition(e.clientX);
  }

  function cleanupDrag(e) {
    if (!isDragging) return;
    isDragging = false;
    try {
      sliderElement.releasePointerCapture(e.pointerId);
    } catch {}
  }

  sliderElement.addEventListener('pointerdown', onPointerDown);
  sliderElement.addEventListener('pointermove', onPointerMove);
  sliderElement.addEventListener('pointerup', cleanupDrag);
  
  // CRITICAL: Handle interrupted gestures without freezing state
  sliderElement.addEventListener('pointercancel', cleanupDrag);
  sliderElement.addEventListener('lostpointercapture', cleanupDrag);
  window.addEventListener('blur', cleanupDrag);
}
```

**Gesture Invariants:**
- `pointercancel`: Browser intercepted gesture to perform native scroll. Clear dragging state immediately.
- `lostpointercapture`: Drag capture was reassigned or lost. Clear state.
- `window.blur`: User switched tabs or window lost focus. Clear state.
- Following an interruption, the next click or drag must work cleanly without requiring a page reload.
