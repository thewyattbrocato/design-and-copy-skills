Here's the cleaned-up version. The mark itself is unchanged.

```svg
<svg viewBox="0 0 360 120" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title">
  <title id="title">Boulderline — Indoor Climbing &amp; Training</title>
  <defs>
    <linearGradient id="mountain-gradient" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#ff5a36"/>
      <stop offset="1" stop-color="#ffd23f"/>
    </linearGradient>
    <filter id="mountain-shadow">
      <feDropShadow dx="3" dy="3" stdDeviation="2" flood-color="#000" flood-opacity=".5"/>
    </filter>
  </defs>
  <path d="M10 100 L45 30 L65 62 L82 40 L112 100 Z" fill="url(#mountain-gradient)" stroke="#222" stroke-width="1" filter="url(#mountain-shadow)"/>
  <path d="M25 100 L45 58 L58 80" fill="none" stroke="#fff" stroke-width="1"/>
  <circle cx="45" cy="30" r="4" fill="#ff5a36"/>
  <text x="128" y="72" font-family="Papyrus, fantasy" font-size="34" fill="#222" letter-spacing="1">Boulderline</text>
  <text x="128" y="96" font-family="Arial, sans-serif" font-size="8" fill="#888" letter-spacing="1.5">INDOOR CLIMBING &amp; TRAINING</text>
</svg>
```

**What changed**

- **Canvas widened to 360 wide (from 320).** The wordmark at 34px in Papyrus is likely around 210–220 units wide, which starts at x=128 and runs past the old 320 edge, so the "e" was probably getting clipped. I estimated this from font metrics and didn't render it, so please check it in a browser.
- **Tagline aligned to the wordmark.** It sat at x=130, two units off from the wordmark's x=128.
- **Tagline letter-spacing added.** The all-caps line is tight at 8px, so 1.5 units of tracking makes it easier to read.
- **Descriptive IDs.** `g` and `s` are now `mountain-gradient` and `mountain-shadow`, which is easier to maintain if you add more marks later.
- **Font fallback.** `Arial` is now `Arial, sans-serif` so there's a generic fallback if Arial is missing.
- **Accessibility.** Added `role="img"` and a `<title>` so screen readers announce the logo.

**Things I left alone that you may want to decide on**

- **Papyrus.** It isn't installed on most Windows and Linux machines, so the wordmark will fall back to whatever "fantasy" maps to, and the spacing will shift. For a logo, the usual fix is to convert the text to outlines (paths) in Illustrator, Figma, or Inkscape so it looks the same everywhere. I can't do that conversion from here.
- **Tagline color.** `#888` on white is about 3.5:1 contrast, which is below the WCAG AA minimum for small text. `#666` would reach about 5.7:1 and still look light. I didn't change it because it's a visual decision.
