---
title: Compensate for Optical Alignment and Icon Weight
impact: MEDIUM
impactDescription: Strict geometric centering looks off-center to the human eye on asymmetrical shapes like triangles and icon badges.
tags: surfaces, alignment, icons, optical-alignment, polish
---

# Compensate for Optical Alignment and Icon Weight

Compensate visually where geometric centering produces an off-center optical perception. For asymmetric icons (such as right-facing play buttons), nudge the icon slightly toward its narrow tip. When placing icons next to text, match the icon stroke weight to the font weight and align with the font cap-height.

## Bad Example

```css
/* Geometric center leaves the play icon looking heavy on the left */
.play-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 48px;
  height: 48px;
  border-radius: 50%;
}
.play-btn svg {
  /* No optical compensation */
}
```

## Good Example

```css
.play-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 48px;
  height: 48px;
  border-radius: 50%;
}

.play-btn svg {
  /* Nudge rightward by ~10% of width to align center of visual mass */
  transform: translateX(2px);
}

.label-with-icon {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
}

.label-with-icon svg {
  width: 1.1em;
  height: 1.1em;
  stroke-width: 2px; /* Matches 600 semi-bold font weight */
}
```
