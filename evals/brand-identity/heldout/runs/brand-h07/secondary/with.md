Here's the cleaned SVG. The concept, colors, and layout are unchanged.

```svg
<svg viewBox="0 0 320 120" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title">
  <title id="title">Boulderline: Indoor climbing &amp; training</title>
  <!-- Wordmark uses Papyrus. Outline it before handoff, or the text falls back on machines without it. -->
  <path d="M10 100 L45 30 L65 62 L82 40 L112 100 Z" fill="#ff5a36" stroke="#222" stroke-width="1" stroke-linejoin="round"/>
  <path d="M25 100 L45 58 L58 80" fill="none" stroke="#fff" stroke-width="1"/>
  <circle cx="45" cy="30" r="4" fill="#ff5a36"/>
  <text x="128" y="72" font-family="Papyrus, fantasy" font-size="34" fill="#222" letter-spacing="1">Boulderline</text>
  <text x="128" y="96" font-family="Arial, sans-serif" font-size="8" fill="#888" letter-spacing="0.5">INDOOR CLIMBING &amp; TRAINING</text>
</svg>
```

**What changed**
- Flattened the mountain fill from the gradient to solid `#ff5a36`, the gradient's starting color. The gradient was an effect, not part of the mark.
- Removed the drop-shadow filter. Filters often break when the file is opened in Figma, Illustrator, or Inkscape.
- Added `role="img"` and a `<title>` so the logo has an accessible name.
- Aligned the tagline to the wordmark's left edge (x 130 → 128).
- Added a line-join to the mountain outline so the sharp peak doesn't spike.
- Added generic font fallbacks to the text and a small tracking value on the tagline.

**Things I didn't change, but you should check**
- **Papyrus is the biggest risk.** It ships with macOS but not Windows or most web setups, so the wordmark will fall back to a different font elsewhere. Outline the text in Figma or Illustrator before you use the file anywhere else.
- **I couldn't render the file here**, so I can't confirm that "Boulderline" fits inside the 320-wide viewBox. Papyrus is wide, so check the right edge and widen the viewBox if the "e" is clipped.
- **The tagline is #888 at 8px**, which is light for small print on white. A darker gray such as #666 would read better, but I kept your color.
- **The gradient is gone from the core mark.** If you want it back, I'd suggest keeping it as a separate application version, not the primary logo.

Next, I can make a one-color version that uses `currentColor` for use on photos or single-color print.
