Prefill anything the tool can predict reliably and a manager would otherwise retype. Leave blank anything where a wrong guess would be saved without anyone noticing.

## Prefill these

| Field | Prefill from | Notes |
|---|---|---|
| **Location** | The location open right now. If none is open, use the location of their most recent shift. | If they have only one location, don't show the field. |
| **Date** | The calendar cell they clicked, if they came from one. Otherwise today. | Managers often schedule ahead, so if most of their last 20 shifts were created for future dates, use the date of the latest one instead. Check this against your data. |
| **Start and end time** | The most common start and end times among their recent shifts at that location. | Use the same role when you know it. If there's no clear pattern, use the last shift's times. |
| **Role** | The chosen employee's usual role. | This depends on the employee, so it fills after the employee is picked. Keep it editable, because people cover other roles. |
| **Break length** | The most common value in their recent shifts at that location. | Only do this if you store breaks. |

## Leave these blank on purpose

- **Employee.** It's the main decision on the screen. A wrong guess means someone gets scheduled by accident. Offer an explicit "Open shift (unassigned)" option so blank doesn't read as forgotten.
- **Repeat or recurrence.** Default to "Does not repeat". A wrong guess here creates many bad shifts at once.
- **Notes.** They're specific to each shift.
- **Notify the employee.** Follow the manager's existing notification setting. Don't infer it from past shifts.

## Behavior rules

- Put prefilled values in the fields as real values, not as grey placeholder text. The manager can see them and overwrite them.
- If the manager changes location, refresh the time and break suggestions. Only refresh fields they haven't edited yet.
- Block past dates in the date picker, or warn on them if backfilling is a real use case. Don't show an error.
- Add a "Copy a recent shift" shortcut for cases where the last 20 shifts show several distinct patterns, such as opening and closing shifts. Without it, one set of prefilled times would be wrong half the time.
- Keep the Employee field first in the focus order after the prefilled fields, so the usual flow is: open the screen, pick a person, check the details, save.
