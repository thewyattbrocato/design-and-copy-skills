Here's the cleaned-up version. The mountain, gradient, highlight, and layout stay the same.

```svg
<svg viewBox="0 0 350 120" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title">
  <title id="title">Boulderline - Indoor Climbing &amp; Training</title>
  <defs>
    <linearGradient id="peak-gradient" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#ff5a36"/>
      <stop offset="1" stop-color="#ffd23f"/>
    </linearGradient>
    <filter id="peak-shadow" x="-20%" y="-20%" width="150%" height="150%">
      <feDropShadow dx="3" dy="3" stdDeviation="2" flood-color="#000" flood-opacity=".5"/>
    </filter>
  </defs>
  <path d="M10 100 L45 30 L65 62 L82 40 L112 100 Z" fill="url(#peak-gradient)" stroke="#222" stroke-width="1" filter="url(#peak-shadow)"/>
  <path d="M25 100 L45 58 L58 80" fill="none" stroke="#fff" stroke-width="1"/>
  <circle cx="45" cy="30" r="4" fill="#ff5a36"/>
  <text x="128" y="72" font-family="Papyrus, fantasy" font-size="34" fill="#222" letter-spacing="1">Boulderline</text>
  <text x="128" y="96" font-family="Arial, sans-serif" font-size="8" fill="#888">INDOOR CLIMBING &amp; TRAINING</text>
</svg>
```

**What changed:**

- **Wordmark no longer clipped.** The viewBox was 320 wide, but "Boulderline" at 34px starting at x=128 likely runs past 320. I widened it to 350. That's estimated from typical font metrics, since I can't render Papyrus here, so check it in a browser.
- **Tagline aligned.** It started at x=130 while the wordmark starts at x=128. Both now use 128.
- **Shadow filter region enlarged.** The default filter region was tight enough that the drop shadow could be clipped at the bottom edge of the peak. The explicit region fixes that.
- **Accessibility.** Added `role="img"` and a `<title>` so screen readers announce the logo.
- **Clearer IDs.** Renamed `g` and `s` to `peak-gradient` and `peak-shadow`. This only matters if other code references those IDs.
- **Font fallback.** Added `, sans-serif` to Arial so there's a fallback if Arial is missing.

**Things I left alone that you may want to decide on:**

- **Papyrus isn't portable.** It ships with macOS and Office but not on most Linux or Android systems, so the wordmark will look different across machines. For a logo file, converting the text to outlines (in Illustrator or Inkscape) makes it render identically everywhere.
- **The tagline is tiny.** At 8 units it'll be hard to read when the logo is shown small. It works at large sizes, but you may want a minimum display size or a bigger font.
