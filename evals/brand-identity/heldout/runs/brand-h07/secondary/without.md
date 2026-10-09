Here's the cleaned-up version with the same design:

```svg
<svg viewBox="0 0 340 120" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title">
  <title id="title">Boulderline: indoor climbing and training</title>
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#ff5a36"/>
      <stop offset="1" stop-color="#ffd23f"/>
    </linearGradient>
    <filter id="s">
      <feDropShadow dx="3" dy="3" stdDeviation="2" flood-color="#000" flood-opacity=".5"/>
    </filter>
  </defs>
  <path d="M10 100 L45 30 L65 62 L82 40 L112 100 Z" fill="url(#g)" stroke="#222" stroke-width="1" filter="url(#s)"/>
  <path d="M25 100 L45 58 L58 80" fill="none" stroke="#fff" stroke-width="1"/>
  <circle cx="45" cy="30" r="4" fill="#ff5a36"/>
  <text x="128" y="72" font-family="Papyrus, fantasy" font-size="34" fill="#222" letter-spacing="1">Boulderline</text>
  <text x="128" y="96" font-family="Arial, sans-serif" font-size="8" fill="#888">INDOOR CLIMBING &amp; TRAINING</text>
</svg>
```

**What changed:**
- **Widened the viewBox from 320 to 340.** "Boulderline" at 34px is probably wider than the 192px left after x=128, so the final letters may be clipped. This is an estimate, so check it in a browser. If it still clips, reduce the font size to about 30 instead.
- **Aligned the tagline with the wordmark.** It was at x=130 and the title at x=128. Both are now at 128.
- **Added a `<title>` and `role="img"`** so screen readers and hover tooltips identify the logo.
- **Added `, sans-serif` to the Arial fallback** and reformatted the defs and stops onto separate lines for readability.

**Left alone:** the mountain, the gradient, the shadow, the highlight line, and the peak circle. The font is still the weak point. Papyrus is only on some Macs, so Windows and most phones will fall back to a generic font and the wordmark will look different. For a final logo file, convert the text to outlines in Illustrator or Figma (or use Inkscape's Path > Object to Path) so it renders the same everywhere.
