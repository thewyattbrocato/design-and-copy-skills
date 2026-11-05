## When it goes wrong

### What Nudge does
Nudge emails clients who are late on invoices, on the freelancer's behalf, from the freelancer's own address. Reminders go out 3, 10 and 21 days after the due date, unless the freelancer has paused that client.

Because the emails come from the freelancer's own address, a mistaken reminder reaches the client as a message from the freelancer, not from Nudge.

### What can't be undone
- **A sent email cannot be recalled.** Once a reminder has gone, nothing in Nudge or in support's hands can pull it back.
- **Stopping is possible only before sending.** A freelancer can stop any scheduled reminder up until 15 minutes before it sends. After that point the reminder will go.

### What stops reminders
- **Marking an invoice as paid cancels all remaining reminders for it.** This works at any time.
- **Pausing a client** stops reminders for that client.
- **Stopping an individual reminder** works up to 15 minutes before its send time.

### Known failure: reminder for an invoice that is already settled
**What happens.** When a client pays by bank transfer and the freelancer has not marked the invoice as paid, Nudge can still send a reminder for the settled invoice. The client receives a chase for money they have already paid, under the freelancer's name.

**How often.** It happened 3 times across 40 beta accounts.

**Why it happens.** Nudge relies on the freelancer marking the invoice paid. In the bank-transfer case that has not happened, so the invoice still looks overdue and the schedule continues.

**What the freelancer can do.**
- Mark the invoice as paid as soon as the payment arrives. This cancels all remaining reminders.
- If a reminder is already scheduled, stop it, but only up to 15 minutes before it sends.
- If the reminder has already been sent, it cannot be recalled. The freelancer would need to contact the client themselves.

### Visibility and support
- Every reminder is logged with the text sent, the time and the reason it was sent. This lets the freelancer and support see what the client received and why it was triggered. For the failure above, the log will show a reminder sent for an invoice that was not marked paid.
- **Support can read the log but cannot edit, resend or cancel anything on a freelancer's behalf.** Support can confirm what was sent and why. Any action, such as marking paid, stopping a reminder or pausing a client, has to be done by the freelancer.

### Open question: apology and credit
There is no apology or credit policy yet. Until one exists, support has nothing approved to offer a freelancer whose client received a mistaken reminder. This needs an owner and a decision before launch. The decision should cover whether Nudge offers any apology or credit, and what support is allowed to say in the meantime.
