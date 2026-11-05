I cleaned up the SVG without changing the layout or the mountain-and-line concept.

**Full color**

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 370 120" role="img" aria-labelledby="title">
  <title id="title">Boulderline: Indoor climbing and training</title>
  <path d="M10 100 L45 30 L65 62 L82 40 L112 100 Z" fill="#ff5a36"/>
  <path d="M25 100 L45 58 L58 80" fill="none" stroke="#fff" stroke-width="3" stroke-linejoin="round"/>
  <circle cx="45" cy="30" r="4" fill="#222"/>
  <text x="128" y="72" font-family="Arial, Helvetica, sans-serif" font-weight="700" font-size="34" fill="#222" letter-spacing="1">Boulderline</text>
  <text x="130" y="96" font-family="Arial, Helvetica, sans-serif" font-size="8" fill="#666" letter-spacing="1.5">INDOOR CLIMBING &amp; TRAINING</text>
</svg>
```

**One color** (follows the text color, with the route line and summit dot knocked out)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 370 120" role="img" aria-labelledby="title">
  <title id="title">Boulderline: Indoor climbing and training</title>
  <mask id="knock">
    <rect width="370" height="120" fill="#fff"/>
    <path d="M25 100 L45 58 L58 80" fill="none" stroke="#000" stroke-width="3" stroke-linejoin="round"/>
    <circle cx="45" cy="30" r="4" fill="#000"/>
  </mask>
  <path d="M10 100 L45 30 L65 62 L82 40 L112 100 Z" fill="currentColor" mask="url(#knock)"/>
  <text x="128" y="72" font-family="Arial, Helvetica, sans-serif" font-weight="700" font-size="34" fill="currentColor" letter-spacing="1">Boulderline</text>
  <text x="130" y="96" font-family="Arial, Helvetica, sans-serif" font-size="8" fill="currentColor" letter-spacing="1.5">INDOOR CLIMBING &amp; TRAINING</text>
</svg>
```

**What changed**

- **Gradient flattened to #ff5a36.** The gradient and drop shadow were effects, not part of the mark. The yellow #ffd23f was only used in the gradient, so it's gone. If you want it back, add it as a flat accent in a specific application.
- **Dark outline removed from the mountain.** The 1px outline disappears at small sizes and was only there to frame the gradient.
- **Route line thickened from 1 to 3.** A 1px hairline won't survive at small sizes.
- **Summit dot changed from orange to #222.** On the orange peak it was nearly invisible.
- **Wordmark font changed from Papyrus to Arial Bold.** Papyrus isn't installed on Windows or Linux, so those systems fell back to a generic "fantasy" font. This is the one change that alters the look, so tell me if you'd rather keep a display face and I'll pick a substitute.
- **ViewBox widened to 370.** The old 320 cut off the end of "Boulderline." The width is estimated, so check it in a browser.
- **Tagline darkened from #888 to #666.** The lighter gray was hard to read at 8px.
- **Accessible name added** with `role="img"` and a `<title>`.

**Still to do:** The wordmark is still live text, so it will only look right where Arial is installed. Before you send the logo out, convert the text to outlines in Illustrator or Figma (or run the SVG through a font-to-path tool).
