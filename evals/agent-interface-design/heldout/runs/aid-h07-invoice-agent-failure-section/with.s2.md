# When it goes wrong

## Why mistakes are visible
Nudge emails a freelancer's clients from the freelancer's own address, so a bad reminder reaches the client under the freelancer's name. A sent email cannot be recalled.

## Controls that exist today
| Control | What it does | Limit |
|---|---|---|
| Stop a scheduled reminder | The freelancer can stop any scheduled reminder. | Only until 15 minutes before it sends. |
| Mark invoice as paid | Cancels all remaining reminders for that invoice. | Works at any time, but only if the freelancer does it. |
| Pause a client | Reminders (3, 10 and 21 days after the due date) are skipped for that client. | The freelancer must set it. |
| Reminder log | Records the text sent, the time and the reason it was sent. | Read-only for support. |

## Known failure: reminder for an already-paid invoice
**What happens:** A client pays by bank transfer, and the freelancer has not marked the invoice paid. Nudge can then send a reminder for an invoice that is already settled.

**How often:** It happened 3 times across 40 beta accounts. That is a count of accounts. We have no per-email rate, and we should not quote one.

**Impact:** The client gets a "you're late" email they don't deserve, from the freelancer's own address. It cannot be recalled.

**What stops it:** The freelancer marks the invoice paid, which cancels all remaining reminders. They can also stop an individual scheduled reminder more than 15 minutes before it sends. Neither happens automatically today.

## What support can and cannot do
- **Can:** Read the log to see what was sent, when, and why.
- **Cannot:** Edit, resend or cancel anything on a freelancer's behalf.

Support can confirm what happened and tell the freelancer how to mark the invoice paid or stop a reminder. Support cannot fix it for them.

## Open items (no decision yet)
- **Apology or credit:** There is no policy. Until one exists, support has nothing approved to offer a freelancer whose client received a wrongful reminder.
- **Prevention of the bank-transfer case:** The beta data shows the failure but not a fix. Product needs to decide whether to address it, and how.
