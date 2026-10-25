---
title: Use the Native Inert Attribute to Disable Background Content
impact: CRITICAL
impactDescription: Failing to isolate background content during drawers, sidebars, and modals allows keyboard and screen reader focus to leak into invisible elements.
tags: html, inert, accessibility, keyboard, focus-management, drawer, modal
---

# Use the Native Inert Attribute to Disable Background Content

**Impact: CRITICAL (Keyboard and screen reader focus leaking into hidden or obscured background DOM trees violates WCAG 2.4.3)**

Use the native global HTML attribute `inert` on background page containers whenever a non-modal overlay, sliding drawer, off-canvas navigation panel, or multi-step wizard step is active.

When present on an element, the boolean `inert` attribute tells the browser to completely ignore the element and all of its descendants:
1. It removes all interactive elements inside from the sequential keyboard focus order (`Tab` navigation).
2. It completely hides the subtree from the accessibility tree (equivalent to automatic `aria-hidden="true"`).
3. It blocks all user interaction events (clicks, taps, text selection, pointer hover).

This replaces brittle, error-prone custom scripts that iteratively applied `tabindex="-1"` and `aria-hidden="true"` to dozens of background DOM nodes.

## Bad Example

Custom slide-over drawer that leaves the main document interactive to keyboard and screen reader users:

```html
<!-- Background content remains focusable behind slide-over drawer! -->
<main id="main-content">
  <button id="primary-action">Edit Profile</button>
  <a href="/settings">Settings</a>
</main>

<aside id="slide-drawer" class="drawer is-open">
  <h2>Filter Results</h2>
  <button id="close-drawer">Close</button>
  <!-- When tabbing through this drawer, focus jumps back into #main-content behind the overlay! -->
</aside>

<script>
  // Developers previously wrote 40+ lines of fragile JS to crawl the DOM
  // and manually toggle tabindex="-1" and aria-hidden on everything outside the drawer.
</script>
```

## Good Example

Declaring `inert` on the main page wrapper when the off-canvas drawer is opened:

```html
<!-- Main page container: gets marked 'inert' when drawer is active -->
<div id="page-wrapper">
  <header>
    <nav>
      <a href="/">Dashboard</a>
    </nav>
    <button type="button" id="open-filter-btn" aria-controls="filter-drawer">
      Open Filters
    </button>
  </header>

  <main id="main-content">
    <h1>Project Catalog</h1>
    <a href="/project/1">Alpha Project</a>
  </main>
</div>

<!-- Off-canvas drawer (outside page-wrapper) -->
<aside id="filter-drawer" class="drawer" aria-labelledby="filter-title" hidden>
  <div class="drawer-header">
    <h2 id="filter-title">Filter Projects</h2>
    <button type="button" id="close-filter-btn" aria-label="Close filters">✕</button>
  </div>
  <div class="drawer-body">
    <label for="status-filter">Status</label>
    <select id="status-filter">
      <option value="all">All</option>
      <option value="active">Active</option>
    </select>
  </div>
</aside>

<script>
  const pageWrapper = document.getElementById('page-wrapper');
  const drawer = document.getElementById('filter-drawer');
  const openBtn = document.getElementById('open-filter-btn');
  const closeBtn = document.getElementById('close-filter-btn');

  function openDrawer() {
    drawer.removeAttribute('hidden');
    // Lock all background content out of focus & accessibility tree with one attribute:
    pageWrapper.inert = true;
    closeBtn.focus();
  }

  function closeDrawer() {
    drawer.setAttribute('hidden', '');
    // Restore all background interactivity:
    pageWrapper.inert = false;
    openBtn.focus();
  }

  openBtn.addEventListener('click', openDrawer);
  closeBtn.addEventListener('click', closeDrawer);
</script>
```

```css
/* Style inert subtrees to visually indicate disabled state if partially visible */
[inert] {
  opacity: 0.6;
  user-select: none;
  pointer-events: none;
}

.drawer {
  position: fixed;
  top: 0;
  right: 0;
  width: 24rem;
  height: 100vh;
  background: var(--color-surface);
  box-shadow: var(--shadow-high);
  z-index: var(--z-modal);
}
```

## Why

- **Eliminates Focus Traps and Leaks**: Prevents keyboard users from accidentally navigating into background page content while interacting with an overlay.
- **Native Accessibility Tree Removal**: Screen readers behave as if the inert elements do not exist, eliminating confusing auditory clutter.
- **Pointer Event Suppression**: Browsers natively prevent pointer clicks and text selection inside inert trees without requiring custom overlay masks.
- **Zero Performance Overhead**: Handled in the browser engine's C++ layer rather than recursively mutating DOM attributes via JavaScript.
- **Clean State Management**: A single boolean property on a parent container (`element.inert = true / false`) controls the entire subtree cleanly.

## Related

- Reference: [`references/semantic-html.md`](../references/semantic-html.md)
- Reference: [`references/accessibility.md`](../references/accessibility.md)
- Rule: [`rules/html-dialog-modal-native.md`](html-dialog-modal-native.md)
- Rule: [`rules/a11y-focus-visible.md`](a11y-focus-visible.md)
