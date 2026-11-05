# Migration run interface: before, during, after

**Assumptions:** The old database stays intact and readable until the delete step. The batch copy can be re-run safely (idempotent writes). The app can be pointed back at the old database after cutover, at least until new writes diverge. Please check each of these, because the design depends on them. All thresholds below are starting values to test, not findings.

**The promise, shown at the top of the run page:**
"While you're away it will copy and validate records in batches and quarantine any that fail. It will never switch the app to the new database or delete the old tables without your approval."

The agent does two kinds of work. Copying and validating are cheap to redo, so it can do them unattended. Cutover and deletion are costly or irreversible, so each gets its own approval.

## Before the run

**1. Plan, editable, with stopping points marked.** Show the steps as:
1. Copy and validate in batches.
2. **Stop: review the results, then approve cutover.**
3. Switch reads to the new database.
4. Observation week.
5. **Stop: approve deleting the old tables.**

The engineer can set batch size and concurrency here. Steps 3 and 5 can't be reordered or removed.

**2. Failure policy, set before launch.** This is the decision that matters most overnight. Ask for:
- **Quarantine limit.** For example, "Pause the run if more than N% of a rolling window of batches fail, or if any single batch fails entirely." (N is a placeholder. Ask the engineer to set it, and suggest a value based on what they expect to fail.)
- **Failure categories.** For example, "missing field", "amount mismatch" and "orphaned reference". The engineer can mark categories as expected (quarantine and continue) or unexpected (pause on the first occurrence).
- **Who gets paged and how.** Name the person and channel, plus a backup. The plan can't be "the engineer will notice."

**3. Dry run on a sample before going live.** Run a small sample of real records through copy and validate, writing to a scratch target. Show the failures it finds and why. This is worth the time because a bad validation rule discovered at hour 4 costs far more than one found in minutes. Launch is disabled until a dry run has completed or the engineer explicitly skips it.

**4. Restated scope with examples.** Show, in plain words: "Will copy N records from `billing_old` to `billing_new`. Records with *[example failing case]* will be quarantined, not copied. Records with *[example edge case]* will be copied but flagged." Use real examples from the dry run.

## During the run

**One status page.** Make it glanceable from a phone:
- State: running, paused, stopped or waiting on you, in unmistakable text and color, not just a spinner.
- Progress: records copied, validated, quarantined and remaining, plus the current batch and the last batch completed with its time. If no batch has completed within the expected interval, show "stalled" rather than "running". A silent hang must not look the same as a slow run.
- Failure rate against your limit, for example "quarantined 0.4% of the window; pause threshold is N%". This is the concern view: it shows drift toward the limit before the limit is hit.
- Pause and Stop, one tap from this page.

**Pause is not stop.** Offer both:
- **Pause** finishes the current batch, holds state and takes new direction (for example, adjust the threshold or change a category's handling) before resuming.
- **Stop** ends work now, keeps what is committed, and states exactly what is half-done: "Batch 412 was mid-write; 38 of 500 records copied, rolled back / needs check." It never restarts without a fresh, explicit start.

**Message kinds overnight:**

| Kind | Trigger | Channel |
|---|---|---|
| Problem | Run paused itself (threshold crossed, stall, database error, an unexpected category) | Page immediately |
| Concern | Failure rate at about half the threshold, or throughput well below plan | Single message, not repeated; says what's drifting, what the agent is doing, when you'll hear next |
| Completion | Batches done | No notification. Visible on the status page only |
| Check-in | Hourly heartbeat | Optional and off by default. Engineers can turn it on if they want proof of life |

Example problem message: "Migration paused at 41% (batch 2,310). Failure rate hit the limit: 6.2% of the last window, mostly *amount mismatch*. Nothing was deleted or switched. 4,812 records are quarantined and safe. Open the run → review failures, adjust, or resume."

**Quarantined records are a first-class list, not a log.** Group by failure reason, show a count per group, and for each record show source values, the specific check that failed and the proposed fix if there is one. Controls:
- **Retry** this record or group.
- **Fix and retry**, for a corrected value.
- **Skip permanently**, with a required note. This one stays visible in the final report.
- **"Treat this reason as expected / unexpected"**, which shows the rule it creates and a preview of how many records it affects.

**Seam check-in before cutover.** When copying finishes, the agent stops and writes two lines: what it believes is true (counts matched, N quarantined) and what it assumes (for example, "no writes to the old database since copy started"). That assumption matters: records changed in the old database during six hours of copying could be silently stale. The agent should state how it checked, and if it can't verify, say so.

## Cutover (approval gate)

This is not a "Continue?" dialog. Show:
- **Reconciliation:** source count, copied count, quarantined count and skipped count, with the difference explained, not just totals. Quarantined records are listed doubtful-first.
- **Drift check:** records changed in the old database since they were copied, and whether they've been re-synced.
- **The consequence in plain words:** "The app will read from `billing_new`. The 4,812 quarantined records will not be visible in the app until fixed." If any customers would see missing billing data, say how many.
- **Rollback:** "You can switch reads back to the old database until [condition]." State plainly what rollback cannot cover, for example writes made to the new database after cutover.
- **Scope of the grant:** this cutover only, not "always."

## After cutover

**Observation week.** The status page switches to a post-cutover view: read errors and any customer-facing discrepancies the agent can detect, plus the quarantine count falling as records are resolved. Rollback stays one step away, with the divergence caveat above.

**The end-of-run report.** Not "1.2M migrated." It should have:
- Reconciliation by category, each with its own list.
- Everything quarantined or skipped, with who decided and when.
- Every setting change made during the run, with the time it applied, so a record isn't judged by a rule that changed later.

**Deleting the old tables (second approval gate, a week later).**
- The agent doesn't delete on a timer. At the one-week mark it asks, and the request has the same shape as cutover: what will be deleted, what remains unresolved (quarantined records that exist only in the old tables), and the fact that deletion can't be undone.
- Refuse by default if any quarantined records are unresolved. Make the engineer resolve or explicitly accept each remaining group.
- Offer a hold: "Remind me in 7 days" or "Take a final snapshot first." A snapshot is a cheap safety net for an irreversible step, so recommend it.
- Require a fresh confirmation, and ideally a second person for sign-off, since this is the point of no return. Approval of the job earlier doesn't count as approval of this.

## Two things I'd decide before building

1. **What happens to writes during the six hours?** If the old database is still taking writes, the cutover check can't promise that new data is complete. The answer changes the seam check-in and cutover screens most.
2. **Who is the backup contact?** The design assumes someone can respond to a page at 3 a.m. If that's nobody, set the failure thresholds more conservatively and let the run pause earlier.
