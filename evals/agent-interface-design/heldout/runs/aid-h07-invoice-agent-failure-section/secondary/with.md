## When it goes wrong

Nudge sends email on the freelancer's behalf, from the freelancer's own address. Once an email is sent, it cannot be recalled. Every failure case below is therefore about what happens before a send, what the freelancer can still stop, and what the record shows afterwards.

### Controls before a send

- **Pausing a client** stops reminders for that client. Reminders otherwise go out 3, 10 and 21 days after the due date.
- **Stopping a scheduled reminder** is possible up until 15 minutes before it sends. After that window, the reminder cannot be stopped.
- **Marking an invoice as paid** cancels all remaining reminders for that invoice. This works at any time.

### Known failure: reminder sent for a settled invoice

- **What happens:** When a client pays by bank transfer and the freelancer has not marked the invoice as paid, Nudge can send a reminder for an invoice that is already settled.
- **How often:** This happened 3 times across 40 beta accounts.
- **What the freelancer can do:** Mark the invoice as paid. This cancels all remaining reminders for it. It does not recall a reminder that has already been sent.
- **Prevention:** Nothing in the current facts detects a bank-transfer payment automatically. Until it does, the freelancer's mark-as-paid action is the only control that stops these reminders.

### What is logged

- Every reminder is logged with the text sent, the time it was sent, and the reason it was sent.
- Support can read this log. Support cannot edit, resend or cancel anything on a freelancer's behalf.

### Support handling

- Support can use the log to show a freelancer exactly what was sent, when, and why.
- Support cannot fix the situation for the freelancer. Any change to a scheduled or sent reminder must be made by the freelancer.

### Open items

- **No apology or credit policy exists yet.** Support has no defined response for a client who received a reminder for a settled invoice, and no defined remedy for the freelancer.
