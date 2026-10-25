---
name: ui-ux
description: "Framework-agnostic web UI/UX design, technical audits, and quality diagnostics: interaction flows, semantic HTML, modern CSS specifications, responsive CSS layout recipes, typography, design tokens, motion, form ergonomics, WCAG 2.2 accessibility, the Craft Floor, Core Web Vitals, real content design, interface affordances, and modern CSS architecture."
---

# UI & UX Design Standards

A comprehensive, framework-agnostic guide for web interface design, technical quality audits, and accessibility review, grounded in native web standards, latest CSS specifications, and WCAG 2.2. Adapt its recommendations to the product, audience, existing design system, and technical constraints; distinguish conformance requirements from preferred design practices.

## Specialized Agents

Optional focused persona prompts for visual design, systems craft, and technical accessibility. Read the relevant file when a task benefits from that extra focus; they are guidance files, not a requirement to split ordinary work into separate agents.

| Agent | Role | Focus |
|-------|------|-------|
| **ui-designer-pro** | UI & Design Systems Expert | Design tokens, OKLCH palettes, typography scales, the Craft Floor, browser surface theming, concentric radii, optical alignment, diffuse elevation, cascade layers (`@layer`), tokenized z-index scales, Anchor Positioning, Layout Cookbook recipes, and refusing design clichés. |
| **ux-designer-pro** | UX, Accessibility & Diagnostics Expert | 5-dimension diagnostic audits, semantic HTML first, WCAG 2.2 AA compliance, keyboard flows, touch hit targets, real content design, interface affordances, UX copywriting clarity, form ergonomics (`:user-valid`), Core Web Vitals, fluid interruptible motion, and production resilience. |

## When to Use

Proactively assist when:
- Designing new web layouts, components, design tokens, or complete design systems
- Applying modern CSS layout recipes (centering via `place-content`, sticky footers with `100dvh`, split navigation, breadcrumbs, card footers)
- Implementing next-gen CSS specifications (Anchor Positioning, Scroll-driven animations, Scroll snap carousels, typed properties with `@property`, and boundary isolation with `@scope`)
- Running systematic technical UI audits across accessibility, performance, responsiveness, polish, and resilience
- Triaging frontend defects into structured priority tiers (P0–P3) and separating local bugs from design system drift
- Critiquing AI-generated UI code to eradicate template residue, fake lorem ipsum, and pseudo-semantics
- Structuring modern CSS architecture with Cascade Layers (`@layer`) and tokenized z-index stacking scales
- Designing with real, varied content models (uneven titles, missing optional fields, derived metadata)
- Auditing interface affordances to ensure critical actions are never hidden behind hover alone
- Rewriting unclear UI copy, button labels, error alerts, and destructive confirmation dialogs
- Hardening interfaces against real-world edge cases (extreme text lengths, localized expansion, network latency, interrupted pointer gestures)
- Optimizing Core Web Vitals (LCP, INP, CLS) and eliminating forced layout thrashing
- Defining CSS custom property tokens (colors, typography, spacing, shadows, radii)
- Implementing or refactoring forms, virtual keyboard triggers, validation timing with `:user-valid`/`:user-invalid`, and double-submit prevention
- Choosing typography pairings, modular fluid scales via `clamp()`, tabular numbers, or optical letter-spacing
- Structuring continuous physical motion, interruptible transitions, springs, duration tokens, and intentional reduced-motion alternatives
- Establishing the Craft Floor by theming browser-native surfaces (`::selection`, `caret-color`, `scrollbar-color`, `text-underline-offset`)

## Working Approach

Start from the user's goal, context, and task. Identify the key content, actions, states, and constraints before choosing a visual treatment. For an existing product, preserve its design language unless the user asks for a redesign. When details are unknown, state practical assumptions and make the smallest coherent design decision.

For design or implementation work, cover all essential states: default, hover, focus-visible, active, disabled where appropriate, loading, empty, success, and error. Consider narrow viewports, zoom/reflow, keyboard use, and reduced motion. For reviews, report concrete findings with impact, evidence, and an actionable fix; categorize defects by priority and identify whether the root cause is a local bug, a missing token, a one-off implementation, or a conceptual mismatch.

## Core Philosophy

1. **Prefer Native Semantics**: Use native HTML controls (`<button>`, `<a>`, `<dialog>`, `<details>`, `<dl>`) before recreating behaviors with custom ARIA and JavaScript.
2. **Establish the Craft Floor**: Unstyled browser defaults are defects. Theme text selection, input carets, scrollbars, link underlines, and tabular numbers directly from the brand palette.
3. **Declarative Modern CSS over JS Layouts**: Leverage modern platform features (Anchor Positioning, Scroll-driven animations, Scroll Snap, CSS Subgrid, `@layer`, `@property`, `@scope`) to deliver fluid 60fps experiences with zero JavaScript layout recalculations.
4. **Real Content Shapes Layouts**: Design with representative, varied content models rather than uniform placeholders. Do not force artificial copy lengths to rescue a rigid card grid.
5. **Perceptible Affordances**: Critical actions must never depend on hover alone. All interactive states (default, hover, focus-visible, pressed, selected, disabled, loading) must explain themselves visually and functionally.
6. **Continuous Physical Motion**: Interfaces feel natural when they behave like responsive physical systems. Interactive motion must be interruptible, preserve velocity across gestures, and prefer natural springs over locked keyframes.
7. **Modern CSS Architecture**: Govern cascade precedence with Cascade Layers (`@layer`) and keep selector specificity flat (0-1-0). Eliminate magic numbers (`z-index: 9999`) with a disciplined tokenized stacking scale.
8. **Refuse Habitual Clichés**: Reject reflexive design habits (identical 3-card grids, hero-metrics by reflex, eyebrow badges on every heading, arbitrary section numbers, gradient text, cosmetic glassmorphism, and monospace as a technical costume) unless the brief explicitly earns them.
9. **Interface Copy as Core Design Material**: Eliminate vague labels and internal jargon. Structure messages by Problem → Consequence → Next Action. Controls must declare their precise action; errors must provide actionable recovery.
10. **Defend Against Real-World Chaos**: Real interfaces encounter extreme string lengths, localization expansion (+30%), empty datasets, 10,000+ items, network timeouts, and interrupted pointer interactions. Design defensively.
11. **Web Performance is Foundational UX**: Eliminate synchronous layout thrashing (batch DOM reads before writes), reserve explicit image dimensions to avoid CLS, and optimize the rendering pipeline for smooth 60fps interaction.

## Core Directives

### MUST DO

- **Semantic HTML**: Use `<button>` for actions, `<a>` for navigation, `<dialog>` for modals, `<main>` for primary content.
- **Native State Pseudo-Classes**: Style element states with native pseudo-classes (`:disabled`, `:checked`, `:open`, `:invalid`, `:read-only`) rather than custom data attributes.
- **Cascade Layers (`@layer`)**: Organize stylesheet precedence into explicit layers (`reset`, `base`, `layout`, `components`, `utilities`) to prevent specificity wars.
- **Tokenized Z-Index Scale**: Restrict z-index declarations to semantic tokens (`--z-dropdown`, `--z-modal`, `--z-toast`) on `:root`.
- **Modern Centering**: Use `display: grid; place-content: center;` or `margin: auto` over legacy absolute-transform hacks.
- **Sticky Footer Baseline**: Use `grid-template-rows: auto 1fr auto; min-height: 100dvh;` to pin footers cleanly on short content.
- **Split Navigation**: Use `margin-inline-start: auto` within flex navigation bars for clean, bidirectional link alignment.
- **Breadcrumb Navigation**: Structure breadcrumbs with `<nav aria-label="Breadcrumb"> <ol>` and mark active step with `aria-current="page"`.
- **Anchor Positioning**: Position floating popovers, tooltips, and contextual menus with native `anchor-name` and `position-anchor`.
- **Scroll-Driven Animations**: Link scroll progress indicators and reveal transitions to `animation-timeline: scroll()` or `view()` for GPU-driven 60fps performance.
- **Touch Carousels via Scroll Snap**: Implement horizontal galleries using native `scroll-snap-type: x mandatory` and `scroll-snap-align: start`.
- **Animatable Custom Properties**: Register typed CSS tokens via `@property` (`syntax: "<percentage>"`) for smooth transitions on gradients and variables.
- **Polite Validation Timing**: Use `:user-valid` and `:user-invalid` so inputs show validation borders only after the user has interacted.
- **Persistent Affordances**: Ensure all primary actions and status cues remain discoverable without requiring mouse hover; support `:focus-within` on pointer containers.
- **Interruptible Interactive Motion**: Ensure animations triggered by users can be redirected or reversed immediately without waiting out locked keyframes.
- **The Craft Floor Theming**: Theme native browser surfaces (`::selection`, `caret-color`, `scrollbar-color`, and `text-underline-offset`) from the project palette.
- **Action-Oriented Control Verbs**: Use specific `[Verb] + [Noun]` labels (`Publish article`, `Delete workspace`) instead of vague placeholders (`Submit`, `OK`, `Yes`).
- **Defensive Text Containers**: Apply `min-width: 0` and `overflow-wrap: break-word` on flex and grid children containing dynamic or user-generated text.
- **Tabular Figures**: Apply `font-variant-numeric: tabular-nums` to numerical data tables, countdown timers, price tags, and metric counters.
- **Batch DOM Reads & Writes**: In performance-sensitive code, batch all geometric reads (`offsetHeight`, `getBoundingClientRect`) before performing style writes to prevent layout thrashing.
- **Responsive Images & CLS Prevention**: Serve modern image formats (AVIF/WebP) with explicit `aspect-ratio` or `width`/`height` attributes.
- **Form Association & Autofill**: Bind inputs with persistent `<label>` tags, provide relevant `autocomplete` tokens, and associate errors via `aria-describedby` and `aria-invalid`.
- **Mobile Input Font Size**: Enforce at least 16 CSS px (`max(1rem, 16px)`) on inputs, selects, and textareas to prevent mobile browser auto-zoom.
- **Comfortable Hit Targets**: Aim for comfortable targets (44×44 CSS px); check WCAG 2.2 SC 2.5.8's 24×24 CSS px minimum with spacing exceptions.
- **Spacing Rhythm & Proximity**: Group related elements through tight spacing intervals; allocate noticeably more space *above* a heading than *below* it.
- **Streamlined Themes with `light-dark()`**: Use `color-scheme: light dark;` and `light-dark()` on `:root` to eliminate duplicate dark-mode media query blocks.
- **Heading Tracking Floor**: Tighten display and headline letter spacing (-0.02em to -0.04em); loosen tracking (+0.05em to +0.1em) on all-caps text.
- **Readable Measure**: Keep body copy reading columns constrained to 45–75 characters (optimal 65ch) with unitless `line-height`.
- **Concentric Radii**: When nesting rounded surfaces with padding, ensure `outer_radius = inner_radius + padding`.
- **Intentional Reduced Motion**: Support `prefers-reduced-motion` with functional non-spatial transitions without stripping visual focus or status feedback.

### MUST NOT DO

- **No Absolute Transform Centering Hacks**: Never use `position: absolute; top: 50%; transform: translate(-50%, -50%)`; it causes blurry text and animation collisions.
- **No JS Scroll Animation Listeners**: Never bind `window.onscroll` to animate properties; use CSS `animation-timeline`.
- **No Bulky JS Carousel Libraries**: Do not import heavy slider plugins when native CSS Scroll Snap meets the requirement.
- **No Premature Red Error Borders**: Do not use raw `:invalid` on required inputs before interaction; use `:user-invalid`.
- **No Hover-Only Critical Actions**: Never hide essential buttons, links, or controls behind mouse hover alone.
- **No Magic Z-Index Numbers**: Never write `z-index: 9999` or random large integers; use the tokenized stacking scale.
- **No Locked Keyframe Blockers**: Do not lock user interactions behind long (500ms+) non-interruptible `@keyframes` sequences.
- **No Custom State Classes for Native Controls**: Do not use `.is-disabled` or `data-disabled` where native `:disabled` applies.
- **No Outline Removal**: Never write `outline: none` or `outline: 0` without immediately supplying a contrasting `:focus-visible` replacement.
- **No Div Buttons**: Never attach click listeners to generic `<div>` or `<span>` elements without native button semantics.
- **No Blunt Universal Motion Reset**: Never apply `* { transition: 0.01ms !important; animation: 0.01ms !important; }`; it destroys focus rings, hover cues, and status awareness.
- **No Habitual Card Grids**: Do not split every page into identical 3-column cards of icon + heading + text by reflex. Never nest cards inside cards.
- **No Eyebrow Labels by Default**: Do not place small uppercase category kickers above every heading; let the heading speak for itself.
- **No Generic Gray on Colored Surfaces**: Never use washed-out generic gray for secondary text on colored backgrounds; derive it from the surface hue or foreground.
- **No Hard Offset Shadows (Outside Neobrutalism)**: Avoid raw `box-shadow: 4px 4px 0` block shadows; use multi-layered soft ambient blur.
- **No Monospace as a Costume**: Do not use monospace fonts to make regular text look "technical"; reserve monospace strictly for code, hashes, and CLI output.
- **No Form Double Submissions**: Never leave submit buttons enabled during asynchronous network requests; prevent concurrent mutations.
- **No Layout-Driving Property Animations**: Do not animate `width`, `height`, `top`, `left`, `margin`, or `padding`; use `transform` and `opacity` for smooth 60fps rendering.
- **No Trapping Tab Order**: Avoid positive `tabindex` values; they disrupt natural document sequence.

## Category Index

| # | Category | Impact | Load when… | Reference | Prefix | Rules |
|---|----------|:------:|------------|-----------|:------:|:-----:|
| 1 | Semantic HTML First | CRITICAL | Constructing document flow, landmarks, interactive controls, tables, top-layer overlays | [`references/semantic-html.md`](references/semantic-html.md) / [`references/html-elements-reference.md`](references/html-elements-reference.md) | `html-` | 12 |
| 2 | Accessibility (WCAG 2.2) | CRITICAL | Keyboard navigation, focus rings, touch targets, screen readers | [`references/accessibility.md`](references/accessibility.md) | `a11y-` | 6 |
| 3 | Typography & Text Rhythm | HIGH | Modular scales, fluid typography, leading, tracking, smart quotes | [`references/typography.md`](references/typography.md) | `type-` | 5 |
| 4 | Color Systems & Contrast | CRITICAL | Token architecture, OKLCH, contrast ratios, state derivation | [`references/color-systems.md`](references/color-systems.md) | `color-` | 3 |
| 5 | Surfaces & Visual Polish | MEDIUM | Concentric border radius, optical alignment, diffuse elevation | [`references/design-tokens-and-surfaces.md`](references/design-tokens-and-surfaces.md) | `surface-` | 5 |
| 6 | Layout & Responsive | HIGH | Container queries, mobile-first, subgrid, scroll affordances, Layout Cookbook recipes, Squint Test | [`references/layout-and-responsive.md`](references/layout-and-responsive.md) / [`references/css-layout-cookbook.md`](references/css-layout-cookbook.md) | `layout-` | 6 |
| 7 | Motion & Animation | HIGH | Choreography, duration scales, easing, hardware acceleration, springs | [`references/motion-and-animation.md`](references/motion-and-animation.md) | `motion-` | 3 |
| 8 | Form UX & Ergonomics | CRITICAL | Input types, virtual keyboards, autocomplete, error timing | [`references/form-ux-and-patterns.md`](references/form-ux-and-patterns.md) | `form-` | 1 |
| 9 | Component Patterns | HIGH | Overlays, responsive tables, breadcrumbs, pagination, popover API, anchor positioning | [`references/components-and-patterns.md`](references/components-and-patterns.md) | `comp-` | 1 |
| 10 | Technical Audit & Diagnostics | CRITICAL | Code-level quality checks, 5-dimension scan (0–4), P0–P3 triage, AI critique | [`references/ui-ux-audit-and-diagnostics.md`](references/ui-ux-audit-and-diagnostics.md) | `audit-` | — |
| 11 | UX Copywriting & Clarity | CRITICAL | Action-oriented verbs, 3-part message hierarchy, error recovery | [`references/ux-copywriting-and-clarity.md`](references/ux-copywriting-and-clarity.md) | `ux-copy-` | 1 |
| 12 | Resilience & Edge Cases | CRITICAL | Defensive CSS, extreme strings, i18n, interrupted gestures | [`references/resilience-and-edge-cases.md`](references/resilience-and-edge-cases.md) | `resilience-` | 1 |
| 13 | Web Performance & CWV | HIGH | Core Web Vitals (LCP, INP, CLS), layout thrashing, image formats | [`references/web-performance-and-cwv.md`](references/web-performance-and-cwv.md) | `perf-` | 2 |
| 14 | The Craft Floor & Anti-Patterns | HIGH | Browser chrome theming, decluttering, refusing visual clichés | [`references/craft-floor-and-anti-patterns.md`](references/craft-floor-and-anti-patterns.md) | `craft-` | — |
| 15 | Real Content & Affordances | CRITICAL | Real content modeling, perceptible actions, cursor semantics, state clarity | [`references/real-content-and-affordances.md`](references/real-content-and-affordances.md) | `affordance-` | — |
| 16 | Modern CSS Architecture & Specs | HIGH | Cascade layers (`@layer`), flat specificity, z-index scales, Anchor Positioning, Scroll Animations, `@property`, `@scope`, `:user-valid` | [`references/modern-css-architecture.md`](references/modern-css-architecture.md) / [`references/modern-css-reference.md`](references/modern-css-reference.md) | `css-` | 9 |

## Rule Index

### Semantic HTML (`html-`) — CRITICAL / HIGH / MEDIUM
[`html-semantic-elements`](rules/html-semantic-elements.md) · [`html-native-state-pseudo-classes`](rules/html-native-state-pseudo-classes.md) · [`html-dialog-modal-native`](rules/html-dialog-modal-native.md) · [`html-interactive-details-summary`](rules/html-interactive-details-summary.md) · [`html-table-structure-semantics`](rules/html-table-structure-semantics.md) · [`html-time-datetime-attribute`](rules/html-time-datetime-attribute.md) · [`html-media-picture-responsive`](rules/html-media-picture-responsive.md) · [`html-inert-attribute`](rules/html-inert-attribute.md) · [`html-sectioning-landmarks`](rules/html-sectioning-landmarks.md) · [`html-forms-advanced-semantics`](rules/html-forms-advanced-semantics.md) · [`html-popover-api-native`](rules/html-popover-api-native.md) · [`html-global-attributes-keyboard-input`](rules/html-global-attributes-keyboard-input.md)

### Accessibility (`a11y-`) — CRITICAL / HIGH
[`a11y-focus-visible`](rules/a11y-focus-visible.md) · [`a11y-form-labels-errors`](rules/a11y-form-labels-errors.md) · [`a11y-hit-targets`](rules/a11y-hit-targets.md) · [`a11y-accessible-svg-icons`](rules/a11y-accessible-svg-icons.md) · [`a11y-ios-input-zoom`](rules/a11y-ios-input-zoom.md) · [`a11y-no-hover-only-critical-actions`](rules/a11y-no-hover-only-critical-actions.md)

### Typography (`type-`) — HIGH / MEDIUM
[`type-fluid-scale`](rules/type-fluid-scale.md) · [`type-tabular-numerals`](rules/type-tabular-numerals.md) · [`type-measure-and-leading`](rules/type-measure-and-leading.md) · [`type-curly-quotes`](rules/type-curly-quotes.md) · [`type-non-breaking-spaces`](rules/type-non-breaking-spaces.md)

### Color Systems (`color-`) — CRITICAL / MEDIUM
[`color-semantic-tokens`](rules/color-semantic-tokens.md) · [`color-contrast-wcag`](rules/color-contrast-wcag.md) · [`color-state-derivation`](rules/color-state-derivation.md)

### Modern CSS Architecture & Specs (`css-`) — HIGH / MEDIUM
[`css-cascade-layers-and-specificity`](rules/css-cascade-layers-and-specificity.md) · [`css-tokenized-z-index-scale`](rules/css-tokenized-z-index-scale.md) · [`css-modern-color-light-dark`](rules/css-modern-color-light-dark.md) · [`css-anchor-positioning`](rules/css-anchor-positioning.md) · [`css-scroll-driven-animations`](rules/css-scroll-driven-animations.md) · [`css-scroll-snap-carousel`](rules/css-scroll-snap-carousel.md) · [`css-typed-custom-properties`](rules/css-typed-custom-properties.md) · [`css-scope-donut`](rules/css-scope-donut.md) · [`css-form-user-validity`](rules/css-form-user-validity.md)

### Surfaces & Polish (`surface-`) — MEDIUM / HIGH
[`surface-concentric-radius`](rules/surface-concentric-radius.md) · [`surface-optical-alignment`](rules/surface-optical-alignment.md) · [`surface-browser-chrome-theming`](rules/surface-browser-chrome-theming.md) · [`surface-aspect-ratio-skeletons`](rules/surface-aspect-ratio-skeletons.md) · [`surface-press-scale`](rules/surface-press-scale.md)

### Layout & Responsive (`layout-`) — HIGH / MEDIUM
[`layout-container-queries`](rules/layout-container-queries.md) · [`layout-modern-centering`](rules/layout-modern-centering.md) · [`layout-sticky-footer`](rules/layout-sticky-footer.md) · [`layout-split-navigation`](rules/layout-split-navigation.md) · [`layout-proximity-over-borders`](rules/layout-proximity-over-borders.md) · [`layout-scroll-shadows`](rules/layout-scroll-shadows.md)

### Motion & Animation (`motion-`) — HIGH / CRITICAL
[`motion-hardware-acceleration`](rules/motion-hardware-acceleration.md) · [`motion-interruptible-springs`](rules/motion-interruptible-springs.md) · [`motion-reduced-motion`](rules/motion-reduced-motion.md)

### Component Patterns (`comp-`) — HIGH
[`comp-breadcrumbs-nav`](rules/comp-breadcrumbs-nav.md)

### Form UX (`form-`) — HIGH
[`form-autocomplete-attributes`](rules/form-autocomplete-attributes.md)

### UX Copywriting (`ux-copy-`) — HIGH
[`ux-copy-action-verbs`](rules/ux-copy-action-verbs.md)

### Production Resilience (`resilience-`) — HIGH / CRITICAL
[`resilience-text-overflow-wrap`](rules/resilience-text-overflow-wrap.md)

### Web Performance (`perf-`) — HIGH / CRITICAL
[`perf-prevent-layout-thrashing`](rules/perf-prevent-layout-thrashing.md) · [`perf-modern-image-formats`](rules/perf-modern-image-formats.md)

## Validation Checklist

- [ ] All interactive controls use semantic native HTML elements (`<button>`, `<a>`, `<dialog>`, `<input>`)
- [ ] Interactive states are styled via native pseudo-classes (`:disabled`, `:open`, `:checked`, `:invalid`, `:user-valid`, `:user-invalid`)
- [ ] Stylesheet precedence is organized into Cascade Layers (`@layer`) with flat single-class specificity
- [ ] Z-index values strictly follow the tokenized stacking scale without magic numbers (`9999`)
- [ ] Element centering uses `place-content: center` or `margin: auto` over absolute-transform hacks
- [ ] Page layouts use `min-height: 100dvh` and Grid rows to pin footers cleanly on short content
- [ ] Navigation bars use `margin-inline-start: auto` for direction-aware link splitting
- [ ] Breadcrumb navigation uses semantic `<nav> <ol>` with `aria-current="page"` and CSS separators
- [ ] Floating elements leverage native CSS Anchor Positioning (`anchor-name`, `position-anchor`)
- [ ] Scroll progress and reveal animations use `animation-timeline: scroll()` or `view()` for GPU acceleration
- [ ] Touch carousels use native `scroll-snap-type` and `scroll-snap-align` over heavy JS plugins
- [ ] Animatable variables in gradients and tokens are registered via `@property`
- [ ] Boundary-sensitive components isolate styles using `@scope`
- [ ] Essential actions and primary affordances are never hidden behind `:hover` alone
- [ ] Interactive transitions and animations are interruptible and preserve continuous velocity
- [ ] Keyboard navigation is smooth and logical with visible `:focus-visible` rings (min 2px with offset)
- [ ] Interactive targets are comfortably sized (44×44 CSS px) and meet WCAG 2.2 SC 2.5.8 minimums (24×24 CSS px)
- [ ] Decorative SVGs use `aria-hidden="true"`; icon-only buttons have accessible text labels (`.sr-only`)
- [ ] Form controls have persistent `<label>` tags and displayed errors are associated with `aria-describedby`
- [ ] Form inputs use appropriate `autocomplete` tokens; computed font-size is at least 16px to prevent mobile auto-zoom
- [ ] Contrast ratios meet WCAG AA: ≥ 4.5:1 for body text and ≥ 3:1 for large text and UI components
- [ ] Reusable colors use semantic roles; secondary text on colored surfaces is derived from the hue, not generic gray
- [ ] Dark theme surfaces use explicit lightness elevation steps or native `light-dark()` rather than raw black
- [ ] Native browser surfaces (`::selection`, `caret-color`, `scrollbar-color`, `text-underline-offset`) are themed from the palette
- [ ] Interactive controls use specific action verbs (`Publish draft`, `Save changes`) over generic labels (`Submit`, `OK`)
- [ ] Form submit buttons prevent double-submission by disabling and setting `aria-busy="true"` during asynchronous requests
- [ ] Flex and grid text containers include `min-width: 0` and `overflow-wrap: break-word` to defend against container blowout
- [ ] Structured numerical data (counters, timers, table metrics) uses `font-variant-numeric: tabular-nums`
- [ ] Long-form reading lines are constrained to 45–75 characters with unitless `line-height`
- [ ] Display headings have tightened tracking (-0.02em to -0.04em); all-caps labels have loosened tracking (+0.05em)
- [ ] Nested rounded corners align with the concentric formula (`outer = inner + padding`)
- [ ] Optical compensation is applied to asymmetric shapes and cap-height icon alignments
- [ ] Clickable controls provide tactile micro-feedback via `:active` scale (`transform: scale(0.97)`)
- [ ] Visual hierarchy passes the Squint Test; proximity establishes grouping without unnecessary container borders
- [ ] Headings have visibly more space above them than below them (`margin-top > margin-bottom`)
- [ ] Multi-column layouts adapt gracefully to single-column mobile views, tablet master-detail, and print stylesheets
- [ ] Images serve modern responsive formats (AVIF/WebP) and reserve explicit `aspect-ratio` to prevent CLS
- [ ] Performance-critical JavaScript batches all DOM reads before writes to eliminate forced layout thrashing
- [ ] Non-essential motion avoids layout recalculations and respects `prefers-reduced-motion` with intentional alternatives
- [ ] Custom drag and slider gestures gracefully handle `pointercancel`, `lostpointercapture`, and window blur
