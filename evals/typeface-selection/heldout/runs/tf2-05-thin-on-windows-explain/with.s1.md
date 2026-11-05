This is almost certainly screen rendering, not your CSS or font files. Each OS draws the same outlines differently, and your designer's screen is the most forgiving one.

**Why they differ**

- **Pixel density.** A MacBook Retina display has about 220 pixels per inch (2× density). A typical office monitor and an old tablet have far fewer pixels, so a thin stroke that is 1.5 pixels wide on the Mac has to be rounded to 1 or 2 pixels on the others. That rounding causes the jagged edges and the uneven stroke weight.
- **Rasterizer.** macOS doesn't snap glyphs to the pixel grid, and it renders text slightly heavier and smoother. Windows (DirectWrite/ClearType) fits glyphs to the pixel grid, which gives thinner, sharper, more uneven strokes. Old Android renders in plain grayscale with little or no hinting, so it is usually the roughest.
- **Weight and contrast.** Light weights (300 or below) and high-contrast faces with hairline strokes are the most affected. They look elegant on Retina and break up on low-density screens.
- **Hinting.** Hinting is the instructions inside a font that tell it how to fit the pixel grid. A TTF or WOFF2 file with poor or missing hinting looks fine on Mac, because the Mac ignores hinting, and rough on Windows.

**What to do**

1. **Confirm the font actually loads.** Open DevTools on the Windows machine and the tablet, go to Elements, then Computed, then Rendered Fonts. Old Android browsers sometimes fall back to a default font without any visible error. Skip this step if you've already confirmed the web font is what's rendering.
2. **Check the body weight.** If body text is at 300 or lighter, move it to 400 or heavier. Change the font before the size: pick a cut with lower contrast, open letter shapes and a larger x-height, which is the height of the lowercase letters. A thin geometric or high-contrast face should only be used for large headings.
3. **Add a weight bump for low-density screens if you use a variable font.** For example:
   ```css
   @media (max-resolution: 1.5dppx) { body { font-weight: 450; } }
   ```
   Treat that as a starting point and tune it by eye.
4. **Check the file format.** If you self-host, serve WOFF2 and make sure the files are hinted. Fonts from the foundry or Google Fonts are normally prepared for Windows already. I can't tell from here whether yours are, so check with the source.
5. **Don't rely on `-webkit-font-smoothing`.** It only affects macOS. It won't fix Windows or Android, and on a Mac it makes text lighter, which may be why the designer sees it that way.
6. **Review on the worst screens.** Have the designer check the same page on a low-density Windows monitor and the tablet before sign-off. Include a body paragraph at its smallest size.

If you share the font name, the weights in use and the body font size, I can say which of these is most likely the cause.
