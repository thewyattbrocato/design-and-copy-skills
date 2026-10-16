**Why it happens:** The same font file is rasterized differently on each OS. Your CSS and font files are identical, but the pixels come from the platform's text renderer.

- **macOS** doesn't use hinting and applies grayscale antialiasing that slightly thickens glyphs, so strokes keep the designer's proportions. MacBook screens are also Retina (2x or more), which gives you 4+ pixels per CSS pixel to draw curves with.
- **Windows** uses DirectWrite, often with ClearType subpixel rendering and some hinting. That snaps stems to the pixel grid, and on a ~96 DPI office monitor a thin stroke can end up one pixel wide or lighter than intended. Hence "thinner and jagged."
- **Old Android tablets** typically have a low-density screen, an older FreeType build, and little or no subpixel positioning. Light weights fall apart there.

The biggest factors are screen density and font weight. A 300 or 200 weight that looks elegant at 2x looks spindly at 1x.

**What to do:**

1. **Test on real low-DPI screens.** You already have two. Don't judge typography only on a Retina display.
2. **Raise the weight for body text.** Use 400 instead of 300, or a variable font where you can nudge it (for example `font-weight: 350`–`400`). This is the most effective fix.
3. **Don't use thin weights below about 18–20px.** Keep them for large headings.
4. **Increase size or contrast slightly.** Pure gray text on white makes thin strokes look worse. Darken the text color a bit.
5. **Check the font format.** If you're serving TTF/OTF, make sure WOFF2 has the same hinting data. Some fonts (especially web-optimized ones) are poorly hinted for Windows. Using a font with good ttfautohint or a variable font built for screen use helps.
6. **Add `text-rendering: optimizeLegibility;`.** It's cheap and sometimes helps kerning. Avoid relying on `-webkit-font-smoothing: antialiased`. It only affects macOS, and it makes text *thinner* there, so it can widen the gap.
7. **Consider a different body font.** Fonts designed for screens, like Inter, Roboto and Source Sans, hold up better on low-DPI displays than fonts designed for print.

You won't get pixel-identical rendering across platforms. The goal is text that is still comfortable to read on the worst screen your users have. If you want, I can look through the CSS for the font weights and sizes in use. Point me at the project directory, since the current working directory doesn't appear to contain the site.
