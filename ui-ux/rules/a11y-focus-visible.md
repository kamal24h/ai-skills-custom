---
title: Ensure Visible Focus Indicators with :focus-visible
impact: CRITICAL
impactDescription: Removing focus indicators makes interfaces completely inoperable for keyboard-only and switch-device users.
tags: accessibility, a11y, focus, keyboard-navigation, wcag
---

# Ensure Visible Focus Indicators with :focus-visible

Keep keyboard focus visibly indicated. If you suppress the browser's default outline, provide a clearly visible replacement that works on every relevant surface. `:focus-visible` can avoid showing the keyboard-specific treatment for pointer focus. A 2px contrasting outline with offset is a strong baseline, not by itself a guarantee of WCAG conformance; WCAG 2.2 SC 2.4.13's specific size and contrast thresholds are Level AAA.

## Bad Example

```css
/* Removes the focus indicator entirely */
button,
a,
input {
  outline: none;
}

/* A subtle shadow may disappear against the current surface */
button:focus {
  outline: none;
  box-shadow: 0 0 2px rgba(0, 0, 0, 0.2);
}
```

## Good Example

```css
/* Maintain natural focus styling for keyboard navigators */
:focus-visible {
  outline: 2px solid var(--color-focus-ring, oklch(0.55 0.22 255));
  outline-offset: 2px;
}

/* Preserve distinct focus rings even on dark or colored containers */
.dark-panel :focus-visible {
  outline: 2px solid oklch(0.9 0.05 255);
  outline-offset: 2px;
}
```
