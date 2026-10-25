---
title: Constrain Measure and Balance Headings
impact: HIGH
impactDescription: Excessively wide text columns cause eye strain and line loss; unbalanced multi-line headings create unsightly rags.
tags: typography, measure, leading, text-wrap, line-length
---

# Constrain Measure and Balance Headings

Constrain body copy line length to between **45 and 75 characters** (ideally 60–68ch) using the `ch` unit. Apply modern CSS `text-wrap: balance` to headings to prevent single-word orphan lines, and `text-wrap: pretty` to body paragraphs.

## Bad Example

```css
/* Text spans the entire width of large screens, causing extreme reading fatigue */
article p {
  width: 100%;
  line-height: 1.2; /* Far too cramped for body copy */
}

/* Headings break naturally without balancing, leaving solitary words on new lines */
h1 {
  /* No text-wrap specified */
}
```

## Good Example

```css
article p {
  max-width: 68ch; /* Optimal line length */
  line-height: 1.6; /* Comfortable reading rhythm */
  text-wrap: pretty; /* Prevents awkward trailing words */
}

h1, h2, h3 {
  text-wrap: balance; /* Evenly distributes words across lines */
  line-height: 1.2;   /* Tight leading appropriate for large titles */
}
```
