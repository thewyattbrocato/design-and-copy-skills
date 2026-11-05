**Why it looks boxed in**

Three things combine:

1. **Every section gets the same treatment.** A border plus 16px padding on every block says "each of these is a separate object" and gives them all equal weight. Real relationships have levels: a label belongs to its field, a field to its section, a section to the page. A uniform box flattens those levels, so nothing reads as more closely related than anything else.
2. **Borders add visual noise.** Each one is a hard line your eye has to cross. With many sections you get a grid of lines competing with the content.
3. **The padding is probably smaller than the gaps it needs to beat.** If the gap between cards is 16px or less and the padding inside is 16px, the cards blur into one mass. The border then has to do all the separating that space should be doing. Padding inside a card also eats width, so the content feels squeezed.

**Other ways to show things belong together**

Use the lightest device that works, in this order:

1. **Space.** Make the gap inside a group about half the gap between groups, or less. For example, use 8px between a label and its field, 16px between fields in the same section, and 32–48px between sections. Put more space above a section heading than below it, roughly 2:1, so the heading attaches to its own content.
2. **Headings and alignment.** A heading plus a shared left edge groups content without any container.
3. **A hairline rule.** Use this when space alone isn't enough, such as in dense lists or tables. Use one weight and a quiet color, with space on both sides.
4. **A tinted region.** Use a subtle background fill, with no border, for a cluster of controls that must read as one unit, like a toolbar, filter panel, or sticky footer.
5. **A card.** Keep these for discrete objects the user can open, select, drag, compare, or act on as a whole, such as a product tile or a message. If you do use cards, give them all one consistent surface. Don't stack border, shadow, and fill together, and don't nest cards inside cards.

**Practical fixes**

- Remove the borders from section wrappers and let a heading and extra vertical space define each section.
- Pick a small spacing scale (for example 4, 8, 16, 24, 32, 48) and use only those values.
- Let the parent container own the spacing with `gap` instead of `margin-bottom` on every child. That avoids a doubled gap after the last item.
- Where you keep cards, make the gap between them at least as large as the card padding.

If you share the markup or CSS, I can show you the specific changes.
