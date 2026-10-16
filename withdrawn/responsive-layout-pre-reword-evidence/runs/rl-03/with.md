## Verdict

Don't ship this as is. The viewport tag and the fixed 960px layout explain both QA complaints, "off on some phones" and "older users".

## Problems, by impact

**1. The viewport meta locks the page to desktop width and blocks zoom.**
`width=1024` makes phones render a 1024px page and shrink it. `maximum-scale=1, user-scalable=no` stops pinch-zoom, which older and low-vision users rely on. It also fails WCAG 1.4.4.

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

**2. `html { font-size: 62.5% }` with `body { font-size: 1.4rem }` gives 14px body text.**
The 62.5% trick shrinks the default text size. The `rem` values then look like they follow user settings, but 14px is small for body copy. Users who raised their browser text size get less benefit than they should. `line-height: 20px` is also fixed, so it doesn't grow with enlarged text and lines can collide.

```css
html { font-size: 100%; }
body { font-size: 1rem; line-height: 1.5; }
```

**3. `.content { width: 960px }` and `.card { width: 280px }` break narrow screens.**
Anything under 960px scrolls sideways. The `@media (min-width: 1440px)` rule sets the same 960px, so it does nothing. Delete it. The `max-width: 768px` card rule hides the problem on some phones but not at 769–960px. It also doesn't fix `.content`.

```css
.content { inline-size: min(60rem, 100% - 2rem); margin-inline: auto; }
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(17.5rem, 100%), 1fr));
  gap: 1.25rem;
}
.card { min-inline-size: 0; overflow-wrap: anywhere; }
```

This needs a `.cards` wrapper in the markup. It replaces the float, the margins and the 768px query. The grid wraps by itself, so the query goes away. A 320px screen gets one column and a wide window gets three or four.

**4. `.hero { height: 100vh }` clips content.**
On landscape phones, with enlarged text, or when mobile browser bars show, the heading and button can overflow or be cut off. The 48px `h1` makes it worse.

```css
.hero {
  min-block-size: 100vh;
  min-block-size: 100dvh;
  display: grid;
  place-content: center;
  padding: 1.5rem;
  background: #14325c;
  color: #fff;
}
.hero h1 { font-size: clamp(2rem, 1.2rem + 4vmin, 3rem); }
```

**5. Floats.**
`.card` floats with no clearing, so the container collapses. The grid in fix 3 removes this.

## What already works
- The hero colors are fine. `#fff` on `#14325c` has high contrast, about 11:1.
- Centering with `margin: 0 auto` is fine. The fix above only swaps its width.

## Checks I reasoned through
- **320px:** one column, no sideways scroll. The content width is 100% − 2rem.
- **200% text:** the hero grows via `min-block-size`, and `line-height` is unitless.
- **Wide screen:** the content caps at 60rem (960px at default text size), the same as today.
- **Queries:** I removed both media queries. The first was replaced by the grid and the second did nothing.

I haven't seen your markup or run the page, so test it on a real phone and at 200% browser zoom before Friday. I assumed evergreen browsers, plain CSS and left-to-right text.
