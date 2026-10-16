The two biggest problems, the viewport tag and the fixed 960px width, probably explain both QA complaints. I'd fix those before Friday.

## Blockers

**1. Viewport meta tag**
```html
<meta name="viewport" content="width=1024, initial-scale=1, maximum-scale=1, user-scalable=no">
```
- `width=1024` makes phones lay the page out at 1024px and shrink it to fit, so everything looks tiny. That's likely the "looks off on some phones" report.
- `maximum-scale=1` and `user-scalable=no` block pinch-zoom. That fails WCAG 1.4.4 (Resize Text) and hurts the older users QA mentioned.

Replace it with:
```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

**2. Fixed `.content { width: 960px }`**
On any screen narrower than 960px this causes horizontal scrolling or clipping. Use `max-width` instead. The `@media (min-width: 1440px)` rule sets the same 960px, so it does nothing and can go.

**3. Mobile card overflow**
At ≤768px, `.card` is `width: 100%` plus `margin: 10px` on each side, so each card is 20px wider than its container. Floats also need clearing, and there's no `box-sizing: border-box`. A grid fixes all of this.

## Accessibility and readability

**4. Small text.** `62.5%` with `1.4rem` gives 14px body text, which is small for older users. The percentage does respect the browser's font-size setting, but the 14px base is the problem. Use `100%` on `html` and at least `1rem` (16px) on `body`. `1.125rem` would be friendlier.

**5. `line-height: 20px`.** A fixed line height doesn't scale with text size, so lines overlap when users enlarge the font. Use a unitless value like `1.5`.

**6. `.hero h1 { font-size: 48px }`.** It's too large for narrow phones and ignores user font settings. Use `clamp()` with rem units.

**7. `.hero { height: 100vh }`.** On mobile, `100vh` is taller than the visible area because of the browser toolbar. A fixed height also clips content when text is enlarged or the phone is in landscape. Use `min-height`.

The white-on-`#14325c` contrast is fine, at about 12:1.

## Suggested rewrite

```css
*, *::before, *::after { box-sizing: border-box; }

html { font-size: 100%; }
body { font-size: 1.125rem; line-height: 1.5; }

.hero {
  min-height: 100vh;
  min-height: 100svh;
  padding: 2rem 1rem;
  background: #14325c;
  color: #fff;
}
.hero h1 { font-size: clamp(2rem, 6vw, 3rem); line-height: 1.2; }

.content { max-width: 960px; margin: 0 auto; padding: 0 1rem; }

.cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 1rem;
}
```

This needs a `.cards` wrapper around the `.card` elements in the markup. With the grid, you can delete the float, the media queries and the card width rules.

## Before shipping
- Test at 320px width, in landscape, and with the browser's text size set to 200%.
- Test pinch-zoom on a real iOS device and a real Android device.
- I only saw the head and this CSS, so I couldn't check focus outlines, tap target sizes (at least 44px), or form input font sizes. iOS Safari auto-zooms inputs below 16px.

I can apply the changes if you point me at the files.
