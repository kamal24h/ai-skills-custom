---
title: Implement Fluid Typography via clamp()
impact: HIGH
impactDescription: Hardcoded font sizes and jarring media queries produce abrupt layout shifts and poor reading comfort.
tags: typography, css, clamp, fluid-type, responsive
---

# Implement Fluid Typography via clamp()

Use CSS `clamp(min, preferred, max)` to scale typography continuously between mobile and desktop viewports, avoiding abrupt font size jumps at arbitrary media query breakpoints. Always specify unitless `line-height` so leading scales proportionally.

## Bad Example

```css
/* Abrupt jumps and pixel-based line-height that does not scale */
h1 {
  font-size: 24px;
  line-height: 32px;
}

@media (min-width: 768px) {
  h1 {
    font-size: 36px;
    line-height: 48px;
  }
}

@media (min-width: 1200px) {
  h1 {
    font-size: 54px;
    line-height: 64px;
  }
}
```

## Good Example

```css
/* Smooth, continuous scaling across viewports with unitless line-height */
:root {
  --font-size-h1: clamp(2rem, 1.45rem + 2.4vw, 3.5rem);
  --font-size-body: clamp(1rem, 0.95rem + 0.25vw, 1.125rem);
}

h1 {
  font-size: var(--font-size-h1);
  line-height: 1.15; /* Inverted ratio: large headings need tighter leading */
}

p {
  font-size: var(--font-size-body);
  line-height: 1.6;  /* Body copy requires generous leading for readability */
}
```
