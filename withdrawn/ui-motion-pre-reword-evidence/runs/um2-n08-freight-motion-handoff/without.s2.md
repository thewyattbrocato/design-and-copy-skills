# Motion

Motion in Tallowfield explains what changed on screen. It never decorates. Dispatchers repeat the same actions hundreds of times a day, so every animation has to be fast enough to disappear. If you notice the animation, it's too slow or too big.

## Rules

1. **Use tokens only.** Never write a raw `ms` value or `cubic-bezier()` in component code.
2. **Exits are faster than entrances.** Leaving UI shouldn't make people wait.
3. **Animate `opacity` and `transform`.** The one exception is expandable rows (see below). Never animate `top`, `left`, `width`, or `margin`.
4. **Never block input.** Everything stays clickable and typeable while it animates. Don't disable a control "until the animation finishes."
5. **Don't animate data.** Values, statuses, and table content update instantly. We never fade or slide a load's status, rate, or ETA, because a dispatcher scanning a table needs it to be stable.

## Tokens

```css
:root {
  /* Durations */
  --duration-instant: 80ms;   /* menu close, tiny state changes */
  --duration-fast:    120ms;  /* menu open, most exits, chevrons, hover/focus */
  --duration-base:    200ms;  /* modal open, toast enter, row expand */
  --duration-slow:    280ms;  /* side panel open: the largest surface we animate */

  /* Easings */
  --ease-enter: cubic-bezier(0, 0, 0.2, 1);    /* things arriving: starts fast, settles */
  --ease-exit:  cubic-bezier(0.4, 0, 1, 1);    /* things leaving: accelerates away */
  --ease-move:  cubic-bezier(0.4, 0, 0.2, 1);  /* things already on screen that move or resize */

  /* Distances */
  --motion-shift: 8px;   /* small slide offset for menus and toasts */
  --motion-scale: 0.97;  /* starting scale for modals */
}
```

**Choosing an easing**
- Appearing: `--ease-enter`.
- Disappearing: `--ease-exit`.
- Already visible and changing position or size: `--ease-move`.
- Spinners and indeterminate progress bars: `linear`. Nothing else uses it.

**Nothing is slower than 280ms.** If you think you need more, the interaction probably needs a different design.

## Component recipes

| Component | Enter | Exit | Properties |
|---|---|---|---|
| Menu / dropdown | `fast`, `enter` | `instant`, `exit` | opacity, translateY(-8px → 0) |
| Modal | `base`, `enter` | `fast`, `exit` | opacity, scale(0.97 → 1); scrim fades with opacity only |
| Toast | `base`, `enter` | `fast`, `exit` | opacity, translateY(8px → 0) |
| Side panel | `slow`, `enter` | `base`, `exit` | translateX(100% → 0); scrim fades with opacity |
| Expandable row | `base`, `move` | `fast`, `move` | grid row height; chevron rotates 90° over `fast` |
| Page navigation | `fast`, `enter` | none | opacity on the content area only |

### Menus
- Set `transform-origin` to the trigger's edge, so the menu grows from the button.
- Submenus use the same recipe. Open them immediately on hover or arrow key, with no hover delay beyond the usual safe-triangle.
- On close, fade only (no slide).

```css
.menu[data-state="open"]   { animation: menu-in  var(--duration-fast)    var(--ease-enter); }
.menu[data-state="closed"] { animation: menu-out var(--duration-instant) var(--ease-exit); }

@keyframes menu-in  { from { opacity: 0; transform: translateY(calc(var(--motion-shift) * -1)); } }
@keyframes menu-out { to   { opacity: 0; } }
```

### Modals
- The dialog scales from the center. The scrim fades but doesn't scale.
- Focus moves into the dialog immediately, not after the animation.
- Stacked modals aren't allowed. If you need one, you need a different pattern.

```css
.modal[data-state="open"]   { animation: modal-in  var(--duration-base) var(--ease-enter); }
.modal[data-state="closed"] { animation: modal-out var(--duration-fast) var(--ease-exit); }
.scrim[data-state="open"]   { animation: fade-in   var(--duration-base) var(--ease-enter); }
.scrim[data-state="closed"] { animation: fade-out  var(--duration-fast) var(--ease-exit); }

@keyframes modal-in  { from { opacity: 0; transform: scale(var(--motion-scale)); } }
@keyframes modal-out { to   { opacity: 0; transform: scale(var(--motion-scale)); } }
@keyframes fade-in   { from { opacity: 0; } }
@keyframes fade-out  { to   { opacity: 0; } }
```

### Toasts
- Enter from the edge they're anchored to (bottom-right by default).
- When a toast is removed, the toasts around it slide to close the gap using `--duration-base` and `--ease-move`. Don't make them jump.
- Pausing on hover/focus is required. Toast timing:
  - Success and info auto-dismiss after 5s.
  - Errors and anything with an action stay until dismissed.

```css
.toast[data-state="open"]   { animation: toast-in  var(--duration-base) var(--ease-enter); }
.toast[data-state="closed"] { animation: toast-out var(--duration-fast) var(--ease-exit); }
.toast-stack > .toast       { transition: transform var(--duration-base) var(--ease-move); }

@keyframes toast-in  { from { opacity: 0; transform: translateY(var(--motion-shift)); } }
@keyframes toast-out { to   { opacity: 0; } }
```

### Side panels
- The panel slides in from the right. It's the only place we use a full-distance slide.
- If the panel is non-modal (the table behind stays usable), don't show a scrim and don't shift the page content. Overlay it.

```css
.panel[data-state="open"]   { animation: panel-in  var(--duration-slow) var(--ease-enter); }
.panel[data-state="closed"] { animation: panel-out var(--duration-base) var(--ease-exit); }

@keyframes panel-in  { from { transform: translateX(100%); } }
@keyframes panel-out { to   { transform: translateX(100%); } }
```

### Expandable table rows
Rows are the most repeated interaction in the product, so keep this one tight.
- Put the detail content in a full-width cell (`colspan`) containing a wrapper. Animate the wrapper, not the `<tr>`.
- Use the `grid-template-rows: 0fr → 1fr` technique. This is the one sanctioned layout animation, because the content height is unknown.
- Fade the content in with the expand. Don't stagger or delay it.
- Rows below the expanded one move as a natural result of the height change. Don't add separate animation for them.
- If you're expanding or collapsing more than ~10 rows at once ("Expand all"), skip the animation and switch instantly.

```css
.row-detail         { display: grid; grid-template-rows: 0fr; opacity: 0;
                      transition: grid-template-rows var(--duration-fast) var(--ease-move),
                                  opacity var(--duration-fast) var(--ease-exit); }
.row-detail > div   { overflow: hidden; }
.row[aria-expanded="true"] + .row-detail-wrap .row-detail {
                      grid-template-rows: 1fr; opacity: 1;
                      transition-duration: var(--duration-base);
                      transition-timing-function: var(--ease-move), var(--ease-enter); }
.row .chevron       { transition: transform var(--duration-fast) var(--ease-move); }
.row[aria-expanded="true"] .chevron { transform: rotate(90deg); }
```

### Page navigation
- The app shell (nav, header) never animates between routes.
- The content area fades in over `--duration-fast`. There's no exit animation and no slide, so the new page starts rendering right away.
- Don't hold the old page on screen to play an exit. Show the new route's skeleton right away if the data isn't ready.
- Don't use shared-element or view transitions between routes.

```css
.page { animation: fade-in var(--duration-fast) var(--ease-enter); }
```

## Hover, focus, and press
- Color, background, and border changes on hover/focus use `--duration-fast` and `--ease-move`.
- Focus rings appear instantly. Never delay or fade an indicator keyboard users depend on.
- Don't use scale or translate on buttons.

## Loading
- Don't show a spinner until a request has been pending for 300ms. Short waits shouldn't flash UI.
- Once a spinner shows, keep it visible for at least 400ms to avoid flicker.
- Skeletons don't shimmer. A static placeholder is fine, since shimmer on a dense table is noisy.

## Reduced motion

Users with `prefers-reduced-motion: reduce` get fades only: no sliding, scaling, or height animation. Add this once, globally. Components built on the tokens above need no extra work.

```css
@media (prefers-reduced-motion: reduce) {
  :root {
    --motion-shift: 0px;
    --motion-scale: 1;
  }
  .panel[data-state] { animation-name: fade-in-or-out; } /* see note below */
  .row .chevron      { transition: none; }
  .row-detail        { transition-property: opacity; grid-template-rows: 1fr; }
}
```

Notes:
- Define `fade-in-or-out` as plain opacity keyframes keyed on `data-state` for the side panel, since its slide uses `100%` and isn't covered by the tokens.
- Row detail under reduced motion should show and hide with opacity only. No height animation.
- Spinners may keep rotating. Reduced motion is about large movement, not about hiding that something is loading.
- In JS, check `window.matchMedia('(prefers-reduced-motion: reduce)').matches` before running any animation that doesn't go through these CSS tokens.

## Do and don't

| Do | Don't |
|---|---|
| `transition: opacity var(--duration-fast) var(--ease-exit)` | `transition: all 0.3s ease` |
| Make exits faster than entrances | Use the same duration for both |
| Update table data instantly | Fade or count up numbers in the table |
| Keep controls usable mid-animation | Disable buttons while a panel finishes opening |
| Use `--ease-move` for things that resize | Use `--ease-enter` for repositioning |
| Add a new token and update this page if you need something new | Add a one-off `350ms` in your component |

## Adding or changing motion

If none of the tokens fit, raise it in the design channel before shipping. If it's a real gap, we add a token here. Otherwise, we fix the design so it fits. Before merging, check:

- [ ] Only tokens are used, with no raw durations or curves.
- [ ] Exit is faster than enter.
- [ ] Only `opacity` and `transform` are animated, apart from row expansion.
- [ ] It works with reduced motion on.
- [ ] Keyboard and focus behavior doesn't wait on the animation.

---

A few things to check before publishing, since I picked them without your product data:
- The specific timings (80/120/200/280ms) and the 5s toast duration are my defaults for a dense, repeat-use tool. Tune them against how the app feels.
- The reduced-motion block needs a matching fade-only keyframe for the side panel. I left that as a note rather than inventing names that may clash with your CSS.
- The examples assume `data-state="open|closed"` attributes (as Radix and similar libraries use). If you use another mechanism, such as classes, the selectors will need adjusting.
