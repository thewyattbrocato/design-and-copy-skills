**Short answer: not yet.** Don't upload the files until you've confirmed the license covers web use.

**Why it matters**
- A desktop install and a web embed are separate rights. Fonts are usually licensed per use: desktop, web, app and embedding, often with traffic or seat limits. A license that lets your designer install the .otf files on laptops may not let you serve them from your site.
- I can't tell you what the Marlowe Grotesk license says, and I haven't verified it. Ask your designer for the license or receipt, or check with the foundry. Ask specifically about web embedding, any pageview limits, and whether the licensee is your company or the designer's studio.
- Files that came bundled with the logo package are often logo-only or desktop-only. Get the web license before you ship.

**If web use is licensed, load it properly**
1. Ask the foundry for WOFF2 web files, or convert and subset only if the license allows modification. Serve WOFF2 only.
2. Ship two to four files: regular, a medium or semibold, bold, and a true italic if you use italics. Don't let the browser fake bold or italic.
3. Self-host it, with a preload for the main text file.

```css
@font-face {
  font-family: "Marlowe Grotesk";
  src: url("/fonts/marlowe-grotesk-regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
/* repeat for 500/600 and 700 */

body { font-synthesis: none; }
```

**Fallback until it's sorted**

Don't reference "Marlowe Grotesk" in your CSS until it's actually loaded. A named font with no `@font-face` just renders as the generic family. For now, ship the system UI stack:

```css
--font-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
```

It's a sturdy grotesque-style sans on every platform and has the weights you need. Once the font is licensed and loading, put it first in the same stack:

```css
--font-ui: "Marlowe Grotesk", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
```

**Two caveats**
- To keep the swap from shifting your layout, tune a local fallback `@font-face` with `size-adjust`, `ascent-override` and `descent-override`. Match its x-height to Marlowe Grotesk.
- I'm assuming a Latin-only site. If you need other scripts or Vietnamese, check that Marlowe Grotesk covers them. Otherwise the browser will substitute mismatched glyphs.

I can write the fallback metrics once you have the web files.
