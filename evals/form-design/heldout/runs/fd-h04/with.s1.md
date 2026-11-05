Prefill a field when the guess is right most of the time and a wrong guess is obvious and cheap to fix. Leave it blank when a wrong guess would be accepted without anyone noticing, or when the field is the actual decision. I'm assuming the usual fields: location, date, start and end time, employee, role, break, notes and repeat.

## Prefill

| Field | Prefill from | Notes |
|---|---|---|
| **Location** | The location they have open now | If they have only one, don't show it as a field. Show it as text in the heading. |
| **Date** | The day they clicked in the calendar. Otherwise the date of the last shift they created. | Don't default to today. Managers mostly schedule ahead, and a same-day shift accepted by accident is costly. Use today's date only to stop the picker from allowing past dates. |
| **Start and end time** | The most common pair among their last 20 shifts at this location | The most common pair beats the last one, which may have been a one-off. Show them as real values in the field, not grey placeholder text. |
| **Role** | The chosen employee's usual role | This only works if the employee comes first. If the manager picks the role first, filter the employee list by it and leave the employee blank. |
| **Break length** | The most common value in the last 20 shifts | Same method as the times. |
| **Repeat** | "Does not repeat" | This is a safe default. A wrong "repeats weekly" creates a lot of bad shifts. |

## Leave blank on purpose

- **Employee.** This is the main decision on the screen. A wrong prefill gets saved, and the wrong person may get notified. Make it quick to fill with a searchable list that puts people from recent shifts first. Offer "Open shift (unassigned)" as an explicit choice.
- **Notes.** Notes are specific to one shift, and a carried-over note will be wrong.
- **Anything with pay or cost impact**, such as overtime flags or rate overrides. Set these deliberately.

## Practical details

- Show prefilled values as ordinary editable values, with the same styling as typed ones. Don't use grey placeholder text, because people read that as empty.
- Validate on save, not on load. Prefilled values shouldn't open with errors showing.
- Add a "Copy a recent shift" action that lists the last few shifts. It covers the cases where the guessed times or role are wrong, and it's often faster than editing fields.
- After "Save and add another", keep the date, location and times. Clear only the employee and notes. Managers often enter a whole day's shifts in one sitting.
- Prefill is a guess, so don't hide the fields it fills. Use an "Edit" toggle only if it's a lot of fields.
