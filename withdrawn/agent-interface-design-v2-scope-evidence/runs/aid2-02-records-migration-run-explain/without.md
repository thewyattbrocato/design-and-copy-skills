# Interface design for the billing migration

Design around one fact: the engineer will be asleep for most of the run. The interface has to work as a handoff, not a live dashboard. Before the run, the engineer approves a plan. During it, the agent mostly acts alone and calls them only when it truly needs a human. Afterward, the engineer gets a short morning report with evidence they can trust.

## Before the run: approve a plan and the rules for stopping

**Preflight checks (blocking, not advisory)**
- Source and target connectivity, credentials, and free disk space on the target.
- A verified backup or snapshot of the old database, including a test that it restores.
- A dry run on a sample, such as 1,000 records, with its validation results shown.
- A row count and checksum baseline of the source.
- Rollback readiness: the app's read-source switch has been tested in both directions.

**A run plan the engineer approves explicitly**
- Record count, batch size, and estimated duration.
- The validation rules, in plain language.
- What the agent may do alone and what it must stop and ask about (see the table below).
- Who gets paged, through which channel, and who is the backup if the engineer doesn't respond.

**Pre-agreed thresholds.** Decide these now so nobody improvises at 3am:
- Pause if more than X% of a batch fails validation, or if failures cluster on one cause.
- Pause if target latency or error rates degrade.
- Hard stop on any sign of data corruption or source/target count mismatch.

## During the run: quiet by default, loud when it matters

**One glanceable status view**
- State: running, paused, waiting for you, or failed.
- Progress: for example "612,000 of 1.2M (51%), ETA 02:40".
- Counts: migrated, failed validation, and quarantined.
- A small trend of failure rate and throughput, so a drift is visible at a glance.

**Failed records go to quarantine and don't block the run.**
- The agent skips them, logs the record ID, the rule that failed, and the reason, and moves on.
- Failures are grouped by cause. "4,100 records: null postal code" is actionable. 4,100 separate lines are not.
- Nothing is silently fixed, dropped, or coerced. If the agent applies an approved transformation, that is logged separately.

**Controls**
- Pause, resume, and stop (finishing the current batch cleanly).
- Adjust throughput.
- Retry a quarantined group after a fix.
- Every control confirms what it will do and is safe to repeat.

**Alerting**
- Page only on pause conditions, hard stops, and completion.
- Don't send a notification for every batch or every failure.
- Make the page self-contained: what happened, the current state, what the agent did, and what it needs from the engineer.

**Resumability.** Batches are idempotent and checkpointed. If the run crashes at record 700,000, restarting continues from the checkpoint and creates no duplicates.

**Cutover is a separate gate that the agent never triggers on its own.** Copying and validating can run unattended, but switching the app to the new database needs a human decision, ideally in the morning with fresh eyes. The agent finishes the copy and then waits.

## After the run: a report that supports a decision

**Completion report (the first thing the engineer reads)**
- Total records: migrated, quarantined, and unaccounted for. The unaccounted number should be 0, and a reconciliation of source count against target count plus quarantined should prove it.
- Checksums or sampled field-level comparison between old and new.
- Quarantine summary by cause, with a downloadable list of record IDs and suggested fixes.
- Anything the agent did that wasn't strictly the plan: retries, pauses, throttling.

**Cutover screen**
- A checklist of conditions that must be true: reconciliation clean, quarantine resolved or consciously accepted, and any records that changed on the old database during the run re-synced.
- Show what the switch does, how to reverse it, and how long reversal takes.
- Require a deliberate confirmation. Don't use a casual single button.

**Quarantine resolution.** The engineer can fix and re-run a group, mark it "accept and skip" with a reason, or export it for the billing team. Each decision is recorded.

**The week before deletion**
- Show a countdown: "old tables will be deleted on [date]".
- Keep a rollback path available until then.
- Run a daily health check comparing old and new, plus app error rates on the new source.

**Deletion is its own gated action, not an automatic timer.**
- It happens only after explicit confirmation, which lists exactly which tables will go.
- Preconditions are shown: cutover stable for 7 days, quarantine closed, and a final backup archived with a restore verified.
- The agent proposes the deletion, and the engineer approves it. An approval from the start of the run does not cover it.

## What the agent decides and what the human decides

| Action | Who decides |
|---|---|
| Copy and validate batches, retry transient errors | Agent, alone |
| Quarantine failing records | Agent, alone |
| Pause on a threshold breach | Agent, alone (it notifies the engineer) |
| Resume after a pause | Human |
| Fix or transform failing records | Human, or pre-approved rules only |
| Cutover | Human |
| Rollback after cutover | Human |
| Delete old tables | Human, after the waiting week |

## One more thing to settle first

Billing data keeps changing during a six-hour copy. Decide how the migration handles records modified on the old database after they were copied. Options include freezing writes, change-data-capture re-sync, or a final delta pass before cutover. The answer changes what the interface has to show, so I'd settle it before designing the screens.

If it would help, I can sketch the status view and the pause-alert message in more detail.
