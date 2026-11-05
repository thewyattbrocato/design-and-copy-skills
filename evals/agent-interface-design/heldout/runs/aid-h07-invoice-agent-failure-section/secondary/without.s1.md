## When it goes wrong

Nudge sends email on the freelancer's behalf, from the freelancer's own address. Once an email is sent, it cannot be recalled. The freelancer's main control is the window before each send, and the main fix for a settled invoice is marking it paid.

### Controls available

| Control | Who | When it works |
|---|---|---|
| Pause a client | Freelancer | Stops reminders for that client. |
| Stop a scheduled reminder | Freelancer | Any time up to 15 minutes before it sends. |
| Mark invoice paid | Freelancer | Any time. Cancels all remaining reminders for that invoice. |
| Read the log | Freelancer, support | Every reminder is logged with the text sent, the time, and the reason it was sent. |
| Edit, resend, or cancel a reminder | Nobody on the freelancer's behalf | Support cannot do any of these. |

### Known failure: reminder sent for a settled invoice

- **What happens:** A client pays by bank transfer, and the freelancer has not marked the invoice paid. Nudge can still send a reminder for that invoice.
- **Observed:** 3 times across 40 beta accounts.
- **Why it happens:** The invoice is still open in Nudge because the freelancer has not marked it paid.
- **Freelancer action:** Mark the invoice paid. This cancels all remaining reminders for it. A reminder already sent cannot be recalled.
- **Support action:** Read the log to confirm what was sent and when. Support cannot cancel the remaining reminders, edit, or resend anything. Tell the freelancer to mark the invoice paid.
- **Customer-facing remedy:** None yet. There is no apology or credit policy.

### Scenario: client should not have been chased

- **What happens:** A reminder is scheduled for a client the freelancer does not want chased now, and the client is not paused.
- **Freelancer action:** Pause the client, or stop the specific reminder, if it is more than 15 minutes before it sends.
- **If inside the 15-minute window or already sent:** The email cannot be recalled. Support can show the log entry (text, time, reason) but cannot cancel or resend anything.

### Scenario: wrong wording or content sent

- **What happens:** A reminder was sent with text the freelancer did not want.
- **Freelancer action:** None can undo the send. Use the log to see exactly what went out.
- **Support action:** Read the log and share it with the freelancer. Support cannot edit or resend.

### Support runbook (summary)

1. Read the log: the text sent, the time, and the reason.
2. Tell the freelancer which controls they can use (pause, stop before send, mark paid).
3. Do not promise a recall, resend, cancel, edit, apology, or credit. None of these exist yet.

### Open items

- No apology or credit policy yet. Support needs an answer before handling affected beta accounts.
