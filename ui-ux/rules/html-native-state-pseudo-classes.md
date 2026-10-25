---
title: Style Interactive States with Native Pseudo-Classes Over Custom Data Attributes
impact: MEDIUM
impactDescription: Inventing parallel state attributes like data-disabled or data-open often causes desynchronization with true browser accessibility states and adds unnecessary JS complexity.
tags: html, css, states, semantics, accessibility, pseudo-classes
---

# Style Interactive States with Native Pseudo-Classes Over Custom Data Attributes

HTML form controls and interactive elements have native, platform-integrated state pseudo-classes (`:disabled`, `:checked`, `:open`, `:invalid`, `:read-only`, `:focus-visible`). These states are automatically understood by browser accessibility trees, keyboard focus engines, and screen readers.

Avoid building parallel state mechanisms with custom classes (e.g. `.disabled`, `data-state="disabled"`) when the element already supports native semantic states.

## Bad Example

Custom class toggling that disconnects visual styling from the true DOM state:

```html
<!-- ❌ Screen reader sees enabled button; JS class only changes appearance -->
<button type="button" class="btn is-disabled">Save Document</button>
```

```css
.btn.is-disabled {
  opacity: 0.5;
  pointer-events: none; /* Fragile hack; doesn't prevent keyboard activation */
}
```

## Good Example

Native attributes paired with native state pseudo-classes:

```html
<!-- ✅ Browser genuinely disables button in accessibility tree and keyboard sequence -->
<button type="button" class="btn" disabled>Save Document</button>
```

```css
/* ✅ Matches standard HTML state semantics */
.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Disclosure state on <details> */
details[open] > summary {
  color: var(--color-action-primary);
}

/* Form validation state */
.form-input:user-invalid {
  border-color: var(--color-feedback-danger);
}
```
