Your designer is mostly right, but not about all of them. Delete the popups on the reversible actions and keep one on "Send payments", with the details filled in.

**Assumptions:** a few people at your agency use this once a month on a desktop. It's a low-frequency, high-stakes screen with about 60 rows.

**Remove these popups and make the actions undoable instead:**
- **Archive a freelancer.** Archive immediately and show a toast with Undo. Put archived people in an "Archived" filter where they can be restored. Archiving should never delete data. One caveat: if the person has a payment pending in the current run, say so in the toast, or block the archive until that's resolved.
- **Edit a rate.** Edit it in place and save it quietly. Show the old rate in the row's history, and add Undo in a toast. If a new rate differs sharply from the old one (my suggestion is more than about 25%, but pick your own threshold), flag it in the row with a small "was $X" note. Don't use a popup for this.
- **Attach a receipt.** Attach it right away. Removing a receipt is also undoable. A popup here only makes the routine path slower.

Popups on reversible actions teach people to click "OK" without reading. Then the one popup that matters gets the same reflex click.

**Keep one confirmation: "Send payments".** Money leaving your account can't be taken back, so this is the case where a confirmation earns its place. Make it specific rather than "Are you sure?":
- Title it with the facts: "Send 58 payments totaling $X from [account]?"
- Show what's unusual: anyone with a changed rate, a missing receipt, or a much higher or lower amount than last month. Don't list all 60.
- Name the people who will be skipped and why, such as an archived freelancer or missing payment details.
- Label the buttons with the action ("Send 58 payments" and "Cancel"), not "Yes" and "No".

**Make the screen carry the review.** Most of this review should happen before the click.
- Show a running total and count at the top of the screen, and a status for each row (ready, needs receipt, changed since last month).
- Let people filter to "needs attention" so problems are visible before they send.
- After sending, show a progress state and per-row results (sent, failed). A failed payment should offer a retry on that row. Don't use a success popup.

**If your payment provider allows cancelling or scheduling,** use that instead of an extra confirmation. For example, offer a short "Sending in 30 seconds. Undo" window. I don't know what your provider supports, so check before relying on it.

In short, your designer is right that blanket popups are lazy, but replacing them with undo only works where something can be undone. Sending money can't, so that popup stays and should be more useful.
