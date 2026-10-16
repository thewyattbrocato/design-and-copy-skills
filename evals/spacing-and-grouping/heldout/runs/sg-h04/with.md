**Why it looks boxed in**

1. **Every section gets the same treatment.** A border plus 16px padding on every section gives each one equal weight, so nothing reads as more or less related to anything else. Groups only show up when the space inside a group is clearly smaller than the space between groups. Identical boxes erase that difference.
2. **Borders compete with the content.** Every section gets a closed outline, so your eye reads a grid of containers before it reads the content. A border says "this is a discrete object". Applied to everything, it just adds noise.
3. **The gaps between cards are probably too small.** If the gap between cards is about the same as or smaller than the 16px padding, the cards blur into one mass of lines.
4. **Cards often nest.** A bordered section holding bordered sub-items, or a border plus a shadow plus a fill on one element, compounds the heavy feel.

**Lighter ways to show items belong together**

Try these in order and stop at the first one that works:

1. **Space.** Keep items in a group close, about half the gap you use between groups. For example, use 8px within a group, 24px between groups, and 40–48px between major sections. Put more space above a heading than below it, about 2:1, so the heading sits with its content.
2. **Headings and alignment.** A clear heading and a shared left edge group things well on their own.
3. **A hairline rule.** Use it when space alone isn't enough, such as dense lists or tables. Use one quiet color and one weight, with space on both sides of the line.
4. **A tinted region, with no border.** Use it when a cluster of controls must read as one unit and can't be moved closer together, such as a toolbar, a filter panel, or a sticky footer.
5. **A card.** Keep it for discrete objects the user can open, select, drag, or compare as a whole. Give every such object the same single surface, using a border or a fill or a shadow, not all three.

**Practical fixes**

- Remove the borders from most sections and let headings and space do the work.
- Keep cards only for real objects, like items in a list or grid.
- Build spacing from a small scale, for example 4, 8, 12, 16, 24, 32, 48. Don't use one-off values.
- Let the parent container own the gaps (`display: grid; gap: …`) instead of putting a bottom margin on every child.

To check the result, squint at the page. You should see the groups you intended, no more and no fewer. If you share the markup or CSS, I can suggest specific changes.
