---
title: Provide Standard Form Autocomplete Attributes
impact: HIGH
impactDescription: Missing autocomplete attributes slow down checkout/login flows and violate WCAG 2.1 SC 1.3.5 (Identify Input Purpose).
tags: forms, autocomplete, usability, autofill, a11y
---

# Provide Standard Form Autocomplete Attributes

Use appropriate standard HTML `autocomplete` tokens for fields whose purpose is known, such as name, email, address, current or new password, and one-time code. Correct tokens help browsers and password managers offer autofill; WCAG 1.3.5 applies to the input purposes listed by that criterion, not every field.

## Bad Example

```html
<!-- Browser and password managers cannot reliably identify input purpose -->
<input type="text" name="usr_name" />
<input type="password" name="pwd" />
<input type="text" name="zip" />
```

## Good Example

```html
<!-- Conforms to WCAG 2.1 SC 1.3.5 with standardized autofill tokens -->
<input type="text" name="name" autocomplete="name" required />
<input type="email" name="email" autocomplete="email" required />
<input type="password" name="password" autocomplete="current-password" required />
<input type="text" name="postal-code" autocomplete="postal-code" inputmode="numeric" />
<input type="text" name="two-factor" autocomplete="one-time-code" inputmode="numeric" />
```
