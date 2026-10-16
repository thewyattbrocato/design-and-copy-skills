**Why it feels boxed in**

1. **Every section gets the same treatment.** A border plus 16px padding on every block makes each one look equally important and equally separate. Nothing is grouped, because everything is a container.
2. **Borders add visual noise.** Each card contributes four edges, and the edges compete with the content. Borders dominate when there are many of them, so you see the grid of boxes before you see the content.
3. **Padding plus gaps adds up.** 16px inside, a border, and then the gap between cards makes the content look small and fenced off. If the gap between cards is smaller than the padding, the cards also blur into one mass.
4. **Cards say "this is a separate object."** That's right for things users open, select, drag, or compare. It's wrong for ordinary sections, where the boxes claim a separateness that isn't there.

**Other ways to show items belong together**

Use the lightest device that works, in this order:

1. **Space.** Make the gap inside a group about half the gap between groups, or less. For example, use 8px between a label and its field, 16px between fields in a group, and 32–48px between groups. Proximity alone does most of the work.
2. **Headings and alignment.** Put more space above a heading than below it (about 2:1), so the heading sits closer to its content than to the previous section. A shared left edge also reads as a group.
3. **A hairline rule.** Use one when space isn't enough, such as in dense lists, tables, or unlike items that must sit close. Use one weight and a quiet color, with space on both sides of it.
4. **A tinted region.** Use a subtle background fill, with no border, when a cluster of controls must read as one unit and can't be moved closer together. Toolbars, filter panels, and sticky footers are typical cases.
5. **A card.** Keep this for discrete objects, such as a product, a message, or a file. Give all of them one consistent surface.

**Practical fixes**

- Remove the borders from section wrappers and let headings and whitespace do the grouping.
- Use only one of border, shadow, or fill on a surface, never all three. Avoid cards inside cards.
- Let the parent own the spacing, using `gap` on the container instead of `margin-bottom` on every child. That avoids a doubled gap after the last item.
- Take spacing values from a small scale (for example 4, 8, 16, 24, 32, 48) instead of one-off numbers.
- Squint at the page. You should see the groups you intended, no more and no fewer.

If you share the markup or CSS, I can show a concrete before and after.
