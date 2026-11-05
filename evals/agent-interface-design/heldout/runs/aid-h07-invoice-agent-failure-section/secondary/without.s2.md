## When it goes wrong

Nudge sends reminders on the freelancer's behalf, from the freelancer's own email address, to clients who are late on an invoice. Reminders go out 3, 10 and 21 days after the due date, unless the freelancer has paused that client. Because the email comes from the freelancer's address, a wrong reminder reaches the client as if the freelancer sent it.

### Known failure: reminder sent for an invoice already paid by bank transfer

- **What happens:** When a client pays by bank transfer and the freelancer has not marked the invoice as paid in Nudge, Nudge can still send a reminder for that invoice.
- **How often:** Seen 3 times across 40 beta accounts.
- **Freelancer's options:**
  - Mark the invoice as paid at any time. This cancels all remaining reminders for that invoice.
  - Stop any individual scheduled reminder up to 15 minutes before it sends.
- **What cannot be undone:** A reminder that has already been sent cannot be recalled.
- **Status:** No fix is documented in this spec. Engineering owns the root cause and the fix.

### Other failure modes

| Situation | What Nudge does | What the freelancer can do | What cannot be done |
|---|---|---|---|
| Freelancer wants to stop a reminder before it sends | Sends it unless it has been stopped | Stop the reminder up to 15 minutes before send time | Stop it within 15 minutes of send time |
| Freelancer wants to stop a reminder after it has sent | Nothing further, for that reminder | None for the sent email | Recall the email |
| Client has paid but the freelancer has not marked the invoice paid | Continues scheduled reminders | Mark the invoice paid, which cancels remaining reminders | Undo reminders already sent |
| Freelancer wants to stop all reminders for a client | Continues unless the client is paused | Pause the client | Nothing else is documented |

### Audit log

Every reminder is logged with:
- the exact text sent,
- the time it was sent,
- the reason it was sent.

Use the log to establish what a client received and why. It is the record of truth for any dispute about a reminder.

### Support's role

- Support can **read** the log.
- Support **cannot** edit, resend or cancel anything on a freelancer's behalf. Any change to a reminder or invoice has to be made by the freelancer.
- Support should direct the freelancer to the relevant action (mark paid, stop reminder, pause client) and confirm from the log what was sent.

### Compensation

There is no apology or credit policy yet. Support should not promise credits or make commitments on Nudge's behalf for a bad reminder until a policy exists.

### Open items

- Fix and timeline for the bank transfer failure.
- Apology and credit policy.
