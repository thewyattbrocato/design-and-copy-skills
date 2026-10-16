Your stylesheet is mostly sound: Georgia at 1.125rem with 1.65 leading and a ~36rem measure is a good reading setup. The changes below address what makes it read plainer than it needs to.

```css
.essay {
  font-family: Georgia, 'Times New Roman', serif;
  font-size: 1.125rem;
  line-height: 1.65;
  max-width: 36rem;
  margin: 0 auto;
  padding: 0 1.25rem;
  color: #222;
  font-kerning: normal;
  font-synthesis: none;
}
.essay h1 {
  font-size: clamp(2rem, 5vw, 2.75rem);
  line-height: 1.15;
  letter-spacing: -0.01em;
  text-wrap: balance;
  margin: 0 0 0.5em;
}
.essay h2 {
  font-size: 1.5rem;
  line-height: 1.25;
  letter-spacing: -0.005em;
  text-wrap: balance;
  margin: 1.75em 0 0.875em;
}
.essay p {
  margin: 0 0 1em;
  text-wrap: pretty;
}
.essay .kicker {
  font: 600 0.8125rem/1 system-ui, sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-bottom: 1rem;
}
.essay blockquote {
  margin: 1.5em 0;
  padding-left: 1.25rem;
  border-left: 3px solid #bbb;
  color: #444;
}
.essay .stat { font-variant-numeric: tabular-nums; }
```

What changed and why:

- **h2 spacing:** `2.2em 0 0.6em` put about 3.7× as much space above the heading as below it, so headings floated away from their sections. `1.75em 0 0.875em` is about 2× and ties each heading to the text it introduces.
- **Headings:** `text-wrap: balance` avoids a stranded word on a second line, and the slight negative tracking on the h1 suits a larger display size.
- **Paragraphs:** `text-wrap: pretty` prevents single-word last lines without changing the measure.
- **Kicker:** 0.75rem (12px) is at the floor for tracked caps; 0.8125rem gives it a bit more presence without competing with the h1.
- **Blockquote:** It was using italic, a rule and an indent together. I dropped the italic, so the rule and indent carry the quote alone, and set the text to `#444` so it reads as a step back. If you'd rather keep the italic, remove the border and the indent instead.
- **Global:** `font-kerning: normal` and `font-synthesis: none` make sure Georgia's own kerning is used and nothing gets faux-bolded or faux-italicized.
