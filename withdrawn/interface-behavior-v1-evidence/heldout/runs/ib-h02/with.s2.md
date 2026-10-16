**What's going on:** Ledgerleaf has its safeguards upside down. The reversible, high-frequency actions get a confirmation, and the irreversible, outward-facing one gets none.

Assumption: the users are bookkeepers on desktop, doing hundreds of these actions per month-end in long sessions. They are past their first week.

**Diagnosis**

- **Category change, reconcile, draft delete:** each of these asks "Are you sure?" even though the action is routine and should be reversible. Over a month-end that is hundreds of Yes clicks. People learn to click Yes without reading, so the dialogs protect nothing. This is most likely the "tiring" feeling.
- **"Invoice deleted. OK":** a modal announcing normal success. It adds a click and tells the user nothing.
- **Void of an emailed invoice, with no dialog:** this is the one action with outside consequences. The client already has the invoice, and the void is a legal and accounting record. It is also the only place a specific confirmation would help, and it is the one place there isn't one.
- **Silent save on navigate-away:** autosave is the right behavior. But with no visible state ("Saved" / "Saving…" / "Couldn't save") and no undo, users can't trust it. They also can't fix a slip.
- **No way to recover anything:** this is the root cause. Because nothing can be undone, the team put a dialog in front of every action to compensate. Fixing recovery lets you remove most of the dialogs.

**What I'd change first**

1. **Add undo, then remove the dialogs it replaces.**
   - When a user changes a category, marks a transaction reconciled, or deletes a draft, apply the change immediately. Show a toast with an Undo button for several seconds.
   - Announce the toast to screen readers, and don't remove it before it can be read.
   - Delete the three Yes/No dialogs and the "Invoice deleted" dialog.
   - Drafts go to a Trash with retention, so they can still be recovered after the toast is gone. I'd pick the retention window with you rather than guess one.
   - Add per-transaction history for category and reconciliation changes, so an earlier change can be reverted too.
   - Un-reconcile should be one click.
2. **Put one specific confirmation on voiding an emailed invoice.** For example: "Void INV-1042? It was emailed to [client] on [date]. They won't be notified automatically." Offer a "Void and send notice" option if that fits your workflow. Name the invoice and the consequence, and keep it rare so people still read it. This should be the only confirmation in the flow.
3. **Show save state in place.** Add a quiet "Saved" / "Saving…" indicator near the record. Failures should say so loudly. Success should stay silent, with no popup. Keep unsaved edits through errors and crashes.

**Later, if the flow is still slow**

- Bulk select with a count bar, so categorizing or reconciling many rows is one action with one undo.
- Keyboard routes for the common actions.
- Remember the last category used per payee.

I haven't seen the app's code or any usage data. The above is based only on the behaviors you listed. Before you build, check whether voiding a posted invoice is truly irreversible in your data model. If you can un-void, you may be able to treat it with a toast too, with the confirmation only for the "already emailed" case.
