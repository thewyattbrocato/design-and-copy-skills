# Handback, trust and exit

Load when the person may have to take over from an agent, when deciding how scope should grow, when designing off, pause or delete flows, when asking how to tell whether the agent is any good, or when an automated flow needs a route to a person. Names and numbers are invented; adapt the pattern.

## Do not plan on vigilance

Watching a system that almost never fails is something people do badly. Attention drifts within tens of minutes, sooner when nothing happens, and skills for the work fade when software does it. A plan that says "the user supervises and steps in" is a plan that works in demos. Pick one of these instead, and write it down:

- Another party covers the failure: a remote operator, a nearby system, a safe stop the agent can reach by itself.
- The agent shrinks its own job as it nears trouble (slower, smaller steps) before it needs anyone.
- The person practices: scheduled drills that are real and varied, sometimes unannounced, with an explicit marker for a real emergency, or a high-fidelity simulator.

Low stakes need none of this: a missed task that costs a messy room is not worth a drill.

## When a person must take over

Do this only where a handoff is realistic. If the person cannot cope in the time available, route elsewhere.

**Before the threshold, warn in stages.** Early and small, then firmer, then the ask. "Sensor drifting, compensating." "Drift growing, may need you to step in within about ten minutes." "I need you to take over by 4:10." Bad news that arrives as the end of a visible trend is acted on; a siren at the last second is not.

**Carry enough to act.** An alarm says what is wrong, what is needed, by when and which options exist. It names who must act and who is next in line if they do not, so each of several people does not assume another will.

**Take-over view.** Persistent and glanceable, in a place the person already looks. Not a modal that hides the situation, not a chat window to type into, not decorated or branded. It shows the problem, the recommended action and the alternatives, and the agent keeps helping with what it still can.

**Taking back.** The agent signals when it is ready. Whether it returns automatically depends on the domain; for anything where a surprise is dangerous, the person agrees first. Make agreement possible without leaving the main task: a spoken or one-touch reply, not a trip to another screen. After the return, keep a short reassurance period in which it says it is watching, then give one plain note on how to avoid a repeat.

Example: a grain-dryer controller at a co-op.

- Early: "Moisture reading is climbing faster than the fan can clear. Fan at full; I'll tell you in 20 minutes if that's not enough."
- Firm: "Still climbing. You may need to move the load before the next truck arrives. Crew chief, you're first; Dana is second."
- Persistent panel on the shed screen: the current reading against the limit, the one recommended action (open bay 3 for transfer), the other options, and a countdown.
- Return: "Back under the limit since 2:20. Ready for me to resume the normal cycle? [Resume] [Keep manual]"

## Trust is earned slowly and lost fast

It also depends on stakes, on whether one weak subtask taints the rest, and on how much reach the agent has. So scope grows from evidence.

- Start with small, reversible tasks. Show results as they happen.
- Offer wider reach after a run of results the person can see: "Twelve orders approved without changes. Let me place orders under $50 without asking? [Yes] [Not yet]". The person accepts; the product does not decide for them, and it does not widen silently where it sends, spends or deletes.
- Let the person do the task themselves in parallel and compare, and keep a small manual piece when the skill is worth keeping. This helps skeptics build trust or lose it, tunes the agent, and keeps the person able to take over.
- After a bad incident, the right response is a smaller scope and a plain account of what changed, not a reassurance.
- Where the agent personalizes information (news, recommendations), let the person tune it and keep a controlled share of items from outside their stated preferences, so tuning does not close them in.

## Leaving

- Off, pause and delete are reachable from the status home and from agent messages, and need no explanation and no extra confirmation beyond the plain consequence.
- Say what happens next: in-flight work (finish, cancel), past actions (stay, reverse), stored data (kept for a stated period, then removed), and how to come back.
- A standing request that has produced nothing for a long time offers to close itself rather than nag or run forever.
- When a person has died, a standing agent should not keep acting for them; give family or an executor a way to close it, and make the rule visible in setup where consequences warrant.
- Do not make exit a retention funnel. How the exit is offered, and whether a save offer is allowed, is `fair-persuasion`.

## A route to a person

An automated flow keeps a visible way to reach a human, in any state, including for the least valuable customers. Cost pressure does not justify removing it. Say plainly that the agent is automated; a friendly name and voice are fine, but a convincing human impression lends itself to abuse, and a spoofed friendly voice can talk someone into things. Where the agent says it acts for the person, the person can verify that the message came from the product.

## Does it work?

Do not accept the agent's own report of its accuracy. Check at three levels.

1. **Did it act correctly?** An independent audit of a sample of actions and non-actions: how many times it acted when it should have, how many it missed, against what it was specified to do.
2. **Do people feel in control?** Ask how far people agree with plain statements such as "I can see whether it is running", "I understand why it did that", "it leaves me alone unless it matters", "when it is wrong I can put it right".
3. **Is it worth having?** Count those who switched it off and why, and compare outcomes with people who do not use it. Failures dominate memory, so use counts, not impressions.

Judge cooperation too: can the person direct it, does it know its limits, and does it leave the person equipped when it hands over? A lab session of an hour cannot judge an agent whose work plays out over weeks; use a longer study or logs from real use.
