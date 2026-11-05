# Checkout Outage Postmortem: Slide Outline (25 min)

**Structure:** Lead with the answer for the execs, then give the engineers the detail, then return to the decision. Plan about 18 minutes of content and 7 minutes of Q&A. Most of the room's attention is gone after minute 20, so the ask should land by about minute 17.

---

**1. Title and bottom line (0:45)**
- One slide with three lines:
  - "Checkout was down 2h40m on Saturday [date]."
  - "Cause: a config change to the payment service connection pool."
  - "We're asking for 2 engineers for 1 quarter to make this class of failure much less likely."
- Execs get the shape of the whole talk up front, and engineers know the detail is coming.

**2. Impact (1.5 min)**
- Big numbers: 2h40m, orders failed or lost, estimated revenue, customers affected, support tickets, any SLA or partner consequences.
- Say plainly that it was a Saturday and what that did to detection and response.
- *Fill in:* the revenue figure needs to come from finance before Thursday. The CFO will ask, and a number you got from them is safer than one they have to question.

**3. Timeline (3 min)**
- A horizontal visual timeline with 6–8 events, not a table. Include:
  - Config change deployed
  - First symptom
  - First alert, or first customer report
  - Page acknowledged
  - Wrong hypotheses (one line each)
  - Root cause identified
  - Rollback or fix applied
  - Full recovery confirmed
- Use real timestamps and show elapsed time from the change.

**4. Where the 2h40m went (1.5 min)**
- A single stacked bar: time to detect, time to diagnose, time to fix, time to recover.
- This is the most useful slide for both audiences. It shows whether the problem was prevention, detection or response, and it sets up the fix.
- *Fill in:* if detection or diagnosis dominated, say so. It shapes what you propose.

**5. Root cause (3 min)**
- A simple diagram of the payment service, its connection pool and the database, with the changed parameter highlighted.
- Show before and after values, and explain the mechanism: why that value caused checkout to fail (pool exhaustion, timeouts, retry amplification, or whatever it was).
- Keep it to one diagram and a few bullets. Put deeper detail in the appendix for engineers who want it.

**6. Why it got through (2 min)**
- Contributing factors as a short list of system gaps, each phrased as a missing safeguard:
  - Config changes bypass the review or testing that code gets.
  - Staging doesn't reproduce production load.
  - No canary or gradual rollout.
  - No alert on pool saturation.
  - No fast rollback path.
- Frame it as blameless. Never name the person who made the change. The room will be watching how you treat them.
- Keep only the gaps that really applied.

**7. What went well (45 sec)**
- Two or three real items, such as the on-call response, cross-team coordination or customer communication. It's brief, but it keeps the talk from feeling like a pure indictment.

**8. Will it happen again? (1.5 min)**
- This is the execs' first question, so answer it directly.
- Split it in two:
  - **This exact failure:** already fixed, with the immediate remediation (e.g., config reverted, guardrail added). State what's done.
  - **This class of failure** (an unsafe config change reaching production): yes, it could recur today unless we close the gaps from slide 6.
- Don't hedge and don't overpromise. "We've fixed the instance, and the class is still open" is credible.

**9. Proposed fix (2.5 min)**
- Three workstreams that map one-to-one to the gaps on slide 6, for example:
  1. Safe config rollout (validation, review and staged deploys for config)
  2. Detection (saturation alerts and checkout-health alerting that pages in minutes)
  3. Fast recovery (one-step rollback and a runbook)
- For each one, give the outcome and which part of the 2h40m it shrinks.

**10. Cost and tradeoff (2 min)**
- Cost: 2 engineers × 1 quarter. Convert it to a dollar figure, and name what those engineers would otherwise work on. The VP of product will care about that.
- Compare it with the cost of the outage (slide 2) and with the expected cost of recurrence.
- Note anything you considered and cut, to show the scope is deliberate.
- *Fill in:* the opportunity cost and the loaded cost per engineer. Don't leave these for the Q&A.

**11. Milestones and how we'll know (1 min)**
- Three checkpoints (30/60/90 days), each with a measurable outcome, such as "config changes go through staged rollout" or "detection under 5 minutes in a game-day test."
- Promise a check-in to the execs at the end of the quarter.

**12. The ask (45 sec)**
- One slide with the decision: approve 2 engineers starting [date]. Name who owns it.
- Close here, then open the floor.

**13. Q&A (about 7 min)**
- Leave the ask slide up while you take questions.

**Appendix (not presented):** detailed logs and graphs, full config diff, extended timeline, and the alternatives considered. Engineers will ask for these, and having them ready saves you.

---

**Rehearsal notes**
- Expect the CFO to ask for revenue and what happens if you don't fund this. The CEO will likely ask whether it can happen again, and the VP of product will ask what gets delayed.
- If you run long, cut slide 7 and compress slide 6. Don't cut slide 4 or slide 8.
- Slide 3 is the one most likely to start a debate among engineers about what happened when. Decide in advance how much you'll take in the room and how much you'll defer to after the meeting.

If you share the actual timeline, root-cause details and numbers, I can draft the slide text and speaker notes.
