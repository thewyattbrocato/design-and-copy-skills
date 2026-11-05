**Why it happens:** the font files and CSS are identical, but the rasterizer is not.

- **macOS** applies extra smoothing. It doesn't snap outlines to the pixel grid, and it adds some stem darkening. That makes strokes look slightly bolder and softer. Retina screens also have about 2x the pixel density, so even thin strokes land on several pixels.
- **Windows** uses DirectWrite with ClearType. On a typical 96 dpi office monitor, hinting snaps stems to whole pixels. A 1px-wide stroke is either one pixel or none, so thin weights look spindly and diagonals and curves look jagged.
- **Old Android tablets** are worse. They are usually low density, have weaker grayscale antialiasing, and have no subpixel tuning. Light weights and high-contrast faces break up the most there.

So your designer sees the design as intended. You and your dad see it on screens where thin strokes can't be drawn cleanly.

**What to do:**

1. **Check the weight and face first.** This is the most likely cause, and the fix needs no hacks. If body text uses a light or thin weight (300 or lower) or a high-contrast or thin geometric face, switch body and small text to a regular (400) weight in a sturdier face with lower contrast and open apertures. Keep delicate weights for large headings only.
2. **Test on real low-density screens.** Use a Windows monitor at 100% scaling and a mid-range Android device, not just the Mac. Also test any light-on-dark text, which looks bolder on screen, so you may need to step the weight down there.
3. **Check that the right font file is loading.** In DevTools, look at the Network and Computed → Rendered Fonts panes on Windows. A missing weight, a wrong `@font-face` mapping, or a failed load makes the browser fall back to a system font or fake the weight. Faux bold and italic look especially rough.
4. **Check the font format.** Serve WOFF2 files, and prefer fonts that ship with good hinting, or variable fonts built for screen. Some fonts that look great on Mac are poorly hinted for Windows. If this is a commercial font, ask the foundry about its screen or hinted version.
5. **Don't rely on `-webkit-font-smoothing`.** It only affects macOS, and it's the reason the Mac render differs. Using `antialiased` there makes Mac text thinner, which makes the gap smaller, but it does nothing for Windows or Android. Don't use it to chase the Windows look.
6. **Set a sensible body size.** Aim for 16px or larger for body text, with 12px as the floor for small UI text. A bump in size helps low-density screens more than any CSS rendering property.

If you tell me which font and weights the site uses, I can say whether the typeface or weight is the likely culprit and suggest a replacement. I can also look at the `@font-face` rules if you point me to the project. The working directory has no project files right now.
