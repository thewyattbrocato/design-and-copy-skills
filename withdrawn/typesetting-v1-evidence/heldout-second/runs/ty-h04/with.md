I kept your selectors and made small changes. The size, measure (about 60 to 65 characters) and leading were already sound.

```css
.essay {
  font-family: Georgia, 'Times New Roman', serif;
  font-size: 1.125rem;
  line-height: 1.65;
  max-width: 36rem;
  margin: 0 auto;
  padding: 0 1.25rem;
  color: #222;
  font-synthesis: none;
  text-rendering: optimizeLegibility;
}
.essay h1 {
  font-size: clamp(2rem, 5vw, 2.75rem);
  line-height: 1.15;
  letter-spacing: -0.015em;
  text-wrap: balance;
  margin: 0 0 0.5em;
}
.essay h2 {
  font-size: 1.5rem;
  line-height: 1.25;
  letter-spacing: -0.01em;
  text-wrap: balance;
  margin: 2.2em 0 0.6em;
}
.essay p {
  margin: 0 0 1em;
  text-wrap: pretty;
}
.essay .kicker {
  font: 600 0.75rem/1 system-ui, sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #666;
  margin-bottom: 1rem;
}
.essay blockquote {
  margin: 1.75em 0 1.75em 1.25rem;
  font-size: 1.25rem;
  line-height: 1.5;
  font-style: italic;
}
.essay .stat { font-variant-numeric: lining-nums tabular-nums; }
```

What changed and why:
- **Headings:** Slightly tighter tracking gives the large type a more set, editorial look. `text-wrap: balance` stops one-word last lines. Paragraphs get `text-wrap: pretty` for the same reason.
- **Blockquote:** It had a border, an indent and italics. I dropped the gray bar and kept the italics and indent, and made the quote slightly larger. This is the biggest visible change. If your partner likes the rule, put the `border-left` back and remove the italics instead.
- **Kicker:** I gave it a muted gray (`#666`) so it recedes from the headline.
- **Figures:** Georgia's default numerals are old-style, which look uneven in a stat. `lining-nums` fixes that, and `font-synthesis: none` prevents faux bold or italic.

I assumed a light background and a screen-only page. Nothing here depends on a webfont. A real editorial serif such as Source Serif or Newsreader would change the feel more than any CSS tweak.
