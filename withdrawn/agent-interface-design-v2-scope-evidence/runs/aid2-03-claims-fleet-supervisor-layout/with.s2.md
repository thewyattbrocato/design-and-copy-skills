**Assumptions (change any that are wrong):** the supervisor isn't the person who signs off on claims over $25,000, and the agents can keep working on other claims while one is parked. Every number below is a placeholder to test.

## Replace the grid with a queue

Thirty-five equal tiles show 35 things that mostly don't need the supervisor. The screen should help them find the few that do.

**1. A count strip across the top.** It shows Working, Waiting on you, Stuck, and Done this shift, with Waiting and Stuck first and in the loudest color. "Stuck" means an agent that has stopped sending signs of life without asking for anything. That is different from "waiting on you", which is an agent that has asked. A quiet agent should never look the same as a broken one.

**2. One queue of everything that needs a person, across all agents.** This is the main area of the screen. Each row shows:
- the reason, as one of three types: unreadable document, ambiguous policy rule, or over $25k sign-off
- the claim number and how long it has been waiting
- what the agent has already done
- what it needs, and what it would do by default

**3. A collapsed list of the healthy agents.** It is filterable by state. Opening an agent shows its plan, its log and its current claim. Don't use a draggable board, because moving a card wouldn't change the work.

## How to step in when five or six are stuck

**Triage by cause, not by agent.** The three stuck types need different people and different actions:

| Reason | Who can fix it | What the supervisor does |
|---|---|---|
| Unreadable document | Intake, or the claimant | Approve one "please resend" request. It shows the exact message and recipient, because it contacts a policyholder. |
| Ambiguous policy rule | A coverage or policy specialist | Route it, or record a ruling. |
| Over $25k | An adjuster with authority | Route it with the evidence packet attached. The supervisor doesn't sign it. |

**Batch only when the reason is the same.**
- If three claims hit the same unclear clause, show them together as one question with the clause text. One ruling then applies to all three, and each claim stays individually reversible.
- Unreadable-document requests can go out as a batch. The supervisor sees the message once, plus the list of recipients.
- Sign-offs are never batched. Each one opens its own evidence packet, because the approver needs to read it.

**Order by deadline and age, then group by reason.** A claim with a regulatory or customer deadline goes first. Within the same deadline, clear the group that unblocks the most agents.

**Agents park and move on.** A stuck agent sets the claim aside, marks it "waiting on: [reason]", and takes its next claim. The supervisor's response time then doesn't leave 35 workers idle.

**The agent brings a proposal.** For an ambiguous rule, the agent shows how it read the clause, the alternative reading, and which one it would pick. The supervisor confirms or corrects it instead of starting from scratch.

## Keeping the queue manageable

- **Set a queue ceiling.** Decide how many open items one supervisor can really handle (placeholder: N). Past that, agents stop pulling claims of the type that is piling up, and a concern notice appears: "Ambiguous-rule items are at N. New claims of this type are held. Route to a specialist?"
- **Send a concern before the ceiling, not after.** For example: "Queue is growing. 4 of 6 waiting items are the same clause. A ruling would clear them."
- **Make "not this one" and "always for this kind" two separate actions.** For example: "Always ask for a resend when a photo is under X resolution." The screen shows the rule in plain words and which recent claims it would have caught.
- **Keep Pause and Stop one step away,** by group, with the count shown first ("Pause 6 agents on this clause?"). Pause keeps the working state. Stop ends work and says what was left half-done.
- **Record which instruction version applied.** After a ruling changes, the log shows which version each claim ran under.

## Things to decide with the team

- **Who actually holds sign-off authority,** and what happens when that person is away. The screen shouldn't depend on the supervisor happening to notice. It should show a named owner and a time.
- **How eager the agents should be.** If a wrong guess on policy ambiguity is costly and a miss is cheap, they should ask more. If the supervisor can only clear about N items a shift, they should ask less. Pick the setting from the cost of each error and the supervisor's review capacity, and put it where an owner can change it.

I can sketch the layout or write the actual row text for the three queue types if that would help.
