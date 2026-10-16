Your designer is half right. Popups on everything are a real problem, but deleting all of them would be a mistake.

**Why blanket popups are bad:** When nearly every action asks "Are you sure?", people click through without reading. That means the one popup that matters gets the same reflex click as the rest. They also add friction to routine work.

**A better rule:** Ask for confirmation only when an action is hard to undo or has consequences outside the screen. For everything else, let it happen and offer a way back.

**What I'd do for each action:**

- **Send payments: keep the confirmation, and make it informative.** This moves real money to about 60 people, and you can't recall it. Replace "Are you sure?" with a summary: "Pay 58 freelancers a total of $41,230.00 on Oct 31," plus anything unusual (a rate that changed this month, a new payee, an amount well above their usual). The button should say "Send $41,230.00 to 58 freelancers," not "OK." This is the one place where a speed bump earns its keep.
- **Editing a rate: remove the popup.** It's reversible. Show the change inline ("$60/hr → $65/hr") and save it. If a rate change affects an in-progress payment run, flag that on the payments screen where it will be seen. A history or audit log is worth having.
- **Attaching a receipt: remove the popup.** It's low-stakes and easy to fix. Add a "Remove" option on the attachment, or an Undo toast after upload.
- **Archiving a freelancer: remove the popup and add Undo.** Archiving is usually reversible, so show "Freelancer archived. Undo" for several seconds and keep an "Archived" filter to restore them. Make an exception if archiving also cancels scheduled payments or deletes data. In that case, state the consequence in a specific confirmation, such as "This will remove them from the Oct 31 run."

**Two supporting ideas:**

1. **Undo beats confirmation** for reversible actions. It's faster, and it protects people from mistakes better than a popup they click past.
2. **Make destructive buttons specific.** "Archive Maria Lopez" and "Send $41,230.00" are better than "Yes" and "OK," because the button label forces the person to read what they're doing.

**The result:** one meaningful confirmation (sending payments) and quiet, undoable actions everywhere else. This will make the screen faster for day-to-day work and make the payment confirmation much more likely to be read.

If you tell me whether archiving affects scheduled payments, and whether payments can be canceled after sending, I can tighten these recommendations.
