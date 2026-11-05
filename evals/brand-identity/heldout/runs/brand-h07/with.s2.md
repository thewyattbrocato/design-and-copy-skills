I couldn't save the files because the Write tool is disabled in this session, so the cleaned SVG is below. I haven't rendered it or tested it at small sizes.

```svg
<svg viewBox="0 0 320 120" xmlns="http://www.w3.org/2000/svg" role="img">
  <title>Boulderline – Indoor Climbing &amp; Training</title>
  <!-- Fonts: Papyrus (wordmark), Arial (tagline). Convert text to outlines before print or sending to third parties. -->
  <g id="symbol">
    <path d="M10 100 L45 30 L65 62 L82 40 L112 100 Z" fill="#ff5a36"/>
    <path d="M25 100 L45 58 L58 80" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
    <circle cx="45" cy="30" r="5" fill="#222"/>
  </g>
  <text x="128" y="72" font-family="Papyrus, fantasy" font-size="34" fill="#222" letter-spacing="1">Boulderline</text>
  <!-- Optional line: drop for small sizes -->
  <text id="tagline" x="130" y="96" font-family="Arial, sans-serif" font-size="9" fill="#666" letter-spacing="1.2">INDOOR CLIMBING &amp; TRAINING</text>
</svg>
```

**What I changed**
- **Gradient and drop shadow:** I removed both and made the mountain a flat `#ff5a36`. That's the orange you already use, and it now survives one-color printing and tiny sizes.
- **Outline stroke:** I removed the 1px dark outline on the mountain.
- **Route line:** It was a 1px white hairline that would vanish when small. It's now 3px with round caps and joins.
- **Summit hold:** It was the same orange as the mountain, so it disappeared into it. It's now dark `#222` and slightly larger (r=5), so the route reads as ending at a hold.
- **Tagline:** I darkened it from `#888` to `#666`, raised it from 8px to 9px, and added a little tracking so it stays legible. It's now its own optional element, `#tagline`, rather than part of the mark.
- **Structure:** I added `role="img"` and a `<title>`, wrapped the symbol in a group, and added a font fallback to Arial.
- **Left alone:** The mountain geometry, layout, wordmark and the route-up-the-boulder idea.

**Two things I didn't do**
- **Wordmark:** Papyrus is a very recognizable stock font, and it doesn't match the clean, solid mountain. I kept it because you asked me not to redo the logo, but I'd test a heavier, more neutral face. It's the weakest part of the logo.
- **Text outlines:** The text is still live, so the logo depends on Papyrus being installed. I can't convert it to outlines without font tooling, so do that in Illustrator or Inkscape before sending files out.

**Still missing:** one-color, reversed and symbol-only versions, plus a drawn 16–32px icon (the full logo shrunk won't work as a favicon). I can write the one-color version with `currentColor` and a symbol-only file once Write is available.
