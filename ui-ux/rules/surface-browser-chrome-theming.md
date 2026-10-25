---
title: Theme Browser-Native Chrome Surfaces from the Design Palette
impact: MEDIUM
impactDescription: Default browser styles for selection, scrollbars, and input carets look uncrafted and disconnect the user from the brand palette.
tags: craft, styling, selection, caret, scrollbars, surfaces
---

# Theme Browser-Native Chrome Surfaces from the Design Palette

The browser surfaces you do not explicitly draw—text selection highlighting, text input carets, custom scrollbars, and link underline styling—still carry the visual experience. Theming these subtle browser defaults is an immediate signal of high-craft engineering.

## Bad Example

Leaving browser chrome to default system values:

```css
/* ❌ Browser defaults: harsh blue selection, unstyled black caret, default wide gray scrollbars */
input {
  /* Default browser caret */
}

a {
  /* Default tight underline that collides with descenders */
  text-decoration: underline;
}
```

## Good Example

Explicitly style browser surfaces from the token palette:

```css
/* ✅ 1. Brand-tinted text selection */
::selection {
  background-color: oklch(0.60 0.20 250 / 0.25);
  color: oklch(0.20 0.02 250);
}

/* ✅ 2. Themed input caret */
input,
textarea {
  caret-color: var(--color-action-primary, oklch(0.55 0.22 250));
}

/* ✅ 3. Modern unobtrusive scrollbars */
html {
  scrollbar-color: oklch(0.70 0.01 250) transparent;
  scrollbar-width: thin;
}

/* ✅ 4. Elegant link underline offset */
a:not([class]) {
  text-decoration: underline;
  text-underline-offset: 0.25em;
  text-decoration-thickness: 1.5px;
  text-decoration-color: oklch(from currentColor l c h / 0.35);
  transition: text-decoration-color 0.15s ease;
}

a:not([class]):hover {
  text-decoration-color: currentColor;
}
```
