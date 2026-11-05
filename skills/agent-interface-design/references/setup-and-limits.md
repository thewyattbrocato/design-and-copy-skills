# Setup and limits

Load when deciding whether something should be delegated, onboarding an agent, wording a standing instruction, choosing caps and permissions, or planning a trial run. Names and numbers below are invented; adapt the pattern.

## Should it run without them?

Before drawing a screen, look for reasons to keep it manual or suggest-only. Any one is enough:

- It cannot finish without stopping to ask the person something each time.
- When it is due is a matter of taste or mood, not something software can detect.
- The person wants to be the one doing it (a craft, a hobby, a skill they are building).
- The outcome needs the person's own eye now and then, and nothing will make that practical.

Design for the goal, not the task: "keep the greenhouse stocked" outlives "reorder seed trays", and a goal can be checked over weeks. The request still has to be concrete enough to act on. If it is too narrow it will find nothing next month; if it is too vague it will wander. Help the person phrase it, with examples they can edit.

## Choose the rung

| Rung | The agent | Fits when |
|---|---|---|
| Suggest | Proposes, never acts | Taste decides, or the first weeks of any new agent |
| Draft for approval | Prepares the action, waits for one tap | The action reaches other people or moves money |
| Act within limits, report | Acts, lists what it did, everything reversible | Each action is cheap to undo and the volume is high |
| Act silently | Acts, reports only exceptions | Proven over many runs, harm is tiny, the person asked |

A feature can sit on different rungs for different actions: sort silently, draft the reply, never send without approval. Say which action is on which rung.

## Standing instructions

A setup that cannot capture all of these is not finished:

- The action itself, and the ceiling on how much of it may happen before the agent stops to ask.
- The trigger: a schedule, an event or a threshold.
- The carve-outs: suppliers to leave alone, a week it must not touch, a person it must never contact.

The ceiling is the one drafts forget. Away from supervision the agent follows the wording to the letter, and a runaway costs real things. Set a ceiling for each thing that can run away:

| It can | Cap to set | Starting value to test |
|---|---|---|
| Spend | Per order and per week | A low sum the person names, never a default sized to the plan tier |
| Message people | Per day, per recipient, and a list it may not contact | A handful a day, once per person per week |
| Delete or overwrite | Count per run, and only items it created or the person tagged | Small enough to review in a minute |
| Run | Length of time and number of steps | Short, then extended on request |

When a cap is hit the agent stops and says so as a problem, not silently skipping the remainder.

## Permissions

Default: ask at the moment a permission is needed, for the narrowest scope that does the first job, and say what it buys ("Read the supplier invoices folder so I can match deliveries to orders"). Show the maximum scope next to the request. Say it can be widened later and where. Change to asking up front only when the first action cannot work without it. A "recommended" broad scope that is pre-selected is a fair-persuasion matter; here, scope starts narrow and grows by the person's choice.

## Fewer questions

- Offer a draft instead of an interview: "Based on your last four orders I'd reorder trays when fewer than 20 remain. Change anything?" Do the same from permissions already granted, or by watching the person do the task once.
- Ask now only what gates safe operation (caps, exemptions, who may be contacted). Defer taste (formats, names, preferred times) to a small event after launch, which also gives the agent an honest reason to check in early.
- Where the stakes are high or a rule forbids guessing (money limits, medical or legal settings), ask outright; a wrong guess costs more than the question.

## Say what it is not

State range once, plainly, where setup begins: what it does and the main things it does not. Pitch the register to the proven range. A warm, human-sounding voice is fine only if it still says "I can only reorder from your listed suppliers"; the stronger the voice, the sooner people ask for the thing it cannot do. A light, true reply to a playful or out-of-range request tells people the boundary without a failure message.

## Trial run before going live

Default for any agent whose worst case is costly: let the person try it first. Use simulated stock or money, compressed time, a way to fire the trigger on demand, and for each outcome a short why ("Chose 40 trays because the last frost date is in 6 days and 12 are on hand"). A correct result for a wrong reason is a defect nobody sees until it matters, so the why belongs in the trial. Skip the trial when a mistake costs a skipped song.

## Going live

- State what happens next: "Starting Monday it will check stock at 7 each morning. First order, if any, will wait for your approval for the first two weeks."
- Make pause easy to find before anything else in the launch message.
- Match the moment to the effort: a long setup earns a clear confirmation and a first scheduled check; a one-tap feature does not need a ceremony.
- Show the idle state immediately (next check, what it is watching), so a quiet agent does not read as a dead one.

## Worked example: a plant nursery's reorder agent

Weak setup: a screen of eleven toggles, an "Allow purchasing" switch and a card on file. Nothing says how much it may buy.

Better, in order:

1. One-line promise: "Each morning I check tray and soil stock and place orders with your three listed suppliers. I won't order from anyone else or spend more than the weekly limit."
2. Draft rule: "Reorder when fewer than 20 seed trays remain. Skip the week of the open day. Order 40 at a time." Three sample cases beneath it: "At 18 trays: I'd draft an order for 40. At 25: nothing. On 12 May: nothing, you've paused ordering that week."
3. Caps: [weekly spend limit, set by the owner], one order per supplier per day, no new suppliers.
4. Rung: draft for approval for the first two weeks; the owner can then move it to act-and-report.
5. Permission: read access to the stock sheet now; payment later, when the first approved order is ready to place.
