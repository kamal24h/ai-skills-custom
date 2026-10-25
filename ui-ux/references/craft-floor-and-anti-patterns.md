# The Craft Floor, Browser Surfaces & Anti-Patterns to Refuse

**Impact:** HIGH · **Prefix:** `craft-` · **Visual Baseline & Intentional Design Decisions**

The "Craft Floor" defines the baseline standard of execution that distinguishes a professionally crafted product from generic assembly. It establishes mandatory browser chrome theming, intentional decluttering, and a set of reflexive design clichés that should be refused by default.

## Load When

- Reviewing visual finish and design polish on any page or template
- Theming browser-native surfaces (selection, caret, scrollbars, focus rings)
- Decluttering busy layouts, redundant borders, and nested containers
- Preventing reflexive design clichés (identical card grids, hero-metrics, eyebrows)
- Verifying contrast, depth, and typographic rhythm in the rendered output

## Rules

| Rule | Summary |
|------|---------|
| [`surface-browser-chrome-theming`](../rules/surface-browser-chrome-theming.md) | Style native browser surfaces (`::selection`, `caret-color`, `scrollbar-color`, `text-underline-offset`) from the palette |
| [`layout-proximity-over-borders`](../rules/layout-proximity-over-borders.md) | Group elements via whitespace rhythm instead of container borders; more space above headings |

---

## The Craft Floor Verifications

Run these checks together on the rendered output:

1. **Contrast verification**: Body text ≥ 4.5:1, large text ≥ 3:1 against computed background. On colored surfaces, tint secondary text from that background hue or foreground; never use generic washed-out gray.
2. **True depth over halos**: Shadows must carry an offset and a soft blur (`0 4px 12px -2px rgba(...)`). A zero-offset colored glow is decoration, not a lighting/elevation model.
3. **Spacing cadence**: Tight grouping for related items, generous intervals between sections, and visibly more space above a heading than below it (a heading belongs to the section that follows it).
4. **Typographic rigor**: Body measure constrained to 45–75ch (optimal 65ch); display tracking tightened to -0.02em to -0.04em; headings balanced; tabular numbers on data and counters.
5. **Authored motion**: One deliberate, purposeful moment of motion rather than scattered section-by-section fade-ins. Prefer exponential ease-out from an already visible default.
6. **Complete state readiness**: Default, hover, focus-visible, active, disabled, loading, empty, and error states all implemented with real content.

---

## Browser Surface Theming

The parts of the interface you didn't explicitly draw still carry the brand's identity. Leaving browser defaults unstyled is the most reliable sign of an incomplete interface:

```css
:root {
  /* 1. Text Selection */
  ::selection {
    background-color: oklch(0.65 0.22 250 / 0.25);
    color: oklch(0.20 0.02 250);
  }

  /* 2. Text Input Caret */
  input, textarea {
    caret-color: var(--color-action-primary, oklch(0.55 0.22 250));
  }

  /* 3. Modern Cross-Browser Scrollbars */
  html {
    scrollbar-color: oklch(0.75 0.01 250) transparent;
    scrollbar-width: thin;
  }

  /* 4. Link Underline Spacing & Thickness */
  a:not([class]) {
    text-decoration: underline;
    text-underline-offset: 0.25em;
    text-decoration-thickness: 1.5px;
    text-decoration-color: oklch(from currentColor l c h / 0.4);
    transition: text-decoration-color 0.15s ease;
  }
  a:not([class]):hover {
    text-decoration-color: currentColor;
  }

  /* 5. Tabular Figures for UI Numbers */
  .numeric,
  .badge,
  .timestamp,
  .metric-value {
    font-variant-numeric: tabular-nums;
  }
}
```

---

## Anti-Patterns to Refuse by Default

These patterns are frequently reached for by habit without conscious decision. Refuse them unless the specific product brief explicitly calls for them:

### 1. The Identical Card Grid
- ❌ **The Cliché**: Splitting every page into a 3-column grid of identical rounded cards (Icon + Heading + Paragraph).
- ❌ **Nested Cards**: Cards inside cards inside cards.
- ✅ **The Alternative**: Differentiate content structures. Use lists for scan-ability, tables for dense comparison, horizontal split rows for features, and open whitespace grouping without borders.

### 2. The Hero-Metric Template by Reflex
- ❌ **The Cliché**: Giant 64px number stacked on top of a tiny 12px label with a colored badge for every stat on a dashboard.
- ✅ **The Alternative**: Emphasize actionable trends, sparkline contexts, direct comparisons to baseline, or inline status narratives.

### 3. The Eyebrow / Kicker Label Above Every Heading
- ❌ **The Cliché**: Tiny uppercase pill badge or small gray category label above every single heading on a page.
- ✅ **The Alternative**: Let the heading carry its own weight. If the heading needs a label to explain what it is, rewrite the heading.

### 4. Arbitrary Section Numbers
- ❌ **The Cliché**: Slapping `01 / 02 / 03` in front of section titles purely as visual filler.
- ✅ **The Alternative**: Use numbers only when there is a true chronological or sequential workflow that the user must follow in order.

### 5. Modals by Reflex
- ❌ **The Cliché**: Trapping the user in a modal dialog for simple filters, quick edits, or non-destructive tasks.
- ✅ **The Alternative**: Inline expansion (`<details>`), slide-out side drawers, or native popovers (`popover="auto"`). Reserve modals strictly for critical workflows requiring protected focus.

### 6. Cosmetic Gradient Text & Glassmorphism Defaults
- ❌ **The Cliché**: Setting headings in multi-color gradient fills (`linear-gradient(...) -webkit-background-clip: text`) or applying heavy frosted glass blurs (`backdrop-filter: blur(16px)`) across regular cards.
- ✅ **The Alternative**: Create typographic emphasis through scale, weight, and contrast. Reserve blur for actual overlaid backdrops.

### 7. Hard Offset Shadows (Outside Neobrutalism)
- ❌ **The Cliché**: Using `box-shadow: 4px 4px 0px #000` on random UI elements.
- ✅ **The Alternative**: Use multi-layered soft blur shadows (`0 4px 12px -2px rgba(...)`) that reflect realistic ambient light.

### 8. Monospace as a "Technical" Costume
- ❌ **The Cliché**: Setting product features, stats, or navigation in monospace fonts simply to make the UI look "developer-oriented."
- ✅ **The Alternative**: Restrict monospace strictly to actual source code, CLI commands, hashes, and terminal outputs.

---

## Distillation & Decluttering

```
┌──────────────────────────────────────────────┐
│ Before: Cluttered Nesting                    │
│ ┌──────────────────────────────────────────┐ │
│ │ ┌─────────────┐ ┌──────────────────────┐ │ │
│ │ │ [Icon Box]  │ │ Card Heading Inside  │ │ │
│ │ └─────────────┘ └──────────────────────┘ │ │
│ │ ──────────────────────────────────────── │ │
│ │ [Bordered Tag] [Bordered Tag]            │ │
│ └──────────────────────────────────────────┘ │
└──────────────────────────────────────────────┘
                       ▼ Distilled
┌──────────────────────────────────────────────┐
│ After: High Content-to-Chrome Ratio          │
│ Heading with Clear Proximity                 │
│ Natural text description with subtle tags    │
│ Clear primary action link                    │
└──────────────────────────────────────────────┘
```

- **Proximity over borders**: Remove unnecessary bounding box borders. White space rhythm creates cleaner, calmer visual grouping than visible lines.
- **Content-to-chrome ratio**: Maximize space for user content while minimizing administrative UI framing, thick borders, and heavy container boxes.
- **Progressive disclosure**: Surface primary actions immediately; place secondary options behind contextual menus or detail panels.
