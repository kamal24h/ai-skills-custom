# HTML Elements & Attributes Technical Reference

**Standards Baseline:** W3C / WHATWG HTML Living Standard & MDN Web Reference  
**Focus:** Semantic Architecture, Accessibility Tree Mapping, Keyboard Interaction & Native Browser Engine Behaviors

This reference provides a definitive technical mapping of native HTML elements, grouping semantics, content categories, and global attributes for professional web UI/UX development.

---

## 1. Document & Metadata

Metadata elements define document-level properties, character encoding, title hierarchy, viewport configuration, and relationships to external stylesheets and scripts.

| Element | Primary Purpose | Required / Critical Attributes | Accessibility & UX Impact |
|---|---|---|---|
| `<!DOCTYPE html>` | Triggers Standards Mode in modern browsers. | None. Must be the very first line of the document. | Prevents Quirks Mode layout bugs and legacy rendering behaviors. |
| `<html lang="..." dir="...">` | Document root container. | `lang` (e.g. `en`, `tr`, `de`), `dir` (`ltr`, `rtl`). | Crucial for screen reader pronunciation, font glyph substitution, and hyphenation. |
| `<head>` | Machine-readable metadata container. | None. | Contains non-rendered instructions parsed before document body rendering. |
| `<meta charset="UTF-8">` | Declares document character encoding. | `charset="UTF-8"` (must appear in first 1024 bytes). | Prevents UTF-8 character mangling and cross-site scripting vulnerabilities. |
| `<meta name="viewport">` | Sets initial layout viewport size and scaling. | `content="width=device-width, initial-scale=1.0"`. | Responsive layout baseline. **Never** set `user-scalable=no` or `maximum-scale=1`. |
| `<title>` | Canonical window / tab title. | Text content only. | Announced first when screen reader loads page; primary label in bookmarks/search. |
| `<link rel="...">` | Connects document to external resources. | `rel="stylesheet"`, `rel="icon"`, `rel="preload"`, `rel="canonical"`. | Governs resource priority and preloading behaviors without layout blocking. |
| `<base href="...">` | Specifies baseline URL for all relative URLs. | `href="..."`. | Centralizes path resolution; must appear before any link or script tags. |

### Document Metadata Boilerplate

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Customer Dashboard | Acme Cloud</title>
    <link rel="stylesheet" href="/assets/styles.css" />
  </head>
  <body>
    <!-- Document content -->
  </body>
</html>
```

---

## 2. Sectioning & Landmarks

Landmarks establish the high-level structural map of a webpage. Screen readers construct a navigational "rotor" of landmarks, enabling users to jump directly between primary regions.

| Element | ARIA Role Mapping | Usage Constraints | When to Use |
|---|---|---|---|
| `<header>` | `banner` (when top-level) | Do not nest multiple top-level `<header>` elements. Can be used inside `<article>`/`<section>`. | Site logo, global navigation, user profile trigger, or article introductory banner. |
| `<nav>` | `navigation` | Always provide unique `aria-label` when multiple nav elements exist. | Primary site navigation, breadcrumbs (`aria-label="Breadcrumb"`), pagination. |
| `<main>` | `main` | **Strictly 1 visible `<main>` per document.** Never nest inside `<article>`, `<aside>`, or `<header>`. | Primary unique content of the page; excludes repeated headers, navs, and footers. |
| `<article>` | `article` | Must represent a self-contained, distributable composition. | Blog posts, news items, product cards, forum threads, user review items. |
| `<section>` | `region` (when labeled) | Must have a descriptive heading (`<h2>`–`<h6>`) or `aria-labelledby`. | Thematic grouping of content within an article or page; never use as pure styling div. |
| `<aside>` | `complementary` | Content tangentially related to the main content. | Sidebars, related links, author bio callouts, glossary side-panels. |
| `<footer>` | `contentinfo` (when top-level) | Can appear at page level or scoped inside `<article>`/`<section>`. | Copyright notices, legal links, author credits, document metadata. |
| `<search>` | `search` | Modern HTML5 standard element. Replaces `<div role="search">`. | Container for site search forms, filtering bars, and search inputs. |
| `<hgroup>` | `group` | Groups a primary heading with subtitles, kickers, or taglines. | Prevents decorative subheadings from polluting document heading outlines. |
| `<address>` | `group` | Strictly for contact information of the author/owner. | Physical address, contact email, phone numbers for the site or article author. |

### Landmark Architecture Blueprint

```html
<header class="site-header">
  <a href="/" class="brand-link">Acme</a>
  <nav aria-label="Primary navigation">
    <ul>
      <li><a href="/dashboard">Dashboard</a></li>
      <li><a href="/reports">Reports</a></li>
    </ul>
  </nav>
  <search>
    <form action="/search" method="get">
      <input type="search" name="q" placeholder="Search..." aria-label="Search" />
    </form>
  </search>
</header>

<main id="main-content">
  <hgroup>
    <h1>Quarterly Performance</h1>
    <p>Financial results for Q3 2026</p>
  </hgroup>

  <section aria-labelledby="revenue-heading">
    <h2 id="revenue-heading">Revenue Streams</h2>
    <!-- Relational metrics -->
  </section>
</main>

<footer class="site-footer">
  <p>© 2026 Acme Corp.</p>
</footer>
```

---

## 3. Text & Grouping

Text and grouping elements govern typographic hierarchy, inline semantics, code notation, temporal stamps, and structured lists.

| Element | Semantic Category | Best Practice / Requirement | Anti-Pattern to Reject |
|---|---|---|---|
| `<p>` | Paragraph | Standard text block. Never put block elements (`<div>`, `<table>`) inside `<p>`. | `<div class="p">` or multiple `<br><br>` hacks for paragraph separation. |
| `<h1>`–`<h6>` | Headings | Maintain sequential hierarchy without skipping (`h1` → `h2` → `h3`). | Skipping levels (`h1` → `h4`) for visual font size convenience. |
| `<blockquote>` | Extended Quotation | Encloses multi-line quoted citations; optional `cite="..."` attribute. | Quotes without `<cite>` or generic styled divs. |
| `<pre>` | Preformatted Text | Preserves whitespace and linebreaks exactly as typed in source. | Manually adding `&nbsp;` and `<br>` to replicate preformatted layout. |
| `<code>` | Inline / Block Code | Represents machine-readable computer code, keywords, or variables. | Unsemantic `<span>` with monospace font styles. |
| `<kbd>` | User Input Key | Represents keyboard input keys (`<kbd>Ctrl</kbd> + <kbd>C</kbd>`). | Generic styled spans lacking accessibility input announcements. |
| `<time>` | Temporal Stamp | Must include valid machine-readable `datetime="YYYY-MM-DDTHH:MM:SSZ"`. | Plain text dates (`3 hours ago`) without machine-readable `datetime`. |
| `<mark>` | Highlighted Text | Represents text highlighted for relevance or search match in current context. | `<span>` with yellow background color. |
| `<abbr>` | Abbreviation / Acronym | Use `title="..."` to expand acronym on first occurrence on a page. | Unexpanded jargon causing cognitive friction. |
| `<ul>`, `<ol>`, `<li>` | Unordered & Ordered Lists | Use `<ul>` for order-independent sets; `<ol>` for sequential procedures. | Div stacks with fake bullet characters (`•`). |
| `<dl>`, `<dt>`, `<dd>` | Definition / Metadata List | `<dt>` specifies term/label; `<dd>` specifies value/definition. | Key-value pairs rendered as unstructured div soup. |
| `<figure>`, `<figcaption>` | Self-Contained Illustration | Encloses diagrams, photos, code snippets, or charts with caption. | Disconnected image and paragraph without programmatic linkage. |
| `<strong>` | Strong Importance | Indicates serious importance or urgency (not purely visual bolding). | Obsolete `<b>` for important warnings. |
| `<em>` | Verbal Emphasis | Alters the vocal stress and meaning of a sentence. | Obsolete `<i>` for semantic stress. |
| `<small>` | Side Comments / Fine Print | Legal disclaimers, copyright notices, terms conditions. | Misusing `<small>` for primary subheadings or secondary UI copy. |

### Definition List Example for Relational Metadata

```html
<dl class="specs-grid">
  <dt>Server Location</dt>
  <dd>Frankfurt (fra-01)</dd>

  <dt>Encrypted At Rest</dt>
  <dd>AES-256-GCM</dd>

  <dt>Provisioned Date</dt>
  <dd><time datetime="2026-04-12">April 12, 2026</time></dd>
</dl>
```

---

## 4. Table Semantics

Data tables communicate multi-dimensional relationships between variables. Every table must provide clear programmatic connections between headers and data cells.

| Element | Role | Required Semantic Attributes | Purpose |
|---|---|---|---|
| `<table>` | Data grid container | None. | Establishes tabular layout and screen reader table navigation mode. |
| `<caption>` | Table title & description | Place as immediate first child of `<table>`. | Provides canonical accessible name announced upon table focus. |
| `<thead>` | Column header group | Encloses header `<tr>` rows. | Separates header definitions from data rows; repeats on print pages. |
| `<tbody>` | Data rows container | Encloses data `<tr>` rows. | Contains primary content cells (`<td>`). |
| `<tfoot>` | Summary / totals row group | Place at bottom of table. | Summarizes totals, averages, or footnotes across columns. |
| `<tr>` | Table row | Container for cells. | Organizes horizontal records. |
| `<th>` | Header cell | `scope="col"` for columns, `scope="row"` for row headers. | Maps header name to all corresponding data cells in that axis. |
| `<td>` | Data cell | None. | Individual relational data point. |
| `<colgroup>`, `<col>` | Column formatting | `span="..."`, `class="..."`. | Applies column-wide widths and styling without touching individual cells. |

### Accessible Table Blueprint

```html
<div class="table-container" tabindex="0" role="region" aria-labelledby="billing-table-cap">
  <table>
    <caption id="billing-table-cap">Monthly Invoices & Settlement History</caption>
    <thead>
      <tr>
        <th scope="col">Invoice ID</th>
        <th scope="col">Issue Date</th>
        <th scope="col">Status</th>
        <th scope="col">Amount</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">INV-2026-081</th>
        <td><time datetime="2026-10-01">Oct 1, 2026</time></td>
        <td>Paid</td>
        <td class="numeric">$1,450.00</td>
      </tr>
    </tbody>
    <tfoot>
      <tr>
        <th scope="row" colspan="3">Total Outstanding</th>
        <td class="numeric">$0.00</td>
      </tr>
    </tfoot>
  </table>
</div>
```

---

## 5. Forms & Controls

Native HTML form elements provide built-in focus management, platform validation, and screen reader bindings.

| Element | Native Capability | Essential Attributes | Common UX Failure |
|---|---|---|---|
| `<form>` | Submission orchestration | `action`, `method`, `novalidate` (for custom validation). | Submitting without preventing duplicate clicks or lacking submit button. |
| `<label>` | Input association & tap target expansion | `for="inputId"` matching input's `id`. | Wrapping inputs without `for` or using unassociated text. |
| `<input>` | Data entry control | `type`, `id`, `name`, `autocomplete`, `inputmode`. | Missing `type` or omitting mobile keyboard optimizations. |
| `<button>` | Action trigger | `type="button"`, `type="submit"`, `type="reset"`. | Forgetting `type="button"`, causing unintended form submission on click. |
| `<select>` | Option picker dropdown | `id`, `name`, `required`. | Inaccessible custom JS dropdowns replacing native select on mobile. |
| `<optgroup>` | Categorical group in select | `label="Category Name"`. | Flat dropdown with 100+ unorganized options. |
| `<option>` | Selectable item | `value="..."`. | Missing value attribute causing label text to submit as raw data. |
| `<textarea>` | Multi-line text input | `id`, `name`, `rows`, `maxlength`. | Using `contenteditable` divs instead of native textarea. |
| `<fieldset>` | Form control group container | Contains `<legend>` as first child. | Ungrouped radio buttons leaving auditory context undefined. |
| `<legend>` | Accessible group caption | Immediate first child of `<fieldset>`. | Placing legend outside fieldset or using a plain paragraph. |
| `<datalist>` | Freeform input suggestions | `id="..."` referenced by input's `list="..."`. | Reinventing autocomplete with fragile JS dropdowns. |
| `<output>` | Calculation result container | `for="inputA inputB"`. | Disconnected text span lacking programmatic formula linkage. |
| `<progress>` | Task completion indicator | `value="..."`, `max="..."`. | Custom div progress bar lacking ARIA value properties. |
| `<meter>` | Fractional scalar measurement | `min`, `max`, `value`, `low`, `high`, `optimum`. | Misusing progress bars for disk capacity or battery levels. |

---

## 6. Embedded & Media

Modern media elements enable art direction, device optimization, and multi-modal accessibility.

| Element | Optimal Use Case | Required Attributes | Fallback Behavior |
|---|---|---|---|
| `<picture>` | Art direction and modern format negotiation. | Container for `<source>` and one closing `<img>`. | Must always conclude with a standard `<img>` for rendering. |
| `<source>` | Format / breakpoint media variant. | `srcset`, `media`, `type` (`image/avif`, `image/webp`). | Evaluated sequentially from top to bottom; first match loads. |
| `<img>` | Image rendering engine. | `src`, `alt`, `width`, `height`, `loading`, `decoding`. | `alt=""` for decorative images; descriptive text for informative images. |
| `<video>` | Embedded video playback. | `controls`, `poster`, `preload`. | Fallback text and download link inside tag. |
| `<audio>` | Sound and voice playback. | `controls`, `preload`. | Accessible transcript link adjacent to player. |
| `<track>` | Timed text track for media. | `kind="captions|subtitles"`, `src="...vtt"`, `srclang`, `label`. | Native closed captioning rendered in media overlay. |
| `<iframe>` | Isolated embedded browsing context. | `title="..."`, `loading="lazy"`, `sandbox`. | **Never** omit `title`; screen readers require it to identify iframe content. |

---

## 7. Interactive & Top-Layer

The modern HTML specification provides declarative, browser-engine-backed top layer overlays and interactive toggles.

### `<dialog>` (Modal & Non-Modal Dialogs)
- **Modal Mode:** Trigger with `dialog.showModal()`. Traps focus, dims background with native `::backdrop`, locks scrolling, dismisses on `Escape`.
- **Top Layer:** Renders above all other elements regardless of `z-index` or parent `overflow: hidden`.
- **Dismissal:** Native `<form method="dialog">` allows buttons to close the dialog and pass `returnValue` without custom JS.

### `<details>` & `<summary>` (Disclosures & Accordions)
- **Built-in Keyboard Control:** Pressing `Space` or `Enter` on `<summary>` toggles visibility.
- **Exclusive Accordions:** Add matching `name="group-name"` across multiple `<details>` elements to automatically close others when one opens.
- **Find-In-Page:** Automatically opens when users search via `Ctrl+F` for text inside a closed summary.

### Popover API (`popover="auto|manual"`)
- **Non-Modal Overlays:** Tooltips, action menus, comboboxes, and hover cards.
- **Light-Dismiss:** `popover="auto"` automatically closes when clicking outside or pressing `Escape`.
- **Declarative Triggers:** Opened via `<button popovertarget="my-popover">` with zero JavaScript.

---

## 8. Global Attributes

Global attributes are valid on every HTML element and govern accessibility, keyboard interaction, and mobile device behaviors.

| Attribute | Valid Values | Behavior & Purpose | Anti-Pattern |
|---|---|---|---|
| `inert` | Boolean (`inert`) | Completely disables element and descendants from focus order, accessibility tree, and pointer events. | Manually writing scripts to apply `tabindex="-1"` and `aria-hidden` to background elements. |
| `popover` | `auto`, `manual` | Transforms element into a top-layer popover with light-dismiss. | Writing custom document click listeners to dismiss dropdown menus. |
| `hidden` | `""` (empty), `until-found` | `until-found` keeps content hidden visually while remaining searchable via browser `Ctrl+F`. | Using `display: none` for accordion content, completely hiding it from search. |
| `inputmode` | `numeric`, `decimal`, `tel`, `email`, `url`, `search` | Configures the virtual keyboard layout on touch devices. | Forcing users to manually toggle numeric keyboard view for credit cards or OTP codes. |
| `enterkeyhint`| `enter`, `done`, `go`, `next`, `previous`, `search`, `send` | Customizes the label/icon of the Enter key on mobile touch keyboards. | Ambiguous return key on mobile forms. |
| `tabindex` | `0`, `-1` (**never positive integers**) | `0` inserts element into sequential tab order; `-1` makes it focusable via script only. | Positive values (`tabindex="3"`) that hijack natural document tab order. |
| `lang` | BCP 47 language tag (`en-US`, `tr`, `fr`) | Declares language of element for screen readers and hyphenation. | Missing `lang` on multilingual quotes or translated blocks. |
| `dir` | `ltr`, `rtl`, `auto` | Directionality of text content. | Relying purely on CSS `direction: rtl` for bidirectional text. |
| `contenteditable`| `true`, `false`, `plaintext-only` | Enables rich text editing in the element. | Using unconstrained contenteditable divs instead of `<textarea>` for standard forms. |
| `autofocus` | Boolean | Directs focus to element upon page load. | Setting autofocus automatically without explicit user intent, disorienting screen readers. |

---

## 9. Obsolete & Anti-Patterns to Reject

Modern standards deprecate purely visual markup in favor of semantic HTML and CSS styling:

| Obsolete Element | Modern Semantic Replacement | Reason for Deprecation |
|---|---|---|
| `<center>` | CSS `margin-inline: auto` or `text-align: center` | Presentational; mixes layout with document structure. |
| `<font>` | CSS `font-family`, `font-size`, `color` | Hardcodes styling attributes directly into HTML. |
| `<b>` | `<strong>` for importance; CSS `font-weight: 700` | Lacks semantic urgency or importance in accessibility trees. |
| `<i>` | `<em>` for stress; CSS `font-style: italic` | Lacks vocal emphasis in speech synthesizers. |
| `<big>`, `<small>` (presentational) | CSS font sizing; semantic `<small>` for disclaimers only | Inconsistent cross-browser scaling. |
| `<strike>`, `<s>` | `<del>` for deleted text; CSS `text-decoration: line-through` | Lacks machine-readable edit tracking semantics. |
| `<marquee>`, `<blink>` | CSS keyframe animations (with `prefers-reduced-motion`) | Severe accessibility hazard; causes disorientation and seizures. |
| `<frame>`, `<frameset>` | Modern CSS grid layouts or standard responsive components | Destroys URL history, bookmarking, and accessibility trees. |

---

## 10. Related Rules & References

- Overview & Principles: [`references/semantic-html.md`](semantic-html.md)
- Native Overlays: [`rules/html-dialog-modal-native.md`](../rules/html-dialog-modal-native.md)
- Interactive Disclosures: [`rules/html-interactive-details-summary.md`](../rules/html-interactive-details-summary.md)
- Data Table Standards: [`rules/html-table-structure-semantics.md`](../rules/html-table-structure-semantics.md)
- Machine-Readable Timestamps: [`rules/html-time-datetime-attribute.md`](../rules/html-time-datetime-attribute.md)
- Responsive Picture & Media: [`rules/html-media-picture-responsive.md`](../rules/html-media-picture-responsive.md)
- Background Isolation: [`rules/html-inert-attribute.md`](../rules/html-inert-attribute.md)
- Landmarks & Headings: [`rules/html-sectioning-landmarks.md`](../rules/html-sectioning-landmarks.md)
- Advanced Forms & Controls: [`rules/html-forms-advanced-semantics.md`](../rules/html-forms-advanced-semantics.md)
- Top-Layer Popover API: [`rules/html-popover-api-native.md`](../rules/html-popover-api-native.md)
- Keyboard & Global Attributes: [`rules/html-global-attributes-keyboard-input.md`](../rules/html-global-attributes-keyboard-input.md)
- State Pseudo-Classes: [`rules/html-native-state-pseudo-classes.md`](../rules/html-native-state-pseudo-classes.md)
- Core Semantic Elements: [`rules/html-semantic-elements.md`](../rules/html-semantic-elements.md)
