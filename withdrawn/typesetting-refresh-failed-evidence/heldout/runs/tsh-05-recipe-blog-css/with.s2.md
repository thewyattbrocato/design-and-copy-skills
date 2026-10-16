Your instinct is right, and the cause is several settings working against each other. Here's what's wrong, in order of impact.

**What's wrong**

1. **Body is 14px with 1.15 line height.** This is the main cause of the cramped feel. Lines sit almost touching, and Georgia has a large x-height, so it needs more room than most faces. Reading text should be about 1rem to 1.125rem with leading near 1.5.
2. **`letter-spacing: 0.04em` on body.** Tracking lowercase text makes it look loose and cheap. Remove it and trust Georgia's own spacing.
3. **`text-align: justify` with no hyphenation.** Without `hyphens: auto`, justification opens uneven rivers of white space between words. Use ragged-right on screen.
4. **`.post` is 1100px wide.** At that width, lines run well past 100 characters, which is hard to follow. Cap the text at about 65ch. A fixed 1100px also breaks on phones.
5. **h1 is 56px with `line-height: 1.5` and 0.06em tracking.** Headings need tighter leading (about 1.1 to 1.2), and big display type should be tightened slightly (about -0.01em), not opened up. At 1.5, a two-line title falls apart. There's also no space-above and space-below logic around headings.
6. **`h2.tag` is 11px uppercase with `letter-spacing: 0`.** Small caps-style labels need tracking (0.05 to 0.1em) and should be at least 12px. As written, they're cramped and hard to read.
7. **`blockquote` is italic, bold and uppercase together.** That's three emphasis devices stacked, and all-caps sentences read slowly. Pick one, such as italic alone.
8. **`.price, .qty` have no tabular figures.** Georgia's default figures are old-style and proportional, so columns of amounts and quantities won't line up. This matters on a recipe blog.
9. **Links have no styling.** `text-decoration: none` with `color: inherit` makes links invisible until hover, and hover is no help on touch screens.

**Suggested CSS**

```css
body {
  font-family: Georgia, serif;
  font-size: 1.125rem;
  line-height: 1.55;
  color: #333;
  text-align: left;
  hyphens: auto;
  font-synthesis: none;
}
.post { max-width: 65ch; margin: 0 auto; padding: 0 1rem; }
p { text-wrap: pretty; }

h1 {
  font-size: clamp(2rem, 5vw, 3rem);
  line-height: 1.15;
  letter-spacing: -0.01em;
  font-weight: 700;
  text-wrap: balance;
  margin: 0 0 0.5em;
}
h2 { margin: 2em 0 0.75em; line-height: 1.25; }
h2.tag {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-weight: 400;
}

a {
  color: inherit;
  text-decoration: underline;
  text-underline-offset: 0.2em;
  text-decoration-thickness: 1px;
}
a:hover { color: #c0392b; }

.price, .qty {
  font-family: Georgia, serif;
  font-variant-numeric: lining-nums tabular-nums;
  text-align: right;
}

blockquote { font-style: italic; margin: 1.5em 0; padding-left: 1em; }
```

**Notes**

- I assumed a screen and a light background. Add `lang="en"` on `<html>` so hyphenation works if you re-enable justification.
- Since `.post` now has `max-width`, add a `padding` so text doesn't touch the edges on small screens (included above).
- I removed the bold and uppercase from `blockquote` and kept only the italic. If you want it to stand out more, try a slightly larger size instead, not more weight.
- If you have spacing rules elsewhere for paragraphs and `h2`, check they still make sense. Headings should have about twice as much space above as below.
