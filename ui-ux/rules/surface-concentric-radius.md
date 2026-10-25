---
title: Apply Concentric Border Radius Formula
impact: MEDIUM
impactDescription: Using identical border-radii for nested elements creates awkward, pinched corners and visual tension.
tags: surfaces, border-radius, visual-polish, geometry, polish
---

# Apply Concentric Border Radius Formula

When nesting a rounded element inside a padded rounded container, compute the outer radius using the concentric formula:
$$\text{Outer Radius} = \text{Inner Radius} + \text{Padding}$$

## Bad Example

```css
/* Both container and child have border-radius: 12px with 16px padding */
.card-bad {
  border-radius: 12px;
  padding: 16px;
}

.card-bad .image {
  border-radius: 12px; /* Pinched, non-concentric corner curve */
}
```

## Good Example

```css
/* Mathematically concentric curvature */
.card-good {
  --padding: 1rem;       /* 16px */
  --inner-radius: 0.5rem; /* 8px */

  /* Outer radius: 8px + 16px = 24px (1.5rem) */
  border-radius: calc(var(--inner-radius) + var(--padding));
  padding: var(--padding);
}

.card-good .image {
  border-radius: var(--inner-radius);
}
```
