---
title: Use Native Dialog Element for Modal and Non-Modal Overlays
impact: CRITICAL
impactDescription: Custom div modals lack built-in focus trapping, Esc key dismissal, top-layer stacking, and return-of-focus to the trigger.
tags: html, dialog, modal, accessibility, keyboard, top-layer
---

# Use Native Dialog Element for Modal and Non-Modal Overlays

**Impact: CRITICAL (Severe accessibility and focus-trapping defects in custom modal implementations)**

Always use the native HTML5 `<dialog>` element for modal dialogs, confirmation prompts, and user intervention flows. Trigger modal dialogs with the native JavaScript API `dialog.showModal()` rather than `dialog.show()` or custom CSS visibility toggles.

Native `<dialog>` elements automatically render in the browser's Top Layer (above all CSS `z-index` stacking contexts), trap keyboard tab navigation inside the dialog, close upon pressing the `Escape` key, and automatically return keyboard focus to the opening trigger button when closed.

## Bad Example

Custom `<div>` overlay relying on manual backdrop management, fragile focus trap scripts, and complex z-index overrides:

```html
<!-- Inaccessible div modal: focus escapes into background, Esc key fails, no top-layer rendering -->
<div id="custom-modal" class="modal-overlay" style="z-index: 9999; display: none;">
  <div class="modal-card" role="dialog" aria-modal="true">
    <h3>Delete Project</h3>
    <p>Are you sure you want to permanently delete this project?</p>
    <div class="modal-actions">
      <button onclick="closeModal()">Cancel</button>
      <button class="btn-danger" onclick="confirmDelete()">Delete</button>
    </div>
  </div>
</div>

<script>
  // Requires dozens of lines of error-prone JavaScript to trap Tab key,
  // listen for Escape key, disable body scroll, and restore trigger focus.
</script>
```

## Good Example

Native `<dialog>` element opened via `.showModal()` with semantic `<form method="dialog">` buttons:

```html
<!-- Trigger button -->
<button type="button" class="btn-danger" id="open-delete-dialog">
  Delete Project
</button>

<!-- Native modal dialog -->
<dialog id="delete-dialog" aria-labelledby="dialog-title" aria-describedby="dialog-desc">
  <form method="dialog" class="dialog-content">
    <h3 id="dialog-title">Delete Project</h3>
    <p id="dialog-desc">
      Are you sure you want to permanently delete this project? This action cannot be undone.
    </p>

    <footer class="dialog-actions">
      <!-- value="cancel" closes the dialog and sets dialog.returnValue to 'cancel' -->
      <button type="submit" value="cancel" class="btn-secondary">
        Cancel
      </button>
      <!-- value="confirm" closes the dialog and passes 'confirm' to the close event -->
      <button type="submit" value="confirm" class="btn-danger">
        Delete permanently
      </button>
    </footer>
  </form>
</dialog>

<script>
  const dialog = document.getElementById('delete-dialog');
  const openBtn = document.getElementById('open-delete-dialog');

  openBtn.addEventListener('click', () => {
    // Opens as a modal with automatic focus trap, backdrop, and top-layer placement
    dialog.showModal();
  });

  dialog.addEventListener('close', () => {
    if (dialog.returnValue === 'confirm') {
      executeProjectDeletion();
    }
    // Keyboard focus automatically returns to openBtn upon dismissal!
  });
</script>
```

```css
/* Style native backdrop cleanly without z-index hacks */
dialog {
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: var(--space-6);
  max-width: 32rem;
  width: 90vw;
  box-shadow: var(--shadow-high);
}

dialog::backdrop {
  background-color: oklch(0 0 0 / 0.55);
  backdrop-filter: blur(4px);
}
```

## Why

- **Automatic Focus Trapping**: `dialog.showModal()` restricts keyboard `Tab` cycles strictly within the dialog without manual keydown listeners.
- **Top Layer Placement**: Renders directly in the browser's top layer, completely bypassing `overflow: hidden` parent containers and CSS `z-index` stacking wars.
- **Built-in Keyboard Dismissal**: Pressing the `Escape` key automatically dismisses the modal and fires the `cancel` and `close` events.
- **Focus Restoration**: When the dialog closes, the browser automatically restores focus to the element that invoked `.showModal()`.
- **Form Method Dialog**: `<form method="dialog">` allows action buttons to dismiss the dialog without requiring custom JavaScript `.preventDefault()` calls.

## Related

- Reference: [`references/semantic-html.md`](../references/semantic-html.md)
- Reference: [`references/accessibility.md`](../references/accessibility.md)
- Rule: [`rules/html-inert-attribute.md`](html-inert-attribute.md)
- Rule: [`rules/html-popover-api-native.md`](html-popover-api-native.md)
