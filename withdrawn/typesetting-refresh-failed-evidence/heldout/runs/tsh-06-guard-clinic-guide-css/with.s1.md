This stylesheet is sound, and I'd ship it with one small addition.

**What already works:**
- **Body:** 1.125rem at 1.6 leading, in rem.
- **Measure:** a 38rem column gives about 65 characters per line.
- **Headings:** tight leading, balanced wrapping, and about three times as much space above `h2` as below.
- **Scale:** six roles, each with its own size, and the steps between them are clear.
- **Labels:** the caps label is 12px, tracked and semibold.
- **Tables:** tabular figures with right-aligned number columns.
- **Links:** underlined, with a visible focus ring.
- **Contrast:** the muted text and link colors look fine on white.

**One change:** add `text-wrap: pretty` to paragraphs. It avoids one-word last lines.

```css
p { margin: 0 0 1em; hyphens: auto; text-wrap: pretty; }
```

**Check before launch:** `hyphens: auto` only works if the page has `<html lang="en">` (or the right language). Without it, browsers skip hyphenation, and screen readers may pronounce the text wrong. I can't see your HTML, so please confirm it's there.

The `p + p { margin-top: 0; }` rule does nothing, because paragraphs already have no top margin. It's harmless, so I left it. I changed nothing else.
