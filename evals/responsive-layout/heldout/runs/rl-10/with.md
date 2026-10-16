I've capped the line length and added side gutters. Everything else is unchanged.

```css
body { margin: 0; font: 17px/1.55 Georgia, serif; color: #222; background: #fbfaf7; }
header { background: #1d3b2a; color: #fff; padding: 20px 0; }
header .inner { padding: 0; }
main { padding: 40px 0; }
main p, main li { margin: 0 0 1em; }
pre { background: #efece4; padding: 16px; overflow: auto; }
img { width: 100%; }

/* Reading width: at most 70ch, with a 1rem gutter on narrow screens.
   The header shares it so the two stay aligned. */
header .inner,
main {
  inline-size: min(100% - 2rem, 70ch);
  margin-inline: auto;
}
```

- **Big monitors:** `header .inner` and `main` stop growing at 70ch, about 70 characters per line, and center themselves.
- **Phones:** `100% - 2rem` leaves a 1rem gutter on each side, so text no longer touches the edges. At 320px the column is 288px wide, and it can't overflow sideways.
- **Unchanged:** colors, fonts, vertical padding, and the `pre` and `img` rules. On a laptop the column will now be narrower than before if your window is wider than about 70ch.

I assumed `header .inner` is a block wrapper inside the header, and that `main` holds the doc text directly. I couldn't see your HTML. If `main` has a different inner structure, the same two lines apply to whichever wrapper holds the content. Code blocks and images are capped at the same width, and `pre` still scrolls sideways inside its box.
