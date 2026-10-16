**Not yet.** Having the .otf files installed on laptops only shows you have a desktop license, and that usually doesn't cover web embedding.

**Why it matters**
- Most foundry EULAs treat desktop and web as separate licenses. Web licenses are often priced by pageviews or domains.
- Uploading the .otf files makes them publicly downloadable. Anyone can grab them, and foundries do scan for this.
- Converting to WOFF2, which you'd want for performance, is sometimes explicitly restricted too.

**What to do**
1. Ask your designer where the font came from (Adobe Fonts, Google Fonts, a foundry purchase, or a custom commission) and for the license or receipt.
2. Check the EULA for "web," "webfont," or "embedding" terms.
3. If it's desktop-only, buy or upgrade to a web license from the foundry. They'll typically give you WOFF2 files and sometimes a hosted-CSS option.
4. If it's an open-source font (for example, OFL-licensed), you're fine to self-host. I can't confirm that for "Marlowe Grotesk" from here, so verify it.

**Fallback until then**
Use a system stack that looks like a neutral grotesque, with no font files to upload:

```css
body {
  font-family: "Helvetica Neue", Helvetica, Arial, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
```

Once licensing is sorted, put the brand font first and keep the stack above as the fallback:

```css
@font-face {
  font-family: "Marlowe Grotesk";
  src: url("/fonts/MarloweGrotesk-Regular.woff2") format("woff2");
  font-weight: 400;
  font-display: swap;
}
body { font-family: "Marlowe Grotesk", "Helvetica Neue", Helvetica, Arial, system-ui, sans-serif; }
```

`font-display: swap` shows the fallback text right away and swaps the brand font in when it loads.

Once you know the license status, I can help set up the `@font-face` rules and tune the fallback metrics to reduce layout shift.
