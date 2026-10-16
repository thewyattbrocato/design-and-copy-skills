Here's what I'd change. I haven't looked at your code, so the values are starting points.

**1. Item padding: 4px → 8px vertical, 12px horizontal**
- 4px is too tight for a click target. `8px 12px` gets rows to about 32–36px tall with a 14px font, and that's the usual density for admin UIs.
- If you want it denser, keep 8px vertical and trim the horizontal padding.

**2. Group spacing: separate groups more than items**
- Put 20–24px above each group title, and keep 6–8px between the title and its first item. Space above the title should be at least 2–3× the space below it, so the title reads as belonging to the items under it.
- Today the 4px above and 4px below make the title look equally attached to the previous group and its own. Proximity is what's failing, and the borders are only hiding that.
- Use `margin-top` on the group, not `margin-bottom` on the last item. Then the first group doesn't get a stray gap at the top.

**3. Remove the 1px borders on items and groups**
- A border on every row adds visual noise and makes the sidebar look like a table. Spacing already separates the items.
- For items, use no border and a subtle background on hover. For the active item, use a filled background, plus an optional 2–3px accent bar on the left edge.
- For groups, drop the border and make the title look different from the items: 11–12px, uppercase, `letter-spacing: 0.04em`, muted color, medium weight.
- If you still want a divider, use one hairline between major sections, not between every group.

**4. Small extras**
- Use 2px of gap between items for a slight rhythm, with a `border-radius` of 6px on the hover and active backgrounds.
- Keep a visible `:focus-visible` outline, since removing the borders can remove your only focus affordance.

**Sketch**
```css
.nav-group { margin-top: 24px; }
.nav-group:first-child { margin-top: 0; }
.nav-group-title {
  margin-bottom: 8px;
  padding: 0 12px;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--text-muted);
}
.nav-item {
  padding: 8px 12px;
  border: 0;
  border-radius: 6px;
}
.nav-item + .nav-item { margin-top: 2px; }
.nav-item:hover { background: var(--bg-hover); }
.nav-item[aria-current="page"] { background: var(--bg-active); }
```

If you point me at the sidebar's stylesheet or component, I can make these changes against your actual tokens and class names.
