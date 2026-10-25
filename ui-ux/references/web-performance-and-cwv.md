# Web Performance & Core Web Vitals (CWV)

**Impact:** HIGH · **Prefix:** `perf-` · **Speed as a Foundational UX Quality**

Performance is an intrinsic component of user experience. Latency degrades perceived quality, causes rage clicks, and triggers drop-off. Modern web performance focuses on user-centric metrics: perceived loading speed (LCP), interaction responsiveness (INP), and visual stability (CLS).

## Load When

- Designing or building media-heavy pages, hero sections, and image galleries
- Implementing client-side data filtering, long lists, and data grids
- Structuring font loading stacks and critical CSS assets
- Auditing runtime animation jank or scroll stutter
- Preventing layout thrashing and cumulative layout shifts

## Rules

| Rule | Summary |
|------|---------|
| [`perf-prevent-layout-thrashing`](../rules/perf-prevent-layout-thrashing.md) | Batch DOM reads before writes; avoid interleaved geometry queries in animation or loops |
| [`perf-modern-image-formats`](../rules/perf-modern-image-formats.md) | Use modern formats (AVIF/WebP) with explicit `aspect-ratio` and responsive `srcset` |

---

## Core Web Vitals UX Impact

| Metric | Target | UX Meaning | Primary Culprits |
|---|---|---|---|
| **LCP** (Largest Contentful Paint) | `< 2.5s` | "Is the page actually useful yet?" | Unoptimized hero images, render-blocking CSS/JS, slow server response |
| **INP** (Interaction to Next Paint) | `< 200ms` | "Does the interface respond when I click?" | Heavy JavaScript on main thread, un-debounced event listeners, long tasks |
| **CLS** (Cumulative Layout Shift) | `< 0.1` | "Did the button just jump away as I clicked it?" | Images without dimensions, dynamically injected banners, web font swap shifts |

---

## Asset Loading Optimization

### 1. Modern Responsive Images
Never load a 3000px desktop JPEG on a mobile screen. Serve next-gen formats with explicit dimensions to eradicate CLS:

```html
<picture>
  <!-- Modern AVIF for supporting browsers -->
  <source type="image/avif" srcset="hero-400.avif 400w, hero-800.avif 800w, hero-1200.avif 1200w" sizes="(max-width: 600px) 100vw, 800px">
  <!-- Fallback WebP -->
  <source type="image/webp" srcset="hero-400.webp 400w, hero-800.webp 800w, hero-1200.webp 1200w" sizes="(max-width: 600px) 100vw, 800px">
  <!-- Default element with explicit aspect ratio to prevent CLS -->
  <img 
    src="hero-800.webp" 
    alt="Platform overview dashboard showing real-time analytics" 
    width="800" 
    height="450" 
    loading="lazy" 
    decoding="async"
    style="width: 100%; height: auto; aspect-ratio: 16 / 9;"
  />
</picture>
```
*Note: The primary hero image above the fold should use `loading="eager"` (or omit `loading="lazy"`) and be preloaded via `<link rel="preload">` in the document `<head>`.*

### 2. High-Performance Font Loading
Custom web fonts must not cause invisible text (FOIT) or sudden layout shifts (FOUT):

```css
@font-face {
  font-family: 'Inter';
  src: url('/fonts/inter-latin.woff2') format('woff2');
  font-display: swap;              /* Show fallback immediately, swap when loaded */
  font-weight: 100 900;             /* Variable font cuts payload dramatically */
  unicode-range: U+0000-00FF, ...;  /* Subset to characters actually used */
}
```

---

## Rendering & Runtime Performance

### 1. Eliminating Layout Thrashing
Layout thrashing occurs when JavaScript interleaves DOM reads (forcing the browser to recalculate geometric layout) with DOM writes:

```javascript
// ❌ BAD: Alternating read and write forces layout recalculation on every iteration
cards.forEach(card => {
  const height = card.offsetHeight; // READ: Forces synchronous layout
  card.style.height = `${height * 1.2}px`; // WRITE: Invalidate layout
});

// ✅ GOOD: Batch all reads first, then batch all writes
const heights = cards.map(card => card.offsetHeight); // Batch READS
cards.forEach((card, index) => {
  card.style.height = `${heights[index] * 1.2}px`; // Batch WRITES
});
```

### 2. Offscreen Rendering Containment: `content-visibility`
For long articles, comment sections, or infinite lists, tell the browser engine to skip layout and painting for offscreen content until it nears the viewport:

```css
.long-feed-item,
.comment-card {
  /* Skips rendering offscreen content; drastically reduces initial paint time */
  content-visibility: auto;
  /* Reserves approximate placeholder space to preserve scrollbar accuracy */
  contain-intrinsic-size: auto 180px;
}
```

### 3. GPU-Accelerated Animation Pipeline
Confine animations to properties that composite directly on the GPU without triggering Layout or Paint:

- **GPU Composite Properties (Smooth 60fps)**: `transform`, `opacity`
- **Expensive Layout Properties (Avoid Animating)**: `width`, `height`, `top`, `left`, `margin`, `padding`
- **Expensive Paint Properties (Use Sparingly / Isolate Area)**: `box-shadow`, `filter`, `backdrop-filter`

```css
/* ✅ 60fps GPU acceleration */
.modal-enter {
  transform: translateY(0) scale(1);
  opacity: 1;
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.2s ease;
}

/* ❌ Avoid: Triggers layout on every frame */
.modal-enter-bad {
  top: 100px;
  height: 400px;
  transition: top 0.25s ease, height 0.25s ease;
}
```
