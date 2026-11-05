**Why it feels boxed in**

1. **Every section gets the same container.** When all sections are bordered cards, the border says "this is a separate object" for each one. Nothing is more or less related to anything else, so the page reads as a stack of unrelated crates. The boxes carry the grouping, and they carry it identically everywhere.
2. **Borders add visual noise.** Each card has four edges, and the eye has to trace every one of them. With many cards, the edges compete with your content.
3. **Uniform 16px padding makes the inside and the outside look alike.** The gap inside a card is about the same as the gap between cards. The groups blur together, and the page looks squashed and uniform instead of organized. If the gap between cards is smaller than the padding, the cards also merge into one mass.
4. **Nesting makes it worse.** A card inside a card (or a bordered table or input inside a card) creates a box within a box. That is the strongest "boxed in" signal.

**Other ways to show that items belong together**

Use the lightest device that works, and move down this list only when the one above fails:

1. **Space (try this first).** Make the space within a group about half the space between groups, or less. For example, use 8px between a label and its field, 16px between fields in a group, and 32–48px between sections. Proximity alone does most of the grouping.
2. **Headings and alignment.** A heading placed closer to its content than to the section above it (roughly 2:1 above to below) anchors the group. A shared left edge ties items together without a line.
3. **A hairline rule.** Use a thin, quiet divider when rows are dense, as in lists and tables, or when unlike things have to sit close together. Leave space on both sides of the rule, and use one weight and color everywhere.
4. **A tinted region.** Use a subtle background fill when a cluster of controls must read as one unit and can't be moved apart, such as a toolbar, a filter panel, or a sticky footer. Skip the border, because the fill is enough.
5. **A card, only for discrete objects.** Keep cards for things the user can open, select, drag, compare, or act on as a whole, like a product, a project, or a message. If you do use cards, give them one consistent surface. Use a border or a shadow or a fill, not all three, and don't nest them.

**A practical way to fix your page**

- Remove the borders from the section containers and let headings and whitespace separate the sections.
- Set the spacing from a small scale (for example 4, 8, 16, 24, 32, 48) so every gap is a deliberate step.
- Let the parent container own the gaps (`gap` in flex or grid) instead of putting a bottom margin on every child.
- Keep the cards only for the items that are real objects, such as a list of projects.
- Squint at the page. You should see only the groups you meant, no more and no fewer.

If you share the markup or CSS, I can show you specific changes.
