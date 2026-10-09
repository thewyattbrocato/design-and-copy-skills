Right now every gap is 4px, so nothing reads as grouped. The group title floats equally between two groups, and the borders box everything in. I'd make these changes.

**1. Make the space between groups larger than the space within them**
- The title should sit closer to its own items than to the previous group. Put 4px between a title and its items, and 24px between one group's last item and the next group's title. That's about a 6:1 ratio, so the groups show up without borders.
- Keep items inside a group tight: 0–2px between rows.

**2. Pad items by their content**
- Use `8px 12px` instead of 4px all round. That gives rows about 32–36px tall, which is still compact for a pointer-only admin tool.
- Align the title's left edge with the item text, using the same 12px inset, so everything shares one inner edge.

**3. Remove the borders**
- Drop the 1px border on every item and group. Space now separates the groups.
- Show state with fills instead: a subtle background on hover and a stronger tint on the active item.
- If you still want a divider, use one quiet 1px rule between major sections, with space on both sides of it. Don't use one per item.

**4. Let the container own the gaps**
- Use `gap` on the parent instead of `margin-bottom` on each child. That avoids doubled space after the last item in a group.

```css
.sidebar-nav   { display: flex; flex-direction: column; gap: 24px; padding: 12px; }
.nav-group     { display: flex; flex-direction: column; gap: 2px; }
.nav-group-title { padding: 0 12px 4px; /* small, muted */ }
.nav-item      { padding: 8px 12px; border: 0; border-radius: 6px; }
.nav-item:hover      { background: var(--surface-hover); }
.nav-item[aria-current="page"] { background: var(--surface-active); }
```

The values all come from a 4px scale (2, 4, 8, 12, 24). If your project already has spacing tokens, map these onto its nearest steps and keep the ratio of about 2:1 or more between group gaps and item gaps.

I haven't seen your actual sidebar code, since there's nothing in this directory. If you point me to the component or stylesheet, I can apply these changes directly.
