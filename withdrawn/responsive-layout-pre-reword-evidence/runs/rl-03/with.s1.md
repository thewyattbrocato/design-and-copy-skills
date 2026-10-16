Don't ship this as is. The viewport tag and the fixed-pixel layout explain both of QA's complaints.

## Problems, by impact

**1. The viewport tag blocks zoom and fakes a desktop width.**
`width=1024` makes phones render a 1024px page and shrink it to fit, so everything looks tiny. `maximum-scale=1, user-scalable=no` stops low-vision users from zooming. That is the "older users" complaint, and it is also a WCAG failure (1.4.4).
```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

**2. `.content { width: 960px }` can't fit a phone.**
Below 960px the page scrolls sideways. The `min-width: 1440px` query sets the same 960px again, so it does nothing. Delete it.
```css
.content { inline-size: min(60rem, 100% - 2rem); margin-inline: auto; }
```

**3. The root size is 62.5% and the body is 1.4rem, so body text is 14px.**
That is small for older users. It also scales with the browser setting, but 14px is a poor starting point. `line-height: 20px` is fixed, so enlarged text will overlap itself.
```css
html { font-size: 100%; }
body { font-size: 1rem; line-height: 1.5; }
```

**4. `.hero { height: 100vh }` clips content.**
On phones, 100vh includes the browser toolbar, so the bottom is cut off. On landscape phones or at large text sizes, the fixed height clips the headline and any button. The 48px `h1` is also fixed.
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
.hero h1 { font-size: clamp(2rem, 6vmin + 1rem, 3rem); overflow-wrap: anywhere; }
```
Check `#14325c` on white: the contrast is high, so the colors are fine.

**5. Floated 280px cards with a 768px breakpoint.**
- Floats need a clearfix, or the parent collapses.
- Fixed 280px cards leave a ragged gap on the right at most widths.
- The 768px query only repairs a layout that was already broken.
- `width: 100%` plus `margin: 10px` overflows by 20px, so you get sideways scroll on phones.
- Margins on each child should be a parent `gap` instead.

This pattern needs no media query:
```css
*, *::before, *::after { box-sizing: border-box; }
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(17.5rem, 100%), 1fr));
  gap: 1.25rem;
}
.card { min-inline-size: 0; overflow-wrap: anywhere; }
```
Wrap the cards in `.cards` and drop `float`, `width` and `margin` from `.card`.

## Result
- Both media queries are removed. One was a no-op and the other is replaced by the grid, so no breakpoints remain. The layout adapts to its container.
- The units changed from px to rem, `ch`/`%` and `dvh`/`vmin`.
- Widths I reasoned through:
  - At 320px, the content is 288px wide, there is one card column, and nothing scrolls sideways.
  - At 200% text size, the line height and hero height both grow with the text, so nothing overlaps.
  - At 1440px, the content is capped at 960px and centered.

## Left alone
- The hero colors.
- Centering with `margin: 0 auto`, which I only converted to the logical form.

## Assumptions
- Evergreen browsers (for `dvh`, `min()`, `clamp()`).
- Plain CSS, left-to-right text.
- The card markup is a flat list, so it can sit inside one wrapper.

I only had the snippets, not the full stylesheet. Check for other fixed widths, such as the nav, forms and tables, before Friday. Test at 320px, with browser text set to Large, and with pinch-zoom on a real phone.
