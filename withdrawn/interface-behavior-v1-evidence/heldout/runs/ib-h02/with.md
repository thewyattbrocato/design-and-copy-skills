**What's going on:** the confirmations are on the wrong actions. Ledgerleaf asks permission for things that are cheap and common, and stays silent on the one action that really is dangerous.

- **Category change, reconcile, draft delete:** each gets an "Are you sure?" dialog. A bookkeeper does these hundreds of times in a month-end, so they click Yes without reading. That is the tiring part. A confirmation only protects anyone if it's rare.
- **"Invoice deleted. OK":** this is a success modal for normal operation. It adds a click and tells them nothing.
- **Voiding an emailed invoice:** this is the one action that touches the outside world, because the client has already received the invoice. It's the least reversible thing on the list, and it's the only one with no warning. The grey row is the only feedback.
- **Silent autosave with no history:** saving silently is fine. The problem is that nothing can be recovered. A wrong category or a deleted draft is permanent, so the dialogs were standing in for undo. And because nobody trusts the dialogs, people probably don't trust the autosave either.

**What I'd change first:** remove the safety nets that don't work and add the one that does.

1. **Add undo, then delete the dialogs.** This is the core fix.
   - Category change: apply it immediately and show a toast, "Category changed to Office Supplies · Undo", for about 8 seconds.
   - Mark reconciled: apply it immediately, with Undo. Un-reconciling should always work from the row itself.
   - Delete draft: move it to a Trash that keeps items for a retention period (to be decided, I'm not assuming a number), and show a toast with Undo. Remove the "Invoice deleted" dialog.
   - Make the toasts announce to screen readers and stay long enough to read.
2. **Give void a specific confirmation.** This is one of the few places a dialog is right, because the client already has the invoice and nothing can recall it. Name the consequences: "Void INV-1042 for Acme Co.? It was emailed to the client on [date]. Voiding won't unsend that email. [Void and notify client] [Void only] [Cancel]". Offering to send a void notice or a credit note would be even better. If your accounting rules treat a void as reversible, use an undo toast instead.
3. **Add an edit history.** Add a per-transaction log of who changed what and when, with a "Restore" action. This covers edits that aren't covered by the undo toast, such as ones noticed the next day, and it's what an accounting tool needs for audit anyway. Keep the quiet autosave, and show a small "Saved" state in the page where people are already looking, rather than in a popup.

**Order of work:** build undo and Trash first (item 1), because the dialogs can't be removed safely until it exists. Add the void confirmation in the same release, since it's the biggest risk today. Edit history can follow.

**Assumptions:** the users are bookkeepers on desktop, in long sessions, doing the same actions repeatedly. I've seen only your description, not the code, so check whether reconciled and voided states are reversible in your data model before promising Undo on them.

**How to check it worked:** a month-end should need far fewer clicks per transaction. It's also worth watching how often people use Undo, which tells you whether the old dialogs were ever catching mistakes.
