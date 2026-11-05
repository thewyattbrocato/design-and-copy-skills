# How to lay out the Monday readout

Lead with what you want decided, not with the order the tasks appeared in the session. Product teams act when each item has a severity, a count, and a named decision.

## Slide 1: The headline (one slide)
> "In a 5-person task test, the seat picker was the main problem. It caused two wrong-deck purchases and blocked our screen-reader participant. Everything after checkout worked."

Add one line on the sample: 5 people, one at a time, doing real tasks. Say who they were and what's missing from the group. I don't have that detail, so fill it in yourself: `[who they were / how recruited]`.

## Slide 2: Ranked findings table
Sort by severity, then by how central the task is. Don't sort by count alone. Use this format:

| # | Task | Hit | What happened | Severity |
|---|------|-----|---------------|----------|
| 1 | Seat picker | 4 of 5 | Couldn't tell which seats were available; 2 bought the wrong deck | **Blocks**, with a money consequence |
| 2 | Seat picker (screen reader) | 1 of 1 screen-reader user | Couldn't complete seat selection at all | **Blocks**, an access barrier |
| 3 | Card payment | 1 of 5 | Error on card entry; abandoned the task | **Blocks**, but a single case (lead) |
| 4 | Terminal map link | 2 of 5 | Missed it; both were first-time visitors to the port | Slows |
| 5 | Promo code field | 3 of 5 | Didn't notice it; 1 said they'd have used one | Slows |
| 6 | Date picker | 1 of 5 | Chose the wrong month, noticed, fixed it | Annoys |

Findings 1 and 2 are the same screen. Show them as 1a and 1b so the team sees one fix area, not two unrelated tickets.

## Slide 3: One slide per top finding (seat picker, payment)
Use the same four parts each time:
1. **What we saw:** a short clip or screenshot, plus the n of N.
2. **Why it matters:** wrong-deck purchases mean refunds, support contacts, and an unhappy traveler. Add real figures only if you have them: `[refund/support data to collect]`.
3. **What we don't know yet:** for example, what exactly the payment error was.
4. **Decision requested:** an owner and a date. For example: "Seat picker redesign goes into the next sprint. Owner: ___."

## Slide 4: Worked / don't touch
- Confirmation page: 5 of 5 found their ticket without trouble.

This earns trust and stops people from reworking something that's fine.

## Slide 5: Parked, and what's still unknown
- **Home screen colors** ("a bit dull," 2 of 5): this is a preference, not a usability problem. Nobody failed a task. Park it and don't put it in the ranked table.
- **Promo code:** one person saying they'd have used one is a weak signal. Check how often codes are redeemed in your analytics before deciding how much it matters.
- **Payment error:** check your payment logs for card-entry errors. That will tell you whether it was a one-off or a real bug, and it costs little.
- **Screen reader:** n=1 can't tell you how common the problem is, but a task that can't be completed is a real barrier. Don't wait for a bigger sample before fixing it.

## Slide 6: Next steps
Say which fixes come first, and propose retesting them with new participants (3 to 5) after the changes ship.

## Presenting tips
- **Use "4 of 5," not "80%."** With five people, percentages overstate certainty. Say once that this is a small test and the counts are directional.
- **Keep findings and fixes separate.** Put the observation on the finding slide and the proposed fix on the decision slide. The team can then disagree about solutions without disputing what happened.
- **Show, don't summarize.** A 20-second clip of someone choosing the wrong deck will do more than the slide text.
- **Bring a one-page version** of the table for people who weren't in the room.

## What you need to do before Monday
- Fill in the participant description and any cost data. I haven't invented either.
- Pull the 20-second clips for the seat picker and the payment error.
- Put names on the decisions. Without an owner, nothing on slide 3 will happen.
