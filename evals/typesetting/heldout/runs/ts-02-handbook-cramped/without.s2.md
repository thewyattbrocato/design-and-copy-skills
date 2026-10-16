Here's a revised stylesheet. Only typography and spacing changed. Colors and HTML are untouched.

```css
body {
  font: 18px/1.6 Arial, sans-serif;
  color: #2b2b2b;
  background: #fbfaf7;
  margin: 0;
}
.page {
  max-width: 68ch;
  margin: 0 auto;
  padding: 32px 24px 64px;
}
h1 {
  font-size: 32px;
  line-height: 1.2;
  margin: 0 0 16px;
}
h2 {
  font-size: 22px;
  line-height: 1.3;
  margin: 40px 0 8px;
}
p {
  margin: 0 0 1em;
}
.note {
  font-size: 14px;
  color: #777;
}
```

What changed and why:

- **Body text 13px → 18px.** 13px is small for long reading. 18px is comfortable on a 1440px screen.
- **Line height 1.2 → 1.6.** The tight leading made paragraphs read as dense blocks. 1.6 gives lines room to breathe.
- **Line length capped at `68ch`.** This is the biggest fix for the edge-to-edge problem. About 60–75 characters per line is easiest to track. The `.page` is now centered with `margin: 0 auto`. The side padding drops to 24px, which keeps small screens from touching the edges.
- **Paragraph spacing 6px → 1em.** Paragraphs now separate clearly.
- **Headings.** h2 gets a larger top margin (40px) and a smaller bottom margin (8px). That groups each heading with the text below it and separates sections. The h2 size also steps up to 22px, so the hierarchy stays clear against 18px body text. h1 goes to 32px.
- **`.note` 10px → 14px.** 10px is too small to read. 14px still looks secondary next to the body text.

One thing I can't change without altering colors: `.note` uses `#777` on `#fbfaf7`. That's about 4.2:1 contrast, just under the 4.5:1 WCAG AA target for small text. With the larger size it's more readable, but if you ever relax the color constraint, `#6b6b6b` would pass.
