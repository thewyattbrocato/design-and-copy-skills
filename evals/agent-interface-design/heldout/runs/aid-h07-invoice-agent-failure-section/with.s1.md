# When it goes wrong

## What Nudge does, and why mistakes are visible
Nudge emails clients who are late on invoices, on the freelancer's behalf, from the freelancer's own address. Clients see a reminder as coming from the freelancer, so a wrong reminder is the freelancer's mistake in the client's eyes.

Reminders go out 3, 10 and 21 days after the due date, unless the freelancer has paused that client.

## What can be stopped, and what can't
| Situation | What happens |
|---|---|
| Reminder is scheduled and more than 15 minutes from sending | The freelancer can stop it. |
| Reminder is scheduled and within 15 minutes of sending | It can no longer be stopped. |
| Reminder has been sent | It **cannot be recalled**. |
| Invoice is marked paid, at any time | All remaining reminders for that invoice are cancelled. |
| Client is paused | No reminders go out for that client. |

Marking paid stops future reminders only. It does not undo one that has already been sent.

## Known failure: reminder for an invoice that is already paid
**What happens:** A client pays by bank transfer, and the freelancer has not marked the invoice paid. Nudge can't tell the invoice is settled, so it sends a reminder as scheduled.

**How often:** 3 times across 40 beta accounts.

**Why it matters:** The client is chased for money they have already paid, in the freelancer's name.

**Current mitigations:**
- The freelancer can mark the invoice paid, which cancels all remaining reminders.
- The freelancer can stop an individual scheduled reminder up to 15 minutes before it sends.
- Pausing a client prevents further reminders for that client.

**Not mitigated:** Nudge has no way to detect a bank transfer on its own. Until the freelancer marks the invoice paid, the failure can recur.

## The log
Every reminder is logged with:
- the text sent
- the time it was sent
- the reason it was sent

The log is the source of truth for answering "what did my client receive, and why?"

## What support can and can't do
- **Can:** read the log for a freelancer's reminders.
- **Cannot:** edit, resend or cancel anything on a freelancer's behalf.

Support can confirm what was sent and why. Any action, such as marking paid, stopping a reminder or pausing a client, has to come from the freelancer.

## Not yet decided
- **Apology or credit policy.** There isn't one. Support should not promise credits, refunds or compensation until one exists.
- **Fix for the bank-transfer failure.** No fix is specified. Engineering needs to decide whether to build one and what it looks like.
