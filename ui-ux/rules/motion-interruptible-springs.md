---
title: Ensure Interactive Motion is Interruptible and Continuous
impact: HIGH
impactDescription: Long, non-interruptible keyframe animations lock user control, delay task execution, and feel unresponsive compared to physical systems.
tags: motion, animations, fluid-design, springs, interruptibility
---

# Ensure Interactive Motion is Interruptible and Continuous

Digital interfaces feel physical when they behave like continuous, responsive systems rather than locked, predetermined state flips. If a user clicks to dismiss a drawer while it is currently animating open, the interface must immediately redirect or reverse rather than forcing the user to wait out the animation.

Prefer natural springs, short ease-out curves (150–300ms), and direct CSS transitions over multi-step locked `@keyframes` for interactive surfaces.

## Bad Example

Long locked keyframe animations that block or ignore rapid user interaction:

```css
/* ❌ 800ms locked animation: user must wait before interacting */
.modal-overlay {
  animation: slideAndRotateIn 0.8s cubic-bezier(0.2, 0.9, 0.3, 1) forwards;
}

@keyframes slideAndRotateIn {
  0% { transform: translateY(100%) rotate(-5deg); opacity: 0; }
  60% { transform: translateY(-10px) rotate(2deg); opacity: 0.8; }
  100% { transform: translateY(0) rotate(0deg); opacity: 1; }
}
```

## Good Example

Short, snappy CSS transitions that cleanly reverse when interrupted:

```css
/* ✅ Interruptible transition: immediately reverses if state changes mid-flight */
.modal-overlay {
  transform: translateY(0) scale(1);
  opacity: 1;
  transition:
    transform 0.25s cubic-bezier(0.16, 1, 0.3, 1),
    opacity 0.2s ease;
}

.modal-overlay[hidden] {
  display: block;
  pointer-events: none;
  transform: translateY(12px) scale(0.97);
  opacity: 0;
}
```
