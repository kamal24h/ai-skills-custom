---
title: Build Touch Carousels with CSS Scroll Snap Over Heavy JS Plugins
impact: HIGH
impactDescription: Bulky JavaScript slider libraries add 50KB+ of bundle size, hijack native touch scrolling, and break accessibility tab order.
tags: css, scroll-snap, carousel, mobile, touch
---

# Build Touch Carousels with CSS Scroll Snap Over Heavy JS Plugins

**Impact: HIGH (Native, hardware-accelerated flick scrolling without third-party slider weight)**

Traditional JavaScript slider plugins (like Swiper or Slick) add significant bundle overhead, hijack native scrolling physics, and frequently fail keyboard navigation.

Native CSS Scroll Snap (`scroll-snap-type: x mandatory`, `scroll-snap-align: start`) provides 60fps, touch-friendly, momentum-preserving carousel mechanics using the browser's native scrolling engine.

## Bad Example

Complex JavaScript slider initialization:

```javascript
// ❌ 60KB library hijacking native scrolling and touch events
const slider = new HeavySlider('.slider-container', {
  slidesPerView: 3,
  spaceBetween: 16,
  touchRatio: 1
});
```

## Good Example

Pure CSS Scroll Snap with keyboard accessibility:

```html
<div class="carousel" tabindex="0" role="region" aria-label="Product showcase">
  <article class="carousel-card">Card 1</article>
  <article class="carousel-card">Card 2</article>
  <article class="carousel-card">Card 3</article>
</div>
```

```css
/* ✅ 100% native browser physics, instant trackpad and touch flicking */
.carousel {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-padding-inline: var(--space-4);
  gap: var(--space-4);
  overscroll-behavior-x: contain;
  -webkit-overflow-scrolling: touch;
  padding-block: var(--space-2);
}

.carousel-card {
  flex: 0 0 calc(100% - 2rem);
  scroll-snap-align: start;
  scroll-snap-stop: normal;
}

@media (min-width: 48rem) {
  .carousel-card {
    flex: 0 0 calc(33.333% - 1rem);
  }
}
```

## Why

- **Native Physics**: Respects the device's native flick speed, momentum, and trackpad gestures.
- **Accessibility**: Standard scroll containers maintain natural DOM tab order and screen reader reading sequences.
- **Zero JS Weight**: Completely eliminates slider dependencies from application bundles.

## Related

- Reference: [`references/modern-css-reference.md`](../references/modern-css-reference.md)
- Reference: [`references/layout-and-responsive.md`](../references/layout-and-responsive.md)
