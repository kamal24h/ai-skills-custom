---
title: Organize Colors into a Three-Tier Token Architecture
impact: CRITICAL
impactDescription: Hardcoding raw color primitives directly into components prevents theming, breaks dark mode, and leads to inconsistent UI.
tags: colors, tokens, design-systems, css-variables, dark-mode
---

# Organize Colors into a Three-Tier Token Architecture

For reusable or themeable interfaces, semantic color roles help keep components consistent and support themes. A three-tier hierarchy is one useful pattern; small or one-off interfaces may need fewer layers. Avoid unexplained colors that make contrast and theme changes difficult:
1. **Primitives** (e.g. `--blue-500`)
2. **Semantic Roles** (e.g. `--color-action-primary`, `--color-surface`)
3. **Component Scoped** (e.g. `--button-primary-bg`)

## Bad Example

```css
/* Direct binding to palette primitives prevents theme switching */
.btn-primary {
  background-color: var(--blue-500);
  color: #ffffff;
  border: 1px solid var(--blue-600);
}

.card {
  background-color: #ffffff; /* Fails in dark mode */
  color: #111827;
}
```

## Good Example

```css
:root {
  /* Tier 1: Primitives */
  --blue-500: oklch(0.58 0.20 250);
  --neutral-100: oklch(0.95 0.008 250);
  --neutral-900: oklch(0.20 0.015 250);

  /* Tier 2: Semantic Roles */
  --color-surface: var(--neutral-100);
  --color-text-primary: var(--neutral-900);
  --color-action-primary: var(--blue-500);
}

/* Tier 3: Component consumers */
.btn-primary {
  background-color: var(--color-action-primary);
  color: var(--color-text-on-action, #ffffff);
}

.card {
  background-color: var(--color-surface);
  color: var(--color-text-primary);
}
```
