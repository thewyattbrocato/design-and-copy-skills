Nothing is broken, but the spacing is flat, and that's the main thing I'd change.

**Spacing**
- Every gap is 16px, so the title, paragraph, fields and footer all read as one stack. Spacing should show grouping.
- Tighten title to paragraph to about 8px, since the paragraph belongs to the title.
- Keep 16px between the two fields.
- Increase paragraph to fields to about 20–24px, and fields to footer to 24px. The footer is a separate action zone.
- Keep the 24px outer padding. It's consistent with the 24px footer gap.

**Smaller points**
- **Button gap:** you didn't specify one. Use 8–12px between Cancel and Confirm.
- **Button styling:** Cancel should be secondary or ghost, and Confirm primary. If Confirm is destructive, style it that way and label it specifically, for example "Delete" instead of "Confirm".
- **Shadow:** a subtle shadow is fine on its own, but the modal also needs a dimmed scrim behind it. Otherwise it won't separate from the page.
- **Field labels:** check that each field has a visible label, and that error text has room to appear without shifting the footer. A 16px gap can get cramped when validation messages show up.
- **Title size:** 20px is reasonable. Confirm the line-height is set, since the 16px gap is measured from the text box, not the glyphs.
- **Behavior:** if it isn't already there, add a close affordance (X or Esc), focus trapping, and initial focus on the first field.

If the design system already mandates a single 16px rhythm, then what you described is consistent with it and fine to ship. Otherwise I'd make the spacing changes above.
