Here's a revised version. The main moves are a slightly larger, tighter text column, more contrast in headings, a heavier pull quote, and a drop cap.

```css
.essay {
  font-family: Georgia, 'Times New Roman', serif;
  font-size: 1.1875rem;
  line-height: 1.6;
  max-width: 34rem;
  margin: 0 auto;
  padding: 0 1.25rem;
  color: #1a1a1a;
  font-kerning: normal;
  font-variant-ligatures: common-ligatures;
  text-rendering: optimizeLegibility;
  hyphens: auto;
  -webkit-hyphens: auto;
}
.essay h1 {
  font-size: clamp(2.25rem, 6vw, 3.25rem);
  font-weight: 400;
  line-height: 1.08;
  letter-spacing: -0.02em;
  margin: 0 0 0.6em;
  text-wrap: balance;
}
.essay h2 {
  font-size: 1.625rem;
  font-weight: 700;
  line-height: 1.2;
  letter-spacing: -0.01em;
  margin: 2.4em 0 0.5em;
  text-wrap: balance;
}
.essay p {
  margin: 0 0 1.1em;
  text-wrap: pretty;
}
.essay a {
  color: inherit;
  text-decoration-thickness: 1px;
  text-underline-offset: 0.15em;
}
.essay .kicker {
  font: 600 0.72rem/1 system-ui, sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: #666;
  margin-bottom: 1.25rem;
}
.essay .dropcap::first-letter {
  float: left;
  font-size: 3.6em;
  font-weight: 700;
  line-height: 0.85;
  padding: 0.08em 0.1em 0 0;
}
.essay blockquote {
  margin: 2em 0;
  padding: 0.25em 0 0.25em 1.25rem;
  border-left: 2px solid #1a1a1a;
  font-size: 1.3em;
  font-style: italic;
  line-height: 1.4;
  color: #111;
}
.essay .stat { font-variant-numeric: tabular-nums; }
```

**What changed and why:**

- **Measure and size:** The column is narrower (34rem, about 60–70 characters per line), and the body text is slightly larger. This reads more like a printed page.
- **Headings:** The h1 is lighter and tighter, which is a common editorial move. The h2 is bolder so it stands out from the body.
- **Pull quote:** The grey border is now dark and the text is larger. This is the biggest change in feel.
- **Details:** `text-wrap: balance` and `pretty` reduce orphaned words and uneven headline breaks. `hyphens: auto` needs a `lang` attribute on the `<html>` or essay container to work.
- **Drop cap (optional):** Add `class="dropcap"` to the first paragraph of an essay to use it. I used a class instead of `:first-of-type` so it doesn't hit a kicker or other element by accident.

If you want a bigger change, the biggest lever is the typeface. Georgia is a safe default, but a web font like Newsreader, Source Serif, or Tiempos would feel much more editorial. I can add the `@font-face` or Google Fonts setup if you pick one.
