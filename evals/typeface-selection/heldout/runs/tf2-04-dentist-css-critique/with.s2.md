**Short version:** the body text is set in a script face, and there are six families where one or two would do. Both problems match what parents describe.

## What's wrong

**Chaos (design):**
- **Six families:** Lobster, Playfair Display, Montserrat, Raleway, Comic Neue and Courier New. Each element gets its own voice, so nothing looks like it belongs to the same practice.
- **Montserrat and Raleway are near-twins.** They're both geometric sans faces, and the difference reads as a mistake, not a choice.
- **Body copy is in Lobster at 13px with `line-height: 1.2`.** Script faces are for a few big words. Used for paragraphs, with tight leading and small size, they're tiring to read. Parents are trying to find hours, insurance and what to expect, and this is where they'll struggle most.
- **Weight 100 and 200 text** is used for `h2` (uppercase, 4px tracking) and 12px nav links. Hairline strokes at small sizes turn thin and washed out, especially on low-density screens. The nav is the thing people need to be able to read.
- **Comic Neue on buttons** adds a sixth personality. The playful feel is fine for a kids' practice, but Lobster, Playfair and Comic Neue all compete for it.
- **Courier New for prices and hours** makes the most practical information look like a typewriter receipt. Monospace is for code and aligned columns, and it doesn't suit a children's dentist.
- **Faux bold:** Lobster only ships a regular weight. Any `<strong>`, `<b>` or `<th>` in the body gets a browser-synthesized bold, which looks smeared.

**Slow (loading):**
- **`@import` inside CSS** makes the browser download the stylesheet, then find the import, then fetch Google's CSS, then fetch the font files. That's a serial chain, and it blocks rendering.
- **`display=block`** hides all text until the fonts arrive, for up to about 3 seconds. On a slow phone connection, parents see a blank page.
- **Too many weights:** Montserrat loads 7 weights and Playfair loads 3. You use one of each (100 and 900). Across five web families, that's well over a dozen font files. Only the weights you actually use should load.
- **No fallbacks.** `'Montserrat'`, `'Raleway'`, `'Comic Neue'` and `'Courier New'` have no generic family after them. If the web font is slow or blocked, the browser picks whatever it likes.

## What I'd do

Assumptions: the audience is parents on phones, Latin script only, and you want friendly rather than clinical. One rounded family with real weight range covers everything. Nunito is my suggestion. It's on Google Fonts under an open license, but confirm the license terms yourself. Any sturdy, friendly sans with 400 to 800 would work too.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;800&display=swap">
```

```css
:root {
  --font: 'Nunito', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
}
body { font-family: var(--font); font-size: 16px; line-height: 1.6; color: #444; }
h1   { font-weight: 800; font-size: 40px; line-height: 1.15; }
h2   { font-weight: 800; font-size: 24px; }            /* no all-caps, no hairline */
nav a { font-weight: 600; font-size: 15px; }
.price, .hours { font-weight: 600; font-variant-numeric: tabular-nums; }
.btn { font-weight: 800; }
```

- **One family, three weights.** Hierarchy comes from weight and size, so the page reads as one voice and loads three files instead of a dozen.
- **`<link>` instead of `@import`**, with `preconnect` and `display=swap`. Text shows right away in the system font and swaps when Nunito arrives.
- **Body is 16px with 1.6 leading**, and the nav is 15px at weight 600.
- **Prices and hours are in the same family.** Tabular figures keep the numbers aligned.
- **A real fallback stack** means the page still looks intentional if the font never loads.

If you want one expressive moment, such as the logo or the `h1`, keep Lobster for that line only. Load just that text with `&text=` or a subset, and don't use it anywhere else. I'd skip that on the first pass and see how the calmer version feels.

Next, I'd self-host the Nunito files (subset to Latin, `woff2`) with a preload for the regular weight. That removes the Google round trip entirely. It's the next biggest speed win after the changes above.
