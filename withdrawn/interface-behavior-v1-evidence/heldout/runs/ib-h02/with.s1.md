**Assumption:** the users are bookkeepers on desktop who spend long sessions in the app, doing the same actions hundreds of times at month-end. I haven't seen the code, so this comes from your description only.

## What's going on

Confirmations are attached to the wrong actions. The app asks for confirmation where nothing is at risk, and stays silent where something is.

| Action | Today | Actual risk |
|---|---|---|
| Change category | Confirm dialog | Low. It's reversible, but there's no undo. |
| Mark reconciled | Confirm dialog | Low. It's reversible, but there's no undo. |
| Delete draft | Confirm dialog, then an "Invoice deleted" dialog | Low to medium. It's unrecoverable, and the dialog is the only protection. |
| Void an emailed invoice | Nothing | **High.** The client has already seen it, and the record is legal and financial. |
| Navigate away with edits | Silent save | Medium. It's fine if visible and undoable. |

This causes the tiredness in three ways:

- **Volume.** A month-end run means hundreds of Yes/No clicks, and each one breaks the bookkeeper's rhythm.
- **Learned dismissal.** Bookkeepers click "Yes" without reading, so the dialogs protect nothing. The one dialog that matters would also get ignored.
- **No safety net.** Because nothing can be undone, the dialogs are the only protection. They are weak protection, because people click through them.

The bookkeepers likely sense this, and it probably adds to the tiredness. They have to stay on guard the whole time because the app won't catch a mistake.

## What I'd change first

**1. Add undo, then remove the dialogs it replaces.** Undo is the foundation, and the other fixes depend on it.
- Category change and reconcile: apply immediately, then show a toast with Undo for about 8 seconds. Announce it to screen readers. Keep an activity or audit trail of these changes. This is likely wanted for bookkeeping anyway.
- Delete draft: move it to a Trash with retention, and show an Undo toast. Remove both dialogs. The "Invoice deleted." OK dialog goes entirely, because success shouldn't interrupt anyone. The row disappearing is the feedback.

**2. Put the one real confirmation on voiding an emailed invoice.** This is the only action here that can't be cleanly taken back, because the client already has the invoice. The confirmation should be specific. For example: "Void INV-1042? It was emailed to Acme on Oct 3. They'll still have the original. [Void and send notice] [Void only] [Cancel]." Keep this dialog rare so people still read it. A voided row should also say "Voided" in text, not only turn grey, since colour alone is a weak cue.

**3. Make silent saves visible and recoverable.**
- Show a small "Saved" or "Saving…" indicator near the form, and show failures loudly.
- Add per-record version history for edits. This also covers the "changed category" case from the second bullet of your list.

## Order of work

1. Undo infrastructure (toast, trash, change log).
2. Remove the four low-value dialogs once undo works. Don't remove them before, or you'd strip the only protection.
3. Add the void confirmation.
4. Add the save indicator and version history.

Steps 1 and 2 should deliver most of the relief. Bulk actions such as selecting many transactions to categorize or reconcile are likely the next big gain. I haven't seen evidence for them, so that's a guess, and I'd check it with a bookkeeper.

If you want, point me at the codebase and I can find where these dialogs live and sketch the undo mechanism.
