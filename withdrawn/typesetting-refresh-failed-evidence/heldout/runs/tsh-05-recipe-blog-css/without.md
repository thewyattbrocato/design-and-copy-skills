The "cheap" feeling comes from a few settings that each break a typographic convention, and they compound. The body text is the biggest culprit.

## What's wrong

**Body text (the cramped feeling)**
- `line-height: 1.15` is far too tight for paragraphs. Body copy wants about 1.5 to 1.7.
- `font-size: 14px` is small for long-form reading. Use 17 to 19px for a serif like Georgia.
- `letter-spacing: 0.04em` on lowercase text is the "cheap" signal. Tracking is for small caps and uppercase, not body copy.
- `text-align: justify` with no hyphenation produces uneven word gaps and rivers, especially in narrow columns.
- `.post { width: 1100px }` gives line lengths of 150+ characters, so the eye loses its place. Aim for 60 to 75 characters. The fixed width also breaks on mobile.

**Headings**
- `h1` has `line-height: 1.5`, which is body-text leading. Large headings want about 1.1 to 1.2, and a wrapped title looks broken at 1.5.
- Positive tracking (`0.06em`) on a 56px bold heading looks loose. Large type usually takes slightly negative tracking.
- 56px against 14px is a 4:1 jump. That's partly because the body is too small.
- `h2.tag` is 11px uppercase with `letter-spacing: 0`. Small caps text needs open tracking (about 0.08em), and 11px is also too small to read comfortably. The tag also probably shouldn't be an `h2` semantically.

**Details**
- `a { text-decoration: none; color: inherit }` makes links invisible until hover. That's an accessibility problem, and it's bad for a recipe blog where people look for links.
- `.price, .qty` use Georgia, which has old-style numerals (3, 4, 5, 7, 9 drop below the baseline). Quantities like "1 ½ cups" and prices look uneven, and the digits don't align in columns. The declaration is also redundant, since it matches the body font.
- `blockquote` stacks italic, bold, and uppercase. That's three emphasis signals at once, and it reads as shouting. Pick one, or at most italic.

## Suggested CSS

```css
body {
  font-family: Georgia, serif;
  font-size: 18px;
  line-height: 1.6;
  color: #333;
  text-align: left;
  hyphens: auto;
}
.post { max-width: 68ch; margin: 0 auto; padding: 0 1rem; }

h1 {
  font-size: clamp(2rem, 5vw, 2.75rem);
  line-height: 1.15;
  letter-spacing: -0.01em;
  font-weight: 700;
}
.tag {                     /* consider a <p> or <span> instead of h2 */
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-weight: 600;
}

a {
  color: inherit;
  text-decoration: underline;
  text-underline-offset: 0.15em;
  text-decoration-thickness: 1px;
}
a:hover { color: #c0392b; }

.price, .qty {
  font-variant-numeric: lining-nums tabular-nums;
}

blockquote {
  font-style: italic;
  margin: 1.5em 0;
  padding-left: 1em;
  border-left: 3px solid #ddd;
}
```

## Optional upgrades
- Pair the serif body with a clean sans (for example system-ui) for the tag, the ingredient list, and the metadata. The contrast makes the page feel designed.
- Add `h2, h3 { line-height: 1.25; margin-top: 2em; }` so sections have clear vertical rhythm.
- Space paragraphs with `p { margin: 0 0 1em }` rather than extra line-height.

If you share a screenshot or the page URL, I can check how this plays out with your real content.
