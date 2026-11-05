# New shift: what to prefill

## Prefill

| Field | Prefill from | Notes |
|---|---|---|
| **Location** | The location they have open right now. | If they belong to only one, show it as plain text instead of a field. Keep it changeable, because managers sometimes build another site's schedule. |
| **Date** | Today's date, or the date they were viewing if they opened "New shift" from a day or cell in the calendar. | A calendar click beats "today". Don't prefill a past date. |
| **Start and end time** | The start and end of their most recent shift at this location. If the last few shifts differ, use the most common pair among the last 20. | Show the end time as a duration too ("8 hrs") so a wrong default is obvious. Prevent an invalid state instead of erroring on it. For example, let overnight shifts roll to the next day with a visible "ends next day" cue. |
| **Role** | The selected employee's usual role. | If no employee is chosen yet, use the role from their last shift at this location. Changing the employee updates the role only if the manager hasn't edited it by hand. |
| **Break** | Whatever the last shift at this location used. | Only if you have a break field. |
| **Notes** | Nothing. | See below. |

If the manager clicked an employee's row, prefill that employee and their role from the calendar. That context is stronger than anything from history.

## Leave blank on purpose

- **Employee.** A wrong prefill here means someone gets scheduled by accident, and it's easy to miss when saving quickly. Make the manager pick, but put people who usually work this role, day and location at the top of the list.
- **Notes.** Carrying over last week's "cover for Sam" would be wrong and embarrassing. Copying it silently is worse than typing it fresh.
- **Anything that notifies or commits**, such as "publish to employee" or "send alert". Don't default it to on based on past behavior. Make it an explicit choice, or put it on the button ("Save shift" and "Save and notify").
- **Pay rate and overrides**, if they exist. Take them from the employee record, not from the last shift.

## Practical rules

1. **Show the defaults in the fields.** Don't hide them behind a "use last shift" link. Prefilled fields should look like real values the manager can read and overwrite in one keystroke.
2. **Tell people what you prefilled.** A one-line hint such as "Times from your last shift at Downtown" under the time fields lets them trust or ignore it. This matters most for times, where a wrong default looks plausible.
3. **Use recency per location, not globally.** A manager with two locations probably has different hours at each. Pull the last shifts only from the open location, and refresh the defaults if they switch location before editing anything.
4. **Order the form by how fast it can be done.** Employee first, since it drives role and suggestions. Then date and times, which are usually already right. Then everything else.
5. **Add "Save and add another".** It keeps the date, location and times for the next shift. Entering a block of similar shifts is where the biggest time savings are, more than prefilling the first one.
6. **Don't prefill empty history.** For new managers with fewer than a few shifts, fall back to blank times instead of a guess from one data point.

Worth testing: track how often managers change each prefilled field. If a default gets overwritten more than about half the time, it isn't helping and should go back to blank.
