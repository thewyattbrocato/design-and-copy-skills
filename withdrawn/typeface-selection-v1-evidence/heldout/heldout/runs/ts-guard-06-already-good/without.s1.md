I'd fix a few things before this goes out. I couldn't find a file for it, so the corrected CSS is below.

```css
:root {
  --font-body: Georgia, Cambria, 'Times New Roman', serif;
  --font-ui: system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  --font-mono: ui-monospace, Menlo, Consolas, 'Courier New', monospace;
}
body {
  font-family: var(--font-body);
  font-size: 1.125rem;
  line-height: 1.6;
}
main, article { max-width: 65ch; }

nav, button, label, input, select, textarea, .meta { font-family: var(--font-ui); }

code, pre { font-family: var(--font-mono); font-size: 0.9em; }
pre code { font-size: inherit; }

h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-ui);
  font-weight: 600;
  line-height: 1.2;
  letter-spacing: -0.01em;
}
```

**What changed and why**

1. **`font-weight: 650` is now `600`.** 650 only renders as written if the font is variable. Most system-ui stacks (Segoe UI, Roboto, Helvetica Neue, Arial) snap it to 700 or 400 unpredictably, so the heading weight would differ from machine to machine. 600 maps predictably.
2. **Headings now have `line-height: 1.2`.** They were inheriting the body's 1.6, which looks loose and gappy on multi-line headings at large sizes.
3. **`pre code { font-size: inherit }` is new.** Without it, `code` inside `pre` gets 0.9em twice, which is about 0.81em. Code blocks would come out noticeably smaller than inline code.
4. **Headings now cover `h4`–`h6`.** Otherwise they fall back to the serif body font and look inconsistent with `h1`–`h3`.
5. **`select` and `textarea` are added to the UI font rule.** Form controls don't inherit fonts, so they'd render in the browser default.
6. **There's a new `max-width: 65ch` on `main, article`.** For a long-form essay site, 1.125rem text with no measure limit runs lines far past a comfortable ~60–75 characters on wide screens. Change the selector to match your markup, or drop it if you set the width elsewhere.

**Left alone, but worth knowing**
- Sans headings over a serif body is a legitimate pairing. I assumed it's intentional.
- Cambria is effectively dead weight in the body stack, since Georgia is on both macOS and Windows. It's harmless.
