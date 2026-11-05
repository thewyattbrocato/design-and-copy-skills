# Interface design for the billing migration run

The engineer will be away for most of the six hours. Design for a person who comes back at 3am to a phone alert, or at 8am to a summary, and has to decide quickly what to do. Everything below follows from that.

## Before the run: make starting it a deliberate act

**Preflight checks (blocking, with pass/fail per item)**
- Connectivity and credentials for both databases.
- Row counts on the old DB, the expected total (about 1.2M), and free space on the target.
- A verified backup or snapshot of the old DB, with its timestamp.
- Write-load check: whether the old DB is still taking writes, and how the run handles records that change mid-migration.
- A dry run on a small sample (say 1,000 records) that shows real validation failures before the big run.

**Explicit run configuration, shown on one confirmation screen**
- Batch size, failure threshold for auto-pause (for example, pause if more than 2% of a batch or more than N consecutive batches fail), and retry policy.
- What the agent will do on its own and what it will stop and ask about. Make this a visible policy, not something implied.
- Who gets notified, through which channel, and who is the backup if the engineer doesn't respond.

**The start action**
- Starting covers only phase 1 (copy and validate). Cutover and deletion are separate, later actions and are not part of "Start."
- State plainly what this run will and won't touch: "Writes to the new DB only. Old DB is read-only to this process."

## During the run: a glanceable status and a clear way in

**Top-line status (readable in five seconds, also in the alert message)**
- One state: Running, Paused (by agent or by human), Waiting on you, Failed, or Complete.
- Progress as records processed out of 1.2M, with a rate and an ETA based on recent throughput.
- Counts: migrated and validated, failed validation, pending, retrying.
- Time since the last successful batch. A stalled run looks identical to a slow one unless you show this.

**Failures as a first-class view, not a log**
- Group failures by cause (for example, "null billing address: 412", "currency code unrecognized: 38"), with a few example records for each group.
- Show the failure rate over time so a sudden spike, which suggests a systemic bug, stands out from steady scatter, which suggests dirty data.
- Failed records go into a quarantine table with the reason, the source values and a timestamp. Nothing is silently dropped or "fixed" without a record of it.

**Controls**
- **Pause** and **Resume**, which finish the current batch cleanly. Pausing should be safe at any time.
- **Stop**, which is different from pause and requires confirmation.
- Adjust the failure threshold mid-run.
- Skip a failure group, or retry it after a fix.
- Do not offer "force continue past validation" as a one-click action.

**Alerts: be sparing**
- Page only for things that need a human: the run auto-paused, throughput stalled, the target DB is erroring, or the failure rate crossed the threshold.
- Send non-urgent progress ("50% done, 214 failures so far") to a quiet channel or digest, not as pages.
- Every alert should include what happened, what the agent already did (for example, "paused after batch 812"), and the one or two sensible next actions with links.

**Decision requests from the agent**
- When the agent stops for a judgment call, show the specific question, the options, the agent's recommendation, and what happens if nobody answers. For example, "Stays paused. No data at risk."
- Make the safe default always "wait."

**Audit log**
- Append-only, with a timestamp, actor (agent or named human) and action for every state change, batch result and config change. It should be searchable and exportable.

## After the copy: separate gates for cutover and deletion

**Completion report**
- Reconciliation: source count = migrated + quarantined + intentionally skipped, with zero unaccounted records. If the arithmetic doesn't close, say so prominently.
- Validation summary beyond row counts: checksums or spot-checks of sums and balances on a sample, plus any aggregate comparison finance would care about (total balances, invoice counts by period).
- The quarantine list, with per-group counts and a way to export or assign it.
- A clear recommendation: "Ready for cutover," "Ready after resolving X," or "Not ready."

**Cutover (its own action, ideally not same night)**
- A checklist the engineer must confirm: failures resolved or accepted by a named person, reconciliation clean, rollback plan visible.
- Catch-up step for any records written to the old DB since the copy started.
- A rollback control that stays available and tested: switch reads back to the old DB with one action. Show how long it's expected to take.
- A post-cutover health view (error rates, latency, mismatch checks between old and new reads, if you can shadow-read) for the first hours.

**Deletion of old tables (a week later)**
- Do not auto-run it. Schedule a reminder, and when the date arrives, show a pre-deletion checklist: days since cutover, incidents since, confirmation a final backup exists and is restorable, and sign-off on any unresolved quarantined records.
- Require a typed confirmation that names the tables ("delete `billing_legacy.*`"), and ideally a second approver, because this is the one irreversible step.
- Consider renaming or revoking access first and deleting later, so the "delete" is reversible for a while.

## Principles to hold the design together

1. **Separate the three irreversibility levels.** Copying is reversible, cutover is reversible with effort, deletion is not. Each gets its own gate with escalating friction.
2. **The agent's default under uncertainty is to pause, not to proceed.**
3. **Every number must reconcile.** Show what happened to every record.
4. **Design the alert, not just the dashboard.** The 3am message is the real interface for most of this run.
5. **Make state recoverable.** If the engineer or agent restarts mid-run, the run resumes from the last committed batch without duplicating records (idempotent batches).

If you tell me where the engineer will interact with this (Slack, a web dashboard, a CLI), I can sketch the specific screens or the alert message formats.
