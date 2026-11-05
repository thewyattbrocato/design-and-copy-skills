## Replace the grid with a queue

35 equal tiles with a status dot spends the supervisor's attention on agents that are fine. It gives no reason for a stuck agent, no sense of urgency, and nothing to act on. The supervisor's job is knowing where to look, so the screen should be built around what needs them.

I'm assuming the agents recommend and an adjuster decides, so nothing here pays out or sends anything. That's why the design leans toward agents asking early rather than acting. The thresholds below, including the $25,000 sign-off, are your rules. Every other number is a placeholder to test.

### Screen layout (top to bottom)

1. **Counts by state:** Working · Needs you · Stuck · Done this shift. "Needs you" and "Stuck" come first and are visually loudest. When everything is fine, the strip is quiet, so a quiet screen means no problems.
2. **One queue of items that need the supervisor, across all 35 agents.** This is the main surface and takes most of the screen. Each row shows:
   - **Reason**, as one of three types: *Unreadable document*, *Ambiguous policy rule*, *Over $25k, sign-off needed*.
   - Claim number, claim amount, and how long the agent has waited.
   - What the agent has already done, and its specific question. For example: "Photo 4 of 9 is blurred. I can continue on the other 8 and flag the gap, or hold."
   - A suggested default answer the supervisor can accept in one tap.
3. **A filterable list of all 35 agents** below or beside the queue. Filter by state, and open any agent to see its plan, what it has found so far, and its log. This replaces the grid, and nobody should need it during a normal shift.
4. **Pause and stop by group,** with the count shown before it applies ("Pause 6 agents?"). Stop and pause are different: stop keeps finished work and says what was left half-done, and pause keeps the working state so the agent can resume.

### When five or six agents are stuck at once

Individual alerts would make the supervisor answer whichever pinged last. Instead:

- **Group by reason, then by cause.** Six stuck agents are usually two or three problems. For example, four are waiting on one ambiguous clause (say, water damage from a gradual leak), one has an unreadable scan, and one is a $38k claim. The supervisor should see "3 groups, 6 agents," not six alerts.
- **One decision per group, applied together only when the reason is the same.** For the ambiguous clause, the supervisor reads the clause and the four claims side by side, decides once, and applies it to all four. Show the four claims, so a claim that doesn't fit can be excluded. Never batch the over-$25k sign-offs. Each one is a separate decision with its own record.
- **Order by cost of waiting, not arrival.** Rank by a deadline if the claim has one, then by how many agents are blocked, then by claim value. Say why the top item is on top.
- **Keep unblocked work moving.** A stuck agent should continue the parts of the claim that don't depend on the problem, such as the other photos, rather than going idle. That makes waiting cheaper, so the supervisor isn't racing the clock.
- **Route what the supervisor shouldn't decide.** An unreadable document may need the policyholder to resend. A policy ambiguity may need a coverage specialist. Give each row a "Send to…" action that names the person, so the supervisor can triage without becoming the bottleneck. The list of people comes from your org.
- **Rules from repeats.** If the same ambiguity comes up a second time, offer to turn the supervisor's decision into a rule. Show the rule in plain words with example claims it would and wouldn't catch, and let it be "this shift only" or "always." Treat it as a proposal the supervisor accepts, never something applied silently.

### Reduce the volume before it's a crisis

- **Warn before the limit.** Give a concern notice when the queue is trending past what one person can clear. Say what is drifting, what the agents are doing meanwhile, and what the supervisor can do (for example, pause intake for claims in the affected category). Set the threshold from how many items one supervisor can actually clear in a shift. You'll need to measure this, and I'd label it a placeholder until you have.
- **Over-$25k claims are predictable,** so don't make them an interruption. Have agents prepare the full file and put the claim in a "ready for sign-off" lane the moment it crosses the threshold, with the recommendation done. Sign-off becomes review, not a surprise.
- **Digest the routine.** Completed claims go into a batched summary. Only items that need the supervisor interrupt them.
- **Don't rely on the supervisor noticing.** If the queue is unattended past a set time, escalate to a named backup, such as a second supervisor or the team lead.

### Things to check before you build

- **Mistakes:** Each agent's output needs "not this one" and "always/never for this kind" corrections. Keep a list of what agents skipped or marked low confidence, because missed items go unnoticed.
- **Record:** Log who decided what and under which version of a rule, for audit.
- **Dry run:** Test the queue with simulated stuck claims before the 35 go live, specifically a burst of six at once.

If it helps, I can sketch the queue row and the grouped-decision view as a wireframe or an HTML mockup next. What's the realistic cap on how many items a supervisor can clear per hour? That's the number I'd set the thresholds from.
