---
title: Optimize Mobile Input and Document Ergonomics with Global Attributes
impact: HIGH
impactDescription: Missing inputmode and enterkeyhint creates friction on mobile keyboards, while positive tabindex breaks predictable tab order.
tags: html, global-attributes, inputmode, enterkeyhint, tabindex, ergonomics
---

# Optimize Mobile Input and Document Ergonomics with Global Attributes

**Impact: HIGH (Dramatically streamlines mobile data entry, protects keyboard order, and supports in-page search)**

Leverage HTML global attributes to enhance mobile ergonomics, document accessibility, and rendering efficiency:

1. **`inputmode`**: Declare `numeric`, `decimal`, `tel`, `email`, `url`, or `search` on text inputs to invoke the specialized virtual keyboard layout on touch devices without triggering unwanted browser number spinners.
2. **`enterkeyhint`**: Configure the mobile virtual return key action (`enterkeyhint="go|done|next|search|send"`) to give users unmistakable visual clarity on what tapping the keyboard action button will trigger.
3. **`hidden="until-found"`**: For collapsible content panels, use `hidden="until-found"` instead of `hidden` or `display: none`. This allows browser native find-in-page (`Ctrl+F`) to find matching text inside the hidden block and automatically reveal it by removing the attribute.
4. **`tabindex`**: Never declare positive integer values (`tabindex="1"`, `tabindex="5"`). Use `tabindex="0"` to insert an element into natural sequential focus order, and `tabindex="-1"` for programmatically focusable elements.

## Bad Example

Missing virtual keyboard hints, positive tabindex hijacking document sequence, and standard hidden blocking search:

```html
<!-- Friction: Opens full alphanumeric keyboard with tiny numbers on touch screens -->
<label for="credit-card">Card Number</label>
<input type="text" id="credit-card" name="card_num">

<!-- Anti-pattern: Positive tabindex hijacks natural document order, creating chaos for keyboard users -->
<input type="text" tabindex="1">
<button tabindex="2">Proceed</button>

<!-- Hidden panel completely invisible to Ctrl+F find-in-page -->
<div id="terms-content" hidden>
  <p>Refund policy details...</p>
</div>
```

## Good Example

Ergonomic `inputmode`, action-oriented `enterkeyhint`, natural focus order, and searchable `hidden="until-found"`:

```html
<!-- Tailored mobile keyboard layout: 10-digit numeric pad with 'Next' enter action -->
<div class="form-group">
  <label for="card-number">Card Number</label>
  <input 
    type="text" 
    id="card-number" 
    name="card_number" 
    inputmode="numeric" 
    pattern="[0-9\s]{13,19}" 
    enterkeyhint="next" 
    autocomplete="cc-number" 
    placeholder="4532 •••• •••• 8910" 
  />
</div>

<!-- Monetary amount with localized decimal keyboard and 'Done' action -->
<div class="form-group">
  <label for="donation-amount">Transfer Amount ($)</label>
  <input 
    type="text" 
    id="donation-amount" 
    name="amount" 
    inputmode="decimal" 
    enterkeyhint="done" 
    placeholder="25.00" 
  />
</div>

<!-- Search query with specialized mobile keyboard search button -->
<div class="form-group">
  <label for="query-input">Search Documentation</label>
  <input 
    type="search" 
    id="query-input" 
    name="q" 
    inputmode="search" 
    enterkeyhint="search" 
    placeholder="Search components..." 
  />
</div>

<!-- Collapsible panel that automatically reveals itself if user searches for 'Refund' via Ctrl+F -->
<div id="refund-details" hidden="until-found" class="expandable-panel">
  <h3>Refund Guarantee</h3>
  <p>You can request a full refund within 30 days of initial purchase.</p>
</div>
```

```javascript
// Listen to beforematch event when hidden="until-found" is revealed by browser search
const refundPanel = document.getElementById('refund-details');
refundPanel.addEventListener('beforematch', () => {
  // Synchronize UI state (e.g. flip accordion icon)
  updateAccordionState(true);
});
```

## Mobile Virtual Keyboard Modes (`inputmode`)

| `inputmode` Value | Virtual Keyboard Layout | Recommended Use Case |
|---|---|---|
| `numeric` | Full 0-9 number keypad (no punctuation) | Credit cards, OTP 2FA codes, PINs, zip codes |
| `decimal` | Numeric keypad with decimal separator (`.` or `,`) | Currency amounts, weights, coordinates |
| `tel` | Phone dial pad with `*` and `#` | Telephone numbers, SMS verification numbers |
| `email` | Alphanumeric with dedicated `@` and `.com` keys | Email login, newsletter signups |
| `url` | Alphanumeric with `/` and `.com` keys | Website URLs, domain entry |
| `search` | Alphanumeric with prominent "Search" action key | Global search bars, filter inputs |

## Why

- **Eliminates Mobile Data Entry Friction**: Mobile users avoid manually switching between alphabet and numeric keyboard views.
- **Action Clarity**: `enterkeyhint` indicates what tapping the software keyboard return key will do (`Search`, `Go`, `Next`, or `Send`).
- **Unbroken Document Flow**: Avoiding positive `tabindex` prevents bizarre focus jumps that confuse keyboard users.
- **Find-In-Page Discoverability**: `hidden="until-found"` exposes hidden accordion and tab content to native browser search without cluttering the initial viewport.

## Related

- Reference: [`references/semantic-html.md`](../references/semantic-html.md)
- Reference: [`references/form-ux-and-patterns.md`](../references/form-ux-and-patterns.md)
- Rule: [`rules/form-autocomplete-attributes.md`](form-autocomplete-attributes.md)
- Rule: [`rules/a11y-focus-visible.md`](a11y-focus-visible.md)
