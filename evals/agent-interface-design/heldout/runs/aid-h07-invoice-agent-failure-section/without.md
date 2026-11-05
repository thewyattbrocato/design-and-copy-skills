# When it goes wrong

## What Nudge does that can't be undone

Nudge sends email to a freelancer's clients, from the freelancer's own address. **A sent email cannot be recalled.** Everything below follows from that.

## Controls the freelancer has

| Control | Effect | Limit |
|---|---|---|
| Stop a scheduled reminder | That reminder does not send. | Only until 15 minutes before its send time. |
| Pause a client | No reminders go to that client. | Applies to the client, not to a single invoice. |
| Mark an invoice as paid | Cancels all remaining reminders for that invoice. | None. It works at any time. |

Reminders go out 3, 10 and 21 days after the due date unless the client is paused.

## Known failure: reminder for an already-paid invoice

**What happens:** A client pays by bank transfer and the freelancer has not marked the invoice paid. Nudge doesn't know the invoice is settled, so it can send a reminder for it.

**How often:** 3 times across 40 beta accounts.

**Why it can't be fully prevented today:** The only signal Nudge has that an invoice is paid is the freelancer marking it paid. If they haven't, the reminder goes out on schedule. Once it has sent, it can't be recalled.

**What limits the damage:**
- The freelancer can stop a scheduled reminder up to 15 minutes before it sends.
- Marking the invoice paid cancels all later reminders, so one wrong reminder doesn't become three.

## The reminder log

Every reminder is logged with:
- the text that was sent
- the time it was sent
- the reason it was sent

For a wrongly sent reminder, the log shows exactly what the client received and why Nudge sent it. Use it to confirm whether the invoice had been marked paid at send time.

## What support can and can't do

- **Can:** read the log.
- **Cannot:** edit, resend or cancel anything on a freelancer's behalf.

So support can confirm what was sent and why. Any action, such as stopping a reminder, pausing a client or marking an invoice paid, has to be taken by the freelancer.

## Open gaps

- **No apology or credit policy exists yet.** Support has no approved wording or remedy to offer when a client got a reminder for an invoice they had already paid. This needs a decision before wider release.
- Nothing in the current design lets Nudge detect a bank-transfer payment on its own. The beta failure above is a known limitation, not a bug awaiting a fix.
