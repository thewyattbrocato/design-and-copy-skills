**I wouldn't drop the review for those customers.** The reasoning, "they obviously just click through," shows the review is cheap to pass, not that the run is correct. Three clean approvals say the customer trusted the earlier runs. They don't say the next run is right, and the review exists to catch the run that isn't. Autopilot failures tend to be new: a timesheet with an unusual format, a rate change, overtime crossing a threshold, a deploy that changes parsing. History from three runs doesn't cover those. A bad run that skips review lands in employees' bank accounts the next day, and for an 8-person business the owner may be the only person who would catch it.

The asymmetry settles it. Keeping the review costs a few seconds of a customer's time. Removing it risks wrong wages that are hard to recall, which means employee trust, possible wage-law exposure, and support load. Before anything like this ships, legal or compliance should weigh in on whether a payroll provider can skip customer approval at all.

If the goal is to reduce friction, I'd propose these instead:

1. **Make the review faster to pass, not absent.** Show a summary with deltas from the last run: total gross, each employee's hours versus their usual, new or removed employees, rate changes, and any overtime. Most runs then need one glance and one tap, and the screen only asks for real attention when something moved.
2. **Auto-approve only on a clean diff.** If the run matches the prior run within tight tolerances and has no flags, skip the button, but still send a notice with a short window to hold or cancel. This ties trust to the content of the run, not to the customer's history.
3. **Keep the hold window before the bank file goes out.** Support says money lands the next day, so a few hours of hold before submission costs little and is the best recall tool you have.
4. **Measure first.** How often does a review change something, and how often do customers correct a run after sending? If reviews almost never change anything and post-send corrections are near zero, a clean-diff auto-approve is a reasonable experiment. Start with an opt-in pilot and watch the correction rate.

So: don't remove the review for three-in-a-row customers. Make the review quicker for runs that look like the last one, and let the anomalies stand out.
