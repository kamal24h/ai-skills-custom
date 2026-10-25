# Accessibility (WCAG 2.1 & 2.2 Standards)

**Impact:** CRITICAL · **Prefix:** `a11y-` · **Standards-Driven**

Web accessibility ensures all users, including those with visual, auditory, motor, or cognitive impairments, can perceive, understand, navigate, and interact with digital interfaces.

## Load When

- Designing and implementing interactive controls (buttons, forms, modals, tabs)
- Reviewing UI contrast, keyboard navigation, and focus order
- Handling dynamic asynchronous updates, alerts, and live announcements
- Sizing touch targets for mobile and touch devices
- Ensuring WCAG 2.1/2.2 AA compliance

## Rules

| Rule | Summary |
|------|---------|
| [`a11y-focus-visible`](../rules/a11y-focus-visible.md) | Keep keyboard focus visible; use a contrasting indicator that works across surfaces |
| [`a11y-form-labels-errors`](../rules/a11y-form-labels-errors.md) | Explicit `<label>` binding; inline errors linked via `aria-describedby` and `aria-invalid` |
| [`a11y-hit-targets`](../rules/a11y-hit-targets.md) | Comfortable target sizing; WCAG 2.2 AA 24×24 CSS px criterion and exceptions |
| [`a11y-accessible-svg-icons`](../rules/a11y-accessible-svg-icons.md) | Add `aria-hidden="true"` to decorative SVGs; provide accessible text for icon-only buttons |
| [`a11y-ios-input-zoom`](../rules/a11y-ios-input-zoom.md) | Enforce minimum 16px font size on inputs to prevent mobile browser auto-zoom |

## The POUR Principles

1. **Perceivable**: Information and interface components must be presentable in ways users can perceive (text alternatives, adequate contrast, captions).
2. **Operable**: Interface components and navigation must be operable via keyboard, provide enough time, and avoid seizures or physical reactions.
3. **Understandable**: Information and operation must be understandable (predictable layouts, clear error messages, readable text).
4. **Robust**: Content must be robust enough to be interpreted reliably by a wide variety of user agents, including assistive technologies.

## Focus Management and Keyboard Support

### Visible Focus Rings

Keep keyboard focus visibly indicated. If you suppress the browser's default outline, provide a clearly visible replacement that works on every relevant surface. `:focus-visible` can avoid showing the keyboard-specific treatment for pointer focus. WCAG 2.2 AA requires keyboard focus to be visible (SC 2.4.7); the defined 2px perimeter and 3:1 change in SC 2.4.13 are Level AAA. A contrasting 2px outline with offset is a useful baseline, but check it against the surfaces where it appears.

```css
/* Standard focus ring pattern */
:focus-visible {
  outline: 2px solid var(--color-focus-ring, oklch(0.55 0.22 255));
  outline-offset: 2px;
}

/* Ensure controls with custom background still stand out */
button:focus-visible,
a:focus-visible,
input:focus-visible,
select:focus-visible,
textarea:focus-visible {
  outline: 2px solid var(--color-focus-ring);
  outline-offset: 2px;
}
```

### Skip to Main Content Link

Provide a keyboard shortcut link as the first focusable element on every page:

```html
<a href="#main-content" class="skip-link">Skip to main content</a>
```

```css
.skip-link {
  position: absolute;
  top: -100%;
  left: 1rem;
  z-index: 1000;
  padding: 0.75rem 1.25rem;
  background-color: var(--color-surface-elevated, #ffffff);
  color: var(--color-text-primary, #111827);
  border: 2px solid var(--color-focus-ring, #2563eb);
  border-radius: 0.375rem;
  font-weight: 600;
  text-decoration: none;
  box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
  transition: transform 0.2s ease-in-out;
  transform: translateY(-200%);
}

.skip-link:focus {
  transform: translateY(0);
}
```

### `tabindex` Guidance

- `tabindex="0"`: Inserts a non-interactive element into the natural tab order.
- `tabindex="-1"`: Makes an element programmatically focusable (via `element.focus()`) without placing it in the natural tab cycle.
- Avoid positive `tabindex` values such as `1` or `5`; they disrupt natural DOM order and create a separate focus sequence.

## Hit Areas and Target Sizing (WCAG 2.2 SC 2.5.8)

Aim for comfortable target sizes, often **44×44 CSS pixels** or larger for touch. WCAG 2.2 AA SC 2.5.8 applies a **24×24 CSS pixel** minimum to pointer targets, with exceptions for spacing, inline targets, equivalent controls, user-agent controls, and essential presentations. Larger targets can still improve ease of use.

If the visual design calls for a compact icon, prefer a larger button box around it. A pseudo-element can extend the hit area when it will not overlap adjacent controls or intercept other interactions:

```css
.icon-button-compact {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
  background: transparent;
  border: none;
  padding: 0;
}

/* Optional expansion; check that this area does not overlap neighbors */
.icon-button-compact::after {
  content: "";
  position: absolute;
  inset: -10px; /* expands 24px + 20px = 44px */
  cursor: pointer;
}
```

## Screen Readers and Assistive Technology

### Visually Hidden Utility (`.sr-only`)

For icon-only buttons or context intended only for screen readers:

```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}
```

```html
<!-- Example usage on icon button -->
<button type="button" class="icon-button">
  <svg aria-hidden="true" width="20" height="20" viewBox="0 0 24 24">
    <!-- SVG paths -->
  </svg>
  <span class="sr-only">Close cart drawer</span>
</button>
```

### Dynamic Updates with `aria-live`

- `aria-live="polite"`: Screen reader waits until the user is idle before announcing changes (search results count, cart update notification).
- `aria-live="assertive"`: Interrupts user immediately. Reserve strictly for critical system errors or time-sensitive warnings.

```html
<div class="search-feedback" aria-live="polite" aria-atomic="true">
  14 products found for "wireless keyboard"
</div>
```

## Disabled Controls and Explanations

Choose `disabled` or `aria-disabled` based on the control's behavior and interaction pattern. Native `disabled` controls are removed from the normal tab sequence; if users need to understand why an action is unavailable, provide that explanation in nearby, discoverable text or validate on activation and guide them to what needs attention. `aria-disabled="true"` leaves focus management to the author and does not suppress activation by itself, so prevent the action in code and preserve a clear disabled state.

For example, a focusable unavailable action can reference its explanation:

```html
<button type="button" aria-disabled="true" aria-describedby="disabled-hint">
  Complete Purchase
</button>
<p id="disabled-hint" class="field-hint">
  Enter a valid shipping address to continue.
</p>
```


