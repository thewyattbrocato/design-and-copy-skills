Here's the cleaned SVG. The mountain, the boulder line, and the wordmark are unchanged.

```svg
<svg viewBox="0 0 340 120" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title">
  <title id="title">Boulderline</title>
  <path d="M10 100 L45 30 L65 62 L82 40 L112 100 Z" fill="#ff5a36" stroke="#222" stroke-width="1"/>
  <path d="M25 100 L45 58 L58 80" fill="none" stroke="#fff" stroke-width="1"/>
  <circle cx="45" cy="30" r="4" fill="#ffd23f"/>
  <text x="128" y="72" font-family="Papyrus, fantasy" font-size="34" fill="#222" letter-spacing="1">Boulderline</text>
  <text x="128" y="96" font-family="Arial, sans-serif" font-size="8" fill="#666">INDOOR CLIMBING &amp; TRAINING</text>
</svg>
```

**What changed**

- **Removed the gradient and drop shadow.** The core mark is now flat. The gradient would have been the mountain's only color, so it became solid `#ff5a36`, the gradient's start color.
- **Recolored the summit dot to `#ffd23f`.** On a solid orange mountain the old orange dot would vanish. The yellow keeps it visible and reuses the gradient's end color.
- **Widened the viewBox to 340.** The 34px wordmark starting at x=128 likely runs past 320. I estimated this without rendering, so check the right edge in a browser.
- **Aligned the tagline to x=128** to match the wordmark's left edge (it was at 130).
- **Darkened the tagline from `#888` to `#666`.** The original gray on white was about 3.5:1 contrast, below the 4.5:1 needed for small text.
- **Added a `role="img"` and `<title>`** for accessibility.

**Not changed, but needs attention**

- **Papyrus is not embedded.** It will render as a fallback on most machines, and it reads as dated. The wordmark should be converted to outlines in Figma or Illustrator before this ships. I couldn't outline it here because I don't have the font file.
- **The white inner line is 1 unit wide.** It will disappear at small sizes. For favicons or app icons, redraw the mountain with a heavier simplified line.

I haven't made a one-color `currentColor` version or a reversed version. Say the word and I'll add them.
