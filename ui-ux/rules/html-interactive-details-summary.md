---
title: Use Native Details and Summary for Expandable Disclosures and Accordions
impact: HIGH
impactDescription: Custom accordion widgets often lack Space/Enter keyboard support, proper ARIA expansion state synchronization, and native browser find-in-page integration.
tags: html, interactive, details, summary, accordion, accessibility
---

# Use Native Details and Summary for Expandable Disclosures and Accordions

**Impact: HIGH (Improper custom accordion widgets break keyboard navigation and assistive technology states)**

Always use the native HTML5 `<details>` and `<summary>` elements to create collapsible disclosure widgets, FAQ sections, and accordion groups. Do not reinvent accordions with generic `<div>` containers, custom click handlers, and manual `aria-expanded` attributes unless a strict framework requirement prevents native element usage.

Modern HTML supports the `name` attribute on `<details>`, which creates native exclusive accordion groups (only one item open at a time) without requiring a single line of JavaScript. Furthermore, `<details>` elements integrate seamlessly with browser find-in-page (`Ctrl+F`), automatically expanding when search matches occur inside closed summaries.

## Bad Example

Custom `<div>` accordion relying on click listeners, missing keyboard triggers, and manually synchronized ARIA attributes:

```html
<!-- Inaccessible div accordion: no Space/Enter keyboard support, fragile ARIA syncing -->
<div class="faq-item">
  <div class="faq-header" onclick="toggleFaq(this)" role="button" tabindex="0">
    <span>What payment methods do you accept?</span>
    <span class="chevron">▼</span>
  </div>
  <div class="faq-body" style="display: none;">
    <p>We accept Visa, Mastercard, American Express, and PayPal.</p>
  </div>
</div>

<script>
  function toggleFaq(el) {
    const body = el.nextElementSibling;
    const isHidden = body.style.display === 'none';
    body.style.display = isHidden ? 'block' : 'none';
    // Developer forgot to update aria-expanded, forgot Space key handler,
    // and content remains invisible to browser search (Ctrl+F).
  }
</script>
```

## Good Example

Native `<details>` with `<summary>`, styled with the native `:open` pseudo-class and grouped via the `name` attribute:

```html
<!-- Native exclusive accordion group: zero JS required -->
<div class="accordion-group">
  <details name="billing-faq" class="disclosure-card" open>
    <summary class="disclosure-header">
      <span class="disclosure-title">What payment methods do you accept?</span>
      <span class="disclosure-icon" aria-hidden="true"></span>
    </summary>
    <div class="disclosure-content">
      <p>We accept Visa, Mastercard, American Express, and PayPal.</p>
    </div>
  </details>

  <details name="billing-faq" class="disclosure-card">
    <summary class="disclosure-header">
      <span class="disclosure-title">Can I cancel my subscription at any time?</span>
      <span class="disclosure-icon" aria-hidden="true"></span>
    </summary>
    <div class="disclosure-content">
      <p>Yes. You can cancel your subscription directly from your billing settings page.</p>
    </div>
  </details>
</div>
```

```css
/* Clean styling using native semantic pseudo-class */
.disclosure-card {
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  margin-bottom: var(--space-3);
  overflow: hidden;
}

.disclosure-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: var(--space-4);
  font-weight: 600;
  cursor: pointer;
  list-style: none; /* Removes default triangle marker */
  user-select: none;
}

/* Remove default marker in WebKit */
.disclosure-header::-webkit-details-marker {
  display: none;
}

.disclosure-header:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: -2px;
}

.disclosure-icon::after {
  content: "›";
  font-size: 1.25rem;
  display: inline-block;
  transition: transform 0.2s ease;
}

/* Smooth indicator rotation using native :open state */
.disclosure-card[open] .disclosure-icon::after {
  transform: rotate(90deg);
}

.disclosure-content {
  padding: 0 var(--space-4) var(--space-4);
  color: var(--color-text-secondary);
}
```

## Why

- **Native Keyboard Support**: Pressing `Space` or `Enter` on `<summary>` toggles visibility without custom event listeners.
- **Find-In-Page Integration**: Browsers automatically expand closed `<details>` elements when a user searches for text (`Ctrl+F` / `Cmd+F`) on the page.
- **Zero-JS Accordion Groups**: The modern standard `name="..."` attribute on `<details>` natively enforces single-open accordion behavior.
- **Screen Reader Parity**: Screen readers announce "disclosure triangle", collapsed/expanded state, and item count out of the box.
- **Native State Styling**: Directly styleable via `details[open]` or the `:open` pseudo-class without custom classes like `.is-active`.

## Related

- Reference: [`references/semantic-html.md`](../references/semantic-html.md)
- Reference: [`references/components-and-patterns.md`](../references/components-and-patterns.md)
- Rule: [`rules/html-native-state-pseudo-classes.md`](html-native-state-pseudo-classes.md)
- Rule: [`rules/html-dialog-modal-native.md`](html-dialog-modal-native.md)
