# Supervisor screen for 35 claims agents

A grid of 35 equal tiles shows the supervisor mostly healthy agents. They only need to see the few that need them, and the tiles give no reason, urgency or action for those. Design for management by exception: the screen should answer "who needs me, why, and what's the fastest way to clear them?"

## Layout

**1. Attention queue (about 60% of the screen, the main element)**
A ranked list of every agent that's blocked, one row each. Each row shows:
- **Reason**, as a typed label: *Unreadable document*, *Ambiguous policy rule*, or *Over $25k sign-off*.
- **Time waiting**, because it drives the ranking.
- **A one-line question in plain language.** For example: "Page 3 of the contractor estimate is blurred. Can I proceed using the summary total?" This is more useful than a claim number.
- **The claim's dollar value and any deadline**, such as a statutory response date.
- **The agent's proposed default**, where it has one, so the supervisor can approve with one click.

**2. Fleet summary strip (top, slim)**
Counts only: working, blocked (split by the three reasons), finished this shift, and throughput against target. A rising "ambiguous policy" count is a signal in itself, and a plain count shows it better than 35 dots.

**3. Quiet roster (bottom or side, compressed)**
The healthy agents shrink to a dense row of small dots or a sortable table. It's there for reassurance and drill-down, and it shouldn't compete for attention. Agents that are slow but not blocked, such as one far over its usual time on a claim, get a subtle "at risk" marker. That catches problems before they turn into stuck states.

**4. Detail pane (opens on selecting a row)**
It shows the thing the agent is stuck on beside the agent's reasoning: the document image, the policy clause, or the recommendation summary. The supervisor shouldn't have to open another system to decide.

## When five or six agents are stuck at once

1. **Order the queue by consequence.** Sort by deadline risk, then dollar value, then time waiting. Don't use a plain first-in-first-out order.
2. **Batch by cause.** Group the queue by blocker type, because each type has a different fix:
   - **Ambiguous policy rule:** Often several agents hit the same clause. Let the supervisor write one ruling and apply it to every matching claim. Store the ruling so later agents don't get stuck on the same clause. Check that each claim really matches before applying it.
   - **Unreadable document:** Offer bulk actions, such as "request re-upload from policyholder" and "continue without it and flag". Send them in one step for all affected claims.
   - **Over $25k sign-off:** Route these to whoever holds the authority. This may not be the supervisor. Show them as a review list with each agent's recommendation and evidence summary. Approving, rejecting and sending back to the agent should each take one click.
3. **Don't make the supervisor the bottleneck.** Let them hand items to a named adjuster or specialist, with the question attached. Their job is to clear or route each item, not to resolve all of them personally.
4. **Keep blocked agents useful.** Where possible, an agent that's blocked on one claim should park it and pick up the next, so a slow response doesn't idle the agent.
5. **Make the response visible.** Once the supervisor answers, the row should show "answered, agent resuming" and then drop off when work continues. If the agent gets stuck again, bring it back with a flag. Silent re-queuing hides failures.
6. **Alert sparingly.** Notify only on new blockers that are past a deadline threshold or that match a cluster. Six simultaneous pings are worse than one grouped message like "4 agents are blocked on the same clause".

## Questions to settle with the supervisors
- Who is actually authorized to sign off above $25k? That decides whether those items belong in this queue or in an adjuster's.
- Can a supervisor rule on policy ambiguity, or only escalate it? That decides whether "apply ruling to all" exists.
- What are the real deadline rules per claim? Urgency ranking is only as good as that data.

I'd test the design with a replay of a bad shift, with six blockers arriving within a minute, and time how long it takes a supervisor to clear them. Compare the grid mockup and the queue design on that measure.
