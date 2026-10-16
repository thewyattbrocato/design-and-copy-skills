**Short version:** this setup has too many roles, the body font is the wrong choice, and the loading method is slow. Both complaints come from the font setup.

## Why it feels chaotic

- **There are six families and no system.** Lobster, Playfair Display, Montserrat, Raleway, Comic Neue and Courier New all appear. Each one is a different personality. The skill's rule is one family by default and two at most, each with a defined role.
- **The body text is set in Lobster.** It's a bold display script, and here it runs at 13px with 1.2 line height. That is the worst problem on the page. Parents read hours, insurance and appointment info in it, and script faces get tiring and hard to read at small sizes.
- **Several faces are too similar.** Montserrat, Raleway and Comic Neue are all rounded or geometric sans faces. Pairing near-identical faces looks like a mistake and not a deliberate choice.
- **The weights are too thin.** The h2 is Montserrat 100 with 4px tracking and the nav is Raleway 200 at 12px. Hairline weights wash out at small sizes and on low-density screens, and nav links are the thing people need to hit.
- **Courier New is used for prices and hours.** It's monospace for a "typewriter" feel, which doesn't fit a kids' dental practice. If you want aligned numbers, use a sans with tabular figures.
- **The text is small and low-contrast.** Body is 13px in #666 gray. That is too small for text this decorative, and the gray is weak on white.
- **The font ranges for h1 and Lobster look like different brands.** A 900-weight Playfair h1 above a Lobster body reads as two sites stitched together.

## Why it loads slowly

- **It uses a CSS `@import`.** The browser has to download the stylesheet before it finds the font request, which delays everything behind it. Use `<link rel="preconnect">` plus `<link>` in the HTML head, or self-host.
- **It requests about 18 weights.** Montserrat 100–700 is 7 weights, Playfair is 3, Raleway is 3, and the rest are single weights. You actually use about 6 of them. Request only the ones you use.
- **It uses `display=block`.** That hides all text for up to about 3 seconds while fonts load. Use `swap` or `optional`.
- **The fallbacks are weak.** `cursive` and `serif` are bare generic names, and `'Montserrat'` and `'Raleway'` have no fallback at all. Text will visibly jump when the fonts arrive, and some visitors will see a default Times or a system cursive.

## Fix

One family for the interface and body, plus one friendly display face used only for the h1 and a few headings. I'm assuming the Latin script, a screen, and that web fonts can load.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&family=Fredoka:wght@600&display=swap">
```

```css
body {
  font-family: 'Nunito', system-ui, -apple-system, 'Segoe UI', sans-serif;
  font-size: 17px;
  line-height: 1.55;
  color: #333;
}
h1, h2 { font-family: 'Fredoka', 'Nunito', system-ui, sans-serif; font-weight: 600; }
h1 { font-size: 44px; line-height: 1.1; }
h2 { font-size: 28px; }              /* drop the uppercase and 4px tracking */
nav a { font-weight: 600; font-size: 16px; }
.price, .hours { font-variant-numeric: tabular-nums; }
.btn { font-weight: 700; }           /* same family as the body */
```

- **Nunito** is a rounded, friendly sans for reading and the interface. It has real weights and an italic.
- **Fredoka** is a playful display face, used only for the big headings.
- **The price, hours and button styles** now share the body family. Tabular figures replace the typewriter look.

That drops the page from six families to two and from about 18 weights to 4. Text shows immediately, and a matching system fallback keeps the layout steady while the fonts arrive.

I picked these two for tone and haven't tested them on your real pages. Open the site on a phone, read a full paragraph of the hours and insurance text, and adjust from there. Both are Google Fonts. If you plan to self-host, check the license on the font's Google Fonts page.
