Your designer is mostly right, but "delete every one" goes too far. Keep exactly one confirmation, on "Send payments".

**Assumption:** a few admins on desktop use this screen once a month, so it's low frequency but high stakes. About 60 payees go out per run.

**Remove the popup and make the action undoable:**
- **Archive a freelancer:** archive immediately and show a toast with Undo for several seconds. Put archived people in an "Archived" filter where one click restores them. Nothing is lost, so a popup only adds friction.
- **Edit a rate:** edit in place and save quietly. Keep a change history (who, old rate, new rate, when) so a mistake is easy to spot and revert. If the edit touches a payment batch you've already queued, show a note beside the field, e.g. "Applies to the next run, not the 14 queued." Don't use a popup for that.
- **Attach a receipt:** attach it immediately, show the filename in place, and add a "Remove" link. This is trivially reversible.

**Keep one confirmation, and make it specific:**
- **Send payments** moves money, and you can't pull it back. A generic "Are you sure?" is the lazy version your designer is right to dislike. Replace it with a summary that earns its interruption:
  - The total amount and the number of freelancers ("Pay 58 freelancers $41,230.00").
  - Anything unusual flagged inline: rates changed since last month, people with no receipt, amounts far from their usual, anyone archived but still in the batch.
  - A button that names the action ("Send $41,230.00 to 58 freelancers"), not "OK" or "Yes".
  - A way back out: Esc or Cancel, with focus returned to the screen.

**Make the confirmation easier to trust:**
- Keep it rare. If every action warns, people click through the one that matters.
- Before sending, show a review state in the main view (a "Ready to send" list with the flags above). The final dialog then just confirms what they've already seen.
- After sending, show status in place (per-person Sent / Pending / Failed), not a "Success!" popup. Failures should say which payment failed and why.
- If your payment provider allows it, a short cancel window after sending (e.g. "Sent. Undo for 30 seconds") is better than any popup. I'm assuming you don't know whether it does, so check.

**Accessibility:** Undo toasts should be announced to screen readers and stay up long enough to read. The confirmation should trap focus and return it on close.

**Bottom line:** the popups on archive, rate edit and receipt are fixing the wrong problem. Undo and history fix it better. The popup on "Send payments" is the one that should stay, but it should show the total, the count and the flags.
