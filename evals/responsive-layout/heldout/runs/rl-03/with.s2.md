The viewport tag and the root font size are almost certainly what QA is seeing. Here are the problems by impact, each with a fix.

## 1. Viewport meta tag (phones and older users)
`width=1024` makes phones lay the page out at 1024px wide and shrink it, so text is tiny. `maximum-scale=1` and `user-scalable=no` stop people from pinching to zoom, which hurts low-vision users and fails WCAG 1.4.4.

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

## 2. `62.5%` root size and pixel line-height (older users)
`html { font-size: 62.5% }` overrides the reader's browser text-size setting. Body text also comes out at 14px, which is small. `line-height: 20px` is fixed, so it doesn't grow when text is enlarged, and lines overlap or cramp.

```css
body { font-size: 1rem; line-height: 1.5; }
```

Delete the `html` rule. If the design needs slightly larger text, use `font-size: 1.125rem` on `body`. Don't change the root.

## 3. Cards overflow on phones
Below 768px, `.card` becomes `width: 100%` and still has `margin: 10px`. That makes each card 20px wider than its container and causes sideways scroll. The floats are also never cleared, so the parent collapses. Replace floats and the media query with a grid:

```css
.content {
  max-inline-size: 60rem;
  margin-inline: auto;
  padding-inline: 1rem;
}
.cards {  /* wrap the cards in this */
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(min(17.5rem, 100%), 1fr));
  gap: 1rem;
}
```

Remove the `.card` float, width and margin. Also delete the `min-width: 1440px` query, because it sets `960px`, which is what the base rule already sets.

## 4. Hero
`height: 100vh` clips content when text is large or the screen is short, such as a landscape phone. Mobile browser toolbars also make `vh` taller than the visible area. The fixed 48px `h1` has the same clipping problem on short screens.

```css
.hero {
  min-block-size: 100vh;
  min-block-size: 100dvh;
  display: grid;
  align-content: center;
  padding: 2rem 1rem;
  background: #14325c;
  color: #fff;
}
.hero h1 { font-size: clamp(2rem, 6vmin + 1rem, 3.5rem); }
```

## What I left alone
The hero colors are fine. `#fff` on `#14325c` has roughly 12:1 contrast.

## What I checked
- **Media queries:** I went from 2 to 0. The 768px one is replaced by the grid, and the 1440px one did nothing.
- **Units changed:** `62.5%` root → default, `1.4rem` → `1rem`, `20px` line-height → `1.5`, `960px` → `60rem` max, `48px` → `clamp()`, `100vh` → `dvh` with a `vh` fallback.
- **320px:** one card per column (`min(17.5rem, 100%)` caps it at the container), and no sideways scroll.
- **768px:** two columns.
- **1440px:** the content stays at 60rem, with three cards per row.
- **200% text size:** the hero grows instead of clipping, and line spacing scales.

I haven't run this in a browser, so check it on a real phone and with the browser's text size set to large before Friday. The markup also needs a `.cards` wrapper around the `.card` elements, which I assumed since I only saw the CSS.
