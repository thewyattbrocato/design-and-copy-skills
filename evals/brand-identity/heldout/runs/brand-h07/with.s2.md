Here's the cleaned-up version. The mountain, the route line and the hold dot are all still there.

```svg
<svg viewBox="0 0 320 120" xmlns="http://www.w3.org/2000/svg" role="img">
  <title>Boulderline – Indoor Climbing &amp; Training</title>
  <!-- Fonts: wordmark and tagline are live text. Outline them before print or sign use. -->
  <path d="M10 100 L45 30 L65 62 L82 40 L112 100 Z" fill="#ff5a36" stroke="#222" stroke-width="2" stroke-linejoin="round"/>
  <path d="M25 100 L45 58 L58 80" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="45" cy="30" r="5" fill="#222"/>
  <text x="126" y="70" font-family="'Helvetica Neue', Arial, sans-serif" font-size="30" font-weight="700" fill="#222">Boulderline</text>
  <text x="128" y="92" font-family="'Helvetica Neue', Arial, sans-serif" font-size="9" letter-spacing="1" fill="#555">INDOOR CLIMBING &amp; TRAINING</text>
</svg>
```

What I changed:
- **Shadow:** I removed the drop-shadow filter and its `<defs>`. It turns to mud in one color and on dark backgrounds.
- **Gradient:** I flattened it to your orange, `#ff5a36`. The yellow end is gone, so say if you want it back as a flat second color.
- **Hairlines:** The 1px strokes would vanish at small sizes. The outline is now 2 and the route line 3, with rounded joins and caps.
- **Hold dot:** It was orange on an orange peak, so it was invisible. It's now `#222` and slightly larger.
- **Tagline:** I darkened it from `#888` to `#555` for contrast and nudged it to line up with the wordmark.
- **Accessibility:** I added `role="img"` and a `<title>`.
- **Wordmark font:** I swapped Papyrus for a bold sans (Helvetica Neue, then Arial). This is the one change that goes beyond tidying, because Papyrus isn't installed on many machines and renders differently across systems. It also doesn't match the bold mountain. I'd pick a proper font next and then outline the text. If you want Papyrus back, change `font-family` on that one line.

I haven't tested it solid black, reversed on a dark background, or at 16–32px. If you want, I can make a one-color version using `currentColor`, a reversed version, and a symbol-only icon. The icon would be a heavier mountain drawn for small sizes, not the full logo shrunk.
