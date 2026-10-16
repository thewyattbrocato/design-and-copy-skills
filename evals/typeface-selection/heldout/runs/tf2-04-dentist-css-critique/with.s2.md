The setup is chaotic because it has six typefaces and no roles for them. It's slow because of how they're loaded.

## What's wrong

**Why it feels chaotic**
- **Six families, none with a job.** Lobster, Playfair Display, Montserrat, Raleway, Comic Neue and Courier New each take a different role. A page with this many voices reads as noise, and parents pick up on that.
- **Lobster is the body font.** It's a script display face, and here it sets every paragraph at 13px with 1.2 line height in mid-gray. That's the most damaging choice. Script is hard to read at length, 13px is too small, and 1.2 leading is too tight for body text. Lobster also has only one weight and no italic, so any `<strong>` or `<em>` is faux-bolded or faux-slanted by the browser.
- **Hairline weights.** The `h2` uses Montserrat 100, uppercase, with 4px tracking. The nav uses Raleway 200 at 12px. Those strokes get thin or blurry on ordinary screens, especially phones. Nav links are what a worried parent is hunting for.
- **Courier New for `.price` and `.hours`.** This is the information parents most need, and it's set in a typewriter face. Monospace is for code. Use a sturdy face with tabular figures for prices and hours.
- **Comic Neue on buttons.** It's a novelty face matched to the subject ("kids!"). It makes the main call to action look unserious next to a Playfair 900 headline. Kid-friendly should come from warmth and color, not a joke font.
- **Two display-weight faces collide.** Playfair 900 and Lobster are both loud, and nothing calm sits between them.

**Why it's slow**
- **`@import` inside CSS** makes the browser download the stylesheet, then discover and fetch the Google CSS, then fetch the font files. That chain blocks rendering. A `<link>` with `preconnect`, or self-hosting, avoids it.
- **You request far more than you use.** That's 3 Playfair weights (only 900 is used), 7 Montserrat weights (only 100 is used on `h2`), 3 Raleway weights (only 200 is used) and several others. Each unused weight is a wasted download.
- **`display=block` hides all text for up to about 3 seconds** on slow connections. On a phone in a waiting room, that's a blank page. Use `swap` or `optional`.
- **Bad fallbacks.** `Montserrat`, `Raleway` and `Comic Neue` have no fallback at all, and `Courier New` has no `monospace`. If a font fails to load, you get the browser default serif. Lobster's `cursive` fallback varies wildly by device, and on some it's Comic Sans.

## Fix

Use one family with real range, plus at most one display face for the `h1`. I'd use Nunito. It's rounded and friendly without being a gimmick, and it works for body text, UI and numbers. It's a variable font, so one file covers every weight. I believe it's open-licensed, but confirm that before you ship it.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet"
  href="https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,400..800;1,400..800&display=swap">
```

```css
:root {
  --font: 'Nunito', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
body {
  font-family: var(--font);
  font-size: 17px;          /* 16–18px for body */
  line-height: 1.55;
  color: #3a3a3a;           /* darker than #666 */
}
h1 { font-weight: 800; font-size: 44px; line-height: 1.1; }
h2 { font-weight: 700; font-size: 28px; }   /* drop the uppercase hairline */
nav a { font-weight: 600; font-size: 16px; }
.price, .hours { font-variant-numeric: tabular-nums; font-weight: 600; }
.btn { font-weight: 700; font-size: 17px; }
```

Better still, self-host the file as WOFF2, subset to Latin, and preload it. That removes the third-party round trip entirely.

If the brand wants more personality, keep Lobster for the logo or one short tagline. Don't use it for text.

**Assumptions:** this is a Latin-script, screen-only site, and no brand font is mandated. If a designer has locked in Lobster or Playfair as brand fonts, tell me. I'd keep them for the logo and `h1` only, and use the sturdy sans for everything else.
