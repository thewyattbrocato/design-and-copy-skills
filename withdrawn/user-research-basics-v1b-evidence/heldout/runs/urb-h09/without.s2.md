**Lead with a ranked list of what to fix and who owns it, not a walk through the test.** Teams act when they see a prioritized list with a clear ask, so don't order the findings by task flow.

## Suggested structure (about 10 minutes)

**1. One-slide summary**
- One sentence: "Seat selection is the main problem. It cost two people the wrong ticket and blocked our screen reader user entirely."
- A table of 3 to 4 fixes with severity and a proposed owner. This is the slide people will photograph.

**2. Ranked findings, one slide each for the top items**

| Tier | Finding | Evidence |
|---|---|---|
| **Critical** | Seat picker: availability unclear | 4/5 confused, 2 bought the wrong deck |
| **Critical** | Seat selection inaccessible | Screen reader user couldn't complete it |
| **High** | Card entry error | 1/5 abandoned. Check logs to see if it's reproducible |
| **Medium** | Promo code is easy to miss | 3/5 missed it, 1 said they'd have used one |
| **Medium** | Terminal map link is easy to miss | 2/5 missed it, both first-time visitors |
| **Low** | Date picker month error | 1/5, self-corrected |
| **Low** | Home screen colors "a bit dull" | 2/5, opinion only, no behavioral impact |

Treat the two seat-picker items as one story on one slide, since they're the same screen. For each top item, use the same format:
- **What happened:** a 15-second clip or a direct quote.
- **Why it matters:** wrong ticket, lost sale, or excluded user.
- **Recommended fix:** one concrete proposal.
- **Owner and next step.**

**3. What's working**
The confirmation page had 5/5 success, so say "don't touch this." It builds credibility and keeps people from redesigning things that work.

**4. Close with asks**
Name a decision for each critical item, such as "Design to propose a new availability treatment by [date]." End on that, not on a recap.

## Tips
- **Show counts ("4 of 5"), not percentages.** With 5 people, percentages overstate precision. Say once that this is directional, not statistical.
- **Don't dismiss single-user issues.** The payment error and the screen reader failure are blockers, so severity matters more than frequency. Frame the payment one as "needs engineering to check logs," not as proof of a widespread bug.
- **Segment the map link finding.** "Both misses were first-time visitors" points to a specific audience, and that's your likely target.
- **Keep the color feedback low.** It's taste, not behavior. If you mention it, pair it with a contrast check so it doesn't turn into a debate.
- **Put the rest in an appendix.** The date picker and any other minor items can go there for people who want completeness.
- **Use video.** A 15-second clip of someone buying the wrong deck persuades more than any slide text.

I can draft the summary slide or the seat picker slide if you'd like.
