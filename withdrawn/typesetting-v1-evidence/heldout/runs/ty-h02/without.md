## Problems

1. **`color: #999` on white**: contrast is about 2.8:1, below the WCAG AA minimum of 4.5:1. This is the biggest cause of fatigue, and it matters more for hospital readers who may be older, stressed, or have low vision.
2. **`font: 12px`**: too small for body text. Use 16px or more. Pixel sizes also ignore user font-size preferences, so use `rem`.
3. **`line-height: 1.1`**: lines are nearly touching. Body text needs about 1.5 to 1.6.
4. **`max-width: none`**: lines run the full window width, which can reach 150+ characters. The comfortable range is 50–75, so use about `65ch`.
5. **`text-align: justify`**: without hyphenation it creates uneven word gaps and "rivers" of white space, which is especially hard for readers with dyslexia. Use left-aligned text.
6. **`p {margin: 0 0 4px}`**: paragraphs are nearly run together. Use about 1em of spacing.
7. **`h2` at 13px**: it is barely larger than the 12px body, so there is little hierarchy. It is also all caps, which slows reading, and `letter-spacing: 0` removes the spacing caps need. Use a larger size in sentence case, with space above it so it groups with the text below.
8. **`font: ... Arial`**: there is no fallback family. The shorthand also resets `font-weight` and related properties.

## Corrected version

```css
body {
  font: 1rem/1.6 Arial, Helvetica, sans-serif;  /* 16px base, scales with user settings */
  color: #222;                                   /* ~16:1 contrast on white */
  max-width: 65ch;                               /* ~65 characters per line */
  margin: 0 auto;
  padding: 0 1rem;
  text-align: left;
}

h2 {
  font-size: 1.5rem;
  line-height: 1.3;
  font-weight: 700;
  margin: 2em 0 0.5em;                           /* more space above than below */
}

p {
  margin: 0 0 1em;
}
```

Notes:
- If you want uppercase headings, keep them short and add `letter-spacing: 0.05em`. Sentence case is easier to read.
- If you want justified text, use `text-align: justify; hyphens: auto;` and set `lang="en"` on the `<html>` element. Left-aligned is still the safer choice for accessibility.
- If the newsletter is also sent as email, many email clients ignore `max-width` and `rem`. Test it there, or use a fixed-width wrapper table.
