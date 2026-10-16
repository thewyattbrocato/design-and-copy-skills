Honest verdict: the setup is causing both complaints. Here's what's wrong, roughly in order of impact.

## Why it feels chaotic

1. **Five typefaces plus a system font.** Lobster, Playfair Display, Montserrat, Raleway, Comic Neue, and Courier New. A good site uses one or two families. Six reads as a ransom note.

2. **Lobster as the body font.** This is the biggest problem. Lobster is a display script meant for a logo or a single headline. Set at 13px with a 1.2 line-height in gray, it's hard to read, especially for tired parents on phones.

3. **Body text is too small, too tight, and too light.**
   - 13px is below the usual 16px minimum.
   - A 1.2 line-height is cramped. Aim for 1.5–1.6 for body text.
   - `#666` on white is about 5.7:1, so it passes. But with a thin script at 13px, the effective legibility is poor.

4. **Hairline weights at small sizes.**
   - Nav links use Raleway 200 at 12px. That's tiny and very thin.
   - h2s use Montserrat 100 with uppercase and 4px tracking. The strokes nearly vanish.
   - These are both accessibility problems and hard to tap or read on mobile.

5. **The heading styles clash.** An ultra-heavy Playfair 900 h1 sits above a hairline spaced-out Montserrat h2. The extremes of weight and style fight each other and set no consistent hierarchy.

6. **Courier New for prices and hours.** It's the most important practical info on the page, and it's in a typewriter font that looks unrelated to everything else. It's also a system font, so it renders differently across devices.

7. **Comic Neue on buttons.** Comic Sans-style type on a button, next to Lobster and Playfair, adds to the chaos. For a pediatric dentist, "playful" is fine, but it should be a deliberate, consistent choice.

## Why it loads slowly

1. **`@import` inside CSS.** The browser has to download the CSS file, find the `@import`, then request the Google Fonts stylesheet, and only then request the font files. That's a serial chain. Use `<link rel="preconnect">` and `<link rel="stylesheet">` in the HTML `<head>` instead.

2. **Too many weights.** You're requesting roughly 18 font files:
   - Montserrat: 7 weights
   - Raleway: 3 weights
   - Playfair: 3 weights
   - Plus Lobster and Comic Neue

   Most of these are probably never used. The CSS only uses Montserrat 100, Raleway 200, and Playfair 900, plus defaults for the others.

3. **`display=block`.** Text is invisible until the fonts arrive (up to about 3 seconds). On a slow connection, parents see a blank page. Use `display=swap` (or `optional`) so text shows right away.

4. **Unused weights are a waste.** Montserrat is requested at 100–700, but only 100 is used. Raleway is requested at 100, 200, and 300, but only 200 is used. Playfair is requested at 400, 700, and 900, but only 900 is used. Comic Neue is requested at its default weight only, so there's no waste there.

5. **No fallback stacks.** `font-family: 'Montserrat'` with no fallback causes a bigger layout shift and a worse flash while loading. Always add `sans-serif` or similar.

## What I'd do

Pick **one friendly heading font and one clean body font**. For example:

- **Headings:** Nunito or Fredoka (rounded, kid-friendly, still professional)
- **Body, nav, buttons, prices and hours:** Nunito Sans or system-ui

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;700&family=Nunito+Sans:wght@400;600&display=swap">
```

```css
body { font-family: 'Nunito Sans', system-ui, sans-serif; font-size: 16px; line-height: 1.6; color: #444; }
h1, h2 { font-family: 'Nunito', system-ui, sans-serif; font-weight: 700; }
h1 { font-size: clamp(32px, 5vw, 44px); line-height: 1.2; }
h2 { font-size: 1.75rem; }
nav a { font-weight: 600; font-size: 1rem; }
.price, .hours { font-weight: 600; }
.btn { font-family: 'Nunito', sans-serif; font-weight: 700; }
```

This drops you from about 18 font files to about 4. It also gives you readable text, a consistent look, and no invisible-text period. If you want to go further, self-host the fonts (subset to Latin) to remove the Google round trip entirely.

I haven't seen the actual site, only this CSS, so I can't say how much of the slowness comes from fonts versus images or scripts. Fonts are likely a real contributor, but run Lighthouse or WebPageTest to confirm that before assuming they're the whole story.
