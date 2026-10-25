# Form UX & Input Ergonomics

**Impact:** CRITICAL · **Prefix:** `form-` · **Conversion, Usability & Data Integrity**

Forms are the most interaction-heavy touchpoints in web applications. Clumsy inputs, unexpected keyboard jumps, missed autocomplete attributes, and unhelpful error timing cause high drop-off rates and accessibility failures.

## Load When

- Designing or reviewing forms, inputs, selects, toggles, and multi-step wizards
- Implementing form validation and accessible error handling
- Optimizing mobile input ergonomics (virtual keyboards, auto-zoom prevention)
- Supporting browser autofill and password managers via standard autocomplete tokens
- Preventing duplicate API submissions and handling asynchronous mutations

## Rules

| Rule | Summary |
|------|---------|
| [`form-autocomplete-attributes`](../rules/form-autocomplete-attributes.md) | Use relevant autocomplete tokens for autofill and WCAG input-purpose requirements |
| [`a11y-form-labels-errors`](../rules/a11y-form-labels-errors.md) | Explicit `<label>` binding; inline errors linked via `aria-describedby` and `aria-invalid` |
| [`a11y-ios-input-zoom`](../rules/a11y-ios-input-zoom.md) | Enforce minimum 16px font size on inputs to prevent mobile browser auto-zoom |
| [`ux-copy-action-verbs`](../rules/ux-copy-action-verbs.md) | Use specific, action-oriented verbs (`Save changes`) over generic labels (`Submit`) |

---

## Form Field Anatomy

Every robust form field consists of four interconnected parts:
1. **Persistent Label**: A clear `<label for="id">`; placeholder text can supplement but must never replace the label.
2. **Input Control**: Configured with the correct `type`, `inputmode`, and `autocomplete`.
3. **Helper / Hint Text**: Instructions placed between the label and input or below the input, linked via `aria-describedby`.
4. **Validation Message**: Linked with `aria-describedby` and flagged with `aria-invalid="true"` when invalid.

```html
<div class="form-group">
  <label for="billing-phone" class="form-label">Phone Number</label>
  <p id="phone-hint" class="form-hint">Used strictly for delivery status SMS updates.</p>
  <input
    type="tel"
    id="billing-phone"
    name="phone"
    class="form-input"
    autocomplete="tel"
    inputmode="tel"
    aria-describedby="phone-hint phone-error"
    aria-invalid="false"
  />
  <p id="phone-error" class="form-error" role="alert" hidden>
    Please enter a valid phone number including area code.
  </p>
</div>
```

---

## Mobile Virtual Keyboards: `type` and `inputmode`

Trigger the optimal mobile software keyboard to minimize friction:

| Input Intent | HTML `type` | `inputmode` | Virtual Keyboard Triggered |
|---|---|---|---|
| Email address | `type="email"` | `inputmode="email"` | QWERTY with `@` and `.` keys |
| Telephone number | `type="tel"` | `inputmode="tel"` | Numeric dial pad with `+`, `*`, `#` |
| Credit card / 2FA OTP | `type="text"` | `inputmode="numeric"` | Clean 0–9 numeric keypad |
| Decimal number / Price | `type="text"` | `inputmode="decimal"` | 0–9 keypad with decimal separator |
| Website URL | `type="url"` | `inputmode="url"` | QWERTY with `.com`, `/`, `.` keys |
| Search queries | `type="search"` | `inputmode="search"` | Enter key labeled "Search" |

### Prevent Mobile Web Browser Auto-Zoom
Mobile browsers (notably WebKit / mobile Safari) automatically zoom the viewport when an input with a font size smaller than 16px is focused. Enforce 16px minimum:

```css
input,
select,
textarea {
  font-size: max(1rem, 16px);
}
```

---

## Validation Timing Guidelines

- **Do not announce errors while the user is actively typing**: Premature errors cause anxiety and distract the user before they finish entering their data.
- **Validate on blur**: Check field validity when the user leaves the input to move to the next field.
- **Clear errors on fix**: Once a field is marked invalid, clear or update the error message immediately as the user types the fix.
- **Submit validation summary**: If the user submits with errors, focus the first invalid input and display a high-level summary at the top of the form with anchor links to the offending fields.

---

## Double-Submission Prevention

Never allow a user to trigger duplicate transactions by double-clicking a submit button:

```javascript
async function handleSubmit(event) {
  event.preventDefault();
  const submitBtn = event.target.querySelector('button[type="submit"]');

  if (submitBtn.disabled) return;

  try {
    submitBtn.disabled = true;
    submitBtn.setAttribute('aria-busy', 'true');
    await submitFormPayload();
  } catch (error) {
    submitBtn.disabled = false;
    submitBtn.removeAttribute('aria-busy');
    showFormError(error.message);
  }
}
```

---

## Fieldsets and Radio/Checkbox Groups

Group related options using semantic `<fieldset>` and `<legend>` so assistive devices announce the question context for each option:

```html
<fieldset class="radio-group">
  <legend class="group-legend">Preferred Contact Method</legend>
  <div class="option-row">
    <input type="radio" id="contact-email" name="contact-method" value="email" checked />
    <label for="contact-email">Email</label>
  </div>
  <div class="option-row">
    <input type="radio" id="contact-phone" name="contact-method" value="phone" />
    <label for="contact-phone">Phone</label>
  </div>
</fieldset>
```
