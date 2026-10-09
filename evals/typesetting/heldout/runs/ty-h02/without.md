**What's going on:** the type is small, tightly spaced, and stretched across the whole screen. Each of those makes reading harder, and together they make it tiring.

1. **13px text is small.** Body text for sustained reading should be 16–18px.
2. **`line-height: 1.2` is very tight.** Lines of paragraph text need about 1.5–1.7. At 1.2 the lines almost touch, and the eye has trouble tracking from one line to the next.
3. **`letter-spacing: -0.02em` squeezes the letters together.** That's a trick for large display headings. At small sizes it hurts legibility. Remove it.
4. **`width: 100%` on a 1440px window gives lines of about 200+ characters.** Comfortable reading is roughly 60–80 characters per line. Long lines make it easy to lose your place when you jump back to the start of the next one. This is probably the biggest single cause of "tiring."
5. **The vertical spacing is nearly zero.** Paragraphs have 4px of space between them, list items have none, and headings have only 6px above them. A heading needs more space above than below, so it clearly attaches to the text it introduces. Right now nothing separates one section from the next, which is what makes it feel cramped.
6. **The heading hierarchy is flat.** 20/16/14px against 13px body means an h3 is barely larger than the text around it. Readers can't skim the page by its headings.

**What I'd change:**

```css
body {
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif;
  font-size: 17px;
  line-height: 1.6;
  color: #1f2328;          /* softer than pure black */
  margin: 0;
}
.article {
  max-width: 44rem;        /* ~700px, roughly 70 characters per line */
  margin: 0 auto;          /* center it in the window */
  padding: 32px 24px 64px;
}
.article h1 { font-size: 2rem;    line-height: 1.25; margin: 0 0 1rem; }
.article h2 { font-size: 1.5rem;  line-height: 1.3;  margin: 2.5rem 0 0.75rem; }
.article h3 { font-size: 1.2rem;  line-height: 1.35; margin: 2rem 0 0.5rem; }
.article p  { margin: 0 0 1.1em; }
.article ul,
.article ol { margin: 0 0 1.1em; padding-left: 1.5em; }
.article li { margin: 0 0 0.4em; }
```

**Why these values:**
- `max-width` with `margin: 0 auto` fixes the line length. The article gets a centered column and the extra space becomes margin. That's normal for documentation.
- Spacing is in `em`/`rem`, so it scales with the font size if a user zooms or changes their browser's default.
- Each heading has more space above than below, so it groups with what follows.
- I dropped the fixed Arial in favor of the system font stack, which renders crisply on each OS. Arial is fine if brand requires it, and the other changes matter more than the font.

**Things to check:**
- If your articles have wide tables or code blocks, let those scroll horizontally (`overflow-x: auto`) instead of widening the column.
- On mobile, 17px with 24px side padding works as is. If you see issues, test at 375px wide.
- The 17px size and the 44rem width are starting points. Try them on a real article, and nudge the size between 16 and 18px if it feels off.

I'd expect the width cap, the line-height, and the font size to make most of the difference. The spacing between paragraphs and headings does the rest.
