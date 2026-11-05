The setup is the problem, not any one font. It has five competing voices and a heavy, blocking load, and the text parents need to read is set in the hardest-to-read faces.

## What's wrong

**Chaos**
- **Five families with no roles.** Lobster (script) is the body, Playfair Display (high-contrast serif) is h1, Montserrat is h2, Raleway is nav, and Comic Neue is buttons. Courier New for prices and hours makes six. Nothing connects them, so the page looks chaotic.
- **A script face as body text at 13px with 1.2 leading.** Lobster is a display face. Set small and tight, it's tiring to read, and it's the main text on a page parents use to find hours and book visits.
- **Hairline weights for text.** Raleway 200 at 12px for nav and Montserrat 100 in spaced-out caps for h2 will look thin and blurry on ordinary screens. Navigation is where parents need to click.
- **Faces that mimic the subject.** Comic Neue buttons and the Lobster body are trying to read as "kid-friendly". That reads as a joke next to a 900-weight Playfair headline, not as warmth.
- **Courier New for prices and hours.** Monospace is for code. Here it looks like a typewriter dropped into a medical site. It's also a thin system font, and it has no fallback.

**Slow load**
- **`@import` inside the CSS.** The browser has to download the CSS, then discover the font CSS, then fetch the fonts. That's a serial chain before anything renders.
- **About 14 weights requested across four families, and most go unused.** You load Montserrat 100–700 but use only 100. You load Raleway 100–300 but use only 200. You load Playfair 400/700/900 but use only 900.
- **`display=block`.** Text stays invisible for up to about 3 seconds while those fonts load. That's probably a big part of "slow".
- **No real fallbacks.** `'Montserrat'`, `'Raleway'`, `'Comic Neue'` and `'Courier New'` have no generic family after them. If a font fails, the browser uses its default serif.

**What works:** nothing here is worth keeping as-is. The idea of a display face for h1 is fine, but only one face should play that role.

## Fix

One family with real weight range, and no second family. Nunito is a variable font with rounded terminals, so it's friendly without being a novelty face. I haven't verified its license or script coverage, so confirm those before launch. If you want a distinct h1, add one display face for that line only.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@400..800&display=swap">
```

```css
:root {
  --font: 'Nunito', ui-rounded, system-ui, -apple-system, 'Segoe UI', sans-serif;
}
body { font-family: var(--font); font-size: 17px; line-height: 1.55; color: #444; }
h1   { font-weight: 800; font-size: 40px; line-height: 1.15; }
h2   { font-weight: 700; font-size: 26px; line-height: 1.25; } /* drop uppercase and the 4px tracking */
nav a { font-weight: 600; font-size: 16px; }
.price, .hours { font-weight: 600; font-variant-numeric: tabular-nums; }
.btn { font-weight: 700; font-size: 16px; }
```

The starting sizes are my suggestions, so check them on a real phone. The stack now ends in real system fallbacks, and it no longer uses `@import`, hairline weights, monospace or `display=block`.

**Next steps**
1. Test with the font blocked, to see the fallback.
2. Check that 1/l/I and 0/O are distinct in prices and hours at 16px.
3. Once it works, self-host two or three font files with a preload for the main one. That's faster still, but it's a second step.

If the practice has a brand font or logo typeface, tell me and I'll build the stack around it.
