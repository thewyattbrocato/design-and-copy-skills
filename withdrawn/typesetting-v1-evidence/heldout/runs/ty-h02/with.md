**Problems**

1. **Body size is 12px, set in pixels.** That's too small for sustained reading, and pixels ignore the reader's browser setting. This matters for a hospital audience that likely includes older readers. Use `rem`, with 1rem (16px) as the body size.
2. **`color: #999` on white is about 2.8:1 contrast.** That fails WCAG AA, which needs 4.5:1 for body text. It's probably the biggest cause of the tiredness. Use a dark grey such as `#222`.
3. **`line-height: 1.1` is far too tight for body text.** Lines nearly touch, and the eye loses its place when moving to the next line. Use a unitless value of about 1.5.
4. **`max-width: none` lets lines run the full width of the container.** On a desktop that can mean 150 or more characters per line. Cap the text at about 65ch. Put the cap on the text elements, not on a wrapper, so images and tables can stay wider.
5. **`text-align: justify` is used without hyphenation.** This creates uneven word gaps and "rivers" of white space, which are worse on narrow screens and for readers with dyslexia. Use flush-left, ragged-right text.
6. **`p {margin: 0 0 4px}` leaves almost no gap between paragraphs.** The text reads as a solid wall. Use about 0.75 to 1em between paragraphs.
7. **The `h2` is 13px, barely larger than the 12px body.** It also has the wrong spacing and styling:
   - Size: it's 1px bigger than the body, so there's almost no hierarchy.
   - All caps: uppercase headings are slow to read, and `letter-spacing: 0` is wrong for caps, which need tracking.
   - Spacing: the heading has no margins set, so it isn't tied to the text it introduces. It needs about twice as much space above as below.
   - Line height: it inherits the body's 1.1, so a wrapped heading has no room to breathe.
8. **The font stack is `Arial` with no fallback.** Add a generic family.

**Corrected version**

```css
body {
  font: 1rem/1.5 Arial, Helvetica, sans-serif;
  color: #222;
}

p, ul, ol {
  max-width: 65ch;
  margin: 0 0 1em;
  text-align: left;
}

h2 {
  font-size: 1.25rem;
  line-height: 1.25;
  font-weight: 700;
  margin: 2em 0 0.75em;
  max-width: 65ch;
  text-wrap: balance;
}
```

**Notes**

- I made the `h2` sentence case and dropped the `text-transform`. If the newsletter's style requires caps, keep them for short headings only, with `letter-spacing: 0.06em` and a size of at least 1rem.
- `#222` on white is about 16:1. Any dark grey of `#333` or darker also works.
- If you ever want justified text, for example in a print edition, add `hyphens: auto` and `lang="en"` on the `html` element. Keep it off on screen.
- If the newsletter needs other sizes, such as captions, keep the total to four to six sizes. Captions and metadata can go down to about 0.8125rem (13px).
