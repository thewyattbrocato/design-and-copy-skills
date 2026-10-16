The cause is that a flex item's default `min-width` is `auto`, so `.info` can't shrink below its content width. With `white-space: nowrap`, that content is the full route name. The name pushes the row wider than the viewport, and the siblings get squeezed. On a laptop there's room, so you don't see it.

```css
/* Let the text column shrink, and stop the fixed-size items from shrinking */
.info{flex:1;min-width:0}
.thumb,.badge,.more{flex-shrink:0}
.badge{white-space:nowrap}

/* Narrow screens only: wrap the name (max 2 lines) instead of one long line */
@media (max-width:480px){
  .name{
    white-space:normal;
    overflow-wrap:anywhere;
    display:-webkit-box;
    -webkit-line-clamp:2;
    -webkit-box-orient:vertical;
    overflow:hidden;
  }
}
```

- **`.info{min-width:0}`** is the main fix. It lets the column shrink below its content width, so the row stays inside the viewport.
- **`flex-shrink:0` on the thumb, badge and button** keeps the badge from being squished. The thumbnail and button have fixed sizes, so they should keep them.
- **`white-space:nowrap` on `.badge`** keeps "12.4 km" on one line.
- **The media query** is the only part that changes the name's layout, and it applies only at 480px and below. Desktop keeps the single-line name. The clamp shows two lines and then ellipsizes. `overflow-wrap:anywhere` handles very long unbroken words, such as German compounds.

**Optional:** the badge and `.meta` both show "12.4 km". On small screens you could drop the duplicate with `@media (max-width:480px){ .meta{display:none} }`. That would also drop the duration, so you may prefer to leave `.meta` visible and hide only the badge.

If you want a single-line ellipsis on desktop too, add `overflow:hidden;text-overflow:ellipsis` to the base `.name` rule. That changes desktop behavior only for names that already overflow.
