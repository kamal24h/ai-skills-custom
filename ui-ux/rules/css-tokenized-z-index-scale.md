---
title: Eliminate Arbitrary Z-Index Values with a Tokenized Stacking Scale
impact: HIGH
impactDescription: Hardcoded magic numbers like z-index: 9999 trigger stacking wars, causing dropdowns and tooltips to clip underneath navigation bars or overlay modals unexpectedly.
tags: css, z-index, stacking-context, layout, tokens
---

# Eliminate Arbitrary Z-Index Values with a Tokenized Stacking Scale

Arbitrary z-index numbers (`z-index: 999`, `z-index: 10000`) cause unpredictable layer collisions across components. When multiple developers pick random large numbers, floating menus hide underneath sticky headers, and modal backdrops cover interactive dialogs.

Define a structured, semantic z-index scale in CSS custom properties and restrict all z-index declarations to these tokens.

## Bad Example

Random, escalating z-index values scattered across components:

```css
/* ❌ Magic numbers with no defined relationship */
.sticky-header {
  z-index: 999;
}

.dropdown-menu {
  z-index: 1000;
}

.modal-dialog {
  z-index: 99999; /* Guessing to win the stacking contest */
}
```

## Good Example

Centralized, semantic z-index tokens on `:root`:

```css
/* ✅ Documented, predictable stacking order */
:root {
  --z-base:      0;
  --z-raised:   10;
  --z-dropdown: 100;
  --z-sticky:   200;
  --z-overlay:  300;
  --z-modal:    400;
  --z-toast:    500;
  --z-tooltip:  600;
}

.sticky-header {
  position: sticky;
  top: 0;
  z-index: var(--z-sticky);
}

.dropdown-menu {
  position: absolute;
  z-index: var(--z-dropdown);
}

.toast-notification {
  position: fixed;
  z-index: var(--z-toast);
}
```
