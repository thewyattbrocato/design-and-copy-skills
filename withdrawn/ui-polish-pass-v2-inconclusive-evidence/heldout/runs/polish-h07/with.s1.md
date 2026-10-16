The cause is that `.info` is a flex item with the default `min-width: auto`. Because `.name` is `nowrap`, `.info` can't shrink below the full width of the title. It pushes the row wider than the viewport, and the other items get squeezed.

**Changes**

```css
.info{flex:1;min-width:0}                 /* allow the text column to shrink */
.name{font-weight:600;white-space:nowrap;
      overflow:hidden;text-overflow:ellipsis}  /* truncate instead of overflow */

.thumb,.badge,.more{flex-shrink:0}        /* stop the fixed-size items being squished */
.badge{white-space:nowrap}                /* keep "12.4 km" on one line */
```

**Optional: show the full name on small phones**

If you'd rather wrap than truncate:

```css
@media (max-width:480px){
  .name{white-space:normal;overflow-wrap:anywhere;
        display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical}
}
```

**Why desktop looks the same**
- `min-width:0` only matters when the row is too narrow.
- Ellipsis only appears when the text overflows.
- `flex-shrink:0` matches what you already see on desktop, where nothing needs to shrink.

**Other things to check**
- If the page still scrolls sideways, an ancestor (the `ul` or a wrapper) may be a flex or grid item with the same `min-width:auto` problem. Add `min-width:0` there too.
- On narrow screens the badge repeats the distance already in `.meta`. You could hide the distance in `.meta` under 480px to save space, but that's a design choice, so I left it out.
- With truncation, add `title` to `.name` or use the wrapping variant, so people can still read the full route name.

I haven't run this, because there's no project in the working directory. It's based on the markup and CSS you pasted.
