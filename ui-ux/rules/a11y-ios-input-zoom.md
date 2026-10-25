---
title: Prevent Mobile Web Browser Auto-Zoom with Minimum 16px Input Font Size
impact: HIGH
impactDescription: Inputs smaller than 16px trigger an unrequested automatic viewport zoom on mobile web browsers, breaking responsive layouts and disorienting users.
tags: accessibility, mobile-web, forms, typography, responsive
---

# Prevent Mobile Web Browser Auto-Zoom with Minimum 16px Input Font Size

On touch and mobile web browsers (notably WebKit / Safari mobile), focusing a form control with a computed font size under 16px triggers an automatic viewport zoom. This un-requested zoom breaks responsive layout framing, pushes navigation offscreen, and confuses users.

Use a minimum computed font size of `16px` (e.g. `max(1rem, 16px)`) on all inputs, selects, and textareas. Never attempt to solve this by disabling viewport zooming via `user-scalable=no`, which severely violates accessibility standards (WCAG 1.4.4).

## Bad Example

Form inputs styled with sub-16px font sizes:

```css
/* ❌ Triggers automatic viewport zoom on mobile web browsers */
input[type="text"],
input[type="email"],
select {
  font-size: 14px;
}
```

## Good Example

Safely guaranteeing the 16px threshold without disabling user pinch-to-zoom:

```css
/* ✅ Safely meets the 16px minimum threshold on mobile web viewports */
input[type="text"],
input[type="email"],
input[type="tel"],
input[type="password"],
input[type="number"],
select,
textarea {
  font-size: max(1rem, 16px);
}
```
