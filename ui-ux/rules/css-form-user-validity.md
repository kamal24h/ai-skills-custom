---
title: Apply Form Validation Styles with :user-valid and :user-invalid
impact: HIGH
impactDescription: Styling inputs with :invalid shows aggressive red error borders on freshly loaded, untouched forms before the user has typed anything.
tags: css, forms, validation, pseudo-classes, user-experience
---

# Apply Form Validation Styles with :user-valid and :user-invalid

**Impact: HIGH (Prevents hostile red error states on empty, untouched form fields)**

Styling inputs using the classic `:invalid` pseudo-class causes immediate visual failure on required inputs: the moment a user opens a registration or checkout form, every blank required input glows with aggressive red error borders before they have even touched a key.

Modern CSS provides `:user-valid` and `:user-invalid`, which match an element's validity only after the user has actively interacted with the input (typing, altering value, or blurring), ensuring error indicators appear only when timely and helpful.

## Bad Example

Using `:invalid` directly on form controls:

```css
/* ❌ Lights up red on page load when inputs are completely empty */
input:required:invalid {
  border-color: #ef4444;
  background-color: #fef2f2;
}
```

## Good Example

Using `:user-invalid` for polite, interaction-aware feedback:

```css
/* ✅ Remains neutral until the user attempts to enter data or leaves the field invalid */
.form-input:user-invalid {
  border-color: var(--color-feedback-danger);
  outline-color: var(--color-feedback-danger);
}

.form-input:user-valid {
  border-color: var(--color-feedback-success);
}
```

## Why

- **Reduced User Anxiety**: Prevents penalizing users before they have had an opportunity to fill out the form.
- **Standards-Compliant Timing**: Matches WCAG and usability best practices without requiring custom JavaScript "dirty" state flags.
- **Clean Fallback**: Integrates naturally with browser HTML5 constraint validation (`required`, `pattern`, `minlength`).

## Related

- Reference: [`references/modern-css-reference.md`](../references/modern-css-reference.md)
- Reference: [`references/form-ux-and-patterns.md`](../references/form-ux-and-patterns.md)
