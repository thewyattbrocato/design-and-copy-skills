The cause is that `.info` is a flex item with `flex:1`, and flex items default to `min-width:auto`. With `white-space:nowrap`, the item can't shrink below the full width of the name. It pushes the row wider than the viewport, and the siblings get squeezed. Laptops have enough room that you never notice.

**Change these rules:**

```css
.info{flex:1;min-width:0}                 /* allow it to shrink below its content width */
.name{font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.badge{background:#eef;border-radius:12px;padding:2px 8px;flex-shrink:0;white-space:nowrap}
.more{width:28px;height:28px;flex-shrink:0}
.thumb{flex-shrink:0}
```

- `min-width:0` on `.info` is the real fix. The ellipsis rules only work once `.info` can actually shrink.
- `flex-shrink:0` on `.badge`, `.more` and `.thumb` stops them from being squished. The name then takes all the shrinking.
- `white-space:nowrap` on the badge keeps "12.4 km" on one line.

On desktop, where the name fits, nothing changes visually.

**Optional: wrap on phones instead of truncating.** A name like yours loses the "via Schlossbergtunnel (scenic)" part to an ellipsis. To show two lines on small screens only:

```css
@media (max-width:480px){
  .name{
    white-space:normal;
    overflow-wrap:anywhere;
    display:-webkit-box;
    -webkit-line-clamp:2;
    -webkit-box-orient:vertical;
  }
}
```

Also, `.meta` and `.badge` both show "12.4 km". If space is tight, you could hide the badge on narrow screens, or drop the distance from `.meta`.

I haven't run any of this, since I only have the snippet. Check it in DevTools at 320px width.
