---
title: Rule Title Here
impact: CRITICAL | HIGH | MEDIUM
impactDescription: One-sentence explanation of why this rule is essential for web UI/UX, accessibility, or performance.
tags: category-tag, subtopic-tag, web-standards
---

# Rule Title Here

**Impact: CRITICAL | HIGH | MEDIUM (Brief summary of severity)**

Provide a concise, practical explanation of the rule, why it matters in modern web UI/UX, and how browser-native behavior or WCAG standards relate to it.

## Bad Example

Demonstrate the common anti-pattern, inaccessible hack, or poor UX practice:

```html
<!-- Inaccessible or problematic implementation -->
<div class="custom-widget" onclick="handleAction()">
  Action
</div>
```

## Good Example

Demonstrate the clean, semantic, accessible, and performant implementation using web standards:

```html
<!-- Accessible, semantic, standards-compliant implementation -->
<button type="button" class="btn-primary" onclick="handleAction()">
  Action
</button>
```

## Why

- **Accessibility**: Built-in keyboard accessibility, screen reader role announcement, and native focus management.
- **Reliability & Maintenance**: Eliminates fragile JavaScript event listeners and custom ARIA synchronization.
- **Performance**: Browser C++ engine handles layout, rendering, and event dispatch without script overhead.
- **User Experience**: Familiar platform behaviors (Esc key dismissal, native copy-paste, touch gestures) work out of the box.

## Related

- Reference: [`references/semantic-html.md`](../references/semantic-html.md)
- Reference: [`references/accessibility.md`](../references/accessibility.md)
