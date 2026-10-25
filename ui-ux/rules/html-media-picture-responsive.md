---
title: Implement Responsive Media and Art Direction with Picture and Source
impact: HIGH
impactDescription: Omitting picture elements for art direction or missing fallback img tags breaks mobile composition and destroys accessibility.
tags: html, media, picture, responsive, images, video, audio, track
---

# Implement Responsive Media and Art Direction with Picture and Source

**Impact: HIGH (Unresponsive media wastes cellular bandwidth, crops focal points on mobile, and misses accessibility captions)**

Use the `<picture>` element whenever media requires art direction (serving different crops or aspect ratios across mobile and desktop screens) or modern image format negotiation (`image/avif` with fallback to `image/webp` and JPEG).

When serving images, always embed an `<img>` element as the final child of `<picture>`. The `<img>` tag is the element that actually renders the pixels, receives accessibility announcements via `alt`, and handles layout dimensions via `width`, `height`, or CSS `aspect-ratio`. Never use CSS `background-image` for informative imagery.

For video and audio content, always provide timed text tracks using `<track kind="subtitles|captions" srclang="..." label="...">` to support deaf and hard-of-hearing users as well as muted autoplay environments.

## Bad Example

Single desktop-oriented landscape image that gets awkwardly squeezed or unreadably miniaturized on small screens:

```html
<!-- Fails art direction: Hero text/face in image is too tiny on mobile; no AVIF format negotiation -->
<div class="hero-container">
  <img src="/assets/hero-ultra-wide.jpg" alt="Hero banner" class="hero-img" />
</div>

<!-- Video lacking captions: Inaccessible to hard-of-hearing and muted mobile users -->
<video src="/assets/walkthrough.mp4" controls></video>
```

## Good Example

Responsive `<picture>` element providing portrait crop on mobile, landscape crop on desktop, modern format fallbacks, and an accessible `<video>` with caption tracks:

```html
<!-- Art Direction + Next-Gen Format Negotiation -->
<picture class="hero-media">
  <!-- Mobile Portrait Crop (under 640px) -->
  <source 
    media="(max-width: 640px)" 
    type="image/avif" 
    srcset="/assets/hero-portrait-400.avif 400w, /assets/hero-portrait-800.avif 800w" 
    sizes="100vw"
  />
  <source 
    media="(max-width: 640px)" 
    type="image/webp" 
    srcset="/assets/hero-portrait-400.webp 400w, /assets/hero-portrait-800.webp 800w" 
    sizes="100vw"
  />

  <!-- Desktop Landscape Crop (641px and above) -->
  <source 
    media="(min-width: 641px)" 
    type="image/avif" 
    srcset="/assets/hero-landscape-800.avif 800w, /assets/hero-landscape-1600.avif 1600w" 
    sizes="(max-width: 1200px) 100vw, 1200px"
  />
  <source 
    media="(min-width: 641px)" 
    type="image/webp" 
    srcset="/assets/hero-landscape-800.webp 800w, /assets/hero-landscape-1600.webp 1600w" 
    sizes="(max-width: 1200px) 100vw, 1200px"
  />

  <!-- Fallback and Rendering Engine -->
  <img 
    src="/assets/hero-landscape-800.jpg" 
    alt="Founder reviewing team analytics on an interactive tablet dashboard" 
    width="1600" 
    height="900" 
    loading="eager" 
    fetchpriority="high"
    decoding="async"
    class="responsive-hero-img"
  />
</picture>

<!-- Accessible video with closed captions and subtitles -->
<video controls preload="metadata" poster="/assets/video-poster.webp" class="product-video">
  <source src="/assets/product-tour.mp4" type="video/mp4" />
  <source src="/assets/product-tour.webm" type="video/webm" />
  <track 
    kind="captions" 
    src="/assets/captions-en.vtt" 
    srclang="en" 
    label="English captions" 
    default 
  />
  <p>
    Your browser does not support HTML5 video. 
    <a href="/assets/product-tour.mp4">Download the tour video</a>.
  </p>
</video>
```

```css
.responsive-hero-img {
  width: 100%;
  height: auto;
  display: block;
  object-fit: cover;
}

@media (max-width: 640px) {
  .responsive-hero-img {
    aspect-ratio: 4 / 5; /* Taller crop for portrait mobile viewports */
  }
}

@media (min-width: 641px) {
  .responsive-hero-img {
    aspect-ratio: 16 / 9; /* Wide cinematic crop for desktop */
  }
}
```

## Why

- **True Art Direction**: Adapts framing and focal points to the viewer's device form factor rather than naively shrinking wide desktop landscapes down to mobile illegibility.
- **Bandwidth Optimization**: Mobile devices download specifically tailored, tightly cropped small files rather than downloading 2MB desktop assets.
- **Progressive Modern Formats**: Modern browsers receive high-compression AVIF/WebP assets while older environments seamlessly fall back to JPEG/PNG.
- **Media Accessibility**: `<track>` elements ensure video and audio content conforms to WCAG 2.2 Level A criteria (SC 1.2.2 Captions Prerecorded).
- **Core Web Vitals Protection**: Combining explicit `width`, `height`, and `aspect-ratio` reserves layout dimensions ahead of download, eliminating Cumulative Layout Shift (CLS).

## Related

- Reference: [`references/semantic-html.md`](../references/semantic-html.md)
- Reference: [`references/web-performance-and-cwv.md`](../references/web-performance-and-cwv.md)
- Rule: [`rules/perf-modern-image-formats.md`](perf-modern-image-formats.md)
- Rule: [`rules/surface-aspect-ratio-skeletons.md`](surface-aspect-ratio-skeletons.md)
