The root cause is `white-space:nowrap` on `.name`, combined with a flex item that can't shrink. A flex child has `min-width:auto`, so `.info` refuses to get narrower than its longest unbreakable content. The long name therefore forces the row wider than the viewport, and the badge and button get squeezed.

**Changes**

```css
.info{flex:1;min-width:0}

.name{
  font-weight:600;
  white-space:nowrap;
  overflow:hidden;
  text-overflow:ellipsis;
}

.badge{flex:none;white-space:nowrap;background:#eef;border-radius:12px;padding:2px 8px}
.more{flex:none;width:28px;height:28px}
.thumb{flex:none}
```

**What each one does**

- `.info{min-width:0}` is the key fix. It lets the text column shrink below its content width, so the row stays within the viewport.
- `overflow:hidden` and `text-overflow:ellipsis` on `.name` keep it on one line, as on desktop, and truncate it with "…" when space runs out. These only take effect once `.info` can shrink.
- `flex:none` on `.badge`, `.more` and `.thumb` stops them from being compressed. `white-space:nowrap` on the badge keeps "12.4 km" on one line.

On desktop, where the name fits, nothing changes. The ellipsis only appears when the text doesn't fit.

**Optional: wrap on small screens**

If you'd rather show the full name on phones than truncate it:

```css
@media (max-width:480px){
  .name{white-space:normal;overflow-wrap:anywhere}
}
```

Alternatively, use `-webkit-line-clamp:2` to allow two lines before truncating.

**Other notes**

- The badge duplicates the distance already in `.meta` ("12.4 km · 38 min"). On very small screens you could hide one of them, for example `@media (max-width:360px){.badge{display:none}}`.
- If the page still scrolls sideways after this, the `<ul>` or a parent may have a fixed width. Check for that, and make sure `<meta name="viewport" content="width=device-width, initial-scale=1">` is present.

I haven't run this in a browser. The fix follows standard flexbox behavior, so it's worth checking at about 320px width in devtools.
