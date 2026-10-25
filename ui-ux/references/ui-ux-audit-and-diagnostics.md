# UI/UX Technical Audit & Quality Diagnostics

**Impact:** CRITICAL · **Prefix:** `audit-` · **Verifiable Code-Level Quality & Triage**

A systematic technical audit evaluates measurable, verifiable frontend quality across five core dimensions. It separates objective defects from design critiques, scores implementation rigor, and prioritizes remediation to safeguard user trust and task completion.

## Load When

- Auditing an existing web interface, design system, or page template
- Running pre-release quality assurance and code-level verification
- Diagnosing accessibility, performance, responsive layout, or state gaps
- Triaging frontend defects into actionable priority tiers (P0–P3)
- Distinguishing local bugs from system-wide design token or component drift
- Critiquing AI-generated UI output to identify template residue, magic values, or pseudo-semantics

## 5-Dimension Diagnostic Scan

Score each dimension from **0 (Failing / Critical Gaps)** to **4 (Exemplary / Production Hardened)**.

```
┌────────────────────────────────────────────────────────┐
│ 1. Accessibility (WCAG 2.2 AA Conformance)       [0–4] │
│ 2. Web Performance & Core Web Vitals (CWV)       [0–4] │
│ 3. Responsive & Device Adaptability              [0–4] │
│ 4. Visual Polish & Design System Integrity       [0–4] │
│ 5. Resilience, State Coverage & Edge Cases       [0–4] │
└────────────────────────────────────────────────────────┘
```

### Dimension 1: Accessibility (A11y)
- **Contrast ratios**: Body text ≥ 4.5:1, large text ≥ 3:1, UI controls/borders/focus rings ≥ 3:1 against actual computed backgrounds.
- **Focus visibility**: Every interactive element has an unambiguous `:focus-visible` indicator (minimum 2px with offset). Zero focus traps.
- **Semantic structure**: Proper landmark elements (`<main>`, `<nav>`, `<header>`, `<footer>`), valid heading hierarchy (`h1` → `h2` → `h3` without skips), native `<button>` and `<a>` elements instead of `div`/`span` click handlers.
- **ARIA & labels**: Form controls have explicit `<label>` or accessible names; icon buttons provide `.sr-only` text; decorative SVGs have `aria-hidden="true"`.
- **Motion sensitivity**: Respects `prefers-reduced-motion` with intentional reduced alternatives; never a blunt `0.01ms` universal wipe that destroys focus perception and state cues.

### Dimension 2: Web Performance & Core Web Vitals
- **LCP (Largest Contentful Paint)**: Hero image/text rendered swiftly; priority images preloaded with modern formats (AVIF/WebP) and responsive `srcset`.
- **INP (Interaction to Next Paint)**: Main thread unblocked; expensive event handlers debounced/throttled; no synchronous layout thrashing (alternating DOM reads and writes).
- **CLS (Cumulative Layout Shift)**: Media, embeds, and async slots reserve explicit space via `aspect-ratio` or dimension attributes; zero unexpected layout shifts.
- **Resource weight & DOM depth**: Lean DOM tree; large data lists virtualized; non-critical JavaScript lazy-loaded.

### Dimension 3: Responsive & Device Adaptability
- **Viewport meta**: `<meta name="viewport" content="width=device-width, initial-scale=1">` present without `user-scalable=no` or `maximum-scale=1`.
- **Touch ergonomics**: Hit targets meet 44×44 CSS px (WCAG 2.2 minimum 24×24 CSS px with spacing exceptions); thumbs-first reachable controls on mobile viewports.
- **Layout stability**: No unintentional horizontal overflow (`overflow-x: hidden` hacks on `<body>` flag unaddressed layout breaks); cards reflow via Grid `auto-fit` or container queries.
- **Input font size**: Form inputs use at least 16 CSS px (`max(1rem, 16px)`) to prevent automatic mobile browser viewport zoom.

### Dimension 4: Visual Polish & System Integrity
- **Spacing rhythm**: Deliberate scale; tight grouping for related items, generous separation between sections; more space above headings than below them.
- **Typography hierarchy**: Obvious scale and weight steps; display letter-spacing floor (-0.02em to -0.04em); tabular numbers (`font-variant-numeric: tabular-nums`) on data and counters; long-form measure restricted to 45–75ch.
- **Surface & depth consistency**: Concentric border radii (`outer = inner + padding`); multi-layered soft shadows with realistic light offset; no zero-blur colored halos.
- **Browser chrome theming**: Text selection (`::selection`), caret color (`caret-color`), custom scrollbars (`scrollbar-color`), and link underlines styled from the palette.

### Dimension 5: Resilience, State Coverage & Edge Cases
- **Complete state coverage**: Every component handles default, hover, focus-visible, active, disabled, loading, error, and empty states.
- **Extreme text handling**: Resilient against long unbroken strings (`overflow-wrap: break-word`), empty text, special characters, emoji, and localized length expansion (+30%).
- **Network & async errors**: Graceful recovery for offline, timeout, 4xx, and 5xx responses with actionable user guidance and retry buttons.
- **Pointer & gesture resilience**: Drag surfaces, sliders, and interactive controls handle `pointercancel`, `lostpointercapture`, and window blur cleanly without sticking.

---

## AI Output Critique & Quality Verification

AI-generated interfaces often look deceptively polished in quick screenshots while harboring deep structural flaws underneath. When reviewing or refining model output, run this 6-point verification:

```
┌────────────────────────────────────────────────────────┐
│ 1. Semantic Integrity: Are they real buttons and       │
│    inputs, or div soup with synthetic click listeners?  │
│ 2. Token Compliance: Did the model pull from root      │
│    design tokens, or generate ad-hoc hex and px values?│
│ 3. Layout Intention: Is there deliberate hierarchy, or │
│    lazy template residue (e.g. 3 identical cards)?     │
│ 4. Motion Continuity: Is animation compositor-friendly │
│    and interruptible, or a locked 800ms keyframe?      │
│ 5. State Completeness: Did the model build hover,      │
│    focus-visible, active, loading, empty, and error?   │
│ 6. Neighbor Fit: Does the component match neighboring  │
│    patterns, spacing intervals, and typography scales? │
└────────────────────────────────────────────────────────┘
```

Never accept a preview render at face value; always audit the underlying HTML semantics, CSS token fidelity, and interactive state coverage.

---

## Triage Priority Hierarchy

When issues are discovered, categorize and remediate them in strict order:

```
┌────────────────────────────────────────────────────────┐
│ P0: Blocker / Critical                                 │
│ Broken user tasks, data loss, severe A11y blockers,    │
│ missing error boundaries, infinite spinners.           │
├────────────────────────────────────────────────────────┤
│ P1: High                                               │
│ Unusable on common viewports, missing empty/error      │
│ states, keyboard traps, severe layout shifts (CLS).    │
├────────────────────────────────────────────────────────┤
│ P2: Medium                                             │
│ Spacing inconsistencies, sub-optimal touch targets,    │
│ missing hover/active feedback, token drift.            │
├────────────────────────────────────────────────────────┤
│ P3: Low / Polish                                       │
│ Browser chrome theming, optical alignment micro-nudges,│
│ smart typographic punctuation, dead CSS cleanup.       │
└────────────────────────────────────────────────────────┘
```

---

## Defect vs. System Drift Classification

Before altering code, classify the root cause to fix it at the narrowest correct architectural level:

1. **Missing Token**: The design system lacks a reusable value (e.g., an intermediate elevation shadow or responsive spacing step). Add it to root tokens, don't hardcode magic numbers.
2. **One-Off Implementation**: A bespoke element was hand-coded where an existing shared component or pattern already exists. Replace it with the system standard.
3. **Conceptual Mismatch**: The flow, hierarchy, or mental model diverges from the rest of the application. Align the interaction pattern with neighboring workflows.
4. **Local Defect**: The implementation is simply incomplete or buggy (e.g., missing focus ring or broken flex alignment). Fix the local CSS/HTML without expanding system scope.

---

## Structured Audit Report Format

When reporting technical audit findings, use this structured format:

```markdown
### Summary Score: [Total / 20]
- Accessibility: [Score / 4]
- Performance: [Score / 4]
- Responsiveness: [Score / 4]
- Visual Polish: [Score / 4]
- Resilience: [Score / 4]

### Priority Findings

#### [P0] Critical: Missing Accessible Name on Primary Action
- **Selector / Location**: `header .btn-checkout`
- **Issue**: Icon-only cart button lacks accessible label; screen readers announce "button" with no destination.
- **Fix**: Add `<span class="sr-only">Checkout (3 items)</span>` inside the `<button>`.

#### [P1] High: Layout Shift from Asynchronous Banner
- **Selector / Location**: `.hero-banner img`
- **Issue**: Banner image lacks explicit width/height or aspect-ratio, causing 0.35 CLS on initial paint.
- **Fix**: Apply `aspect-ratio: 16 / 9; width: 100%; height: auto;` in CSS.
```
