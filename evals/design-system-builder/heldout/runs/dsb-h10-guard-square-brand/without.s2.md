The brand is already a rule set, so the tokens should be small. A short scale would invite soft shapes, shadows and motion. I'd define only what the brand permits.

## Radius

One token, with no scale:

```css
--radius-none: 0;
```

- Apply it globally (`*, ::before, ::after { border-radius: 0 }`). Safari and iOS give buttons, inputs and selects default rounding, so this needs an explicit reset.
- Don't define `sm`, `md` or `lg`. Without them, nobody can reach for a rounded corner.
- The only real question is whether radio buttons and avatars may be circles. If so, add `--radius-round: 9999px` and restrict it to those two uses. If the answer is no, use square radios and avatars.

## Elevation

Depth comes from rule weight and stacking order, not blur. So "elevation" here means two things.

**Rules (border weights):**
```css
--rule-hairline: 1px;   /* table rows, dividers inside a component */
--rule-medium:   2px;   /* inputs, cards, default component edge */
--rule-heavy:    4px;   /* section breaks, masthead, emphasis */
--rule-color:    var(--color-ink);   /* black */
```
Three weights is enough. Heavier means more structural, and that's the whole depth model.

**Layering:**
```css
--z-base: 0;
--z-sticky: 10;     /* sticky header */
--z-overlay: 20;    /* menus, popovers */
--z-modal: 30;
--z-toast: 40;
--scrim: rgb(0 0 0 / 0.6);   /* flat, no blur */
```
Overlays separate from the page with a `--rule-heavy` border and a solid fill, never a soft shadow.

**Decision for you:** a hard offset shadow with zero blur, such as `4px 4px 0 var(--color-ink)`, is a common way to lift popovers and menus. It stays within "no soft shadows", but it isn't strictly "rules only". I'd leave it out by default and add `--shadow-hard` only if menus look flat against the page in practice.

Also define `--focus-ring: 3px solid var(--color-accent)` with a positive `outline-offset`. It's the one place the tomato red does functional work, and it keeps keyboard focus clearly visible without any shadow.

## Motion

The default is none:

```css
--duration-none: 0ms;
--easing-none: linear;
```

- Hover, active, focus, open and close all snap. A state change is a hard swap, such as inverting to black fill or switching to red.
- If you want any softness, allow one optional token, `--duration-quick: 80ms`. Use it only for color changes on interactive states, never for movement, scale or fades.
- Don't define easing curves, spring values or a duration scale.
- `prefers-reduced-motion` then needs almost no handling. Just make sure nothing, including third-party components, introduces transitions.

## What to leave out

No blur, no `backdrop-filter`, no gradients for depth, no scale or translate on hover, and no skeleton shimmers. For loading, use static text like "Loading" or a blocky stepped indicator, using `steps()` if you must animate.

If you want, I can write these out as a tokens file in whatever format the site uses (CSS variables, Tailwind config or JSON for Style Dictionary).
