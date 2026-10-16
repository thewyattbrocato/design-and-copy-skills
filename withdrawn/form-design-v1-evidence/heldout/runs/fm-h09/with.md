**Recommendation: three separate day, month and year fields, with a format hint. Don't use a calendar picker.**

**Why not a date picker.** A birthdate is far from today. For someone born in 1971, a calendar widget means paging back decades or finding a year dropdown. Native pickers also differ a lot between phones and desktops. Typing is faster for a date the person already knows.

**Why three fields over one text box.** A single free-text box invites format confusion (03/14 vs 14/03) and needs parsing and error handling for every variant. Three labeled fields make the order explicit and avoid the ambiguity.

**Spec**
- **Label:** "Date of birth" as a visible label above the group, with a hint between the label and the fields: "For example, 14 3 1988".
- **Fields:** Day, Month, Year, each with its own visible label. Use `type="text"` with `inputmode="numeric"` for the numeric keypad. Don't use `type="number"`, because the spinner is wrong for dates.
- **Widths:** Day and month about 2 characters wide, year about 4. The width hints at the expected length.
- **Text size:** 16px or larger, so phones don't zoom on focus.
- **Autofill:** `bday-day`, `bday-month` and `bday-year`.
- **Input handling:** Accept "3" and "03". Don't auto-advance focus between fields, because it breaks corrections and screen readers.
- **Order:** Match the order your audience expects. Put day-month-year or month-day-year in the hint so it matches the field order.
- **Validation:** Check on submit only. Once a field shows an error, re-check it as the person edits. Check that the date is real (no 31 Feb) and in the past.
- **Error text:** Put it at the field, with a cue other than color. For example: "Enter a date of birth in the past, like 14 3 1988." For a specific failure, name the part: "Month must be between 1 and 12."
- **Required or optional:** Say so in words. If you only need to confirm they're an adult, consider asking "Are you 18 or over?" instead of collecting the full date. Collect the full date only if the enrollment system needs it. Ask for what you actually need.

**Why not three dropdowns.** Dropdowns work, but they're slower on desktop (scrolling through about 100 years) and clumsy on phones. Typing 14, 3, 1988 takes a few seconds. If your team has a strong convention for selects, a month dropdown with typed day and year is an acceptable compromise, since month names help people avoid day/month mix-ups. A full set of three selects is the weakest option.

If you share the markup or component library you use, I can write the field or check what you already have.
