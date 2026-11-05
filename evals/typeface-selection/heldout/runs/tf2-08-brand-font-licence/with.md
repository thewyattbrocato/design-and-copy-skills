**Probably not as it stands. Confirm the license before you upload anything.**

Having the .otf files installed on laptops doesn't mean you can serve them from a website. Desktop licenses and web licenses are usually separate, and a desktop license often doesn't allow embedding or hosting the font files. I don't know the terms for Marlowe Grotesk, and I can't verify them, so check these with your designer or the foundry:

1. **Who holds the license, and what does it cover?** Ask whether it includes web or webfont use, since the designer may have bought it for desktop or logo work only. Also ask whether it covers the number of seats or the traffic you have.
2. **Is self-hosting allowed?** Some foundries only allow web use through their own hosted service, and some require a separate webfont package.
3. **Is it a custom or commissioned face?** If so, the contract decides, not a standard license.

If the license does cover the web, ask the foundry or designer for the **WOFF2 webfont files**. Don't upload the .otf files. WOFF2 is smaller, and it's the format the license normally covers for web use. Subset it to the characters you need and load it with `font-display: swap`.

**Fallback until then**

Name only fonts that are actually loaded or reliably present, so leave "Marlowe Grotesk" out of the stack until the files are live. A grotesque is closest to a system UI sans:

```css
:root {
  --font-brand: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}
body { font-family: var(--font-brand); }
```

Don't use a bare `sans-serif` as the whole stack, because then the browser picks. Don't list "Marlowe Grotesk" on its own without an `@font-face`, either. Visitors don't have it installed, so they would just get the generic fallback. Your team will see the real font on their laptops, so check the site on a machine without it installed to see what customers get.

**When the licensed WOFF2 files arrive**

```css
@font-face {
  font-family: "Marlowe Grotesk";
  src: url("/fonts/MarloweGrotesk-Regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
/* repeat for the weights and the true italic you actually have */

:root {
  --font-brand: "Marlowe Grotesk", system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif;
}
```

- Load only the weights the brand uses. If there's no italic file, set `font-synthesis: none` so the browser doesn't fake one.
- Preload the one or two critical files.
- Tune the fallback's `size-adjust` to match Marlowe's x-height so the swap doesn't shift the layout.

If it turns out the license doesn't cover the web, you can ask the foundry for a web license or look for an open-licensed grotesque as a stand-in. The fallback stack above works in the meantime.
