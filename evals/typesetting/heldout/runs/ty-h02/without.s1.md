# What's going on

Several settings each make the text harder to read, and together they cause the tiredness and cramped feel.

1. **Line length is the biggest problem.** `width: 100%` in a 1440px window gives lines of about 1390px. At 13px that is roughly 200+ characters per line. Comfortable reading is 60-80 characters. With lines that long, the eye loses its place when it jumps back to the start of the next line, and that is what tires people out.
2. **The body text is small.** 13px Arial is below what's comfortable for long-form reading. 16px is the usual baseline.
3. **The line height is too tight.** `1.2` is fine for headings but too tight for paragraphs. Body text wants about 1.5-1.6.
4. **The letter-spacing is negative.** `-0.02em` squeezes the letters together, and at small sizes it hurts legibility. Remove it.
5. **The vertical spacing is minimal.** Paragraphs are 4px apart, list items have no spacing, and headings have 6px above them. That makes everything run together, and it's the main source of the "cramped" feeling. A heading needs more space above it than below it so it visibly belongs to the section that follows.
6. **The heading hierarchy is weak.** The h1 is 20px, h2 is 16px and h3 is 14px, against 13px body text. Headings are barely distinguishable from the text around them, so people can't scan the page.

# What I'd change

```css
body {
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  color: #1f2328;           /* softer than pure black */
  margin: 0;
}
.article {
  max-width: 720px;         /* ~70 characters per line */
  margin: 0 auto;           /* centered in the pane */
  padding: 32px 24px 64px;
}
.article h1 { font-size: 32px; line-height: 1.25; margin: 0 0 24px; }
.article h2 { font-size: 24px; line-height: 1.3;  margin: 40px 0 12px; }
.article h3 { font-size: 19px; line-height: 1.35; margin: 28px 0 8px; }
.article p  { margin: 0 0 16px; }
.article ul,
.article ol { margin: 0 0 16px; padding-left: 24px; }
.article li { margin: 0 0 8px; }
```

## Why these values

- **`max-width: 720px` with centering** fixes the biggest issue. The empty space at the sides is intentional and helps readability.
- **16px at 1.6** gives the text room to breathe.
- **The heading sizes** step up clearly (32, 24, 19). Each heading has about 3x more space above than below, which groups it with its own content.
- **The 16px paragraph and list spacing** matches the body font size, so the vertical rhythm feels consistent.
- **The system font stack** renders crisply on each OS. If you'd rather keep Arial, that's fine. It matters much less than the spacing and width.

If the pane also holds a sidebar or table of contents, apply the `max-width` to the text column rather than the whole pane. Code blocks and tables can be allowed to run wider than 720px if they need to.

I haven't rendered this against your real articles. Check a long article with images, tables and code blocks before shipping, since those may need their own spacing rules.
