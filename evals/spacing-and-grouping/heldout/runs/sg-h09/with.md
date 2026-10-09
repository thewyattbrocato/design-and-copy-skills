**Use extra space and headings only.** Don't add cards or horizontal lines.

**Why this fits your form**
- You have three sections and 12 controls in total. Space and headings can show that grouping without extra visual weight.
- Cards are for discrete objects, such as something you open, select, drag or compare. A form section isn't one of those. Wrapping each section in a box adds borders and padding without adding meaning. It also leaves you with nested surfaces, because the inputs already have their own borders.
- Rules are for dense, many-row lists where space alone can't separate the items. Three short sections don't need them.

**How to do it**
- **Within is smaller than between.** Keep fields in a section close together, for example 16 px between fields. Put at least twice that between sections, for example 32–40 px.
- **Headings sit closer to what they introduce.** Use about 32–40 px above a section heading and 12–16 px below it. A heading with equal space on both sides floats between sections.
- **The container owns the gaps.** Use a flex or grid `gap` on the form and on each section, not `margin-bottom` on every child. The last item then adds no stray space.
- **Use steps from one scale.** For example, 4, 8, 12, 16, 24, 32, 40 px.
- **Keep the labels tight.** Each label should be visibly closer to its own input than to the field above it.
- **Lay out the Address fields by content.** If you put short fields side by side, such as city, state and ZIP, keep the horizontal gap equal to the vertical field gap, so they still read as one group.
- **Space the toggles for touch.** Give the three Preferences toggles at least 44 px targets with about 8 px or more between them.

**When I'd change this**
- **Add a hairline rule** if the form grows to many sections or the headings are too subtle to scan. Use one weight and a quiet colour, with space on both sides of the rule.
- **Use a tinted region or card** only if a section needs to read as a separate object. An example is Preferences with its own Save button, or a form placed on a busy page background.

**Quick check:** blur your eyes at the rendered form. You should see exactly three clusters. If you see more, tighten the spacing inside the sections. If you see fewer, increase the space between sections.
