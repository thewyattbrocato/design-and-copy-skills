Your designer is mostly right, but not about all of them. Remove most of the popups. Keep one, and make it a better one.

**Assumption:** a few staff use this on a desktop once a month. Each session is long, and the same people use it repeatedly. About 60 payments go out in each run.

**Remove the popup and add Undo:**
- **Archiving a freelancer:** archive right away and show a toast saying "Archived Sam R. · Undo" for about 8 seconds. Add an "Archived" filter where you can restore them at any time. Nothing is lost, so a question adds no safety.
- **Editing a rate:** save the edit when the field is committed. Show the old rate beside the new one, and keep a change history (who, when, old and new). If the freelancer has a pending payment, show "This will change the pending payment from $X to $Y" next to the field. That tells people what the edit affects without making them click through a popup.
- **Attaching a receipt:** attach it right away. Show the file name with Replace and Remove links. Removing it can also use an Undo toast.

People click through popups they see on every action. Once they do that, they also click through the one popup that matters. Fewer popups is what makes the remaining one work.

**Keep one confirmation: "Send payments."** Money has left your account and you can't call it back, so this is the one action nothing can undo. Where the designer is right is that a bare "Are you sure?" is lazy. Replace it with a review step that shows the facts:
- The total and the number of payments ("Send $48,200 to 58 freelancers").
- Anything unusual, called out in place. Examples are a rate changed since last month, a payment much larger than that person's usual amount, a missing receipt, or a freelancer with no payout details. Skip anyone who is archived or has a problem, and say you skipped them.
- A button that repeats the action and amount ("Send $48,200"), not "OK" or "Yes".

**Other behavior for the send:**
- Let people send part of the batch. Anyone with a problem can be held back without blocking the other payments.
- After you press send, show progress in the main view with a status for each person (sent, pending, failed). Don't show a "Success!" popup.
- Failures should stay on screen and have a Retry button for each one.
- If your payment provider supports it, add a short delay or a "Cancel batch" option for a few minutes. That would make even this step partly reversible.

**Check before you ship:** make sure archiving a freelancer really can be undone. If it deletes their payment history or breaks old records, then it needs a specific confirmation that says what will be lost. Also make sure the Undo toast can be reached by keyboard and is announced to screen readers.

I haven't seen your screen. If you share it or the code, I can check these against what's actually there.
