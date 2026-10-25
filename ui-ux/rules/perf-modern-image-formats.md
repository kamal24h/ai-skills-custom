---
title: Serve Modern Image Formats with Responsive Sizes and Aspect-Ratio
impact: HIGH
impactDescription: Unoptimized legacy image formats and missing dimensions cause massive bandwidth waste, slow LCP times, and disruptive layout shifts (CLS).
tags: performance, images, cwv, lcp, cls, responsive
---

# Serve Modern Image Formats with Responsive Sizes and Aspect-Ratio

Images constitute the largest portion of web payload and are the primary driver of poor Largest Contentful Paint (LCP) and Cumulative Layout Shift (CLS).

Always serve next-generation formats (AVIF and WebP) using `<picture>` or `srcset`, size them responsively for mobile and desktop screens, and declare explicit `aspect-ratio` or `width`/`height` attributes to reserve placeholder space before pixels load.

## Bad Example

Single high-resolution JPEG without dimensions or responsive source variants:

```html
<!-- ❌ Heavy 3MB payload on mobile, zero reserved space causes layout jump -->
<img src="/assets/hero-banner.jpg" alt="Hero banner" class="banner" />
```

## Good Example

Multi-format responsive `<picture>` element with reserved aspect-ratio:

```html
<!-- ✅ Next-gen formats, responsive breakpoints, zero layout shift -->
<picture>
  <!-- AVIF (Highest compression efficiency) -->
  <source 
    type="image/avif" 
    srcset="/assets/hero-400.avif 400w, /assets/hero-800.avif 800w, /assets/hero-1200.avif 1200w" 
    sizes="(max-width: 640px) 100vw, 800px" 
  />
  <!-- WebP Fallback -->
  <source 
    type="image/webp" 
    srcset="/assets/hero-400.webp 400w, /assets/hero-800.webp 800w, /assets/hero-1200.webp 1200w" 
    sizes="(max-width: 640px) 100vw, 800px" 
  />
  <!-- Base element with aspect-ratio reserve -->
  <img 
    src="/assets/hero-800.webp" 
    alt="Analytics dashboard showing real-time conversion statistics" 
    width="800" 
    height="450" 
    loading="lazy" 
    decoding="async"
    style="width: 100%; height: auto; aspect-ratio: 16 / 9;" 
  />
</picture>
```
