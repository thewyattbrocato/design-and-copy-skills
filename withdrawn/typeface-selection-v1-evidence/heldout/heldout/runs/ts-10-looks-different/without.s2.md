**Short version:** "Helvetica Neue" isn't a web font. It's a font that ships with macOS and iOS, and each device is showing whatever it has.

**What's happening**
- **MacBook:** It has Helvetica Neue, so you see the intended design. macOS also renders text with heavier, smoother antialiasing, which makes everything look crisp and slightly bolder.
- **Windows PC:** It doesn't have Helvetica Neue, so the browser falls to the next font in your stack. That is probably Helvetica, which Windows maps to Arial, or Arial itself. Windows also renders text differently (DirectWrite/ClearType), and light weights look thinner and rougher, especially on a standard-DPI monitor. If your headings use weight 300 or lighter, Arial has no such weight, so you get a substitute or a synthesized one.
- **Old Android tablet:** It has neither font. If your stack ends in a generic family like `sans-serif`, you get Roboto or the device default. If it doesn't, you can get the browser's default serif, which would explain headings that look totally different.

**The fix**
1. Self-host a licensed web font as WOFF2 with `@font-face`, and use `font-display: swap`. Helvetica Neue is commercially licensed, so you can't legally serve it from your site without a web license. Inter, or a Helvetica-like font you have licensed, is the usual choice.
2. Make the fallback stack deliberate and end it with a generic family, for example: `"YourWebFont", -apple-system, "Segoe UI", Roboto, Arial, sans-serif`.
3. Reduce layout shift while the font loads. A fallback face with `size-adjust` and `ascent-override` can match the web font's metrics.
4. Only use weights you actually load. Don't ask for 300 if you ship 400 and 700.

**What to test before launch**
- **Which font is rendering:** Open Chrome DevTools, go to Elements, then Computed, then Rendered Fonts. Check this on every device. In the Network tab, confirm the font files load with a 200 status, with correct CORS and cache headers.
- **Windows:** Test Chrome, Edge and Firefox. Try display scaling at 100%, 125% and 150%, and on both a low-DPI and a high-DPI monitor.
- **Android:** Test an old version and a recent one, in both Chrome and the stock browser or Samsung Internet if you have them.
- **iOS Safari and macOS Safari**, to check that the web font looks the same as Helvetica Neue did.
- **Weights and styles:** Look at every heading weight, italics and bold for synthesized "faux" styles.
- **Loading behavior:** Throttle the network to Slow 3G. Look for flashes of unstyled text, layout shift and invisible text.
- **Fallback:** Block the font file and confirm the page still looks acceptable.
- **Legibility:** Check contrast and small text on Windows, where thin text suffers most.

Expect the web font to make fonts consistent across devices, but not rendering. Windows will still draw text a bit lighter than macOS. If it looks too thin there, bump body weight slightly, for example from 300 to 400.
