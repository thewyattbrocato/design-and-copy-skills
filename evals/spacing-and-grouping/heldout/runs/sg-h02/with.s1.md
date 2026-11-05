I'd change four things. I haven't looked at your code, so the values below are a starting point.

**1. Remove the borders on items and groups.**
- A 1px box around every item turns the sidebar into a stack of small boxes. That adds visual noise and no information.
- Use a tinted background for hover and for the active item. Items are rows in a list, so they don't need to be boxes.
- Space and the group titles already separate the groups. If you want a rule, use one hairline at a real boundary, such as above a pinned footer or account block.

**2. Give items more padding.**
- Change 4px to about 8px vertical and 12px horizontal. That gives rows roughly 32–36px tall.
- A daily-use admin tool can stay compact, but 4px padding is too tight to read comfortably or to click accurately.
- Let the list container own the spacing between items, with a 2px `gap` or none. Don't put margins on each item.

**3. Make the group title spacing asymmetric.**
- A title with 4px above and 4px below floats between two groups, so it doesn't clearly belong to either.
- Give it about 24px above, which separates it from the previous group. Give it about 4–8px below, which ties it to its own items.
- That makes the space between groups roughly 3–4 times the space inside a group.
- The first group needs no top space. Put the group gap on the container, not as a bottom margin on each group, so the last group doesn't leave an extra gap.

**4. Make the titles read as labels.**
- Use a smaller, muted, possibly uppercase style.
- Align their left edge with the item text, not with the item's outer edge, so everything lines up on one inner edge.

**Scale:** use only 4, 8, 12 and 24px for everything here. The result is tighter within groups and looser between them, so the sidebar should look less cramped without taking more vertical room overall. Dropping the borders also saves 2px per item.

If you share the sidebar's CSS or component, I can make these changes directly.
