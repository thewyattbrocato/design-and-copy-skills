**What's going on**

Helvetica Neue is a font installed on Apple devices. Windows and Android don't ship it, and your site doesn't load it. So the designer saw the intended font, and you and your sister saw whatever each device substituted. The page isn't broken. Nobody has designed the non-Apple experience yet.

- **Windows PC:** the stack most likely fell through to Helvetica, which Windows maps to Arial, or to Arial directly. That's a different typeface. Windows also renders text differently from a Retina MacBook. Its ClearType/DirectWrite rendering gives thinner, sharper-edged strokes, and on a standard-density monitor it looks rougher. Part of the gap is the screen and renderer, and no font choice will remove it.
- **Old Android tablet:** it has no match for any named font, so it uses its own default, usually Roboto. If the headings look *different from the body* too, check that the heading stack ends in a generic family such as `sans-serif`. Without one, some browsers fall back to a serif default. I haven't seen your CSS, so this is a guess.

**What to do**

1. **Pick a font that loads everywhere, and stop depending on a system font.** Self-host a sans with real weight range (an open-license option like Inter is a common choice, but confirm the license terms yourself). Subset it, use `font-display: swap`, and preload the main file. Or, if you don't need a brand look, use a system UI stack and accept that each platform looks native.
2. **Keep a real fallback chain after it,** for example `"Your Web Font", system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif`. Put `sans-serif` at the end of every role's stack, headings included.
3. **Don't use light weights for body text.** Thin weights hold up on Retina and fall apart on standard-density Windows screens. Use a regular (400) or sturdier weight for body, and keep light weights for large headings.
4. **Load the real bold and italic.** If you only load regular, browsers fake the bold, and that looks rough.

**What to test before launch**

- **Devices:** Windows with Chrome, Edge and Firefox, ideally on both a standard-density monitor and a high-DPI laptop. Also macOS Safari, iPhone Safari, a recent Android phone, and the old tablet as your worst case.
- **Fallbacks:** block the web font in DevTools (Network tab) and reload. Check that the page still looks acceptable and that the layout doesn't jump when the real font arrives.
- **Text:** read a real paragraph at your smallest size, not just the headings. That's where Windows weakness shows up first.
- **Weights and styles:** check every weight and italic you use, and look for faux bold.
- **Characters:** check numbers, currency symbols, and any non-English text or accents your audience uses. A missing glyph triggers a mismatched substitute font.
- **Loading:** throttle the network to "Slow 3G" and confirm there's no invisible text while the font loads.
- **Zoom and display settings:** test at 125% and 150% Windows scaling, and with browser text zoom.

If you paste your `font-family` rules, I can check the stacks and write the fixed versions. If the project is in a folder I can read, point me to it.
