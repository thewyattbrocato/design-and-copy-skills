**What's going on:** The stylesheet has five separate problems, and together they make the page tiring.

1. **The text is too small.** 13px is below a comfortable reading size, and customers read these articles to follow instructions.
2. **The lines are far too long.** `width: 100%` on a 1440px window gives roughly 200+ characters per line. The comfortable range is 45–75. Your eye loses its place when it jumps back to the next line, and this is probably the biggest cause of the tiredness.
3. **The lines sit too close together.** A line height of 1.2 is a heading value. Body text wants about 1.5.
4. **Negative letter-spacing squeezes the letters.** `-0.02em` on body text makes small letters crowd and blur. Only large display type should be tightened, and only slightly.
5. **The spacing between blocks is almost gone.**
   - Paragraphs have 4px between them, and list items have 0.
   - Headings have equal space above and below (6px/6px), so they don't clearly start a new section.
   - The sizes are also close together (13/14/16/20px), so the headings barely stand out.

**What I'd change:**

```css
body {
  font-family: Arial, sans-serif;
  font-size: 1.125rem;      /* 18px: comfortable for long reading */
  line-height: 1.5;
  margin: 0;
}
.article {
  max-width: 65ch;          /* ~65 characters per line */
  padding: 0 24px;
  margin: 0 auto;           /* centered in the window */
}
.article h1 { font-size: 2rem;     line-height: 1.2;  margin: 0 0 1rem; }
.article h2 { font-size: 1.5rem;   line-height: 1.25; margin: 2.5rem 0 0.75rem; }
.article h3 { font-size: 1.25rem;  line-height: 1.3;  margin: 2rem 0 0.5rem; }
.article p  { margin: 0 0 1em; }
.article li { margin: 0 0 0.5em; }
```

Why each change helps:
- **`1.125rem` body:** it's easy to read, and `rem` units respect users' browser font settings.
- **`max-width: 65ch`:** this fixes the line length. It's on the article, not `body`, so other pages are unaffected.
- **`line-height: 1.5`:** this gives the eye room to find the next line. Headings stay tighter at 1.2–1.3 because they're larger and short.
- **Letter-spacing removed:** the font's own spacing is already tuned for body text.
- **Heading margins:** each heading gets about 3× more space above than below. That ties it to the text it introduces and separates it from the previous section.
- **`1em` paragraph gap and `0.5em` list gap:** these give the text visible breathing room.
- **Heading sizes (32/24/20/18px):** each step is clearly distinct, so people can scan the page.

Two assumptions: this is a light background with dark text, and Arial stays as the font. If your pages include tables or code blocks, they need separate rules. They can be wider than the 65ch text column.
