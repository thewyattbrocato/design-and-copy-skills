This stylesheet is sound, and I'd change almost nothing.

**What already works**
- **Body:** 1.125rem at 1.6 line height in a 38rem column gives about 65 characters per line, which is right for long reading.
- **Headings:** the line heights are tight (1.12 and 1.25), `text-wrap: balance` is set, and there's about 3:1 space above versus below each heading.
- **Scale:** there are five sizes, each with a role, and the steps between them are clear.
- **Labels and notes:** the all-caps label is 12px, tracked and sentence-length-safe. The muted gray is about 5.9:1 against white, so small notes stay legible.
- **Tables and links:** the tables use tabular figures with right-aligned number columns. Links are underlined with a visible focus ring.

**One tweak to make**

Add `text-wrap: pretty` to paragraphs so the last line doesn't end on a single word:

```css
p { margin: 0 0 1em; hyphens: auto; text-wrap: pretty; }
```

**Before launch**
- `hyphens: auto` only works if the page has `<html lang="en">` (or the right language). Without it, browsers skip hyphenation, so please confirm that attribute.
- `p + p { margin-top: 0; }` does nothing, because `p` already has no top margin. It's harmless, so I left it.

I haven't edited any files.
