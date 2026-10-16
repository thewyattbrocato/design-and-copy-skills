**Prefill these**

| Field | Prefill from | Notes |
|---|---|---|
| Location | The location they have open now. If none is open, use the location of their most recent shift. | Show it as a visible, changeable control. If they have only one location, show it as plain text and not a picker. |
| Date | Today's date. If they arrived from a calendar day, use that day instead. | Constrain the picker so past dates are hard to pick. Don't show an error for something the picker could have prevented. |
| Start and end time | The most recent shift at that location with the same role. Fall back to the most common start and length in the last 20 shifts. | Match on location as well. A lunch pattern at one site shouldn't carry over to another. |
| Role | The chosen employee's usual role. If no employee is chosen yet, the role from the last shift. | Make it a visible, editable value. People cover other roles, so don't lock it. |
| Break length, notes, and other fields that rarely change | The last shift at this location. | Leave notes blank unless the manager is duplicating a shift. |

**Order matters.** Put location and date first, then role, then employee, then times. Each answer can then improve the next prefill. If the manager picks an employee, set the role from that employee's usual role. If they change the location, refresh the times. If they have already edited a field, never overwrite it silently.

**Leave these blank on purpose**

- **Employee.** Prefilling it risks scheduling the wrong person, and the manager will often skip past a wrong guess. Do a quick search or autocomplete. You can offer a short list of people who usually work that role at that location, but don't preselect one.
- **Anything that costs money or notifies someone.** Examples are overtime-triggering hours, pay rate overrides, and "notify employee" if it sends a message. Make these deliberate choices.
- **Notes and special instructions.** Copying them forward leaves stale text, such as "cover for Sam", on new shifts.
- **A field with no real pattern.** If the last 20 shifts show no common value, such as scattered start times, leave it blank. A wrong guess is slower to fix than an empty field.

**Make prefill safe**

- Prefilled values should look like real values in the control, not gray placeholder text. Managers need to see at a glance what will be saved.
- The button says "Create shift" and stays pressable.
- After saving, offer "Add another" that keeps the location, date and times. Managers building a week often create many similar shifts.
- Offer "Copy from a previous shift" as a separate shortcut for repeating a specific shift. Don't make it the default behavior.

Start with location, date and times, since they give the biggest saving. Add role and employee-driven prefill after that.
