## When it goes wrong

### Failure 1: A reminder goes out that the freelancer wanted to stop

Nudge sends reminders from the freelancer's own address, so the client sees the message as coming from the freelancer. A sent email cannot be recalled.

- The freelancer can stop any scheduled reminder until 15 minutes before it sends.
- After that window, the reminder cannot be stopped.
- Marking the invoice as paid, at any time, cancels all remaining reminders for it. This stops future reminders but does not recall one already sent.

### Failure 2: A reminder is sent for an invoice that is already settled (known beta issue)

When a client pays by bank transfer and the freelancer has not marked the invoice as paid, Nudge can send a reminder for an invoice that is already settled. This happened 3 times across 40 beta accounts.

- **Freelancer action:** Mark the invoice as paid. This cancels all remaining reminders for it.
- **Already-sent reminders:** These cannot be recalled.
- **Root cause:** Not yet confirmed.

### Evidence: the reminder log

Every reminder is logged with:

- the text sent
- the time it was sent
- the reason it was sent

Use the log as the source of truth for any question about what was sent, when, and why.

### Who can do what

| Action | Freelancer | Support |
|---|---|---|
| Read the reminder log | Yes | Yes |
| Stop a scheduled reminder (until 15 minutes before send) | Yes | No |
| Mark an invoice as paid (cancels remaining reminders) | Yes, at any time | No |
| Edit, resend or cancel anything | Yes | No |

Support cannot edit, resend or cancel anything on a freelancer's behalf.

### Support playbook

1. **Client reports an unexpected reminder:** Check the log for the text, time and reason.
2. **Client says they already paid by bank transfer:** Check whether the freelancer has marked the invoice as paid.
   - If not, tell the freelancer to mark it as paid. This cancels remaining reminders.
   - Tell them any reminder already sent cannot be recalled.
3. **Do not promise an apology or credit.** There is no apology or credit policy yet.

### Open items

- **Apology and credit policy:** Not defined. Needs an owner and a decision before support can respond to affected freelancers.
- **Bank-transfer root cause:** Not confirmed. Engineering to investigate.
