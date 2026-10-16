**Verdict: don't ship as is.** The viewport tag causes most of what QA is seeing. The rest of the CSS adds to it.

## Problems, by impact

**1. The viewport tag forces a desktop layout on phones and blocks zoom.**
- `width=1024` makes phones render a 1024px page and shrink it to fit. That's why text looks tiny.
- Your `max-width: 768px` query never fires, because the layout viewport is 1024px wide.
- `maximum-scale=1` and `user-scalable=no` stop users from pinching to zoom. That is the main cause of the "older users" complaint, and it is an accessibility failure (WCAG 1.4.4).

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

**2. Type ignores the reader's settings and is small.**
- `html { font-size: 62.5% }` makes `1.4rem` equal 14px. It also breaks every rem for anyone who has changed their browser text size.
- `line-height: 20px` clips or crowds text once it's enlarged.
- The 48px `h1` doesn't scale down on phones or up on large screens.

```css
body { font-size: 1rem; line-height: 1.5; }
.hero h1 { font-size: clamp(2rem, 5vmin + 1rem, 3.5rem); }
```
Delete the `html { font-size }` rule.

**3. `.content { width: 960px }` overflows every screen narrower than 960px.** That includes all phones and tablets, and it forces sideways scrolling. The 1440px query sets the same 960px, so it does nothing.

```css
.content { inline-size: min(60rem, 100% - 2rem); margin-inline: auto; }
```

**4. The cards are fixed at 280px and floated.**
- The container isn't cleared, so it collapses.
- Margins don't collapse the way a `gap` would.
- Only one query handles narrow screens, and that query never fired because of problem 1.

```css
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(min(17.5rem, 100%), 1fr));
  gap: 1.25rem;
}
.card { min-inline-size: 0; overflow-wrap: anywhere; }
```
Wrap the cards in `.cards`. This reflows on its own, so both media queries can go.

**5. `.hero { height: 100vh }` clips content.** On phones, `100vh` is taller than the visible area because of the browser toolbar. On landscape phones or at larger text sizes, the heading and any button can get cut off. Use a minimum height instead, and let the content set the real height.

```css
.hero {
  min-block-size: 100vh;
  min-block-size: 100dvh;
  display: grid;
  place-content: center;
  padding: 2rem 1rem;
  background: #14325c;
  color: #fff;
}
```

## What already works
- `#fff` on `#14325c` has a contrast ratio of about 12:1, which passes AA and AAA. Leave it.
- The centered-column idea is fine. Only the fixed width was wrong.

## Checks (reasoned, not run in a browser)
- **Breakpoints:** 0 remain. Both queries were removed because the grid and `min()` handle the layout, and the 1440px one was a no-op.
- **Units changed:** `px` to `rem`/`clamp()` for the h1; `line-height: 20px` to `1.5`; `62.5%` root removed; fixed `960px`/`280px` replaced with `min()`.
- **320px wide:** content is 288px wide and cards are one column of 288px, with no sideways scroll.
- **200% text size:** the hero grows instead of clipping, and line height scales with the text.
- **Wide screens:** content stops at 60rem and the card grid adds columns as room allows.

**Assumptions:** plain CSS, evergreen browsers, left-to-right, and a minimum width of 320px. I haven't seen your markup, so check that the cards sit in a single wrapper. Please also re-test on a real phone and with the browser's text size set to Large.
