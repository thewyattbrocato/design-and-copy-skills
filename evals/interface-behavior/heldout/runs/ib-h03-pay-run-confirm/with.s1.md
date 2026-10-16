Your designer is mostly right, but not about all four. Delete three of the popups and keep one, rewritten.

**Assumption:** You or one or two staff use this on a desktop about once a month, with around 60 payees. Changes are occasional, and "Send payments" is the one high-stakes step.

**Remove the popup and make the action undoable**
- **Archiving a freelancer:** Archive immediately and show a toast with Undo for about 8 seconds. Add an "Archived" filter where you can restore them any time. Archiving only hides a record, so a popup adds friction and protects nothing.
- **Editing a rate:** Save the change when the field loses focus. Show the old rate beside the new one ("was $60/hr") and keep a small change history. If the rate affects a payment that's already queued, flag that in place.
- **Attaching a receipt:** Attach it straight away and show it as a thumbnail with a Remove link. This is easy to reverse, so it needs no confirmation.

**Keep one confirmation: Send payments**
Money that has left your account can't be pulled back, so this is the one place a confirmation earns its keep. Make it specific rather than a generic "Are you sure?":
- Name the stakes in the title: "Send $18,450 to 58 freelancers?"
- Show the account it's paid from and the date.
- Flag anything unusual in the summary. Examples are a rate that changed since last month, a payee with no receipt, or an amount far above their usual one.
- Label the button with the action ("Send $18,450"), not "OK" or "Yes".
- After sending, show per-person status on the screen (Pending, Paid, Failed), not a success popup.

Because this is the only popup left, people will actually read it. Today, with a popup on everything, they've likely learned to click through all of them, including this one.

**One optional safeguard:** if your payment provider allows it, add a short "Cancel send" window (a few minutes) after confirming. That would cover the one case where nothing else can undo a mistake.

Your designer's instinct, that blanket confirmations are lazy, is sound. The fix is to make mistakes cheap to undo and to save the confirmation for the irreversible step. Deleting every popup, including the one on "Send payments", would go too far.
