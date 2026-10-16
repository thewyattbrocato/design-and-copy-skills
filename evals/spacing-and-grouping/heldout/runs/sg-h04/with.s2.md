**Why it feels boxed in**

- **Every section gets the same treatment.** A border plus 16px padding on each section says "each of these is a separate object," so nothing reads as more related than anything else. Boxes are meant to mark discrete objects, such as something you can open, select, or drag. Page sections aren't objects.
- **Borders add visual noise.** Each box adds four edges, and the eye has to parse all of them. The padding then creates a gutter inside every box, so you get lots of small enclosed rooms.
- **Uniform padding hides the hierarchy.** If the space inside a group, between groups, and around the page are all about 16px, the layout can't show which things belong together.
- **Boxes inside boxes make it worse.** Nested borders and padding stack up quickly.

**Other ways to show items belong together**

Use the lightest device that works, in this order:

1. **Space (try this first).** Keep related items close and put more distance between groups. As a rule of thumb, the space inside a group should be about half the space between groups, or less. Pick values from a small scale, for example 4, 8, 16, 24, 40, 64.
   - Headings: put more space above than below, about 2:1, so each heading sits closer to its own content than to the section above.
   - Let the parent own the gaps (`display: grid; gap: …` or flex `gap`) instead of a `margin-bottom` on every child.
2. **Headings and alignment.** A clear heading with a shared left edge groups content without any lines.
3. **A hairline rule.** Use a single quiet 1px divider when space alone isn't enough, such as dense lists or tables. Leave space on both sides of it.
4. **A tinted region (no border).** Use a subtle background fill for a cluster that has to read as one unit, such as a toolbar, a filter panel, or a sticky footer.
5. **A card.** Keep this for real objects, such as items in a grid that users click, compare, or drag. Give them one consistent surface.

**If you keep some cards**

- Use only one or two of border, shadow, and fill on an element, not all three.
- Don't nest a card inside another card.
- Keep the gap between cards at least as large as the card padding. Otherwise they blur into one mass.

**Quick test:** squint at the page. You should see only the groups you meant, no more and no fewer. If you see a grid of rectangles, remove the borders and widen the gaps between sections first.

If you share the markup or CSS, I can show a concrete before and after.
