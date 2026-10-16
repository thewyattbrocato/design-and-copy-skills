I couldn't save the file because the Write tool is disabled in this session, so the cleaned SVG is below. I haven't rendered it. The wordmark width is my estimate and needs a quick look.

```svg
<svg viewBox="0 0 320 120" xmlns="http://www.w3.org/2000/svg" role="img">
  <title>Boulderline: indoor climbing &amp; training</title>
  <!-- Wordmark is live text; outline it before print or sign use. -->
  <g id="symbol">
    <path d="M10 100 L45 30 L65 62 L82 40 L112 100 Z" fill="#ff5a36" stroke="#ff5a36" stroke-width="2" stroke-linejoin="round"/>
    <path d="M25 100 L45 58 L58 80" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
    <circle cx="45" cy="30" r="4" fill="#222"/>
  </g>
  <text x="128" y="72" font-family="'Arial Black', 'Helvetica Neue', Arial, sans-serif" font-weight="700" font-size="28" fill="#222">Boulderline</text>
  <text x="128" y="94" font-family="Arial, Helvetica, sans-serif" font-size="8" fill="#666" letter-spacing=".8">INDOOR CLIMBING &amp; TRAINING</text>
</svg>
```

I kept your mountain silhouette, the white route line, the summit hold and the horizontal layout. Here is what changed:

- **Gradient and drop shadow:** I removed both. The mark is now flat `#ff5a36`, so it holds up in one color, on dark backgrounds and at small sizes.
- **Outline:** I swapped the 1px dark outline for a 2px outline in the fill color with rounded joins. This softens the corners slightly.
- **Route line:** It went from 1px to 3px with round caps, because a hairline disappears small. The route is the best part of the idea, so I made it more visible.
- **Summit circle:** It was the same color as the fill, so it did nothing. It's now dark `#222` and reads as the finishing hold.
- **Alignment:** The tagline sat 2px off the wordmark (x=130 against x=128). I aligned both to x=128 and moved the tagline up a little.
- **Tagline:** It's now `#666` instead of `#888`, which is easier to read, and has slight letter-spacing. It stays a separate text element, not part of the symbol.
- **Structure:** I added `role="img"`, a `<title>` and a `<g id="symbol">` so the symbol can be exported alone for avatars and favicons.

**Decision for you:** I replaced Papyrus with a bold sans-serif. Papyrus is a stock font that falls back unpredictably (`fantasy`) and looks different on every machine. It's also the part of the logo most likely to date it. This is the one change that alters the look, and it's easy to revert by restoring your original `font-family` and size on that line. If you'd rather keep Papyrus, I'd still outline the text before it goes on anything printed.

**Next steps:** To finish the set, I'd add a one-color version using `currentColor`, a reversed version for dark backgrounds, and a symbol-only favicon redrawn for 16 and 32px. I can do those if you want them.
