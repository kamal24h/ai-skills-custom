---
title: Indicate Overflow Content with Scroll Shadows
impact: MEDIUM
impactDescription: Content that is clipped horizontally or vertically without an affordance remains undiscovered by users.
tags: layout, scrolling, tables, overflow, affordance
---

# Indicate Overflow Content with Scroll Shadows

When tables, chips, or carousels overflow horizontally, visual edges can appear flush with the screen border, hiding the fact that more items exist off-screen. Provide subtle gradient fade masks or scroll-driven shadows as visual affordances indicating scrollable content.

## Bad Example

```css
/* Overflow is scrollable, but content appears abruptly chopped off with zero hint of more items */
.chip-container {
  display: flex;
  overflow-x: auto;
  gap: 0.5rem;
}
```

## Good Example

```css
.chip-container {
  display: flex;
  overflow-x: auto;
  gap: 0.5rem;
  padding-inline: 1rem;
  /* Visual scroll affordance: subtle gradient mask at the right edge indicating more content */
  mask-image: linear-gradient(
    to right,
    black calc(100% - 2.5rem),
    transparent 100%
  );
  -webkit-mask-image: linear-gradient(
    to right,
    black calc(100% - 2.5rem),
    transparent 100%
  );
}
```
