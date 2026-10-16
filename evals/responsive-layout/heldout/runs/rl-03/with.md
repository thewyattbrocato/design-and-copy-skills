The layout isn't ready to ship. The cause of both QA complaints is in the code you pasted. I reviewed it against the skill's checks and didn't open the reference files. Findings are in order of impact.

## 1. The viewport meta locks phones to a desktop layout and blocks zoom
```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```
- `width=1024` makes every phone render a 1024px canvas and scale it down. That's why it "looks off on some phones". Text shrinks and the `@media (max-width: 768px)` rule never fires.
- `maximum-scale=1` and `user-scalable=no` stop pinch-zoom. That blocks the older users QA mentioned, and it fails WCAG 1.4.4 (Resize Text) and 1.4.10 (Reflow).

## 2. The `html` font-size of 62.5% shrinks everyone's text
`62.5%` of the default 16px is 10px, so `body { 1.4rem }` is 14px. That's small, and it's the likely source of "older users". The percentage does follow browser text-size settings. The 14px result is still too small, and the `line-height` in pixels (below) is a second problem. Leave the root alone and set the body size in rem:
```css
html { font-size: 100%; }
body { font-size: 1rem; line-height: 1.5; }
```
`line-height: 20px` is fixed. When text is enlarged it will overlap. Use a unitless value.

## 3. The fixed 960px container and cards force sideways scroll
`.content { width: 960px }` is wider than any phone. The `min-width: 1440px` rule sets the same 960px, so it does nothing and can be deleted. The cards use a float with a 280px width and 10px margins, and they only go full-width below 768px, which never triggers (see #1).
```css
.content { inline-size: min(60rem, 100% - 2rem); margin-inline: auto; }

.cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(min(17.5rem, 100%), 1fr));
  gap: 1.25rem;
}
.card { min-inline-size: 0; overflow-wrap: anywhere; }
```
Wrap the cards in a `.cards` element. This replaces the float and the 768px media query. The cards wrap by themselves, and `min()` keeps one card from overflowing a 320px screen.

## 4. The hero can clip on short screens, and the h1 is fixed at 48px
`height: 100vh` clips the content on landscape phones. On mobile browsers `100vh` is also taller than the visible area because of the address bar. A fixed 48px h1 is too big at 320px and doesn't scale with the user's text size.
```css
.hero {
  min-block-size: 100vh;   /* fallback */
  min-block-size: 100dvh;
  display: grid;
  place-content: center;
  padding: 2rem 1rem;
  background: #14325c;
  color: #fff;
}
.hero h1 {
  font-size: clamp(2rem, 1.2rem + 4vmin, 3rem);
  overflow-wrap: anywhere;
}
```
Add `box-sizing: border-box` globally, because the padding above relies on it.

## Already fine
The hero's `#14325c` on white text has strong contrast (about 12:1), so leave it.

## Checks I reasoned through
- At 320px, the container is 288px wide, there's one card column, and there's no sideways scroll.
- At 200% text size, the line-height scales with the text and nothing overlaps.
- At 1440px, the container stays at 60rem.
- I removed 2 media queries and kept none. Wrapping is handled by the grid, and nothing here depends on the device.

## Before Friday
Test on a real phone at 320–390px wide and with the OS text size set to large. I haven't run the page. These are conclusions from reading the code, not from testing it. I can't see the rest of the stylesheet, so check that nothing else sets a fixed width, such as nav, forms or tables.
