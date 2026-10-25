---
title: Pin Footers Modernly with Grid min-height 100dvh
impact: HIGH
impactDescription: When page content is brief, footers float awkwardly in the middle of the screen unless pinned modernly to the viewport bottom.
tags: layout, footer, grid, dvh, responsive
---

# Pin Footers Modernly with Grid min-height 100dvh

**Impact: HIGH (Prevents floating footers on short pages across mobile and desktop)**

On pages with minimal content (such as 404 error pages, login screens, or empty state feeds), standard document flow leaves the `<footer>` floating awkwardly halfway up the screen. Conversely, fixed footers (`position: fixed`) cover content when the page is scrolled.

Use CSS Grid with `grid-template-rows: auto 1fr auto` and `min-height: 100dvh` on the page wrapper. This guarantees the footer stays pinned to the bottom of the viewport on short pages, while pushing down naturally when content exceeds screen height.

## Bad Example

Using fixed positioning or legacy `100vh`:

```css
/* ❌ Overlaps content when scrolling, or jumps when mobile address bar hides */
footer {
  position: fixed;
  bottom: 0;
  width: 100%;
}
```

## Good Example

Declarative Grid template rows with dynamic viewport units:

```css
/* ✅ Keeps footer pinned on short content; pushes down naturally on long content */
.page-wrapper {
  display: grid;
  grid-template-rows: auto 1fr auto; /* Header, expandable main, footer */
  min-height: 100dvh;               /* Dynamic viewport units adapt to mobile browser chrome */
}

main {
  /* Automatically expands to fill remaining viewport height */
}
```

## Why

- **Mobile Viewport Stability**: `100dvh` adapts dynamically as mobile browser URL bars appear or hide, eliminating awkward viewport jumps.
- **Scroll Naturality**: Allows footers to sit naturally below content on long scrollable pages without obscuring interactive controls.
- **Maintainability**: Pure CSS solution requiring zero JavaScript viewport height calculations.

## Related

- Reference: [`references/css-layout-cookbook.md`](../references/css-layout-cookbook.md)
- Reference: [`references/layout-and-responsive.md`](../references/layout-and-responsive.md)
