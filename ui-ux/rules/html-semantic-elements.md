---
title: Use Native Semantic HTML Elements
impact: CRITICAL
impactDescription: Divs with click handlers lack built-in keyboard navigation, role announcement, and accessible states.
tags: semantic-html, accessibility, a11y, web-standards
---

# Use Native Semantic HTML Elements

Always use native HTML elements (`<button>`, `<dialog>`, `<nav>`, `<main>`, `<a>`) for interactive and structural elements. Avoid generic `<div>` or `<span>` elements with click handlers and artificial ARIA roles.

## Bad Example

```html
<!-- Inaccessible pseudo-button: no Enter/Space key support, no focus ring, no native disabled state -->
<div class="custom-button" onclick="handleCheckout()">
  Checkout Now
</div>

<!-- Non-semantic landmark: screen reader cannot jump to main content -->
<div class="content-wrapper">
  <div class="navigation-bar">
    <div onclick="navigateHome()">Home</div>
  </div>
</div>
```

## Good Example

```html
<!-- Native button: fully accessible with Enter, Space, tab focus, and disabled support -->
<button type="button" class="btn-primary" onclick="handleCheckout()">
  Checkout Now
</button>

<!-- Semantic landmarks: natively integrated into the browser's accessibility tree -->
<header>
  <nav aria-label="Primary navigation">
    <a href="/">Home</a>
  </nav>
</header>

<main id="main-content">
  <!-- Primary content -->
</main>
```
