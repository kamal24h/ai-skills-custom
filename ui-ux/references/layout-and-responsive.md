# Layout & Responsive Design

**Impact:** HIGH · **Prefix:** `layout-` · **Modern CSS & Fluid Adaptability**

Modern web layouts must adapt effortlessly to infinite viewport sizes, split screens, foldable displays, and modular parent containers without fragile hardcoded device breakpoints. Layout turns product priority into reading order, grouping, cadence, and usable space.

## Load When

- Building page layouts, grids, split columns, and content architectures
- Adapting interfaces across screen contexts (Desktop, Tablet, Mobile, Print)
- Replacing rigid viewport media queries with modular container queries
- Aligning card headers, footers, and content using CSS Subgrid
- Auditing visual hierarchy using the Squint Test

## Rules

| Rule | Summary |
|------|---------|
| [`layout-container-queries`](../rules/layout-container-queries.md) | Container queries (`@container`) over rigid viewport media queries for modular components |
| [`layout-proximity-over-borders`](../rules/layout-proximity-over-borders.md) | Establish grouping through whitespace proximity over box borders; more space above headings |
| [`layout-scroll-shadows`](../rules/layout-scroll-shadows.md) | Indicate scrollable overflow regions with visual scroll-shadow affordances |

---

## The Squint Test for Visual Hierarchy

Before adjusting grid columns or margins, apply the squint test: squint your eyes until all text blurs into indistinct shapes.
- Can you immediately identify the primary element, the secondary element, and the major groupings in order?
- If the blurred page looks like an undifferentiated soup of equally weighted cards, the layout lacks hierarchical contrast.
- Establish visual rank through scale contrast, distinct background tone, or deliberate asymmetric width.

---

## Proximity, Rhythm & Cadence

- **Tight grouping, generous separation**: Keep closely related items (e.g. icon + label, headline + body) close together (`gap: var(--space-2)` to `var(--space-3)`). Separate distinct conceptual blocks generously (`gap: var(--space-8)` to `var(--space-12)`).
- **Heading vertical cadence**: A heading introduces the content beneath it. Always allocate noticeably more space *above* a heading than *below* it (`margin-top: 2.5rem; margin-bottom: 0.5rem`). Equidistant margins leave headings visually detached and floating.
- **Density modes**: Calibrate density to user intent:
  - *Operate & Data-Entry*: Compact density, minimal padding, high row count.
  - *Read & Consume*: Generous line-height, constrained measure (65ch), ample breathing room.
  - *Persuade & Discover*: Bold scale contrast, expressive whitespace, asymmetric cadence.

---

## Context Adaptation Strategies

Adaptation is rethinking the experience for the target screen and input context, not merely scaling pixels down.

### 1. Desktop to Mobile Adaptation
- **Reflow structure**: Collapse multi-column layouts to single-column vertical stacks.
- **Touch ergonomics**: Ensure all interactive targets meet at least 44×44 CSS px; place primary navigation and frequent actions within comfortable thumb reach (bottom navigation bars, bottom sheets).
- **Progressive disclosure**: Surface primary content upfront; tuck secondary filters and metadata into drawers or expandable disclosures (`<details>`).
- **Input font size**: Enforce at least 16 CSS px (`max(1rem, 16px)`) to prevent automatic mobile browser viewport zoom.

### 2. Mobile to Desktop Adaptation
- **Horizontal space utilization**: Shift from vertical scrolling to multi-column arrangements, persistent side navigation, and side-by-side master-detail panels.
- **Max-width constraints**: Restrict main content wrappers (`max-width: 80rem / 1280px` or `90rem / 1440px`) centered with `margin-inline: auto`. Never let text blocks or forms stretch unconstrained across 4K or ultrawide monitors.
- **Pointer capabilities**: Enhance with hover tooltips, keyboard shortcuts, and multi-row data tables.

### 3. Tablet Adaptation (Hybrid Approach)
- **Master-detail views**: Use split two-column views (list on the left, active item details on the right).
- **Orientation adaptability**: Reorganize dynamically between portrait (stacked/drawer) and landscape (persistent split panes).

### 4. Print Adaptation (`@media print`)
- Remove navigation headers, sticky banners, footers, search bars, and interactive buttons.
- Force background colors to white and text to crisp black for ink conservation.
- Expand truncated text, reveal destination URLs after links (`a[href^="http"]::after { content: " (" attr(href) ")"; }`), and insert clean page breaks:
```css
@media print {
  header, nav, footer, button, .no-print {
    display: none !important;
  }
  body {
    background: #fff;
    color: #000;
  }
  article {
    break-inside: avoid;
    break-after: auto;
  }
}
```

### 5. Email HTML Constraints
- Restrict layout width to 600px maximum.
- Use single-column layouts with inline CSS styling for email client engine compatibility.
- Ensure large, unambiguous CTA buttons (not fragile inline text links).

---

## Modern CSS Layout Techniques

### Container Queries (`@container`)
Components should adapt based on the size of their immediate container, not the viewport. A card in a narrow sidebar should look like a mobile card even on a wide desktop screen.

```css
/* 1. Establish containment context on parent */
.card-wrapper {
  container-type: inline-size;
  container-name: card;
}

/* 2. Base card layout (stacked) */
.user-card {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

/* 3. Horizontal card when parent container is at least 400px */
@container card (min-width: 25rem) {
  .user-card {
    flex-direction: row;
    align-items: center;
  }
}
```

### Harmonizing Card Heights with CSS Subgrid
Unequal content lengths often cause misaligned buttons and headers across adjacent grid cards. CSS Subgrid aligns children across the parent row track:

```css
.cards-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(18rem, 1fr));
  gap: 1.5rem;
}

.card-item {
  display: grid;
  /* Card participates in 3 parent row tracks: header, body, footer */
  grid-row: span 3;
  grid-template-rows: subgrid;
  padding: 1.5rem;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
}
```

### Mobile Safe Areas & Dynamic Viewport Units
Ensure fixed elements respect mobile display cutouts and browser address bars:

```css
/* Dynamic viewport unit accounts for address bar showing/hiding */
.hero-screen {
  min-height: 100dvh;
}

/* Respect hardware notches and navigation bars */
.bottom-nav {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  padding-bottom: max(1rem, env(safe-area-inset-bottom));
  padding-left: max(1rem, env(safe-area-inset-left));
  padding-right: max(1rem, env(safe-area-inset-right));
}
```
