The CSS and font files are the same on every device, but the text is drawn differently on each one.

## Why it happens

1. **Pixel density.** A MacBook Retina screen has about 220 ppi and uses 2× pixels. A typical office monitor is around 96 ppi at 1×, and an old tablet is often low-res too. A thin stroke that spans several pixels on the Mac gets about one pixel on the other screens, so the curves turn into stair-steps and look jagged.
2. **Different rasterizers.** macOS fattens glyphs slightly when it draws them, and it doesn't snap them to the pixel grid. That gives the soft, slightly heavier look. Windows (DirectWrite/ClearType) snaps stems to whole pixels and doesn't add weight, so the same weight looks thinner and sharper-edged. Android varies by device and version, and old tablets are usually the worst.
3. **Light weights and high-contrast faces suffer most.** A light, hairline or high-contrast face looks elegant on Retina. On a low-density screen its thin strokes drop out or break up. This is the most likely cause if your body text is a light weight (300 or below) or a thin geometric or Didot-style face.
4. **Possible file mismatch.** If the web font files are unhinted, or if only one weight is loaded and the browser fakes the others, Windows and Android will look worse. Check this too.

## What to do

1. **Test on the bad screens first.** Look at a real paragraph at its smallest size on the Windows monitor and the old tablet. Don't judge from the Mac.
2. **Change the weight and face before the CSS.**
   - Set body text to regular (400) or heavier, not light.
   - If the face is thin or high-contrast, use it only for big headlines, at about 40px or larger. Give body text and UI a sturdier, lower-contrast partner with open apertures and a larger x-height.
3. **Check the weights.** Make sure every weight you use (regular, medium or semibold, bold, true italic) is actually loaded. If any is missing, the browser fakes it, so remove the synthesis or add the real file.
4. **Check the web font files.** Confirm the fonts are loading (DevTools → Network or Computed → Rendered Fonts) and aren't silently falling back to something else. If you control the files, use a build that's hinted for Windows. Most well-made open fonts are, and a foundry can confirm for a commercial one.
5. **Don't try to force the Mac look.** Avoid `-webkit-font-smoothing: antialiased`. It only affects macOS and makes the text thinner there. A 400 weight at a reasonable size (16px or larger for body) also helps.
6. **If you have light text on dark backgrounds,** step the weight down one notch. Light-on-dark looks bolder, so the same weight doesn't need to be as heavy.

If you tell me which font and weights the site uses, I can tell you which of these is the likely culprit and suggest a replacement or pairing. I haven't looked at your code, so these are the usual causes. I haven't confirmed which one applies to you.
