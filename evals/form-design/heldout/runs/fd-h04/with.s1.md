I'm assuming the usual fields: location, date, employee, role, start and end time, break, notes, and repeat. Prefilled values should be visible in the control and easy to change. Never apply them silently.

## Prefill

| Field | Prefill from | Notes |
|---|---|---|
| **Location** | The location open right now | If the manager has only one, show it as text, not a control. If they have several, keep a select. This is the highest-value default, because a wrong location puts the shift on the wrong schedule. |
| **Date** | Today, or the date of the schedule view they came from | If they opened "New shift" from a day or week column, use that day. Today is the fallback. |
| **Start and end time** | The most common start and end among their last 20 shifts at this location | Use the mode, not the last shift, so one odd shift doesn't skew it. Better still, key it to the role: once a role is chosen, switch to that role's typical times. |
| **Break** | Same as the times, taken from recent shifts with the same role or length | Only prefill if the pattern is consistent. |
| **Role** | The selected employee's usual role | This only applies if the employee is chosen first (see below). |
| **Repeat** | "Does not repeat" | Only prefill a repeat pattern if the manager has created repeating shifts in most of their last 20. |

## Leave blank on purpose

- **Employee.** A guessed employee is the costliest wrong default. It looks finished, gets saved unnoticed, and puts the wrong person on the schedule. You can help without prefilling: sort the list by who is likely (usual role, available, not already scheduled) and let the manager pick.
- **Notes.** There's no pattern to predict, and the field is optional anyway. Label it "optional".
- **Anything that notifies or commits people.** This includes "notify employee" and "publish". Show these as a visible choice, not a hidden default. If you do default them, show the default in the control.

## Field order

Put **employee first** if you can. Choosing them fills role, and the role fills the times. The manager answers one question and three fields follow. If your managers think "I need a closer Friday" rather than "I need Sam", put role first instead and filter employees by it.

## Rules to keep it safe

1. **Prefilled values must look editable and be visible.** Don't use gray placeholder text, which reads as empty. Use real values.
2. **When a change cascades, say so.** If picking a role changes the times, update them, but not if the manager has already edited the times by hand. Don't overwrite manual input.
3. **Prefill only when the pattern is strong.** For example, if one start time covers about 60% or more of recent shifts, use it. Otherwise leave the field blank rather than showing a coin-flip guess.
4. **Keep the button pressable and specific.** "Add shift" is better than "Submit". After a save, keep the manager on the form with the location and date retained, so they can add a second shift in a few seconds.
5. **Offer "Duplicate shift"** on existing shifts as a second route. For many managers it will beat any prefill.

I left the thresholds out on purpose, because they should come from your real shift data. If you can look at the last 20 shifts for a handful of managers, check how often the mode start time matches the next shift before you commit to the defaults.
