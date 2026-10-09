The article is cramped for three reasons, and the first one matters most.

1. **Lines are far too long.** `.article` is `width: 100%` in a 1440px window, so each line runs roughly 1,400px. At 13px Arial that's around 200+ characters per line. Readers lose their place when they jump back to the start of the next line, and that wears them out. Comfortable reading is roughly 50–75 characters per line.
2. **The text is small and tightly packed.** 13px is small for body copy (16px is the usual baseline). `line-height: 1.2` is too tight; body text usually needs about 1.5. Together these make every line dense.
3. **Negative letter-spacing hurts legibility.** `-0.02em` pushes letters together. That's fine for large display type, but on small body text it makes words harder to tell apart.

The spacing also makes it worse. Paragraphs have only 4px below them and list items have none, so blocks run together. Headings have 6px above and below, so a heading doesn't visually separate the section above it from the content it introduces.

Here's what I'd change:

```css
body {
  font-family: Arial, sans-serif;
  font-size: 16px;
  line-height: 1.5;
  letter-spacing: normal;
  margin: 0;
}
.article {
  max-width: 70ch;       /* limits line length; ~600–700px */
  margin: 0 auto;        /* centers the column in the pane */
  padding: 32px 24px;
}
.article h1 { font-size: 32px; line-height: 1.2; margin: 0 0 16px; }
.article h2 { font-size: 24px; line-height: 1.3; margin: 40px 0 12px; }
.article h3 { font-size: 19px; line-height: 1.3; margin: 28px 0 8px; }
.article p  { margin: 0 0 16px; }
.article ul,
.article ol { margin: 0 0 16px; padding-left: 1.5em; }
.article li { margin: 0 0 8px; }
```

The most important changes are the `max-width` on `.article` and the body font size and line height. Headings now have more space above than below, so each one attaches to the content that follows it.

I haven't seen the rendered page, so treat these numbers as starting points. The easiest check is to show the old and new versions to a few customers or teammates and compare. If your product UI is intentionally dense, keep 13–14px for the chrome around the article, but the article body itself should be at least 16px.
