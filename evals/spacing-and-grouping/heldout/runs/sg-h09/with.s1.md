**Use extra space and headings only.** Skip the cards and the horizontal lines.

**Why this works for your form**
- Twelve fields in three sections is a small form with one level of grouping. Space and headings are enough to show that grouping.
- Cards suit discrete objects that people open, select, or compare. Form sections aren't that. Boxing each one adds borders and padding without adding meaning. It also shrinks the field width inside each box.
- Rules need space on both sides to work. If you already have that space, the rule is redundant and just adds visual noise.

**How to make it read clearly**
- **Within is smaller than between.** Space between fields inside a section should be about half the space between sections. For example, use 16px between fields and 40px between sections (steps from a 4px scale).
- **Headings sit closer to their content than to the section above.** Put about 2× more space above a heading than below it, for example 40px above and 16px below. This is what keeps a heading attached to its own fields.
- **Let the container own the gap.** Use `gap` on the form or section wrappers, not `margin-bottom` on each child. That avoids doubled space after the last item.
- **Make the heading clearly distinct.** Use a heavier weight or slightly larger size than the field labels.
- **Keep toggle rows tappable.** Use about 44px row height with at least 8px between them. The Preferences toggles are the section most likely to look cramped.

**When to change this**
- **Add a hairline rule** if the sections get long or dense enough that space alone stops separating them, or if the form sits among other busy content.
- **Add a tinted region or card** only if one section is a distinct object. An example is Preferences that save independently with their own button. A card then makes sense for that section alone.

**Quick check:** Squint at the form. You should see exactly three clusters. Each heading should look closer to its fields than to the section above it.
