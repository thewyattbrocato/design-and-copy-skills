Add this to your CSS and leave the existing rules as they are:

```css
header .inner,
main {
  width: min(70ch, 100% - 2.5rem); /* readable line length; keeps a 1.25rem gutter on narrow screens */
  margin-inline: auto;             /* centered on wide monitors */
}
```

- **Big monitor:** the header content and the body text now sit in a centered column about 70 characters wide, which is roughly 700px at your 17px Georgia. The header's green band still spans the full width.
- **Phone:** the column is the screen width minus 1.25rem on each side, so the text no longer touches the edges. At 320px that leaves about 280px of text width.
- **Look:** I didn't touch colors, fonts, vertical padding, `pre` or `img`. Code blocks and images now fill the column instead of the whole window, and `pre` still scrolls sideways when a line is too long.
- **Alignment:** the header content and the main text share the same column and left edge.

I haven't tested this in a browser. I also assumed the header's inner element is `.inner` and the body text is directly inside `main`, since I haven't seen your markup. If the structure differs, change the selectors to match.
