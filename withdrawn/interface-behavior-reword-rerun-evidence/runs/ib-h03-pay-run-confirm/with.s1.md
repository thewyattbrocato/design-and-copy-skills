Your designer is mostly right, but not about all of them. Delete the popups on three actions and keep one, and make that one better.

**Assumption:** a few people at your agency use this screen, probably one person on a laptop, mostly once a month. Payment runs are rare and the stakes are high.

**Remove the popup and make the action undoable:**
- **Archive a freelancer.** Archiving can be reversed, so move them to an "Archived" filter and show a toast with Undo. Keep the toast up for at least 6–10 seconds, and don't dismiss it while the pointer or keyboard focus is on it. Offer "Restore" from the archived list so the undo doesn't depend on the toast.
- **Edit a rate.** Save it in place, and show the old rate beside the new one until the next payment run. If someone types an odd value, such as 10× the previous rate, flag it next to the field instead of blocking it. Keep a change history showing who changed what and when.
- **Attach a receipt.** Attach it immediately and show a "Remove" link. Nothing is lost if it's attached by mistake.

The reason is that people click through popups that appear on every action. Once "Are you sure?" shows up everywhere, nobody reads it. So when the one popup that matters appears, they dismiss it without reading.

**Keep a confirmation, but redesign it: "Send payments."**
Money that has left your account can't be pulled back, so this is the one place a confirmation is justified. A generic "Are you sure?" doesn't count. Make it a review step that shows:
- The total amount and the number of freelancers: "Send $X to 58 freelancers."
- Anything unusual since last month, such as new payees, rates that changed, a total far from last month's, or freelancers with no receipt or missing payout details.
- The funding source and the date the money will arrive.
- A button that names the action ("Send $X to 58 freelancers"), not "OK" or "Yes."

Two more things make this safer:
- Let the person exclude or fix individual rows before sending. A single-row mistake shouldn't mean cancelling the whole run.
- If your payment provider allows it, add a short delay or "scheduled for…" window before the money moves. That turns an irreversible action into one you can cancel, and then the confirmation matters less.

**Apply the same rules elsewhere on this screen:**
- Don't show a "Saved!" popup. Show failures in place, and keep success quiet.
- Make the destructive controls visually quiet (not a bold red button) until undo exists.
- Make "Send payments" the only prominent, deliberate action on the screen.

**Summary for your designer:** removing the popups is right for reversible actions, as long as undo replaces them. Removing the one on "Send payments" would be a mistake, because that action can't be undone.
