# Modern CSS Architecture, Cascade Layers & Specificity

**Impact:** HIGH · **Prefix:** `css-` · **Maintainable Stylesheets & Platform Features**

Modern CSS provides native primitives that replace legacy preprocessor workarounds and fragile specificity hacks. Disciplined architecture uses Cascade Layers (`@layer`) to govern specificity, tokenized Z-Index scales to eradicate stacking wars, and native relational selectors (`:has()`, `:is()`, `:where()`) for expressive styling.

## Load When

- Organizing stylesheet structure, design token systems, or component libraries
- Resolving specificity conflicts and eliminating `!important` declarations
- Establishing a disciplined Z-index stacking hierarchy
- Structuring themes using `light-dark()` and CSS custom properties
- Implementing parent-aware styling with `:has()` and zero-specificity grouping with `:where()`

## Rules

| Rule | Summary |
|------|---------|
| [`css-cascade-layers-and-specificity`](../rules/css-cascade-layers-and-specificity.md) | Use `@layer` to govern cascade order and keep selectors at single-class (0-1-0) specificity |
| [`css-tokenized-z-index-scale`](../rules/css-tokenized-z-index-scale.md) | Eliminate magic numbers (`z-index: 9999`) with a tokenized stacking scale |
| [`css-modern-color-light-dark`](../rules/css-modern-color-light-dark.md) | Leverage `light-dark()` and relative color syntax (`color-mix()`) for fluid theming |

---

## Cascade Layers (`@layer`)

Cascade Layers give authors explicit control over which styles override others, regardless of selector specificity:

```css
/* 1. Declare layer order at the very top of the stylesheet */
@layer reset, base, layout, components, utilities;

/* 2. Base layer: Element defaults */
@layer base {
  body {
    font-family: var(--font-sans);
    color: var(--color-text-primary);
    background-color: var(--color-canvas);
  }
  h1, h2, h3 {
    text-wrap: balance;
  }
}

/* 3. Component layer: Reusable UI widgets */
@layer components {
  .btn {
    display: inline-flex;
    align-items: center;
    padding: 0.5rem 1rem;
    border-radius: var(--radius-md);
  }
}

/* 4. Utilities layer: Always wins over component styles, even with simple classes */
@layer utilities {
  .hidden {
    display: none !important;
  }
  .sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    clip: rect(0, 0, 0, 0);
  }
}
```

**Key Benefit:** A rule in a later layer (e.g. `utilities`) always wins over a rule in an earlier layer (e.g. `components`), even if the component selector has higher specificity (e.g. `#nav .btn.primary`).

---

## Tokenized Z-Index Scale

Arbitrary values like `z-index: 9999` trigger unmaintainable stacking wars where elements accidentally overlay dialogs, dropdowns, or notifications.

Establish a centralized, documented z-index scale in CSS custom properties:

```css
:root {
  --z-below:    -1;   /* Decorative background elements */
  --z-base:      0;   /* Default page content */
  --z-raised:   10;   /* Elevated cards, sticky table headers */
  --z-dropdown: 100;  /* Select menus, popovers, contextual tooltips */
  --z-sticky:   200;  /* Sticky navigation bars */
  --z-overlay:  300;  /* Backdrop scrims */
  --z-modal:    400;  /* Modal dialogs (<dialog> enters top-layer automatically) */
  --z-toast:    500;  /* System notifications, toast alerts */
  --z-tooltip:  600;  /* High-priority floating tooltips */
}
```

*Note: Native HTML `<dialog>.showModal()` and the Popover API render into the browser's native **Top Layer**, which sits above all standard CSS z-index stacking contexts automatically without z-index collisions.*

---

## Modern Relational & Grouping Selectors

### 1. Parent-Aware Styling with `:has()`
Style a parent container or sibling based on its child state without requiring JavaScript class toggles:

```css
/* Highlight a card when its internal checkbox is checked */
.pricing-card:has(input[type="radio"]:checked) {
  border-color: var(--color-action-primary);
  box-shadow: var(--shadow-medium);
}

/* Add extra spacing to a header if it contains a banner */
header:has(.announcement-banner) {
  padding-top: var(--space-12);
}
```

### 2. Zero-Specificity Grouping with `:where()`
Use `:where()` to apply defaults that can be easily overridden without fighting specificity:

```css
/* Zero specificity (0-0-0): easily overridden by any single class */
:where(h1, h2, h3, h4, p) {
  margin-block-start: 0;
}
```

### 3. Matched Specificity Grouping with `:is()`
Use `:is()` to group complex selectors without code repetition while taking the specificity of the most specific argument:

```css
/* Replaces long repeated chains */
:is(header, main, footer) :is(h1, h2, h3) {
  color: var(--color-text-primary);
}
```

---

## Modern Units Strategy

| Unit | Appropriate Use Case | What to Avoid |
|---|---|---|
| **`rem`** | Typography, spacing scales, layout widths | Never use `px` for font-size; `rem` respects browser zoom and user accessibility settings |
| **`em`** | Component-relative sizing (e.g. icon width matching text `1.125em`, padding scaling with button font-size) | Avoid deeply nested `em` typography calculations that compound uncontrollably |
| **`px`** | Hairline borders (1px), subtle box-shadow offsets, fine optical alignments | Avoid fixed `px` widths on text containers or mobile layout wrappers |
| **`dvh` / `svh`** | Full-height hero screens (`min-height: 100dvh`) | Avoid raw `vh` on mobile web, which clips under mobile address bars |
| **`ch`** | Reading column measure (`max-width: 65ch`) | Avoid wide percentage widths for long body text paragraphs |
