I've assumed the old database stays live during the copy, so a catch-up pass picks up changes before cutover. I've also assumed the engineer isn't the only person who can be paged overnight. If either is wrong, the design changes. Every threshold below is a placeholder for you to set.

**What the engineer is promised:** "While you're away it will copy and validate batches, set aside records that fail, and stop safely if things go wrong. It will never switch the app to the new database or delete old tables without your approval, and it never changes the old database."

## Before the run

- **Editable plan with the stop points marked.** The steps are preflight, copy and validate, catch-up pass, **ask to cut over**, watch period, and **ask to delete**. The run ends at "ready for cutover" and waits. Cutover happens with a person present, not at 4am.
- **Dry run on a small sample.** It copies and validates into a scratch target and shows what it would quarantine and why. This is where validation rules get fixed cheaply.
- **Limits stated as caps.**
  - Halt if the failure rate exceeds [X]%.
  - Halt after [N] consecutive failed batches.
  - Halt on target database errors or lag above [Y].
  - Concern notices start at [half of each limit].
- **Cover named.** The engineer picks who gets paged for a halt overnight. If nobody is named, the run can't start.
- **Preflight checks.** Verified backup of the old database, target capacity, and a restart that is safe (batches are idempotent). Anything failing blocks the start.
- **Restated instruction with examples,** for example: "A record with a missing billing address is quarantined, not copied. A record that differs only in whitespace is copied."

## During the run

**One status home:** running or paused, current step, batches done and remaining, last batch and when, next check, copied / quarantined / retrying counts, and each limit with how close it is. Pause and Stop sit one click away.

- **Pause** keeps the working state and accepts new direction.
- **Stop** keeps finished batches, lists any half-done batch, and never restarts on its own.

**Messages, by kind:**
- **Problem (pages the named person):** the run has halted. "Halted at batch 412: failure rate passed [X]%. Nothing is lost, and copied batches are intact. Most failures share one cause: [reason]. Resume, fix rule, or stop." The agent stays halted until someone responds.
- **Concern (chat, no page):** "Failures are at [60%] of your halt limit and rising. Cause: [reason]. Still running. Next update in [N] batches or on any change."
- **Check-in:** one proof-of-life line at an interval they choose, so silence doesn't look the same as broken.
- **Completions:** none per batch. They go into the morning digest.

**Quarantined records** go to a list, not the log. They're grouped by failure reason, each with the record, the reason, and its own controls: retry, fix and retry, or exclude with a note. Low-confidence items come first.

**Fixing a bad rule** has two options:
- **"Not this record"** excludes or retries a single record.
- **"This kind of failure"** edits the rule. It's shown in plain words with a preview of what it would newly catch, what barely qualifies, and what barely misses. Batches already run under the old version are marked, and affected ones can be rerun.

## At the seam: ready for cutover

The engineer opens a two-line summary: the goal as it now reads, what the agent assumed, and what it will do next. The summary gives:
- The reconciliation between old and new databases, with both error counts. Don't show "99% valid" alone.
- The quarantine list, with doubtful items first.

**Unresolved quarantined records are the key problem.** After cutover, those customers would be missing from the new database. So by default, cutover stays blocked until every failed record is fixed or explicitly set aside with an owner and a reason. Setting records aside is a conscious choice, not a default.

**The cutover approval** names the action, the target, and the consequence: "Switch the app to read from the new billing database." The default scope is this once.

**It states what rollback cannot reach.** Reverting reads to the old database within the week is available. Writes made to the new database after cutover won't exist in the old one unless you sync them back. Say this in the approval, not in documentation.

## The week after cutover

The status home stays up and shows "Old tables kept until [date]," with new-database error rates and the open quarantine count. Rollback is one step away. Concern notices fire if error rates drift toward a limit you set.

**Deletion is a separate approval, not a timer.** It can't be deleted automatically on day seven. Staged reminders arrive before the date. The request lists the tables, row counts, and confirmation that the backup is verified. It's blocked while any quarantine record is unresolved. It runs after a short hold. If nobody responds, nothing is deleted and the tables simply stay. The engineer can postpone with one click. Say plainly that deletion can't be undone, and that the backup is the only recovery.

## Final report

It's a change set, not a total: what was copied, what was quarantined and how each was resolved, and which rule version each batch ran under. It also lists everything the engineer approved, with times and names.

**Leaving at any point:** abort needs no reason and says what happens to the work in flight. A human contact for the platform team appears on every page and message.
