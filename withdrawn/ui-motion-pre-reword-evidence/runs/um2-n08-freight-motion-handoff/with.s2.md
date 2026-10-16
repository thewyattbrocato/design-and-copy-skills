I couldn't save this as a file because the Write tool is disabled in this session. The full section is below, so you can paste it into your docs. I assumed a calm, decisive feel, plain CSS, and no existing motion tokens. If you already have tokens or a brand motion word, tell me and I'll swap them in.

---

# Motion

**Feel: calm and decisive.** Things arrive, stop, and get out of the way. Dispatchers and shippers repeat the same actions all day. Motion exists to show where something came from or went, and to confirm that an action worked. Anything else is instant.

Don't pick your own durations or easings. Use the tokens below. If nothing here fits, ask the design team before inventing a value.

## Tokens

```css
:root {
  /* Durations */
  --duration-fast: 120ms;  /* hover, press, menu exit */
  --duration-quick: 160ms; /* menu enter, toast exit, row collapse, page crossfade */
  --duration-base: 200ms;  /* toast enter, row expand, modal/panel exit */
  --duration-slow: 280ms;  /* modal and side panel enter. Nothing is longer. */

  /* Easings */
  --ease-out: cubic-bezier(0.2, 0, 0, 1);      /* things arriving */
  --ease-in: cubic-bezier(0.4, 0, 1, 1);       /* things leaving */
  --ease-in-out: cubic-bezier(0.4, 0, 0.2, 1); /* things moving between two on-screen spots */
}
```

Rules that apply everywhere:

1. **Enter uses `--ease-out`, exit uses `--ease-in`.** Exits are always shorter than the matching entrance.
2. **Animate only `opacity` and `transform`**, plus color for hover and press. The one exception is the expandable row. Never use `transition: all`. List the properties.
3. **Never block input.** Don't disable buttons or set `pointer-events: none` while something animates. Use CSS transitions, not keyframes, for anything toggled. A second click then reverses from the current position.
4. **No bounce, overshoot or springs, and no stagger.** Table rows, lists and toast stacks appear together.
5. **No loader for waits under 1 second.** See [Waiting and feedback](#waiting-and-feedback).
6. **Honor reduced motion** using the variants below. Never use a blanket `* { transition: none }`, because it also removes focus and state feedback.

## Spec table

| Component | Trigger | Properties | Duration | Easing | Interrupt behavior | Reduced motion |
|---|---|---|---|---|---|---|
| Hover / press (buttons, rows, links) | pointer / pressed | `background-color`, `color`, `box-shadow`; press adds `scale(0.97)` on buttons only | fast (120) | `--ease-out` | Retargets instantly | Keep color; drop the scale |
| Menu / popover | open | `opacity 0→1`, `scale 0.98→1`, `translateY(-4px)→0`, origin at trigger | quick (160) | `--ease-out` | Closing mid-open reverses from the current value | Opacity only |
| | close | opacity to 0 | fast (120) | `--ease-in` | | Same |
| Modal | open | dialog `opacity 0→1`, `scale 0.98→1`; scrim fades on the same clock | slow (280) | `--ease-out` | Esc and scrim click work at any moment | Opacity only |
| | close | opacity to 0, `scale 1→0.98` | base (200) | `--ease-in` | | Same |
| Side panel | open | `translateX(100%)→0` from its own edge; scrim fades with it | slow (280) | `--ease-out` | Close reverses from the current position | Opacity only, no slide |
| | close | back to the edge it came from | base (200) | `--ease-in` | | Same |
| Toast | arrive | `opacity 0→1`, `translateY(8px)→0` | base (200) | `--ease-out` | Hover or focus pauses the dismiss timer | Opacity only |
| | dismiss | opacity to 0 | quick (160) | `--ease-in` | | Same |
| Expandable table row | toggle | detail height via `grid-template-rows 0fr↔1fr` plus `opacity`; chevron `rotate(90deg)` | open base (200), close quick (160) | `--ease-out` open, `--ease-in` close | Re-click reverses | Instant height change; chevron swaps with no rotation |
| Row insert / remove / reorder (live updates) | data change | position via `transform` (FLIP); removed rows fade 120, then collapse | base (200) | `--ease-in-out` | New data retargets | Instant |
| Page navigation | route change | crossfade the content region only; header and nav stay still | quick (160) | `--ease-out` | A new click replaces the transition | Instant swap |

Toast timing: a toast stays for 6 s, or indefinitely if it has an action or is an error. Announce toasts through a live region (`role="status"`, or `role="alert"` for errors).

## Implementation patterns

### Menu, modal, toast

```css
.menu {
  transform-origin: var(--trigger-origin, top left);
  transition:
    opacity var(--duration-fast) var(--ease-in),
    transform var(--duration-fast) var(--ease-in),
    display var(--duration-fast) allow-discrete;
}
.menu[data-open] {
  transition-duration: var(--duration-quick);
  transition-timing-function: var(--ease-out);
}
.menu:not([data-open]) { opacity: 0; transform: scale(0.98) translateY(-4px); }

@starting-style {
  .menu[data-open] { opacity: 0; transform: scale(0.98) translateY(-4px); }
}
```

Modals and toasts use the same shape with the values from the table. Keep start and end styles in the same rule set, so the content is still visible if the animation never runs. An exiting element must stop taking clicks and focus as soon as it starts leaving. Use `inert`, or `display: none` via `allow-discrete`.

### Side panel

```css
.panel {
  transform: translateX(100%);
  transition: transform var(--duration-base) var(--ease-in);
}
.panel[data-open] {
  transform: none;
  transition: transform var(--duration-slow) var(--ease-out);
}
.panel-scrim { opacity: 0; transition: opacity var(--duration-base) var(--ease-in); }
.panel-scrim[data-open] { opacity: 1; transition: opacity var(--duration-slow) var(--ease-out); }
```

### Expandable row

```css
.row-detail {
  display: grid;
  grid-template-rows: 0fr;
  opacity: 0;
  transition:
    grid-template-rows var(--duration-quick) var(--ease-in),
    opacity var(--duration-quick) var(--ease-in);
}
.row-detail > * { overflow: hidden; }
.row-detail[data-open] {
  grid-template-rows: 1fr;
  opacity: 1;
  transition-duration: var(--duration-base);
  transition-timing-function: var(--ease-out);
}
```

This is the one place we animate a layout property. It's a small, bounded region, so don't copy it to large containers. Keep `aria-expanded` on the toggle button.

### Page navigation

```js
function navigate(update) {
  if (!document.startViewTransition || matchMedia('(prefers-reduced-motion: reduce)').matches) {
    return update();
  }
  document.startViewTransition(update);
}
```

```css
::view-transition-group(root) {
  animation-duration: var(--duration-quick);
  animation-timing-function: var(--ease-out);
}
```

Give the header and sidebar a `view-transition-name` so they stay still. Content must be readable immediately. If a page is slow, show its skeleton right away. Never hold the old page on screen waiting for a transition. Back navigation uses the same crossfade.

### Reduced motion

Write the reduced variant next to the normal one. Remove movement and scale. Keep opacity, color and focus.

```css
@media (prefers-reduced-motion: reduce) {
  .menu, .modal, .toast { transform: none; transition-duration: var(--duration-fast); }
  .panel { transform: none; opacity: 0; transition: opacity var(--duration-fast) linear; }
  .panel[data-open] { opacity: 1; }
  .row-detail { transition: none; }
  .btn:active { transform: none; }
}
```

In JS, check `matchMedia('(prefers-reduced-motion: reduce)')` before starting any movement-based animation, such as FLIP reorders or view transitions.

## Waiting and feedback

| Wait | What to show |
|---|---|
| Under ~100 ms | Pressed state only |
| 100 ms to 1 s | Nothing new. Keep the UI still. |
| Over 1 s | Progress inside the control that started it, shown after a 200 ms delay and held at least 400 ms |
| Over 10 s | Steps or an estimate, plus a Cancel |

- **Buttons:** keep the width. Swap the label ("Booking…" then "Booked") in the same footprint. Don't disable unrelated controls.
- **Tables and panels loading:** use content-shaped skeletons, not spinners. First paint is already the skeleton, never an empty frame. Stale data stays visible, slightly dimmed, during a refetch.
- **Live updates** (a new load posted, a status changed) away from where the user is looking: highlight the row with a background that starts strong and fades over 1 s. Limit it to one pulse per batch.
- **Errors:** show persistent text next to the field, with an icon and color. Move focus to the message or the first bad field. No layout jump and no scroll to top. An optional 4 px horizontal shake of the field (240 ms) is allowed. Under reduced motion the shake is dropped and the text and highlight stay.
- **Optimistic updates:** fine for reversible things, like starring a lane. Show the rollback if it fails. Never use them for booking confirmation, payment, rate acceptance or anything irreversible. Those show a pending state and prevent double submit.
- **Destructive removal** (such as deleting a saved lane): fade 120, collapse the space 200, and offer Undo.

## Don't

- Fade-up on scroll, parallax, count-ups on load, or looping pulses.
- `transition: all`, or animating `width`, `height`, `top` or `left` on anything large.
- Different durations or curves per screen for the same kind of element.
- Moving a click target out from under the pointer.
- Disabling controls, or ignoring clicks, until an animation ends.
- Toasts that travel across the screen, or modals that grow from the page edge.

## Adding something new

1. Name its job: orient, focus attention on a change, show cause and effect, or confirm an action. "It looks nice" means skip it.
2. Ask how often a dispatcher hits it. Frequent means fast or none.
3. Reuse the nearest row in the spec table. Enter uses `--ease-out`, exit uses `--ease-in`, and exits are shorter.
4. Check that a second click or Esc during the animation works.
5. Write the reduced-motion variant.
6. Add a row to the spec table in the same PR.

## Review checklist

- [ ] Durations and easings are tokens, with no raw `ms` or `cubic-bezier` in component CSS
- [ ] Only `opacity` and `transform` animate (expandable row excepted)
- [ ] Enter eases out, exit eases in and is shorter
- [ ] Nothing is disabled or click-blocked during motion
- [ ] A reduced-motion variant exists, and focus and state styles still transition
- [ ] No loader shows for waits under 1 s
- [ ] Tested with CPU throttled, with no empty frame before a skeleton

---

I haven't run or tested any of the CSS. The menu is 160 ms, shorter than the usual 200 to 300 ms for menus, because dispatchers open menus constantly. If you want it to feel slightly softer, raise the menu and toast enters by one token step.
