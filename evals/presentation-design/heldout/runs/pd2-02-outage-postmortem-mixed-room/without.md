# Checkout Outage Postmortem: Slide Outline (25 min)

**Approach:** Put the execs' answers up front (will it recur, what does it cost), then give engineers the depth, then close on the ask. The execs may have to leave early, and engineers will sit through the answer anyway. Aim for 12 content slides at about 2 minutes each, with a few minutes of buffer for questions.

---

### Opening (3 min)

**1. Title and bottom line (1 min)**
- "Checkout outage, [date]: what happened, why, and what we're doing about it."
- One-line summary: *A config change to the payment service's connection pool took checkout down for 2h40m. We can prevent a repeat with 2 engineers for 1 quarter.*

**2. Customer and business impact (2 min)**
- Big numbers: 2h40m down, Saturday, [failed orders], [estimated revenue lost], [support tickets], [customers affected].
- Use real figures, even if approximate. The CFO will anchor on them, and this slide sets up the cost comparison later.
- Say plainly that it's blameless and about the system, not a person.

### Engineer section (10 min)

**3. Timeline (3 min)**
- A horizontal timeline, not a table: change deployed → first symptom → alert fired (or didn't) → page → diagnosis → mitigation → recovery.
- Mark **time to detect**, **time to diagnose**, and **time to fix** as separate intervals. They show where the 2h40m went and support the fix later.
- Include the Saturday factor: who was on call, how long it took to get the right people.

**4. Root cause (3 min)**
- Show the specific change as a before/after diff (pool size, timeout, or whatever it was).
- Explain the mechanism in a 3–4 step diagram: change → pool exhausted → payment calls queue/time out → checkout fails.
- Say why it wasn't obvious.

**5. Why it wasn't caught (2 min)**
- The "five whys" condensed to three or four contributing factors, for example:
  - The change had no review or validation gate.
  - Staging doesn't reproduce production load.
  - The alert was missing or too slow.
  - The rollback path was unclear.
- Frame these as gaps in the system that let a normal change cause an outage.

**6. What went well / what was hard (2 min)**
- Credit specific things that worked (a fast rollback, good communication, whatever is true). It keeps the tone fair and tells engineers what to keep doing.
- Then name what slowed the response.

### Exec section (8 min)

**7. Will it happen again? (2 min)**
- Give a direct answer: "Yes, the same class of failure can recur today. Nothing currently stops a risky config change from reaching production unvalidated."
- Be candid here, because execs trust a clear assessment more than reassurance.
- Add one sentence on how likely and how severe, if you can estimate it.

**8. The proposed fix (3 min)**
- Three or four workstreams mapped to the gaps on slide 5, such as:
  - Config change validation and staged rollout
  - Production-like load testing for the payment path
  - Alerting and faster detection on connection pool saturation
  - Runbook and rollback automation
- For each, show which part of the timeline it shortens or which failure it blocks.

**9. Cost and return (2 min)**
- Cost: 2 engineers × 1 quarter (roughly [X] loaded cost, and say what they're *not* working on).
- Compare it to the outage: [lost revenue per hour] × expected recurrence risk.
- If you can, include what the fix does to detection time and recovery time, as targets.

**10. Delivery plan and milestones (1 min)**
- A simple quarter view with 3–4 milestones.
- Name early wins, such as the alert and the config gate landing in the first few weeks, so risk drops before the full quarter is done.

### Close (3 min)

**11. The ask (1 min)**
- "Approve 2 engineers for Q[X]." State who the decision belongs to (the VP of product, or the CEO and CFO).
- Say what happens if you wait: you keep the current exposure.

**12. Questions (2+ min)**
- Backup slides, not part of the 25 minutes:
  - Detailed metrics
  - Alternatives considered (a cheaper partial fix, and what it leaves uncovered)
  - Full action-item list with owners and dates

---

### Notes for delivery
- **Rehearse slides 3 and 4 hardest.** Engineers will probe those, and you'll lose them if the mechanism is vague.
- **Expect these questions:** "Why wasn't this caught in review?", "Are there other services with the same config risk?", "Why two engineers and not one?", "What if we only do the alert?" Prepare a backup slide for the last two.
- **Alternatives:** Execs usually ask whether there's a cheaper option. Have a "minimum viable fix" ready, with its cost and the risk it leaves.
- **Open items:** I don't have your impact numbers, the exact timeline, or the cost figures. Those are the slides most worth getting right.

If you give me the real timeline and numbers, I can draft the speaker notes or the slide text for any of these.
