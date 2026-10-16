**What's going on:** the stylesheet has five separate problems, and together they produce "tiring and cramped."

1. **Text is too small.** 13px is below a comfortable reading size, and it's set in fixed px.
2. **Lines are too long.** `width: 100%` in a 1440px window gives roughly 200+ characters per line. The eye loses its place on the return sweep, which is the main cause of tiredness. Comfortable is about 45–75 characters.
3. **Leading is too tight.** `line-height: 1.2` is a heading value. Body text wants about 1.5.
4. **Body text is letterspaced.** `-0.02em` tightens the letters until they crowd, and it hurts small text most. Leave tracking alone for body copy.
5. **Spacing is too small and in the wrong places.**
   - Paragraphs are separated by only 4px, so they barely register as separate.
   - Headings have equal space above and below (6px/6px), so they float between sections instead of attaching to what follows.
   - List items have zero spacing.
   - The heading sizes (20/16/14px) sit too close to a 13px body, so there's little contrast between levels.

**What I'd change:**

```css
body {
  font-family: Arial, sans-serif;
  font-size: 1.0625rem;      /* 17px */
  line-height: 1.5;
  margin: 0;
}
.article {
  max-width: 42rem;          /* ~65–70 characters per line */
  padding: 0 1.5rem;
  margin: 0 auto;
}
.article h1 { font-size: 2rem;     line-height: 1.2;  margin: 0 0 1rem; text-wrap: balance; }
.article h2 { font-size: 1.5rem;   line-height: 1.25; margin: 2.5rem 0 0.75rem; text-wrap: balance; }
.article h3 { font-size: 1.1875rem; line-height: 1.3; margin: 2rem 0 0.5rem; }
.article p  { margin: 0 0 1rem; text-wrap: pretty; }
.article li { margin: 0 0 0.5rem; }
```

**Why each change helps:**
- **Larger rem body text:** easier to read, and it respects users' browser font-size settings.
- **`max-width` with centering:** this is the biggest fix. The text stays in a readable column, and the empty space on a wide screen is fine.
- **Line-height 1.5 for body, tighter for headings:** gives the lines room to breathe while keeping wrapped headings compact.
- **No letter-spacing:** the font's own spacing is designed to work.
- **Headings with about twice as much space above as below:** each heading groups with the text it introduces.
- **Paragraph and list gaps of about half to one line:** the content is easier to scan.
- **Clearer size steps (32/24/19px against 17px body):** the heading levels are distinct from each other and from the body.

I assumed a light background and that you want to keep Arial. If you're open to changing the typeface, that's a separate decision from these fixes. Check the result with a few real articles that have long lists, since list spacing is the easiest part to tune by eye.
