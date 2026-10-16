**Why it happens**

Browsers don't have your font when they first render, so they have to pick a behavior while it downloads. That's controlled by `font-display`:

- **Invisible headline (FOIT):** With `font-display: block`, or the default `auto` in most browsers, text in that font is hidden for up to about 3 seconds while the file loads. That's your blank headline.
- **Flash of a different font, then a jump (FOUT plus layout shift):** With `swap` (or `fallback`), the browser shows text immediately in a fallback font. When your font arrives, it swaps. The two fonts have different glyph widths, ascent and descent, and line height. Lines re-wrap and everything below shifts. This counts against your CLS score.

Both are symptoms of the same thing: the font arrives late, and the fallback doesn't match it.

**What to do, in order of impact**

1. **Preload the font file.** Put this in `<head>`:
   ```html
   <link rel="preload" href="/fonts/heading.woff2" as="font" type="font/woff2" crossorigin>
   ```
   The `crossorigin` attribute is required even for same-origin fonts. Without it the preload is wasted and the file is fetched twice. Without a preload, the browser doesn't discover the font until it has parsed the CSS and seen text that uses it. That delay is a big part of what you're seeing.

2. **Self-host as WOFF2.** If you're loading from Google Fonts or another third-party host, you pay for an extra DNS, TLS and connection setup. Serving from your own origin or CDN avoids that. Make sure it's WOFF2 and has long-lived cache headers (`Cache-Control: public, max-age=31536000, immutable`, with a hashed filename).

3. **Pick `font-display: swap` or `optional` deliberately:**
   - `swap` makes the text always visible, but the swap can cause a jump. This is the safe default. If you use it, do step 4.
   - `optional` gives the font about 100ms to load. If it misses, the browser uses the fallback for that page view and uses your font on later views once it's cached. There's no jump and no invisible text. With a preload, the font usually makes the window on a fast connection. It's the best choice if brand fidelity on the very first visit is less important than stability.

4. **Match the fallback metrics so the swap doesn't shift anything.** This is the real fix for the jump. Define a tuned fallback face:
   ```css
   @font-face {
     font-family: "Heading Fallback";
     src: local("Arial");
     size-adjust: 104%;
     ascent-override: 92%;
     descent-override: 24%;
     line-gap-override: 0%;
   }
   h1, h2, h3 {
     font-family: "Heading", "Heading Fallback", sans-serif;
   }
   ```
   Don't copy those numbers. They're placeholders. Compute them from your actual font. Tools like Fontaine, Capsize, or the `next/font` and Nuxt font modules generate them automatically. The result is that the fallback occupies the same space as your real font, so the swap changes letter shapes but nothing moves.

5. **Subset the file.** If you only need Latin, subset it (`pyftsubset` or glyphhanger) and use `unicode-range`. A variable font can be large. Also trim axes you don't use. If you only need weights 600 to 800, a limited-range axis is smaller than the full range.

**Things specific to your setup**

- Body text is in the system font, so it never waits on a download. Only headings are affected. That makes this easier, because the metric-matched fallback is needed for one family only.
- A variable font is typically larger than a single static weight. If you use only one or two weights, a static subset can be smaller than the variable file. Check the byte size before assuming variable is better.
- If the headline is the largest element on screen, it's also probably your LCP element. Fixing font loading will improve LCP as well as CLS.

**My recommendation**

Preload, self-host as a subsetted WOFF2, use `font-display: swap`, and add a metrics-matched fallback. If the remaining swap still bothers you, switch to `optional`. Then verify. Throttle to "Slow 4G" in DevTools, check the Performance panel for layout shifts, and run Lighthouse for CLS.

If you point me at the site's code, I can look at how the font is currently declared and loaded and make these changes.
