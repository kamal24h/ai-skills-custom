---
title: Establish Grouping Through Whitespace Proximity Over Box Borders
impact: HIGH
impactDescription: Overusing borders and container outlines clutters interfaces, adds visual noise, and decreases the content-to-chrome ratio.
tags: layout, spacing, proximity, gestalt, visual-hierarchy
---

# Establish Grouping Through Whitespace Proximity Over Box Borders

Gestalt psychology's Law of Proximity states that objects placed close together are naturally perceived as a group. Modern high-craft layouts rely on disciplined spacing intervals and rhythmic whitespace rather than enclosing every single item inside heavy borders and boxes.

Additionally, a heading must always sit closer to the content it introduces than to the previous section: `margin-top` must be visibly larger than `margin-bottom`.

## Bad Example

Heavy box-in-box nesting and symmetrical heading margins:

```css
/* ❌ Excessive container borders; heading floating equidistant between sections */
.feature-section {
  border: 1px solid #ccc;
  padding: 1rem;
}

.feature-section h2 {
  margin-top: 1.5rem;
  margin-bottom: 1.5rem; /* Equidistant: disconnects heading from following content */
}

.feature-item {
  border: 1px solid #ddd; /* Unnecessary border on every child item */
  padding: 0.75rem;
}
```

## Good Example

Deliberate spacing cadence where proximity establishes the visual relationship:

```css
/* ✅ Rhythm and proximity establish structure naturally */
.section-block {
  display: flex;
  flex-direction: column;
  gap: var(--space-8); /* Generous separation between major sections */
}

.section-block h2 {
  margin-top: var(--space-8);   /* Generous space from preceding section */
  margin-bottom: var(--space-2); /* Tight space: clearly introduces following text */
}

.item-list {
  display: flex;
  flex-direction: column;
  gap: var(--space-3); /* Tight proximity groups items without borders */
}
```
