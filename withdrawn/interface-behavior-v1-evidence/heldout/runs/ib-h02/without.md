**What's going on:** the confirmations are inverted relative to risk. The app asks permission for safe actions and stays silent on dangerous ones.

| Action | Risk | Current behavior |
|---|---|---|
| Change category | Low, and fixable if undo existed | Confirm dialog |
| Mark reconciled | Low to medium, routine and repeated hundreds of times | Confirm dialog |
| Delete draft | Destructive, no recovery | Confirm dialog, then a "deleted" dialog |
| Void emailed invoice | High, because it has external consequences (the client already has it) | Nothing |
| Edit and navigate away | Medium | Silent save, no feedback |
| Undo | n/a | Doesn't exist |

**Why it's tiring:**

1. **Confirmation fatigue.** A bookkeeper doing month-end clicks through the same Yes/No dialog on hundreds of routine actions. Because "Yes" is always right, they learn to click it without reading. Those dialogs add effort and give no protection.
2. **Dialogs cover for missing undo.** Confirmations are the only safety net, so the team added them everywhere. The cost is paid on every action, including the 99% that were correct.
3. **The actually dangerous actions are unprotected.** Voiding a client-facing invoice is the one case that needs a speed bump. By then the user has been trained to dismiss dialogs, so the dialog they get on deleting a draft is probably ignored too.
4. **Pointless "Invoice deleted." dialog.** It's a modal that reports something the user just did, and it blocks them until they click OK.
5. **Silent autosave creates anxiety.** With no "Saved" indicator and no undo, users can't tell whether an edit stuck or whether a stray click changed something. Part of the tiredness is the constant low-level vigilance.

**What I'd change first, in order:**

1. **Add undo, and remove the routine confirmations.** This is the root fix. Make category change, reconcile, and draft delete immediately reversible. Show a toast like "Category changed · Undo" for about 8 seconds. For deletes, use soft delete (a trash or recently-deleted view, kept 30 days). This needs backend work (an audit or history trail for changes and a `deleted_at` flag). It's the biggest effort, but everything else depends on it. If you ship only one thing, ship this.
2. **Delete the category-change, reconcile, and "Invoice deleted." dialogs.** Once undo exists, they're pure friction. They're a quick win you can ship alongside step 1. If undo is delayed, remove the "Invoice deleted." and category dialogs now, because the toast-free cost is small.
3. **Add a real confirmation for voiding an emailed invoice.** Make it specific: "This invoice was emailed to Acme Co. on Oct 2. Voiding won't recall the email. Void invoice?" with a clearly labeled destructive button (not Yes/No). Consider offering to send a void notice or issue a credit note. This is a small change and it closes the most serious gap.
4. **Show save state.** Add a small "Saved" or "Saving…" indicator, and an error state if a save fails. Pair it with the change history from step 1 so users can see and revert past edits.

**Principle to adopt going forward:** confirm only when an action is irreversible or affects people outside the app. Otherwise make it undoable and say so with a non-blocking toast.

**Caveats:** this is from the behavior you described, not from the code or usage data. Before rebuilding, I'd check two things. First, whether reconciled transactions have any lock or period-close rules, since accounting compliance may require an audit trail, not just undo. Second, how often users hit the existing dialogs, to confirm that month-end volume is the driver. I can help look through the codebase if you point me to it. The working directory here is empty.
