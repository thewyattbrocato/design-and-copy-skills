**What's going on:** "Helvetica Neue" is installed on Apple devices only. Your CSS asks for a font the visitor's device has to already own. Nothing is downloaded, so each device uses the first font in your stack that it has.

- **MacBook:** It has Helvetica Neue, so the designer sees the font the design was made in. macOS also renders text a bit heavier and smoother.
- **Windows PC:** It doesn't have Helvetica Neue, so it falls to the next name in the stack. That is usually Arial, or Helvetica, which Windows maps to Arial. Windows (DirectWrite/ClearType) also draws strokes thinner and sharper, so the same font looks lighter and rougher. If the design uses light weights (300 or below), this gets worse.
- **Old Android tablet:** It has neither Helvetica Neue nor Arial. It drops to the stack's generic fallback, which is Roboto, an older Droid font, or the manufacturer's own font. If the stack ends without a generic `sans-serif`, you can even get a serif. Headings often differ most because they use weights (500 to 600, or light) that the fallback font doesn't have. The browser then fakes them or picks a nearby weight.

I haven't seen your CSS, so this is the standard explanation. Check the real stack and the heading weights to confirm it.

**Fix before launch:** Stop depending on installed fonts.

1. **Ship a web font.** Pick an open-license family with the weights you use, and self-host it as WOFF2 (two to four files, subset to the languages you need). Use `font-display: swap` and preload the main file. Confirm the license covers web use. If the designer needs Helvetica Neue specifically, that's a commercial license to confirm with the foundry.
2. **Give it a real fallback.** For example: `"YourWebFont", system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif`. Each device then lands on a sturdy native UI font, not whatever happens to match.
3. **Avoid hairline weights for body text.** Keep body at 400 or heavier, and use light weights only for large headings. This matters most on Windows.
4. **Use only weights the family really has.** Faux bold and italic are what make headings look wrong on fallback fonts.

**What to test:**

- **Devices:** Windows with Chrome, Edge and Firefox. Include a standard-density monitor, not only a high-DPI laptop. Also test Safari on Mac and iPhone, a current Android phone, and the old tablet.
- **Font loading:** Throttle the network to Slow 3G and block the font file. Check that text appears immediately in the fallback, that nothing is invisible, and that the layout doesn't jump when the font swaps in.
- **Fallback look:** Temporarily remove the web font and compare. Headings and body should still look acceptable, and line breaks shouldn't change much.
- **Weights and styles:** Check every weight and italic used. Headings, buttons, and small labels at the smallest size are the usual trouble spots.
- **Real content:** Use real paragraphs, numbers and any non-English text. Check that accented and non-Latin characters don't switch to a different font.
- **Browser settings:** Test with browser zoom, large system text, and Windows text scaling.

If you paste the `font-family` lines and the heading weights, or point me at the stylesheet, I can say which fallback each device is hitting and write the replacement stack.
