Here's what I'd change, based on the relationships in your sidebar. I haven't looked at your code, so the values are proposals on a 4px-based scale.

**The main problem is that the spacing doesn't show grouping.**
Group titles sit 4px above their items and 4px below the previous group's last item. Equal space on both sides means a title floats between groups, and Orders, Inventory and Reports blur into one list. Borders on every item and group then add visual noise without fixing that.

**Changes**

1. **Group spacing: more above the title, less below.**
   - Put about 20–24px between the previous group's last item and the next title.
   - Put about 4–8px between a title and its first item.
   - This is roughly 2:1 or more, so each title reads as belonging to the items under it.
   - Within a group, keep items tight (0–2px gap). Space between groups should be at least twice the space between items.

2. **Remove the borders on items and groups.**
   - Space now does the grouping, so the borders are redundant.
   - Show state with a tinted background on hover and on the active item, not an outline.
   - If you want a visible separator, use one hairline in a quiet color between groups only, with space on both sides. Don't put a border on each item.

3. **Raise item padding from 4px to about 8px vertical and 12px horizontal.**
   - Horizontal padding should be about 1.5–2× vertical.
   - That gives rows roughly 32–36px tall. This suits a dashboard used with a mouse, and it stays compact for expert use.
   - If the sidebar needs to work on touch, aim for 44px rows.
   - Keep the text on one inner left edge. Align group titles with the item text or the item icons, and use the same edge for both.

4. **Differentiate the titles without extra boxes.**
   - Make them smaller, uppercase or muted, with no border.
   - They are labels for a group, so they shouldn't compete with the items.

5. **Let the container own the gaps.**
   - Use `gap` on the sidebar and each group, or a margin on the group that follows. Don't put `margin-bottom` on every child.
   - That avoids doubled space after the last item and keeps the rhythm consistent.

**Sketch**

```css
.sidebar        { display: flex; flex-direction: column; gap: 24px; padding: 16px 12px; }
.group          { display: flex; flex-direction: column; gap: 2px; }
.group-title    { padding: 0 12px 6px; font-size: 12px; text-transform: uppercase; color: var(--muted); }
.item           { padding: 8px 12px; border-radius: 6px; border: 0; }
.item:hover     { background: var(--hover); }
.item[aria-current="page"] { background: var(--active); }
```

The values to check against your own scale are 24 (between groups), 6 (title to items), 2 (between items), and 8/12 (item padding). If you already have spacing tokens, snap these to the nearest ones and keep the ratios.

If you point me at the sidebar's stylesheet or component, I can make the changes directly.
