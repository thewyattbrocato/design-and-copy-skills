The cause is that flex items default to `min-width: auto`. `.info` can't shrink below the width of its `nowrap` name, so the row grows wider than the viewport. The row is then too wide, so the other items (badge, button, thumb) get shrunk to make room, and that's what squishes the badge.

**Changes**

```css
.route{display:flex;align-items:center;gap:12px;padding:12px;border-bottom:1px solid #e3e3e3}
.info{flex:1;min-width:0}                 /* allow it to shrink below its content width */
.name{font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.thumb,.more{flex-shrink:0}               /* fixed-size items keep their size */
.badge{background:#eef;border-radius:12px;padding:2px 8px;flex-shrink:0;white-space:nowrap}
.more{width:28px;height:28px}
```

On desktop the name fits, so the ellipsis never triggers and the layout is unchanged.

**Optional: wrap instead of truncating on phones**

A long route name like yours loses the "via Schlossbergtunnel (scenic)" part when truncated. If you'd rather show the whole name on small screens, add:

```css
@media (max-width:480px){
  .name{white-space:normal;overflow-wrap:anywhere;
        display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical}
}
```

That gives up to two lines, then an ellipsis. `overflow-wrap:anywhere` also protects against long unbroken German compounds.

**Side note:** `.meta` shows "12.4 km" and so does the badge, so the distance appears twice. On narrow screens you could drop one, for example `.badge{display:none}` inside the media query, which also frees up width for the name. That is a design choice, so I haven't included it above.

I haven't tested this in a browser. Check it with devtools at about 320px width.
