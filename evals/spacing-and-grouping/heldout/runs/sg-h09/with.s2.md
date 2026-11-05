**Use extra space and headings only.** Skip the cards and the horizontal lines.

**Why this fits your form**
- Twelve fields in three sections is a small, single-level form. Space can show the grouping without help.
- Cards are for discrete objects, such as things you open, select, or compare. Personal info, Address, and Preferences are sections of one task, so boxing them adds borders and padding without adding meaning. Cards also shrink the width available to fields and push you toward nested surfaces.
- Rules are for dense lists or places where space can't do the separating. Here they would only repeat what the gaps already show.

**How to make the space work**
- **Within is smaller than between.** Use about 16px between fields in a section (a 4px-base scale step). Use about 40–48px between sections, at least 2× the within-gap.
- **Headings sit closer to their content than to the section above.** Put about 40px above a heading and about 16px below it. Never use equal space on both sides, or the heading floats.
- **The container owns the gaps.** Use `gap` on a flex or grid parent, or a rule on the following sibling. Avoid `margin-bottom` on every child, which doubles the space after the last item.
- **Keep every value on the scale.** Use something like 4, 8, 16, 24, 40, 48, and no one-off numbers.
- **Align everything to one left edge.** Labels, fields, and headings should share it.

**Preferences needs the most care**
Three toggles are a different kind of row from text inputs. Give each toggle row the same height and 8–12px between rows, with the label on the left and the switch on the right. If a short description sits under each label, keep it tight to its label. If the section feels too close to Address, add space before the heading rather than a divider.

**When I'd change this**
- Add a hairline rule only if you later add many tightly packed rows, or if testing shows people missing the section breaks.
- Use cards only if the sections become independent objects, for example separately editable or saved with their own buttons.
- If the form sits on a busy background, put the whole form on one surface rather than boxing each section.

Squint at the page or blur it. You should see exactly three groups. If two sections merge, increase the between-gap rather than adding a device.
