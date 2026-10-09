Here's a cleaned-up version. The mountain, gradient, route line, and wordmark layout are unchanged.

```svg
<svg viewBox="0 0 340 120" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="t">
  <title id="t">Boulderline – Indoor Climbing &amp; Training</title>
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#ff5a36"/>
      <stop offset="1" stop-color="#ffd23f"/>
    </linearGradient>
    <filter id="s" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="2" dy="2" stdDeviation="2" flood-color="#000" flood-opacity=".35"/>
    </filter>
  </defs>

  <path d="M10 100 L45 30 L65 62 L82 40 L112 100 Z"
        fill="url(#g)" stroke="#222" stroke-width="1.5" stroke-linejoin="round" filter="url(#s)"/>
  <path d="M25 100 L45 58 L58 80"
        fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="45" cy="30" r="4" fill="#ff5a36" stroke="#222" stroke-width="1.5"/>

  <text x="128" y="72" font-family="Papyrus, 'Trebuchet MS', sans-serif"
        font-size="34" fill="#222" letter-spacing="1">Boulderline</text>
  <text x="128" y="96" font-family="Arial, Helvetica, sans-serif"
        font-size="8" fill="#666" letter-spacing="1.5">INDOOR CLIMBING &amp; TRAINING</text>
</svg>
```

**What I changed**
- **Canvas:** The viewBox is now 340 wide instead of 320. At 34px, "Boulderline" ran right up to the edge and could clip, especially in Papyrus.
- **Shadow:** The filter region is set explicitly so the shadow can't get cut off. I also softened it from 50% to 35% opacity, and it's slightly tighter.
- **Outline:** The 1px stroke is now 1.5px with rounded joins, so it holds up at small sizes.
- **Route line:** It went from 1px to 2px with round caps and joins. At 1px, the white line on the orange fill nearly vanished.
- **Peak hold:** The circle was the same color as the gradient's start, so it blended into the mountain. It now has the same dark outline.
- **Alignment:** The tagline was at x=130 and the wordmark at x=128. Both are now at 128.
- **Tagline:** The gray went from `#888` to `#666` for better contrast on white. I added a little letter-spacing so the caps read more cleanly.
- **Fonts:** Papyrus is kept, but the fallback is now `Trebuchet MS, sans-serif` instead of `fantasy`, which renders unpredictably. Arial also has a Helvetica/sans-serif fallback.
- **Accessibility:** I added a `<title>` and `role="img"`.

Papyrus isn't installed everywhere, such as on many Android devices and Linux machines. If the logo needs to look identical everywhere, convert the text to outlines before exporting. I can do that if you send the font file.
