Your sidebar has one spacing value and one grouping device applied to everything. The fix is to give groups their own spacing and to drop most of the borders.

**What's wrong**
- Every gap is 4px, so the item-to-item, title-to-items, and group-to-group distances are all the same. Nothing reads as a group.
- Each group title sits 4px below the previous group's last item and 4px above its own items. A title should be closer to its own items than to the group above it, and here they're equal.
- Every item and group has a 1px border, so the sidebar is a stack of boxes and the lines compete with the labels.
- 4px of padding is tight even for a dense tool, and it makes the click targets small.

**What I'd change**

1. **Item padding:** 8px vertical and 12px horizontal. That keeps the sidebar compact for daily use and gives rows of about 32–36px with a comfortable hit area.
2. **Spacing inside a group:** 4px between a title and its items, and 2px between items (or 0, with padding doing the work). Within-group space should stay small.
3. **Spacing between groups:** 24px above each group title. That's roughly a 6:1 ratio to the 4px below it, so each title clearly belongs to the items under it. Anything at about 2:1 or more would work.
4. **Borders:** remove them from items and groups. Use space to separate groups. For the active or hovered item, use a subtle background tint instead of an outline.
5. **Optional divider:** if you still want something between groups, use one 1px hairline in a quiet color with space on both sides of it. Don't box each group.
6. **Group titles:** use smaller, muted, uppercase or semibold text so they read as labels. I'd do this through type styling rather than extra borders or padding.
7. **Implementation:** let the container own the spacing. Use `gap` on the nav list and a group-level margin or gap, rather than `margin-bottom` on every child. That avoids doubled space after the last item.

**Sketch**
```css
.sidebar-nav { display: flex; flex-direction: column; gap: 24px; }   /* between groups */
.nav-group   { display: flex; flex-direction: column; gap: 2px; }    /* within group */
.nav-group-title { padding: 0 12px 4px; font-size: 12px; color: var(--muted); }
.nav-item { padding: 8px 12px; border: 0; border-radius: 6px; }
.nav-item:hover, .nav-item[aria-current="page"] { background: var(--surface-hover); }
```

I haven't seen your code, so these values are a starting point. If you already have spacing tokens, I'd snap them to those (for example 4, 8, 12, 24). If you point me at the sidebar's stylesheet or component, I can make the change directly.
