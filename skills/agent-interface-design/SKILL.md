---
name: agent-interface-design
description: Use when designing software that does things for a person over time while they are not watching, in any words - "design an assistant that handles my inbox or schedule", "auto-triage", "an autopilot feature", "a background agent that does tasks for users", "what should it ask first", "how do we show what it did", "how do users stop or undo it", "people don't trust it". Covers what to delegate, setup and standing rules with limits, what it shows while idle, what it reports and when it interrupts, notification volume, handling its mistakes, override, pause and undo, handing control back, trust that is earned over time, and leaving. Not for chatbot wording and tone (ux-microcopy), ordinary notifications or settings (interface-behavior), consent and dark patterns (fair-persuasion), or open-ended generative chat products.
---

# Agent interface design

A product that acts for someone while they are elsewhere is not a better tool; it is a delegate. The screens that decide whether it works are the rare ones: granting the job and its limits, glancing to see it is alive, hearing about trouble, correcting a mistake, taking over, leaving. The usual draft spends its care on the happy path, then covers the rest with one permission toggle, a "Done!" ping per action, a thumbs-down and a log. Design those rare moments first and the happy path second.

## Do not produce

- One "Allow" or "Enable" grant for an agent that sends, spends, deletes or contacts people, with no stated maximum (count, amount, recipients, time window).
- A notification per action, or one stream where a finished chore, a suggestion and a real problem look alike.
- A report that gives a total ("42 items handled") without the items, the doubtful ones first, each with its own reverse control.
- Feedback that is only a thumbs-down, "report a problem" or a global off switch, with no "not this time" versus "never for this kind".
- A saved instruction the person never sees restated in plain words with example cases the agent would act on.
- A safety plan of "the user will notice and step in", or a first warning that arrives after the limit is crossed.
- An idle agent that looks the same as a broken one, a paused state that cannot be seen, or pause buried more than one step from the status view.
- Leaving that needs a reason, support or a call, or an automated flow with no route to a person.
- Invented figures: accuracy, time saved, success rates, "typical" volumes. Use a labeled assumption or a placeholder.

## When to use

- A feature or product that watches something and acts on its own: triage, scheduling, ordering, filing, monitoring, drafting and sending, long-running task agents.
- Setting up, reporting on, correcting, pausing, handing back or leaving such a thing; judging a draft that already exists.

## When not to use

- Wording of each message, button and fallback line, and the tone of a chat persona: `ux-microcopy`. This skill decides which messages exist, when they fire and what facts each carries.
- Ordinary notifications, undo, settings and defaults in a product that only acts when the person does: `interface-behavior`; settings controls: `form-design`. Defaults that serve the business, consent, engagement nudges, cancel flows: `fair-persuasion`. Whether a stat or claim is true: `honest-claims`. Tours and first-run teaching: `teaching-interfaces`. All if installed.
- A chat or writing product where the person reads every output before anything happens: out of scope. Cover it only at the point it starts to act on their behalf.
- A small fix (one alert, one undo) needs the matching decision and the quick checks, not the whole list. An explicit instruction, an existing design system, a platform convention or a regulatory duty beats every default here. If the design already handles a moment well, say so and change at most one thing.

## What current models change

People can state a rule in ordinary language and the agent infers the trigger and the steps, so input no longer needs fencing into menus. The risk moved: the agent is confidently wrong, or quietly widens its own scope. So show how it read the instruction (decision 2), keep its reach capped, and keep every action reviewable. Keep the old caution about range: claim only what it has proven, in any register. A friendly voice is a choice; a promise of general ability is the failure.

## When facts are missing

Infer the task, the stakes and who is affected from the brief and state them in one line. Ask once only if the chat is interactive and one answer would change the design (what the agent may spend or send is the usual one). Otherwise deliver on stated assumptions with starting values marked as such. Numbers in this skill are starting points to test, not findings.

## Decisions, in order

A small task starts at the decision it touches.

1. **What to delegate, and how far.** Default: delegate only a task that has a detectable trigger, needs no fresh taste or judgment each time, and the person does not want to do themselves. Keep it manual or suggest-only when they are meant to learn it or the trigger is a matter of preference. Pick the starting rung by worst case: suggest, draft for approval, act within limits and report, act silently. Start on the lowest rung that is still useful; start on act-and-report only where every action is cheap to reverse. Set how eager it is from the cost of a wrong act against the cost of a miss and how many flags the person can really check, not from the worst case alone. Write one line: "While you are away it will ___, and it will never ___." Detail: [setup and limits](references/setup-and-limits.md). For a one-off long job, one person supervising many agents, or permission scopes: [long jobs, fleets and permissions](references/long-jobs-fleets-and-permissions.md).
2. **Setup.** Default: propose a first draft of the instruction from what is already known and ask only for corrections; ask only what gates safe operation and defer personalization to after the first run. A standing instruction says what it does and how much of it is allowed, then when it runs and what it must leave alone. Anything that sends, spends, deletes or contacts others gets an explicit cap. Ask for the narrowest permission that works, say what it buys, and say it can be widened later. Restate the instruction as the agent understood it, with three example cases. Change to a dry run before going live when the worst case is costly: simulated items, a way to fire the trigger now, a view of why it chose each. Skip it when a wrong action costs nothing.
3. **What it shows while idle.** Default: one status home showing running or paused, last action and when, next check, and what it is watching against its limit. Pause sits one step from there, and the paused state is unmissable. When a trigger passes while paused, say what was skipped without blame and offer resume now or on a date. Change to an ambient indicator only for agents the person checks rarely.
4. **What it tells them, and when.** Sort every message into five kinds, most urgent first, each with its own bar: problem (needs the person now), concern (a trend heading toward a limit), completion (small, batched), suggestion (rare, only when the value is very likely), check-in (proof of life, adjustable). Default: routine completions go into one digest on a schedule the person picks; only problems interrupt at once; each kind has its own off control and the total has a ceiling. Change to immediate for things with a deadline the person can still act on. Concern notices and the action report: [reports and alerts](references/reports-and-alerts.md).
5. **Mistakes.** Default: two corrections from the item itself, "not this one" (optional duration or place) and "always or never for this kind", the second showing the rule it creates. Propose a rule after the same skip twice. Keep a skipped and rejected list, low-confidence first, because missed actions go unnoticed. Any rule edit shows the plain-language rule and a preview of edge cases: what would newly be caught, what barely qualifies, what barely misses. A random sample is not that preview. Change to a one-tap flag with context saved for later when the person cannot tune now. See [mistakes and rules](references/mistakes-and-rules.md).
6. **Reversal.** Default: every action is reversible from the activity record, singly or by batch, for a stated period. Actions that cannot be undone (a message others have read, money moved) stay on the draft-for-approval rung or run after a short hold. Say plainly what undo cannot reach.
7. **Handing back control.** Default: do not make watchfulness the safety plan; people stop attending when nothing happens and lose the skill. Name who or what covers a failure. Where the person truly must act, warn in stages before the threshold, show one persistent, glanceable view of what is wrong, what is needed and by when, keep the agent helping, and name who acts. See [handback, trust and exit](references/handback-trust-and-exit.md).
8. **Trust over time.** Default: start small and reversible, and offer a wider scope only after a run of clean results the person can see, as a proposal they accept. Never widen silently where it sends, spends or deletes. Keep a small piece of the task manual if the skill is worth keeping.
9. **Leaving.** Default: off, pause and delete are reachable from the status home and from agent messages, need no reason, say what happens to work in flight and to past actions, and dormant standing requests offer to close themselves. A person is reachable from any automated flow.

## Output

Deliver what was asked. For a product design: the assumption line, then only the moments that matter for this product, each as "when X, do Y, because Z", with the actual message text where messages are the point. For a message or a spec section: the text first, nothing before it. A stated length or count beats this format. No notes section unless a note changes what the reader does; at most two one-line notes.

## Quick checks

- The one-line promise of what it does and never does is stated.
- Every send, spend or delete action has a named cap; the grant says its maximum.
- The instruction is restated in plain words with example cases before it goes live.
- Status home shows alive or paused, last action, next check; pause is one step away.
- Each message is one of the five kinds, with a bar, a frequency and an off control.
- Each concern notice says what is drifting against which limit, what the agent is doing, when they will hear next and what they can do.
- Both "not this one" and "always or never" exist, plus a list of skipped items.
- Nothing relies on the person noticing; every irreversible action sits behind approval or a hold.
- Leaving needs no reason; a human path exists; no invented numbers.

## References

- [setup-and-limits.md](references/setup-and-limits.md): load for onboarding an agent, standing instruction wording, caps, permission scopes, dry runs, and the delegate-or-not call.
- [reports-and-alerts.md](references/reports-and-alerts.md): load for the idle status view, message kinds, digests, concern notices, action reports and how to talk about its value.
- [mistakes-and-rules.md](references/mistakes-and-rules.md): load for correcting wrong actions, missed actions, rule editing and previews, and reviewing what it skipped.
- [handback-trust-and-exit.md](references/handback-trust-and-exit.md): load for high-stakes takeover, the staged warning, widening trust, leaving, a human path and judging whether the agent works.
- [long-jobs-fleets-and-permissions.md](references/long-jobs-fleets-and-permissions.md): load for an hours-long one-off job or a run with phases, one operator over many agents, how eager an agent should be, and permission scopes at commit points.
