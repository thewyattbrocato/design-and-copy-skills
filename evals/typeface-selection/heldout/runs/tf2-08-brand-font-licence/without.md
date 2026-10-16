Not yet. Installing the .otf files on laptops and serving them from your website are usually covered by different licenses.

**Why to check first**
- Most commercial font licenses are split by use: desktop, web, app, and so on. A desktop license normally doesn't allow uploading the font to a server. Once it's behind `@font-face`, anyone can download it.
- Sometimes the web license is just a separate purchase or an add-on. Sometimes the foundry hosts it for you, as with Adobe Fonts or Monotype. Sometimes the font is custom-commissioned, and then the contract decides.
- Unlicensed web use is the kind of thing foundries do audit for, and they send invoices or takedown notices.

**What to do**
1. Ask your designer where the font came from (foundry, purchase receipt, or a custom contract). I don't know "Marlowe Grotesk" well enough to say what its license allows.
2. Look for a web or "webfont" license in the EULA, and check any limits on pageviews, domains, or self-hosting.
3. If it's covered, convert the files to WOFF2 (the foundry often supplies these) and self-host them. Don't serve raw .otf files. If it isn't covered, buy the web license or use the foundry's hosted service.

**Fallback until then**

Use a system font stack with a similar feel. It loads fast and needs no license:

```css
font-family: "Marlowe Grotesk", -apple-system, BlinkMacSystemFont, "Segoe UI",
  Helvetica, Arial, sans-serif;
```

If you want something closer to a grotesk's look, Inter, Work Sans, or Hanken Grotesk are free on Google Fonts under the OFL, which allows web use. Put one right after "Marlowe Grotesk" in the stack so it's what shows until the licensed font is ready.

Once you do load the real font, add `font-display: swap;` in the `@font-face` rule so text shows right away in the fallback. If you want, I can write the `@font-face` block and the CSS variables once you know the license is covered.
