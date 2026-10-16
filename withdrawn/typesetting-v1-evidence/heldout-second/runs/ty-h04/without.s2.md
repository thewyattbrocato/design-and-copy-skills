Here's a revised stylesheet. I kept your selectors and added a few rules for elements your original didn't cover (links, lists, `hr`, `figcaption`). I haven't seen your markup, so the drop cap and subtitle rules rest on assumptions, noted below.

```css
.essay {
  font-family: Charter, 'Iowan Old Style', 'Palatino Linotype', Palatino, Georgia, serif;
  font-size: clamp(1.0625rem, 1rem + 0.3vw, 1.2rem);
  line-height: 1.6;
  max-width: 34rem;              /* ~65 characters per line */
  margin: 0 auto;
  padding: 0 1.25rem;
  color: #1f1d1b;                /* warm near-black, softer than #222 on white */
  font-kerning: normal;
  font-feature-settings: 'liga', 'onum';   /* old-style figures sit better in running text */
  text-rendering: optimizeLegibility;
  hyphens: auto;
  -webkit-font-smoothing: antialiased;
}

/* Headings */
.essay h1,
.essay h2 {
  text-wrap: balance;
  hyphens: manual;
  font-feature-settings: 'lnum';  /* lining figures in headings */
}
.essay h1 {
  font-size: clamp(2.25rem, 5.5vw, 3.25rem);
  font-weight: 700;
  line-height: 1.08;
  letter-spacing: -0.02em;
  margin: 0 0 0.4em;
}
.essay h2 {
  font-size: 1.5rem;
  font-weight: 700;
  line-height: 1.2;
  letter-spacing: -0.01em;
  margin: 2.5em 0 0.6em;
}

/* Deck / subtitle: assumes a <p class="dek"> after the h1 */
.essay .dek {
  font-size: 1.3em;
  line-height: 1.4;
  font-style: italic;
  color: #5a5651;
  margin: 0 0 1.5em;
  text-wrap: balance;
}

/* Body text */
.essay p {
  margin: 0 0 1em;
  text-wrap: pretty;             /* avoids orphans on the last line */
}

/* Drop cap on the first paragraph following the h1/dek block */
.essay h1 + p::first-letter,
.essay .dek + p::first-letter {
  float: left;
  font-size: 3.6em;
  line-height: 0.82;
  font-weight: 700;
  padding: 0.06em 0.1em 0 0;
}

/* Kicker */
.essay .kicker {
  font: 600 0.75rem/1 system-ui, -apple-system, 'Segoe UI', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  color: #9a3b2e;                /* one restrained accent color */
  margin-bottom: 1.1rem;
}

/* Blockquote as pull quote */
.essay blockquote {
  margin: 2em 0;
  padding: 0 0 0 1.25rem;
  border-left: 2px solid #9a3b2e;
  font-size: 1.15em;
  line-height: 1.5;
  font-style: italic;
  color: #3a3733;
  text-wrap: pretty;
}
.essay blockquote p:last-child { margin-bottom: 0; }
.essay blockquote cite,
.essay blockquote footer {
  display: block;
  margin-top: 0.6em;
  font: normal 600 0.8rem/1.3 system-ui, sans-serif;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #6b665f;
}

/* Links */
.essay a {
  color: inherit;
  text-decoration: underline;
  text-decoration-thickness: 0.06em;
  text-underline-offset: 0.18em;
  text-decoration-color: #9a3b2e;
}
.essay a:hover { text-decoration-thickness: 0.12em; }

/* Lists */
.essay ul,
.essay ol { margin: 0 0 1em; padding-left: 1.4em; }
.essay li { margin-bottom: 0.35em; }

/* Section break */
.essay hr {
  border: 0;
  margin: 2.5em 0;
  text-align: center;
  line-height: 1;
}
.essay hr::after {
  content: '\2766';              /* ❦ */
  color: #9a3b2e;
  font-size: 1.25rem;
}

/* Captions */
.essay figcaption {
  font: 0.8125rem/1.4 system-ui, sans-serif;
  color: #6b665f;
  margin-top: 0.5em;
}

/* Numbers */
.essay .stat {
  font-variant-numeric: lining-nums tabular-nums;
  font-feature-settings: 'lnum', 'tnum';
}

@media (prefers-color-scheme: dark) {
  .essay { color: #e8e4de; }
  .essay .dek,
  .essay blockquote { color: #b9b4ac; }
  .essay .kicker,
  .essay hr::after { color: #e08a7b; }
  .essay blockquote,
  .essay a { border-color: #e08a7b; text-decoration-color: #e08a7b; }
}
```

**What changed and why**
- **Typeface:** Charter and Iowan Old Style ship on macOS, iOS and Windows and read as more bookish than Georgia. Georgia is still the fallback. If your partner wants a stronger editorial feel, a webfont such as Source Serif 4 or Newsreader would help more than anything else here.
- **Hierarchy:** the headline is larger and tighter, with negative tracking. An optional deck line sits beneath it, and the kicker gets a single accent color.
- **Line breaks:** `text-wrap: balance` on headings and `pretty` on paragraphs remove awkward breaks and single-word last lines.
- **Details:** old-style figures in body text and lining figures in headings and stats, an ornamental `hr`, a drop cap, and quieter link underlines.
- **Measure:** `34rem` at the new font size is about 65 characters per line.

**Check these**
- The drop cap and `.dek` assume the essay opens with `h1` followed by an optional `<p class="dek">`, then a paragraph. If your markup differs, adjust or remove that rule. A kicker placed between them wouldn't break it.
- `#9a3b2e` is a placeholder accent. Swap in a brand color if you have one. Check that it has enough contrast on your background.
- I added a dark-mode block. Delete it if your site doesn't support dark mode.

If you share a sample essay's HTML, I can tune the selectors to match it.
