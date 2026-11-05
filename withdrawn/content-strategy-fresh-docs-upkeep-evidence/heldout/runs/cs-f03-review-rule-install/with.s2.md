# Brindlemoor install guide: review rule

**Why:** Last release the guide went out unreviewed and step 6 was wrong. A customer lost a day. Silence from reviewers must never count as approval for this guide.

## Roles

| Role | Who | Does |
|---|---|---|
| Owner | `[name]` | Decides what goes in. Settles reviewer conflicts. Has the right to hold a release. |
| Step-runner | `[name]` (a second person if the owner wrote the change) | Runs every changed step on the release build. |
| Reviewer | `[name per area, e.g. support, engineering]` | Checks accuracy within their area. |

## The rule

1. **Run the steps.** The step-runner follows the guide from step 1 on the **release build**, not the previous one. Reading it through doesn't count. Record who ran it, the build, and the date at the top of the review ticket.
2. **Ask reviewers early.** Send the draft to named reviewers as soon as it's ready, not on release day. Each reviewer has one area and `[N]` working days to reply. Send all reviewers the draft at once and collect the comments in one place. The owner merges them.
3. **Silence means different things by step type.**
   - Steps that **change or delete data, change security or access, or can leave the system unusable if wrong:** silence is *not* approval. Nobody has run them, so they can't go out as verified.
   - Everything else: if a reviewer hasn't answered after `[N]` days, the owner pings them once. After one more day the page ships on the step-runner's verification alone.
4. **If the run isn't done by release day**, the guide either ships with an "Unverified, last tested on `[build]`" banner on the affected steps, or the owner delays it. The owner decides which. Nobody publishes it as "verified" without a run.
5. **Product changes bring doc changes.** A change to an install step, a version, a limit or a default is done only when its guide change is in the same release. Before release, the change author lists every page that mentions the changed value, including screenshots and the troubleshooting section.

## If a release is urgent

The owner may call the short path: the step-runner runs only the changed steps, one reviewer signs off, and the owner posts in `[channel]`. The full run follows within `[days]` days.

## After a mistake

If a customer reports a wrong step, log it: the symptom, the step, and the fix. The owner triages it within `[days]` days and corrects the guide. If the cause was a skipped run, say so in the log.

---

I assumed the install steps can affect data, access or system state, which is why they fall under the "silence is not approval" rule. If they're purely informational, drop rule 3's first bullet. I left names, the reply window `[N]` and the channel as placeholders because I don't know them. Your manager needs to fill those in, and the owner row must name a real person. A rule with no named owner is how the last release happened.
