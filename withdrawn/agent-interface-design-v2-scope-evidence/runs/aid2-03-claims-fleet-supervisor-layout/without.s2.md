# Supervisor screen: a queue of what needs a human, not a grid of agents

With 35 equal tiles, a supervisor has to scan all 35 to find the 5 that matter. A dot color tells them an agent is stuck. It doesn't tell them why, how urgent it is, or what to do. Most of the screen would show agents that are working fine.

## What to put on the screen

**1. A summary strip across the top.**
- Counts by state: working, waiting on a human, parked, done this shift.
- The age of the oldest waiting item.
- Claims completed per hour against target.
- A count of items nearing a deadline.

**2. A "Needs you" queue as the main panel, taking about 60% of the screen.**
- Each stuck agent is a card. Sort by urgency, not by agent name.
- Urgency combines time waiting, claim value, and any policyholder or regulatory deadline.
- Each card shows:
  - the claim number and a stuck-reason badge (Unreadable doc, Policy ambiguity, or Over $25k);
  - the specific question, such as "Page 3 of the contractor estimate is illegible" or "Does the water-damage exclusion apply to a slow leak under endorsement HO-9?";
  - the agent's proposed answer or recommendation, if it has one;
  - the evidence, meaning a thumbnail of the document or photo, the policy clause, and the amount;
  - the action buttons for that reason (see below).

**3. A compact roster of the healthy agents.**
- Show it as a dense table or a strip of small marks, not big tiles.
- Each row shows the agent, claim, stage (photos, documents, policy check, drafting), and time on this claim.
- Healthy agents stay quiet. Expand a row only when the supervisor wants to inspect it.

**4. A separate flag for agents that are unhealthy but not asking for help.** Examples are looping, much slower than the median for their stage, or repeatedly erroring. Those agents won't raise their hand, so the system has to.

## Actions for each stuck reason

| Stuck reason | Supervisor actions |
|---|---|
| Unreadable document | Request a re-upload from the policyholder, send it to a human for transcription, or tell the agent to proceed without it and flag the gap. |
| Ambiguous policy rule | Give a ruling, and optionally save it as a rule for similar cases. Or escalate to underwriting or a coverage specialist. |
| Over $25k | Approve the recommendation, reject it, return it with a question, or reassign it to someone with the right authority. |

Every action should be one or two clicks, with keyboard shortcuts. The agent resumes automatically afterward.

## When five or six agents are stuck at once

1. **Group by cause.** Sections or filters for the three reasons turn six interruptions into about three decisions.
2. **Detect shared causes.** If four agents are stuck on the same clause, show one banner: "4 claims blocked on HO-9 slow-leak exclusion." One ruling releases all four. This matters most because ambiguity tends to repeat across claims.
3. **Batch the mechanical work.** For unreadable documents, select several and send re-upload requests in one action.
4. **Review sign-offs one at a time.** Use a review pane with next and previous. Don't offer bulk approval for claims over $25k, because that invites rubber-stamping the cases that most need scrutiny.
5. **Delegate.** The supervisor shouldn't be the only resolver. Allow "assign to" a senior adjuster, document team, or coverage specialist, with the card showing who has it and for how long.
6. **Keep the throughput up.** A stuck agent should park the claim and pick up the next one, so a waiting agent isn't idle. The queue then measures waiting claims, not just wasted agent time.
7. **Keep the screen stable.** New items shouldn't reorder cards while the supervisor is reading or about to click. Add them with a visible "3 new" indicator. Use icons and labels as well as color, since a red dot alone is easy to miss and not accessible.

## Also worth adding
- An audit trail of every ruling and approval: who, when, and the basis. This matters for claims.
- A shift handoff view of open items and standing rulings.
- A drill-down per agent showing the full reasoning trail, which the supervisor opens only when needed.

## Questions that change the design
- Who is authorized to sign off over $25k? If it's not the supervisor, the queue needs routing, not just a button.
- Are there deadlines, such as a statutory acknowledgment window, that should drive the sort order?
- How often do rulings repeat? If often, a "saved rulings" feature will cut the supervisor's load more than any layout change.

I can sketch this as a wireframe or a clickable HTML mockup if that would help.
