# Modern CSS Layout Cookbook

**Standards Baseline:** W3C CSS Specifications & MDN Layout Cookbook  
**Focus:** Native, Resilient Component & Page Layout Recipes Using Flexbox, Grid, and Modern CSS

This reference provides production-ready, framework-agnostic CSS recipes for common web interface patterns, eliminating legacy float hacks, fragile absolute positioning, and unnecessary JavaScript layout calculations.

---

## 1. Centering an Element

Modern CSS provides three distinct ways to center elements horizontally and vertically depending on layout context:

### A. Grid Container (One-Liner)
Ideal when centering single or multiple children inside a container:

```css
.center-container {
  display: grid;
  place-content: center; /* Centers along both block and inline axes */
  min-height: 100dvh;
}
```

### B. Auto Margins in Flex/Grid
When an item needs to self-center within available track space:

```css
.modal-content {
  margin: auto; /* Centers element within flex or grid parent */
}
```

### C. Flexbox Alignment
```css
.flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

---

## 2. Sticky Footer Page Layout

Keeps the footer pinned to the bottom of the viewport when content is short, but allows it to push down naturally when content exceeds screen height.

```html
<div class="page-layout">
  <header>Header content</header>
  <main>Main content</main>
  <footer>Footer content</footer>
</div>
```

```css
.page-layout {
  display: grid;
  grid-template-rows: auto 1fr auto; /* Header, expandable content, footer */
  min-height: 100dvh; /* Adapts to dynamic mobile browser address bars */
}
```

---

## 3. The Media Object Pattern

Displays an image, avatar, or icon alongside body text, maintaining consistent alignment regardless of text length:

```html
<div class="media-object">
  <img src="/avatar.webp" alt="Sarah Connor" class="media-figure" width="48" height="48" />
  <div class="media-body">
    <h3 class="media-heading">Sarah Connor</h3>
    <p>Engineering Director at Cyberdyne Systems.</p>
  </div>
</div>
```

```css
.media-object {
  display: flex;
  align-items: flex-start;
  gap: var(--space-4);
}

.media-figure {
  flex-shrink: 0;
  border-radius: var(--radius-full);
  aspect-ratio: 1 / 1;
  object-fit: cover;
}

.media-body {
  min-width: 0; /* Prevents flex blowout from long strings */
  flex: 1 1 auto;
}
```

---

## 4. Split Navigation Bar

Common navigation pattern where the site logo sits on the left and utility actions (account, logout, search) sit on the right:

```html
<nav class="split-nav" aria-label="Main navigation">
  <a href="/" class="nav-brand">Platform</a>
  <ul class="nav-links">
    <li><a href="/features">Features</a></li>
    <li><a href="/pricing">Pricing</a></li>
    <li class="nav-split"><a href="/login">Sign In</a></li>
    <li><a href="/signup" class="btn-primary">Get Started</a></li>
  </ul>
</nav>
```

```css
.split-nav .nav-links {
  display: flex;
  align-items: center;
  gap: var(--space-4);
  list-style: none;
  margin: 0;
  padding: 0;
}

/* margin-inline-start: auto pushes item and subsequent siblings to the far right */
.nav-split {
  margin-inline-start: auto;
}
```

---

## 5. Breadcrumb Navigation

Provides clear hierarchical orientation for deep content architectures:

```html
<nav aria-label="Breadcrumb" class="breadcrumbs">
  <ol>
    <li><a href="/dashboard">Dashboard</a></li>
    <li><a href="/dashboard/projects">Projects</a></li>
    <li aria-current="page">Infrastructure Q3</li>
  </ol>
</nav>
```

```css
.breadcrumbs ol {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: var(--space-2);
  list-style: none;
  margin: 0;
  padding: 0;
  color: var(--color-text-secondary);
}

.breadcrumbs li:not(:last-child)::after {
  content: "/";
  margin-inline-start: var(--space-2);
  color: var(--color-text-muted);
  speak: never;
  aria-hidden: true;
}

.breadcrumbs [aria-current="page"] {
  color: var(--color-text-primary);
  font-weight: 600;
}
```

---

## 6. Card Layout with Pinned Action Footers

When multiple cards sit in a responsive row, varying description lengths often push action buttons to misaligned vertical positions. Use CSS Subgrid or Flexbox column pinning:

```html
<div class="card-grid">
  <article class="card">
    <div class="card-body">
      <h3>Starter Plan</h3>
      <p>Basic tier description with short text.</p>
    </div>
    <div class="card-footer">
      <button type="button" class="btn-primary">Select Plan</button>
    </div>
  </article>
</div>
```

```css
.card {
  display: flex;
  flex-direction: column;
  padding: var(--space-6);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  background-color: var(--color-surface);
}

.card-body {
  flex: 1 1 auto; /* Expands to push footer downward */
}

.card-footer {
  margin-top: var(--space-4);
}
```

---

## 7. Pagination Controls

Keyboard-navigable, accessible pagination with active page semantics:

```html
<nav aria-label="Pagination" class="pagination">
  <ul class="pagination-list">
    <li><button type="button" class="btn-page" disabled aria-label="Previous page">←</button></li>
    <li><button type="button" class="btn-page" aria-current="page">1</button></li>
    <li><button type="button" class="btn-page">2</button></li>
    <li><button type="button" class="btn-page">3</button></li>
    <li><span class="pagination-ellipsis" aria-hidden="true">…</span></li>
    <li><button type="button" class="btn-page">14</button></li>
    <li><button type="button" class="btn-page" aria-label="Next page">→</button></li>
  </ul>
</nav>
```

```css
.pagination-list {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  list-style: none;
  margin: 0;
  padding: 0;
}

.btn-page {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 2.5rem;
  height: 2.5rem;
  padding-inline: var(--space-3);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  background: var(--color-surface);
  font-variant-numeric: tabular-nums;
  cursor: pointer;
}

.btn-page[aria-current="page"] {
  background-color: var(--color-action-primary);
  color: var(--color-text-on-action);
  border-color: var(--color-action-primary);
  font-weight: 600;
}
```
