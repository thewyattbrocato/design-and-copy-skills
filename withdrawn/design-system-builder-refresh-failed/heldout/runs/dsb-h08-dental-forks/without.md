Mostly no. Enforcing harder is the wrong first move, and it could make things worse.

**What your data says**

- Two teams forked Button and DatePicker. That's rarely defiance. Those are the two components most likely to need real product variation (scheduling flows, date ranges, availability states), and the teams couldn't wait.
- Forty-plus requests, some six months old, means the system is a bottleneck. Forks are what teams do when the official path is slower than the unofficial one.
- Enforcement (lint rules, review gates, mandates) raises the cost of leaving the system but does nothing about why they left. With two people on the system, you'd also become the blocker on every enforced path, which makes the queue longer.

**What I'd do**

1. **Triage the board this week.** Close or merge duplicates, and label every request: *will do*, *won't do (with reason)*, *teams can do themselves*, *needs more info*. A stale "maybe" is worse than an honest "no." I'd expect the 40 to shrink to about 10–15 real items. Tell requesters the outcome either way.

2. **Audit the two forks before judging them.** Diff each against your current component and list what changed. The changes will usually fall into three groups:
   - Real gaps you should absorb into the system, like missing variants or props.
   - One-off needs that can stay local.
   - Things that are just wrong, such as accessibility regressions, which are the real risk in a patient-facing portal.

   Then talk to both teams. Absorbing their changes upstream is the best outcome, because it turns a fork into a contribution.

3. **Make the extension path cheaper than forking.** Add slots, composition points, or a documented "extend, don't copy" pattern for Button and DatePicker. Set a service-level target you can actually hit, such as a response within 5 business days and a decision within 2 weeks. Allow teams to contribute directly, with a lightweight review from you.

4. **Narrow your scope.** With one engineer and a part-time designer, you can't be responsive on everything. Decide which components you own fully (probably the 10–15 most used) and which are "supported, contributions welcome." Publish that.

5. **Add measurement, not mandates.** Track adoption, forks, and request age. Visibility is a mild form of enforcement that doesn't make anyone your adversary.

6. **Then add targeted enforcement where it matters.** That means accessibility and brand-critical or compliance-relevant surfaces, such as patient-facing forms. Light guardrails like a lint rule against deep imports or a CI check for known forks make sense once the supported path is fast enough that they're not punitive.

**What to tell your manager**

Something like: "Enforcement works when compliance is cheap. Right now it isn't, because our backlog is 6 months deep. I'll fix the throughput and the extension path first, bring the two forks back in, and then add guardrails on the things that carry real risk. I'll report on request age and fork count so you can see whether it's working." Bring the numbers. A manager who says "enforce harder" usually wants fewer divergent UIs, and you can give them that with data.

**Caveat**

If a fork turns out to be a deliberate decision by a team that doesn't want the system at all, that's a leadership conversation about whether the system is mandatory. Still, fix your side of the queue first, so the answer to "why didn't they use it?" isn't "because it was slow."

If you can share the board export or the fork diffs, I can help you do the triage or audit.
