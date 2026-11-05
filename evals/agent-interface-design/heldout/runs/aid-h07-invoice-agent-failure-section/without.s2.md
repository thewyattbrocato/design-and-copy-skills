## When it goes wrong

### What to know first
- Nudge sends from the freelancer's own address, so the client sees every reminder as coming from the freelancer.
- **A sent email cannot be recalled.** Every control below works only before a send.

### Controls that prevent a bad send
| Control | What it does | Limit |
|---|---|---|
| Stop a scheduled reminder | Freelancer cancels that one reminder | Up to 15 minutes before it sends |
| Pause a client | No reminders go to that client at the 3, 10 and 21 day marks | Applies per client |
| Mark invoice as paid | Cancels all remaining reminders for that invoice | Works at any time |

### Known failure: reminder sent for an invoice that is already paid
**What happens.** A client pays by bank transfer and the freelancer has not marked the invoice paid. Nudge can then send a reminder for an invoice that is already settled.

**How often.** It happened 3 times across 40 beta accounts.

**Impact.** The freelancer's client gets a payment chase for something they already paid, and it comes from the freelancer's own address. The email cannot be recalled.

**Mitigation today.** The freelancer can mark the invoice paid, which cancels all remaining reminders. They can also stop an individual reminder up to 15 minutes before it sends. Both depend on the freelancer acting in time.

### What support can and cannot do
- Support **can** read the reminder log. Each entry has the text sent, the time and the reason it was sent. Use it to confirm what a client received and why.
- Support **cannot** edit, resend or cancel anything on a freelancer's behalf. If a reminder is still scheduled, the freelancer has to stop it or mark the invoice paid themselves.

### Handling a report
1. Find the reminder in the log and confirm the text, time and reason.
2. If the invoice is already paid, tell the freelancer to mark it paid. That cancels any remaining reminders for it.
3. Tell the freelancer that the sent email cannot be recalled.

### Open items
- **No apology or credit policy exists yet.** Support has nothing approved to offer a freelancer affected by a wrongly sent reminder. Until one is written, support should not promise compensation. This needs an owner and a decision.
