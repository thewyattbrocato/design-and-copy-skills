Here's the cleaned version. It's the same mountain, route line, hold and wordmark, with the same layout.

```svg
<svg viewBox="0 0 320 120" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="t">
  <title id="t">Boulderline – Indoor Climbing &amp; Training</title>
  <!-- Wordmark uses live text: Papyrus. Outline it before print or sending to others. -->
  <path d="M10 100 L45 30 L65 62 L82 40 L112 100 Z" fill="#ff5a36"/>
  <path d="M25 100 L45 58 L58 80" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="45" cy="30" r="4" fill="#ffd23f"/>
  <text x="128" y="72" font-family="Papyrus, fantasy" font-size="34" fill="#222" letter-spacing="1">Boulderline</text>
  <text x="128" y="96" font-family="Arial, sans-serif" font-size="9" fill="#666" letter-spacing="1">INDOOR CLIMBING &amp; TRAINING</text>
</svg>
```

**What I changed**
- **Gradient and drop shadow:** I replaced them with a flat `#ff5a36`. The shadow would turn to mud in one color and on dark grounds, and the gradient wouldn't survive a stamp or embroidery. Your orange and yellow are both still in use.
- **Outline stroke:** I removed the 1px dark stroke on the mountain, which was only there to fight the shadow.
- **Route line:** It's now 3px with round caps, up from a 1px hairline that would vanish at small sizes.
- **Hold:** It was the same orange as the mountain, so it disappeared into the peak. It's now yellow and reads as a hold.
- **Tagline:** I darkened it from `#888` to `#666` for contrast and bumped it from 8 to 9. I also added letter-spacing and aligned its left edge with the wordmark (x=128 for both, where it was 130).
- **Accessibility and scaling:** I added a `<title>` and `role="img"`. The `viewBox` was already correct and the background stays transparent.

**Two things I left alone**
- **Papyrus:** It's an untouched stock font and is widely overused, which makes it the weakest part of the logo. You said not to redo it, so I haven't swapped it. If you ever want one upgrade, I'd start there. Either way, the wordmark needs to be converted to outlines before this file goes to a printer or sign shop.
- **Missing versions:** There's no one-color, reversed or small-size version yet. I can add those, plus a symbol-only icon, if you want them.
