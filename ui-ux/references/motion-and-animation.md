# Motion & Interaction Design

**Impact:** HIGH · **Prefix:** `motion-` · **Choreography, Fluid Physics & Performance**

Motion clarifies system state, spatial orientation, and cause-and-effect relationships. Purposeful motion makes digital interfaces feel continuous and physical rather than discontinuous state flips, while uncoordinated, gratuitous animation induces cognitive fatigue and performance stutter.

## Load When

- Implementing micro-interactions (button press, hover lifts, toggle switches)
- Creating enter/exit transitions (modals, drawers, dropdowns, toast alerts)
- Designing continuous spring physics and interruptible gesture transitions
- Preserving spatial continuity across page transitions using the View Transitions API
- Gating hover triggers across dense grid/list surfaces to prevent rapid strobing
- Supporting user motion preferences (`prefers-reduced-motion`)

## Rules

| Rule | Summary |
|------|---------|
| [`motion-hardware-acceleration`](../rules/motion-hardware-acceleration.md) | Prefer `transform` and `opacity` where suitable; avoid unnecessary layout work |
| [`motion-interruptible-springs`](../rules/motion-interruptible-springs.md) | Ensure interactive motion is interruptible and continuous; prefer springs over locked keyframes |
| [`motion-reduced-motion`](../rules/motion-reduced-motion.md) | Respect reduced-motion preferences with intentional alternatives; avoid blunt global wipes |

---

## Fluid Design Principles

Digital objects should obey the laws of continuous physical systems:

1. **Continuous Physical Continuity**: Prefer responsive springs and short transitions over fixed, locked keyframes.
2. **Mandatory Interruptibility**: Every animation triggered by a user must be interruptible. If a user dismisses a panel mid-open, the motion must immediately reverse or settle without completing the forward cycle.
3. **Preserve Velocity Across Boundaries**: When releasing a dragged sheet or carousel, transfer the gesture's release velocity into the settle animation.
4. **Acted Object Leads, Surroundings Yield**: In orchestrated sequences, the element directly acted upon responds instantly (0ms delay); surrounding elements yield and settle in a tight cascading stagger (30–50ms interval).

### Spring Parameter Starting Points
When configuring spring-based physics in CSS or animation libraries:
- **Snappy UI Feedback (Buttons, toggles, badges)**: Stiffness `300–400`, Damping `25–30`, Mass `0.8–1.0`
- **Surface Transitions (Drawers, sheets, modals)**: Stiffness `200–250`, Damping `22–26`, Mass `1.0–1.2`
- **Layout Reflows**: 200–350ms duration or critically damped spring (no overshoot)

---

## Spatial Continuity: View Transitions API

When an item expands from a card in a grid to a full-screen view, keep its shared identity intact rather than cutting abruptly:

```css
/* Assign a unique view-transition-name to the shared element */
.product-card-thumbnail {
  view-transition-name: active-product-image;
}
```

```javascript
// Wrap DOM mutation in document.startViewTransition
function expandProduct(productId) {
  if (!document.startViewTransition) {
    updateDOMToProductDetail(productId);
    return;
  }
  document.startViewTransition(() => {
    updateDOMToProductDetail(productId);
  });
}
```

---

## Velocity-Aware Hover Gating on Dense Surfaces

On dense data grids, card galleries, or menu lists, a user moving their pointer rapidly across the screen can trigger dozens of consecutive hover states, creating a distracting, strobing visual flash.

- **Gate fast sweeps**: Add a subtle entry delay (~40–60ms) or check pointer speed before activating heavy hover tooltips, preview popovers, or dramatic 3D lifts.
- **Instant exit**: While entry can be gently gated, exit should clear immediately on pointer departure to keep the interface feeling responsive.

---

## Duration Scales & Easing Curves

```css
:root {
  /* Duration Scale */
  --duration-instant: 100ms;  /* Direct touch/hover micro-feedback */
  --duration-short:   200ms;  /* Tooltips, dropdowns, small popovers */
  --duration-medium:  300ms;  /* Modals, drawers, expandable accordions */
  --duration-long:    450ms;  /* Major page navigation transitions */

  /* Easing Curves */
  /* Enter: Rapid start, gentle deceleration into resting place */
  --ease-out-standard: cubic-bezier(0, 0, 0.2, 1);

  /* Exit: Gradual start, accelerates off screen */
  --ease-in-standard: cubic-bezier(0.4, 0, 1, 1);

  /* Emphasized Spring: Snappy response, crisp settling */
  --ease-emphasized: cubic-bezier(0.16, 1, 0.3, 1);
}
```

---

## Animation Performance Pipeline

Browsers render updates in three sequential phases: **Layout → Paint → Composite**.
- Animating layout-driving properties (`width`, `height`, `top`, `left`, `margin`, `padding`) forces geometry recalculation on every frame, causing dropped frames (jank).
- Animating composite properties (`transform`, `opacity`) runs directly on the GPU without triggering layout or paint reflows.

```css
/* ❌ POOR: Forces synchronous layout recalculation on every frame */
.drawer-bad {
  left: -320px;
  transition: left 0.3s ease;
}
.drawer-bad.is-open {
  left: 0;
}

/* ✅ FAST: Handled purely on GPU composite thread */
.drawer-good {
  transform: translateX(-100%);
  transition: transform 0.3s var(--ease-emphasized);
}
.drawer-good.is-open {
  transform: translateX(0);
}
```

---

## Native Enter/Exit Animations (`@starting-style`)

Modern CSS supports animating elements as they transition into and out of `display: none`:

```css
.popover-menu {
  display: none;
  opacity: 0;
  transform: translateY(-8px) scale(0.96);
  transition: opacity 0.2s ease, transform 0.2s var(--ease-emphasized), display 0.2s allow-discrete;
}

.popover-menu.is-open {
  display: block;
  opacity: 1;
  transform: translateY(0) scale(1);

  /* Defines starting state immediately when rendered */
  @starting-style {
    opacity: 0;
    transform: translateY(-8px) scale(0.96);
  }
}
```

---

## Intentional Reduced Motion (`prefers-reduced-motion`)

Vestibular disorders can cause severe dizziness, nausea, and disorientation from large spatial motion or parallax scrolling.

**Never use a destructive global reset:**
```css
/* ❌ BAD: Destroys focus rings, state changes, and functional feedback */
* {
  animation: 0.01ms !important;
  transition: 0.01ms !important;
}
```

**Instead, provide intentional, non-disorienting alternatives:**
```css
/* ✅ GOOD: Preserves functional state awareness while eliminating spatial motion */
@media (prefers-reduced-motion: reduce) {
  /* Eliminate spatial translation and parallax */
  .drawer-good,
  .modal-dialog,
  .popover-menu {
    transform: none !important;
    transition: opacity 0.15s ease !important;
  }

  /* Disable infinite decorative animations */
  .decorative-orb,
  .marquee-track {
    animation: none !important;
  }

  /* Instant scroll jump without dizzying smooth scroll */
  html {
    scroll-behavior: auto !important;
  }
}
```
