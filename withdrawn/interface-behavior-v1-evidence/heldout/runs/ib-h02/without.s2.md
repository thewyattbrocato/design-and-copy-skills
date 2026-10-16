**What's going on:** the confirmations are inverted. The app spends the user's attention on safe or trivial actions and spends none on the risky ones.

| Action | Current | Actual risk |
|---|---|---|
| Change category | Confirm dialog | Low, and it's the most frequent action |
| Mark reconciled | Confirm dialog | Low if reversible |
| Delete draft | Confirm dialog, then an "Invoice deleted" dialog | Medium, because it's unrecoverable |
| Void emailed invoice | Nothing | High, because the client has already seen it |
| Edit and navigate away | Silent save | Unclear to the user, and there's no undo |
| Deleted draft or changed category | Can't be recovered | The root cause |

Bookkeepers do these actions hundreds of times a month. Each "Are you sure?" is a small interruption, and people click through them reflexively. That trains them to dismiss dialogs without reading, so the one dialog that matters gets dismissed the same way. The constant interruptions and the lack of any safety net are probably what customers mean by "tiring". They have to stay vigilant on every click because the app never tells them which clicks matter and never lets them take one back.

**What I'd change first: add undo, then remove the routine dialogs.**

1. **Add undo for category changes, reconciliation, and draft deletion.** Show a toast like "Category changed. Undo" for about 8–10 seconds. For deletes, use soft-delete with a "Recently deleted" area. Undo makes the confirmations unnecessary, and it also covers the silent-save problem. Consider a small change history per transaction too.
2. **Remove the dialogs for category change, reconcile, and the "Invoice deleted." OK box.** Replace them with the undo toast. The OK-only dialog is pure friction.
3. **Add a real confirmation for voiding an emailed invoice.** Spell out the consequence: "This invoice was emailed to [client] on [date]. Voiding won't unsend it. Void and notify client?" Offer to send a void notice or credit note. This is the only action here that has external effects, so it's the one that deserves a dialog.
4. **Keep the silent autosave, but make it visible.** Show "Saved" or "Saved just now" so it's no longer invisible. Pair it with the undo or history from step 1.

Do step 1 first, because the rest depends on it. Step 3 is the smallest change and guards against the worst outcome, so I'd ship it in parallel.

**Caveats:**
- Reconcile may deserve a closer look. If reconciled periods are locked or feed filed reports, un-reconciling needs to be possible but deliberate, and I'd want to know how your app treats it.
- This is inferred from your description. Before rebuilding, I'd check that the dialog count per session matches the "tiring" feedback. Session recordings or a few observed month-ends would confirm it.

I haven't looked at the codebase. If you point me at it, I can find where these dialogs are wired up and sketch the undo mechanism.
