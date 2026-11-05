**Assumptions:** the engineer is on the platform team and can be paged, and someone else is on call overnight. The old DB stays readable and intact until the delete step. Every threshold below is a placeholder to set in the plan.

**Promise, shown at the top of the plan and the status page:** "While you're away, I will copy and validate records in batches and set aside any that fail. I will not switch the app to the new database or delete anything from the old one without your approval."

## Before: plan, rehearsal, caps

1. **Editable plan.** Show the four phases: copy and validate, reconcile, cutover, delete. Mark where it will stop and ask: before cutover and before delete. The engineer can reorder or cut steps.
2. **Rehearsal first.** Run a small sample copy into the new DB, or a staging copy, with a button to fire a batch now. For each sampled record, show why it passed or failed. The cost of a wrong live run justifies this step.
3. **Limits to set, with starting values marked as placeholders:**
   - Auto-pause if the failure rate in the last N batches exceeds X%.
   - Auto-pause on any validation error type never seen in rehearsal.
   - Auto-pause if throughput falls far enough that the projected finish passes a deadline (e.g. before the morning traffic peak).
   - Write-load ceiling on the old DB, so the copy doesn't hurt live billing.
4. **Restated instruction with three example cases:** a record that passes and is copied, a record that fails and is quarantined, and a record that changed in the old DB after it was copied. Say how that last case is handled, or flag it as an open question. Without an answer, the new DB will be stale at cutover.
5. **Named cover.** Pick who gets paged when it halts at 3am, and show that person's name on the status page. The plan shouldn't depend on the engineer waking up and checking.
6. **Preflight checks.** Confirm a verified backup or snapshot of the old DB, and confirm the new DB has capacity and the right schema. Don't allow start until these are green.

## During: the overnight run

**Status home (one page, glanceable):**
- State in large type: running, paused, stopped, or waiting for you.
- Records copied, validated, and quarantined out of 1.2M, plus the current batch.
- Projected finish time, with a note if it is slipping.
- Failure rate against its limit.
- Last action and when. A heartbeat timestamp tells an idle run from a dead one.
- **Pause** and **Stop** buttons on this page, one click each.

**Pause vs stop:** Pause keeps working state and accepts new direction (e.g. a raised limit) before resuming. Stop ends work now, keeps finished batches, and lists what was left half-done. It never restarts without a new explicit start.

**Messages, five kinds with a bar for each:**
- **Problem (pages immediately):** auto-halt triggered, DB errors, or the agent can't reach a database. The message says what stopped, how far it got, what's safe (nothing is half-committed), and what the engineer can do: resume, raise the limit, or inspect.
- **Concern (message, not a page):** failure rate at 60% of its limit, or the finish time slipping. It says what is drifting against which limit, what the agent is doing (e.g. slowing batch size), and when the next update comes.
- **Completion:** none per batch. One digest per phase milestone, e.g. each quarter of the records.
- **Check-in:** an hourly heartbeat on the status page only, not a notification.
- **Suggestion:** rare, e.g. "These 400 failures share one cause. Fix the mapping and I'll retry them."

**Staged warnings.** The failure rate should cross a "concern" line before it hits the halt line, so the first warning never arrives at the limit.

## Failed records: quarantine, don't block

- Failed records go to a quarantine table. The run continues unless a limit trips.
- **Never show a flat list of failures.** Group them by cause (e.g. "missing currency code," "invoice total mismatch") with a count, a few examples, and the old and new values side by side.
- Per group, the engineer can:
  - Retry after a fix.
  - Accept a proposed transformation, after previewing what it would change.
  - Exclude with a reason.
  - Export.
- **Two-level correction:** "fix this record" and "apply this fix to the whole group," with the rule shown in plain words before it applies. Applying a fix to a group is a rule edit, so it shows edge cases first: what it would newly catch, and what barely qualifies.
- The record of each action says which rule version was in force when it ran.
- Every record ends in one of three states: migrated, quarantined, or excluded with a reason. Their counts must sum to 1.2M.

## Cutover: its own approval

Approving the run is not approving cutover. The run ends in a "ready to cut over" state and does not proceed on its own.

**Cutover screen shows:**
- Reconciliation: counts match, checksums on key tables match, quarantined and excluded counts are stated, and a sample comparison with the doubtful items first.
- Anything changed in the old DB since it was copied.
- A plain statement of what happens: "The app will read from the new database. Writes go to ___."
- **Rollback, stated honestly.** Switching reads back is possible only while the old DB still receives writes or can be reconciled. State until when, and what is lost after that. If rollback is not clean, say so, and add a short hold or a staged rollout (a small share of traffic first).
- A required go/no-go from a named person, preferably daytime, with a person to contact.

Post-cutover, a watch panel shows error rates and read mismatches against the old DB. It auto-alerts on a limit and has a one-step revert, if the above allows one.

## After: the week before deletion

- **Report:** a change set, not a total. It shows what was migrated, quarantined, and excluded; how each exception was resolved; and what the engineer accepted. It's kept as the audit record.
- **Deletion is not a timer.** At day 7 the agent proposes it, with a checklist that must be green:
  - Cutover stable.
  - Quarantine empty or signed off.
  - Backup verified and restorable.
  - No reads hitting the old tables in the last N days (a log check).
- The request names the action, the target, and the consequence: "This permanently drops these tables. A restore comes only from the backup taken on ___."
- Deletion is irreversible, so it needs a named approver and a short hold after approval. Offer *this once* as the only grant. If checks fail, it doesn't delete and says why.
- Reminders escalate gently, and the agent offers to close the task and keep the tables if no one acts, since an open-ended "pending delete" shouldn't sit forever.

## Leaving and human path

Stop and "hand back" need no reason. The stop message says what's finished and what's in flight. A human contact (the on-call name) is on every page and every alert.

**One open question that changes the design:** how do you handle writes to the old DB during and after the copy? If the old billing system is live for six hours, records will change mid-run. That decides whether you need a delta sync and a freeze window, and it determines whether rollback is possible at all.
