---
title: Provide Machine-Readable Timestamps with Time and Datetime Attribute
impact: MEDIUM
impactDescription: Relative timestamps (e.g. '3 hours ago') without datetime attributes confuse screen readers, prevent calendar extraction, and degrade search engine indexing.
tags: html, time, datetime, semantics, microdata, i18n
---

# Provide Machine-Readable Timestamps with Time and Datetime Attribute

**Impact: MEDIUM (Ambiguous relative dates hinder accessibility tools, calendar integrations, and search parsers)**

Always wrap temporal information—publication dates, event schedules, transaction timestamps, deadlines, and durations—in the semantic HTML5 `<time>` element with a valid, machine-readable `datetime` attribute adhering to ISO 8601 or RFC 3339 formats.

While human readers benefit from friendly relative copy such as *"Yesterday"*, *"3 hours ago"*, or *"Next Tuesday at 4 PM"*, user agents, screen readers, translation engines, and web crawlers require an unambiguous, standardized timestamp in UTC or with an explicit timezone offset.

## Bad Example

Ambiguous date rendered as plain text in a generic `<span>` without machine-readable metadata:

```html
<!-- Ambiguous text: Screen readers cannot parse timezone; search bots cannot extract publish date -->
<div class="article-meta">
  <span class="author">Elena Vance</span> · 
  <span class="date">3 days ago</span>
</div>

<!-- Ambiguous meeting time: Calendar scrapers cannot parse relative weekday -->
<p>Project standup is scheduled for next Thursday at 2:30.</p>
```

## Good Example

Semantic `<time>` elements with ISO 8601 timestamps, explicit timezones, and duration strings:

```html
<!-- Publication date with full ISO 8601 UTC timestamp -->
<div class="article-meta">
  <span class="author">Elena Vance</span> · 
  <time datetime="2026-10-25T14:30:00Z" class="timestamp">
    3 days ago
  </time>
</div>

<!-- Scheduled event with local time and explicit timezone offset -->
<p>
  Next release review: 
  <time datetime="2026-10-29T14:30:00-04:00">
    Thursday, Oct 29 at 2:30 PM EDT
  </time>
</p>

<!-- Duration representation using ISO 8601 duration format -->
<p>
  Estimated reading time: 
  <time datetime="PT8M">8 minutes</time>
</p>

<!-- Specific year-month representation for invoices and archiving -->
<p>
  Billing period: 
  <time datetime="2026-10">October 2026</time>
</p>
```

## Valid Datetime Formats (MDN Standards)

| Use Case | Format Pattern | Example |
|---|---|---|
| **Full Date & Time (UTC)** | `YYYY-MM-DDTHH:MM:SSZ` | `2026-10-25T17:00:00Z` |
| **Date with Timezone Offset**| `YYYY-MM-DDTHH:MM:SS±HH:MM`| `2026-10-25T20:00:00+03:00` |
| **Year-Month-Day only** | `YYYY-MM-DD` | `2026-10-25` |
| **Year and Month only** | `YYYY-MM` | `2026-10` |
| **Time only (24h clock)** | `HH:MM:SS` or `HH:MM` | `14:30:00` |
| **Duration (ISO 8601)** | `P[n]Y[n]M[n]DT[n]H[n]M[n]S` | `PT2H30M` (2h 30m), `P3D` (3 days) |

## Why

- **Screen Reader Clarity**: Assistive software can announce unambiguous absolute dates or expand relative expressions to the user's localized timezone.
- **Search Engine Rich Snippets**: Search engine indexers consume `<time datetime="...">` directly for article carousels, event schemas, and freshness rankings.
- **Operating System & Browser Integrations**: Modern mobile and desktop browsers enable users to click or tap `<time>` tags to add events directly to system calendars.
- **Standardized Internationalization**: Translators and i18n formatters can inspect the `datetime` attribute and format the display string dynamically for any locale.

## Related

- Reference: [`references/semantic-html.md`](../references/semantic-html.md)
- Reference: [`references/real-content-and-affordances.md`](../references/real-content-and-affordances.md)
- Rule: [`rules/html-semantic-elements.md`](html-semantic-elements.md)
- Rule: [`rules/type-tabular-numerals.md`](type-tabular-numerals.md)
