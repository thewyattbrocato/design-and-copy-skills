I'm assuming the usual shift fields. Swap in your own names if they differ.

## Prefill

| Field | Prefill from | Notes |
|---|---|---|
| **Location** | The location open right now. | If the manager has only one location, don't show a picker, just print the name. |
| **Date** | Today's date. | Better: if their recent shifts cluster on a pattern, such as always scheduling next week, default to the next date they're likely to schedule. Start with today and add this only if the data supports it. |
| **Start and end time** | The most common start and end among their last 20 shifts at this location. | Match on location, since a breakfast spot and a bar differ. Use the mode, not the last shift. |
| **Role** | The role of their most recent shift at this location. | This is the fallback when no employee is chosen. |
| **Role, once an employee is chosen** | That employee's usual role. | It overwrites the default role only if the manager hasn't touched the role field. |
| **Break length** | The most common value in recent shifts. | Leave it blank if recent shifts vary widely. |
| **Repeat** | "Does not repeat". | Never default to repeating. |

Show every prefilled value in the field itself as a real, editable value, not placeholder text. That way the manager can see it and change it. When a value came from history, add a quiet hint such as "Usual for Downtown". Don't make the manager hunt for what was filled.

## Leave blank on purpose

- **Employee.** A wrong guess here puts the wrong person on the schedule, and the manager may not notice. Make it a fast autocomplete. You can sort recently scheduled people to the top, but don't preselect anyone.
- **Notes.** Prefilled notes from old shifts would go stale and leak into new shifts.
- **Anything that notifies or commits someone**, such as "notify employee" or "publish". Default to the safer, reversible state, and state it in the label.
- **Pay rate or overrides**, if you have them. A copied exception is a silent payroll error.

## Rules that keep prefill safe

1. **Don't prefill across locations.** If the manager switches location, re-derive times, role and break from that location's history. Don't overwrite fields they've already edited.
2. **Use the mode, not the latest.** A single odd shift shouldn't set the defaults.
3. **Fall back to blank.** With fewer than about 3 relevant shifts at a location, leave times blank rather than guessing from noise.
4. **Consider "Duplicate shift" as a separate entry point.** It covers the case where they want to copy a specific shift exactly. It's cheaper than trying to predict everything on the blank form.

Test this with managers: if they usually change the prefilled time, your rule for choosing it is wrong, and blank would serve them better.
