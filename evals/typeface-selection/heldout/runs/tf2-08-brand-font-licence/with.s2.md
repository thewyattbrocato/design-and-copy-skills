**Not yet.** Having the font installed on the laptops doesn't mean you can put it on the website.

**Licensing**
- Desktop licenses usually cover installing the font on a set number of computers. Web embedding via `@font-face` is often a separate license, sometimes priced by pageviews. Many foundries also forbid putting the raw `.otf` files on a public server, because anyone can download them.
- I can't tell what the license for "Marlowe Grotesk" allows. Ask your designer for the license or receipt, or check with the foundry. You want to know whether it includes web use, whether you can self-host or must use their hosted service, and whether you can convert the files to WOFF2.
- If web use isn't covered, buying the add-on is usually the fix. It's often cheap compared with the risk of a violation claim.

**Once you have the rights**
- Don't ship the `.otf` files. Convert them to WOFF2, subset them to the characters you need, and use only the weights and styles the site actually uses (probably 2–4 files).
- Load them like this:

```css
@font-face {
  font-family: "Marlowe Grotesk";
  src: url("/fonts/MarloweGrotesk-Regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
/* repeat for medium/semibold/bold, and italic only if the family has a true italic */
```

Add a `<link rel="preload" as="font" type="font/woff2" crossorigin>` for the regular weight. Declare each weight as its own `@font-face`. Otherwise the browser fakes bold and italic, which looks bad.

**Fallback for now**
I'm assuming a Latin-script audience and a screen-only site. Since this is a grotesque, use a neutral system sans:

```css
font-family: "Marlowe Grotesk", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
```

Until the license is sorted, drop `"Marlowe Grotesk"` from the front, because a name that isn't loaded does nothing. Visitors without it installed will just get the system sans. When the font is licensed and loaded, put it back first.

You can reduce the layout jump when the web font swaps in by adding a `size-adjust` fallback `@font-face` built on Arial. Tune it once the real files are in.

**The logo**
Logo files are separate from the typeface license. Logos are normally supplied as SVG or PNG with the lettering already drawn, so they don't need the font.
