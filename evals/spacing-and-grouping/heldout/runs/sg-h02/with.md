I'd drop the borders, make the space around group titles uneven, and give the items a bit more room.

**What's wrong now**
- A group title sits 4px from its items and 4px from the previous group's last item. Because those gaps are equal, the title floats and nothing reads as a group.
- A 1px border on every item and group makes the sidebar look boxed-in. It adds visual noise without adding any structure.
- 4px padding makes the items cramped, and it's the same value inside items as between groups.

**What I'd change** (4px scale)

| Thing | Now | Change to |
|---|---|---|
| Item padding | 4px | `8px 12px` (horizontal about 1.5× vertical, ~32–36px rows) |
| Gap between items in a group | 0 or borders | 2px, set by the parent |
| Group title to its first item | 4px | 8px |
| Previous group's last item to the next title | 4px | 24px (about 3× the title-to-items gap) |
| Item and group borders | 1px | none |

1. **Remove the item borders.** Show hover and selected states with a subtle background tint, plus an accent color or weight on the active item.
2. **Remove the group borders.** Spacing now does the grouping. If you still need a visual break, use one quiet hairline between groups, with 12px or more of space on each side. Don't box each group.
3. **Make the title relationships unequal.** A title should be much closer to its items than to the group above. Style the titles small, muted, and uppercase or semibold, so they act as labels and not as clickable items.
4. **Let the parent own the spacing.** Use a flex column with `gap` on the nav, and the same on each group. Don't put `margin-bottom` on every child, which doubles the gap after the last item.
5. **Use only scale values (4, 8, 12, 24).** That gives the same spacing for the same relationship everywhere.

```css
.sidebar-nav { display: flex; flex-direction: column; gap: 24px; }
.nav-group   { display: flex; flex-direction: column; gap: 2px; }
.nav-group-title { padding: 0 12px; margin-bottom: 6px; /* 2px gap + 6 = 8 */ }
.nav-item { padding: 8px 12px; border: 0; border-radius: 6px; }
.nav-item:hover { background: var(--surface-hover); }
.nav-item[aria-current="page"] { background: var(--surface-selected); font-weight: 600; }
```

This is an all-day expert tool, so compact is fine. If you want more rows on screen, drop the item padding to `6px 12px` and keep the 24px group gap. Shrink the small steps but keep the ratio between them, or the groups will merge again.

If you point me at the sidebar's CSS or component file, I can make these edits directly.
