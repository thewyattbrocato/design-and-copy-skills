Don't ship this as is. Both QA complaints trace back to a few specific lines. I reviewed the code you pasted and didn't run it in a browser.

## Problems, by impact

**1. The viewport meta tag breaks phones and blocks zoom.**
- `width=1024` makes phones lay out a 1024px page and shrink it. That's why it looks off on phones.
- `maximum-scale=1, user-scalable=no` stops pinch-zoom. That locks out older and low-vision users, and it fails WCAG 1.4.4 (Resize Text) and 1.4.10 (Reflow).
- Because of the 1024px width, your `max-width: 768px` query never fires on a phone.

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

**2. `html { font-size: 62.5% }` overrides the user's text-size setting.**
- It shrinks the root to 10px. Combined with `body { font-size: 1.4rem }`, body text is 14px. That's small for older users.
- The pixel `line-height` and `h1` don't scale with the text either.

```css
html { font-size: 100%; }  /* or delete the rule */
body { font-size: 1rem; line-height: 1.5; }
.hero h1 { font-size: clamp(2rem, 1.2rem + 4vmin, 3rem); }
```

**3. `.content { width: 960px }` forces sideways scroll below 960px.**
- On a 375px phone the content is wider than the screen.
- The `min-width: 1440px` query sets the same 960px, so it does nothing. Delete it.

```css
.content { inline-size: min(60rem, 100% - 2rem); margin-inline: auto; }
```

**4. The floated 280px cards are fragile.**
- Floats need clearing, and the 10px margins make the row math awkward.
- The 768px query only works around that. Use a grid that wraps by itself, which removes the need for the query:

```css
.cards {  /* wrapper around the cards */
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(min(17.5rem, 100%), 1fr));
  gap: 1.25rem;
}
.card { min-inline-size: 0; overflow-wrap: anywhere; }
```

If you can't add a wrapper, `.content` could be the grid itself.

**5. `.hero { height: 100vh }` can clip content.**
- On a landscape phone or at large text sizes, the headline or button can get cut off.
- `100vh` on mobile Safari and Chrome also includes the URL bar area.

```css
.hero {
  min-block-size: 100vh;   /* fallback */
  min-block-size: 100dvh;
  display: grid;
  place-content: center;
  padding: 1rem;
}
```

## Already fine
- The hero's `#14325c` background with white text has strong contrast (about 12:1).

## Result
- Net result: the 768px and 1440px media queries are both gone, since neither is needed.
- At 320px, the content area is 288px wide with no sideways scroll.
- At 200% text size, text wraps and the hero grows instead of clipping.

## Assumptions
- Your support target is evergreen browsers, since I used `dvh`, `min()` and `clamp()`. The `100vh` fallback covers older ones.
- The cards sit directly in `.content`. I added a `.cards` wrapper, so adjust that to your markup.
- The page reads left to right.

Before Friday, test on a real phone, with browser text size set to large, and with pinch-zoom to 200%.
