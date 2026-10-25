---
title: Use Smart Curly Punctuation
impact: MEDIUM
impactDescription: Straight typewriter quotes and double hyphens degrade typographic professionalism and editorial credibility.
tags: typography, punctuation, entities, formatting, micro-typography
---

# Use Smart Curly Punctuation

For editorial customer-facing prose, follow the product's language and typography conventions. Curly quotes, typographic apostrophes, en/em dashes, and ellipses can improve polished prose when they match the locale. Do not mechanically rewrite code, identifiers, user-entered text, or content where straight punctuation is conventional.

## Bad Example

```html
<!-- Typewriter quotes and dumb dashes look unrefined -->
<p>He said, "Don't touch that dial" -- before walking away...</p>
<p>Store hours: 9am - 5pm</p>
```

## Good Example

```html
<!-- Typographically polished with curly quotes, smart apostrophe, em dash, and en dash -->
<p>He said, “Don’t touch that dial”—before walking away…</p>
<p>Store hours: 9am–5pm (en-dash for numeric ranges)</p>

<!-- Or using standard HTML entities -->
<p>He said, &ldquo;Don&rsquo;t touch that dial&rdquo;&mdash;before walking away&hellip;</p>
```
