# Slide plan (15 min, about 7 slides)

**1. Recommendation: move search to a hosted vendor**
- One sentence: "I'm proposing we replace our in-house search with [Vendor], and I'd like a decision on a migration pilot."
- State the ask now so Priya doesn't have to guess where this is going.

**2. What we'd be comparing**
- Current state: in-house service, p95 latency 420 ms, about 2.5 engineers/year to maintain.
- Proposed state: [Vendor] at $96k/year.
- Say up front that the in-house service works and the team built it well. This matters with its four builders in the room.

**3. Speed: 420 ms vs 180 ms p95**
- A simple two-bar chart, same queries on both.
- Add a footnote on trial conditions: query count, date range, and whether the data volume matched production.
- Expect the builders to probe here, so be ready to answer "was the trial tuned like ours is?"

**4. Cost: $96k/year vs 2.5 engineers/year**
- Put the vendor quote beside the in-house cost expressed in dollars. Use finance's fully loaded cost per engineer, not a guess.
- Add a line for what those 2.5 engineers would work on instead. That is the real argument, because it's capacity, not just savings.
- Include one-time migration cost and any vendor price escalation, or this slide will look one-sided.

**5. Customer impact**
- One enterprise customer complained twice last quarter about search results.
- Be careful with this one. Two complaints from one customer is a thin signal, and the complaints were about result quality, not latency. Include it only if you can show the vendor does better on relevance for those queries. Otherwise move it to a footnote or drop it.

**6. Risks and how we'd handle them**
- Lock-in, and the exit plan if the vendor fails or raises prices.
- Data and security review.
- Relevance tuning control we'd lose.
- Migration effort and timeline.
- Putting the builders' likely objections here, with answers, shows you've taken their view seriously.

**7. Proposed next step**
- A concrete, low-commitment ask, for example a 4–6 week pilot on a slice of traffic with defined success criteria (p95 under X ms, relevance parity on the complaint queries, total cost under Y).
- Name an owner and a decision date.
- Ask the in-house team to help define the success criteria.

**Timing:** about 1 minute each for slides 1–2, 3 minutes each for 3 and 4, 2 minutes for 5, 3 minutes for 6, and 1 minute for 7. That leaves almost no discussion time, so cut slide 5 if you need room.

## Notes on your inputs

- **Renting vs. owning a house:** I'd drop it, or at most use it once in speech and not on a slide. With the builders listening, "owning" implies they built an asset and you're proposing to sell it. It also isn't accurate, since a house usually appreciates and a search service doesn't. The 2.5-engineers figure makes the same point more strongly, and it's a number rather than a metaphor.
- **Missing numbers:** you'll want the loaded engineer cost, migration cost, and the vendor's multi-year pricing. Priya will ask about each of them.
- **Who you're persuading:** Priya decides, but the four engineers will shape how it lands. Consider talking to them before Wednesday so slide 6 isn't the first time they hear the proposal.

If you send me the trial details and the loaded cost figure, I can write the speaker notes and exact slide text.
