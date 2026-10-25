# Component UX Patterns

**Impact:** HIGH · **Prefix:** `comp-` · **Interaction Blueprints & Web Standards**

Consistent, predictable interaction models across common UI components allow users to apply their existing mental models without friction. Modern web standards (such as native `<dialog>` and the Popover API) provide accessible, resilient building blocks with minimal custom JavaScript.

## Load When

- Implementing data tables, modals, drawers, tabs, or tooltips
- Designing empty states, loading placeholders, and skeleton loaders
- Managing overlay layers and popovers using modern web APIs
- Building toast notifications and transient alert banners
- Refactoring custom JavaScript components into native web primitives

## Rules

| Rule | Summary |
|------|---------|
| [`surface-aspect-ratio-skeletons`](../rules/surface-aspect-ratio-skeletons.md) | Reserve known media dimensions to reduce layout shift; use skeletons when useful |
| [`layout-scroll-shadows`](../rules/layout-scroll-shadows.md) | Indicate scrollable overflow regions with visual scroll-shadow affordances |
| [`type-tabular-numerals`](../rules/type-tabular-numerals.md) | Apply tabular figures (`tabular-nums`) to numerical data, tables, and counters |

---

## Overlay Hierarchy: Modals vs Drawers vs Popovers

| Component | Mechanism | When to Use | Dismiss Behavior |
|---|---|---|---|
| **Modal Dialog** | `<dialog>.showModal()` | Critical decisions, focused destructive workflows | Escape key, backdrop click, explicit cancel/save |
| **Drawer / Sheet** | `<dialog>` or composite panel | Complex filters, mobile navigation menus, item details preview | Escape key, backdrop click, close button |
| **Popover** | Native `popover="auto"` | Contextual menus, profile dropdowns, light tooltips | Light-dismiss (clicking anywhere outside automatically closes) |

### Native Popover Example (HTML & CSS Only)

```html
<!-- Trigger and Popover connected purely via HTML attributes -->
<button type="button" popovertarget="user-menu" class="btn-avatar">
  <img src="/avatar.jpg" alt="User avatar" class="avatar-sm" />
</button>

<div id="user-menu" popover class="menu-popover">
  <nav aria-label="User account">
    <a href="/profile">My Profile</a>
    <a href="/settings">Account Settings</a>
    <hr />
    <button type="button" class="btn-text">Sign Out</button>
  </nav>
</div>
```

```css
.menu-popover {
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  padding: var(--space-2);
  box-shadow: var(--shadow-medium);
  margin-top: 0.5rem;
}

/* Native top-layer auto-positioning and backdrop styling */
.menu-popover::backdrop {
  background: transparent;
}

/* CSS Anchor Positioning (replaces third-party floating libraries) */
.btn-avatar {
  anchor-name: --avatar-anchor;
}

.menu-popover {
  position-anchor: --avatar-anchor;
  top: anchor(bottom);
  left: anchor(start);
  margin-top: 0.5rem;
}
```

---

## Responsive Data Tables

Data tables frequently overflow on narrow viewports. Choose one of two clean patterns:

### 1. Horizontal Scroll with Scroll-Shadow Affordances
Keep tabular structure intact inside a container that hints at hidden overflow content via gradient shadows:

```html
<div class="table-scroll-container" tabindex="0" role="region" aria-label="Order summary table">
  <table>
    <thead>
      <tr>
        <th scope="col">Order ID</th>
        <th scope="col">Date</th>
        <th scope="col">Customer</th>
        <th scope="col">Status</th>
        <th scope="col" class="numeric">Total</th>
      </tr>
    </thead>
    <tbody>
      <!-- Table rows with tabular numbers on total -->
    </tbody>
  </table>
</div>
```

```css
.table-scroll-container {
  overflow-x: auto;
  /* Visual scroll affordance gradient */
  background:
    radial-gradient(farthest-side at 0% 50%, rgba(0, 0, 0, 0.12), transparent) left,
    radial-gradient(farthest-side at 100% 50%, rgba(0, 0, 0, 0.12), transparent) right;
  background-repeat: no-repeat;
  background-size: 10px 100%;
}
```

### 2. Mobile Card Transformation
On narrow viewports, collapse table rows into card summaries using CSS data attributes:

```css
@media (max-width: 40rem) {
  table.responsive-cards,
  table.responsive-cards thead,
  table.responsive-cards tbody,
  table.responsive-cards th,
  table.responsive-cards td,
  table.responsive-cards tr {
    display: block;
  }

  table.responsive-cards thead {
    position: absolute;
    top: -9999px;
    left: -9999px;
  }

  table.responsive-cards tr {
    border: 1px solid var(--color-border);
    border-radius: var(--radius-md);
    margin-bottom: 1rem;
    padding: 0.75rem;
  }

  table.responsive-cards td {
    display: flex;
    justify-content: space-between;
    padding: 0.5rem 0;
    border-bottom: 1px solid var(--color-border-subtle);
  }

  table.responsive-cards td::before {
    content: attr(data-label);
    font-weight: 600;
    color: var(--color-text-secondary);
  }
}
```

---

## Skeleton Loaders & Cumulative Layout Shift (CLS)

Reserve space for media and asynchronous content when its size is known to prevent layout shifts. Skeletons indicate where content will load; keep them close to the real content shape and avoid excessive motion when a static placeholder is sufficient:

```css
.skeleton-card {
  aspect-ratio: 16 / 9;
  border-radius: var(--radius-md);
  background: linear-gradient(
    90deg,
    oklch(0.92 0.005 250) 25%,
    oklch(0.96 0.005 250) 50%,
    oklch(0.92 0.005 250) 75%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
}

@keyframes shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

@media (prefers-reduced-motion: reduce) {
  .skeleton-card {
    animation: none;
    background: oklch(0.92 0.005 250);
  }
}
```
