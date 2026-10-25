# Sections

This file defines all sections, their ordering, impact levels, and descriptions.
The section ID (in parentheses) is the filename prefix used to group rules.

---

## 1. Semantic HTML & Document Architecture (html)

**Impact:** CRITICAL
**Description:** Native HTML5 semantic elements, document metadata, sectioning landmarks (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`, `<search>`), text grouping, tabular data semantics (`<caption>`, `<thead>`, `<th> scope`), form structures (`<fieldset>`, `<legend>`, `<optgroup>`, `<datalist>`, `<output>`), native interactive widgets (`<dialog>`, `<details>`, `<summary>`), modern media (`<picture>`, `<video>`, `<track>`), and top-layer APIs (`popover`, `inert`). Maximizes accessibility tree integration and browser-native keyboard interactions.

## 2. Accessibility Standards [WCAG 2.2] (a11y)

**Impact:** CRITICAL
**Description:** Conformance standards for WCAG 2.2 AA and AAA criteria, including visible `:focus-visible` styling, touch and pointer hit target minimums (44×44 CSS px comfortable / 24×24 CSS px minimum), accessible SVG iconography, screen reader announcements, dynamic contrast, and persistent affordances across all device classes.

## 3. Typography & Text Rhythm (type)

**Impact:** HIGH
**Description:** Typographic scale hierarchy, fluid type sizing with `clamp()`, measure constraint (45–75 characters), unitless line height, optical tracking compensation for uppercase and display headings, tabular figures (`font-variant-numeric: tabular-nums`), true typographic quotation marks, and non-breaking spaces for widows and units.

## 4. Color Systems & Contrast (color)

**Impact:** CRITICAL
**Description:** Semantic color token architecture, OKLCH perceptual color spaces, WCAG 2.2 contrast compliance (4.5:1 text, 3:1 UI components), theme derivation, surface color pairing, and dark theme elevation modeling without generic washed-out grays.

## 5. Surfaces & Visual Polish (surface)

**Impact:** MEDIUM
**Description:** Surface geometry, concentric border radii (`outer = inner + padding`), multi-layered diffuse elevation shadows, optical centering for geometric asymmetries, browser surface theming (`::selection`, `caret-color`, `scrollbar-color`), skeleton loading aspect ratio preservation, and tactile press micro-feedback (`:active`).

## 6. Layout & Responsive (layout)

**Impact:** HIGH
**Description:** Modern fluid layouts, Container Queries (`@container`), CSS Grid with Subgrid, flexible flexbox alignments, centering via `place-content: center` and auto margins, sticky footers with `min-height: 100dvh`, split navigation via `margin-inline-start: auto`, grouping through whitespace proximity over decorative borders, scroll containers with affordance shadows, and passing the Squint Test for visual hierarchy.

## 7. Motion & Animation (motion)

**Impact:** HIGH
**Description:** Kinetic interface ergonomics, choreographing motion durations (100ms–350ms), physical spring simulations, continuous interruptibility during user input, hardware-accelerated transforms (`transform`, `opacity`), and full support for `prefers-reduced-motion` with functional static transitions.

## 8. Form UX & Ergonomics (form)

**Impact:** CRITICAL
**Description:** Ergonomic form experiences, complete `autocomplete` token maps, virtual keyboard type specialization (`inputmode`, `enterkeyhint`), error message association via `aria-describedby` and `aria-invalid`, inline validation timing, submission protection against accidental double triggers, and polite interaction validation via `:user-valid` and `:user-invalid`.

## 9. Component Patterns (comp)

**Impact:** HIGH
**Description:** Resilient UI component blueprints, accessible dialog overlays, anchored floating menus, interactive filter bars, responsive data grids, breadcrumb navigation with ordered lists and `aria-current`, pagination controls, skeleton layout states, empty states, and compound form layouts.

## 10. Technical Audit & Diagnostics (audit)

**Impact:** CRITICAL
**Description:** Structured 5-dimension quality assessment (Accessibility, Performance, Responsiveness, Polish, Resilience), priority defect triaging (P0 Blocker down to P3 Polish), separating local implementation bugs from system-wide token drift, and AI code critique standards.

## 11. UX Copywriting & Clarity (ux-copy)

**Impact:** CRITICAL
**Description:** High-clarity interface language, specific `[Verb] + [Noun]` action triggers, 3-part message architecture (Problem → Consequence → Next Action), friendly contextual guidance, and eliminating ambiguous passive dismissals (`OK`, `Submit`).

## 12. Resilience & Edge Cases (resilience)

**Impact:** CRITICAL
**Description:** Defensive CSS strategies against real-world layout stress: extreme string lengths with `overflow-wrap: break-word` and `min-width: 0`, multi-line badge wrapping, localized text expansion (+30%), zero-data empty states, huge data collections, network latency states, and gesture interruptions (`pointercancel`).

## 13. Web Performance & Core Web Vitals (perf)

**Impact:** HIGH
**Description:** Core Web Vitals optimization targeting Largest Contentful Paint (LCP < 2.5s), Interaction to Next Paint (INP < 200ms), and Cumulative Layout Shift (CLS < 0.1). Prevention of forced synchronous layout thrashing, responsive next-gen images (AVIF/WebP), and efficient DOM tree depth.

## 14. The Craft Floor & Anti-Patterns (craft)

**Impact:** HIGH
**Description:** High-craft frontend execution that polishes default browser surfaces (text selection, input carets, custom scrollbars, link underlines) while ruthlessly refusing superficial design clichés: identical 3-card grids, unearned hero metrics, decorative eyebrow kickers, cosmetic glassmorphism, and fake monospace costumes.

## 15. Real Content & Affordances (affordance)

**Impact:** CRITICAL
**Description:** Designing with representative, asymmetrical content models, establishing persistent interaction affordances without relying on hover discovery, correct cursor semantics (`pointer` only on links/buttons, `grab`, `text`), and unmistakable state communication across focus, active, loading, and disabled modes.

## 16. Modern CSS Architecture & Specifications (css)

**Impact:** HIGH
**Description:** Scalable CSS authoring, Cascade Layers (`@layer`) for explicit stylesheet precedence (`reset`, `base`, `layout`, `components`, `utilities`), single-class flat specificity (0-1-0), tokenized z-index scales on `:root`, seamless dual light/dark themes via `light-dark()` and `color-scheme`, native CSS Anchor Positioning (`anchor-name`, `position-anchor`, `position-area`), declarative scroll-driven animations (`animation-timeline: scroll()`), touch carousels via `scroll-snap-type`, animatable typed variables with `@property`, and boundary isolation with `@scope`.
