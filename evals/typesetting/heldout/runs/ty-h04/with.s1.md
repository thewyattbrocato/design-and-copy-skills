Your stylesheet was already sound: the line length is about 65 characters, the body is in rem, and the heading sizes are sensible. So I changed only what makes it look plain. Here is the updated CSS:

```css
.essay {
  font-family: Georgia, 'Times New Roman', serif;
  font-size: 1.125rem;
  line-height: 1.6;
  max-width: 36rem;
  margin: 0 auto;
  padding: 0 1.25rem;
  color: #222;
  font-synthesis: none;
  text-rendering: optimizeLegibility;
}
.essay h1 {
  font-size: clamp(2rem, 5vw, 2.75rem);
  line-height: 1.1;
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
  letter-spacing: 0.1em;
  color: #6b6b6b;
  margin-bottom: 1rem;
}
.essay blockquote {
  margin: 1.75em 0;
  font-size: 1.25rem;
  line-height: 1.5;
  font-style: italic;
}
.essay .stat { font-variant-numeric: lining-nums tabular-nums; }
```

What changed and why:
- **Headings:** Slight negative tracking and `text-wrap: balance` make large Georgia look set rather than default, and they stop one-word last lines. The h1 leading drops from 1.15 to 1.1.
- **Paragraphs:** `text-wrap: pretty` avoids stranded last words. Body leading goes from 1.65 to 1.6, which is tighter and more book-like at 18px.
- **Kicker:** A slightly wider tracking and a softer gray, `#6b6b6b` (about 5:1 contrast on white), make it a quiet label above the headline.
- **Blockquote:** It used an italic, an indent and a rule, which is three devices doing one job. I kept the italic, made it a step larger, and removed the rule and indent. If your partner likes the rule, keep it and drop the italic instead.
- **Figures:** Georgia's default numerals are old-style, which would make `.stat` columns bounce. `lining-nums` fixes that, and the numerals in prose stay old-style, which suits editorial text.

I assumed this is for screen reading on a light background and that you want to keep Georgia. If you want a bigger shift, such as a display face for headings, that's a typeface choice. I left it out because it's a separate decision.
