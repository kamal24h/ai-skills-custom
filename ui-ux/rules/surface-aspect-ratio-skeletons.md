---
title: Reserve Space for Media and Async Content
impact: HIGH
impactDescription: Media and async content without reserved space can cause avoidable layout shifts that disrupt reading and interaction.
tags: surfaces, layout, cls, performance, aspect-ratio, skeletons
---

# Reserve Space for Media and Async Content

Reserve space for media and asynchronous content when its dimensions can be known in advance. Use intrinsic `width` and `height` on images where available, or `aspect-ratio` for responsive media boxes. Skeletons are optional: use them only when they help users understand that content is loading, and make their geometry match the eventual content.

## Bad Example

```html
<!-- Without intrinsic dimensions, the browser may not reserve space before loading -->
<div class="product-card">
  <img src="/photos/camera.jpg" alt="Vintage Camera" />
  <h3>Vintage Camera</h3>
</div>
```

```css
.product-card img {
  width: 100%;
  height: auto;
}
```

## Good Example

```css
/* Reserves the exact 4/3 rectangular space immediately during initial layout */
.product-card .media-box {
  width: 100%;
  aspect-ratio: 4 / 3;
  border-radius: var(--radius-md);
  overflow: hidden;
  background-color: var(--color-surface-subtle);
}

.product-card img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
```
