**15 minutes, 6 slides (about 10 minutes of talking, 5 for discussion). Takeaway: replacing the in-house search with the vendor gives us faster results for less than the engineer time we spend now, and I'm asking Priya to approve it.**

The four engineers who built the current service are in the room, so I've put their strongest reason before the evidence. Priya decides, so the last slide is written for her.

**Slides**

1. **"We need search that's fast, good for customers, and cheap to keep running"** (~1.5 min)
   - Three criteria on screen: speed, customer impact, cost in engineer time.
   - Say aloud that you'll judge both options on those three, and that migration detail is in the appendix.

2. **"The in-house service is ours: we control it and it fits our product"** (~1.5 min)
   - This is the builders' best case. Check the wording with one or two of them before Wednesday, so they'd sign it.
   - Keep it to 2–3 short phrases, such as control, product fit and no vendor dependency. I don't know their actual argument, so these are placeholders.

3. **"On the same queries, the vendor answered in 180 ms and ours takes 420 ms"** (~2 min)
   - One visual: two bars, p95 latency, in-house 420 ms against vendor 180 ms.
   - Add a small caption with the number of queries and the trial dates: [N queries, dates].
   - Confirm the 180 ms is also a p95. Otherwise the comparison isn't like for like, and the engineers will notice.

4. **"An enterprise customer has already complained about search twice"** (~1.5 min)
   - One line: "Two complaints, one enterprise customer, last quarter."
   - This is one case. It shows search can hurt us, not that it's typically bad, so keep the title and your spoken line to that.

5. **"The vendor costs $96k a year; keeping ours costs 2.5 engineers"** (~2 min)
   - Two figures side by side: $96k/yr and 2.5 engineers/yr, plus [loaded cost per engineer] so the room can compare them. I don't have that number, and the slide needs it.
   - Add a spoken line on what those engineers would work on instead: [project].

6. **"Decision: approve the vendor, with migration owned by [name], done by [date]"** (~1 min, stays up for discussion)
   - One line of recap: faster, cheaper in engineer time, and a customer already affected.
   - Ask, owner and date: Priya approves, [owner] leads, [date].

**Appendix (backup slides for the likely hard questions)**
- Migration effort and timeline.
- Lock-in and how we'd exit.
- Result quality on our real queries, beyond speed.
- Trial method and sample size.
- What happens to the 2.5 engineers' time.
- What happens if the vendor raises prices after year one.

**On the renting vs. owning analogy:** I'd drop it from the slides. To these engineers, "owning" sounds like their work is the house, and "renting" invites the reply that renting costs more over the long run. If you keep it, use it as one spoken line on slide 5, with the numbers right beside it. Your evidence is the latency, cost and complaint figures.

**Assumptions:**
- I assumed the builders oppose the change, so I ordered the deck to hear them out first. If they're neutral, move slide 6's verdict up to the opening.
- I used none of the numbers beyond the ones you gave. The bracketed items are gaps for you to fill.
