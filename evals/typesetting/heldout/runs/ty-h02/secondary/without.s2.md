The text is too small and too tightly packed, and the lines are far too long. Each problem makes the others worse.

**What's going on**

1. **Lines are too long.** The article fills about 1,390px of a 1440px window at 13px type, which is roughly 200+ characters per line. Comfortable reading is about 45-75 characters. Readers have to travel too far across each line and lose their place, which is tiring.
2. **Text is small.** 13px is below what most people find comfortable for body copy. 16px is the usual starting point.
3. **Line spacing is too tight.** `line-height: 1.2` leaves little room between lines, so the eye has trouble moving from one to the next. 1.5-1.6 is the usual range for body text.
4. **Negative letter-spacing.** `-0.02em` pulls letters together. That hurts legibility at small sizes and gives the page a cramped look.
5. **Almost no vertical rhythm.** Paragraphs have a 4px gap and list items have none, so blocks run together with no breathing room between them.
6. **Weak heading hierarchy and spacing.** h3 (14px) is nearly the body size. Headings have only 6px above and below, so a heading sits as close to the previous section as to the one it introduces. Headings need more space above than below so readers can see what belongs to what.
7. **No vertical padding.** The article text touches the top of the pane.

**What I'd change**

```css
body {
  font-family: Arial, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  letter-spacing: normal;
  margin: 0;
}
.article {
  max-width: 70ch;   /* about 620px at 16px: the reading column */
  margin: 0 auto;    /* centers the column in the 1440px pane */
  padding: 32px 24px;
}
.article h1 { font-size: 2em;    line-height: 1.25; margin: 0 0 0.5em; }
.article h2 { font-size: 1.5em;  line-height: 1.3;  margin: 1.6em 0 0.5em; }
.article h3 { font-size: 1.2em;  line-height: 1.3;  margin: 1.4em 0 0.4em; }
.article p  { margin: 0 0 1em; }
.article ul, .article ol { margin: 0 0 1em; padding-left: 1.5em; }
.article li { margin: 0 0 0.4em; }
```

Why these values:
- **`max-width: 70ch` with `margin: 0 auto`** fixes the line length and centers the column. If you'd rather keep the text left-aligned, drop the `margin: auto`.
- **16px / 1.6** gives the text room to breathe.
- **Headings with more space above than below** tie each heading to the content it introduces.
- **`em` units** scale the headings from the body size, so you change one number to resize everything.

**Things to check**

- Setting `font-size` on `body` also affects navigation and other page chrome. If those parts shouldn't change, move the typography rules under `.article`.
- Read a long article at 1440px and at a narrow laptop width. The column should look balanced at both.
- Ask two or three customers to read the revised version and compare. I'm working from the CSS alone, not the markup or real content, so the numbers are starting points, not final answers.
