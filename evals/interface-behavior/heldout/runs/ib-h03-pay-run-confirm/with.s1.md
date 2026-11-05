Your designer is mostly right, but not about all of them. Delete three of the four popups and keep one, with a better design.

**Assumption:** a few people (you and maybe a bookkeeper) use this on a desktop once a month, in one sitting, handling about 60 payees. The stakes are high and the volume is low.

**Remove these popups and make the actions undoable**

- **Archiving a freelancer:** archive right away and show a toast: "Archived Dana. Undo". Keep the toast up for about 8 seconds. Add an "Archived" filter where you can restore them. Archiving only hides a record, so a popup adds nothing. Also, an "Are you sure?" popup you see ten times teaches you to click through it.
- **Editing a rate:** save the edit in place and show the old value in the row's history, or offer "Undo" on a toast. The more useful safeguard is to flag unusual values next to the field. For example: "This is 3× the previous rate." Don't interrupt every edit.
- **Attaching a receipt:** attach it immediately, with a visible "Remove" and "Replace" on the file. This is the most clearly reversible action of the four, so a popup here is pure friction.

**Keep one confirmation: "Send payments"**

Sending money can't be undone, so it's the one place where asking is justified. Make it specific rather than a generic "Are you sure?":

- The title and button should say what happens: "Send 58 payments totaling $X". The button label should say "Send $X to 58 freelancers", not "Yes".
- Put the real information in the confirmation: the count, the total, the payment date, and anything unusual, such as a rate that changed since last month, a payee with no receipt, or someone newly added. Let people click through to fix those items.
- Leave out freelancers who are archived or missing details, and say so: "2 skipped: missing bank details."
- Consider a short cancel window after sending if your payment provider allows it, such as "Sending in 30 seconds. Cancel". I don't know whether yours does, so check before promising it.
- Make the button's busy state clear while it runs. After it finishes, show the result in the page, such as a "Paid" status on each row, instead of a "Success!" popup. Failures should be shown per row, with a retry.

**Why this works**

If every action asks for confirmation, the confirmation that matters gets the same reflex click as the rest. Removing the three low-stakes popups is what makes the "Send payments" one worth reading. The rule is simple: if you can undo it, let people act and offer Undo. If you can't undo it, ask once and be specific.

**Two small things to check**

- Make sure the undo toast can be reached by keyboard and is announced to screen readers. Don't let it vanish too quickly.
- Edits to rates should be logged with who changed them and when, regardless of popups. That log will help most when a payment amount is disputed.
