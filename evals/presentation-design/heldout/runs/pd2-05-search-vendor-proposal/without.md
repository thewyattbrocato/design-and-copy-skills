# Slide outline: Replace in-house search with a hosted vendor
15 minutes works out to about 7 content slides, with the last 5 minutes left for discussion.

**1. Title and the ask**
- "Proposal: move search to a hosted vendor"
- Put the decision up front: "I'm asking Priya for a decision on starting a migration plan, not for a final commitment today."

**2. Where search stands today**
- In-house p95 latency is 420 ms.
- About 2.5 engineers' time per year goes to maintenance.
- One enterprise customer complained twice last quarter about result quality.
- Keep this slide factual, with no judgment yet.

**3. Vendor trial results**
- Chart: p95 of 420 ms in-house vs 180 ms vendor, on the same queries. That's about 57% lower.
- Add a footnote with the trial's query count, date range, and load, so the room can't dismiss it.
- Say plainly that this is a trial, not production traffic.

**4. Cost: what we spend vs what we'd pay**
- Left side: 2.5 engineers/year × fully loaded cost per engineer = **[fill in]**. Get this number from finance or your manager. Don't guess it.
- Right side: $96k/year vendor quote, plus one-time migration effort and any overage or tier terms.
- Include migration cost, or the four builders will raise it for you.

**5. Customer impact**
- State the facts only: one enterprise customer, two complaints, last quarter.
- Be careful here. Two complaints from one customer is a signal, not proof. Before the meeting, check whether those complaints were about relevance, latency, or something else. Only claim the vendor fixes them if the trial showed it.
- If you can, run the complained-about queries through the vendor trial and show the results.

**6. Risks and what we give up**
- Vendor lock-in and exit plan.
- Loss of custom ranking or tuning, if any exists today.
- Data and security review.
- Migration timeline and risk.
- This slide matters most for the engineers in the room, so lead with their concerns.

**7. Proposed path and the decision**
- Concrete next step, for example: 4-week production-traffic pilot, with go/no-go criteria set in advance (p95 under X ms, relevance parity on a query set, total cost under Y).
- What the 2.5 engineers would work on instead. Name it if you can.
- The ask: "Approve the pilot."

**Backup slides (don't present)**
- Trial methodology.
- Detailed cost model.
- Vendor feature comparison.

## Notes on your material

- **Drop the renting-vs-owning analogy, or keep it to one spoken sentence.** It's a weak fit. A house usually appreciates and renting is usually the pricier option, so it can argue against you. It also casts the four builders' work as something to get rid of. The cost and latency numbers make the case better.
- **Credit the in-house team.** You could say "this service got us here, and the question is where those 2.5 engineers' time is best spent." The builders are the people most likely to sink the proposal, so recruit them. You could also ask one of them to review the trial methodology before the meeting.
- **The cost slide will carry the decision.** If 2.5 engineers cost more than $96k, which is likely, the argument is strong. But it only holds if the freed-up time actually goes to other work. Otherwise the vendor fee is added cost.
- **Latency alone may not matter.** Check whether 420 ms causes any user-visible problem. If it doesn't, the 180 ms result is a nice-to-have, not a reason.

I can write speaker notes with timing for each slide, or draft the cost slide once you have the loaded-cost number.
