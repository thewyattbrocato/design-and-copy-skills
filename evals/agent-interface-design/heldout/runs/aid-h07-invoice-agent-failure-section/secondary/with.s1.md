## When it goes wrong

Nudge sends late-payment reminders from the freelancer's own address, on their behalf. Mistakes reach the client directly, and a sent email cannot be recalled. The controls below are the only ways to prevent or limit a bad send.

### Known failure: reminder sent for an invoice already paid by bank transfer

- **What happens:** A client pays by bank transfer, the freelancer has not marked the invoice as paid in Nudge, and Nudge sends a reminder for an invoice that is already settled.
- **How often:** Seen 3 times across 40 beta accounts.
- **Client impact:** The client receives a reminder for a settled invoice, from the freelancer's address.
- **Freelancer workaround:** Mark the invoice as paid. This cancels all remaining reminders for it. It only prevents reminders that have not yet sent.
- **Status:** Root cause and fix are not yet defined. Do not describe this as resolved.

### What the freelancer can do

| Action | Effect | Limit |
|---|---|---|
| Pause a client | Stops reminders for that client | Applies to that client's reminders |
| Stop a scheduled reminder | Cancels that one reminder | Must be done at least 15 minutes before it sends |
| Mark an invoice as paid | Cancels all remaining reminders for that invoice | Available at any time |

Scheduled reminders go out 3, 10 and 21 days after the due date, unless the client is paused.

Once an email has sent, nothing can recall it. The freelancer's only option for that email is to stop the reminders that have not yet sent.

### What support can do

- **Can:** Read the reminder log for any freelancer. Each entry shows the text sent, the time it was sent and the reason it was sent.
- **Cannot:** Edit, resend or cancel anything on a freelancer's behalf.

When a freelancer reports a problem, support uses the log to establish what was sent and when. Support then directs the freelancer to the actions in the table above. Support should not promise any action that the freelancer cannot take themselves.

### Logging

Every reminder is logged with the text sent, the time and the reason. The log is the record of what happened for any incident, including the bank-transfer failure above.

### Compensation

There is no apology or credit policy yet. Until one is defined, support should not offer apologies or credits on Nudge's behalf. This needs a decision from the product owner.

### Open items

1. **Bank-transfer failure:** Root cause and fix are not defined. Engineering owns this.
2. **Apology and credit policy:** Not defined. Product owner decides.
3. **Escalation path for support:** Not defined. Needed for cases the freelancer cannot resolve with the actions above, since support cannot act on an account.
