**What's going on:** the stylesheet is set for a dense tool, not for reading. Each problem below makes the text harder to read on its own, and together they produce the tired, cramped feel.

**What works:** Arial is a safe, legible face. The side padding (24px) is reasonable. Headings step down from h1 to h3, so the outline reads correctly.

**What fails, and the fix:**

1. **Lines are far too long.** At 13px on a 1440px window, the text runs roughly 180 to 200 characters per line. The eye loses its place on every return sweep. *Fix:* cap the text column at about 70 characters and center it.

2. **Body text is too small and fixed in px.** 13px is small for reading, and fixed px ignores the user's browser font setting. *Fix:* use 1rem (16px).

3. **Line height is too tight.** At 1.2, lines nearly touch, which is the main cause of "cramped." *Fix:* 1.5 for body text.

4. **Negative letter-spacing tightens body text.** Tight tracking makes small sans-serif text harder to tell apart. *Fix:* remove it.

5. **Paragraphs and list items barely separate.** A 4px paragraph gap and 0px between list items run the blocks together. *Fix:* a gap of about one line between paragraphs, and some space between list items.

6. **Headings float with equal space above and below.** The 6px above a heading matches the 6px below, so a heading doesn't visibly belong to the section it starts. *Fix:* roughly twice as much space above as below.

7. **The heading sizes are uneven and crowd the body.** h3 at 14px is barely bigger than 13px body text. *Fix:* a steadier scale of about 1.25 steps.

**Revised CSS:**

```css
body {
  font-family: Arial, sans-serif;
  font-size: 1rem;          /* 16px, respects user font settings */
  line-height: 1.5;
  letter-spacing: normal;
  margin: 0;
}
.article {
  max-width: 70ch;          /* keeps lines to ~70 characters */
  margin: 0 auto;           /* center the column in the 1440px pane */
  padding: 0 24px;
}
.article h1 { font-size: 1.75rem; line-height: 1.25; margin: 0 0 0.75em; }
.article h2 { font-size: 1.375rem; line-height: 1.25; margin: 1.5em 0 0.5em; }
.article h3 { font-size: 1.125rem; line-height: 1.25; margin: 1.25em 0 0.4em; }
.article p  { margin: 0 0 1em; }
.article ul,
.article ol { margin: 0 0 1em; padding-left: 1.25em; }
.article li { margin: 0 0 0.5em; }
```

Notes:
- I assumed a screen layout, a light background, and sizes in rem. If your site sets the root font size somewhere else, check that 1rem is 16px.
- I haven't checked text color or contrast. If the gray is pale, that's a second likely cause of the tiring feel, and it's worth checking before anything else.
