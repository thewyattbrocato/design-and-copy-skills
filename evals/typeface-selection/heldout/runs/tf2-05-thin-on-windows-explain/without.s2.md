This is mostly the rendering pipeline, not your CSS or fonts. The same font outlines get rasterized differently on each platform.

## Why it happens

**1. macOS makes text heavier and smoother.**
- Core Text applies stem darkening, which thickens glyph edges a little.
- Its grayscale antialiasing doesn't snap outlines to the pixel grid, so shapes stay close to the designer's intent.
- Retina displays at 2x or 3x pixel density hide most remaining rasterization artifacts.

**2. Windows uses DirectWrite, which stays closer to the exact outline.**
- Windows renders at the true weight, with no stem darkening, so the same weight looks thinner than on a Mac.
- ClearType uses subpixel (RGB) antialiasing. That trades some smoothness for horizontal sharpness, which shows up as color fringing or jaggedness.
- Many office monitors are 1x density (96 DPI). A thin stroke of about 1px can't be drawn smoothly at that density.

**3. The font's hinting data matters a lot at low DPI.**
- Hinting instructions (TrueType `gasp`, `fpgm` and `prep` tables, or their absence) control how outlines snap to pixels.
- Unhinted or auto-hinted web fonts often look wobbly on Windows and Android.
- Fonts converted to WOFF2 with the hinting stripped, which is common for file size, are especially prone to this.

**4. Old Android tablets have weaker text rendering.**
- Older Android versions have less refined FreeType settings and often no subpixel positioning.
- Their low-DPI screens and aging panels, with lower contrast and washed-out colors, make thin text look worse.
- Vendor-modified WebViews or old Chrome builds may handle variable fonts or `font-weight` interpolation differently.

**5. Light weights make everything worse.**
- A font-weight of 300 or lighter, or light gray text on white, looks fine on Retina and falls apart on 1x screens.
- Thin strokes lose contrast when they land between pixels.

## What to do

**Quick wins:**
- **Raise the weight.** Use 400 for body text. If you use 300, move to 400 or use a slightly heavier cut. Check that any `font-weight` value maps to a font file you actually load, so the browser isn't faking it with synthetic bold or light.
- **Increase contrast.** Use darker text colors, such as `#222` instead of `#888`. This is the cheapest fix for the "thin" look.
- **Bump the size slightly.** Small text at 13–14px suffers most. 16px for body is a safe floor.
- **Don't rely on `-webkit-font-smoothing: antialiased`.** It only affects macOS, and it makes Mac text lighter and thinner. If your designer's Mac has it on, that's part of why her view differs from the rest. Removing it brings Mac rendering closer to what Windows users see.

**Font-level fixes:**
- **Use a font with good hinting for Windows.** Check that your WOFF2 files keep hinting. Google Fonts serves different, hinted files to Windows, which is one reason its fonts often look better there than self-hosted ones.
- **Try a variable font** with a weight axis, so you can fine-tune weight (say 350 → 400) to compensate for platform differences.
- **If a specific font looks bad on Windows,** consider swapping it. Some typefaces are designed with screen hinting in mind (Inter, Segoe UI, Roboto), and others look fine only on high-DPI screens.

**Process fixes:**
- **Test on real low-DPI Windows and Android devices,** or use BrowserStack. A Mac-only review will always look best.
- **Make the Mac view less flattering.** Ask your designer to check on a 1x external monitor or in Chrome with device pixel ratio 1. She'll see the same problem you do.
- **Decide what's acceptable.** You can't make rendering identical across platforms. Aim for readable and acceptable on the worst device you support.

## Where I'd start
1. Check whether you use `font-weight: 300` or lighter, or light gray text.
2. Check whether you set `-webkit-font-smoothing: antialiased`.
3. Check whether your self-hosted font files are hinted.
4. Test the updated CSS on your office monitor and your dad's tablet.

If you can share the CSS or tell me which font you use, I can look for specific problems. Nothing in the working directory looks like your site, so I haven't looked at any code.
