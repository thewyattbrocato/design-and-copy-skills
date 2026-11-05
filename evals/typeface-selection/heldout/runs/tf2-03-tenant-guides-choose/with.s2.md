**Recommendation: use one open-licensed family, Source Sans 3, for everything.** Self-host it for the web pages and install the same files for print.

I'm assuming Latin-script text (English, plus Spanish accents if you publish it), body text down to about 16px on screen and 10.5–11pt in print, and that you have no paid font licenses.

**Why this fits your readers and budget**
- **Free:** It's released under the SIL Open Font License, so you can use it on the web and in print and embed it in PDFs at no cost. Confirm that on the project's own page before you rely on it.
- **One family:** It has regular, semibold, bold and true italics. Headings, body, callouts and form labels get their hierarchy from weight and size, so there's no second font to load or keep consistent.
- **Readable at small sizes:** The letters are sturdy and open, and I, l and 1 are easy to tell apart. That helps on low-density older phone screens.
- **Same look everywhere:** Web and print use identical letterforms, so a handout matches its web page.

**CSS**
```css
@font-face {
  font-family: "Source Sans 3";
  src: url("/fonts/SourceSans3-Regular.woff2") format("woff2");
  font-weight: 400; font-style: normal; font-display: swap;
}
@font-face {
  font-family: "Source Sans 3";
  src: url("/fonts/SourceSans3-Italic.woff2") format("woff2");
  font-weight: 400; font-style: italic; font-display: swap;
}
@font-face {
  font-family: "Source Sans 3";
  src: url("/fonts/SourceSans3-Bold.woff2") format("woff2");
  font-weight: 700; font-style: normal; font-display: swap;
}
/* add a Bold Italic file only if you actually use bold italic */

body {
  font-family: "Source Sans 3", system-ui, "Segoe UI", Roboto, Arial, sans-serif;
}
```

**Loading and fallbacks**
- Load only two to four static WOFF2 files (regular, italic, bold). Subset them to Latin so they stay small on slow connections.
- `font-display: swap` means text appears immediately in the fallback font. That matters on old phones and slow library connections.
- The fallback stack renders as Roboto on Android and Segoe UI on Windows, both of which are sturdy sans faces. If the web font fails, the page still reads fine.
- For print, install the same font on whatever computer lays out the handouts, and embed fonts when you export PDFs.

**If you can't self-host**
Use the stack alone: `system-ui, "Segoe UI", Roboto, Arial, sans-serif`. It costs nothing and loads instantly. The look will vary a little between devices, but it's a sound choice, not a failure.

**Check before you commit**
- Print one real page of a guide and view it on the oldest Android phone you can borrow. Look at the smallest text you use, such as footnotes and deadlines, and make sure numbers and dates are easy to read.
- Don't use Georgia or Calibri as named fonts. Android doesn't ship them, so those readers would get a mismatched fallback.
- Don't use light weights, script faces or decorative display faces. They get thin and blurry on old screens and photocopies.

I can draft the full stylesheet, including heading sizes and print rules, if that would help.
