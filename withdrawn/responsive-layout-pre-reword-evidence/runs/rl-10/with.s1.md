Two changes fix both problems. Main text and the header content now share one centered column, capped in width, with a minimum side gutter.

```css
header .inner,
main {
  inline-size: min(72ch, 100% - 2rem); /* readable line length; 1rem gutter each side on narrow screens */
  margin-inline: auto;
}
```

Leave the rest of your CSS as it is. The header's green background still spans the full width, because only `.inner` is constrained. The title lines up with the body text.

- **Big monitor:** lines stop at about 72 characters and the column centers. Before, they ran the full width.
- **Phone (320px):** the column is the screen width minus 1rem on each side, so text no longer touches the edges. The 1rem gutter is the same on both sides, so it also works right-to-left.
- **Unchanged:** colors, fonts, vertical padding, `pre` and images. Images are `width: 100%`, so they now fill the column rather than the whole screen. `pre` keeps its own scrolling for long code lines.

Assumptions:
- Your header content sits in `header .inner` and the body text in `main`.
- Laptop screens will look a little narrower if they were wider than about 72 characters. If you want a wider column, raise `72ch` (for example to `80ch`).

I haven't previewed this in a browser, and I couldn't edit a file because I only had the CSS you pasted.
