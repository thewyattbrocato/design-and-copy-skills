# Postmortem outline: Checkout outage (25 min)

**Structure:** Put the exec answer first, then give engineers the detail, then return to the ask. The execs get their answer in the first 2 minutes. The engineers get 10+ minutes of substance. The ask lands when everyone is still paying attention.

Aim for about 20 minutes of content and 5 minutes of Q&A. Bracketed items are numbers you need to fill in.

---

### Part 1: Bottom line (0:00–3:00)

**1. Title and one-sentence summary (0:30)**
- "On [date], checkout was down for 2h 40m. A config change to the payment service's connection pool caused it. We're proposing a fix that takes 2 engineers for 1 quarter."
- Blameless framing in the subtitle.

**2. Impact (1:00)**
- Big numbers only: 2h 40m down, [failed orders], [revenue lost], [customers affected], [support tickets].
- Saturday, so say whether it was peak or off-peak traffic.
- The CFO and CEO will anchor on this slide. Make the figure defensible and say how you calculated it.

**3. Answers up front (1:30)**
- *Will it happen again?* Give a direct answer, e.g. "This specific failure: no, already fixed. This class of failure: yes, until we do X."
- *What does it cost to stop it?* 2 engineers × 1 quarter, vs. [cost of this outage].
- "The next 20 minutes show the evidence."

### Part 2: What happened (3:00–11:00)

**4. System context (1:00)**
- One diagram: checkout → payment service → connection pool → payment provider/DB.
- Circle the component that failed. Engineers need this to follow the rest, and execs need it to see why one config line could stop checkout.

**5. Timeline (3:00)**
- A horizontal timeline with 6–8 events: config change deployed, first symptom, first alert, page, diagnosis, wrong turns, rollback or fix, recovery, all clear.
- Mark three durations: **time to detect**, **time to diagnose**, **time to fix**. The 2h 40m has to be decomposed, because that is where the improvement opportunity sits.
- Include the wrong turns. Engineers trust a timeline that shows dead ends.

**6. Root cause (2:30)**
- Exactly what changed (before and after values) and why that exhausted the pool or blocked requests.
- Show a graph if you have one, such as pool utilization or error rate with the deploy marked.
- Keep it to one idea. Put the deep detail in an appendix slide.

**7. Why it wasn't caught (1:30)**
- The contributing factors, framed as system gaps, not people. For example: no review requirement on config changes, no staging parity, no canary, no alert on pool saturation, a runbook that didn't exist.
- Title it something like "Five things that had to be true for this to happen." This is the bridge to the fix.

### Part 3: What we're doing (11:00–19:00)

**8. What's already done (1:00)**
- Immediate remediations completed: the config reverted, any guardrails already added.
- This shows momentum and sets up "and here's what remains."

**9. Proposed fix (3:00)**
- 3 or 4 workstreams, each mapped to a gap from slide 7. Examples: config changes go through the same safe-deploy path as code (validation, canary, auto-rollback); saturation alerting; load testing the pool settings.
- For each: the failure it prevents and the deliverable.

**10. Cost and timeline (2:00)**
- 2 engineers, 1 quarter, with milestones by month.
- State what those engineers are not working on, i.e. the opportunity cost. The VP of product will ask, so answer it first.
- Compare with the cost of the outage, and with the expected cost of recurrence if you can estimate it.

**11. What we get and what we don't (1:30)**
- The expected improvement in terms execs care about: e.g. detection time from [X] to [Y], and this class of change can no longer reach production unreviewed.
- Be honest about residual risk. "This won't prevent all outages" builds credibility.

**12. How we'll know it worked (1:00)**
- Two or three measurable outcomes and a date to report back.

### Part 4: Close (19:00–25:00)

**13. The ask and decisions needed (1:00)**
- "Approve 2 engineers for Q[X]." Name who decides, and by when.
- Anything you need from the engineering org at large, such as adopting the config-change process.

**14. Q&A (4+ min)**
- Leave this slide up with the summary: cause, cost, ask.

### Appendix (don't present; use for questions)
- A. Detailed technical timeline with log and metric excerpts
- B. Config diff and the connection pool mechanics
- C. Alternatives considered and why you rejected them (the CFO may ask "why not something cheaper?")
- D. Customer and revenue impact methodology

---

## Notes for delivery

- **Slide 3 is the most important slide for the execs.** If they leave after that slide, they should still have what they need.
- **Spend the time on slides 5 and 7.** Engineers care most about the timeline and the contributing factors. Be quick on slide 4 if people know the architecture.
- **Likely exec questions:** "Why did it take 2h 40m?", "Could this happen on another service?", "Why 2 engineers and a full quarter?" The first is covered by the timeline durations. For the second, have an answer ready on whether other services share the same config-change gap. For the third, break down the workstreams by effort.
- **Likely engineer questions:** "Why didn't we roll back sooner?" and "Who approved the change?" Rehearse blameless answers focused on process.
- **Check your pacing.** 14 slides in 20 minutes is comfortable, but slides 5 and 9 will run long if you let them. Practice with a timer once.

If you give me the actual numbers and the config details, I can draft the text for any slide, including the talking points for slide 3 and the cost comparison on slide 10.
