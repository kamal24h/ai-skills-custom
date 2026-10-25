---
title: Use Specific, Action-Oriented Verbs for Interactive Controls
impact: HIGH
impactDescription: Vague labels like 'Submit', 'OK', or 'Yes' force users to re-read surrounding context and increase anxiety during destructive or consequential actions.
tags: copy, ux, accessibility, microcopy, forms, buttons
---

# Use Specific, Action-Oriented Verbs for Interactive Controls

Buttons and links should clearly describe the exact operation they trigger without requiring the user to decipher the surrounding paragraph. Replace generic placeholder words like "Submit", "OK", "Yes", or "Click Here" with precise `[Verb] + [Noun]` phrases.

## Bad Example

Vague, ambiguous button and modal action labels:

```html
<!-- ❌ Generic form submission -->
<button type="submit">Submit</button>

<!-- ❌ Ambiguous confirmation dialog -->
<div class="modal">
  <p>Are you sure you want to delete this repository?</p>
  <button type="button">No</button>
  <button type="button">Yes</button>
</div>
```

## Good Example

Explicit, action-declaring labels:

```html
<!-- ✅ Exact outcome declared upfront -->
<button type="submit">Create Production Workspace</button>

<!-- ✅ Unambiguous confirmation with consequences stated -->
<div class="modal">
  <h2>Delete "Payment Gateway" Repository?</h2>
  <p>All 42 active deployment keys and pipeline configurations will be permanently removed.</p>
  <button type="button">Keep Repository</button>
  <button type="button" class="btn-danger">Permanently Delete Repository</button>
</div>
```
