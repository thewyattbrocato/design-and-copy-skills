I couldn't render the SVG here, so the width fix below is an estimate. Here's the cleaned version with the design unchanged:

```svg
<svg viewBox="0 0 340 120" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title">
  <title id="title">Boulderline — Indoor Climbing &amp; Training</title>
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
  <text x="130" y="96" font-family="Arial, sans-serif" font-size="8" fill="#888">INDOOR CLIMBING &amp; TRAINING</text>
</svg>
```

Changes:

- **Viewport widened from 320 to 340.** At 34px, "Boulderline" starting at x=128 likely runs past x=320 and gets clipped. The extra width is a guess, so check it in a browser and adjust if needed.
- **Accessibility:** added `role="img"`, `aria-labelledby`, and a `<title>` so screen readers announce the logo.
- **Formatting:** split the gradient and filter onto separate lines. No values changed.
- **Font fallback:** added `sans-serif` to the Arial stack.

Things I left alone that you may want to decide on:

- **Papyrus** is a dated, sometimes-mocked font and is missing on many non-Mac systems, so the fallback to `fantasy` will look different across devices. If the logo should look the same everywhere, convert the wordmark to outlined paths in your design tool.
- **Tagline color `#888` on white** is light for small 8px text. `#666` would be more legible.
