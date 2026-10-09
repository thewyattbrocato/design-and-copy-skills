Here's the cleaned-up SVG. The mountain, boulder, peak dot, palette, and layout are unchanged.

```svg
<svg viewBox="0 0 360 120" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title">
  <title id="title">Boulderline</title>
  <path d="M10 100 L45 30 L65 62 L82 40 L112 100 Z" fill="#ff5a36" stroke="#222" stroke-width="1"/>
  <path d="M25 100 L45 58 L58 80" fill="none" stroke="#fff" stroke-width="1"/>
  <circle cx="45" cy="30" r="4" fill="#ffd23f"/>
  <!-- Wordmark uses Papyrus; outline the text before print or export -->
  <text x="128" y="72" font-family="Papyrus, fantasy" font-size="34" fill="#222" letter-spacing="1">Boulderline</text>
  <g id="tagline">
    <text x="130" y="96" font-family="Arial, sans-serif" font-size="8" fill="#888">INDOOR CLIMBING &amp; TRAINING</text>
  </g>
</svg>
```

What changed:

- **Gradient flattened to solid `#ff5a36`.** Flat fills are the rule for the core mark, and the gradient was the only thing making the mountain different from the dot. Because of that, I moved the peak dot to `#ffd23f`, the gradient's other stop. Without this change the dot disappears into the mountain.
- **Drop-shadow filter removed.** It's an effect, not part of the mark, and it doesn't reproduce in one-color or print.
- **`viewBox` widened from 320 to 360.** Papyrus at 34px is wide, and I estimate "Boulderline" runs past x=320. I can't measure the font here, so please check the right edge in your browser.
- **Accessibility added.** `role="img"` and a `<title>` so screen readers get the name.
- **Tagline grouped** in `<g id="tagline">` so you can delete it for a tagline-free file.

Still open:

- **Papyrus isn't outlined.** Converting to outlines needs the font file, which I don't have. Do that in Illustrator/Figma before this goes on signage or print. If Papyrus has to be replaced, that's a bigger conversation than cleanup.
- **The tagline sits inside the file.** The usual practice is to keep it out of the mark. Use the `#tagline` group as the optional line.
- **The white crease and the `#222` outline are hairlines.** They'll disappear at small sizes, so the favicon and app icon will need a simpler, heavier version.
- **No one-color version yet.** I can add a `currentColor` version next if you want it.
