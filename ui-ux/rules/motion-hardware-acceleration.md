---
title: Prefer Efficient Animation Properties
impact: HIGH
impactDescription: Animating layout and paint properties triggers continuous recalculations, causing jank, stutter, and battery drain.
tags: motion, animation, performance, transform, opacity, css
---

# Prefer Efficient Animation Properties

Prefer `transform` and `opacity` for frequent motion when they express the intended effect: they can often avoid layout and paint work. Do not treat them as the only permissible animated properties; color, filters, and other transitions may be appropriate. Avoid animating layout-triggering properties by default, and profile effects when performance matters. Use `will-change` sparingly and only when a measured need justifies it.

## Bad Example

```css
/* May trigger repeated layout work during the transition */
.slide-drawer {
  position: fixed;
  left: -320px;
  width: 320px;
  transition: left 0.3s ease-out;
}

.slide-drawer.is-active {
  left: 0;
}
```

## Good Example

```css
/* Moves the drawer without repeatedly changing its layout position */
.slide-drawer {
  position: fixed;
  left: 0;
  width: 320px;
  transform: translateX(-100%);
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

.slide-drawer.is-active {
  transform: translateX(0);
}
```
