Yes, there are several problems here, and the first two probably explain most of what QA is seeing.

## Blockers

**1. The viewport meta tag breaks phones and blocks zoom.**
```html
<meta name="viewport" content="width=1024, initial-scale=1, maximum-scale=1, user-scalable=no">
```
- `width=1024` makes phones lay the page out at 1024px wide and shrink it down. Text ends up tiny, and your `max-width: 768px` media query never fires. This is the main cause of "looks off on some phones."
- `maximum-scale=1` and `user-scalable=no` disable pinch-zoom. That fails WCAG 1.4.4 (Resize Text) and is a real problem for older and low-vision users. It also creates legal exposure for a member portal.

Fix:
```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

**2. Fixed 960px `.content` can't fit a phone.**
`width: 960px` forces horizontal scrolling on anything narrower. The `@media (min-width: 1440px) { .content { width: 960px; } }` rule repeats the base value, so it does nothing. Delete it, or use it to set a wider max.

```css
.content { width: min(100% - 32px, 960px); margin-inline: auto; }
```

## Accessibility and "older users"

**3. Body text is small.** `62.5%` on `html` makes 1rem equal 10px, so `body` at `1.4rem` is 14px. That is small for older users. The `62.5%` trick also overrides the user's browser font-size setting, so anyone who raised their default text size is partly ignored. Use the default root size and a larger body:
```css
html { font-size: 100%; }
body { font-size: 1.125rem; line-height: 1.5; } /* 18px at default */
```

**4. `line-height: 20px` is fixed in pixels.** At 14px it's tight. If text is enlarged, lines overlap. Use a unitless value (1.5).

**5. Hero `h1` is `48px`.** It won't scale with the user's text settings, and it's too big on a 360px-wide phone. Use `font-size: clamp(2rem, 5vw + 1rem, 3rem)`.

**6. Contrast.** `#fff` on `#14325c` is about 12:1, so it passes. I can't check the rest without the link, button and muted-text colors. Check those, especially any gray text.

## Layout

**7. `.hero { height: 100vh }`.** On mobile browsers `100vh` includes the area under the collapsing URL bar, so content gets cut off. It also clips the hero if text is enlarged or the screen is in landscape. Use `min-height: 100vh; min-height: 100svh;`, and let the content set the height.

**8. Floated cards.**
- `float: left` with no clearfix means `.content` collapses and the following content can wrap around the cards.
- Fixed `280px` plus `10px` margins gives 300px per card. Three fit in 960px (900px) and leave 60px of slack. That works only at exactly that width.
- Between 769px and 960px the cards overflow the container, because the only breakpoint is at 768px.
- At `width: 100%` plus `10px` margins on each side, cards overflow by 20px on phones. That causes horizontal scroll.

Use grid instead:
```css
.cards { display: grid; gap: 20px;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); }
.card { /* drop float, width, margin */ }
```
Wrap the cards in `.cards`. This replaces the media query.

**9. Missing box-sizing reset.** Add `*, *::before, *::after { box-sizing: border-box; }`. Any padding or border you add to `.card` later will otherwise break the widths.

## Before Friday

- Fix 1 and 2 first. Together they probably account for most of QA's report.
- Test on a real iPhone and a real Android phone, not only DevTools emulation. Also test at 200% browser zoom and with the OS text size set to large.
- Run Lighthouse or axe. Both flag the viewport zoom block automatically.
- Check keyboard focus states and tap targets of at least 44px. I haven't seen that CSS, so I can't tell whether they're in place.

I can rewrite the full stylesheet with these changes if you'd like. Paste the rest of the CSS too if there is more, since forms, nav and buttons are where older users often have trouble.
