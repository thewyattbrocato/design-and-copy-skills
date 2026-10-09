Here's the cleaned-up version. The mountain, route line, summit hold and two-line lockup are all still there.

```svg
<svg viewBox="0 0 320 120" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="t">
  <title id="t">Boulderline – Indoor Climbing &amp; Training</title>
  <!-- Fonts: Papyrus (wordmark), Arial (tagline). Outline both before print or sign use. -->
  <path d="M10 100 L45 30 L65 62 L82 40 L112 100 Z" fill="#ff5a36" stroke-linejoin="round"/>
  <path d="M25 100 L45 58 L58 80" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="45" cy="30" r="4" fill="#222"/>
  <text x="128" y="72" font-family="Papyrus, fantasy" font-size="34" fill="#222" letter-spacing="1">Boulderline</text>
  <text x="128" y="96" font-family="Arial, sans-serif" font-size="9" fill="#555" letter-spacing=".5">INDOOR CLIMBING &amp; TRAINING</text>
</svg>
```

**What I changed**
- **Gradient and drop shadow:** I removed both and made the mountain flat `#ff5a36`, the start of your gradient. A flat shape survives one-color printing, embroidery, favicons and dark backgrounds. The yellow end of the gradient is gone. It would work well as an accent color elsewhere.
- **Outline stroke:** I removed the 1px dark outline. It would disappear at small sizes.
- **Route line:** I thickened it from 1 to 3 and rounded the ends and joins. A 1px white line vanishes when the logo is small.
- **Summit hold:** It was the same color as the mountain, so you couldn't see it. It's now dark `#222`, so it reads as a hold.
- **Alignment:** The tagline started 2px right of the wordmark (130 vs 128). Both now start at 128.
- **Tagline legibility:** I changed it from `#888` at 8px to `#555` at 9px, with slight letter-spacing. The old gray was too faint on white.
- **SVG basics:** I added `role="img"` and a `<title>`, so the logo has an accessible name. I added fallback fonts and noted the font dependency in a comment.

**What I left alone, and why**
- **Papyrus:** It's a stock font that's heavily associated with spa and fantasy branding, and it's the weakest part of the logo. I left it because you asked me not to redo the logo. Changing it is the single biggest upgrade, so tell me if you want a sturdier face with one custom touch, such as a cut that echoes the route line.
- **Text outlines:** I can't convert text to outlines without the font file. Until that's done, the logo depends on the viewer having Papyrus installed.
- **Tagline:** It sits in the same file, but treat it as an optional line that you can drop for small uses.

Next, I can make a one-color version using `currentColor`, a reversed version for dark backgrounds, and a symbol-only icon with a heavier shape for 16 and 32px. Want those?
