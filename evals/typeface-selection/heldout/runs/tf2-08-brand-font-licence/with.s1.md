**Not yet.** Installing the fonts on laptops doesn't mean you can put them on the website.

**Why it matters**
- Font licenses are usually separate for desktop, web (`@font-face`) and app embedding. A desktop license often doesn't cover web serving, and sometimes the web license is priced by pageviews.
- Check the license or invoice with the foundry, or ask your designer where the fonts came from. I can't tell you what Marlowe Grotesk's terms are, so I'm not guessing.
- If web rights are missing, buy or add the web license. Serving the files without it is the risky route.

**If the web license is confirmed**
- Convert the .otf files to WOFF2 and subset them to the characters you need. Check the license allows modification and conversion.
- Self-host two to four files, such as Regular, Medium or Semibold, Bold, and a true italic if the family has one. Don't let the browser fake bold or italic.
- Use `font-display: swap` and preload the one critical file.

```css
@font-face {
  font-family: "Marlowe Grotesk";
  src: url("/fonts/MarloweGrotesk-Regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
/* repeat for 500/600, 700 */
```

**Fallback until then**

Use a system sans stack. A grotesque brand face sits closest to a neutral system sans, and it never falls through to Times:

```css
font-family: "Marlowe Grotesk", system-ui, -apple-system, "Segoe UI", Roboto,
  "Helvetica Neue", Arial, sans-serif;
```

While you wait on the license, drop `"Marlowe Grotesk"` from the stack or leave it off the page. Your laptops have it installed, so it will look right to you and nobody else. Everyone else will see the system font, so preview in a browser on a machine without the font, or you'll misjudge it.

Once the web font is live, add a fallback `@font-face` using `size-adjust` and `ascent-override` against Arial. That reduces layout shift when the swap happens.

**Assumptions:** this is a screen-only Latin-script site. Ask the designer for the license and for any web-ready files, since the foundry may already supply WOFF2.
