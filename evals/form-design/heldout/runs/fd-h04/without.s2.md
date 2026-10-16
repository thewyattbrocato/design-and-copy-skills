# New shift: what to prefill and what to leave blank

## Prefill

| Field | Source | Notes |
|---|---|---|
| **Location** | The location they have open right now. | If they belong to only one location, hide the field. Otherwise show it as a changeable default. |
| **Date** | Today's date by default. | Better: if they're working in a week/day view of the schedule, use the day they clicked. If the last shift they created was for a future date, "next day after that" is often right when they're building a week. |
| **Start and end time** | The most common start/end among their last 20 shifts at this location, ideally for the same role and day of the week. | If the pattern is weak (no time appears in at least a few of the 20), fall back to the most recent shift's times. |
| **Role** | The most recent role used at this location, or the mode of the last 20. | If an employee is chosen first, switch to that employee's usual role. |
| **Break length** | Copied from the most recent similar shift. | Only if your tool has this field. |
| **Position or station, and notes** | Copy only if it was identical on the last few shifts. | Otherwise leave blank. |

**Order matters.** Let the employee be picked first or last, but make the dependencies run both ways:
- Choosing an employee sets the role to their usual role, unless the manager has already set the role by hand.
- Choosing a role first filters the employee list to people who work that role.

**Also offer "Duplicate last shift".** For managers entering a week of similar shifts, this is faster than smart defaults. Put it next to "New shift", or show recent shifts as one-tap templates ("Server, 5–11pm").

## Leave blank on purpose

- **Employee.** A wrong guess here is costly. It could assign the wrong person, trigger a notification, or create an overtime or availability conflict. Make it a fast typeahead, and optionally suggest people who are available and usually work that role. Don't preselect.
- **Anything that notifies or commits.** Examples are "publish to staff", "notify employee", and "open shift for pickup". Use a safe default (draft or unpublished), and don't carry over the last choice.
- **Pay rate or cost overrides.** These should come from the employee or role, not from the last shift. If there's no rule for them, leave them blank.
- **Fields where the last value is a bad predictor.** One-off notes, special-event flags, and swap or coverage reasons all belong here.

## Guardrails

1. **Make prefilled values visible and cheap to change.** Show them as normal, editable values, not greyed placeholders that look empty. Place focus on the first field that probably needs changing (usually employee).
2. **Never silently prefill something that causes harm if missed.** Date and location are fine because they're obvious on screen. Employee isn't.
3. **Fall back gracefully.** A new manager, a new location, or a location with fewer than about 5 shifts should get plain sensible defaults (today's date, the open location) rather than a pattern from thin data.
4. **Scope history by location.** A manager with several locations shouldn't get times from a different restaurant's rhythm.
5. **Measure it.** Track how often managers change each prefilled field. If a field is changed more than about 40–50% of the time, the default isn't helping, so make it blank or change the logic.

If you can only build three things, build these: the location default, the date from the clicked day, and times plus role from recent history. Add "Duplicate last shift" as well.
