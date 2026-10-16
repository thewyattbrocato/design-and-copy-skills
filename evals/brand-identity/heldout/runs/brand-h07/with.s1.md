I couldn't save a file because the Write tool is disabled here, so the cleaned SVG is below for you to paste in.

```svg
<svg viewBox="0 0 320 120" xmlns="http://www.w3.org/2000/svg" role="img">
  <title>Boulderline – Indoor Climbing &amp; Training</title>
  <!-- Symbol -->
  <g id="symbol">
    <path d="M10 100 L45 30 L65 62 L82 40 L112 100 Z" fill="#ff5a36"/>
    <circle cx="45" cy="30" r="4" fill="#ff5a36"/>
    <path d="M25 100 L45 58 L58 80" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
  <!-- Wordmark. Live text: needs Papyrus installed; outline before print/web use. -->
  <text id="wordmark" x="128" y="72" font-family="Papyrus, fantasy" font-size="34" fill="#222" letter-spacing="1">Boulderline</text>
  <!-- Tagline: separate optional line -->
  <text id="tagline" x="130" y="96" font-family="Arial, Helvetica, sans-serif" font-size="9" fill="#595959" letter-spacing=".6">INDOOR CLIMBING &amp; TRAINING</text>
</svg>
```

The peak, the route line, the summit dot, the layout and the orange are all unchanged. What I changed:

- **Drop shadow:** I removed the filter. It would turn to mud in one color and on dark backgrounds, and it was clipped by the default filter region anyway.
- **Gradient:** I flattened it to your lead orange, `#ff5a36`. A gradient is hard to reproduce on a sign, a stamp or an embroidered patch.
- **Mountain outline:** I removed the 1px `#222` stroke. It was a hairline that would disappear at small sizes.
- **Route line:** I changed it from a 1px hairline to 3px with round caps and joins. The hairline was the weakest part of the mark, and now it should still read small.
- **Tagline:** I raised it from 8px to 9px, darkened it from `#888` to `#595959` (the old gray was too faint on white), added a little letter-spacing and a Helvetica fallback. It is a separate element, so you can drop it from tight spaces.
- **Accessibility:** I added `role="img"` and a `<title>`.
- **Structure:** I grouped and named the symbol, wordmark and tagline so you can export them separately.

Two things I didn't touch because they're design decisions:

- **Papyrus:** It's live text, so anyone without the font sees a fallback. It's also a very common stock font, and its soft, rustic look doesn't match the bold angular symbol. Converting the wordmark to outlines is the minimum fix. I'd suggest trying a sturdier face in the same pass, but that's your call.
- **Summit dot:** It's the same color as the mountain, so it only rounds the peak slightly. If you want it to read as a hold, make it white or dark.

I can add one-color (`currentColor`), reversed and symbol-only versions if you want them.
