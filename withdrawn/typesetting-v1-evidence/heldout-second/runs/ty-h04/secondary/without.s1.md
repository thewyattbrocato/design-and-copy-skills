Here's a revised version. It keeps Georgia and the same measure, and adds the details that make long-form text read as printed editorial work.

```css
.essay {
  font-family: Georgia, 'Times New Roman', serif;
  font-size: 1.1875rem;          /* slightly larger body for long reads */
  line-height: 1.7;
  max-width: 36rem;
  margin: 0 auto;
  padding: 0 1.25rem;
  color: #1a1a1a;
  font-kerning: normal;
  font-variant-ligatures: common-ligatures;
  text-rendering: optimizeLegibility;
  hyphens: auto;                 /* needs lang="en" on the page */
}
.essay h1 {
  font-size: clamp(2.25rem, 5.5vw, 3.25rem);
  font-weight: 700;
  line-height: 1.08;
  letter-spacing: -0.02em;
  text-wrap: balance;
  margin: 0 0 0.6em;
}
.essay h2 {
  font-size: 1.625rem;
  font-weight: 700;
  line-height: 1.2;
  letter-spacing: -0.01em;
  text-wrap: balance;
  margin: 2.4em 0 0.6em;
}
.essay p {
  margin: 0;
  text-wrap: pretty;
}
.essay p + p {
  text-indent: 1.5em;            /* book-style indent instead of paragraph gaps */
}
.essay h2 + p,
.essay blockquote + p {
  text-indent: 0;                /* no indent directly after a heading or quote */
}
.essay .kicker {
  font: 600 0.75rem/1 system-ui, sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: #6b6b6b;
  margin-bottom: 1.25rem;
}
.essay blockquote {
  margin: 2em 0;
  padding: 0 0 0 1.25rem;
  border-left: 2px solid #1a1a1a;
  font-size: 1.3125rem;
  font-style: italic;
  line-height: 1.5;
  color: #333;
}
.essay .stat {
  font-variant-numeric: tabular-nums lining-nums;
}
```

**What changed and why**

- **Body size and leading:** 1.1875rem with 1.7 line height. Long essays read more comfortably with a little more air.
- **Text rendering:** kerning, ligatures, and `hyphens: auto` give smoother, more typeset-looking text. Hyphenation only works if the page has `lang="en"` on the `<html>` element.
- **Headings:** bolder, tighter tracking on the h1 and h2, and `text-wrap: balance` so headings don't leave a single orphaned word on the last line.
- **Paragraphs:** `text-wrap: pretty` avoids short final lines. Paragraphs use first-line indents instead of gaps, which is the most "printed book" change. If you prefer web-style spacing, replace the `.essay p + p` rule with `margin-top: 1em; text-indent: 0;`.
- **Kicker:** a muted gray so it reads as a label, not a competing headline.
- **Blockquote:** larger italic, a thinner dark rule instead of gray, and more vertical space around it.

**Optional: drop cap on the opening paragraph**

```css
.essay > p:first-of-type::first-letter {
  float: left;
  font-size: 3.6em;
  line-height: 0.85;
  font-weight: 700;
  padding: 0.08em 0.1em 0 0;
}
```

I haven't rendered this in a browser, so check it on a real essay with long paragraphs and a block quote. Fine-tune the drop cap size and the `max-width` to your preference.
