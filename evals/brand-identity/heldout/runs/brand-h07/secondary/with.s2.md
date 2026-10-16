Here's the cleaned-up SVG. The geometry, gradient, drop shadow, and wordmark are unchanged.

```svg
<svg viewBox="0 0 330 120" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="bl-title">
  <title id="bl-title">Boulderline, indoor climbing and training</title>
  <defs>
    <linearGradient id="bl-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#ff5a36"/>
      <stop offset="1" stop-color="#ffd23f"/>
    </linearGradient>
    <filter id="bl-shadow">
      <feDropShadow dx="3" dy="3" stdDeviation="2" flood-color="#000" flood-opacity=".5"/>
    </filter>
  </defs>

  <path d="M10 100 L45 30 L65 62 L82 40 L112 100 Z" fill="url(#bl-grad)" stroke="#222" stroke-width="1" filter="url(#bl-shadow)"/>
  <path d="M25 100 L45 58 L58 80" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="45" cy="30" r="4" fill="#ff5a36"/>

  <!-- Wordmark is live text in Papyrus. Outline it in your design tool before sending final files. -->
  <text x="128" y="72" font-family="Papyrus, fantasy" font-size="34" fill="#222" letter-spacing="1">Boulderline</text>
  <text x="128" y="96" font-family="Arial, Helvetica, sans-serif" font-size="9" fill="#666">INDOOR CLIMBING &amp; TRAINING</text>
</svg>
```

Changes:

- **Added a title and role.** The SVG now has an accessible name.
- **Renamed the gradient and filter IDs** to `bl-grad` and `bl-shadow`, so they won't collide if the SVG is inlined on a page.
- **Widened the viewBox from 320 to 330.** The wordmark's right edge was probably clipping. I estimated the width without rendering it, so check it.
- **Aligned the tagline to the wordmark's x-position** (128, previously 130).
- **Darkened the tagline from #888 to #666** for contrast on white, and bumped it from 8 to 9 so it's legible at display sizes.
- **Thickened the white inner line from 1 to 2** and rounded its caps and joins so it survives at small sizes.
- **Added fallback fonts** to the tagline stack.

Two things I left alone:

- **Papyrus.** It isn't installed on most Windows, Linux, and Android machines, so the wordmark will fall back to whatever "fantasy" resolves to. The fix is to outline the text in Illustrator or Figma. I can't do that from the SVG alone without the font file.
- **Gradient and shadow.** You asked to keep them, so they stay in this full-color version. For small sizes, single-color uses, or the favicon, you'll want a flat, one-color variant. I can make that version next if you'd like.
