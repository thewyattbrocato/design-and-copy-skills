Here's the cleaned-up version. The mountain, gradient, summit dot, highlight line, and wordmark are unchanged in concept.

```svg
<svg viewBox="0 0 360 120" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title">
  <title id="title">Boulderline — Indoor Climbing &amp; Training</title>
  <defs>
    <linearGradient id="boulderline-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#ff5a36"/>
      <stop offset="1" stop-color="#ffd23f"/>
    </linearGradient>
    <filter id="boulderline-shadow">
      <feDropShadow dx="3" dy="3" stdDeviation="2" flood-color="#000" flood-opacity=".5"/>
    </filter>
  </defs>

  <path d="M10 100 L45 30 L65 62 L82 40 L112 100 Z"
        fill="url(#boulderline-grad)" stroke="#222" stroke-width="1"
        filter="url(#boulderline-shadow)"/>
  <path d="M25 100 L45 58 L58 80" fill="none" stroke="#fff" stroke-width="1"/>
  <circle cx="45" cy="30" r="4" fill="#ff5a36"/>

  <text x="128" y="72" font-family="Papyrus, 'Trebuchet MS', fantasy" font-size="34"
        fill="#222" letter-spacing="1">Boulderline</text>
  <text x="128" y="96" font-family="Arial, Helvetica, sans-serif" font-size="10"
        fill="#666" letter-spacing="0.5">INDOOR CLIMBING &amp; TRAINING</text>
</svg>
```

**What changed**
- **Unique IDs:** `g` and `s` are now `boulderline-grad` and `boulderline-shadow`, so they won't collide with other SVGs when inlined on a page.
- **Viewbox widened to 360:** At 34px, "Boulderline" with letter-spacing is likely wider than the old 320 width and would clip at the right edge. I estimated this without rendering it, so check it in a browser and trim if there's too much room.
- **Subtitle aligned:** It now starts at x=128 to match the wordmark (it was at 130).
- **Subtitle legibility:** Bumped from 8px to 10px and darkened from `#888` to `#666`, which has better contrast on white.
- **Font fallbacks:** Papyrus isn't installed on most machines, so the stack now falls back to Trebuchet MS before the generic `fantasy`.
- **Accessibility:** Added `role="img"` and a `<title>`.

**Still open**
- **Papyrus:** The wordmark will look different on any machine without it. Convert the text to outlines in Illustrator or Figma before using this as the master file. Papyrus also reads as dated, so it's worth a look if you want the wordmark to feel more current.
- **Gradient and drop shadow:** These are effects, so they won't survive one-color printing, embroidery, or small favicon sizes. If you need those versions, I can make a flat, solid-color variant that keeps the same shapes.
