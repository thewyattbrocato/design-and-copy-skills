The text is hard to read because several settings push in the same direction: the text is small, the lines are tightly packed, and the lines are very long. Any one of these would be a minor issue. Together they make the page feel dense.

**What's going on**

1. **Text is small.** 13px is well below the 16px that most reading guidelines treat as a floor for body text. Help articles are read for a long time, so small text tires people faster.
2. **Lines are cramped.** `line-height: 1.2` puts the lines almost on top of each other. Body text usually needs about 1.5 to 1.6.
3. **Letters are squeezed.** `letter-spacing: -0.02em` tightens the gaps between letters. That's useful for big display headings but makes body text harder to read.
4. **Lines are too long.** With `width: 100%` on a 1440px window, each line runs about 1,400px, or roughly 200 characters. Readers lose their place when they move from the end of one line to the start of the next. Comfortable reading is about 60 to 75 characters per line.
5. **Spacing is too tight.** Paragraphs are only 4px apart. Headings have 6px above and below, so they don't clearly belong to the section they start. List items have no space between them. The article also has no top or bottom padding.
6. **Headings barely stand out.** At 13px body text, the h2 (16px) and h3 (14px) are only a little bigger, so the structure is hard to scan.

**What I'd change**

```css
body {
  font-family: system-ui, -apple-system, "Segoe UI", Arial, sans-serif;
  font-size: 17px;
  line-height: 1.6;
  letter-spacing: normal;
  margin: 0;
}
.article {
  max-width: 68ch;          /* keeps lines to roughly 65-75 characters */
  margin: 0 auto;           /* centers the column in the wide pane */
  padding: 40px 24px 64px;
}
.article h1 { font-size: 2em;    line-height: 1.25; margin: 0 0 0.5em; }
.article h2 { font-size: 1.4em;  line-height: 1.3;  margin: 1.6em 0 0.5em; }
.article h3 { font-size: 1.15em; line-height: 1.3;  margin: 1.3em 0 0.4em; }
.article p  { margin: 0 0 1em; }
.article ul, .article ol { margin: 0 0 1em; padding-left: 1.5em; }
.article li { margin: 0 0 0.4em; }
```

The main changes:

- **Body text goes from 13px to 17px**, with line height at 1.6 and normal letter spacing.
- **`max-width: 68ch` with `margin: 0 auto`** is the biggest fix. The text column stays readable and sits centered on a wide screen.
- **Spacing is set in `em`** so it scales with the text. Headings get more space above than below, so each heading sits closer to the section it introduces.
- **Heading sizes are spread out** (34px, 24px, 20px) so the structure is easier to scan.

**Before rolling it out**

- Check the result at a few window widths, especially narrow ones. On a phone the 24px side padding may need to shrink.
- If you can, A/B test the old and new styles on a sample of articles. Measuring time on page or scroll depth will tell you more than my reasoning alone, and it gives you something concrete to show stakeholders.
- Your design system or product may already define a font or color scale. If so, use those values in place of the ones I picked.
