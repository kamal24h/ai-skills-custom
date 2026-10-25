---
title: Ensure WCAG Contrast Compliance and Thoughtful Dark Mode
impact: CRITICAL
impactDescription: Low-contrast text is illegible for millions of users with low vision or when viewing under bright sunlight.
tags: accessibility, colors, contrast, wcag, dark-mode
---

# Ensure WCAG Contrast Compliance and Thoughtful Dark Mode

Text and interactive elements must satisfy WCAG 2.1/2.2 AA contrast ratios: at least **4.5:1** for regular body text, and **3:1** for large text and UI component boundaries. In dark mode, elevate surfaces with lighter shades rather than heavier shadows, and avoid pure `#000000` body backgrounds.

## Bad Example

```css
/* Gray-on-gray text: contrast ratio is ~2.1:1 (fails WCAG AA) */
.caption {
  color: #9ca3af;
  background-color: #f3f4f6;
}

/* Dark mode using stark pure black and ultra-high-chroma vibrating blue */
@media (prefers-color-scheme: dark) {
  body {
    background-color: #000000;
  }
  .link {
    color: #0000ff; /* Saturated blue causes chromatic aberration on black */
  }
}
```

## Good Example

```css
/* High contrast: ratio > 4.5:1 */
.caption {
  color: oklch(0.35 0.015 250); /* #4b5563 on light background */
  background-color: oklch(0.97 0.005 250);
}

/* Dark mode: softer dark neutral and desaturated accent */
@media (prefers-color-scheme: dark) {
  body {
    background-color: oklch(0.14 0.015 250); /* Deep charcoal instead of pure black */
    color: oklch(0.96 0.005 250);
  }
  .card-surface {
    background-color: oklch(0.20 0.015 250); /* Surface elevation indicated by lightness */
  }
  .link {
    color: oklch(0.72 0.14 250); /* Softer, slightly desaturated blue */
  }
}
```
