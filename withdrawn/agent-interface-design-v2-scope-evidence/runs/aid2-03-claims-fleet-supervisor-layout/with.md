# Replace the grid with a queue

35 equal tiles show who exists, not where the supervisor should look. When 29 agents are fine and 6 are stuck, the 6 should be the screen. The supervisor's job is knowing where to look, not watching each agent.

**Assumption:** the agents prepare recommendations and an adjuster makes the final call. So the supervisor is unblocking agents, not approving payouts.

## The screen

**1. A count strip across the top.** Show Needs you, Stuck, Running, and Done this shift. "Needs you" and "Stuck" come first and are visually loudest. Everything else is quiet. If both are zero, the screen says so in words, so a calm screen doesn't look the same as a broken feed.

**2. One queue of everything that needs a person, across all agents.** This is the main panel. Each row has:
- the claim number and agent name
- the reason, as a typed label: **Unreadable document**, **Ambiguous policy rule**, **Over $25,000 sign-off**
- the specific question, such as "Page 3 of the contractor estimate is blurred" or "Policy §4.2 could mean water damage is excluded"
- how long it has waited, and whether it blocks other work
- what the agent has already done, and what it will do next (usually move to another claim)

Sort by waiting time, and put anything with a deadline first. Over-$25,000 items should not sit behind a stuck-document item just because they arrived later.

**3. The agents as a compact filterable list, not tiles.** One line per agent: state, claim, current step, time in step. Filter by state. The supervisor opens one agent to see its plan, what it has found, and a log. Keep the log on demand so it doesn't clutter the view.

**4. Show what the agent did while waiting.** A stuck agent should park the claim and take the next one if it can. Otherwise six stuck agents means six idle agents, and the queue grows faster than the supervisor clears it.

## Stepping in when five or six are stuck

The key move is **grouping by cause, not by agent.** Five stuck agents rarely mean five separate problems.

- **Same-reason batches.** If three agents are stuck on the same ambiguous clause, show them as one group: "3 claims, policy HL-form §4.2, water backup". The supervisor reads the clause once and answers once. The answer applies to all three, with each claim's evidence shown below it so they can exclude one that differs. Batch approval is only allowed when the reason is identical.
- **Different reasons get different handling:**
  - *Unreadable document:* the agent has usually exhausted what it can do. The actions are "request a new copy from the policyholder" (sends a message, so it's drafted for approval), "route to an adjuster," or "proceed without it and flag the gap". These need a human decision, but a quick one.
  - *Ambiguous rule:* this is a judgment call, and it may be a rule that should be written down. Offer "answer for this claim only" or "apply to all claims like this", and show the rule that second option creates in plain words, with edge cases it would newly catch.
  - *Over $25,000:* the agent isn't confused, it is waiting on authority. Show the recommendation, the evidence, and the amount, and let the supervisor approve, route to a named adjuster, or send back with a note. Don't batch these. Each gets its own full-attention view, because a tap-through habit is the risk.
- **Triage order for a surge:** deadlines first, then blockers (a stuck agent holding up other work), then batchable groups (fast wins), then singles.
- **Delegate, don't just resolve.** If the supervisor can't clear six items alone, each row has "Assign to…" so a named person owns it. The queue shows owner and age, so nothing is claimed by nobody.
- **Group controls with counts shown first.** "Pause these 4 agents" or "Park all 3 unreadable-document claims" shows how many will be affected before it applies. Pause and stop are different: pause keeps working state, stop ends work and says what was left half-done. Both sit one step from the main view.

## Reduce the stuck rate before it hits the supervisor

- **Warn early.** Agents flag a probable block ("this claim is likely to exceed $25,000") before they finish, so sign-off can be lined up in advance, not discovered at the end.
- **Send a concern notice when stuck items are climbing.** Something like "5 stuck on the same scanner batch" is more useful than five separate alerts. It should say what is drifting, what agents are doing meanwhile, and what the supervisor can do.
- **Notifications:** only problems interrupt. Completions go into a shift digest. One alert per stuck agent during a surge is how you get ignored.
- **Corrections:** every resolved item offers "just this claim" versus "always for this kind". Propose a rule when the same ambiguity is resolved the same way twice.

## Things to decide with your team

- **What does the supervisor's decision change?** Make sure a rule answer is logged with the version of the instruction in force, so earlier claims aren't judged by a later rule.
- **How many items can one supervisor review per shift?** I don't have a number for you, so measure it in a pilot. It sets how eager agents should be to flag versus proceed. If the queue regularly outgrows that capacity, agents should flag fewer low-stakes cases, but the $25,000 sign-off must stay mandatory.
- **Who covers the supervisor?** The design shouldn't rely on their attention alone. Name a backup, and have aging items escalate to them automatically.
- **Escape hatch:** the supervisor should be able to hand any claim to a human adjuster in one step, with the agent's work attached.

If it helps, I can sketch the queue row and the batched-group view as a wireframe next.
