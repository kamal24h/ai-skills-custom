---
title: Support prefers-reduced-motion Preferences
impact: CRITICAL
impactDescription: Large movement and parallax triggers vestibular disorders, motion sickness, nausea, and migraines.
tags: motion, accessibility, a11y, prefers-reduced-motion, wcag
---

# Support prefers-reduced-motion Preferences

Respect the user's reduced-motion preference through `@media (prefers-reduced-motion: reduce)` or an equivalent mechanism. Remove or adapt non-essential movement such as large parallax effects and decorative loops, while keeping state changes understandable. A brief fade or an immediate change can work; do not replace motion with another effect that still causes discomfort. WCAG 2.2 SC 2.3.3 (Animation from Interactions) is Level AAA, though honoring this preference is a strong inclusive-design practice.

## Bad Example

```css
/* Ignores user accessibility settings and forces rapid bouncing/zooming */
.spinning-hero-badge {
  animation: spin 4s linear infinite;
}

.modal-enter {
  animation: zoomAndFly 0.8s cubic-bezier(0.68, -0.55, 0.27, 1.55);
}
```

## Good Example

```css
/* Standard animations for default users */
.modal-enter {
  animation: slideUp 0.25s ease-out;
}

/* Adapt non-essential motion when the user requests reduced motion */
@media (prefers-reduced-motion: reduce) {
  .modal-enter {
    animation: none !important;
    opacity: 1 !important;
  }
}
```
