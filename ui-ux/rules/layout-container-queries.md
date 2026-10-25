---
title: Prefer Container Queries over Viewport Media Queries for Components
impact: HIGH
impactDescription: Rigid viewport media queries break reusable components when placed inside sidebars, split-views, or multi-column layouts.
tags: layout, container-queries, responsive, modern-css
---

# Prefer Container Queries over Viewport Media Queries for Components

Build reusable components that adapt according to the width of their immediate parent container using `@container` instead of relying on the global viewport `@media (min-width: ...)`.

## Bad Example

```css
/* Component assumes it always has full viewport width */
@media (min-width: 768px) {
  .user-card {
    display: grid;
    grid-template-columns: 200px 1fr;
  }
}
/* If this card is placed in a 250px sidebar on a 1920px screen, it breaks! */
```

## Good Example

```css
/* 1. Define parent as container context */
.container-slot {
  container-type: inline-size;
  container-name: user-widget;
}

/* 2. Mobile/compact card layout by default */
.user-card {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

/* 3. Horizontal card adapts whenever its parent container allows */
@container user-widget (min-width: 28rem) {
  .user-card {
    display: grid;
    grid-template-columns: 8rem 1fr;
    align-items: center;
  }
}
```
