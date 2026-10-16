**Prefill (with a clear way to change it)**

| Field | Prefill from | Notes |
|---|---|---|
| Location | The location they have open now. If they have only one, it's fixed. | Highest-confidence default. Show it as an editable selector, not locked text, for multi-location managers. |
| Date | Today's date, or the next day after the most recent shift they created if they're clearly building a week. | Today is a safe fallback. "Next day after last created" helps batch entry, but only apply it if the last shift was created in this session. Otherwise you'll surprise people. |
| Role | The employee's usual role, once an employee is chosen. | Updates when the employee changes, unless the manager already edited role by hand. |
| Start/end time | The most recent shift at the same location with the same role (or same employee, if picked). | Better than a global "last shift" because lunch and closing patterns differ by role. |
| Break length | Same source as times. | Low risk, since it's usually identical. |
| Notes | Leave blank (see below). | |

**Smart behaviors that cut more typing than prefill alone**
- **"Duplicate shift" / "Repeat"** on recent shifts. For many managers this beats any prefill, because shifts come in patterns.
- **Recent-shift suggestions** as one-tap chips (for example "Server 10:00–16:00") built from the last 20 shifts, ranked by frequency at the current location.
- **Sticky values within a session.** After saving, keep location, role, and times for the next shift and clear only the employee.

**Leave blank on purpose**
- **Employee.** This is the actual decision. A wrong guess (the last person scheduled) gets saved by mistake, and it can cause availability, overtime, or double-booking problems.
- **Notes / instructions.** Copying old notes forward creates stale or wrong instructions ("cover for Sam").
- **Anything with pay or cost implications** (pay rate overrides, premium or holiday flags, overtime acknowledgments). Silent defaults here turn into payroll errors. Derive them from rules, not from the last shift.
- **Open/unassigned and published/notify toggles.** Default to the safe state (for example draft, no notification) rather than copying the last choice, so a manager doesn't accidentally notify staff.

**Practical rules**
1. Make every prefilled field visibly editable, and mark prefilled values subtly (for example a "suggested" style) so they aren't mistaken for deliberate choices.
2. Prefill only when confidence is high. If the last 20 shifts at this location show no dominant time pattern, leave times blank rather than showing a poor guess.
3. Don't let a prefilled value silently override one the manager typed. If they set the role first, don't change it when they pick an employee.
4. Check for conflicts (double-booking, availability) after prefill, since prefilled times can create them without the manager noticing.

If you can only ship one thing first, ship location + date + role-from-employee, then add the recent-shift chips.
