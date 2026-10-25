---
title: Defend Flex and Grid Containers Against Text Overflow with min-width: 0 and overflow-wrap
impact: HIGH
impactDescription: Long uninterrupted strings (URLs, email addresses, non-English words) blow out flex and grid containers, pushing parent layouts offscreen and causing broken horizontal scrolling.
tags: resilience, defensive-css, flexbox, grid, overflow, typography
---

# Defend Flex and Grid Containers Against Text Overflow with min-width: 0 and overflow-wrap

By default, CSS Flexbox and Grid items have an initial `min-width: auto`. This means a container will refuse to shrink smaller than the intrinsic width of its text content. When an unexpectedly long word, URL, or code token appears, the flex child forces the whole page wider than the viewport, generating horizontal scrollbars and broken layouts.

Always set `min-width: 0` on flex/grid children that contain user-generated or dynamic text, paired with `overflow-wrap: break-word`.

## Bad Example

Flex children without minimum width protection:

```css
/* ❌ Breaks layout when user names or URLs are long */
.user-card {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.user-info {
  /* Implicit min-width: auto causes blow-out */
}

.user-email {
  /* No word-breaking strategy */
}
```

## Good Example

Defensive sizing for flex and grid content containers:

```css
/* ✅ Sized defensively against long text strings */
.user-card {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.user-info {
  min-width: 0;               /* Allows flex item to shrink below content width */
  flex: 1 1 auto;
}

.user-email {
  overflow-wrap: break-word;  /* Safely breaks long email addresses without layout shift */
  hyphens: auto;              /* Elegant hyphenation when supported */
}

/* For single-line clamped text (e.g., breadcrumb segments) */
.user-name-truncated {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
```
