Yes, this explains both QA complaints. Several of these should be fixed before Friday.

## Blockers

**1. The viewport meta tag disables mobile layout and zoom.**
```html
<meta name="viewport" content="width=1024, initial-scale=1, maximum-scale=1, user-scalable=no">
```
- `width=1024` makes phones render a 1024px-wide page and scale it down. Text ends up tiny, and your `max-width: 768px` media query never fires, because the layout viewport is 1024px.
- `user-scalable=no` and `maximum-scale=1` block pinch-zoom. That fails WCAG 1.4.4 (Resize Text) and hurts older and low-vision users most. It's also a legal exposure for a member portal.

Fix:
```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

**2. The fixed 960px `.content` width forces horizontal scrolling on any viewport narrower than 960px.**
Use a fluid width with a cap:
```css
.content { max-width: 960px; width: 100%; margin: 0 auto; padding: 0 16px; }
```
The `@media (min-width: 1440px) { .content { width: 960px; } }` rule does nothing, since it repeats the base value. Delete it.

**3. Body text is about 14px, and `line-height` is in fixed pixels.**
- `62.5%` on `html` makes 1rem = 10px, so `1.4rem` = 14px. That's small for body copy, and it overrides the user's browser font-size setting, which is the main way older users scale text.
- `line-height: 20px` doesn't scale with the font. If someone enlarges text, lines will overlap or sit cramped.

Fix:
```css
html { font-size: 100%; }
body { font-size: 1rem; line-height: 1.5; } /* 16px+ by default */
```
If you want the 62.5% convention, you'd need `body { font-size: 1.6rem }`. Dropping it is simpler.

## Should fix

**4. `.hero { height: 100vh }` is unreliable on mobile.** Browser toolbars make `100vh` taller than the visible area, so content can be cut off. Use `min-height: 100vh` with a `100svh` override, or `min-height`. A fixed `height` also clips content when text is enlarged or wraps.
```css
.hero { min-height: 100vh; min-height: 100svh; }
```

**5. `h1 { font-size: 48px }` is fixed.** It's too big on a 320–375px phone and ignores user font settings. Use `font-size: clamp(2rem, 6vw, 3rem);`.

**6. The floated cards are fragile.**
- `float: left` with no clearfix means `.content` collapses to zero height. The cards also wrap awkwardly when the widths don't divide evenly.
- 3 × (280 + 20) = 900px fits in 960px, but any padding or scrollbar changes that.
- Below 768px, `width: 100%` plus `margin: 10px` overflows by 20px, which causes horizontal scroll. Add `box-sizing: border-box` and use grid instead:
```css
*, *::before, *::after { box-sizing: border-box; }
.cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px; }
```
This also removes the need for the media query.

## Also check (not visible in what you sent)
- **Contrast:** white on `#14325c` is fine (about 12:1), but check the body text and link colors elsewhere.
- **Tap targets:** buttons and links should be at least 44×44px for older users and anyone with motor difficulties.
- **Focus styles:** make sure `outline` isn't removed anywhere.
- **Testing:** try 200% browser zoom, a larger OS text size, and a real iPhone and Android device. The simulator alone won't catch the toolbar `100vh` issue.

If you share the full stylesheet or markup, I can check the card structure and write the full replacement.
