---
title: Implement Scroll-Driven Animations with animation-timeline
impact: HIGH
impactDescription: Binding JavaScript scroll event listeners to drive animations clogs the main browser thread, causes scroll stutter, and violates 60fps interaction standards.
tags: css, animation, scroll-timeline, performance, cwv
---

# Implement Scroll-Driven Animations with animation-timeline

**Impact: HIGH (Hardware-composited scroll indicators and reveals without main-thread JS jank)**

Creating reading progress indicators, header shrinkage, or image reveals based on page scroll traditionally required listening to `window.onscroll` in JavaScript. This triggers continuous main-thread evaluation, forced reflows, and dropped frames on mobile devices.

CSS Scroll-Driven Animations decouple scroll effects from JavaScript entirely, allowing keyframe animations to be linked directly to a scroll container (`animation-timeline: scroll()`) or an element's viewport visibility (`animation-timeline: view()`).

## Bad Example

JavaScript scroll event listeners driving DOM style mutations:

```javascript
// ❌ Un-throttled scroll listener floods main thread and drops frame rates
window.addEventListener('scroll', () => {
  const scrollTotal = document.documentElement.scrollHeight - window.innerHeight;
  const progress = (window.scrollY / scrollTotal) * 100;
  progressBar.style.width = `${progress}%`; // Forces layout on every scroll tick
});
```

## Good Example

Declarative CSS Scroll Timeline:

```css
/* ✅ Driven directly by compositor thread with 60fps fluidity */
.reading-progress-bar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background-color: var(--color-action-primary);
  transform-origin: 0 50%;

  /* Animation driven by root scrollbar */
  animation: fill-progress linear;
  animation-timeline: scroll(root block);
}

@keyframes fill-progress {
  from { transform: scaleX(0); }
  to   { transform: scaleX(1); }
}
```

## Why

- **Compositor Thread Execution**: Runs directly on the GPU without competing with JavaScript execution on the main thread.
- **Zero Layout Thrashing**: Uses `transform: scaleX()` rather than modifying `width`, avoiding costly layout recalculations.
- **Battery & CPU Efficiency**: The browser skips animation calculation when the user is not actively scrolling.

## Related

- Reference: [`references/modern-css-reference.md`](../references/modern-css-reference.md)
- Reference: [`references/motion-and-animation.md`](../references/motion-and-animation.md)
