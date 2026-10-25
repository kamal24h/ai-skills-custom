---
title: Derive Interactive States with color-mix()
impact: MEDIUM
impactDescription: Hardcoding arbitrary hex values for hover and active states creates brittle, unmaintainable stylesheets.
tags: colors, css, color-mix, tokens, interactive-states
---

# Derive Interactive States with color-mix()

Instead of hand-picking arbitrary hex values for hover, pressed, or subtle tint states, derive them dynamically from your base semantic color tokens using modern CSS `color-mix()`.

## Bad Example

```css
/* Hardcoded arbitrary colors that desynchronize during theme updates */
.btn-primary {
  background-color: #2563eb;
}
.btn-primary:hover {
  background-color: #1d4ed8; /* Hardcoded guess */
}
.btn-primary:active {
  background-color: #1e40af; /* Hardcoded guess */
}
```

## Good Example

```css
/* Dynamically mixed states based on current semantic action token */
.btn-primary {
  background-color: var(--color-action-primary);
  color: var(--color-text-on-action, #ffffff);
  transition: background-color 0.15s ease;
}

.btn-primary:hover {
  /* Mix with black (or pure tint) in perceptual OKLCH color space */
  background-color: color-mix(in oklch, var(--color-action-primary) 88%, black);
}

.btn-primary:active {
  background-color: color-mix(in oklch, var(--color-action-primary) 78%, black);
}
```
