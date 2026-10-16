Here's a revised stylesheet. Colors are untouched, and no HTML changes are needed.

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
  padding: 32px 24px;
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

- **Body text 13px → 18px.** 13px is small for long reading. 18px is comfortable on a desktop screen.
- **Line height 1.2 → 1.6.** The tight spacing made lines run together. Looser leading is the biggest fix for the "tiring" feel.
- **Line length capped at `68ch`.** Paragraphs ran edge to edge at 1440px, which is far too long for the eye to track. About 65–70 characters per line is the readable range. The column is centered with `margin: 0 auto`.
- **Paragraph spacing 6px → `1em`.** Paragraphs now separate visibly instead of blurring into one block.
- **Headings.** The h2 top margin grows from 16px to 40px, and the bottom margin is small. Each heading then sits closer to its own section than to the previous one, which makes the page easier to scan. The h1 and h2 sizes are scaled up to keep the hierarchy over the larger body text.
- **`.note` 10px → 14px.** 10px is hard to read. Notes are still clearly secondary at 14px.

One thing to check: `.note` is `#777` on `#fbfaf7`, which is about 4.3:1 contrast. That's just under the WCAG AA 4.5:1 minimum for small text. You asked me not to change colors, so I left it. Darkening it to `#6b6b6b` would fix it if you want.
