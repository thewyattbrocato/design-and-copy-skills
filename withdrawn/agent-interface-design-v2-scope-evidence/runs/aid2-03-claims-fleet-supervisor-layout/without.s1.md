# Supervisor screen for 35 agents

**Don't make the supervisor scan 35 tiles. Make the screen a work queue that agents add to when they need a person, with the fleet as background.** A supervisor can't read 35 equal tiles and spot the six that matter. A grid also treats three different kinds of stuck as one red dot, even though each needs a different person and a different action.

## Layout

```
┌ Fleet strip: 29 working · 6 need you · 0 idle · avg wait 4m · oldest 11m ──┐
├────────────────────────────┬───────────────────────────────────────────────┤
│ NEEDS A HUMAN (queue)      │ DETAIL for selected item                      │
│ grouped, sorted by urgency │ what the agent needs, what it tried,          │
│                            │ evidence (photo/doc/clause), options,         │
│                            │ agent's recommendation, action buttons        │
├────────────────────────────┴───────────────────────────────────────────────┤
│ Roster: 35 small cells, colored by state, hover for claim/agent             │
└─────────────────────────────────────────────────────────────────────────────┘
```

- **Fleet strip:** counts by state, the age of the oldest waiting item, and throughput against target. It shows at a glance whether the queue is growing faster than it's being cleared.
- **Queue:** this is the main surface. The roster stays small and peripheral, for noticing patterns like a cluster of one color.
- **Detail pane:** the supervisor should rarely have to open the agent's full transcript. Give them the decision and its evidence on one screen.

## Treat the three stuck types differently

| Type | What's really needed | Who resolves it |
|---|---|---|
| Unreadable document | Better scan, re-request from claimant, or manual transcription | Intake/ops staff, or supervisor if quick |
| Ambiguous policy rule | A coverage interpretation | Adjuster or coverage specialist |
| Over $25k | Sign-off by someone with authority | Authorized approver |

- **Sign-off is expected, not a failure.** Show it as a separate pipeline lane ("awaiting sign-off: 4, $182k total") rather than an alarm. Better still, route it straight to approvers so it never lands on the supervisor.
- **Each queue item should show:**
  - claim number and dollar amount
  - the block type
  - a one-line ask, such as "Is water damage from the 3/14 pipe burst covered under Section C.4?"
  - what the agent already tried
  - how long it has waited
  - any claimant or regulatory deadline
  - the agent's own recommended answer, when it has one
- **Actions sit on the item:** approve, pick an interpretation, request a new document, reassign to a person, take over, or park.

## When five or six are stuck at once

1. **Decouple the agent from the blocked claim.** When an agent hits a block, it parks that claim and pulls the next one. Six stuck claims then cost you six waiting claims, not six idle agents. This takes most of the time pressure out of the situation.
2. **Group by cause before sorting by urgency.**
   - Three agents stuck on the same ambiguous clause is one decision, not three.
   - Four unreadable documents from the same source may mean a scanner or upload problem.
   - Offer "apply to all N matching claims", and log the ruling as a precedent for an adjuster to review.
3. **Sort what remains** by deadline, then dollar amount, then wait time. Show the top item expanded and the rest collapsed, so the supervisor works one thing at a time.
4. **Route, don't resolve.** The supervisor's job is to get each item to the right person. One-click assignment to an adjuster, approver, or intake queue keeps them from becoming the bottleneck. Show who is handling what, so nothing gets worked twice or dropped.
5. **Support a fast keyboard flow.** Next item, decide, confirm, next. At 35 agents the supervisor is processing a stream, so mouse-heavy interaction will slow them down.

## Things the grid would miss

- **Systemic problems.** If 8 agents block on the same cause within 10 minutes, raise one banner ("8 agents blocked on policy form HO-3 2022 edition") instead of 8 queue entries.
- **Silent failures.** An agent that's "working" but has been on one claim 4× longer than the median, or is looping on retries, has a green dot and a problem. Flag time-in-state outliers.
- **Don't rely on color alone.** Use shape or label too, since the supervisor will be watching this for a full shift.
- **Alert fatigue.** Don't use sound or flashing for every block. Reserve interruptions for deadline breaches and systemic clusters.

## Questions that would change the design

- Does the supervisor have sign-off authority, or do they route to someone who does?
- Can the supervisor give coverage interpretations, or only route them?
- Are there claimant or regulatory clocks, such as acknowledgment deadlines, that should drive priority above dollar amount?

I can sketch this as a clickable HTML mockup if you'd like to compare it directly with your current grid.
