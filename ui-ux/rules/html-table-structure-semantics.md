---
title: Structure Data Tables with Explicit Semantics and Header Scopes
impact: CRITICAL
impactDescription: Div tables or tables lacking caption, thead, and th scope fail screen reader data navigation and disorient users navigating multi-dimensional datasets.
tags: html, tables, semantics, accessibility, a11y, data-grid
---

# Structure Data Tables with Explicit Semantics and Header Scopes

**Impact: CRITICAL (Unsemantic or div-based tables fail table navigation mode in screen readers)**

Always structure tabular comparison data and multi-column metrics with semantic HTML table elements: `<table>`, `<caption>`, `<thead>`, `<tbody>`, `<tfoot>`, and `<th scope="col|row">`. Do not construct data tables out of generic `<div>` grids or CSS flexboxes when presenting relational data.

Every data table must have a concise, descriptive `<caption>` describing the purpose of the dataset. Column headers must declare `<th scope="col">` and row headers must declare `<th scope="row">` so that assistive technologies announce the active column and row context as users navigate between individual cells (`<td>`).

For responsive viewports, wrap the `<table>` in an accessible scroll container configured with `tabindex="0"`, `role="region"`, and an `aria-labelledby` or `aria-label` attribute so keyboard users can scroll through overflowing columns.

## Bad Example

Div-based pseudo-table lacking table semantics, header relationships, and caption context:

```html
<!-- Inaccessible div grid: screen reader announces arbitrary text blocks without row/col coordinates -->
<div class="custom-table">
  <div class="table-header">
    <div class="col">Plan</div>
    <div class="col">Storage</div>
    <div class="col">Price</div>
  </div>
  <div class="table-row">
    <div class="col">Starter</div>
    <div class="col">10 GB</div>
    <div class="col">$9/mo</div>
  </div>
  <div class="table-row">
    <div class="col">Enterprise</div>
    <div class="col">Unlimited</div>
    <div class="col">$99/mo</div>
  </div>
</div>
```

## Good Example

Semantic `<table>` with explicit `<caption>`, header scopes (`scope="col"` and `scope="row"`), and an accessible horizontal scroll container:

```html
<!-- Accessible scrollable wrapper for small viewports -->
<div 
  class="table-scroll-container" 
  tabindex="0" 
  role="region" 
  aria-labelledby="plans-table-caption"
>
  <table class="data-table">
    <caption id="plans-table-caption">
      Cloud Subscription Plans & Storage Limits (2026)
    </caption>
    
    <colgroup>
      <col class="col-plan" />
      <col class="col-storage" />
      <col class="col-bandwidth" />
      <col class="col-price" />
    </colgroup>

    <thead>
      <tr>
        <th scope="col">Plan Tier</th>
        <th scope="col">Storage Space</th>
        <th scope="col">Monthly Bandwidth</th>
        <th scope="col">Price</th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th scope="row">Starter</th>
        <td>10 GB SSD</td>
        <td>100 GB</td>
        <td class="numeric">$9/mo</td>
      </tr>
      <tr>
        <th scope="row">Professional</th>
        <td>100 GB NVMe</td>
        <td>1 TB</td>
        <td class="numeric">$29/mo</td>
      </tr>
      <tr>
        <th scope="row">Enterprise</th>
        <td>Unlimited NVMe</td>
        <td>Unlimited</td>
        <td class="numeric">$99/mo</td>
      </tr>
    </tbody>

    <tfoot>
      <tr>
        <td colspan="3">All plans include automated daily backups and 24/7 SLA.</td>
        <td class="numeric">Billed annually</td>
      </tr>
    </tfoot>
  </table>
</div>
```

```css
/* Responsive scroll container and tabular figures */
.table-scroll-container {
  overflow-x: auto;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
}

.table-scroll-container:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

.data-table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
  font-size: var(--text-sm);
}

.data-table caption {
  padding: var(--space-3) var(--space-4);
  font-weight: 600;
  text-align: left;
  color: var(--color-text-primary);
  background-color: var(--color-surface-subtle);
  border-bottom: 1px solid var(--color-border);
}

.data-table th,
.data-table td {
  padding: var(--space-3) var(--space-4);
  border-bottom: 1px solid var(--color-border);
}

.data-table th[scope="col"] {
  background-color: var(--color-surface-muted);
  font-weight: 600;
  color: var(--color-text-secondary);
}

.data-table th[scope="row"] {
  font-weight: 600;
  color: var(--color-text-primary);
}

.data-table .numeric {
  text-align: right;
  font-variant-numeric: tabular-nums;
}
```

## Why

- **Coordinate Navigation in Assistive Technology**: Screen readers enable users to navigate with cell keys (`Ctrl+Alt+Arrows`), announcing both row and column headers when entering any cell.
- **Accurate Dataset Context**: The `<caption>` element serves as the canonical accessible name of the table, avoiding disconnected headings.
- **Column Sizing & Grouping**: `<colgroup>` and `<col>` enable styling and sizing entire columns in one place without repeating classes on hundreds of `<td>` tags.
- **Accessible Overflow Scrolling**: Giving the overflow wrapper `role="region"` and `tabindex="0"` allows keyboard-only users to scroll horizontally without being blocked.
- **Footer Semantics**: `<tfoot>` provides a semantic summary or footnote row that repeats on printed documents.

## Related

- Reference: [`references/semantic-html.md`](../references/semantic-html.md)
- Reference: [`references/components-and-patterns.md`](../references/components-and-patterns.md)
- Rule: [`rules/type-tabular-numerals.md`](type-tabular-numerals.md)
- Rule: [`rules/html-semantic-elements.md`](html-semantic-elements.md)
