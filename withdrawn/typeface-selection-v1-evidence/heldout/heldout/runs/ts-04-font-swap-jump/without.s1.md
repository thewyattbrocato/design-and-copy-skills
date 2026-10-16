## Why it happens

Browsers don't wait for web fonts before rendering. When the page needs your heading font, the browser has to discover it (only after CSS is parsed and a matching element exists), download it, then swap it in. What the user sees during that gap is controlled by `font-display`:

- **Invisible headline**: the default (`auto`, which behaves like `block`) hides the text for up to ~3 seconds while the font loads. That's your blank headline.
- **Flash of different font, then a jump**: with `font-display: swap`, or after the block period ends, the browser shows the fallback immediately and then swaps. If the fallback has different metrics (width, x-height, line height) from your font, text reflows and the page shifts. That's the jump, and it counts against your CLS score.

Your body text uses the system font, so it's unaffected. This is entirely a heading problem.

## What to do

1. **Preload the font** so it starts downloading right away instead of waiting for CSS parsing:
   ```html
   <link rel="preload" href="/fonts/heading.woff2" as="font" type="font/woff2" crossorigin>
   ```
   `crossorigin` is required even for same-origin fonts. Without it, the preload is wasted and the font is fetched twice.

2. **Self-host it as WOFF2**, from the same origin as the page if possible. This avoids an extra DNS and TLS connection to a third-party font host.

3. **Set `font-display: swap`** (or `optional`, see below) in your `@font-face`, so the headline is never invisible:
   ```css
   @font-face {
     font-family: "Heading";
     src: url("/fonts/heading.woff2") format("woff2");
     font-weight: 100 900;   /* range for the variable font */
     font-display: swap;
   }
   ```

4. **Match the fallback's metrics to your font** to eliminate the jump. This is the step that fixes the layout shift. Define an adjusted fallback face:
   ```css
   @font-face {
     font-family: "Heading Fallback";
     src: local("Arial");
     size-adjust: 104%;
     ascent-override: 90%;
     descent-override: 22%;
     line-gap-override: 0%;
   }
   h1, h2, h3 { font-family: "Heading", "Heading Fallback", sans-serif; }
   ```
   The numbers above are placeholders. Generate real ones with a tool like Capsize, or `next/font` / Fontaine if you use a framework. They do this automatically.

5. **Subset the font** to the characters and axes you actually use. Variable fonts can be large, and a smaller file means a shorter swap window. Drop unused axes (e.g. italic, width) and unused language ranges with `pyftsubset` or `glyphhanger`.

## Choosing between `swap` and `optional`

- **`swap`**: the custom font always shows eventually. You get a brief flash of fallback, which is nearly invisible once metrics are matched. This is the right default for a marketing site where the brand font matters.
- **`optional`**: the browser uses the custom font only if it's ready almost immediately, otherwise it sticks with the fallback for that page view (and caches the font for the next one). There's no swap and no shift at all, but first-time visitors may never see your font. Use it if layout stability matters more than brand fidelity on the first visit.

## Recommendation

Do steps 1–4: preload, self-host WOFF2, `font-display: swap`, and a metric-matched fallback. Add subsetting (step 5) if the file is over roughly 50–100 KB. Check the result in Chrome DevTools: the Network tab with throttling to see the swap, and the Performance panel's Layout Shift track to confirm the jump is gone.

If you share the CSS and the font file, or point me at the repo, I can compute the actual fallback override values and make the changes.
