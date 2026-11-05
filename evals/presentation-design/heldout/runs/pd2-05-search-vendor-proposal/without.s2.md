# Draft deck: replace in-house search with a hosted vendor (15 min, about 7 slides)

**1. Title: "Search: should we keep building it or buy it?"**
- Use this framing instead of "replace our search service". It's a question for the room to decide, and it's less defensive for the four engineers.
- Put the ask on this slide: "Decision needed today: approve a [N]-week migration pilot."

**2. "Where search stands today"**
- p95 latency is 420 ms.
- One enterprise customer complained twice last quarter about result quality.
- Maintenance takes about 2.5 engineers' time a year.
- Keep it to facts. Say what the in-house team built that works, so they hear you acknowledge it.

**3. "Vendor trial: same queries, less than half the latency"**
- Show a simple two-bar chart: 420 ms vs 180 ms p95.
- Add a footnote with the trial's query count, duration, and load conditions.
- Be ready for the engineers to ask whether the trial matched production traffic. Have that answer ready.

**4. "What it costs each way"**
- Left column: in-house, 2.5 engineers a year × your fully loaded cost per engineer (get this number from finance).
- Right column: vendor, $96k a year, plus one-time migration cost.
- Add one line on what those 2.5 engineers would work on instead. The savings only count if that time goes to real roadmap work.

**5. "Customer impact"**
- Describe the two complaints: what the customer said, and whether the vendor trial fixes it.
- Don't oversell it. Two complaints from one customer is a signal, not a trend. If you can show the vendor handles their specific queries better, that's much stronger.

**6. "Risks and how we handle them"**
- Cover lock-in and an exit path, relevance tuning control, data security and compliance, vendor price increases, and migration risk.
- Pre-empt the engineers' likely objections here. A slide that names the risks is more credible than silence.

**7. "Proposal and next steps"**
- Propose a time-boxed pilot on a share of traffic, with success criteria set up front (for example, p95 under 200 ms and no relevance regressions).
- Name who owns it, and suggest putting a member of the in-house team in charge of the evaluation.
- Show the decision date and what happens if the pilot misses.

## Things to reconsider

- **The rent-vs-own analogy.** I'd drop it from the slides. Priya may find it intuitive, but the engineers will hear "your work is a mortgage". It also doesn't fit well, because renting usually costs more over time, which undercuts your cost case. If you want a framing, use "what should our engineers spend their time on?"
- **The cost comparison is your strongest point, but it's incomplete.** $96k against 2.5 engineers is lopsided, so make sure the loaded-cost number is on the slide. Also include migration cost and ongoing integration work, or the in-house team will raise them for you.
- **Gaps in your notes.** You don't have result-quality data beyond the complaints, migration effort, or an exit plan. Priya will likely ask about all three, so I'd fill them in before Wednesday.
- **Timing.** At 15 minutes, aim for about 8 minutes of presenting and 7 for discussion. This audience will want to push back.

I can also write speaker notes for each slide, or draft answers to the questions the four engineers are most likely to ask.
