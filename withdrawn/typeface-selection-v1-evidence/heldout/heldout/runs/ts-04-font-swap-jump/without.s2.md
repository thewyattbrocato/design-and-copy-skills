## Why it happens

The browser doesn't know about your font until it has parsed the CSS and found text that uses it. Only then does it start the download. Until the file arrives, it has to choose between two behaviors:

- **Invisible headline (FOIT):** With the default `font-display: auto`, which is effectively `block`, browsers hide text for up to about 3 seconds while the font loads. That's your invisible headline.
- **Flash of a different font, then a jump (FOUT plus layout shift):** If you use `font-display: swap`, the text shows immediately in a fallback font and then swaps. The fallback and your custom font have different widths, x-heights, and line heights, so the headline reflows and everything below it moves. That hurts your CLS score.

Only the headings are affected, since body text uses the system font. That means the fix is small.

## What to do

1. **Self-host the font as WOFF2, and subset it.** Third-party font CDNs add DNS, TLS, and CSS round trips before the font request even starts. Variable fonts are often large, so strip unused glyphs and axes. You may only need Latin and the weight range you actually use.

2. **Preload it.** This starts the download at the top of the page instead of waiting for CSS parsing. The `crossorigin` attribute is required even for same-origin fonts, or the file gets fetched twice.
   ```html
   <link rel="preload" href="/fonts/Heading.woff2" as="font" type="font/woff2" crossorigin>
   ```

3. **Pick `font-display` deliberately.**
   - `swap` always shows the custom font eventually, and a good fallback keeps the jump small. This is the safe default for a brand headline.
   - `optional` avoids any swap or shift. If the font isn't ready within about 100ms, the browser uses the fallback for that page view. With preload and caching, repeat visits get the custom font. Choose this if CLS matters more than first-visit brand fidelity.
   - Avoid `block` and `auto` for this case.

4. **Make the fallback match your font's metrics.** This is the step that removes the jump. Define an adjusted local fallback face:
   ```css
   @font-face {
     font-family: "Heading";
     src: url("/fonts/Heading.woff2") format("woff2");
     font-weight: 100 900;      /* variable range */
     font-display: swap;
   }
   @font-face {
     font-family: "Heading Fallback";
     src: local("Arial");
     size-adjust: 104%;          /* tune these to your font */
     ascent-override: 92%;
     descent-override: 24%;
     line-gap-override: 0%;
   }
   h1, h2, h3 {
     font-family: "Heading", "Heading Fallback", sans-serif;
   }
   ```
   You don't need to compute the override values by hand. Tools like Fontaine, Capsize, or Next.js's `next/font` generate them, and `next/font` also handles self-hosting and preload.

5. **Verify.** Throttle the network in DevTools and check that the font request starts early in the waterfall. Then check CLS in Lighthouse or the Performance panel's layout shift markers.

## My recommendation

Self-host a subsetted WOFF2, preload it, use `font-display: swap`, and add the metric-matched fallback. That fixes the invisible text and reduces the jump to nearly nothing. If you still see a shift on slow connections, switch to `optional`.

If you share the site's stack (Next, Astro, plain HTML, and so on) and the font file, I can make these changes in the repo.
