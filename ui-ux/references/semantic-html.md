# Semantic HTML First

**Impact:** CRITICAL · **Prefix:** `html-` · **Native Web Standards & Document Architecture**

Semantic HTML is interface infrastructure. Native HTML elements provide built-in keyboard accessibility, platform accessibility tree integration, standard focus states, and browser-native behaviors without requiring hundreds of lines of custom JavaScript and fragile ARIA overrides.

For an exhaustive element-by-element directory across all HTML specifications, see [`references/html-elements-reference.md`](html-elements-reference.md).

## Load When

- Constructing page structure, landmarks, navigation, or document flow
- Building interactive components (buttons, links, dialogs, disclosures, menus, popovers)
- Implementing forms, input fields, checkboxes, radio groups, and progress metrics
- Structuring relational comparison datasets or data tables
- Styling component states with native pseudo-classes (`:disabled`, `:checked`, `:open`, `:invalid`, `:popover-open`)
- Isolating background trees during modal or off-canvas interactions using `inert`
- Auditing document structure, metadata (`lang`, viewport), and landmark completeness

## Rules

| Rule | Impact | Summary |
|---|:---:|---|
| [`html-semantic-elements`](../rules/html-semantic-elements.md) | CRITICAL | Use native HTML elements (`<button>`, `<a>`, `<nav>`, `<main>`) over generic `<div>` with event listeners |
| [`html-native-state-pseudo-classes`](../rules/html-native-state-pseudo-classes.md) | MEDIUM | Style interactive states with native pseudo-classes (`:disabled`, `:open`, `:checked`) over custom data attributes |
| [`html-dialog-modal-native`](../rules/html-dialog-modal-native.md) | CRITICAL | Use native `<dialog>` with `.showModal()`, `::backdrop`, and `<form method="dialog">` for top-layer modal workflows |
| [`html-interactive-details-summary`](../rules/html-interactive-details-summary.md) | HIGH | Create zero-JS expandable accordions and disclosures using `<details>` + `<summary>` and the `name` attribute |
| [`html-table-structure-semantics`](../rules/html-table-structure-semantics.md) | CRITICAL | Structure tabular datasets with `<table>`, `<caption>`, `<thead>`, `<tbody>`, `<tfoot>`, and `<th scope="col\|row">` |
| [`html-time-datetime-attribute`](../rules/html-time-datetime-attribute.md) | MEDIUM | Provide machine-readable timestamps with `<time datetime="...">` for dates, schedules, and durations |
| [`html-media-picture-responsive`](../rules/html-media-picture-responsive.md) | HIGH | Implement responsive art direction and next-gen format fallbacks using `<picture>`, `<source>`, and accessible `<track>` |
| [`html-inert-attribute`](../rules/html-inert-attribute.md) | CRITICAL | Lock background DOM trees out of keyboard focus, screen readers, and pointers using the native boolean `inert` attribute |
| [`html-sectioning-landmarks`](../rules/html-sectioning-landmarks.md) | CRITICAL | Structure documents with `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`, and `<search>` |
| [`html-forms-advanced-semantics`](../rules/html-forms-advanced-semantics.md) | HIGH | Organize controls with `<fieldset>` + `<legend>`, `<optgroup>`, `<datalist>`, `<output>`, `<progress>`, and `<meter>` |
| [`html-popover-api-native`](../rules/html-popover-api-native.md) | HIGH | Deploy non-modal dropdowns, action menus, and tooltips using the native Popover API (`popover="auto"`) and `popovertarget` |
| [`html-global-attributes-keyboard-input`](../rules/html-global-attributes-keyboard-input.md) | HIGH | Optimize mobile data entry with `inputmode` and `enterkeyhint`; support find-in-page via `hidden="until-found"` |

---

## The First Rule of ARIA

> *"If you can use a native HTML element or attribute with the semantics and behavior already built in, then do so instead of re-purposing an element and adding an ARIA role, state, or property to make it accessible."* — W3C WAI-ARIA

### Element Selection & Decision Guide

| Intent | Native Element | Reject / Anti-Pattern | Built-in Capabilities |
|---|---|---|---|
| **Performs an action** | `<button type="button">` | `<div onclick="...">`, `<span role="button">` | Space & Enter activation, tab focusable, native disabled state |
| **Navigates to URL** | `<a href="...">` | `<button onclick="location.href=...">` | Open in new tab, bookmarkable, browser history, screen reader link role |
| **Top-layer modal** | `<dialog>` | `<div class="modal">` + JS backdrop | Native top-layer, Escape key closes, automatic focus trap via `.showModal()` |
| **Toggles visibility** | `<details>` + `<summary>` | Custom `div` accordion + JS toggle | Native toggling, Enter/Space support, keyboard focusable, `name` grouping |
| **Transient popup menu** | `<div popover="auto">` | Floating div with manual outside click | Native top-layer, automatic light-dismiss, zero z-index conflicts |
| **Page landmarks** | `<header>`, `<nav>`, `<main>`, `<aside>`, `<footer>`, `<search>` | `<div id="header">`, `<div class="nav">` | Landmark navigation in screen readers; exactly one `<main>` per page |
| **Key-value metadata** | `<dl>`, `<dt>`, `<dd>` | Nested `div` pairs with arbitrary classes | Semantic relationship between label and definition announced to AT |
| **Content sections** | `<article>`, `<section>` | Generic `<div>` containers | Distributable independent items (`<article>`) and thematic blocks (`<section>`) |
| **Data comparisons** | `<table>` with `<caption>`, `<th>` | Flexbox / CSS Grid div table | Screen reader table navigation mode, column/row coordinate reading |
| **Temporal data** | `<time datetime="...">` | Plain text strings in `<span>` | Machine-readable ISO 8601 timestamps, calendar integration, rich snippets |
| **Isolating background** | `inert` attribute | Script toggling `tabindex="-1"` and `aria-hidden` | Completely blocks tab order, screen readers, and pointers in one step |

---

## Document Meta Standards

Every HTML document must provide valid metadata for accessibility, responsiveness, and rendering engines:

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="UTF-8" />
    <!-- Essential responsive viewport meta: NEVER set user-scalable=no or maximum-scale=1 -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Descriptive, Page-Specific Title | Brand</title>
  </head>
  <body>
    <!-- Single primary content landmark -->
    <main id="main-content">
      <!-- Un-skipped heading hierarchy: h1 -> h2 -> h3 -->
      <h1>Production Analytics</h1>
    </main>
  </body>
</html>
```

### Deprecated Elements to Avoid
- Avoid obsolete presentational tags: `<b>`, `<i>`, `<center>`, `<font>`, `<big>`, `<strike>`, `<marquee>`.
- Use `<strong>` for serious importance, `<em>` for verbal emphasis, and CSS for purely visual presentation.

---

## Native Overlays: `<dialog>` and Popover API

### Modal Dialog with `<dialog>`

```html
<!-- Trigger and Dialog -->
<button type="button" id="open-modal-btn">Open Profile Settings</button>

<dialog id="settings-dialog">
  <form method="dialog">
    <header>
      <h2>Profile Settings</h2>
      <button type="submit" aria-label="Close dialog">✕</button>
    </header>
    <div class="dialog-body">
      <label for="username">Display Name</label>
      <input type="text" id="username" name="username" required>
    </div>
    <footer>
      <button type="button" id="cancel-btn">Cancel</button>
      <button type="submit" value="save">Save Changes</button>
    </footer>
  </form>
</dialog>

<script>
  const dialog = document.getElementById('settings-dialog');
  document.getElementById('open-modal-btn').addEventListener('click', () => dialog.showModal());
  document.getElementById('cancel-btn').addEventListener('click', () => dialog.close());
</script>
```

```css
dialog {
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: var(--space-6);
  box-shadow: var(--shadow-high);
  max-width: 32rem;
  width: 90vw;
}

dialog::backdrop {
  background-color: oklch(0 0 0 / 0.5);
  backdrop-filter: blur(4px);
}
```

---

## Key-Value Metadata Semantics: `<dl>`, `<dt>`, `<dd>`

Use definition lists for technical specifications, user profiles, invoice details, and metadata cards:

```html
<dl class="metadata-grid">
  <dt>Account Status</dt>
  <dd><span class="badge-success">Active</span></dd>

  <dt>Billing Cycle</dt>
  <dd>Monthly (renews on 1st)</dd>

  <dt>Seats Allocated</dt>
  <dd class="numeric">18 / 25</dd>
</dl>
```

```css
.metadata-grid {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: var(--space-2) var(--space-6);
}

.metadata-grid dt {
  color: var(--color-text-secondary);
  font-weight: 500;
}

.metadata-grid dd {
  margin: 0;
  font-weight: 600;
}
```

---

## Review Checklist for Semantic HTML

- [ ] Every clickable trigger performing an action on the page is a `<button type="button|submit">`
- [ ] Every clickable trigger changing URL or routing to a resource is an `<a>` with a valid `href`
- [ ] Document includes proper `<!DOCTYPE html>`, `<html lang="...">`, and responsive viewport `<meta>`
- [ ] Page has exactly one `<main>` landmark element and landmarks encompass all primary content
- [ ] Heading hierarchy starts with one logical `<h1>` and proceeds without skipping levels (`<h2>`, `<h3>`)
- [ ] Sectioning blocks use `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`, `<search>`
- [ ] Form controls have associated `<label for="id">` elements; radio/checkbox groups use `<fieldset>` + `<legend>`
- [ ] Tables use `<caption>`, `<thead>`, `<tbody>`, `<tfoot>`, and `<th scope="col|row">`
- [ ] Key-value metadata uses `<dl>`, `<dt>`, `<dd>` instead of unstructured div soup
- [ ] Modals leverage native `<dialog>` with `.showModal()`; dropdowns and action menus use the Popover API
- [ ] Collapsible disclosures and accordions use `<details>` + `<summary>` with modern `name` grouping
- [ ] Timestamps, schedules, and durations use `<time datetime="...">` with ISO 8601 strings
- [ ] Responsive art direction and next-gen format fallbacks use `<picture>` and `<source>`
- [ ] Background trees are isolated with the global `inert` attribute during drawer and modal interactions
- [ ] Virtual keyboards are optimized with `inputmode` and `enterkeyhint`; positive `tabindex` is avoided
- [ ] States rely on native pseudo-classes (`:disabled`, `:open`, `:checked`, `:popover-open`) rather than custom classes
