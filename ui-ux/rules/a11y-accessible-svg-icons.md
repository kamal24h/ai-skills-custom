---
title: Ensure Accessible SVGs and Icon Button Names
impact: CRITICAL
impactDescription: Screen readers announce naked SVG tags with cryptic paths or skip icon-only buttons entirely without an accessible name.
tags: accessibility, svg, icons, screen-reader, a11y
---

# Ensure Accessible SVGs and Icon Button Names

Interactive icon buttons must provide an accessible name via a visually hidden `.sr-only` text span or `aria-label`. All purely decorative inline SVGs must be explicitly hidden from the accessibility tree using `aria-hidden="true"`.

## Bad Example

```html
<!-- Completely unannounced to screen readers: produces an anonymous empty button -->
<button type="button" class="search-trigger">
  <svg viewBox="0 0 24 24">
    <path d="..."></path>
  </svg>
</button>
```

## Good Example

```html
<!-- Screen reader announces "Search products"; decorative vector is ignored -->
<button type="button" class="search-trigger">
  <svg aria-hidden="true" focusable="false" width="20" height="20" viewBox="0 0 24 24">
    <path d="..."></path>
  </svg>
  <span class="sr-only">Search products</span>
</button>

<!-- Alternative using aria-label on the button -->
<button type="button" class="search-trigger" aria-label="Search products">
  <svg aria-hidden="true" focusable="false" width="20" height="20" viewBox="0 0 24 24">
    <path d="..."></path>
  </svg>
</button>
```
