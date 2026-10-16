I couldn't save this to a file because the Write tool is disabled in this session. The full motion section is below, so you can paste it into your docs.

---

# Motion

Tallowfield motion is **quiet and crisp**, like a focused work tool. Dispatchers and shippers use this app all day, so motion has one job: show where something came from, what changed, or that an action worked. If a motion does none of those, don't add it.

You don't pick durations or easings. Pick a preset from the table below and use its tokens.

## Rules

1. **Use the tokens.** No raw `ms` values or `cubic-bezier()` in component code.
2. **Animate `transform` and `opacity` only.** The one exception is the table row expand (see below). Never use `transition: all`. List the properties.
3. **Enter eases out. Exit eases in and is shorter.** Things arrive fast and settle. They leave quickly.
4. **Never block input.** Don't disable controls or set `pointer-events: none` while something animates. A click during a motion reverses or retargets it.
5. **Things come from where they live.** A menu grows from its trigger. A side panel slides from its edge. A toast comes from its corner. Closing reverses the path.
6. **No bounce, no overshoot, no looping attention-getters.**
7. **Nothing over 300 ms.** The longest token is 280 ms. If something feels slow, check input latency and long tasks before you touch a duration.

## Tokens

```css
:root {
  /* Durations */
  --motion-duration-instant: 100ms; /* press, hover, menu exit */
  --motion-duration-fast:    150ms; /* menus, tooltips, toggles, row collapse */
  --motion-duration-base:    200ms; /* row expand, repositioning, panel/modal/toast exit */
  --motion-duration-slow:    280ms; /* modal, side panel, toast entrances */

  /* Easings */
  --motion-ease-enter: cubic-bezier(0.2, 0, 0, 1);   /* arriving: fast start, soft landing */
  --motion-ease-exit:  cubic-bezier(0.4, 0, 1, 1);   /* leaving: accelerates away */
  --motion-ease-move:  cubic-bezier(0.4, 0, 0.2, 1); /* on-screen A to on-screen B */
  /* Progress bars and spinners use `linear`. */

  /* Travel (zeroed under reduced motion, see below) */
  --motion-distance-sm: 4px;
  --motion-distance-md: 8px;
  --motion-distance-lg: 12px;
}
```

Exits run about a quarter to a third shorter than their entrance: slow → base, fast → instant.

## Presets

| Preset | Trigger | Properties | Enter | Exit | Easing (in / out) | Interruption | Reduced motion |
|---|---|---|---|---|---|---|---|
| **Press** | Pointer down or key down on any button, row, or tab | background-color, `scale(0.97)` | instant | instant | enter / exit | Retargets | Keep color change; drop scale |
| **Menu / popover** | Open or close dropdown, select, context menu | opacity, `scale(0.97 → 1)` from the trigger | fast | instant | enter / exit | Reverses from current value | Opacity only, instant |
| **Modal** | Open or close dialog | Dialog: opacity, `translateY(8px → 0)`. Scrim: opacity, same clock | slow | base | enter / exit | Reverses from current value | Opacity only, `fast` |
| **Side panel** | Open or close detail or edit panel | `translateX(100% → 0)` from its own edge. Scrim, if any, fades on the same clock | slow | base | enter / exit | Reverses from current value | Opacity only, `fast` |
| **Toast** | Toast appears or is dismissed | opacity, `translateY(12px → 0)` from its corner | slow | base | enter / exit | Dismiss during enter reverses | Opacity only, `fast` |
| **Toast restack** | A toast is removed and the others close the gap | `translateY` | base | n/a | move | Retargets | Instant |
| **Table row expand** | Click chevron or row to show detail | grid-row `0fr → 1fr`, opacity | base | fast | enter / exit | Reverses from current height | Opacity only, `fast`, no height animation |
| **Page navigation** | Route change | Changed region only: opacity `0 → 1` | fast | none | enter | A new navigation replaces it | Instant |
| **Value changed** | Data updates while the user is looking elsewhere (status, ETA, rate) | Background highlight, strong at once, fades out over 1000 ms, `linear` | n/a | n/a | n/a | Restarts on a new change | Keep (color only) |
| **Inline loading** | Button action takes longer than 300 ms | Spinner inside the button, same footprint | n/a | n/a | linear | n/a | Keep, slow the spin |

## Recipes

### Different timing for enter and exit

Put the transition on the destination state. The open state defines the enter, and the closed state defines the exit. Don't use keyframe animations for things that toggle, because they restart instead of reversing.

```css
.modal {
  opacity: 0;
  transform: translateY(var(--motion-distance-md));
  transition:
    opacity   var(--motion-duration-base) var(--motion-ease-exit),
    transform var(--motion-duration-base) var(--motion-ease-exit);
}
.modal[data-state="open"] {
  opacity: 1;
  transform: none;
  transition:
    opacity   var(--motion-duration-slow) var(--motion-ease-enter),
    transform var(--motion-duration-slow) var(--motion-ease-enter);
}

.scrim { opacity: 0; transition: opacity var(--motion-duration-base) var(--motion-ease-exit); }
.scrim[data-state="open"] {
  opacity: 1;
  transition: opacity var(--motion-duration-slow) var(--motion-ease-enter);
}
```

Side panel, toast, and menu use the same pattern with their own properties.

- **Keep an exiting element mounted until its transition ends** (`transitionend`, or your component library's presence handling). While it leaves, make it `inert` so it can't take focus or clicks.
- **Menus** set `transform-origin` to the trigger. Radix and Floating UI expose this as a CSS variable.
- **Modal focus:** move focus into the dialog on open and return it to the trigger on close. Don't wait for the animation.

### Table row expand

This is the one place height changes. Use the grid-row technique, not a measured `height` or `max-height`.

```css
.row-detail {
  display: grid;
  grid-template-rows: 0fr;
  opacity: 0;
  transition:
    grid-template-rows var(--motion-duration-fast) var(--motion-ease-exit),
    opacity            var(--motion-duration-fast) var(--motion-ease-exit);
}
.row-detail[data-state="open"] {
  grid-template-rows: 1fr;
  opacity: 1;
  transition:
    grid-template-rows var(--motion-duration-base) var(--motion-ease-enter),
    opacity            var(--motion-duration-base) var(--motion-ease-enter);
}
.row-detail > .inner { overflow: hidden; min-height: 0; }
```

- Don't animate if the detail is long (more than about 20 rows) or loads asynchronously. Show a skeleton and let it open instantly.
- Rotate the chevron with `transform`, using the same duration and easing as the open.

### Page navigation

Render the new page immediately. Fade in only the content region, and leave the header and nav untouched. Don't play an exit animation for the old page, and don't make anyone wait for a transition before they can read.

```css
.page-content { animation: page-in var(--motion-duration-fast) var(--motion-ease-enter); }
@keyframes page-in { from { opacity: 0; } }
```

Use `document.startViewTransition` only if you need to carry a shared element across (for example, a load card into its detail page). Fall back to an instant change where it isn't supported.

### Press feedback

```css
.button {
  transition:
    background-color var(--motion-duration-instant) var(--motion-ease-enter),
    transform        var(--motion-duration-instant) var(--motion-ease-enter);
}
.button:active { transform: scale(0.97); }
```

Don't move a control out from under the pointer on hover. Don't animate or remove focus rings.

## Waiting, results and errors

| Wait | What to show |
|---|---|
| Under about 300 ms | Nothing. Keep the UI still. |
| Over about 300 ms | Inline spinner **inside the button** that started it. Keep the button width and swap the label ("Booking…" then "Booked"). Once shown, keep it at least 400 ms so it doesn't flash. |
| Over about 1 s | Add text saying what is happening. |
| Content with a known layout (tables, panels) | Skeleton of the final shape. First paint is the loading state, never an empty frame. |

- **Toasts:** a plain notice stays 5 s. A toast with an action (such as "Undo") stays 8 s. Both pause on hover and focus. Use `role="status"` so screen readers announce it. Show at most 3 at once.
- **Optimistic updates:** only for easily reversible actions (such as starring a lane). If one fails, restore the old state and say why. **Never** use them for booking, tendering, payment, or delete.
- **Errors:** always show text near the problem, plus color and an icon. A single horizontal nudge of 4 px over 300 ms on the field is optional. Don't shake the form or scroll the page. Move focus to the first problem field and reserve space for the message so nothing jumps.
- **Live data:** when a value changes while the user is looking elsewhere, use the *Value changed* highlight. On busy tables, limit it to one pulse per batch. Don't animate numbers counting up. Show the new value.

## Reduced motion

Honor `prefers-reduced-motion: reduce`. Movement goes away, but opacity, color, and focus feedback stay. Don't write a blanket `transition: none`, because it strips focus and state feedback.

Because travel is a token, most of the work is one block:

```css
@media (prefers-reduced-motion: reduce) {
  :root {
    --motion-distance-sm: 0px;
    --motion-distance-md: 0px;
    --motion-distance-lg: 0px;
  }
  .side-panel { transform: none; }        /* fade instead of slide */
  .menu       { transform: none; }
  .button:active { transform: none; }
  .row-detail { grid-template-rows: 1fr; transition-property: opacity; }
  .row-detail:not([data-state="open"]) { display: none; }
  .spinner { animation-duration: 2s; }    /* calmer, still shows activity */
}
```

For JS-driven motion, read `matchMedia('(prefers-reduced-motion: reduce)')` before starting movement, and listen for changes.

## Adding something new

1. **What is its job?** Where it came from, what changed, or did it work. If none apply, don't animate.
2. **How often does it happen?** Many times a session means `fast` or `instant` and little travel. A few times a session means `base` or `slow`.
3. **Is there a preset?** Use it. Menu-like things use *Menu*. Overlays use *Modal* or *Side panel*. Message-like things use *Toast*.
4. **No preset fits?** Combine existing tokens, add a row to the table above, and have another designer review it. Don't add new durations or easings.

## PR checklist

- [ ] Only `--motion-*` tokens. No raw durations, no raw easings, no `transition: all`.
- [ ] Only `transform` and `opacity` animate (table row expand excepted).
- [ ] Exit is shorter than enter. Enter uses ease-enter, exit uses ease-exit.
- [ ] Clicking mid-animation reverses it. Nothing is disabled while it plays.
- [ ] Exiting elements are `inert` and removed after the transition.
- [ ] Reduced motion tested with the OS setting on: no movement, and focus and state changes still visible.
- [ ] Tested with CPU throttled 4x. No stutter.
- [ ] Nothing flashes more than three times per second. Nothing moves on its own for more than 5 s without a way to pause.

---

I assumed a plain-CSS web stack, a quiet and crisp tone, and no existing motion tokens. If you already have tokens or use a library like Framer Motion, tell me and I'll remap the names and recipes. I haven't tested the CSS in a browser.
