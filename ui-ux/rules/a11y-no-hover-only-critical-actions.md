---
title: Never Hide Critical Actions and Affordances Behind Hover Alone
impact: CRITICAL
impactDescription: Controls visible only on mouse hover are completely inaccessible to touch device users, screen reader users, and people navigating via keyboard.
tags: accessibility, affordances, mobile, touch, keyboard, hover
---

# Never Hide Critical Actions and Affordances Behind Hover Alone

Hover is an input enhancement for pointer devices, never a mandatory gate for discovery. Primary tasks—such as editing an item, deleting a row, expanding details, or copying a link—must have persistent visual cues or clear, always-visible action menus.

If secondary convenience shortcuts appear on desktop hover, ensure they are also accessible via keyboard focus (`:focus-within`) and have an explicit permanent equivalent on touch viewports.

## Bad Example

Action buttons hidden with zero opacity until the parent card is hovered:

```css
/* ❌ Inaccessible on mobile touch screens; invisible to keyboard tab order */
.row-actions {
  opacity: 0;
  pointer-events: none;
}

.table-row:hover .row-actions {
  opacity: 1;
  pointer-events: auto;
}
```

## Good Example

Persistent affordances, keyboard focus integration, and mobile accessibility:

```css
/* ✅ 1. Always visible on touch viewports and mobile screens */
.row-actions {
  display: flex;
  gap: var(--space-2);
}

/* ✅ 2. On pointer devices, subtle reveal with full keyboard focus support */
@media (hover: hover) and (pointer: fine) {
  .row-actions {
    opacity: 0.6;
    transition: opacity 0.15s ease;
  }

  /* Reveals on hover OR when any inner button receives keyboard focus */
  .table-row:hover .row-actions,
  .table-row:focus-within .row-actions {
    opacity: 1;
  }
}
```
