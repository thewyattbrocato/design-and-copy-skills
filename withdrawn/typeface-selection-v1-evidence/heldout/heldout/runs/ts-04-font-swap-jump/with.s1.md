## What's happening

Your page is showing the two normal behaviors of web fonts while they download. The browser can't render the heading in your font until the file arrives, so it has to pick one of two behaviors.

- **Invisible headline (FOIT):** With the default `font-display` (`block`), browsers hide the text for up to about 3 seconds while they wait for the font. This is the "headline is just invisible" symptom. It's worse on slow connections, or when the font file is discovered late, because it's only requested after the CSS is parsed and the heading is found.
- **Different font, then a jump (FOUT plus layout shift):** If you use `font-display: swap`, or a browser's default timeout expires, the heading renders in a fallback font first. When your font arrives, the text swaps. The two fonts have different widths, heights and line spacing, so lines rewrap and everything below the heading moves. That's the jump.

Your body text is on the system font, so it never has this problem. Only the headings do, and they are the largest, highest-up text on the page. That makes the swap very visible.

## What to do

1. **Never block text invisibly.** Set `font-display: swap` on the `@font-face` for the heading font. If the heading doesn't need to be in your font on a slow first visit, `optional` is the alternative. It uses the font only if it arrives almost immediately, and otherwise it keeps the fallback for that page view, so nothing swaps or shifts. For a marketing headline, `swap` plus matched metrics (step 3) is usually the better trade.

2. **Preload the one critical file.** Without a preload, the browser finds the font late. Add this in `<head>`:
   ```html
   <link rel="preload" href="/fonts/Heading.woff2" as="font" type="font/woff2" crossorigin>
   ```
   `crossorigin` is required even for same-origin fonts. Without it, the preload is fetched and then ignored.

3. **Match the fallback's metrics to your font.** This is what removes the jump. Define a local fallback face and adjust it to line up with your heading font:
   ```css
   @font-face {
     font-family: "Heading Fallback";
     src: local("Arial");
     size-adjust: 104%;          /* tune these four values */
     ascent-override: 92%;
     descent-override: 24%;
     line-gap-override: 0%;
   }
   h1, h2, h3 {
     font-family: "Heading", "Heading Fallback", system-ui, sans-serif;
   }
   ```
   The numbers above are placeholders. Compute the real ones from your font file. Tools like Fontaine, Capsize, or the Next.js and Nuxt font modules (which do this automatically) can generate them. Then pick a fallback with similar proportions, and test it against the real font.

4. **Self-host and shrink the file.** Serve WOFF2 from your own domain, not a third-party font host. That avoids an extra connection. Subset it to the languages you use, for example Latin only. Check that the file really contains the weight axis you use, and remove any axes you don't use.

5. **Keep the stack honest.** End the heading stack in a real fallback, as in the CSS above, never just `serif` or `sans-serif`. Add `font-synthesis: none` so the browser doesn't fake a bold weight if the variable file fails to load.

6. **Test it the way users hit it.** In DevTools, throttle the network to Slow 4G, disable the cache, and reload. Then block the font file and check that the page still looks fine. Watch for layout shift in the Performance panel or Lighthouse (CLS).

## Result

With `swap`, the preload and metric-matched fallback together, the heading shows up immediately in a similar-looking font. When your font arrives, the swap changes the letterforms slightly but nothing moves. Since you only have one font file and the body is on the system font, you're already in a good position, and this is a small amount of CSS.

I haven't seen your actual CSS. If you share the `@font-face` rule and the font file name, I can work out the real override values and check for other causes, such as a render-blocking stylesheet or a font that loads from JavaScript.
