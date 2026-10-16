Your designer is mostly right, but not about all of them. Keep one popup and delete the rest.

**Assumption:** You or a small team use this on a desktop about once a month. Each session covers roughly 60 payments and has real money behind it.

**Rules**

- **Archive a freelancer: remove the popup and add an Undo toast.**
  - Archiving is reversible, so a popup is just friction.
  - The toast should last about 8 to 10 seconds and pause on hover and focus.
  - It should say "Archived Dana Lee. Undo."
  - Archived people should also stay reachable in an "Archived" filter, so you can restore them after the toast is gone.

- **Edit a rate: remove the popup and save the change directly.**
  - Show the old and new rate in place, for example "Rate: $50 → $55/hr", with Undo.
  - The change can't move money by itself. Payments only use it when you send them.
  - If an edit is far from the old value (say 10× higher), flag it inline on the field. Don't block it with a popup.

- **Attach a receipt: remove the popup.**
  - Attaching is an additive action, and the user can detach it again.
  - Show the file name and a thumbnail on the row, with a "Remove" control.
  - Report only failures, such as a wrong file type or an upload that didn't finish.

- **Send payments: keep the confirmation, and make it specific.**
  - This is the one action nothing can restore. Money moves and freelancers are notified.
  - A generic "Are you sure?" gets clicked through by habit. Replace it with a review step that states what will happen:
    - "Send $18,420 to 58 freelancers on Oct 15."
    - Flag anything unusual: 2 freelancers with no receipt, 1 rate changed since last month, 1 amount more than 30% above their usual (that threshold is a placeholder, so pick your own).
    - Label the button with the action ("Send $18,420"), not "OK" or "Yes".
  - If your payment provider allows scheduling or cancellation, add a short delay after sending, such as a 30-minute window with a visible "Cancel payments" button. That would be better than any popup. I don't know whether your provider supports it, so check.

- **Make mistakes harder to make in the first place.**
  - Keep Send payments visually separate from the row actions, and don't make it the primary button until the list is complete.
  - Show a running total and a status on each row ("Ready", "Missing receipt", "Sent").
  - After sending, put the result in the main view with a per-person status. Don't use a success popup.

**Why this works:** Popups on actions you can undo teach people to click "Yes" without reading. When the one real warning arrives, it gets the same reflex. Removing the three harmless ones is what makes the Send confirmation work.

**Tell your designer:** The popups aren't lazy design on their own. The lazy part is using the same generic popup for all four actions. I'd cut three and rebuild the fourth.
