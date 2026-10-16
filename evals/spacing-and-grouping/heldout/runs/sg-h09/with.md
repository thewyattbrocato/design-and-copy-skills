**Use extra space and headings only.** Add a hairline rule only if testing shows the sections still blur together.

**Why**
- Twelve fields in three sections is a small form with one level of grouping. A heading plus clear spacing is enough to show where each section starts and ends.
- Cards are for discrete objects, meaning things you open, select, drag, or act on as a whole. These sections are just parts of one form. Boxing each one adds borders and padding that compete with the inputs, and the form looks heavier and more fragmented than it is.
- Rules work when space can't do the job, such as dense lists or unlike items that have to sit close together. Here you have plenty of room, so space does the job without extra lines.

**How to make it work**
- **Gaps:** Keep the gap within a section about half the gap between sections. For example, use 16 px between fields and 40 px between sections, with both values taken from your spacing scale.
- **Headings:** Put more space above each heading than below it, roughly 2:1. A heading should sit visibly closer to its own fields than to the section above.
- **Parent-owned spacing:** Set the gaps with `gap` on the container, not `margin-bottom` on every child. That avoids a doubled gap after the last item.
- **Preferences section:** Three toggles can sit tighter than text inputs, since they're a simple list. Give each row at least a 44 px tap target on touch devices.
- **Address fields:** If some of the five fields naturally pair up (city and state, or state and postal code), put them side by side. That shows the grouping inside the section without any extra devices.

**When to change this**
- If the form sits on a busy background or inside a page with other content, a single tinted or bordered surface around the whole form can help. Put it around the form, not around each section.
- If the sections get long, or users need to scan back and forth between them, add a quiet hairline between sections. Keep the same spacing on both sides of it.

**Quick check:** Blur or squint at the page. You should see three clear clusters. If you do, you don't need anything more than space and headings.
