# What's going on

Almost every text-comfort setting is pushed in the cramped direction, and the effects add up.

1. **Lines are far too long.** `width: 100%` in a 1440px window gives lines of about 200+ characters at 13px. Readers lose their place when jumping from the end of one line to the start of the next. Comfortable reading is roughly 60 to 80 characters per line. This is probably the biggest cause of "tiring."
2. **The text is small.** 13px is under the usual 16px body baseline, so readers strain, especially on high-resolution screens.
3. **Line height is tight.** 1.2 is a heading value. Body text usually wants about 1.5 to 1.65. At 1.2, descenders and ascenders nearly touch the next line.
4. **Letter-spacing is negative.** `-0.02em` squeezes the letters together, which hurts legibility at small sizes. Remove it.
5. **There's almost no space between blocks.** 4px paragraph gaps and 0 between list items make everything read as one dense block, and you can't see where one idea ends.
6. **The heading hierarchy is weak and the spacing is backwards.** An h2 at 16px sits just above 13px body text. Headings have the same 6px above and below, so they don't visibly attach to the section they introduce. A heading should have more space above than below.
7. **The side padding doesn't help.** 24px of padding on a full-width pane leaves the text hugging the left while a huge area on the right is empty.

# What I'd change

```css
body {
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  color: #222;
  margin: 0;
}
.article {
  max-width: 70ch;      /* about 70 characters per line */
  margin: 0 auto;       /* centered; use 0 if you want it left-aligned */
  padding: 32px 24px 64px;
}
.article h1 { font-size: 32px; line-height: 1.25; margin: 0 0 16px; }
.article h2 { font-size: 24px; line-height: 1.3;  margin: 40px 0 12px; }
.article h3 { font-size: 19px; line-height: 1.35; margin: 28px 0 8px; }
.article p  { margin: 0 0 16px; }
.article ul,
.article ol { margin: 0 0 16px; padding-left: 1.5em; }
.article li { margin: 0 0 6px; }
```

## Why these values

- **`max-width: 70ch`** fixes the line length. It's the most noticeable change.
- **16px with 1.6 line height** gives the text room to breathe.
- **Dropping the letter-spacing** returns the font to its designed spacing.
- **Heading sizes step from 32 to 24 to 19px.** The margins are larger above than below, so each heading groups with the text that follows it.
- **16px paragraph gaps and 6px list gaps** make the structure scannable.
- **The `system-ui` font stack** renders crisply on each OS. Arial still works as a fallback if you want to keep it.

## Two optional follow-ups

- Check contrast. If the text is a light gray, use something near `#222` on white. I couldn't see your colors, so this is worth a quick look.
- Add `img { max-width: 100%; height: auto; }` and some margin around code blocks and tables. They'll look cramped next to the new spacing if left alone.

I'd ship this and see whether the complaints stop. If your layout has a sidebar or table of contents in the same pane, adjust the `max-width` to apply to the text column only.
