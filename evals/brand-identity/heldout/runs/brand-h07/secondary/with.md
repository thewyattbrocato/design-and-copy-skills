Here's the cleaned-up version. The layout, shapes, colors, and gradient are unchanged.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 344 120" role="img" aria-labelledby="title">
  <title id="title">Boulderline: Indoor climbing &amp; training</title>
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#ff5a36"/>
      <stop offset="1" stop-color="#ffd23f"/>
    </linearGradient>
    <filter id="s" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="3" dy="3" stdDeviation="2" flood-color="#000" flood-opacity=".5"/>
    </filter>
  </defs>
  <path d="M10 100 45 30 65 62 82 40 112 100Z" fill="url(#g)" stroke="#222" stroke-width="1" filter="url(#s)"/>
  <path d="M25 100 45 58 58 80" fill="none" stroke="#fff" stroke-width="1"/>
  <circle cx="45" cy="30" r="4" fill="#ff5a36"/>
  <!-- Live text: outline before shipping, since Papyrus is not installed on most machines -->
  <text x="128" y="72" font-family="Papyrus, fantasy" font-size="34" fill="#222" letter-spacing="1">Boulderline</text>
  <text x="130" y="96" font-family="Arial, sans-serif" font-size="8" fill="#888">INDOOR CLIMBING &amp; TRAINING</text>
</svg>
```

**What changed:**
- Added a `<title>` and `role="img"` so the logo has an accessible name.
- Widened the `viewBox` from 320 to 344. At 34px, the wordmark likely ran past the right edge. I estimated this without rendering it, so check it in a browser.
- Gave the filter an explicit region so the drop shadow can't be clipped.
- Removed the extra whitespace and the redundant commas in the path data, and closed the path with `Z` as before.
- Added a fallback to `sans-serif` on the tagline font.

**Not done, needs your call:**
- **Text outlines:** I can't convert text to paths in this environment. Open the file in Figma, Illustrator, or Inkscape and use "outline text" on both lines. Otherwise the wordmark will show in a fallback font on most computers.
- **Gradient and shadow:** I kept them because you asked. The gradient and drop shadow won't reproduce in one color or on small sizes, so you'll eventually want a flat version alongside this one. I can make a flat, `currentColor` version if you want it.
