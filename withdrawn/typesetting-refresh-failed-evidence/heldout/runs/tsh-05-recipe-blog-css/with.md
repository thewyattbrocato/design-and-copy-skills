The type feels cramped and cheap because several settings fight the text, mostly in the body rule.

## What's wrong

1. **Line length.** `.post` is 1100px wide with 14px text, so lines run about 150 characters. The eye loses its place on the return sweep, and that makes the page feel dense. This is the biggest problem.
2. **Leading.** A `line-height` of 1.15 is for headings, not body text. Combined with the long lines, it gives the cramped look. Body text wants about 1.5.
3. **Body size.** 14px fixed is small for a reading page. Use 1.125rem, which also respects the reader's browser settings.
4. **Tracked lowercase.** `letter-spacing: 0.04em` on body text loosens the word shapes, which reads as amateur. Remove it.
5. **Justified text with no hyphenation.** This leaves uneven gaps and rivers of white space. Go flush-left and ragged.
6. **h1.** A `line-height` of 1.5 makes a wrapped title fall apart, and `+0.06em` tracking on 56px type looks loose. Large display type wants a tight line height (about 1.15) and slightly negative tracking.
7. **h2.tag.** Caps at 11px with `letter-spacing: 0` is the wrong way round. Small caps need tracking (0.05–0.1em) and at least 12px.
8. **Links.** `color: inherit` with no underline means links are invisible until hover, and touch screens have no hover. Keep an underline.
9. **`.price` and `.qty`.** Georgia's default numerals are old-style, so "1½ cups" and "$12" bob up and down. They won't line up in columns, and Georgia has no tabular-figure feature to switch on. Those two classes need a different font that has lining, tabular figures.
10. **blockquote.** Italic, bold and uppercase together is three emphasis devices on one element. Georgia has no bold italic caps worth using, so the browser fakes some of it, and all-caps sentences read slowly. Pick one device, italic.

## Fixed CSS

```css
body {
  font-family: Georgia, serif;
  font-size: 1.125rem;
  line-height: 1.55;
  color: #333;
  text-wrap: pretty;
}
.post { max-width: 65ch; margin: 0 auto; padding: 0 1rem; }

h1 {
  font-size: 3rem;
  line-height: 1.15;
  letter-spacing: -0.015em;
  font-weight: 700;
  text-wrap: balance;
  margin: 0 0 0.75rem;
}
h2.tag {
  font-size: 0.8125rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-weight: 600;
}

a { color: inherit; text-decoration: underline; text-underline-offset: 0.15em; }
a:hover { color: #c0392b; }

.price, .qty {
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  font-variant-numeric: tabular-nums lining-nums;
}

blockquote { font-style: italic; margin: 1.5rem 0 1.5rem 1.25rem; }
```

## Notes

- I removed `text-align: justify`. If you want justified text later, add `hyphens: auto` and `lang="en"` on `<html>`, but ragged is safer on screens.
- `max-width: 65ch` goes on `.post` since it holds the prose. If it also holds wide elements like photos, put the cap on `.post p` instead.
- The sans font on `.price` and `.qty` is an assumption. Any face with lining tabular figures works, such as your site's UI font. If you'd rather keep a serif, you'd need to swap in a webfont that has them.
- I assumed a light background and screen-only reading. Paragraph spacing and heading margins weren't in your CSS, so add about twice as much space above each `h2` as below it.
