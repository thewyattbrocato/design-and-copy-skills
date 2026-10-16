Your designer is mostly right, but not about all of them. Remove three of the four popups and keep one, rewritten.

**Assumptions:** a few admins use this on a desktop about once a month. Sessions are short but the stakes are real, because it moves money to about 60 people. I've assumed payments can't be recalled once sent.

**Remove these, and make them undoable instead**
- **Archiving a freelancer:** archive right away and show a toast with Undo for several seconds. Keep an "Archived" filter where they can be restored later. Archiving can be reversed, so a popup only adds friction.
- **Editing a rate:** save the change as soon as it's made, with no popup. Show the old rate next to the new one, for example "was $50 → $55", until the next send. Keep a change history. Flag odd values in place, such as a rate that jumps 10× (likely a typo). Don't block them.
- **Attaching a receipt:** attach it with no popup. Show the file name in the row, and add a Remove link that can be undone.

The reason is that people click through popups that appear on every action. Once they do, the one popup that matters gets clicked through too.

**Keep one: "Send payments"**
This is the only action here that can't be undone, because the money has moved. Replace the generic "Are you sure?" with a specific confirmation:
- It states the count and total, for example "Send $X to N freelancers."
- It lists anything unusual, such as a rate changed since last month, a freelancer with no receipt, or a payment much higher or lower than last time. Those are the things a person would actually want to catch.
- The button says what it does ("Send $X to N freelancers"), not "OK" or "Yes".
- Freelancers who are archived or missing payment details are excluded by default and listed in the confirmation, so nothing surprising goes out.

**Further changes to the screen**
- Show a running total and a count above the list, so the person has already reviewed the numbers before they reach the confirmation.
- After sending, show per-row status in the list (Sent, Failed, Pending) instead of a "Success!" popup. If any payment fails, say so clearly and let them retry just those rows.
- If your payment provider allows a short hold or cancellation window, use it. It would make the send partly undoable, and you could then lighten the confirmation.

**Caveat:** I haven't seen the screen or your provider's cancellation rules. If sent payments can be reversed, the confirmation can be lighter. If anything else on the screen is irreversible, such as permanently deleting a freelancer's records, that action should also get a specific confirmation.
