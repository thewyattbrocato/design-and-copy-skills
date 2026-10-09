**Recommendation: headings plus extra space, with no cards or lines.**

12 fields in 3 short sections is a small form. Small forms don't need heavy containers.

- **Cards** add borders, padding, and nesting. For 12 fields, that's more visual weight than the content justifies. Cards also shrink the usable width, which hurts on mobile. They make sense when sections are independent, collapsible, or saved separately. They also help when a form is long enough that users need landmarks.
- **Horizontal lines** are the weakest option. They separate sections but don't name them, so you still need headings. They also add clutter without much grouping benefit.
- **Headings and whitespace** group things through proximity. Use roughly 32–40px between sections and 16px between fields within one. A clear heading sits above each section. This is clean, accessible, and responsive.

**Implementation notes**
- Use `<fieldset>` and `<legend>` (or a heading with `aria-labelledby`) so screen readers announce the groups.
- Make the spacing between sections clearly larger than the spacing between fields. That ratio does the grouping.
- Make the headings distinct in size or weight.
- The 3 toggles can sit in a tight list under "Preferences". They'll look different from the text inputs, so they need little extra separation.

**When I'd change this**
- Sections save independently, or users edit them separately, as on a settings page. Use cards.
- The form grows to 5+ sections or becomes long. Add cards, or a light divider between sections.
- The form sits on a busy or tinted background. A card or white panel can help legibility.

If you tell me what the form is for (onboarding, a settings page, or checkout), I can adjust this.
