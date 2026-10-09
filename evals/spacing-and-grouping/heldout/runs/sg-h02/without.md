Here's what I'd change. These are starting values to tune against your actual type scale, since I haven't looked at your code.

**Item padding: 4px → 8px vertical, 12px horizontal**
- 4px is tight for a click target. 8px/12px, with a ~14px font and a line-height of about 20px, gives roughly 36px rows. That's a comfortable target and still dense enough for an admin tool.

**Group spacing: separate groups by space, not by tight packing**
- Add about 24px above each group title, and none above the first group.
- Put about 8px between a title and its first item. That's tighter than the gap between groups, so the title reads as belonging to its items. Right now the 4px/4px split is symmetric, so titles float ambiguously between groups.
- Rule of thumb: the space around a group should be clearly larger than the space within it (24px vs 8px, or at least 2–3×).

**Group titles: make them look like labels**
- Use a smaller size (11–12px), uppercase or semibold, with letter-spacing of about 0.04em and a muted color. Then they stand out from items by style rather than needing extra boxes.

**Borders: remove most of them**
- Drop the 1px border on every item and group. Borders add visual noise and effectively eat 2px of padding on each side.
- For items, use no border at rest. Use a subtle background on hover, and a stronger background plus an accent (e.g. a 2–3px left bar) for the active item.
- For groups, the whitespace should do the separating. If you still want a divider, use one 1px line between groups (or none), not around every group and item.
- Add a 2px focus ring so keyboard focus stays visible.

**Small extras**
- Add 2px of gap between items, and give them a 6px border-radius so hover and active states look cleaner.
- Use 12–16px of padding on the sidebar container itself.

In CSS terms:

```css
.sidebar { padding: 12px; }
.nav-group + .nav-group { margin-top: 24px; }
.nav-group-title {
  margin-bottom: 8px;
  font-size: 11px; font-weight: 600;
  text-transform: uppercase; letter-spacing: .04em;
  color: var(--text-muted);
}
.nav-item {
  padding: 8px 12px; border: 0; border-radius: 6px;
  display: block;
}
.nav-item + .nav-item { margin-top: 2px; }
.nav-item:hover { background: var(--surface-hover); }
.nav-item[aria-current="page"] { background: var(--surface-active); font-weight: 600; }
```

If you point me at the sidebar's component or stylesheet, I can make these changes directly.
