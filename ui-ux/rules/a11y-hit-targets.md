---
title: Maintain Accessible Touch and Hit Target Sizes
impact: HIGH
impactDescription: Small touch targets cause accidental taps, input frustration, and fail WCAG 2.2 Target Size criteria.
tags: accessibility, a11y, mobile, touch-targets, hit-area, wcag
---

# Maintain Accessible Touch and Hit Target Sizes

Aim for comfortably sized, well-spaced controls; **44×44 CSS px** is a useful design target for many touch interfaces. WCAG 2.2 AA SC 2.5.8 sets a **24×24 CSS px** minimum for pointer targets, with exceptions including sufficient spacing, inline targets, equivalent controls, user-agent controls, and essential presentations. If a visual icon is smaller than its interactive area, enlarge the button or its hit area without causing overlap or intercepting nearby controls.

## Bad Example

```css
/* Hit target is only 16px by 16px - frustratingly difficult to tap on mobile */
.close-btn {
  width: 16px;
  height: 16px;
  padding: 0;
  border: none;
  background: none;
}
```

## Good Example

```css
/* A compact icon inside a larger, clearly interactive target */
.close-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 44px;
  height: 44px;
  padding: 0;
  border: none;
  background: transparent;
  cursor: pointer;
}

```
