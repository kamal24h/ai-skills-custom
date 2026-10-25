---
title: Structure Breadcrumbs with Ordered Lists and aria-current
impact: HIGH
impactDescription: Breadcrumbs rendered as unstructured div chains with hardcoded slash characters confuse screen readers and fail orientation accessibility.
tags: component, breadcrumbs, navigation, accessibility, semantics
---

# Structure Breadcrumbs with Ordered Lists and aria-current

**Impact: HIGH (Clear hierarchical wayfinding for screen readers and keyboard users)**

Breadcrumb navigation indicates the user's current location within a hierarchical site architecture. When built using arbitrary `div` chains or hardcoded text slashes (`/`), screen readers announce characters like "slash" between words, and users cannot determine which step represents the current page.

Wrap breadcrumbs in a `<nav aria-label="Breadcrumb">` containing an ordered list (`<ol>`). Mark the current page with `aria-current="page"` and generate separator icons via CSS pseudo-elements (`::after`).

## Bad Example

Unstructured span soup with hardcoded text separators:

```html
<!-- ❌ Screen reader announces: "Home slash Settings slash Billing" with no list structure -->
<div class="breadcrumbs">
  <a href="/">Home</a> / 
  <a href="/settings">Settings</a> / 
  <span>Billing</span>
</div>
```

## Good Example

Semantic ordered list with CSS-generated separators and active page attribute:

```html
<!-- ✅ Screen readers announce: "Breadcrumb navigation, list 3 items, Billing current page" -->
<nav aria-label="Breadcrumb" class="breadcrumbs">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/settings">Settings</a></li>
    <li aria-current="page">Billing</li>
  </ol>
</nav>
```

```css
.breadcrumbs ol {
  display: flex;
  align-items: center;
  list-style: none;
  margin: 0;
  padding: 0;
  gap: var(--space-2);
}

/* CSS-generated visual separator ignored by screen readers */
.breadcrumbs li:not(:last-child)::after {
  content: "/";
  margin-inline-start: var(--space-2);
  color: var(--color-text-muted);
}

.breadcrumbs [aria-current="page"] {
  font-weight: 600;
  color: var(--color-text-primary);
}
```

## Why

- **Screen Reader Context**: Assistive software announces list size, user position, and explicitly flags the active page via `aria-current="page"`.
- **Clean Voice Output**: Decorative separators generated in CSS (`content: "/"`) are not announced as confusing punctuation.
- **Visual Clarity**: Provides clear navigational wayfinding for users deep inside nested product views.

## Related

- Reference: [`references/css-layout-cookbook.md`](../references/css-layout-cookbook.md)
- Reference: [`references/components-and-patterns.md`](../references/components-and-patterns.md)
