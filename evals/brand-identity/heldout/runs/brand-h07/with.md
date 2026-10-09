I couldn't save files here because the Write tool is disabled, so the cleaned SVGs are below to paste in.

**Full color**
```svg
<svg viewBox="0 0 320 120" xmlns="http://www.w3.org/2000/svg" role="img">
  <title>Boulderline – Indoor Climbing &amp; Training</title>
  <!-- Live text: Papyrus (fallback fantasy) and Arial. Outline both before print or sign use. -->
  <g id="symbol">
    <path d="M10 100 L45 30 L65 62 L82 40 L112 100 Z" fill="#ff5a36"/>
    <path d="M25 100 L45 58 L58 80" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
  <text x="128" y="72" font-family="Papyrus, fantasy" font-size="34" fill="#222" letter-spacing="1">Boulderline</text>
  <text x="130" y="96" font-family="Arial, sans-serif" font-size="9" fill="#666" letter-spacing=".5">INDOOR CLIMBING &amp; TRAINING</text>
</svg>
```

**One color** (follows the CSS text color, so it works on dark backgrounds)
```svg
<svg viewBox="0 0 320 120" xmlns="http://www.w3.org/2000/svg" role="img" fill="currentColor">
  <title>Boulderline – Indoor Climbing &amp; Training</title>
  <defs>
    <mask id="cut">
      <rect width="320" height="120" fill="#fff"/>
      <path d="M25 100 L45 58 L58 80" fill="none" stroke="#000" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
    </mask>
  </defs>
  <path d="M10 100 L45 30 L65 62 L82 40 L112 100 Z" mask="url(#cut)"/>
  <text x="128" y="72" font-family="Papyrus, fantasy" font-size="34" letter-spacing="1">Boulderline</text>
  <text x="130" y="96" font-family="Arial, sans-serif" font-size="9" letter-spacing=".5">INDOOR CLIMBING &amp; TRAINING</text>
</svg>
```

I kept the mountain shape, the wordmark, its position and the orange.

**What I changed**
- **Gradient:** I flattened it to solid `#ff5a36`. Gradients turn to mud in one color and on embroidery or signs.
- **Drop shadow:** I removed the filter. It blurs at small sizes and prints badly.
- **Outline:** I removed the 1px dark stroke on the mountain.
- **Peak dot:** I deleted it. It was the same orange as the mountain, so it was invisible.
- **Route line:** I thickened the white inner line from 1 to 3 and rounded the ends. At 1 it disappears when the logo is small.
- **Tagline:** I raised it from 8 to 9 and darkened it from `#888` to `#666` for contrast. It stays a separate line, so you can drop it in small uses.
- **Accessibility:** I added a `<title>` and `role="img"`.
- **Structure:** I grouped the symbol, added `sans-serif` as an Arial fallback, and added the one-color version.

**Not changed, but worth a look**
- **Papyrus:** It's an untouched stock font, and it's closely tied to a cliché look. It also isn't installed on many machines, so the logo will fall back to a generic fantasy font for those viewers. I left it because you didn't ask for a type change. At minimum, convert the text to outlines before you send the logo to a printer or sign maker. I can swap in a sturdier face if you want to see one.
- **Small sizes:** For a favicon or social avatar, use the mountain alone, not the full logo shrunk down. I can draw that version if you want it.
