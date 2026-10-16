**Probably not, at least not until you check the license.** Installing the .otf files on laptops is almost certainly covered by a desktop license. Putting them on a website via `@font-face` is "web embedding," and most foundries license that separately. It's often priced by pageviews or by domain. Serving the raw files also lets anyone download them, which many desktop licenses explicitly prohibit.

**What to check**
- Ask your designer for the font's license or invoice. Look for "web," "webfont," or "embedding" rights.
- If it's only a desktop license, buy or upgrade to a webfont license from the foundry. Many also offer a hosted service, such as Adobe Fonts or Fonts.com.
- If the font is open source (SIL OFL, for example), you can self-host it. I can't verify that "Marlowe Grotesk" is open source, so confirm it with the source.
- Check whether the license allows format conversion. You'd want WOFF2 for the web, since raw .otf files are larger and slower. Some licenses forbid converting them, but foundries usually supply WOFF2 with a webfont license.

**Fallback until it's sorted**

Use a neutral grotesque-style system stack:

```css
font-family: "Helvetica Neue", Helvetica, Arial, system-ui, sans-serif;
```

If you want something closer to a grotesk without licensing worries, use an open-source one such as Inter or Hanken Grotesk, self-hosted under the OFL. Later, put "Marlowe Grotesk" at the front of the stack and keep the same fallbacks behind it.

Use `font-display: swap` in the eventual `@font-face` rule so text shows immediately in the fallback. You can also tune `size-adjust` on a local fallback `@font-face` to reduce layout shift when the real font loads.

If you'd like, I can set up the CSS with the fallback stack now, so swapping in the licensed WOFF2 files later is a one-line change.
