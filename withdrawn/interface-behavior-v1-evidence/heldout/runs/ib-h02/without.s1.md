**What's going on:** the confirmation dialogs are inverted relative to the risk. The app asks permission for things that are cheap and harmless, and stays silent about things that are costly or irreversible. That produces fatigue, and it also trains users to click through dialogs without reading them.

| Action | Current | Real risk |
|---|---|---|
| Change category | Confirm dialog | Low. It's trivially re-editable, but there's no undo. |
| Mark reconciled | Confirm dialog | Low to medium. It's routine and repeated hundreds of times a month. |
| Delete draft | Confirm dialog, then an "Invoice deleted" OK dialog | Medium. It's permanent, and the dialog is the only safety net. |
| Void a posted, emailed invoice | **Nothing** | **High.** It's an external, accounting-significant action that the client has already seen. |
| Edit and navigate away | Silent save | Unclear to the user. They get no feedback and no way to revert. |

The specific problems:

1. **Confirmation fatigue.** The bookkeeper sees "Are you sure?" dozens of times per session for routine actions. By the time they reach a dangerous one, "Yes" is a reflex. The generic wording ("Are you sure…?") hides what is actually changing.
2. **The "Invoice deleted." OK dialog** is pure friction. It blocks the user to report something they just did.
3. **Voiding a posted, emailed invoice has no guard.** This is the one action that deserves friction, and it has none.
4. **No undo anywhere.** Confirmations are standing in for undo. Users can't recover from mistakes, so the app asks them to be sure beforehand every time. This is the root cause.
5. **Silent autosave with no feedback.** Users can't tell whether an edit was saved, and they can't revert it. That's uncomfortable in a financial tool.

**What I'd change first:** add undo, and remove the low-risk confirmations in the same release.

1. **Remove the confirm dialogs on category change and mark reconciled.** Apply the change immediately and show a brief toast, e.g. "Category changed to Office Supplies · Undo" (about 8–10 seconds).
2. **Delete draft:** remove the confirm dialog and the "Invoice deleted." dialog. Delete immediately and show a toast with Undo. A soft delete with a retention window (e.g. 30 days) also makes recovery possible after the toast is gone.
3. **Void posted invoice:** add a real confirmation that names the consequence, e.g. "Void invoice #1042? It was emailed to Acme Co. on Sep 3. The client will not be notified automatically." Use a specific button label like "Void invoice" rather than Yes/No. Consider requiring a reason.
4. **Autosave:** show a subtle "Saved" indicator. Later, add an edit history or revert.

I'd do undo first because it makes the rest safe. Once it exists, the dialogs can go. Reserve blocking confirmations for the few actions that are irreversible or visible to people outside the app, so that they get noticed again.

**Caveats:** I'm working from your description, not the code or usage data, so I haven't verified any of this. Two checks would help. First, find out whether reconciliation has downstream effects, such as locked periods or exports. If it does, it may need an undo path that respects those locks. Second, check whether voiding can be reversed on the accounting side. That decides how strict the void confirmation needs to be. If you'd like, I can look through the codebase and find where these dialogs are implemented. The working directory I'm in is empty of project files, so you'd need to point me at the repo.
