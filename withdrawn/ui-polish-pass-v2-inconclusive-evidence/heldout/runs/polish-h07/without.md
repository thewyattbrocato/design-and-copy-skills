Cause: `.name` has `white-space:nowrap`, and flex items default to `min-width:auto`. That makes `.info` refuse to shrink below the full text width. The row grows wider than the viewport, so the page scrolls sideways and the badge and button get squeezed.

**Changes**

```css
.info{flex:1;min-width:0}            /* allow the flex item to shrink below its content width */
.name{font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.badge{background:#eef;border-radius:12px;padding:2px 8px;flex-shrink:0;white-space:nowrap}
.more{width:28px;height:28px;flex-shrink:0}
.thumb{flex-shrink:0}
```

What each one does:

- **`.info{min-width:0}`** is the actual fix. Without it, nothing else can take effect.
- **`overflow:hidden; text-overflow:ellipsis`** on `.name` keeps the single-line look and truncates with "…". On desktop, where the name fits, nothing changes.
- **`flex-shrink:0`** on `.thumb`, `.badge` and `.more` stops them from being squished. The badge also gets `white-space:nowrap` so "12.4 km" can't wrap onto two lines.

**Optional improvements for small screens**

- The distance appears twice, in `.meta` and in `.badge`. On narrow screens you could hide one of them:
  ```css
  @media (max-width:400px){ .meta{display:none} }
  ```
  Or keep `.meta` and hide `.badge`. This is a design choice, so I left it out of the main fix.
- If you'd rather show the whole name than truncate it, replace the `.name` rules with `white-space:normal; overflow-wrap:anywhere;`. Long names then wrap onto several lines. Desktop would also wrap if a name is wider than the available space, so scope it in a media query if you want desktop unchanged.

I haven't run this in a browser. The behavior follows from standard flexbox rules, but check it at about 320px width.
