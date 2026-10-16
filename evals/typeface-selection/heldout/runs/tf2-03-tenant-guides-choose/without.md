**Short answer:** Use one free, highly legible sans-serif for everything, and make sure the web version falls back to fonts that are already on your readers' devices.

**Recommended setup**

- **Body and headings (web and print):** Atkinson Hyperlegible, or Atkinson Hyperlegible Next, which has more weights. The Braille Institute made it, and it's free under the SIL Open Font License. Its letterforms are designed to be hard to confuse (I/l/1, O/0), which helps with dates, dollar amounts, and case numbers. Download it from Google Fonts and self-host it, so there's no third-party request and it works on slow connections.
- **Web fallbacks:** Library computers are usually locked down and can't load much, so the fallbacks matter. Verdana is the best match on Windows. Roboto and Noto Sans cover Android.

```css
@font-face {
  font-family: "Atkinson Hyperlegible";
  src: url("/fonts/AtkinsonHyperlegible-Regular.woff2") format("woff2");
  font-weight: 400;
  font-display: swap;
}
@font-face {
  font-family: "Atkinson Hyperlegible";
  src: url("/fonts/AtkinsonHyperlegible-Bold.woff2") format("woff2");
  font-weight: 700;
  font-display: swap;
}
body {
  font-family: "Atkinson Hyperlegible", Verdana, Roboto, "Noto Sans", Arial, sans-serif;
  font-size: 1.125rem;
  line-height: 1.55;
}
```

- **Print:** Embed the same font in the PDF so handouts match the web version. If you'd rather have a serif for 15–30 pages of continuous text, Source Serif 4 or Charis SIL are good free options. Keep headings in Atkinson.

**Practical rules that matter more than the font choice**

- Load only two weights, regular and bold. Skip light and thin weights, which wash out on cheap screens and photocopies.
- Use 18px or larger on the web. In print, use 12pt at minimum, and 13–14pt if handouts go to older readers.
- Avoid long passages in italics or all caps. Use bold and clear headings to organize instead.
- Left-align the text, not justified. Keep lines to about 60–75 characters.
- Keep strong contrast, with dark text on white. Photocopies and low-quality screens are hard on gray text.

**Why not the usual alternatives**

- **Google Fonts hotlinking:** It adds a third-party request, and it can be blocked or slow on library networks.
- **Decorative or "friendly" display fonts:** They look worse on low-resolution screens and in photocopies, and they're harder to read for people with dyslexia or low vision.
- **Arial or Times New Roman alone:** They work as fallbacks, but they're less distinct at small sizes.

If you want the simplest possible option, skip the webfont and use `font-family: Verdana, Roboto, "Noto Sans", sans-serif`. It costs nothing, loads instantly, and is very readable. Atkinson is a modest upgrade, not a necessity.
