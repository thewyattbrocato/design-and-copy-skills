## Why it happens

The browser doesn't have your heading font when it first renders, so it has to decide what to show while the file downloads. Two things you're seeing come from that:

- **Invisible headline (FOIT):** With the default `font-display: auto` (usually `block`), browsers hide text for up to about 3 seconds while the font loads. On a slow connection the headline stays invisible. This is also why it only happens "sometimes". It depends on network speed and cache.
- **Fallback flash, then a jump (FOUT plus layout shift):** If you've set `font-display: swap`, the headline shows right away in the fallback font. When your font arrives, it swaps in. The two fonts have different widths, heights and line spacing, so lines rewrap and everything below moves. That jump hurts your CLS score too.

Your body text is a system font, so it never swaps. Only the headings are affected, but a headline sits at the top of the page, so the shift moves everything under it.

## What to do

1. **Never block text.** Use `font-display: swap` on the heading font. If a late swap shifts the layout too much, use `optional`. The browser then uses your font only if it arrives almost immediately, and otherwise keeps the fallback for that page view. For a marketing headline, `swap` plus the metric matching in step 3 is usually the better choice.

2. **Make the font arrive sooner.**
   - Self-host it as WOFF2 instead of loading it from a third-party font host. This removes a DNS and TLS round trip.
   - Preload it: `<link rel="preload" href="/fonts/heading.woff2" as="font" type="font/woff2" crossorigin>`. The `crossorigin` attribute is required even for same-origin fonts. Without it the file is fetched twice.
   - Subset it to the scripts you actually use. Variable fonts can be large, so this often matters most.
   - Keep it to this one file. Don't also load static weights.

3. **Make the fallback match, so the swap doesn't move anything.** This is the fix for the jump. Define a local fallback face with metric overrides:

   ```css
   @font-face {
     font-family: "Heading Fallback";
     src: local("Arial");
     size-adjust: 104%;       /* tune to your font */
     ascent-override: 92%;
     descent-override: 24%;
     line-gap-override: 0%;
   }
   @font-face {
     font-family: "Heading";
     src: url("/fonts/heading.woff2") format("woff2");
     font-weight: 100 900;    /* match the axis range the file really has */
     font-display: swap;
   }
   h1, h2, h3 {
     font-family: "Heading", "Heading Fallback", system-ui, sans-serif;
   }
   ```

   Don't guess the override numbers. Tools such as Capsize, or the font-metrics fallback generation built into Next.js (`next/font`) and Fontaine, calculate them from your file. Use whichever fits your stack.

4. **Stop the headline from wrapping differently.** Reserve space for it with a sensible `min-height`, or use `text-wrap: balance` on headings so a small width difference changes the layout less.

5. **Keep the stacks honest.** Body text can stay as `system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`. Also add `font-synthesis: none` so the browser doesn't fake a weight if the variable axis is missing.

## How to check it

In Chrome DevTools, throttle the network to Slow 4G, disable the cache, and reload. Then check these:
- The headline is visible immediately.
- The swap doesn't visibly move anything.
- The Performance panel's layout shift entries show no shift from the heading.
- The Network panel shows the font requested early, with the preload, and only once.

I haven't seen your code. If you share the CSS and the `<head>`, I can point to the exact cause (a missing `font-display`, a font loaded from a CSS `@import`, a missing `crossorigin`, and so on) and write the fallback metrics for you.
