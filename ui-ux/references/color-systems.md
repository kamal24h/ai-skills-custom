# Color Systems & Contrast

**Impact:** CRITICAL · **Prefix:** `color-` · **Visual Harmony & Accessibility**

A robust color system balances aesthetic identity with strict functional contrast. It organizes colors into an explicit 3-tier token hierarchy, leverages perceptually uniform color spaces like OKLCH, and ensures seamless dark mode adaptability.

## Load When

- Designing or refactoring design tokens and theme variables
- Selecting brand and UI color palettes
- Implementing dark mode and theme switching
- Auditing color contrast for WCAG AA compliance
- Designing interactive states (hover, active, focus, disabled)

## Rules

| Rule | Summary |
|------|---------|
| [`color-semantic-tokens`](../rules/color-semantic-tokens.md) | Use semantic color roles when consistency or theming calls for them |
| [`color-contrast-wcag`](../rules/color-contrast-wcag.md) | 4.5:1 normal text, 3:1 large text and UI components; dark mode lightness elevation over stark pure black |
| [`color-state-derivation`](../rules/color-state-derivation.md) | Derive hover, active, and focus state colors predictably from base tokens |

---

## Visitor Modes: Strategic Color Dosage

Color strategy must reflect the product's primary interaction mode:

- **Persuade + Experience (Marketing, Landing Pages, Brand Experiences)**: Color carries the emotional voice and may own prominent backgrounds, illustrations, or dramatic hero sections.
- **Operate + Read (Web Apps, Dashboards, Productivity Tools)**: Color primarily encodes action, selection, status, and wayfinding. Grayscale provides a quiet backdrop so accent colors retain maximum force. Rarity gives an accent its power; do not scatter primary brand colors on non-interactive decoration.

---

## The Three-Tier Token Architecture

For a reusable or themeable system, semantic roles create a clean boundary between raw palette choices and component meaning:

```
┌────────────────────────────────────────────────────────┐
│ Tier 1: Primitives (Hues & Ramps)                      │
│ Example: --color-blue-500: oklch(0.55 0.22 255);       │
└─────────────────────────┬──────────────────────────────┘
                          │ (Aliased into)
                          ▼
┌────────────────────────────────────────────────────────┐
│ Tier 2: Semantic Roles (Theme & Meaning)               │
│ Example: --color-action-primary: var(--blue-500);      │
│ Example: --color-surface-base: var(--neutral-50);      │
└─────────────────────────┬──────────────────────────────┘
                          │ (Consumed by)
                          ▼
┌────────────────────────────────────────────────────────┐
│ Tier 3: Component Scoped (Contextual Overrides)        │
│ Example: --button-primary-bg: var(--action-primary);   │
└────────────────────────────────────────────────────────┘
```

### CSS Custom Properties Implementation

```css
:root {
  /* Tier 1: Global Primitives (OKLCH for perceptual uniformity) */
  --blue-50:  oklch(0.97 0.02 250);
  --blue-100: oklch(0.93 0.05 250);
  --blue-500: oklch(0.58 0.20 250);
  --blue-600: oklch(0.51 0.21 250);
  --blue-700: oklch(0.44 0.20 250);

  --neutral-0:   oklch(1 0 0);
  --neutral-50:  oklch(0.98 0.005 250);
  --neutral-100: oklch(0.95 0.008 250);
  --neutral-200: oklch(0.89 0.010 250);
  --neutral-700: oklch(0.38 0.015 250);
  --neutral-900: oklch(0.20 0.015 250);
  --neutral-950: oklch(0.14 0.015 250);

  --red-500:   oklch(0.62 0.22 28);
  --green-500: oklch(0.65 0.18 145);

  /* Tier 2: Semantic Tokens (Light Theme Default) */
  --color-canvas:              var(--neutral-50);
  --color-surface:             var(--neutral-0);
  --color-surface-subtle:      var(--neutral-100);
  --color-border:              var(--neutral-200);
  --color-text-primary:        var(--neutral-900);
  --color-text-secondary:      var(--neutral-700);

  --color-action-primary:      var(--blue-500);
  --color-action-primary-hover:var(--blue-600);
  --color-text-on-action:      var(--neutral-0);

  --color-feedback-danger:     var(--red-500);
  --color-feedback-success:    var(--green-500);
}

/* Dark Mode Overrides: Explicit Surface Lightness Elevation */
@media (prefers-color-scheme: dark) {
  :root {
    --color-canvas:              var(--neutral-950);
    --color-surface:             oklch(0.18 0.015 250);
    --color-surface-subtle:      oklch(0.24 0.015 250);
    --color-border:              oklch(0.28 0.015 250);
    --color-text-primary:        oklch(0.96 0.005 250);
    --color-text-secondary:      oklch(0.75 0.010 250);

    /* Slightly desaturate vibrant brand accents on dark backgrounds */
    --color-action-primary:      oklch(0.64 0.18 250);
    --color-action-primary-hover:oklch(0.70 0.18 250);
  }
}
```

---

## OKLCH Ramping & Tinting Rules

- **Why OKLCH?**: Standard HSL and sRGB have erratic perceptual lightness. Pure yellow in HSL has ~98% perceived brightness, while pure blue has ~25%. OKLCH `oklch(L C H)` keeps perceived lightness (`L`) uniform across hues.
- **Taper chroma near extremes**: When deriving ramps, decrease chroma (`C`) as lightness approaches `1.0` (white) or `0` (black). Keeping high chroma at lightness extremes results in muddy or un-displayable out-of-gamut shades.
- **Tinting neutrals**: Only tint gray ramps when the brand hue genuinely enhances emotional cohesion. Pure neutral grays are completely valid when clarity is paramount.
- **Secondary text on colored surfaces**: Never use generic washed-out gray on colored backgrounds. Derive secondary text directly from the background hue or foreground tone (e.g. `oklch(from var(--surface-primary) calc(l + 0.35) calc(c * 0.4) h)`).

---

## WCAG Contrast Thresholds

| UI Element | WCAG AA Minimum | WCAG AAA Minimum |
|---|---|---|
| Regular body text (< 18pt / 24px) | **4.5:1** | **7:1** |
| Large text (≥ 18pt / 24px or ≥ 14pt bold) | **3:1** | **4.5:1** |
| Meaningful UI components & focus indicators | **3:1** | — |
| Decorative graphics / disabled elements | Exempt | Exempt |

---

## Non-Color Cues for Data & Status

Color must never be the sole mechanism used to communicate status, errors, or data trends (WCAG 1.4.1):
- Combine color with **icons** (e.g. checkmark for success, exclamation mark for danger).
- In charts and data visualizations, pair color with **distinct dash patterns, point shapes, or direct data labels**.
