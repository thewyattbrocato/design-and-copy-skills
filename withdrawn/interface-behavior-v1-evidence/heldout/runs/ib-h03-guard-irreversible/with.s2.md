**Neither option fits both actions. Archive list gets an undo toast, and Send campaign gets a specific confirmation, ideally with a short send delay.** Consistency should come from one rule applied to both: if an action can be undone, make it undoable. If it can't, confirm it.

Assumption: small-shop owners using this on desktop, a few times a week, who aren't email experts.

**Archive list: undo toast, no dialog**
- When someone archives a list, hide it right away and show a toast like "Archived 'Spring Customers'. Undo". Keep it up for about 8–10 seconds, which is a starting value.
- Archiving only hides the list from the sidebar, so it can be reversed. A dialog would add friction to a harmless action.
- Add an "Archived" view where lists can be restored later, so recovery doesn't depend on catching the toast.
- Announce the toast to screen readers through a polite live region, and don't dismiss it before it can be read.

**Send campaign: confirm, and add a delay if you can**
- Once an email reaches 200 to 30,000 inboxes, nothing can pull it back, so an undo toast would promise something you can't deliver.
- Use one specific confirmation, not a generic "Are you sure?". Name the list and the recipient count, for example "Send 'Spring Sale' to 12,480 people on 'Spring Customers'?". The button should say "Send to 12,480 people".
- Because the dialog is rare, people will still read it. Don't add it to anything reversible, or they'll start clicking through it.
- Better still, add a short send delay of about 30 seconds to a few minutes, with a visible "Sending in 0:30, Cancel" state. That gives you real undo for the one action that needs it. If you build this, you may be able to simplify the confirmation.
- Show progress in place on the campaign ("Sending… 4,200 of 12,480"), and keep success quiet rather than using a modal.

**What to tell your product lead**
Consistency matters, but users learn what's at stake, not which widget appeared. A dialog on a harmless archive teaches them to dismiss dialogs, so they'd dismiss the one on send too. The shared rule is: reversible gets undo, irreversible gets a specific confirmation. Both actions follow it, and each gets the treatment that fits what it does.

If your product lead insists on a single pattern, use the confirmation for both. Applying it to a harmless archive would be annoying but safe. An undo toast on send would be a false promise, and that's the worse failure.
