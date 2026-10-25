---
title: Bind Units and Numbers with Non-Breaking Spaces
impact: MEDIUM
impactDescription: Orphaned units wrapped onto a new line (e.g., "100" at end of line and "km/h" at start of next) degrade reading rhythm.
tags: typography, punctuation, entities, non-breaking-space, polish
---

# Bind Units and Numbers with Non-Breaking Spaces

Where a line break between a number and its unit would be confusing, use a non-breaking space (`&nbsp;` in HTML or Unicode `\u00A0` in text), for example `10&nbsp;MB` or `5&nbsp;min`. Format currency and numbers according to the user's locale; don't manually bind a currency symbol or code in ways that conflict with locale formatting. Use non-breaking spaces selectively so narrow layouts can still reflow.

## Bad Example

```html
<!-- May wrap as "100" at the end of line 1 and "km/h" at the start of line 2 -->
<p>Top speed reached was 100 km/h in under 4 seconds.</p>
<p>Storage capacity: 256 GB available.</p>
```

## Good Example

```html
<!-- Number and unit remain bound as a single cohesive reading block -->
<p>Top speed reached was 100&nbsp;km/h in under 4&nbsp;seconds.</p>
<p>Storage capacity: 256&nbsp;GB available.</p>
```
