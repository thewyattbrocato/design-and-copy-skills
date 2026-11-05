# Migration interface: before, during, and after

The engineer isn't watching, so the interface has two jobs. It has to let them set the rules before they leave, and it has to tell them quickly and truthfully what happened when they come back. Design around decisions made up front, not live control.

## Before the run

**Preflight screen (a go/no-go checklist, not a form)**
- Source and target connectivity, schema compatibility, and free space on the target.
- Record count on the source (expect about 1.2M) and a dry run on a sample batch. Show what would be written and what would fail validation.
- Whether a rollback path exists and has been tested.
- Who gets paged, and through which channel.

**Policy the engineer sets, then confirms in one summary**
- **Failure thresholds:** For example, quarantine failed records and continue, but pause if more than 2% of the last N batches fail, or if the same error type repeats. A fixed threshold stops the agent from burning six hours on a systematic bug.
- **Pause vs. abort rules:** Which conditions pause (target latency, a failure spike) and which abort (source connection lost, schema mismatch).
- **Cutover mode:** The default should be **stop before cutover and wait for human approval**. Auto-cutover should be an explicit opt-in. Cutover is the least reversible step in the run.
- **Window:** Start time and a hard stop time (for example, don't run into morning traffic).

The "Start" button should show this policy back in plain language, such as "Will pause if >2% fail. Will not cut over without your approval."

## During the run

**One status view that answers "is it fine?" in five seconds**
- A single state: Running, Paused (needs you), Failed, or Waiting for approval.
- Progress: records copied, validated, and quarantined, with throughput and an ETA that updates.
- Failure rate trend and the top failure reasons, grouped by error type.
- Last heartbeat. A stalled agent that looks "running" is the worst failure mode, so show how long ago it last made progress.

**Notifications**
- Push only on state changes that need a human: paused, aborted, threshold breached, waiting for approval, finished.
- Send a short milestone note (25/50/75%) so silence reads as healthy.
- Each alert should say what happened, what the agent did about it, and what the engineer can do.

**Controls**
- **Pause and resume:** Pausing finishes the current batch cleanly.
- **Stop:** It leaves a consistent state, with no half-written batch.
- **Adjust thresholds or throughput** without restarting.
- **No restart-from-scratch button.** Batches should be idempotent and checkpointed, so resume always continues from the last verified batch.

**Failed records**
- Quarantine them in a separate table or queue, never silently dropped, and never blocking the rest.
- Each entry needs record ID, batch, which validation rule failed, and the offending value. Inspecting them mid-run should be possible and read-only.
- The agent shouldn't auto-fix or transform failed records unless the engineer pre-approved a specific rule. Otherwise it would be making data decisions overnight.

**Audit log:** An append-only, searchable log of what the agent did and why. The engineer should be able to reconstruct the night from it.

## After the copy completes

**Run report (the handoff)**
- Totals: copied and validated, quarantined, and skipped. They must reconcile to the source count (1.2M = passed + quarantined), with any gap shown as an error.
- Independent verification beyond per-batch validation, such as row counts, checksums or sampled comparisons per table, and balance totals if these are billing records.
- Quarantine breakdown by cause, each with a suggested action, such as fix and retry, accept as bad data, or manual review.

**Quarantine resolution**
- Actions: retry after fix, retry selected, export, or mark as accepted-with-reason.
- Don't let cutover proceed silently with unresolved failures. Require either zero unresolved or an explicit "I accept N unmigrated records" acknowledgment.

## Cutover

- A separate, deliberate step with its own confirmation, not a continuation of the run.
- Show a pre-cutover checklist: migration reconciled, quarantine resolved or acknowledged, no writes to the old DB since the copy (or a plan for the delta), and rollback tested.
- After cutover, show live health, such as error rates and read latency on the new DB.
- Keep a **one-click revert to the old DB** for the whole week. That means the old DB must stay in sync or be known to be stale, and the interface should say which.

## The week before deletion

- Keep the old tables, and show the countdown and what's blocking deletion.
- Deletion is a **separate, scheduled action**, not automatic. It should require re-confirmation at the time, along with these checks:
  - No reads from the old DB in the past N days.
  - A verified backup or snapshot exists.
  - Quarantine is resolved.
  - A named person approves it.
- Show exactly what will be dropped (table names and row counts) and require typing something specific to confirm.
- Send a reminder before the deadline. Make postponing easy and deleting deliberate.

## Principles behind the design

1. **Default to stopping when unsure.** An unattended agent should pause on ambiguity and never push through it.
2. **Irreversible steps need human gates.** Those are cutover and deletion. The copy itself is reversible, so let it run.
3. **Nothing disappears silently.** Every record is accounted for as migrated, quarantined, or explicitly accepted.
4. **Report state, not just activity.** "Waiting for you" and "healthy" must look different from "stalled."

If you want, I can sketch the status view layout or the alert message formats next. Those are where the design most often goes wrong.
