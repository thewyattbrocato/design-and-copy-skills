The font files and CSS are the same, but the rasterizer, the pixel density and the hinting differ between your devices, so the same outlines get drawn differently.

## Why it differs

- **Pixel density.** A MacBook Retina panel is about 220 ppi. Your office monitor is probably 90–110 ppi, and an old tablet is often low-density with a weak panel. At low density, a 1.5px stem has to land on whole pixels, so strokes look thin, uneven or stair-stepped.
- **Different rasterizers.**
  - macOS doesn't snap glyphs to the pixel grid. It smooths them and tends to render them slightly heavier, so they look even.
  - Windows (DirectWrite/ClearType) fits outlines to the grid and anti-aliases mostly horizontally. Thin, high-contrast strokes can fade or break, and it relies on the font's hinting.
  - Android uses FreeType, usually with light or no hinting and grayscale anti-aliasing. On an old low-resolution screen that gives jagged edges.
- **Light or high-contrast cuts suffer most.** The Mac hides weak strokes, and the other two screens expose them.

## What to do

1. **Check the weight you're shipping.** If body text is 300 or lighter, or the face has hairline strokes, move to a regular (400) cut with lower stroke contrast. This is the most likely cause. Keep delicate weights for large headings only.
2. **Check the CSS for `-webkit-font-smoothing: antialiased`.** It only affects macOS, where it makes text thinner. If it's set, your designer may be seeing a lighter rendering than the default, so try removing it.
3. **Check that hinting survived.** Many subsetting and conversion tools strip hinting, and Windows relies on it. Re-export with hinting kept, or autohint TTF sources (for example ttfautohint) before converting to WOFF2.
4. **Check that every weight you use is actually loaded.** If `font-weight: 500` has no matching `@font-face`, the browser picks a neighbor or fakes bold. Confirm in DevTools (Rendered Fonts) on the Windows machine.
5. **If the font is variable,** nudge the weight up on low-density screens only:
   ```css
   @media (max-resolution: 1.5dppx) { body { font-weight: 450; } }
   ```
6. **Keep body text at 16px or larger,** and 12px or larger for the smallest labels.
7. **Test on the real devices,** not only the Mac. Use a paragraph at your smallest size on the real background. If the Windows and Android renders are still weak, change the face or weight rather than adding CSS tricks.

The Mac render isn't wrong, but the Windows and Android renders are what many of your visitors will see. Design for the weakest screen, because the Mac will still look fine.

If you tell me the font and the weights you're using, I can suggest a specific change. Or point me at the project and I'll check the `@font-face` rules and CSS.
