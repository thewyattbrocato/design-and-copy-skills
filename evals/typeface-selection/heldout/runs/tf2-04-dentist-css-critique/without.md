Parents are right on both counts. Here's what's wrong, roughly in order of impact.

## Why it feels chaotic

1. **Five typefaces plus Courier New.** Lobster (script), Playfair Display (high-contrast serif), Montserrat and Raleway (two similar geometric sans fonts), Comic Neue (casual), and Courier New (monospace). Nothing ties them together. Montserrat and Raleway are close enough to look like a mistake rather than a choice.

2. **Lobster as the body font.** This is the worst problem. Lobster is a heavy display script, and here it sets all paragraph text at 13px with 1.2 line height in mid-gray (#666). That's hard to read for anyone, and parents skimming on a phone are the main audience. Body text should be a plain, readable face at 16px or larger.

3. **Tiny, thin, low-contrast text.**
   - Nav links are Raleway at weight 200 and 12px. Hairline strokes at that size nearly disappear, and the nav is how people find things.
   - #666 on white is about 5.7:1, which passes. But it's weak once you pair it with thin or script type.
   - h2s at weight 100 with 4px letter-spacing in all caps are a fashion-magazine look. They're faint and hard to scan.

4. **Courier New for prices and hours.** These are the facts parents most want to find, and they're set in a system typewriter font that clashes with everything else.

5. **The h1 doesn't match anything.** Playfair at weight 900 and 44px is a heavy editorial voice sitting on top of a script body. The tone is inconsistent: boutique, then bubbly, then typewriter.

6. **Comic Neue on buttons.** It's a Comic Sans cousin. A little playfulness suits a pediatric practice, but only the buttons have it, so it reads as random.

## Why it loads slowly

1. **`@import` inside CSS.** The browser has to download the CSS file, find the `@import`, then fetch the Google Fonts stylesheet, and only then fetch the font files. That's a serial chain, and it blocks rendering. Use `<link rel="preconnect">` and a `<link rel="stylesheet">` in the HTML head instead, or self-host.

2. **Far too many font files.** Counting the weights you request:
   - Playfair Display: 3
   - Montserrat: 7
   - Raleway: 3
   - Lobster: 1
   - Comic Neue: 1

   That's roughly 15 files, and you actually use only about 6 combinations (Lobster 400, Playfair 900, Montserrat 100, Raleway 200, Comic Neue 400, plus whatever the browser synthesizes for bold). Montserrat 200–700 and Raleway 100/300 are downloaded and never used. Playfair 400 and 700 are likely unused too.

3. **`display=block`.** This hides all text for up to about 3 seconds while fonts load. On a slow mobile connection, parents see a blank page. Use `display=swap` (or `optional`), and ideally a metric-matched fallback to limit layout shift.

4. **The URL has a bug.** `Comic+Neue` followed by `&display=block` is fine syntactically, but with no weight spec you only get 400. If anything on the site uses bold Comic Neue (buttons often do), the browser will fake the bold, which looks smeared.

5. **Missing fallbacks.** `'Montserrat'`, `'Raleway'`, and `'Comic Neue'` have no generic fallback, so if they fail the browser picks its default serif.

## What I'd do

Pick **two** families at most, one for headings and one for body, and use real weights for hierarchy.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;700&family=Fredoka:wght@500;600&display=swap">
```

```css
body {
  font-family: 'Nunito', system-ui, sans-serif;
  font-size: 17px;
  line-height: 1.6;
  color: #333;
}
h1, h2, .btn {
  font-family: 'Fredoka', 'Nunito', system-ui, sans-serif;
}
h1 { font-size: 2.5rem; font-weight: 600; line-height: 1.15; }
h2 { font-size: 1.5rem; font-weight: 500; }
nav a { font-size: 1rem; font-weight: 700; }
.price, .hours { font-weight: 700; font-variant-numeric: tabular-nums; }
```

Nunito and Fredoka are rounded and friendly, which fits a kids' dental practice, and they cost 4 font files instead of 15. Use whichever pair fits your brand. The point is two families, readable sizes, and `display=swap`.

Fonts are likely not the only cause of the slowness. Check image sizes, third-party scripts, and whether there's any render-blocking JavaScript. If you send me the page or a Lighthouse report, I can look at those too.
