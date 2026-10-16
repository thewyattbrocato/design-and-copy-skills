Nothing is broken, but the spacing is the weak spot.

**Main issue: every gap is 16px.** Title to paragraph, paragraph to fields, field to field and fields to footer are all the same. That gives a flat rhythm with no grouping. Spacing should show which things belong together.
- **Title to paragraph:** tighten to about 8px, since they read as one header block.
- **Paragraph to fields:** 20–24px, to mark the start of the form.
- **Field to field:** 16px is fine. If each field has a label above it, keep the label-to-input gap at 4–8px so the label clearly belongs to its input.
- **Fields to footer:** 24px or more. At 16px the buttons look like another form row instead of a separate action area.

**Smaller things to check:**
- **Shadow:** a subtle shadow alone often doesn't separate a modal from the page. Make sure there's a dimmed scrim behind it, and use a slightly stronger shadow if the page behind is light.
- **Button gap:** use 8–12px between Cancel and Confirm. Cancel should be secondary or ghost, and Confirm should be the primary style.
- **Button label:** "Confirm" is vague. A specific verb like "Save changes" or "Invite" is clearer.
- **Close affordance:** the layout has no X button or Escape and backdrop-click dismissal. Add them unless the modal is meant to block.
- **Width and accessibility:** set a max-width (about 480–560px) and a responsive fallback for small screens. Also check focus trapping, initial focus on the first field, and `role="dialog"` with `aria-labelledby` pointing to the title.

The 24px padding and 20px title are fine.
