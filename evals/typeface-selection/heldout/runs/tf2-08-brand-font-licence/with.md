**Not yet. Uploading the files is the one step I'd hold off on.**

A desktop license, which is what installing .otf files on laptops normally falls under, usually doesn't cover web embedding. Foundries typically sell web licenses separately, often priced by traffic. They may also restrict converting the font to WOFF2 or subsetting it. I can't verify the terms for Marlowe Grotesk, so ask your designer for the license document, or ask the foundry. You need to know three things:
- Whether web use is covered.
- Whether self-hosting is allowed, or whether it must be served from the foundry's hosted service.
- Whether you can convert or subset the files.

If web use isn't covered, you'd buy a web license or use a hosted kit. Self-hosting without one risks a license violation, and the files are easy to download from a live site.

**Fallback for now:** ship the fallback alone and leave out the `@font-face` rule. Marlowe Grotesk is a grotesque, so use a neutral sans:

```css
body {
  font-family: "Helvetica Neue", Helvetica, Arial, system-ui, sans-serif;
}
```

I put Helvetica and Arial ahead of `system-ui` because they're closer to a grotesque. Check how it looks on Windows and Android too. Your team's laptops will show the real font because it's installed locally, so they won't see what visitors see. Review the site on a machine without the font.

**Once the license is confirmed:**
```css
@font-face {
  font-family: "Marlowe Grotesk";
  src: url("/fonts/MarloweGrotesk-Regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
/* repeat for medium/bold, and italic only if the family has a true italic */

body {
  font-family: "Marlowe Grotesk", "Helvetica Neue", Helvetica, Arial, system-ui, sans-serif;
}
```

- Load only the weights you use, usually two to four files.
- Preload the regular weight.
- `font-display: swap` avoids invisible text.
- Tune the fallback with `size-adjust` so the page doesn't jump when the font loads.

If you tell me which weights the designer supplied, I can write the full rules. The logo files are a separate matter. Logos are normally outlined artwork, so they don't need the font.
