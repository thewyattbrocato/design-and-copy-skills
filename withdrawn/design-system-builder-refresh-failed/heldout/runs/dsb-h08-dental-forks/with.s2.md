Not as the first move. Enforcement would make your bottleneck worse, and it treats the symptom.

**What the evidence says**

- Two teams forked Button and DatePicker, which are probably your most-used components. They likely forked because they needed something the system didn't offer and the contribution path was too slow. A 6-month-old request queue supports that.
- Enforcing harder (lint rules, blocking merges, mandates) sends more demand through the same two-person queue. Teams will route around it or resent it. Forks that are forbidden tend to go underground.
- The forks are also useful information. Their diffs show what teams needed.

**What I'd do, in order**

1. **Triage the board this week.** Close or decline anything stale or out of scope, with a short reason. Sort the rest into three buckets: bug or accessibility fixes, small additions to existing components, and new components. Publish the result. Even a rough pass shows teams you're listening, and it usually shrinks 40 items to about 15 real ones.
2. **Diff the two forks against your versions.** Sort the changes into "we should adopt this" (likely several), "legitimate variant, make it a prop or token," and "genuinely wrong." Ship the first two as an update. Then migrating back becomes a gain for those teams, not a loss.
3. **Set a response SLA you can keep.** Examples are a first reply within 5 business days and a decision (yes, no, or later, with a reason) within 30 days. A fast "no" is better than a silent six months.
4. **Lower the cost of contributing.** Give teams a lightweight path: a short contribution guide, a PR template, and a promise to review contributed PRs within a set time. Your capacity is two people, so the system can't scale unless others can add to it.
5. **Add guardrails after that.** Once the path works, enforcement becomes reasonable and defensible:
   - Lint or CI checks for imports of local copies of Button/DatePicker.
   - A "no new forks without a filed request" rule.
   - Visibility into adoption (see below).

**What to tell your manager**

"Enforcement works when the official path is faster than the workaround. Right now it isn't, so enforcing first would add pressure with no relief. I'm proposing a 6–8 week plan: clear the backlog, absorb the forks, set an SLA, then add automated guardrails. I'll report adoption and request-age metrics so we can see it working."

Offer numbers they can track: median request age, open requests, and the share of Button/DatePicker usages that come from the shared package. These turn "enforce harder" into something measurable.

**One caveat**

If the forks are in patient-facing flows, check them for accessibility or compliance gaps now. That's a real risk, and it would justify faster, firmer action on those two specifically.

If you can share the board export or the fork repos, I can help you categorize requests or diff the components.
