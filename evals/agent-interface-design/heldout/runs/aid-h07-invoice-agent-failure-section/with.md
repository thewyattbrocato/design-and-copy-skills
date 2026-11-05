# When it goes wrong

## What Nudge does, and why mistakes are visible
Nudge emails late clients on the freelancer's behalf, from the freelancer's own address. Clients see any mistake as coming from the freelancer, not from Nudge.

By default, reminders go out 3, 10 and 21 days after the due date. They don't go out for a client the freelancer has paused.

## What can and can't be undone

| Situation | What is possible |
|---|---|
| Reminder is scheduled, more than 15 minutes before send | The freelancer can stop it. |
| Reminder is scheduled, within 15 minutes of send | It can no longer be stopped. |
| Reminder has been sent | It cannot be recalled. |
| Invoice is marked paid (at any time) | All remaining reminders for that invoice are cancelled. Reminders already sent stay sent. |

## Known failure: reminder sent for an invoice that is already paid
**What happens:** A client pays by bank transfer, and the freelancer hasn't marked the invoice paid in Nudge. Nudge can still send a reminder for the settled invoice.

**How often:** This happened 3 times across 40 beta accounts.

**Why it matters:** The client gets a payment demand for money they've already paid, and it appears to come from the freelancer personally. Once sent, the email can't be recalled.

**What limits the damage:**
- Marking the invoice paid cancels every remaining reminder, so one mistaken email shouldn't be followed by the later ones.
- A freelancer who notices a scheduled reminder for a settled invoice can stop it, if there are more than 15 minutes before it sends.

## The log
Every reminder is logged with the text sent, the time, and the reason it was sent. The log is the source of truth for answering "what did my client receive, and why?"

## Who can do what

**Freelancer:** Can pause a client, stop a scheduled reminder (up to 15 minutes before send), and mark an invoice paid.

**Support:** Can read the log. Support cannot edit, resend or cancel anything on a freelancer's behalf. For a wrong-reminder report, support can confirm what was sent, when, and why. Any stopping or marking-paid has to be done by the freelancer.

## For engineers
- Nothing in the current design checks whether a bank-transfer payment has arrived. Only the freelancer marking the invoice paid cancels reminders.
- The 15-minute cutoff is a hard line. Anything inside it is treated as sent.
- Each reminder's log entry must include the reason it was sent. This is what support relies on when a client complains.

## Open: no apology or credit policy
There is currently no policy for apologizing to a freelancer or compensating them after a mistaken reminder. Until one exists, support has nothing approved to offer beyond explaining what happened from the log. Product and the support lead need to decide this before wider launch. Support should not improvise offers in the meantime.
