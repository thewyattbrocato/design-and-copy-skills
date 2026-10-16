I couldn't save this as a file because the Write tool is disabled in this session. The full section is below, ready to paste into your docs.

I assumed a web app with CSS transitions, and I set the tone to quiet and crisp because dispatchers use it all day. The tokens and durations are starting points. Try them in the real app and adjust before you lock them in.

---

# Motion

Tallowfield is a tool people use all day, so motion is quiet and crisp. It tells you where something came from, what changed, or that your action worked. Everything else is instant.

**The rules, in short**

1. Use the tokens below. Don't write your own milliseconds or cubic-beziers.
2. Animate `transform` and `opacity` only. Never use `transition: all`.
3. Nothing blocks input. Never disable a control or set `pointer-events: none` while something animates.
4. Exits are faster than entrances.
5. Every component below has a reduced-motion version. Ship it with the component.

---

## Tokens

```css
:root {
  /* Durations */
  --motion-instant: 120ms; /* hover, press, color change, collapse, menu exit */
  --motion-fast:    180ms; /* menus, row expand, page fade, exits of base */
  --motion-base:    240ms; /* modals, toasts, side panels */
  --motion-slow:    320ms; /* reserved; nothing here uses it. Ask design first. */

  /* Easings */
  --ease-enter: cubic-bezier(0.2, 0, 0, 1);   /* things arriving */
  --ease-exit:  cubic-bezier(0.4, 0, 1, 1);   /* things leaving */
  --ease-move:  cubic-bezier(0.4, 0, 0.2, 1); /* moving between two on-screen places */
  /* linear: only for real progress bars and looping spinners */

  /* Travel */
  --motion-shift-sm: 4px;    /* menus */
  --motion-shift-md: 8px;    /* modals, toasts */
  --motion-shift-edge: 100%; /* side panels, from their own edge */
}

@media (prefers-reduced-motion: reduce) {
  :root {
    --motion-shift-sm: 0px;
    --motion-shift-md: 0px;
    --motion-shift-edge: 0px;
  }
}
```

An exit uses one duration step shorter than its entrance (`base` in, `fast` out; `fast` in, `instant` out). Enter uses `--ease-enter` and exit uses `--ease-exit`. There is no stagger in this system.

---

## Components

| Component | Enter | Exit | Reduced motion |
|---|---|---|---|
| Menu / popover | `fast`, `ease-enter`, fade + move `shift-sm` from the trigger side | `instant`, `ease-exit`, fade only | Fade only, same durations |
| Modal | `base`, `ease-enter`, fade + rise `shift-md` | `fast`, `ease-exit`, fade only | Fade only |
| Toast | `base`, `ease-enter`, fade + move `shift-md` from its screen edge | `fast`, `ease-exit`, fade only | Fade only |
| Side panel | `base`, `ease-enter`, slide from its own edge | `fast`, `ease-exit`, slide back to that edge | Fade only, `instant` |
| Expandable table row | `fast`, `ease-enter`, height open + content fade | `instant`, `ease-exit`, height close + fade | Instant open and close |
| Page navigation | `fast`, `ease-enter`, content fade in, no movement | None. The old page is replaced immediately | Instant swap |

### Menu / popover
- The origin is the trigger. A menu under a button drops from it, and one above rises from it.
- There is no scrim.
- Opening a second menu while one is closing is fine. Each one retargets from its current state.

### Modal
- The scrim fades on the same duration and easing as the modal. It is opacity only.
- No scale-up and no bounce.
- Focus moves into the modal on open and returns to the trigger on close. This is required and isn't animated.
- Escape and the close button work immediately, even mid-enter.

### Toast
- It enters from the edge it's anchored to (bottom-right by default).
- Plain notices stay 4–8 s depending on length. A toast with an action ("Undo", "View load") stays at least 6–10 s and pauses on hover and focus. The action must still be reachable afterward (history or trash).
- Use `role="status"`, or `role="alert"` for errors. Motion tells a screen reader nothing.
- When toasts stack, the others slide to close the gap using `--motion-fast` and `--ease-move`. Don't let them snap.

### Side panel
- It slides from the edge it lives on and returns to that edge.
- Page content behind it doesn't animate. If the panel pushes content, the layout changes instantly and the panel slides in over the freed space.
- If the panel has a scrim, follow the modal rule.
- If the panel is already open and the user picks a different record, swap the contents with no slide. Only the first open and the final close slide.

### Expandable table row
Use the grid-rows technique, not a measured pixel height:

```css
.row-detail {
  display: grid; grid-template-rows: 0fr; opacity: 0;
  transition: grid-template-rows var(--motion-instant) var(--ease-exit),
              opacity var(--motion-instant) var(--ease-exit);
}
.row-detail[data-open="true"] {
  grid-template-rows: 1fr; opacity: 1;
  transition: grid-template-rows var(--motion-fast) var(--ease-enter),
              opacity var(--motion-fast) var(--ease-enter);
}
.row-detail > .inner { overflow: hidden; min-height: 0; }
```

- Rows below close the gap as the detail grows. They must never jump.
- If you auto-collapse another row, do it instantly.
- If the detail needs data, show a skeleton inside the opened row.

### Page navigation
- The header and side nav stay still. Only the content region changes.
- Render the new page as soon as it's ready. Never hold it back to play an exit animation.
- Fade the new content in at `fast`. There is no slide or direction, and back and forward behave the same.
- Use the View Transitions API for this crossfade where it's available, and swap instantly elsewhere.
- An object that continues across pages, such as the same load card on a list and its detail, may use a shared-element transition (`--motion-fast`, `--ease-move`). This is optional.

---

## Feedback and loading

| Moment | Rule |
|---|---|
| Hover on buttons, rows, links | Color change, `instant`, no movement. |
| Press on buttons | Pressed color plus `scale(0.98)`, `instant`. Required on every clickable control. |
| Focus | The ring appears immediately. Never animate it away. |
| Action under 300 ms | Show nothing. |
| Action over 300 ms | Inline spinner **inside the button that started it**, same footprint, no layout shift. Once shown, keep it at least 400 ms. |
| Action over 1 s | Add text saying what's happening ("Booking load…", "Uploading BOL…"). |
| Action over 10 s | Add steps or an estimate, plus Cancel. |
| Success | The button label swaps to "Saved" with a check. Use a toast if the person may have moved on. |
| Tables and panels loading | Content-shaped skeleton from first paint. Never blank, then skeleton. |
| Refetching | Keep the old data visible, dim it slightly, and swap when ready. |

**Live updates** (new bookings, status or ETA changes): dispatchers aren't always looking at the row that changed. Highlight the changed cell or row with a background color that starts strong and fades over about 1 s. Don't use movement or bounce, and don't reorder rows under someone's cursor. If many rows update at once, give one pulse per batch.

**Errors**
- Always show text near the field, plus an icon and color. Motion is never the only signal.
- A field may shake horizontally once, a few pixels, for 200–300 ms. Under reduced motion, drop the shake and keep the highlight and text.
- Reserve space for the message so nothing shifts under the cursor.
- Move focus to the first problem field. Never scroll to the top.

**Optimistic updates** are only for reversible actions that almost always succeed, such as flagging a load. On failure, restore the old state and say why. Never use them for booking confirmation, rate acceptance, payments or deletions.

---

## Reduced motion

We honor `prefers-reduced-motion: reduce`. It means less movement, not less feedback.

- **Remove:** slides, rises, shakes, height animation.
- **Keep:** fades, color changes, focus rings, selected and expanded states, and spinners that report real status.
- **Don't** write `* { transition: none !important }`. It strips focus and state feedback.
- The `--motion-shift-*` tokens go to `0px`, so anything using them degrades to a fade. Row height and the panel slide need explicit overrides:

```css
@media (prefers-reduced-motion: reduce) {
  .row-detail, .row-detail[data-open="true"] { transition: none; }
  .side-panel { transition: opacity var(--motion-instant) linear; transform: none; }
}
```

In JS, check `window.matchMedia('(prefers-reduced-motion: reduce)')` before starting movement, and listen for changes.

---

## Implementation patterns

Use state attributes and transitions, not keyframes, for anything that toggles. Transitions retarget if the user reverses mid-way, but keyframes restart.

```css
.menu {
  opacity: 0;
  transform: translateY(calc(var(--motion-shift-sm) * -1));
  transition: opacity var(--motion-instant) var(--ease-exit),
              transform var(--motion-instant) var(--ease-exit);
}
.menu[data-state="open"] {
  opacity: 1;
  transform: none;
  transition: opacity var(--motion-fast) var(--ease-enter),
              transform var(--motion-fast) var(--ease-enter);
}
```

- An exiting element stays in the DOM until its exit finishes. It must stop taking focus and clicks as soon as it starts leaving (use `inert`).
- Keep open and closed styles in the same stylesheet. If the animation never runs, the content must still be there.
- Use `will-change` only on elements about to animate, and remove it afterward.
- If something feels slow, measure first. Long tasks and delayed input cost more than a 240 ms transition.

---

## What we don't animate

- Content already on screen at page load.
- Numbers and totals. Show the value and don't count up.
- Table sorting and filtering. Rows swap instantly.
- Anything that loops forever on a persistent control.
- Hover effects that move the target away from the pointer.
- Scroll-triggered reveals and parallax.

## Adding something new

Ask whether the motion shows where something went, what changed, whether an action worked, or how to use something. If it answers none of those, don't animate it. If it does, take a duration and easing from the tokens, write the reduced-motion version, and add a row to the component table in the same PR. If you need a value that isn't a token, raise it with design instead of hardcoding it.

---

If you'd like it as a file, tell me where to put it, or enable Write and I'll save it as `motion.md` in the working directory.
