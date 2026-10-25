---
title: Associate Form Labels and Link Inline Errors
impact: CRITICAL
impactDescription: Floating or placeholder-only labels fail screen readers and disappear when users start typing.
tags: accessibility, a11y, forms, labels, validation, wcag
---

# Associate Form Labels and Link Inline Errors

Give form inputs a programmatic accessible name, usually through an associated visible `<label for="...">`. A placeholder can supplement but should not replace a persistent label. When an error is shown, associate its text with the field (for example, using `aria-describedby`) and set `aria-invalid="true"` while the value is invalid. Announce errors at a useful time without interrupting every keystroke.

## Bad Example

```html
<!-- Unassociated label and placeholder used as the only prompt -->
<input type="email" placeholder="Enter your email address" />
<span class="error-text">Email address is invalid</span>
```

## Good Example

```html
<div class="form-field">
  <label for="user-email">Email Address</label>
  <input
    type="email"
    id="user-email"
    name="email"
    required
    autocomplete="email"
    aria-invalid="true"
    aria-describedby="email-error email-hint"
  />
  <p id="email-hint" class="field-hint">We'll never share your email with third parties.</p>
  <p id="email-error" class="field-error" role="alert">Please enter a valid email address with an @ symbol.</p>
</div>
```
