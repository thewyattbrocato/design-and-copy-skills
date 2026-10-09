**What's going on**

1. **Lines are too long.** The article fills about 1,390px of a 1440px window, which holds roughly 200 characters per line. Readers lose their place when they jump that far back to the start of the next line. Comfortable reading is about 45 to 75 characters.
2. **The text is small and tightened.** 13px is small for long reading, and `letter-spacing: -0.02em` pushes letters closer together, which slows reading. Body text should not be letterspaced.
3. **Line spacing is too tight.** `line-height: 1.2` packs lines together. Body text reads best around 1.5.
4. **Paragraphs and headings barely separate.** A 4px gap between paragraphs makes blocks run together. Headings have equal space above and below (6px), so they float instead of marking a new section. Lists have no space between items.
5. **The type scale is flat.** H3 (14px) is almost the same as body (13px), so the hierarchy is weak.

**Changes**

```css
body {
  font-family: Arial, sans-serif;
  font-size: 1rem;          /* 16px */
  line-height: 1.5;
  letter-spacing: normal;
  margin: 0;
}
.article {
  max-width: 68ch;          /* caps the line length; centers the column */
  margin: 0 auto;
  padding: 0 24px;
}
.article h1 { font-size: 1.75rem; line-height: 1.2;  margin: 0 0 0.5em; }
.article h2 { font-size: 1.375rem; line-height: 1.25; margin: 1.75em 0 0.5em; }
.article h3 { font-size: 1.125rem; line-height: 1.3;  margin: 1.5em 0 0.4em; }
.article p  { margin: 0 0 1em; }
.article li { margin: 0 0 0.35em; }
```

Why each change:
- **`max-width: 68ch`**: keeps lines near 70 characters. This is the biggest fix.
- **`1rem` body, `line-height: 1.5`**: larger, airier text that is easier to read for long stretches.
- **`letter-spacing: normal`**: removes the tightening.
- **Heading margins above roughly double those below**: each new section is clearly marked.
- **Paragraph gap of `1em`**: separates blocks without making the page look loose.
- **Clearer scale (28 / 22 / 18 / 16px)**: each level is visibly distinct.

**Assumptions:** the root font size is the browser default of 16px, and you want to keep Arial. Check the result at a 1440px window and on a phone-width screen. If the column looks too narrow at 1440px, raise `68ch` to `72ch`.
