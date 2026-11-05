**Not yet. Check the license first.**

Having the .otf files installed on your laptops doesn't mean you can put them on a website. Most foundries sell desktop and web licenses separately. Web licenses are often priced by traffic, and some forbid self-hosting, converting formats, or both. Publishing the files also lets anyone download them. Ask your designer, or the foundry or the license receipt, these questions:

1. Does the license cover web embedding and self-hosting?
2. May you convert the files to WOFF2? Browsers want WOFF2, and a raw .otf is larger than it needs to be. Some licenses require you to use the foundry's own web files.
3. Are there page-view limits?

I can't tell you what Marlowe Grotesk's terms are, so I'm not guessing. If the license only covers desktop use, buy the web license or use the foundry's hosted service. The logo files are a separate matter, because a logo is artwork and doesn't depend on the font license.

**Once you're cleared**, use the WOFF2 files, not the .otf:

```css
@font-face {
  font-family: "Marlowe Grotesk";
  src: url("/fonts/MarloweGrotesk-Regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
/* repeat for the medium/bold and italic files you actually own */
```

Only declare weights and styles you have files for. Otherwise the browser fakes bold and italic, and it looks wrong. Preload the one file used above the fold, such as the regular weight.

**Fallback until then.** A grotesque pairs best with a neutral system sans, so use this stack:

```css
font-family: "Marlowe Grotesk", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
```

Until the web files are licensed and loaded, drop the first name so the page doesn't depend on it. Your team's laptops will have the font installed and see it, and everyone else will see the system sans. That means your own checks of the site won't match what visitors see. Test in a browser or profile without the font installed.

When the real font loads, the text will shift slightly because the metrics differ. If that bothers you, add a size-adjusted fallback with `size-adjust` and `ascent-override` in an `@font-face` that points at `local("Arial")`.
