Here's the cleaned SVG. The mark, gradient, shadow, and colors are unchanged.

```svg
<svg viewBox="0 0 340 120" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="bl-title">
  <title id="bl-title">Boulderline: Indoor Climbing &amp; Training</title>
  <defs>
    <linearGradient id="bl-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#ff5a36"/>
      <stop offset="1" stop-color="#ffd23f"/>
    </linearGradient>
    <filter id="bl-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="3" dy="3" stdDeviation="2" flood-color="#000" flood-opacity=".5"/>
    </filter>
  </defs>
  <path d="M10 100 L45 30 L65 62 L82 40 L112 100 Z" fill="url(#bl-grad)" stroke="#222" stroke-width="1" stroke-linejoin="round" filter="url(#bl-shadow)"/>
  <path d="M25 100 L45 58 L58 80" fill="none" stroke="#fff" stroke-width="1"/>
  <circle cx="45" cy="30" r="4" fill="#ff5a36"/>
  <text x="128" y="72" font-family="Papyrus, fantasy" font-size="34" fill="#222" letter-spacing="1">Boulderline</text>
  <text x="130" y="96" font-family="Arial, sans-serif" font-size="8" fill="#888">INDOOR CLIMBING &amp; TRAINING</text>
</svg>
```

Changes:
- **viewBox widened to 340** (from 320). "Boulderline" at 34px likely runs past x=320, so the end of the word may have been clipped. I estimated the width without rendering it, so please check this in a browser.
- **Filter region set explicitly.** The default region could clip the drop shadow at the bottom-right edge.
- **Gradient and filter IDs renamed** to `bl-grad` and `bl-shadow`, so they won't collide if the logo is inlined next to another SVG with `g` or `s`.
- **Accessible name added** with `role="img"` and a `<title>`.
- **Font fallback** set to `Arial, sans-serif`.
- **Path join smoothed** with `stroke-linejoin="round"` so the mountain's sharp peaks don't spike past the stroke.

Not done, and why:
- **Text is still live.** Converting "Boulderline" to outlines needs the Papyrus font file, which I don't have here. Papyrus ships with macOS and Microsoft Office but not with most other systems, so on Windows or Linux browsers the wordmark will fall back to a generic fantasy font. Outlining it in Illustrator or Figma would fix that.
- **The summit circle is almost invisible.** Its color `#ff5a36` matches the gradient's start color, which sits right at the peak. If you want it to read, give it a different color or remove it.
