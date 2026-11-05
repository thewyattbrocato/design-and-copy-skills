**Plan:** 25 minutes, with 9 content slides in about 20 minutes and 5 for questions. There's no agenda or title slide, and the first slide opens on the verdict.

**Takeaway:** A single config change took checkout down for 2h40m because nothing could catch it. Two engineers for one quarter close that gap.

**Audience action:** The execs approve the staffing. The engineers adopt the new config-change safeguards.

## Slides

| # | Claim title | On screen | Time |
|---|---|---|---|
| 1 | **A config change took checkout down for 2h40m. Two engineers for one quarter keeps it from happening again.** | A big "2h 40m" and the ask in one line. Spoken preview: what happened, why it can recur, what it costs to stop it. | 1.5 min |
| 2 | **Checkout was down 2h40m on a Saturday, and it cost us [$ revenue, from finance].** | Two or three numbers: lost orders, revenue, support tickets. Use only figures finance has confirmed. | 1.5 min |
| 3 | **Most of the 2h40m went to [finding the cause / rolling back], not to the fix.** | One horizontal timeline with 4–5 marked events: change deployed, first failure, alert, cause found, recovery. The longest stretch is highlighted. The detailed log goes in the appendix. | 4 min |
| 4 | **A connection pool setting change exhausted the payment service under Saturday load.** | One diagram: old value → new value, and what happened to requests. Say it in blameless terms: the system allowed it. | 3 min |
| 5 | **Nothing between the change and production could catch it.** | Three gaps, a few words each, such as no review of config, no staging at load, no rollback trigger. Confirm these against the actual findings. | 2 min |
| 6 | **It will happen again unless config changes get the same safeguards as code.** | One number: [N] services share this unguarded path. This answers the execs' first question directly. | 2 min |
| 7 | **Three safeguards close the gap: validate, roll out gradually, roll back automatically.** | Three icons or short labels in the order a change moves through them. Name the detection time target you'll commit to. | 3 min |
| 8 | **The fix costs two engineers for one quarter. The outage cost [$X] in one afternoon.** | Two figures side by side: the cost of the work (loaded cost of 2 engineers × 1 quarter, from finance) and the outage cost from slide 2. Add what the team isn't building that quarter. | 2 min |
| 9 | **Decision needed: approve two engineers for Q[X]. Owner: [name]. Decision by: [date].** | The ask, the first milestone, and the takeaway line. It stays up during questions. | 1 min |

## How the room is served
- **Execs:** They get the verdict, the cost and the ask in slide 1. Slides 6 and 8 answer "will it happen again?" and "what does it cost?" in plain terms.
- **Engineers:** Slides 3–5 carry the timeline and root cause. This is the longest stretch, since it's their main interest.
- **Order:** The deck leads with the ask instead of following the chronology. The timeline comes after the audience knows why it matters.

## Backup slides after slide 9 (for the hardest questions)
1. Why did detection or rollback take as long as it did?
2. Who approved the change? (Answer: the process allowed it, and here's what changes.)
3. Why two engineers for a quarter, and what do we get if it's one engineer or half the time?
4. What else is exposed, and what's the customer or refund fallout?

## Appendix
- Full incident log
- Config diff
- Safeguards project plan

## If you lose time
Cut in this order: merge slide 2 into slide 1, then fold slide 5 into slide 7. Slides 6, 8 and 9 stay, because they are what the execs came for.

## Placeholders to fill
I have not invented any figures. The bracketed items need real numbers from finance, the incident review and the project plan. Slide 5's gaps and slide 7's safeguards are my guess at the likely shape, so swap in what your review actually found.
