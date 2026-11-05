## Push notification

**Title:** Approve new flight by {hold_expires}?
**Body:** Your 6:40pm to Boston was cancelled. Best option: United 9:15pm tonight, lands 2:55am. $640, needs your OK.

The title carries the deadline, since that's what makes it urgent. The body says what happened, what the replacement is, and why she's being asked.

## Approval screen

> **Seat held for 28:41** *(live countdown, held until {hold_expires})*
>
> **Your 6:40pm flight was cancelled.**
> Here's the replacement:
>
> **United {flight_no}**
> **9:15pm** Denver (DEN) → **2:55am** Boston (BOS)
> Tonight → arrives {Thu, Nov 5}
>
> **$640**, nonrefundable
> $140 over your $500 auto-approve limit, so it needs your OK.
>
> **[ Approve and book $640 ]** *(primary button)*
> **[ Decline ]** *(secondary button)*
>
> *If the hold runs out, the seat may be released and the price may change.*

## Notes

- **Late arrival:** 2:55am lands the next calendar day, so I put the date on the arrival line. A tired reader could otherwise misread it as "tonight."
- **One decision:** There are two buttons and no flight list. If the agent has other options, "See other options" could replace "Decline," but I'd leave it out until the agent can offer them.
- **Placeholders:** `{hold_expires}`, `{flight_no}` and the date should come from the booking data. The countdown should be computed live, not hard-coded.
- **Open question:** The copy doesn't say what happens if she doesn't respond. Whoever owns the product should decide this: the seat is released, or the agent keeps looking. Then the last line can say it plainly, e.g. "If you don't respond, we'll release the seat and keep looking." I didn't want to invent a policy.
- **Original ticket:** I also left out any mention of a refund or credit for the cancelled flight, since I don't know what the agent has done there. If it's been handled, one line like "Your original ticket is being refunded" would help justify the $640.
