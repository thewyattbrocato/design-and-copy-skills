The setup is a pile of unrelated faces, and several of them are doing jobs they can't do. That explains both complaints.

## Why it feels chaotic

- **Six families with no roles.** You have Lobster, Playfair Display, Montserrat, Raleway, Comic Neue and Courier New. A script face, a high-contrast display serif, two geometric sans faces, a casual comic face and a typewriter face each pull in a different direction. Nothing reads as one brand.
- **Body text is in Lobster at 13px with 1.2 line height.** Lobster is a heavy display script. At body size it's slow to read, and the tight leading makes paragraphs clump. 13px is also too small for parents reading on phones. This is probably the biggest cause of the "chaotic" feeling.
- **Montserrat and Raleway are near twins.** Pairing two similar geometric sans faces looks like a mistake, not a choice.
- **Hairline weights.** `h2` is Montserrat 100 in caps with 4px tracking, and the nav is Raleway 200 at 12px. Both strokes break up or vanish on ordinary screens, and the nav is the part people need to find.
- **The buttons are in Comic Neue and the prices and hours are in Courier New.** The buttons clash with everything else. Courier is a monospace face used for "flavor" on the information parents look up most (hours, prices).
- **Three of the font names have no fallback.** `'Montserrat'`, `'Raleway'` and `'Comic Neue'` end with no generic family. If any of them fails to load, the browser drops to its default serif.

## Why it loads slowly

- **`@import` inside CSS.** The browser has to download your stylesheet, then the Google stylesheet, then the font files, one after another.
- **You request far more than you use.** You ask for 7 Montserrat weights but use one (100). You ask for 3 Raleway weights but use one (200). You ask for 3 Playfair weights but use one (900). Every extra weight costs download time.
- **`display=block`.** Text stays invisible for up to a few seconds while fonts load. On a slow phone connection, parents see a blank page. Use `swap` or `optional`.
- **Third-party hosting.** Every visit makes extra connections to Google's servers. Self-hosting removes that, and it's also better for visitor privacy.

## What I'd do instead

One friendly, rounded family with real weight range covers everything. That fits a pediatric practice without resorting to Comic Neue or script faces. I'm assuming a screen-only site, Latin text, and a free font. I picked Nunito, which is on Google Fonts under an open license. Confirm the license terms before you ship it.

```css
@font-face {
  font-family: 'Nunito';
  src: url('/fonts/nunito-var.woff2') format('woff2');
  font-weight: 400 800;
  font-display: swap;
}

:root {
  --font: 'Nunito', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}

body { font-family: var(--font); font-size: 17px; line-height: 1.6; color: #333; }
h1   { font-weight: 800; font-size: clamp(2rem, 5vw, 2.75rem); line-height: 1.15; }
h2   { font-weight: 700; font-size: 1.5rem; line-height: 1.25; }  /* no caps, no tracking */
nav a { font-weight: 600; font-size: 1rem; }
.btn { font-weight: 700; }
.price, .hours { font-variant-numeric: tabular-nums; }  /* same face, not Courier */
```

Also:
- **Self-host and subset.** Serve one variable `woff2` file and preload it.
- **Darken the text.** I changed `#666` to `#333`. Gray body text on white is borderline, especially with thin strokes.
- **Keep any personality big and short.** If you want a playful touch, use a display face for the logo or the h1 only, never for body text or buttons.

I haven't looked at the live site. If parents still call it chaotic after this change, check the colors and spacing next.
