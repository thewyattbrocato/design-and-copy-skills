**What's going on:** Several settings each make the text a little harder to read, and together they make it tiring and cramped.

1. **Text is too small.** 13px Arial is below comfortable reading size, and it's fixed in px, so it ignores users' browser size settings.
2. **Lines are too long.** `width: 100%` in a 1440px window gives lines of about 200 characters. The eye loses its place on the return sweep. Readable lines are about 60–75 characters.
3. **Leading is too tight.** `line-height: 1.2` is a heading value. Body text needs about 1.5, and more when lines are long.
4. **Negative letter-spacing.** `-0.02em` on body text squeezes letters together. Small text needs the font's normal spacing.
5. **Almost no paragraph or list spacing.** 4px between paragraphs and 0 between list items make the page a solid block.
6. **Headings sit too close to the text above them.** Each heading has equal 6px space above and below, so it doesn't clearly belong to the section that follows. The sizes are also close together (13/14/16px), so hierarchy is weak.

**What I'd change:**

```css
body {
  font-family: Arial, sans-serif;
  font-size: 1rem;
  line-height: 1.5;
  margin: 0;
}
.article {
  max-width: 44rem;       /* about 65–75 characters per line */
  padding: 0 1.5rem;
  margin: 0 auto;
}
.article h1 { font-size: 2rem;     line-height: 1.2;  margin: 0 0 1rem;       text-wrap: balance; }
.article h2 { font-size: 1.5rem;   line-height: 1.25; margin: 2.5rem 0 0.75rem; text-wrap: balance; }
.article h3 { font-size: 1.25rem;  line-height: 1.3;  margin: 2rem 0 0.5rem;    text-wrap: balance; }
.article p  { margin: 0 0 1rem; text-wrap: pretty; }
.article li { margin: 0 0 0.5rem; }
```

- **Size:** 1rem is 16px by default and respects user settings. The `letter-spacing` rule is removed.
- **Line length:** `max-width: 44rem` keeps lines readable at any window width. `margin: 0 auto` centers the column. If your articles include wide tables or screenshots, let those break out of the column instead of widening the text.
- **Headings:** Each has about three times more space above than below, so it groups with its own section. The sizes now step clearly (32/24/20px).
- **Spacing:** Paragraphs get a full line of space between them. List items get half a line.

I haven't checked this against your real articles. If they have dense content such as code blocks or tables, check those separately. Also check text color: if the body is light gray, darken it.
