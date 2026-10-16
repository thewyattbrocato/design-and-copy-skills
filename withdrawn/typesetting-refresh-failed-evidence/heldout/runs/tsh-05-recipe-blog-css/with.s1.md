Nothing here is a single big mistake. Several small ones add up to cramped and cheap: tight leading, tracked lowercase, tiny unspaced caps, and a very wide column.

## What's wrong

1. **Body is too small for the container.** 14px text in a 1100px box runs about 150 characters per line. That's twice the comfortable maximum, so the eye loses its place going back to the next line. With 1.15 leading, the lines also sit almost touching. This is the main cause of the cramped feel.
2. **Letter-spacing on lowercase body (`0.04em`).** Tracking lowercase makes the text look loose and slightly amateur. Georgia's own spacing is already good.
3. **Justified text with no hyphenation.** On a wide column this leaves uneven word gaps. Switch to left-aligned, ragged-right text.
4. **The h1 is set backwards.** `line-height: 1.5` is far too loose for 56px, so a wrapped title falls apart into separate lines. `0.06em` tracking on big display type adds to that. Large type should be tighter: leading about 1.1–1.2, tracking slightly negative.
5. **`h2.tag` is too small and unspaced.** Uppercase at 11px with `letter-spacing: 0` is hard to read. Small caps labels need 12px or more and about 0.05–0.1em of tracking.
6. **Links are invisible.** `color: inherit; text-decoration: none` means readers can't tell a link from plain text until they hover.
7. **`.price, .qty` are set in Georgia, which has old-style figures.** In Georgia, digits like 3, 4, 5, 7 and 9 drop below the baseline, and the widths are uneven. Columns of prices won't line up, and `tabular-nums` can't fix that because Georgia doesn't include those features. These need a different face.
8. **The blockquote stacks three emphasis devices.** Italic, bold and uppercase together is shouty, and Georgia has no true bold italic, so the browser fakes it. Pick one device.

## Suggested CSS

```css
body {
  font-family: Georgia, serif;
  font-size: 1.125rem;      /* 18px; recipe pages are long-form reading */
  line-height: 1.55;
  color: #333;
  text-align: left;
  font-synthesis: none;
}
.post { max-width: 65ch; margin: 0 auto; padding: 0 1rem; }
p { text-wrap: pretty; }

h1 {
  font-size: clamp(2.25rem, 5vw, 3.5rem);
  line-height: 1.1;
  letter-spacing: -0.015em;
  font-weight: 700;
  text-wrap: balance;
}
h2.tag {
  font-size: 0.75rem;       /* 12px */
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-weight: 600;
}
a {
  color: inherit;
  text-decoration: underline;
  text-underline-offset: 0.2em;
  text-decoration-thickness: 1px;
}
a:hover { color: #c0392b; }

.price, .qty {
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  font-variant-numeric: tabular-nums lining-nums;
  text-align: right;
}
blockquote { font-style: italic; margin: 1.5em 0 1.5em 1.5em; }
```

## Notes

- Capping the text at `65ch` fixes the line length without shrinking the page. If you want a wider layout for photos, keep `.post` wide and put the `max-width` on `p` and `li` instead.
- The h1 range of 36–56px is only a suggestion. Keep your 56px if you like it on desktop. Just fix the leading and tracking.
- Make sure each paragraph has a gap of about `1em` below it. If your reset removes paragraph margins, add `p { margin: 0 0 1em; }`.
- Give headings roughly twice as much space above as below so they attach to the text that follows.
- I assumed this is a screen-only page with a light background, and that you want to keep Georgia for body text. If the ingredient lists are in tables, I can set those up as well.
