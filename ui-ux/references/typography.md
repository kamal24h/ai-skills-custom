# Typography & Text Rhythm

**Impact:** HIGH · **Prefix:** `type-` · **Readability & Craft**

Typography is the structural backbone of user interface design. Excellent typography establishes an immediate visual hierarchy, maintains comfortable reading cadence, respects linguistic standards, and guarantees effortless legibility across viewports.

## Load When

- Setting up or auditing global typography scales and CSS custom properties
- Configuring heading hierarchies, display styles, and body copy rhythm
- Formatting editorial content, article bodies, and card titles
- Implementing fluid responsive typography via `clamp()`
- Handling tabular numbers, smart punctuation, OpenType features, or letter-spacing

## Rules

| Rule | Summary |
|------|---------|
| [`type-fluid-scale`](../rules/type-fluid-scale.md) | Fluid typography via `clamp()` without jumping breakpoints; unitless `line-height` |
| [`type-tabular-numerals`](../rules/type-tabular-numerals.md) | Apply tabular figures (`tabular-nums`) to numerical data, tables, and counters |
| [`type-measure-and-leading`](../rules/type-measure-and-leading.md) | Measure constrained to 45–75 characters (`ch`), `text-wrap: balance` on headings, `pretty` on body |
| [`type-curly-quotes`](../rules/type-curly-quotes.md) | Smart curly punctuation (`“ ” ‘ ’ — – …`) instead of dumb typewriter glyphs (`" ' - ...`) |
| [`type-non-breaking-spaces`](../rules/type-non-breaking-spaces.md) | Keep numbers and units bound together with non-breaking spaces |

---

## Role Scale & Fluid Hierarchy

Establish distinct functional typography roles rather than arbitrary sizes:

```css
:root {
  /* Fluid Body: scales smoothly from 16px (375px viewport) to 18px (1280px viewport) */
  --font-size-body: clamp(1rem, 0.95rem + 0.22vw, 1.125rem);

  /* Fluid Hierarchy */
  --font-size-caption: clamp(0.75rem, 0.73rem + 0.1vw, 0.875rem);
  --font-size-sm:      clamp(0.875rem, 0.85rem + 0.1vw, 0.95rem);
  --font-size-base:    var(--font-size-body);
  --font-size-lg:      clamp(1.125rem, 1.05rem + 0.35vw, 1.333rem);
  --font-size-xl:      clamp(1.25rem, 1.15rem + 0.6vw, 1.777rem);
  --font-size-2xl:     clamp(1.5rem, 1.3rem + 1.1vw, 2.369rem);
  --font-size-3xl:     clamp(1.875rem, 1.55rem + 1.8vw, 3.157rem);
  --font-size-display: clamp(2.25rem, 1.8rem + 2.6vw, 4.5rem);
}
```

---

## Letter-Spacing (Tracking) Rules

Letter spacing must adapt inversely to font size:

1. **Display & Large Headings (Tighten)**: As glyphs scale up, the spatial gaps between letters look visually loose. Tighten tracking on headings to a floor of `-0.02em` to `-0.04em`:
```css
h1, .display-heading {
  font-size: var(--font-size-display);
  letter-spacing: -0.03em; /* Tightens large letterforms */
  line-height: 1.1;
}

h2 {
  font-size: var(--font-size-3xl);
  letter-spacing: -0.02em;
  line-height: 1.2;
}
```

2. **All-Caps & Small Captions (Loosen)**: Setting text in uppercase without extra tracking creates an illegible, cramped block. Always loosen letter spacing and slightly reduce font size:
```css
.badge-caps,
.table-header-caps {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.06em; /* Crucial breathing room for all-caps */
  font-weight: 600;
}
```

---

## Line Height (Leading) & Measure (Line Length)

- **Unitless line-height**: Always declare `line-height` as a unitless multiplier (e.g. `1.5`) so it scales proportionally with inherited font sizes.
- **Inverted ratio**:
  - Display / Hero (40px+): `1.05 – 1.15`
  - Headings (24px–36px): `1.15 – 1.25`
  - Subheadings (18px–22px): `1.3 – 1.4`
  - Body copy (15px–18px): `1.5 – 1.65`
- **Optimal Measure**: Constrain reading columns to **45–75 characters** (optimal 65ch):
```css
article p,
.prose {
  max-width: 65ch;
  line-height: 1.6;
}
```

---

## Modern Text Wrapping: `balance` and `pretty`

```css
/* Balances headlines across multiple lines for harmonious optical shape */
h1, h2, h3, h4, .headline {
  text-wrap: balance;
}

/* Prevents single-word orphan lines at the end of body paragraphs */
p, li {
  text-wrap: pretty;
}
```

---

## Smart Punctuation & Typographic Entities

Customer-facing UI text should use proper typographic glyphs rather than typewriter approximations:

| Concept | Typewriter (Avoid) | Typographic Standard | HTML Entity | Context |
|---|---|---|---|---|
| Double Quotes | `"text"` | “text” | `&ldquo;` `&rdquo;` | Quotations |
| Single Quote / Apostrophe | `'` or `it's` | ‘text’ or it’s | `&lsquo;` `&rsquo;` | Apostrophes, inner quotes |
| En Dash | `-` or `--` | – | `&ndash;` | Number ranges (2020–2026) |
| Em Dash | `--` | — | `&mdash;` | Sentence break |
| Ellipsis | `...` | … | `&hellip;` | Pauses, omissions |
| Multiplication | `x` | × | `&times;` | Dimensions (1920 × 1080) |

---

## OpenType Features: Tabular Figures

Proportional numerals cause horizontal jitter when counters, stock prices, or countdown timers update. Enable tabular lining figures:

```css
.tabular-nums,
table td.numeric,
.stat-counter,
.price-display {
  font-variant-numeric: tabular-nums;
}
```

---

## Robust Fallback Font Stacks

```css
:root {
  /* High quality modern system sans-serif */
  --font-sans: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
    'Helvetica Neue', Arial, sans-serif;

  /* Monospace for code, hashes, and terminal UI */
  --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas,
    'Liberation Mono', 'Courier New', monospace;

  /* Editorial serif */
  --font-serif: ui-serif, Georgia, Cambria, 'Times New Roman', Times, serif;
}

body {
  font-family: var(--font-sans);
  font-synthesis: none; /* Disables fake browser-smeared bold/italic */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
```
