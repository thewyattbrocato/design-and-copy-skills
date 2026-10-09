Here's a cleaned-up version. I kept the mountain, the gradient, the route line, the peak hold and the layout, and changed only the details.

```svg
<svg viewBox="0 0 320 120" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="bl-title">
  <title id="bl-title">Boulderline – Indoor Climbing &amp; Training</title>
  <defs>
    <linearGradient id="bl-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#ff5a36"/>
      <stop offset="1" stop-color="#ffd23f"/>
    </linearGradient>
    <filter id="bl-shadow" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="2" dy="2" stdDeviation="2" flood-color="#000" flood-opacity=".3"/>
    </filter>
  </defs>

  <path d="M10 100 L45 30 L65 62 L82 40 L112 100 Z"
        fill="url(#bl-grad)" stroke="#222" stroke-width="1.5" stroke-linejoin="round"
        filter="url(#bl-shadow)"/>
  <path d="M25 100 L45 58 L58 80"
        fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="45" cy="30" r="4" fill="#ff5a36" stroke="#222" stroke-width="1.5"/>

  <text x="128" y="72" font-family="'Helvetica Neue', Helvetica, Arial, sans-serif"
        font-size="31" font-weight="700" letter-spacing="0.5" fill="#222">Boulderline</text>
  <text x="128" y="100" font-family="'Helvetica Neue', Helvetica, Arial, sans-serif"
        font-size="8" font-weight="600" letter-spacing="1.5" fill="#555">INDOOR CLIMBING &amp; TRAINING</text>
</svg>
```

**What changed**
- **Font:** I swapped Papyrus for a bold system sans-serif. Papyrus is the biggest thing that makes a logo look dated, and it often isn't installed, so the logo would render differently on different machines. If you want something more distinctive, a custom typeface converted to outlines is the next step.
- **Alignment:** The two text lines had left edges at x=128 and x=130, and now both are at 128. The tagline's baseline now sits on the mountain's base line (y=100).
- **Tagline legibility:** The colour goes from `#888` to `#555`, which gives much better contrast. I also added a little letter-spacing and weight so it holds up at 8px.
- **Line work:** The route line goes from 1 to 2 with round caps and joins, so it's visible at small sizes. The outline is slightly thicker with rounded joins, and the peak hold gets a matching outline.
- **Shadow:** It's softer (opacity .5 → .3, offset 3 → 2) and has an explicit filter region, so it can't clip.
- **Housekeeping:** The IDs `g` and `s` are now `bl-grad` and `bl-shadow`, so they won't collide with other SVGs when inlined in a page. I also added a `<title>` and `role="img"` for accessibility.

I haven't rendered it. The wordmark is sized to fit the 320-wide viewBox with a little room to spare, but check it in your usual browser or design tool. If the font lands wider than expected, drop `font-size` to 30.
