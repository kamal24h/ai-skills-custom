# UX Copywriting, Clarity & Content Hierarchy

**Impact:** CRITICAL · **Prefix:** `ux-copy-` · **Interface Language & Human-Centered Microcopy**

Interface text is a core design material. Vague labels, ambiguous verbs, silent errors, and internal jargon cause user friction and abandonment. Good UX copy preserves meaning, sets a predictable hierarchy, and provides actionable next steps.

## Load When

- Writing or reviewing button labels, dialog prompts, and form field helper text
- Designing error messages, warning alerts, and form validation feedback
- Implementing empty states, 404 pages, and onboarding walkthroughs
- Crafting confirmation dialogs for destructive actions (delete, reset, cancel)
- Auditing microcopy for clarity, tone, and internationalization readiness

## Rules

| Rule | Summary |
|------|---------|
| [`ux-copy-action-verbs`](../rules/ux-copy-action-verbs.md) | Use specific, action-oriented verbs (`Publish draft`, `Delete project`) over vague labels (`Submit`, `OK`, `Yes`) |

## Message Hierarchy Blueprint

Every user-facing message, notification, or error should follow a three-part structural sequence:

```
┌────────────────────────────────────────────────────────┐
│ 1. Problem or System Status (What happened?)          │
│ Plain language; state the facts without jargon.        │
├────────────────────────────────────────────────────────┤
│ 2. Context or Consequence (Why does it matter?)       │
│ Explain the impact on user data or workflow.           │
├────────────────────────────────────────────────────────┤
│ 3. Next Action / Recovery (What can the user do now?) │
│ Provide an immediate, actionable step or link.         │
└────────────────────────────────────────────────────────┘
```

### Example: Error Message Construction

- ❌ **Poor (Opaque & Blaming)**: `Error 500: Invalid payload parameters provided.`
- ❌ **Vague**: `An error occurred. Please try again later.`
- ✅ **Human-Centered & Actionable**: 
  > **Heading**: Couldn't save profile changes.  
  > **Body**: Your network connection dropped before the changes could be saved.  
  > **Action**: [Retry Save] or [Download copy of changes].

---

## Control Labels: Action-Oriented Verbs

Buttons and action triggers must declare their precise outcome. Users scan labels without reading surrounding body paragraphs.

| Context | Vague / Weak Label (Avoid) | Action-Oriented Standard (Prefer) |
|---|---|---|
| Form submission | `Submit`, `Send`, `Done` | `Create account`, `Send inquiry`, `Save changes` |
| Destructive action | `OK`, `Yes`, `Confirm` | `Delete workspace`, `Discard changes`, `Revoke access` |
| Modal dismissal | `Cancel` (when saving) | `Keep editing`, `Stay on page` |
| Navigation | `Click here`, `More` | `View pricing plans`, `Explore documentation` |
| Secondary action | `Dismiss` | `Remind me tomorrow`, `Don't show again` |

---

## Destructive Confirmation Dialogs

Destructive actions (permanently removing projects, deleting accounts, dropping data) require explicit consequences and unambiguous confirmations:

```html
<dialog id="delete-confirm" aria-labelledby="dialog-title" aria-describedby="dialog-desc">
  <div class="dialog-content">
    <h2 id="dialog-title">Delete "Marketing Q3" Workspace?</h2>
    <p id="dialog-desc">
      All 24 team members will immediately lose access, and 142 linked documents 
      will be permanently erased. This action cannot be undone.
    </p>
    <div class="dialog-actions">
      <button type="button" class="btn-secondary" data-dismiss>Keep Workspace</button>
      <button type="button" class="btn-danger">Permanently Delete Workspace</button>
    </div>
  </div>
</dialog>
```

**Key Guidelines:**
- Name the exact entity being destroyed (e.g., `Delete "Marketing Q3"` instead of `Delete item`).
- State the consequence explicitly before asking for confirmation.
- The confirm button should pair with the destructive verb (`Delete Workspace`), not generic `Yes` or `OK`.

---

## Purposeful Empty States

An empty state should never be a dead end. Treat it as an invitation to begin:

```
┌────────────────────────────────────────────────────────┐
│ [Illustrated or Semantic Icon]                         │
│                                                        │
│ No projects found in this workspace                    │
│ Projects help you organize team tasks, files, and      │
│ milestones in one central board.                       │
│                                                        │
│ [ + Create Your First Project ]                        │
│ [ Import from Trello / CSV ]                           │
└────────────────────────────────────────────────────────┘
```

1. **State the fact**: "No projects found."
2. **Explain the value**: What does this section do when populated?
3. **Primary CTA**: A high-contrast button to create the first item.
4. **Alternative path**: Import existing data or read a guide if creation requires preparation.

---

## Tone and Stress Context

- **High Stress (Errors, payments, data loss)**: Direct, calm, objective. Eliminate humor, exclamation marks, or forced levity.
- **Normal Operations (Settings, forms, filters)**: Concise, efficient, unobtrusive.
- **Onboarding & Success**: Encouraging and focused on the immediate next milestone.
