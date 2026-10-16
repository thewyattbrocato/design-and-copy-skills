# What's going on

"Helvetica Neue" is a system font, not a web font. The browser uses whatever the visitor's device has installed, then falls through the stack. You're seeing three different outcomes of that.

**MacBook (crisp):** Helvetica Neue ships with macOS and iOS, so the designer sees the intended font. macOS also renders text with grayscale antialiasing and slight stem-darkening, which makes text look heavier and smoother.

**Windows PC (thinner, rougher):** Windows doesn't ship Helvetica Neue, so you're probably getting the next font in the stack. That is often Helvetica, which Windows maps to Arial, or Arial itself. Even when the same font is present, Windows renders it differently. DirectWrite/ClearType hints glyphs to the pixel grid and renders thinner strokes, especially on lower-DPI monitors. Some of what you see is the font swap and some is the renderer, and you can't fully fix the renderer part.

**Old Android tablet (different headings):** Android has no Helvetica Neue either. It falls to `sans-serif`, which is Roboto, or to a manufacturer default. Old devices may also lack the weight you specified (for example 300 or 500), so the browser picks the nearest weight or synthesizes bold. If the stack has no generic fallback at the end, the browser can even land on a serif font.

# The fix

Self-host or load a web font (WOFF2) so every device gets the same file. Options include Inter, or a licensed Helvetica Neue from a foundry or Adobe Fonts if the brand requires it. Keep system fonts only as fallbacks. For example:

```css
font-family: "Brand Font", "Helvetica Neue", Arial, system-ui, sans-serif;
```

Also add:
- `font-display: swap` (or `optional`) so text shows while the font loads.
- A `size-adjust` or `ascent-override` fallback face to limit layout shift when the font swaps in.
- Only the weights you actually use. Missing weights cause synthesized bold and inconsistent thickness.

# What to test before launch

1. **Real devices, not just emulators:** Windows (at least one 1080p non-retina screen and one high-DPI), an older Android phone or tablet, an iPhone, and a Mac. Check Chrome, Safari, Firefox, and Edge.
2. **Font actually loaded:** In DevTools, open Elements → Computed → Rendered Fonts. It shows which font each element really uses, so you can spot silent fallbacks.
3. **Network conditions:** Throttle to Slow 3G and look for flash of invisible or unstyled text and for layout shift. Also test with the font request blocked, to see how the fallback looks.
4. **Weights and styles:** Confirm that every weight and italic in the design exists as a loaded file.
5. **Fallback quality:** Temporarily remove the web font and check that the layout holds, with no overflow, awkward wrapping, or broken buttons.
6. **Text rendering:** Check body text size and contrast on Windows. Thin weights (300 and below) look worst there, so consider bumping body text to 400.
7. **Licensing and CORS:** Confirm the font license covers web use and that the font files are served with correct headers (`Access-Control-Allow-Origin` if they're on a CDN).
8. **Performance:** Preload the key font file, serve WOFF2, subset it if possible, and check Lighthouse/CLS.

Expect the Windows version to still look slightly lighter than the Mac even with the same web font. That is the renderer, and designers should review on Windows too so they aren't judging the design only by the Mac's rendering.
