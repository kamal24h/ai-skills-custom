# Real Content Design & Interface Affordances

**Impact:** CRITICAL · **Prefix:** `affordance-` · **Perceptible Actions & Content-Driven Layouts**

An interface succeeds when people can immediately perceive what actions are possible, what data represents, and how to accomplish their task. Designing with real, varied content—rather than sanitized placeholders—ensures layouts accommodate real-world complexity without breaking visual hierarchy.

## Load When

- Designing or reviewing card layouts, list views, navigation menus, and data tables
- Auditing hover-dependent actions, ambiguous icon buttons, and hit targets
- Testing layouts against uneven titles, missing optional fields, or variable summary lengths
- Defining interactive states: default, pressed, selected, expanded, loading, and disabled
- Replacing generic Lorem Ipsum placeholders with realistic content models

## Rules

| Rule | Summary |
|------|---------|
| [`a11y-no-hover-only-critical-actions`](../rules/a11y-no-hover-only-critical-actions.md) | Essential actions and critical affordances must never be hidden behind `:hover` alone |
| [`html-native-state-pseudo-classes`](../rules/html-native-state-pseudo-classes.md) | Style interactive states with native pseudo-classes (`:disabled`, `:open`, `:checked`) |

---

## Real Content Design Methodology

Layouts designed around identical 3-word titles and uniform square images inevitably fail in production. Real content has irregular rhythm, optional metadata, and varying significance.

```
┌────────────────────────────────────────────────────────┐
│ The Placeholder Trap (Fragile):                        │
│ [Card 1: 3-word title] [Card 2: 3-word title] [Card 3] │
│ Everything matches; hides line wrapping and overflow. │
├────────────────────────────────────────────────────────┤
│ The Real Content Reality (Resilient):                  │
│ [Card 1: 14-word title wrapped across 3 lines]        │
│ [Card 2: Missing thumbnail image; fallback layout]     │
│ [Card 3: Inactive status badge + derived metadata]     │
└────────────────────────────────────────────────────────┘
```

### 1. Representative Structural Variations
Test interfaces against realistic content variations before finalizing component dimensions:
- **Uneven Titles & Summaries**: Ensure headings survive 1-line vs 3-line variations without breaking vertical alignment (leverage CSS Subgrid for multi-card rows).
- **Missing Optional Metadata**: If a record lacks an avatar, description, or tag, the layout must look intentional rather than broken.
- **Distinguishing Absence**: Distinctly handle three different states of absence:
  - *Unavailable / Not applicable*: Explicit text (e.g. "—" or "None").
  - *Empty dataset*: Purposeful empty state with call to action.
  - *Loading / Fetch failure*: Dedicated skeleton or error retry alert.
- **Never Force Equal Copy**: Do not truncate meaningful content or invent fake words simply to preserve an arbitrary card height. If content varies radically, switch from a rigid card grid to an expandable list, table, or master-detail panel.

---

## Core Affordance Principles

Affordances communicate what an interface can do. If users have to guess whether an element is clickable, expandable, or disabled, the design has failed.

### 1. Persistent Cues Over Hover Discovery
- **Hover is an enhancement, never a prerequisite**: On touchscreens, hover does not exist. Primary controls (edit, delete, bookmark, share) must have persistent visual cues or accessible menu triggers.
- **Secondary actions on hover**: If secondary controls appear on hover on desktop viewports, they must also be permanently accessible via keyboard focus (`:focus-within`) and have a touch-friendly permanent equivalent on mobile viewports.

### 2. State Clarity: Every State Must Explain Itself
Interactive controls must provide unambiguous visual differentiation across all operational states:

| State | Visual Treatment | Implementation Guidance |
|---|---|---|
| **Default** | Clear boundary, contrast, and label | Native `<button>` or `<a>`, minimum 3:1 boundary or fill contrast |
| **Hover** | Subtle elevation or lightness shift | `filter: brightness(1.05)` or background token change |
| **Focus-Visible** | High-contrast outline with offset | 2px contrasting ring with 2px offset; never suppressed |
| **Pressed / Active** | Tactile inset or slight scale down | `transform: scale(0.97)` or inset shadow |
| **Selected** | Solid accent tint, checkmark, or bold fill | `aria-selected="true"`, `aria-current="page"`, or `:checked` |
| **Disabled** | Reduced opacity, muted text, disabled cursor | Native `disabled` attribute; explain reason nearby if non-obvious |
| **Loading** | Inline spinner or shimmer, preserved dimensions | `aria-busy="true"`, disabled trigger to prevent double-submit |

### 3. Cursor Semantics
Always use browser cursor conventions to reinforce affordance:
- `cursor: pointer` — for clickable links and action buttons.
- `cursor: default` — for non-interactive cards, text labels, and containers.
- `cursor: text` — for editable inputs and selectable text regions.
- `cursor: not-allowed` — for disabled or forbidden controls.
- `cursor: grab` / `grabbing` — for draggable surfaces and reorderable list handles.
