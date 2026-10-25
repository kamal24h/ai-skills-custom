---
title: Define Animatable Tokens with @property Typed Custom Properties
impact: MEDIUM
impactDescription: Standard CSS variables cannot be smoothly transitioned or animated because the browser treats them as untyped string tokens.
tags: css, at-rules, custom-properties, animation, tokens
---

# Define Animatable Tokens with @property Typed Custom Properties

**Impact: MEDIUM (Enables smooth transitions on gradients, angles, and custom design tokens)**

Standard CSS custom properties (variables) are untyped tokens. When a property like a gradient stop or rotation angle updates, the browser cannot interpolate between string values, causing transitions and keyframe animations on custom properties to snap abruptly.

The `@property` at-rule registers a typed CSS variable with explicit type checking (`syntax`), inheritance behavior, and an initial fallback value, enabling smooth browser-interpolated transitions.

## Bad Example

Attempting to transition untyped CSS variables in gradients:

```css
:root {
  --gradient-stop: 20%;
}

/* ❌ Does not animate smoothly; snaps abruptly because --gradient-stop is an untyped string */
.hero-card {
  background: linear-gradient(to right, #2563eb var(--gradient-stop), #1e40af);
  transition: --gradient-stop 0.3s ease;
}

.hero-card:hover {
  --gradient-stop: 80%;
}
```

## Good Example

Registering typed custom properties with `@property`:

```css
/* ✅ Informs the browser engine that this variable represents a percentage value */
@property --gradient-stop {
  syntax: "<percentage>";
  inherits: false;
  initial-value: 20%;
}

.hero-card {
  background: linear-gradient(to right, var(--color-action-primary) var(--gradient-stop), var(--color-canvas));
  transition: --gradient-stop 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.hero-card:hover {
  --gradient-stop: 80%; /* Smoothly animates the gradient stop position */
}
```

## Why

- **Smooth Interpolation**: Enables mathematical interpolation across numbers, lengths, percentages, and angles in gradients and animations.
- **Type Safety**: Invalid values are rejected and safely fall back to `initial-value`.
- **CSS-Only Micro-Interactions**: Eliminates JavaScript canvas or SVG workarounds for complex interactive gradient and border effects.

## Related

- Reference: [`references/modern-css-reference.md`](../references/modern-css-reference.md)
- Reference: [`references/motion-and-animation.md`](../references/motion-and-animation.md)
