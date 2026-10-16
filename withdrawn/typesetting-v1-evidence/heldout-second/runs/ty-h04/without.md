I haven't tested this in a browser. Here's a revised stylesheet. It keeps your structure and class names, so it's a drop-in replacement.

```css
.essay {
  font-family: Charter, 'Iowan Old Style', 'Palatino Linotype', Georgia, serif;
  font-size: 1.15rem;
  line-height: 1.7;
  max-width: 37rem;
  margin: 0 auto;
  padding: 0 1.25rem;
  color: #1f1d1a;                       /* warm near-black, softer than #222 */
  font-kerning: normal;
  font-variant-ligatures: common-ligatures;
  font-variant-numeric: oldstyle-nums;  /* numerals sit inside the text */
  hanging-punctuation: first;
  hyphens: auto;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
}

.essay .kicker {
  font: 600 0.72rem/1 system-ui, sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  color: #8a3b2a;                       /* single accent; change to your brand */
  margin-bottom: 1.25rem;
}

.essay h1 {
  font-size: clamp(2.25rem, 6vw, 3.25rem);
  line-height: 1.08;
  letter-spacing: -0.02em;
  font-weight: 700;
  margin: 0 0 0.4em;
  text-wrap: balance;
}

.essay .dek {                           /* optional standfirst under the title */
  font-size: 1.3rem;
  line-height: 1.4;
  font-style: italic;
  color: #5b5750;
  margin: 0 0 2rem;
  text-wrap: balance;
}

.essay h2 {
  font-size: 1.55rem;
  line-height: 1.2;
  letter-spacing: -0.01em;
  margin: 2.4em 0 0.5em;
  text-wrap: balance;
}

.essay p {
  margin: 0 0 1.1em;
  text-wrap: pretty;                    /* avoids orphans on last lines */
}

/* Drop cap on the opening paragraph */
.essay h1 ~ p:first-of-type::first-letter,
.essay .dek ~ p:first-of-type::first-letter {
  float: left;
  font-size: 4.2em;
  line-height: 0.8;
  padding: 0.08em 0.1em 0 0;
  font-weight: 700;
  color: #8a3b2a;
}

.essay a {
  color: inherit;
  text-decoration-line: underline;
  text-decoration-color: #8a3b2a;
  text-decoration-thickness: 1px;
  text-underline-offset: 0.2em;
}
.essay a:hover { text-decoration-thickness: 2px; }

.essay blockquote {
  margin: 2em 0;
  padding: 0 0 0 1.25rem;
  border-left: 2px solid #8a3b2a;
  font-size: 1.25rem;
  line-height: 1.5;
  font-style: italic;
  color: #3a3733;
}
.essay blockquote p { margin: 0; }
.essay blockquote cite {
  display: block;
  margin-top: 0.75em;
  font: 600 0.75rem/1.3 system-ui, sans-serif;
  font-style: normal;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.essay figcaption {
  font: 0.85rem/1.4 system-ui, sans-serif;
  color: #6b675f;
  margin-top: 0.6rem;
}

.essay hr {                             /* section break as a typographic ornament */
  border: 0;
  text-align: center;
  margin: 2.5em 0;
}
.essay hr::after {
  content: '⁂';
  font-size: 1.25rem;
  letter-spacing: 0.5em;
  color: #8a3b2a;
}

.essay .stat {
  font-variant-numeric: lining-nums tabular-nums;  /* override old-style for data */
}
```

**What changed**
- **Typeface:** Georgia is the main reason the page reads as default. The new stack uses Charter or Iowan Old Style, which ship with macOS, iOS and Android, and falls back to Georgia. For a distinctive look, a webfont such as Source Serif, Newsreader or Fraunces would help more than anything else here.
- **Headlines:** They're larger, with tighter line height and slight negative tracking. `text-wrap: balance` keeps titles from leaving a stray word on the second line.
- **Body text:** It's slightly larger with more leading. Kerning, ligatures, old-style numerals, hyphenation and `text-wrap: pretty` give it a book-like texture.
- **Colour:** One restrained accent (`#8a3b2a`) is used for the kicker, drop cap, links, quote rule and section break. Everything else is warm neutrals. Swap in your brand colour.
- **Blockquotes:** They're larger, with a thinner accent rule, so they work as pull quotes.
- **Added elements:** `.dek`, `figcaption`, `hr` and `blockquote cite` styles. They only apply if your markup uses them, so ignore any you don't need.

**Things to check**
- The drop cap selector assumes the first paragraph follows the `h1` or `.dek` as a sibling. If your markup wraps the title in a header, change the selector. Drop caps also render slightly differently across browsers, so look at it in Safari and Chrome.
- Old-style numerals suit prose. If your essays have a lot of years or figures that look odd to you, remove that one line. `.stat` already forces lining, tabular figures.
- If you want it wider on desktop, `max-width: 37rem` is about 65 characters per line. I'd keep it near that.
