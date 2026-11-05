Here's what I'd change. It's a recommendation only, since I haven't seen your code. The main problem is that everything has the same tight spacing and the same border, so nothing reads as a group.

**1. Fix the group spacing first (biggest win)**
- Right now a group title sits 4px above its items and 4px below the previous group's last item. That's equal space on both sides, so the title floats between the groups and the groups blur together.
- Make the space between groups about twice the space inside them. A title should be visibly closer to its own items than to the previous group.
- Suggested values: **16px above the title, 4–6px below it**. Items stay close together inside a group.
- Put this spacing on the container (a `gap`, or a margin-top on each group after the first). That way the last group doesn't add extra trailing space.

**2. Remove the 1px borders on items and groups**
- Borders on every item and group turn the sidebar into a stack of boxes, and they add visual noise.
- Items: no border. Use a hover background and a tinted background for the active item.
- Groups: no border. The spacing from step 1 now does the separating.
- If you still want a divider, use one quiet hairline between major sections, with space on both sides. Don't put one on every item.

**3. Give items more padding, and more on the sides**
- 4px all round is too tight. Use about **8px vertical and 12px horizontal**. That gives a row height of roughly 32–36px, which is comfortable for a pointer-driven tool without wasting space.
- Keep items in a group touching or with a 2px gap. They're one unit, so the hover and active backgrounds provide the separation.

**4. Use a small scale**
- Stick to 4, 8, 12, 16, 24. Use 4 for title-to-items, 8/12 for item padding, and 16 for between groups.
- Make the group title smaller, uppercase or muted, so it reads as a label and not another menu item.

**Sketch**
```css
.sidebar-nav { display: flex; flex-direction: column; gap: 16px; padding: 12px; }
.nav-group { display: flex; flex-direction: column; gap: 2px; }
.nav-group-title { padding: 0 12px 4px; font-size: 12px; text-transform: uppercase; color: var(--muted); }
.nav-item { padding: 8px 12px; border: 0; border-radius: 6px; }
.nav-item:hover { background: var(--hover); }
.nav-item[aria-current="page"] { background: var(--active); }
```

If you point me at the sidebar's stylesheet or component, I can make these edits directly.
