It's the screens and the font renderers, not your CSS or font files. The same outlines get drawn differently on each device.

## Why it happens

1. **Pixel density.** A MacBook Retina display has about 220 ppi, so a thin stroke gets several physical pixels and edges look smooth. A typical office monitor (about 90–110 ppi) and an older tablet give the same stroke one or two pixels. Thin strokes then drop out, get uneven, or look jagged.
2. **Different rasterizers.**
   - macOS adds a little stem darkening and doesn't snap glyphs to the pixel grid. Text looks slightly heavier and softer.
   - Windows (DirectWrite/ClearType) fits glyphs to the pixel grid and uses subpixel RGB rendering. Strokes come out thinner and sharper, and they can look jagged when the font has weak hinting. Web fonts that are only auto-hinted, or not hinted at all, make this worse.
   - Older Android uses FreeType with lighter smoothing and often a low-density panel. Together those give thin, rough text.
3. **Weight and contrast of the font itself.** A light or regular cut of a high-contrast or geometric face has hairline strokes. These survive on Retina and break up on low-density screens.
4. **Possibly a mismatched web font file.** Check that Windows and Android are loading the same file as the Mac. A missing weight or a failed load can mean a fallback font or a faux-bolded one.

## What to do

1. **Check what actually loads on the bad devices.** Open DevTools → Network/Computed → Rendered Fonts on the Windows machine. Confirm the intended family and weight, not a fallback and not synthesized bold.
2. **Use a sturdier weight.** If body text is 300 or a thin regular, move to a true 400, or 500 for small text. If the face has hairline strokes or high contrast, switch to a lower-contrast, more open face for body and keep the delicate face for large headings only. The usual cause on Windows is a light or hairline cut, not the size.
3. **Keep text at 16px or larger for body.** About 12px is the floor for labels, and only in regular weight or heavier.
4. **Don't compensate in CSS.**
   - Don't use `-webkit-font-smoothing: antialiased` on everything. It only affects macOS and makes light text lighter, which widens the gap you're seeing.
   - Leave `text-rendering: optimizeLegibility` alone unless you need kerning or ligatures.
   - Avoid `font-weight` below 400 for text.
5. **Ship hinted, current font files.** Use WOFF2 from a source that includes hinting for Windows (ttfautohint output, or the foundry's web-optimized files). If you're using a variable font, test it on Windows. Some render noticeably lighter there.
6. **Add real fallbacks.** Put a system stack after the web font, with `font-display: swap` and `font-size-adjust: from-font` so a fallback doesn't change the apparent size.
7. **Test on the weakest devices, not just the designer's Mac.** Before you sign off, use your office monitor, your dad's tablet, and a dark-background version of the page. Light text on dark looks bolder, so you may need to step the weight down there.

Tell the designer to check the design on a low-density screen. Something that is crisp only on Retina is not finished. If you share the font name and the CSS weights you use for body text, I can say which of these applies and suggest a specific replacement.
