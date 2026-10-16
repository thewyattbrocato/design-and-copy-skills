I couldn't save this to a file because the Write tool is disabled in this session. The full section is below, so you can paste it into your docs.

---

# Motion

Tallowfield motion is **quiet and crisp, like a focused dispatch tool**. Dispatchers open menus, expand rows and change pages hundreds of times a shift. Motion exists to show where something came from, what changed, or that an action worked. Everything else is instant.

**Use the tokens and presets below. Don't write your own durations or easings.** If nothing fits, ask the design team and we'll add a preset.

## 1. Tokens

```css
:root {
  /* Durations */
  --motion-fast: 120ms;        /* hover, press, color, chevrons */
  --motion-base: 200ms;        /* menus, row expand, small reveals */
  --motion-slow: 280ms;        /* modals, side panels, toasts */
  --motion-exit-base: 140ms;   /* exits are shorter than entrances */
  --motion-exit-slow: 200ms;

  /* Easings */
  --ease-out:    cubic-bezier(0.2, 0, 0, 1);    /* things arriving */
  --ease-in:     cubic-bezier(0.4, 0, 1, 1);    /* things leaving */
  --ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);  /* moving between two on-screen spots */
  /* linear: only for progress bars and looping spinners */

  /* Travel */
  --motion-shift-sm: 4px;      /* menus, tooltips */
  --motion-shift-md: 12px;     /* modals, toasts */
}
```

Four rules cover most cases:

1. **Enter uses ease-out. Exit uses ease-in and is shorter.**
2. **Animate only `transform` and `opacity`.** Color, background-color and box-shadow are also fine for hover and press. Never use `transition: all`; always list the properties.
3. **Never block input.** Don't disable buttons or set `pointer-events: none` while something animates. A click during an opening reverses it.
4. **No stagger.** Table rows, menu items and toasts all arrive together.

## 2. Presets

| Preset | Trigger | Properties | Duration | Easing | Interruption | Reduced motion |
|---|---|---|---|---|---|---|
| `press` | Hover or `:active` on buttons, rows, links, tabs | `background-color`, `color`, `box-shadow`. Buttons also get `scale(0.98)` on `:active`. | `--motion-fast` | out | Retargets from the current value | Keep color, drop scale |
| `menu` | Dropdown, select, context menu, popover | `opacity` 0→1, `translateY(-4px)`→0 | In: `--motion-base`. Out: 120ms | In: out. Out: in | Reverses from the current value | Opacity only, 100ms |
| `modal` | Dialog open and close | Dialog: `opacity`, `translateY(12px)`→0. Scrim: `opacity` on the same clock. | In: `--motion-slow`. Out: `--motion-exit-slow` | In: out. Out: in | Reverses | Opacity only, 150ms, both layers |
| `panel` | Side panel (load details, filters) | `translateX(100%)`→0 from its own edge. Scrim: `opacity`. | In: `--motion-slow`. Out: `--motion-exit-slow` | In: out. Out: in | Reverses | Opacity only, 150ms |
| `toast` | Toast appears or dismisses | `opacity`, `translateY(12px)`→0 from its screen edge | In: `--motion-slow`. Out: `--motion-exit-base` | In: out. Out: in | Dismiss works at any point | Opacity only, 150ms |
| `row-expand` | Expand or collapse a table row | Detail region: grid-row `0fr`→`1fr` plus `opacity`. Chevron: `rotate`. | Expand: `--motion-base`. Collapse: `--motion-exit-base`. Chevron: `--motion-fast`. | In: out. Out: in | Reverses; rows below move with it | Instant height, 100ms opacity |
| `page` | Route change | Content region only: `opacity` crossfade | 160ms | out | A new navigation replaces the one in flight | Same (opacity is fine) |
| `value-flash` | A live value changed (status, ETA, rate) | `background-color` highlight, strong at once, then fading | 1000ms | out | A new change restarts the fade | Keep (it's a color change) |
| `field-error` | Validation fails | Optional 4px horizontal shake, plus persistent text and icon | 300ms | in-out | n/a | Drop the shake, keep text, icon and color |

If a motion isn't in this table, don't add it. When in doubt, use none.

## 3. Component guidance

**Menus and popovers**
- Set `transform-origin` to the trigger, not the center.
- Run the selected action immediately. Don't wait for the exit to finish.
- Item hover uses `press`; nothing moves.

**Modals**
- The scrim and dialog fade on the same clock.
- No scale-from-zero, bounce or overshoot.
- Focus moves into the dialog on open and returns to the trigger on close, independent of the animation. Esc closes immediately.

**Side panels**
- Enter from the edge the panel lives on and leave toward that same edge.
- The page behind doesn't shift or scale.
- Panel width is fixed and the panel translates. Never animate `width`.

**Toasts**
- Stack from one screen edge. When one dismisses, the others close the gap with `--motion-base` and `--ease-in-out`.
- A plain notice stays about 5 s, longer for long text. A toast with an action (such as "Undo") stays at least 8 s. Both pause on hover and keyboard focus.
- Use `role="status"` for success and info, and `role="alert"` for errors.
- Errors that need a decision shouldn't be toasts.

**Expandable table rows**
- Use the grid-row technique: `grid-template-rows: 0fr`→`1fr` on a wrapper, with the inner element set to `overflow: hidden; min-height: 0`. Don't use `max-height` or a measured pixel height.
- Only the toggled row animates, with no stagger.
- Expanding a second row while one is closing runs both at once; nothing waits.
- Live data refreshes must not make an expanded row jump.

**Page navigation**
- Header and side nav never animate on navigation.
- The content region gets a 160ms crossfade, with no slide or direction. Back and forward behave the same.
- **Never delay a page for the transition.** Render the new route immediately, show skeletons for data, and let the crossfade play over it.
- Use the View Transitions API where it exists, and an instant swap where it doesn't.
- The first paint of a route is the skeleton, never an empty frame.

**Buttons and loading**
- Acknowledge every press within 100ms with `press`.
- Under 300ms, show nothing. After 300ms, show a spinner inside the button that started the action, keeping the button's width. Once shown, keep it at least 400ms so it doesn't flash.
- Past 1 s, add text ("Booking load…"). Past 10 s, add steps or an estimate, plus Cancel.
- Success swaps the label ("Saved", "Booked") with a check, in the same footprint. No confetti.
- Use skeletons where the layout is known, with no shimmer or a very slow one.

**Live data (dispatch boards, rates, ETAs)**
- Use `value-flash` on the changed value only.
- Rate-limit it to one flash per batch of updates, and skip trivial changes.
- Never reorder rows on their own while someone is working in the table.

**Errors**
- Always pair the error with text near the field and an icon. The shake is optional.
- Inserting the message must not move the focused field, so reserve its space.
- Move focus to the first invalid field or the message. Don't scroll to the top.

## 4. Reduced motion

Honor `prefers-reduced-motion: reduce` everywhere. **Remove movement and keep feedback.** That means no slides, shakes or scale. Opacity, color, focus rings and every state change stay.

Don't use a blanket `* { transition: none }`. It strips focus and state feedback. Build the reduced variant into each component:

```css
.panel {
  transition: transform var(--motion-slow) var(--ease-out),
              opacity var(--motion-slow) var(--ease-out);
}
.panel[data-state="closed"] {
  transform: translateX(100%);
  opacity: 0;
  transition-duration: var(--motion-exit-slow);
  transition-timing-function: var(--ease-in);
}
@media (prefers-reduced-motion: reduce) {
  .panel,
  .panel[data-state="closed"] {
    transform: none;
    transition: opacity 150ms linear;
  }
}
```

In JS (Web Animations, Framer Motion and so on), read `matchMedia('(prefers-reduced-motion: reduce)')`, branch before starting any movement, and listen for changes.

## 5. Implementation notes

- **Use CSS transitions driven by a `data-state` or class change.** They retarget from the current value, so interruptions are smooth. Keep `@keyframes` for spinners, skeleton shimmer and `field-error`.
- **Exiting elements stay in the DOM until the exit ends.** They stop taking focus and clicks as soon as they start leaving.
- **Keep start and end styles in the same stylesheet.** If the animation never runs, the final state must still be correct and visible.
- Use `will-change` only briefly, on elements about to animate.
- Don't animate `width`, `height`, `top`, `left` or `margin` on large elements. `row-expand`'s grid-row technique is the one exception.
- Test with 4x CPU throttling and a throttled network. If something feels slow, measure input latency and long tasks before touching durations.

**PR checklist for anything touching motion**
- [ ] Uses `--motion-*` and `--ease-*` tokens, with no literal ms or `cubic-bezier` values
- [ ] Matches a preset in section 2, or the design team approved a new one
- [ ] Exit is shorter than enter; enter eases out and exit eases in
- [ ] Nothing is disabled or click-blocked during the animation
- [ ] Reduced-motion variant exists and keeps focus and state feedback
- [ ] Only `transform` and `opacity` (plus color for hover and press)
- [ ] Nothing flashes more than 3 times per second, and nothing loops forever except a loading spinner

## 6. What we deliberately don't animate

- Scroll reveals, parallax, and entrance animations on page load
- Numbers counting up
- Bounce or overshoot on any control
- Staggered lists
- Hover effects that move the target out from under the cursor
- Anything on keystrokes, typing or scrolling
- Slide or zoom page transitions
- Looping attention-getters on buttons or badges

A rare first-run moment, such as a first booking, may get something richer, up to 500ms and skippable. Check with design first.

---

**Assumptions to check.** I assumed web, plain CSS transitions and a "quiet and crisp" tone, since you gave no existing tokens or brand brief. If you already have some values in code, I can fold them in so the doc matches what's shipped. If you have a brand motion trait, I can change the tone. If you use a motion library, the presets map directly, but the implementation notes would change.
