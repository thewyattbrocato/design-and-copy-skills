Here's a revised stylesheet. I kept your structure and class names, so it should drop in. The changes are mostly about hierarchy, rhythm, and a few details that make text look typeset.

```css
.essay {
  font-family: Charter, 'Iowan Old Style', 'Palatino Linotype', Georgia, serif;
  font-size: 1.1875rem;
  line-height: 1.7;
  max-width: 38rem;
  margin: 0 auto;
  padding: 0 1.25rem;
  color: #1f1d1a;
  font-kerning: normal;
  font-variant-ligatures: common-ligatures;
  text-rendering: optimizeLegibility;
  hanging-punctuation: first;
  -webkit-font-smoothing: antialiased;
}

.essay h1 {
  font-size: clamp(2.25rem, 6vw, 3.5rem);
  font-weight: 700;
  line-height: 1.08;
  letter-spacing: -0.02em;
  margin: 0 0 0.4em;
  text-wrap: balance;
}

.essay h2 {
  font-size: 1.6rem;
  font-weight: 700;
  line-height: 1.2;
  letter-spacing: -0.01em;
  margin: 2.4em 0 0.5em;
  text-wrap: balance;
}

.essay p {
  margin: 0 0 1.1em;
  text-wrap: pretty;
  hyphens: auto;
}

/* Dropped-cap opening paragraph */
.essay h1 + p::first-letter,
.essay .kicker + h1 + p::first-letter {
  float: left;
  font-size: 4.2em;
  line-height: 0.8;
  font-weight: 700;
  padding: 0.08em 0.1em 0 0;
}

.essay .kicker {
  font: 600 0.75rem/1 system-ui, -apple-system, 'Helvetica Neue', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  color: #9a3b2e;
  margin-bottom: 1.25rem;
}

.essay blockquote {
  margin: 2em 0;
  padding: 0 0 0 1.5rem;
  border-left: 2px solid #9a3b2e;
  font-size: 1.25em;
  line-height: 1.5;
  font-style: italic;
  color: #3a3631;
  text-wrap: balance;
}
.essay blockquote p { margin: 0; }

.essay .stat {
  font-variant-numeric: tabular-nums lining-nums;
}

.essay a {
  color: inherit;
  text-decoration-thickness: 0.06em;
  text-underline-offset: 0.18em;
  text-decoration-color: #9a3b2e;
}

.essay ::selection { background: #f1d9d3; }
```

**What changed and why**
- **Typeface:** Charter and Iowan Old Style ship with macOS and iOS and read as more book-like than Georgia. Georgia stays as the fallback, so nothing breaks elsewhere.
- **Headlines:** They're larger, with tighter tracking and line height. `text-wrap: balance` avoids orphaned last words. This is the biggest contributor to the editorial feel.
- **Kicker:** I gave it wider tracking and a single accent color (`#9a3b2e`, a brick red). The same color shows up in the blockquote rule and link underlines, so the page has one accent.
- **Blockquote:** It's now a larger pull-quote with a thinner rule, instead of a gray bar.
- **Body text:** Slightly larger and warmer than pure `#222`. `text-wrap: pretty` and `hyphens: auto` smooth the rag. This assumes `<html lang="en">` is set, since hyphenation needs it.
- **Drop cap:** It applies to the first paragraph after the `h1`, or after the `h1` when a kicker precedes it. If your markup puts a byline or dek between them, adjust that selector or delete the block. Drop caps can look off in some fonts, so check it on a real essay.

The accent color is my guess. Swap in your brand color if you have one. If you'd like to push further, I could add a subhead/dek style, a byline row, or figure captions.
