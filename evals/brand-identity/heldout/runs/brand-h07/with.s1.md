Here's the cleaned version. The shapes, route line, summit hold, wordmark and layout are all unchanged.

```svg
<svg viewBox="0 0 320 120" xmlns="http://www.w3.org/2000/svg" role="img">
  <title>Boulderline – Indoor Climbing &amp; Training</title>
  <!-- Fonts: Papyrus is not embedded; outline the text before print or sign use. -->
  <path d="M10 100 L45 30 L65 62 L82 40 L112 100 Z" fill="#ff5a36"/>
  <path d="M25 100 L45 58 L58 80" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="45" cy="30" r="4" fill="#222"/>
  <text x="128" y="72" font-family="Papyrus, fantasy" font-size="34" fill="#222" letter-spacing="1">Boulderline</text>
  <text x="130" y="96" font-family="Arial, Helvetica, sans-serif" font-size="9" fill="#555" letter-spacing="1.2">INDOOR CLIMBING &amp; TRAINING</text>
</svg>
```

**What changed**
- **Gradient removed:** the mountain is now flat `#ff5a36`, the orange from your gradient's start. A flat fill holds up in one color, on a dark ground and at small sizes.
- **Drop shadow and outline removed:** both are effects. The 1px stroke would also vanish at small sizes.
- **Route line:** it's now 3px with round caps and joins. At 1px it would disappear on a sign or in a favicon.
- **Summit hold:** it's now `#222`. It was the same orange as the mountain, so it merged into the peak.
- **Tagline:** it's slightly larger (9 instead of 8), darker (`#555` instead of `#888`, which was too faint on white) and tracked wider. The fallback fonts are better too.
- **Accessibility and file hygiene:** I added `role="img"` and a `<title>`, and a comment about the font.

**Left alone, but worth a look**
- **Papyrus:** it's an untouched stock font, it isn't installed on many machines, and it's strongly associated with other brands. Everything else keeps your idea, so I kept it. The wordmark does need outlining before it goes on anything, and I'd test an alternative against it if you're open to that.
- **Missing versions:** you'll want a one-color version, a reversed version for dark backgrounds, and a symbol-only icon. For the icon, I'd draw the peak and route large and leave out the text. I can make those next if you'd like.
