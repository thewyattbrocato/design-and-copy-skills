It looks boxed in because the borders and the uniform 16px padding all say the same thing, and that thing is wrong.

**Why it happens**

- **Every section gets the same container.** A border says "this is a separate object." When every section has one, the page reads as a stack of equal-weight boxes. Nothing is a unit, a sibling, or a parent.
- **Uniform padding removes the spacing signal.** If the space inside each box and the space between boxes are both about 16px, spacing can't tell the eye what belongs together. The box edges end up doing all the grouping.
- **Borders add visual noise.** Each box adds four lines, and the content sits behind a frame. Nested cards make this worse, with border inside border and padding inside padding.
- **Small gaps between cards blur them into one mass.** If the gap between cards is smaller than the card padding, the cards run together.

**Other ways to show things belong together**

Use the lightest device that works, in this order:

1. **Space.** Make the gap within a group about half the gap between groups, or less. For example, use 8px between a label and its field, 24px between fields in a section, and 48px between sections. Put more space above a heading than below it, about 2:1, so the heading sits closer to its own content.
2. **Headings and alignment.** A clear heading with a shared left edge groups content without a frame.
3. **A hairline rule.** Use a thin, quiet-colored line when space alone isn't enough, such as in dense lists, table-like rows, or unlike items that must sit close. Leave space on both sides of the rule.
4. **A tinted region.** Use a subtle background fill when a cluster must read as one unit and can't be spread out, such as a toolbar, a filter panel, or a sticky footer.
5. **A card.** Keep this for discrete objects the user can open, select, drag, compare, or act on as a whole, like a product tile or an email in a list. Give those objects one consistent surface.

**Practical fixes**

- Remove the borders from section wrappers and let headings and whitespace do the work.
- Pick a small spacing scale, such as 4, 8, 12, 16, 24, 32, 48, and 64. Use only those values.
- Let the parent own the gaps with CSS `gap` instead of `margin-bottom` on every child. That avoids a doubled gap after the last item.
- Don't stack border, shadow, and background fill on one element. Use one, or two at most.
- If you keep cards, make the gap between them at least as large as their padding.

**Quick test:** Squint at the page. You should see the groups you meant, no more and no fewer. If you see a grid of identical rectangles, you have too many boxes and too little variation in spacing.

If you share the markup or CSS, I can show how to restructure it.
