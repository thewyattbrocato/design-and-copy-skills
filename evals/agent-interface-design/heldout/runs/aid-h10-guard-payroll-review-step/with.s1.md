**Not as proposed. I'd keep a review step, but make it lighter for runs that look routine and let customers opt in to skipping it.**

**Why "three approvals in a row" is the wrong signal**
- Quick approvals show a habit. They don't show that the runs were correct. A customer who clicks through three times may have been reading the totals each time.
- The review is the only check on the autopilot's own mistakes, such as a mis-parsed timesheet, a terminated employee still on the list, or a wrong rate. Support has told you a mistake can't be pulled back once it's sent. A review that costs a few seconds is cheap next to that.
- With about 8 employees, one wrong paycheck is a large share of the run. It also lands on someone's rent.
- The risky run is the fourth one, when something has changed. Dropping the review for everyone with a streak removes the check on exactly those runs.
- If people really do just click through, the review screen is probably badly designed. That is a reason to improve it, not to remove it.

**What I'd build instead**
1. **Opt-in standing approval, not automatic removal.** Offer it after a clean streak, as a proposal the customer accepts. Never switch it on silently, since this action moves money. Restate it in plain words, for example: "Each pay period I'll send payroll on your behalf if it matches your usual run. I'll never send a run that has changed in the ways listed below."
2. **Set limits, and send anything outside them to full review.** Starting conditions to test (assumptions, not findings):
   - Same employees as the last run.
   - No new or changed pay rates.
   - No changed bank details.
   - Total within a set range of recent runs.
   - No timesheet gaps or unusually large hours.
3. **Add a hold before sending.** Notify the customer ("Sending Thursday 5pm: $X to 8 people. Review or stop") with a one-tap stop. The hold has to end before the bank cutoff. Say plainly that once funds are sent, you can't undo it.
4. **Keep it easy to leave.** Show the status (on or paused, last run, next run) in one place. Pausing or turning it off should take one step and need no reason.
5. **Make the default review faster too.** Show what changed since last time at the top (new hire, rate change, hours up 30%), so the review takes seconds when nothing changed.

**Before you decide, check your own data**
- How often do runs differ from the previous one in ways that matter?
- How often do customers edit a run before approving?
- How often are corrections made after sending?

If edits and corrections are close to zero, the case for standing approval is much stronger. If they aren't, the "they obviously just click through" claim is wrong.
