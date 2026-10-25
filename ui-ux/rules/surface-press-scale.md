---
title: Provide Tactile Feedback on Clickable Controls via :active Scale
impact: MEDIUM
impactDescription: Buttons that do not respond tactically when pressed feel sluggish, unresponsive, or broken.
tags: surfaces, interactions, buttons, active-state, polish
---

# Provide Tactile Feedback on Clickable Controls via :active Scale

Add subtle, physical tactile feedback to buttons and interactive cards on `:active` (press) state using a gentle `transform: scale(0.98)` or `scale(0.97)`. This gives the user immediate visual confirmation of their touch or click.

## Bad Example

```css
/* Static and lifeless when clicked; user wonders if click registered */
.button-primary {
  background-color: var(--color-action-primary);
  color: white;
}
.button-primary:hover {
  filter: brightness(1.1);
}
/* No :active state specified */
```

## Good Example

```css
.button-primary {
  background-color: var(--color-action-primary);
  color: white;
  transition: transform 0.1s ease, background-color 0.15s ease;
  will-change: transform;
}

.button-primary:active {
  /* Subtle physical depression feedback */
  transform: scale(0.97);
}

@media (prefers-reduced-motion: reduce) {
  .button-primary:active {
    transform: none; /* Respect reduced motion preferences */
  }
}
```
