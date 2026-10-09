I couldn't save the file because the Write tool is disabled in this session, so the cleaned SVG is below. I kept the mountain, the route line, the hold at the summit and the lockup layout.

```svg
<svg viewBox="0 0 320 120" xmlns="http://www.w3.org/2000/svg" role="img">
  <title>Boulderline – Indoor Climbing &amp; Training</title>
  <!-- Colors: orange #ff5a36, yellow #ffd23f, ink #222, grey #555 -->
  <path d="M10 100 L45 30 L65 62 L82 40 L112 100 Z" fill="#ff5a36"/>
  <path d="M25 100 L45 58 L58 80" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="45" cy="30" r="5" fill="#ffd23f"/>
  <!-- Live text: needs Papyrus installed; outline before sending to print or sign makers -->
  <text x="128" y="72" font-family="Papyrus, fantasy" font-size="34" fill="#222" letter-spacing="1">Boulderline</text>
  <text x="130" y="96" font-family="Arial, Helvetica, sans-serif" font-size="8" fill="#555">INDOOR CLIMBING &amp; TRAINING</text>
</svg>
```

**What changed**
- **Gradient and drop shadow:** I removed both and used the gradient's start orange (`#ff5a36`) as a flat fill. The mark now holds up in one color, reversed on dark, and at small sizes.
- **Outline:** I dropped the 1px dark stroke. It disappeared at small sizes and added nothing.
- **Route line:** It went from a 1px hairline to 3px with round caps and joins, so it survives at small sizes.
- **Summit hold:** It was the same orange as the mountain, so it just looked like a bump on the peak. It's now yellow (`#ffd23f`, already in your gradient) and slightly bigger (r5), so it reads as a hold.
- **Tagline:** I darkened it from `#888` to `#555`, because the grey was too faint at 8px. The font stack now has proper fallbacks.
- **Accessibility:** I added `role="img"` and a `<title>`, and removed the unused `<defs>`.

**Left alone, but worth a look**
- **Papyrus:** It's a very common stock font, and it only renders where it's installed. Other machines fall back to a generic fantasy font. I didn't swap it because that changes the look you like. Before the logo goes on signs or print, outline the text in a vector editor. Consider a custom tweak to one letter so it's distinctly yours.
- **Tagline:** It sits inside the logo file. It's cleaner as a separate optional line, so you can drop it at small sizes.
- **Other versions:** You'll want a symbol-only mark (mountain, route and hold) for favicons and avatars, plus a one-color `currentColor` version and a reversed one. I can make those next if you'd like.
