Here's a more editorial version. The main changes are a slightly larger body size with a looser line height, tighter display headings, paragraphs set with first-line indents instead of gaps, and a drop cap on the opening paragraph.

```css
.essay {
  font-family: Georgia, 'Times New Roman', serif;
  font-size: 1.1875rem;
  line-height: 1.7;
  max-width: 36rem;
  margin: 0 auto;
  padding: 0 1.25rem;
  color: #222;
  font-kerning: normal;
  font-variant-ligatures: common-ligatures;
  text-rendering: optimizeLegibility;
  hyphens: auto;
}
.essay h1 {
  font-size: clamp(2.25rem, 6vw, 3.5rem);
  font-weight: 400;
  line-height: 1.05;
  letter-spacing: -0.02em;
  text-wrap: balance;
  margin: 0 0 0.5em;
}
.essay h2 {
  font-size: 1.625rem;
  font-weight: 400;
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
  text-indent: 1.5em;
}
.essay > p:first-of-type::first-letter {
  float: left;
  font-size: 3.4em;
  line-height: 0.85;
  padding: 0.06em 0.1em 0 0;
}
.essay .kicker {
  font: 600 0.75rem/1 system-ui, sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: #666;
  margin-bottom: 1.5rem;
}
.essay blockquote {
  margin: 2em 0;
  padding-left: 1.25rem;
  border-left: 3px solid #bbb;
  font-size: 1.3em;
  line-height: 1.5;
  font-style: italic;
  color: #444;
  text-wrap: balance;
}
.essay .stat { font-variant-numeric: tabular-nums; }
```

Choices I made that you may want to change:

- **Indents instead of paragraph gaps.** This is the most print-like change. The first paragraph after a heading stays flush, and later paragraphs are indented. If you prefer web-style spacing, set `.essay p + p` to `margin-top: 1em` and remove the indent.
- **Headings are regular weight.** Georgia's bold is heavy, and the lighter headings look more editorial. Use `font-weight: 700` if you want them stronger.
- **Drop cap.** It applies only when the first paragraph is a direct child of `.essay`. If your markup wraps the content in another element, change the selector to match.
- **Hyphenation.** `hyphens: auto` only works if the page's `<html>` tag has a `lang` attribute.
- **Kicker color.** I used a neutral gray. Swap in your brand accent if you have one.

The biggest single upgrade would be replacing Georgia with a webfont such as Newsreader, Source Serif 4, or Literata. Those are free, and they look far more like a publication. That requires loading the font, so I haven't made it part of this change.
