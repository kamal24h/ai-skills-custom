# Surfaces, Elevation & Visual Polish

**Impact:** MEDIUM · **Prefix:** `surface-` · **Craft & Precision**

Visual polish transforms a functional interface into an elegant, tactile product. Consistent surface mechanics, concentric border radii, optical alignment compensation, layered shadows, and themed native chrome provide tangible depth and clarity.

## Load When

- Creating cards, containers, modal overlays, tooltips, and badges
- Nesting rounded elements inside rounded containers
- Designing elevation and shadow tokens
- Theming browser chrome surfaces (selection, caret, scrollbars)
- Aligning icons with typography or centering asymmetric shapes

## Rules

| Rule | Summary |
|------|---------|
| [`surface-concentric-radius`](../rules/surface-concentric-radius.md) | Concentric radius formula (`outer = inner + padding`); avoid mismatched corners |
| [`surface-optical-alignment`](../rules/surface-optical-alignment.md) | Optical compensation for asymmetric icons (e.g. play button), icon+text vertical centering |
| [`surface-browser-chrome-theming`](../rules/surface-browser-chrome-theming.md) | Theme browser-native chrome surfaces (`::selection`, `caret-color`, `scrollbar-color`) from the palette |
| [`surface-press-scale`](../rules/surface-press-scale.md) | Provide tactile micro-interaction feedback on `:active` press (`scale(0.97)`) |
| [`surface-aspect-ratio-skeletons`](../rules/surface-aspect-ratio-skeletons.md) | Reserve known media dimensions to reduce layout shift; use skeletons when useful |

---

## Concentric Border Radius

When a rounded element sits inside another rounded container with padding, using the same border-radius for both creates awkward, pinched corners.

### The Concentric Formula

$$\text{Outer Radius} = \text{Inner Radius} + \text{Padding}$$

$$\text{Inner Radius} = \max(0, \text{Outer Radius} - \text{Padding})$$

```css
/* Card container */
.card {
  --card-padding: 1rem;       /* 16px */
  --inner-radius: 0.5rem;      /* 8px */

  /* Outer radius = 8px + 16px = 24px (1.5rem) */
  border-radius: calc(var(--inner-radius) + var(--card-padding));
  padding: var(--card-padding);
}

.card .thumbnail-image {
  border-radius: var(--inner-radius); /* Perfectly concentric */
}
```

---

## Optical Alignment

Geometric center does not always equal visual center. Symmetrical calculations often look misaligned to the human eye.

### 1. Play Button Triangles
A right-facing equilateral triangle has its center of mass to the left of its geometric bounding box. In an icon container, nudge it rightwards by ~10–12% of its width:

```css
.play-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 3rem;
  height: 3rem;
  border-radius: 50%;
}

.play-button svg {
  /* Nudge rightward so visual weight aligns with the circle's center */
  transform: translateX(2px);
}
```

### 2. Button Icon and Text Alignment
Cap-height of text is typically smaller than the line box. Center icons relative to the font's cap-height or use flexbox alignment with inline SVG sizing matching text `1em`:

```css
.action-button {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
}

.action-button svg {
  width: 1.125em;
  height: 1.125em;
  flex-shrink: 0;
  stroke-width: 2px; /* Match font weight */
}
```

---

## Elevation & Multi-Layered Shadows

Single dark harsh shadows look synthetic and muddy. Natural light creates soft, diffuse, layered ambient occlusion:

```css
:root {
  /* Subtle structural card border */
  --border-subtle: 1px solid oklch(0.9 0.01 250);

  /* Low Elevation (Cards, Hover states) */
  --shadow-low:
    0 1px 2px -1px oklch(0 0 0 / 0.06),
    0 2px 4px 0 oklch(0 0 0 / 0.04);

  /* Medium Elevation (Dropdowns, Popovers) */
  --shadow-medium:
    0 3px 6px -2px oklch(0 0 0 / 0.08),
    0 6px 12px -2px oklch(0 0 0 / 0.06),
    0 1px 2px 0 oklch(0 0 0 / 0.04);

  /* High Elevation (Modals, Dialogs) */
  --shadow-high:
    0 10px 20px -4px oklch(0 0 0 / 0.10),
    0 20px 32px -6px oklch(0 0 0 / 0.08),
    0 1px 3px 0 oklch(0 0 0 / 0.05);
}
```

### Depth Principles:
- **True depth requires offset and soft blur**: A zero-offset colored glow (`box-shadow: 0 0 12px var(--color-blue)`) is flat decoration, not lighting.
- **Borders define structure; shadows define elevation**: Use subtle 1px borders to delineate adjacent cards on flat canvas; use shadows to lift overlays above the page.
- **Avatar & user-upload containment**: Pure white or pure black uploaded images must have a subtle semi-transparent border to prevent them from bleeding into the background:
```css
.avatar-image,
.user-upload {
  border: 1px solid oklch(0 0 0 / 0.08);
}
```
