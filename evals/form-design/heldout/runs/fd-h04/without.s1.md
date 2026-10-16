**Prefill these**

| Field | Prefill from | Notes |
|---|---|---|
| Location | The location they have open now. If none, their only location. If several, the location of their most recent shift. | Show it clearly so a wrong location is obvious. Location drives employee lists and roles, so get it right first. |
| Date | The calendar cell or day they came from. Otherwise the day after their most recently created shift. Otherwise today. | Today is the weakest guess. Managers usually schedule days ahead, so only use it as the last fallback. |
| Start and end time | The most common start/end pair in their last 20 shifts at this location. If a role is already set, use the pair for that role. | Use the mode, not just the last shift. One odd shift shouldn't set the default. |
| Role | The selected employee's usual role. | Only when an employee is chosen. See below. |
| Break length | The most common value in their recent shifts. | Low risk and easy to edit. |
| Status | Draft, or whatever your safe default is. | Don't default to published. |

**Leave these blank on purpose**

- **Employee.** A wrong employee means a wrong notification, a possible overtime or availability conflict, and a person who thinks they're working. A blank employee also has a valid meaning (an open shift), so a prefilled name would hide that option. Make picking one fast with a recent-employees list, but don't choose for them.
- **Notes and special instructions.** Carrying these over from an old shift puts stale text in front of staff.
- **Recurrence or repeat.** It should be off unless the manager turns it on. An accidental repeat creates many wrong shifts.
- **Pay or rate overrides and anything with cost implications.** Show the inherited value read-only, but don't invite edits.
- **Role, when no employee is chosen.** If the last 20 shifts don't show one clear dominant role (say, over about 60%), leave it blank. Otherwise you're guessing.

**Mechanics that make it work**

1. **Order the fields so choices cascade.** Put location first, then employee, then role, then times. Picking an employee fills the role, and the role can refine the times.
2. **Keep prefilled values editable and visible.** Don't collapse them behind a "use defaults" toggle. Managers should see what was filled and change it in one tap.
3. **Don't overwrite manual edits.** If the manager changes the start time and then picks a role, leave their time alone.
4. **Add "Duplicate a recent shift" as an escape hatch.** It covers cases where the mode-based guess is wrong, such as a manager who runs very different openers and closers.
5. **Skip prefilling when the data is thin.** With fewer than about 3 relevant recent shifts, leave times blank rather than infer a pattern from noise.

**What to check in testing:** how often managers edit each prefilled field. If one gets changed more than about 40% of the time, the default is probably hurting more than helping. Switch it to blank or change how you derive it.
