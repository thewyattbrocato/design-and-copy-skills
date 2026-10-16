**Cause:** Helvetica Neue is a system font on Apple devices only. It isn't installed on Windows or on most Android devices. Unless you load it as a web font, which also needs a license, each device substitutes whatever your stack names next. Your designer is seeing the font you chose. You and your sister are seeing fallbacks.

**Windows (thinner, rougher):**
- If your stack lists Arial, Windows uses it. Arial has different proportions and weights from Helvetica Neue.
- Windows also renders text differently. ClearType and hinting give thinner, sharper-edged strokes, while macOS smooths and slightly thickens them. A Retina display hides the roughness, and many Windows monitors are lower density.
- If you use light weights (300 or lighter), they look much worse on Windows. Helvetica Neue Light exists on the Mac, but a fallback may not have that weight. The browser then picks the nearest one or fakes it.

**Android tablet (different heading font):**
- This usually means the heading rule has a different stack, or a stack with no generic fallback such as `sans-serif`. The browser then uses its default, often a serif.
- Another cause is a web font that failed to load, for example a blocked file, a wrong path, or a missing weight. Check that headings aren't using a weight you never loaded, such as 600 when you only shipped 400 and 700. That can trigger faux bold or a swap to another font.
- Old tablets also have older WebView and Chrome versions. They may not support WOFF2 or variable fonts.

**Fix:**
1. Stop depending on fonts that only some machines have. Either self-host one licensed or open-license family as WOFF2, or use a system stack on purpose. A system stack would be `system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`.
2. If you self-host, ship only the weights you use, which is usually 2–4 files. Use `font-display: swap` and preload the critical file. Confirm the license covers web use.
3. Every `font-family` rule, headings included, should end in a real fallback and `sans-serif`.
4. Use regular weight or heavier for body text. Avoid 300 and below on Windows.
5. Don't rely on faux bold or italic. Load the real styles, or don't use them.

**Test before launch:**
- **Real devices:** Windows 10/11 in Chrome, Edge and Firefox, ideally on both a standard and a high-density monitor. Also test macOS Safari, iPhone, a current Android phone, and the old tablet.
- **Fallback behavior:** In DevTools, block the font files and throttle the network. Check that the page still looks acceptable, that text is never invisible, and that layout doesn't jump when the font swaps in.
- **Rendered font:** In DevTools, open Elements, then Computed, then Rendered Fonts. Check this for headings and body on each device. Don't assume the named font is the one showing.
- **Weights and styles:** Check every weight, italic and bold in use, and look for synthesized (faux) styles.
- **Small text:** Read a real paragraph at the smallest size on the real background. Check dark mode and any language or accented characters you support.
- **Numbers and look-alikes:** Check that digits, and I, l, 1, O, 0, are distinguishable where it matters, such as prices.
- **Browser settings:** Test with browser zoom and with a larger default font size.

Send me the CSS, or the project folder, and I can check the actual stacks and weights against this list.
