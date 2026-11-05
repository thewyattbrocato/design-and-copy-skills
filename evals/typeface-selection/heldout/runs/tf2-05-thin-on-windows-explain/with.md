**Why it happens**

The CSS and font files are identical, but the rasterizer and the screen are not.

- **Pixel density.** A MacBook Retina display has about 220 ppi and renders at 2x. A typical office monitor is around 90–110 ppi, and an old tablet may be similar or worse. A 1px stem that is smooth on Retina has to snap to whole pixels on the lower-density screens. That produces stems that are too thin or too heavy, and curves that look jagged.
- **Different renderers.** macOS smooths glyphs with grayscale antialiasing and doesn't snap them to the pixel grid. It also tends to make strokes a little heavier. Windows uses DirectWrite with hinting, and sometimes ClearType subpixel rendering. It keeps shapes closer to their true outline, so thin strokes look thinner and sharper. Android varies by device, and old tablets often have weak hinting and low-quality rendering.
- **Delicate fonts suffer most.** Light weights, hairline strokes and high-contrast faces break up first on low-density screens. A regular-weight face with moderate contrast usually looks fine on all three.
- **A mismatched file can make it worse.** If the web font is an unhinted or auto-hinted conversion, or a different format than the designer's installed copy, Windows may render it differently. Check whether the designer has the font installed locally. Then her Mac would be using the local copy instead of your web files.

**What to do**

1. **Test the way your dad and you see it.** Use a real paragraph at the smallest size you ship, on the real background. Check it on a low-density Windows screen and a mid-range Android device. Don't judge it on the Mac alone.
2. **Check the weight first.** If body text is a Light, Thin or hairline cut, move it to Regular (400) or a sturdier cut. Keep the light weights for large headlines, roughly 40px and up. This is the most likely fix. Change it before you touch any CSS.
3. **Prefer a lower-contrast, sturdier face for body and UI.** Look for open apertures and a larger x-height. If the brand face is delicate, keep it for headings and pair it with a sturdy sans or text serif for small text.
4. **Keep small text at 12px or larger, in regular weight or heavier.** If 12px looks weak, change the face before you raise the size.
5. **Check the font files.** Confirm the site serves the files you think it does, with the weights you use. Make sure it isn't faking bold or italic, because synthesized styles look rough on low-density screens. Also confirm the designer isn't previewing a locally installed copy. If you self-host, use properly hinted WOFF2 files, or ask the foundry or font vendor for web-optimized builds.
6. **Don't use `-webkit-font-smoothing` to "fix" Windows.** It only affects macOS. Windows and Android rendering is mostly out of your control, so the fix is choosing the right weights and faces.
7. **Check dark backgrounds separately.** Light text on dark looks bolder, so step down a weight there.

The designer's Mac is the most forgiving screen your users will have. The goal is to make the text hold up on the worst of them.

If you tell me which font and weights you're using, I can suggest a specific sturdier cut or pairing.
