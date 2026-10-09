Your CSS has four problems that compound. The fix is mostly larger numbers and a cap on line length.

**What's going on**

1. **Line-height 1.2 is the main cause of "cramped."** Lines sit almost on top of each other, so the eye has trouble moving from one line to the next. Body text usually needs about 1.5.
2. **Lines are far too long.** The article fills the full 1440px window, so each line is roughly 1,390px wide, about 200 or more characters. Readers lose their place when they jump back to the start of a line, and that wears them out over a long article. Aim for about 65 characters.
3. **Text is small and fixed in pixels.** 13px Arial is small for reading, and `px` ignores the user's browser text-size setting.
4. **`letter-spacing: -0.02em` tightens the letters.** Arial is already fairly tight, so negative tracking makes words crowd together. Use `normal`.
5. **Spacing doesn't separate sections.** Paragraphs have 4px between them, and headings have 6px above and below. Nothing groups content or marks where a new section starts, which makes the page hard to scan. A heading should have about twice as much space above it as below.
6. **The heading sizes are cramped against the body.** The h3 at 14px is barely bigger than 13px body text, so the levels don't read as distinct.

**What I'd change**

```css
body {
  font-family: Arial, sans-serif;
  font-size: 1rem;          /* 16px */
  line-height: 1.5;
  letter-spacing: normal;
  margin: 0;
}
.article {
  max-width: 65ch;          /* keeps lines to about 65 characters */
  margin: 0 auto;
  padding: 0 24px;
}
.article h1 { font-size: 1.75rem; line-height: 1.2;  margin: 0 0 1rem; }
.article h2 { font-size: 1.375rem; line-height: 1.25; margin: 2rem 0 0.5rem; }
.article h3 { font-size: 1.125rem; line-height: 1.3;  margin: 1.5rem 0 0.5rem; }
.article p  { margin: 0 0 1em; }
.article ul, .article ol { margin: 0 0 1em; padding-left: 1.5em; }
.article li { margin: 0 0 0.25em; }
```

The heading sizes step up by about 1.25× each level (16, 18, 22, 28px), so each level is easy to tell apart.

**Notes**

- I haven't rendered this in a browser. Changing the body size and line height first will show most of the improvement, so check that before the rest.
- The `65ch` cap is the change customers will notice most on a wide screen. If your articles include wide tables or images, they may need `max-width` set separately so they aren't clipped by the column.
