The difference almost certainly comes from how each operating system and screen draws the font, not from your CSS or font files.

## Why it happens

**1. Different text rasterizers.**
- **macOS** uses Core Text. It doesn't snap glyphs to the pixel grid and adds a slight weight boost (stem darkening), so text looks smooth and a bit heavier.
- **Windows** uses DirectWrite, which tries to fit glyph outlines to the pixel grid. On a standard-density monitor, thin strokes can fall between pixels, so they look lighter and jagged. Windows often uses ClearType subpixel rendering, which adds color fringing and a thinner look.
- **Android** uses FreeType. Its quality depends on the device, the Android version, and the browser. Old tablets often have weak hinting and no subpixel rendering.

**2. Screen density.** MacBooks have Retina displays at about 220 ppi, with 2 or more device pixels per CSS pixel. Many office monitors and old tablets are about 96–130 ppi at 1x. At 1x, a 1px stem has to land on whole pixels, so it looks jagged. Retina has enough pixels to hide that.

**3. Font weight and design.** Light weights (300 or below) are the worst offenders. A thin stroke that renders fine at 2x can nearly vanish at 1x. The same applies to fonts that aren't hinted for screens.

**4. Font file format.** If you serve a font with weak or no hinting, such as a web-optimized subset with the hints stripped, Windows will render it worse. Windows relies on hinting data more than macOS does.

## What to do

1. **Confirm it's rendering, not a bug.** Check that the same font file loads on all devices and that no fallback font is kicking in. In DevTools, open the Network tab and the Computed > Rendered Fonts panel.
2. **Raise the weight.** Move body text from 300 to 400, and headings from 400 to 500 or 600. This is usually the biggest fix. Pick weights that work on the worst screen, not the best.
3. **Increase size and contrast.** Use at least 16px for body text. Avoid light gray on white. Pure `#000` isn't needed, but something like `#222` or darker helps thin text a lot.
4. **Check the font's hinting.** If you self-host, use a font that includes TrueType hinting (ttfautohint output is common) for Windows. Google Fonts and most commercial foundries already handle this. If you subset or convert files yourself, check that hinting wasn't stripped.
5. **Use a variable font or a heavier static cut** if you want finer control, for example `font-weight: 380`. Note that this only helps if the font supports it.
6. **Be careful with `-webkit-font-smoothing: antialiased`.** It only affects macOS and makes text *thinner* there. If your CSS has it, removing it makes macOS text a little heavier and more consistent with the others. Don't expect it to fix Windows or Android.
7. **Test on real low-density screens.** Have your designer check on a 1x external monitor, or use BrowserStack. Chrome DevTools device emulation does not reproduce platform text rendering.

## Reality check

Some difference between platforms is normal and can't be removed. The goal is for text to be comfortable to read on the worst common screen, not identical everywhere. Bumping the weights and contrast usually gets you most of the way there.

If you want, I can look through your CSS for light font weights, `font-smoothing` rules, and font-loading setup. Point me at the project folder, since the current working directory is empty of site files as far as I know.
