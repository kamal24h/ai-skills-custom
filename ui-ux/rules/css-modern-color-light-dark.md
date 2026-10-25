---
title: Streamline Themes with light-dark() and CSS Relative Color Syntax
impact: MEDIUM
impactDescription: Duplicating entire token trees across light and dark media queries leads to stale values, missed overrides, and bloated CSS rules.
tags: css, color, theming, light-dark, color-scheme, oklch
---

# Streamline Themes with light-dark() and CSS Relative Color Syntax

Modern CSS eliminates the need to duplicate entire blocks of CSS variables inside separate `@media (prefers-color-scheme: dark)` declarations.

By declaring `color-scheme: light dark;` on `:root`, you can define both light and dark values simultaneously using the native `light-dark(lightColor, darkColor)` function, and derive state variants with `color-mix()` or relative OKLCH color syntax.

## Bad Example

Duplicating large variable ramp sets across separate media queries:

```css
/* ❌ Redundant duplication prone to maintenance drift */
:root {
  --canvas: #ffffff;
  --text: #111827;
  --surface: #f9fafb;
}

@media (prefers-color-scheme: dark) {
  :root {
    --canvas: #0f172a;
    --text: #f8fafc;
    --surface: #1e293b;
  }
}
```

## Good Example

Concise declarations using `color-scheme` and `light-dark()`:

```css
/* ✅ Single source of truth, adapts automatically to user preference */
:root {
  color-scheme: light dark;

  /* Automatic theme switching */
  --color-canvas:  light-dark(oklch(0.99 0 0), oklch(0.14 0.015 250));
  --color-surface: light-dark(oklch(1 0 0),    oklch(0.19 0.015 250));
  --color-text:    light-dark(oklch(0.20 0 0), oklch(0.96 0.005 250));
  --color-border:  light-dark(oklch(0.89 0 0), oklch(0.28 0.015 250));

  /* Derive hover state automatically via color-mix */
  --color-action-bg: oklch(0.55 0.22 250);
  --color-action-bg-hover: color-mix(in oklch, var(--color-action-bg), black 10%);
}
```
