---
title: Use Sectioning Landmarks and Hierarchical Headings for Document Architecture
impact: CRITICAL
impactDescription: Missing landmark elements or skipped heading levels break screen reader navigation and disorient users attempting to scan document structure.
tags: html, landmarks, headings, sectioning, accessibility, a11y, seo
---

# Use Sectioning Landmarks and Hierarchical Headings for Document Architecture

**Impact: CRITICAL (Landmarks and heading hierarchies are the primary navigation mode for screen reader users)**

Always structure HTML documents using native sectioning landmark elements: `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`, and the native `<search>` element. Never construct entire page layouts out of generic `<div>` containers.

Every web document must contain exactly one top-level `<main>` landmark representing the dominant content of the page. Do not nest `<main>` inside another sectioning element or repeat multiple `<main>` tags.

Headings (`<h1>` through `<h6>`) must strictly reflect document hierarchy without skipping levels (e.g. an `<h3>` must never appear directly inside an `<h1>` without an intermediate `<h2>`). Use `<hgroup>` when grouping a title with a subtitle or kicker.

## Bad Example

Non-semantic div soup with skipped heading levels and obsolete presentational tags:

```html
<!-- Inaccessible div soup: Screen reader navigation rotor finds zero landmarks -->
<div class="header">
  <div class="logo">Acme SaaS</div>
  <div class="nav-links">
    <a href="/features">Features</a>
  </div>
</div>

<div class="content-body">
  <!-- Top heading is an h1 -->
  <h1>Analytics Dashboard</h1>

  <div class="card">
    <!-- Skipped directly to h4 for visual sizing! -->
    <h4>Monthly Recurring Revenue</h4>
    <p>$48,200</p>
  </div>

  <div class="search-box">
    <!-- Fake search wrapper using generic div -->
    <input type="text" placeholder="Search accounts...">
  </div>
</div>

<div class="footer">
  <p>© 2026 Acme Corp</p>
</div>
```

## Good Example

Native HTML5 landmarks, un-skipped heading hierarchy, and modern `<search>` and `<hgroup>` elements:

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Analytics Dashboard | Acme SaaS</title>
</head>
<body>
  <!-- Banner landmark -->
  <header class="site-header">
    <a href="/" class="brand-logo" aria-label="Acme Home">
      <svg aria-hidden="true" width="32" height="32"><!-- Logo SVG --></svg>
      <span>Acme</span>
    </a>
    
    <!-- Primary navigation landmark -->
    <nav aria-label="Primary navigation">
      <ul>
        <li><a href="/dashboard" aria-current="page">Dashboard</a></li>
        <li><a href="/customers">Customers</a></li>
        <li><a href="/settings">Settings</a></li>
      </ul>
    </nav>

    <!-- Native search landmark (HTML5 standard) -->
    <search>
      <form action="/search" method="get">
        <label for="site-search" class="sr-only">Search accounts and metrics</label>
        <input type="search" id="site-search" name="q" placeholder="Search accounts...">
        <button type="submit">Search</button>
      </form>
    </search>
  </header>

  <!-- Single primary content landmark -->
  <main id="main-content">
    <header class="page-header">
      <hgroup>
        <h1>Analytics Dashboard</h1>
        <p class="subheading">Performance overview for Q4 2026</p>
      </hgroup>
    </header>

    <!-- Content sections with accessible names -->
    <section aria-labelledby="revenue-heading" class="metrics-section">
      <h2 id="revenue-heading">Revenue Breakdown</h2>
      
      <div class="cards-grid">
        <article class="metric-card">
          <h3>Monthly Recurring Revenue</h3>
          <p class="metric-value font-tabular">$48,200</p>
        </article>

        <article class="metric-card">
          <h3>Annual Run Rate</h3>
          <p class="metric-value font-tabular">$578,400</p>
        </article>
      </div>
    </section>

    <!-- Complementary landmark -->
    <aside aria-labelledby="activity-heading" class="recent-activity">
      <h2 id="activity-heading">Recent Audit Events</h2>
      <ul>
        <li>User Alice updated API credentials</li>
        <li>Billing webhook processed</li>
      </ul>
    </aside>
  </main>

  <!-- Contentinfo landmark -->
  <footer class="site-footer">
    <p>© 2026 Acme Corp. All rights reserved.</p>
  </footer>
</body>
</html>
```

## Why

- **Screen Reader Rotor & Landmark Navigation**: Blind and low-vision users utilize keyboard shortcuts (e.g. `D` in NVDA/JAWS) to jump directly between landmarks (`banner`, `navigation`, `main`, `complementary`, `contentinfo`, `search`).
- **Sequential Heading Outline**: Heading level skipping (`h1` → `h4`) confuses assistive technology users who rely on heading trees to assess document hierarchy.
- **Native Search Landmark**: `<search>` replaces obsolete `<div role="search">` containers, exposing a standardized search landmark natively.
- **Grouping Headings with `<hgroup>`**: Keeps decorative subtitles and category kickers structurally tied to their parent `<h1>`–`<h6>` without polluting heading outlines.
- **Search Engine Optimization**: Web crawlers heavily weight content enclosed in `<main>` and `<h1>` elements for search indexation and semantic snippet extraction.

## Related

- Reference: [`references/semantic-html.md`](../references/semantic-html.md)
- Reference: [`references/accessibility.md`](../references/accessibility.md)
- Rule: [`rules/html-semantic-elements.md`](html-semantic-elements.md)
- Rule: [`rules/ux-copy-action-verbs.md`](ux-copy-action-verbs.md)
