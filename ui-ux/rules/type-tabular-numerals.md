---
title: Apply Tabular Figures to Numerical Data, Tables, and Timers
impact: MEDIUM
impactDescription: Proportional figures cause numbers to jitter, wobble, and misalign horizontally when values change in tables, counters, or financial data.
tags: typography, numbers, tabular-nums, data-tables, opentype
---

# Apply Tabular Figures to Numerical Data, Tables, and Timers

In standard proportional fonts, the number "1" is significantly narrower than "8" or "0". When numbers update dynamically (countdown timers, stock tickers, dashboards) or align in table columns, proportional figures cause distracting horizontal layout jitter and misaligned columns.

Use `font-variant-numeric: tabular-nums;` on all structured numerical data to give every numeral an equal, fixed monospace width while preserving proportional letterforms for words.

## Bad Example

Using default proportional numbers for data tables or changing values:

```css
/* ❌ Numbers jitter horizontally when updating, columns do not align vertically */
.metric-counter,
td.number-column {
  font-family: inherit;
  /* Proportional numbers by default */
}
```

## Good Example

Enable tabular lining figures on numeric elements:

```css
/* ✅ Every digit occupies uniform horizontal width */
.metric-counter,
.countdown-timer,
.price-tag,
table td.numeric,
.stat-value {
  font-variant-numeric: tabular-nums;
}
```

```html
<td class="numeric">1,240.50</td>
<td class="numeric">8,888.10</td>
```
