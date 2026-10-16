**Your designer is mostly right, but not about all of them.** Delete the popups on actions you can undo. Keep one confirmation, on "Send payments", because that action can't be undone.

**Assumptions:** One or two people at your agency use this screen. They use it monthly, on a desktop, with about 60 payees. Each payment run is a high-stakes session.

**Rules by action**

- **Archive a freelancer**
  - When someone archives a freelancer, do it immediately and show a toast: "Archived Sam R. · Undo". Keep the toast up for about 8–10 seconds, and pause it on hover and focus.
  - Add an "Archived" filter where they can restore anyone later.
  - Why: archiving is reversible, so a popup only slows down the common case.
  - If archiving would remove someone from a payment run that is already queued, show that in place on the row instead of in a popup.

- **Edit a rate**
  - When someone edits a rate, save it in place and keep the previous value visible. For example, show "$85/hr (was $80)" with an Undo link.
  - Flag odd values (for example, 10× the old rate) with an inline warning, but still accept them.
  - Why: an edit is trivially reversible, and a typo is better caught by seeing the change than by a popup people click through.
  - If a rate change affects a run that is already drafted, show the new total on the run itself.

- **Attach a receipt**
  - When someone attaches a receipt, just attach it and show the file name on the row.
  - Add a remove control that can be undone.
  - Why: nothing is lost or sent, so there's nothing to confirm.

- **Send payments** (the one to keep)
  - When someone clicks "Send payments", show one specific confirmation that summarizes the run. It should include the number of payees, the total amount, the funding account, and anything unusual. For example: "Send $41,200 to 58 freelancers from Operating ••4821. 2 rates changed since last month."
  - Make the button label say what it does, such as "Send $41,200", not "Yes" or "OK".
  - Why: money moved can't be recalled, and this is the only action where a mistake costs real money. Because it's the only confirmation left, people will read it.
  - Consider a short send delay (for example, "Sending in 30s · Cancel") if your payment provider allows cancelling in that window. I'm assuming it might, so check before promising it.

**What the screen should do instead of popups**

- **Show a review state before the send.** Show the run as a draft with a total, a count, and per-row flags for changed rates, missing receipts, and newly added payees. People catch mistakes here, in context, which works better than a popup.
- **Make "Send payments" separate from editing.** Save everything continuously and quietly. Sending is the only deliberate, final step.
- **Show state in place.** Use per-row badges such as Draft, Sent, and Failed, and a progress indicator during sending. Don't use success popups. Report failures on the row that failed, and let people retry just that row.
- **Keep destructive controls visually quiet.** Archive and remove shouldn't look like primary buttons.
- **Make undo accessible.** Toasts should be announced to screen readers and shouldn't disappear before they can be read.

**Why "lazy design" is the wrong frame:** The real problem is that you've used one blanket confirmation for everything. Popups on every action teach people to click through without reading, so the one popup that matters gets the same reflex. Removing the reversible ones is what makes the "Send payments" confirmation work.
