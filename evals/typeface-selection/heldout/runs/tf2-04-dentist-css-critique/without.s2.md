Your parents are right on both counts. The setup has several separate problems.

**Why it feels chaotic**

1. **Five font families on one page.** Lobster (script), Playfair Display (high-contrast serif), Montserrat and Raleway (two similar geometric sans-serifs), Comic Neue (casual), and Courier New (typewriter). Each one has a different personality, so nothing looks like it belongs with the rest. Montserrat and Raleway are near-duplicates, so using both adds noise and no contrast.
2. **Lobster as the body font.** This is the worst choice here. A decorative script at 13px is hard to read in paragraphs, and parents skimming hours, insurance info, or appointment details will struggle. Display fonts like Lobster work for a logo or one short headline.
3. **Body text is too small and cramped.** 13px with `line-height: 1.2` is below the usual 16px minimum, and the line height is tight. The `#666` gray on white is about 5.7:1 contrast, which passes. But it's weak for small, thin text, and the thin text below makes it worse.
4. **Hairline weights at small sizes.** Nav links are Raleway 200 at 12px, and h2s are Montserrat 100 with 4px letter-spacing in all caps. These are thin, tiny, and hard to read, especially on phones and in bright light. The h2 setup is also hard to scan.
5. **No consistent hierarchy.** The h1 is a heavy 900 serif at 44px. The h2 is a hairline uppercase sans. The body is a script. Each level is a different style, so the page doesn't read as one system.
6. **Comic Neue on buttons** looks like a leftover from a different design. Courier New on prices and hours looks like a system default, not a choice.

**Why it loads slowly**

1. **Too many weights.** The URL requests 3 Playfair weights, 7 Montserrat weights, 3 Raleway weights, plus Lobster and Comic Neue. That's about 15 font files. You actually use roughly 5 combinations: Lobster 400, Playfair 900, Montserrat 100, Raleway 200, and Comic Neue 400. Montserrat 200–700 and Playfair 400/700 are never used.
2. **`@import` inside CSS.** The browser has to download and parse the CSS file before it discovers the Google Fonts request, which then needs another round trip for the font files. A `<link>` in the HTML head, with `preconnect`, avoids that chain.
3. **`display=block`.** This hides text for up to about 3 seconds while fonts load, so on a slow mobile connection parents see blank space. Use `display=swap` (or `optional`) so text shows right away.
4. **Courier New** isn't loaded, so it's fine for speed. But it's a system font that varies by device, which adds to the inconsistency.

**What I'd do**

- Use **two families at most**. For example, one friendly rounded heading font (Nunito, Fredoka, or Baloo 2) and one clean body font (Nunito Sans, Inter, or Open Sans). Or a single family with several weights.
- Keep Lobster only if it's part of the logo, and then load it only for that, or better, use the logo as an image or SVG.
- Set body text to **16–18px**, `line-height: 1.5–1.6`, and a darker color such as `#333`–`#444`.
- Make nav links at least 15–16px, weight 500 or higher. Make h2s sentence case, weight 600–700, with no extreme letter-spacing.
- Load only the weights you use (e.g. 400, 600, 700), and use `display=swap`.
- Move the font request to `<link>` tags in the HTML, with `preconnect` to `fonts.googleapis.com` and `fonts.gstatic.com`. Or self-host the WOFF2 files, which is faster and avoids a third-party request.
- Use the same font for buttons, prices, and hours as for the rest of the page. If you want aligned numbers for prices, use `font-variant-numeric: tabular-nums`.

A sketch of the cleaned-up version:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;800&display=swap" rel="stylesheet">
```

```css
body { font-family: 'Nunito', system-ui, sans-serif; font-size: 17px; line-height: 1.6; color: #333; }
h1 { font-weight: 800; font-size: clamp(32px, 5vw, 44px); line-height: 1.15; }
h2 { font-weight: 700; font-size: 28px; }
nav a { font-weight: 600; font-size: 16px; }
.price, .hours { font-variant-numeric: tabular-nums; }
.btn { font-weight: 700; }
```

That drops the page from about 15 font files to 3, removes the render-blocking chain and the invisible-text delay, and gives it a friendly look that still suits a kids' dental practice. If you share the actual page or repo, I can check what else is slowing it down, such as images and scripts.
