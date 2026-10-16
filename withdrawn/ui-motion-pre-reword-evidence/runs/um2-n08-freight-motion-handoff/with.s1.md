I couldn't save this to a file because the Write tool is disabled in this session. Here is the full section as markdown. You can paste it into your docs as `motion.md`, or re-enable Write and I'll create the file.

---

# Motion

**Feel: calm and decisive.** Things arrive, settle and stop. There's no bounce, no overshoot and little travel. Dispatchers use this tool all day, so motion exists to show where something came from or that an action worked. Everything else is instant.

## Rules

1. **Use the tokens below.** Don't write raw milliseconds or `cubic-bezier()` values in components.
2. **Animate `opacity` and `transform` only.** The one exception is expandable rows. Never use `transition: all`. List the properties.
3. **Everything is interruptible.** Use CSS transitions, not keyframes, for anything that toggles. Never disable a button or set `pointer-events: none` while something animates.
4. **Exits are faster than entrances.** Users already know what's leaving.
5. **Things come from where they live.** A menu grows from its trigger, a side panel slides from its edge, a toast rises from its corner.
6. **Frequent means quiet.** Hover, menus, row expansion and page changes happen dozens of times an hour, so keep them short and small.
7. **No motion on load.** Content already on screen at page load doesn't fade or slide in.

## Tokens

```css
:root {
  /* Durations */
  --motion-fast: 120ms;      /* hover, press, color, menu close, page content fade */
  --motion-base: 200ms;      /* menu open, row expand, small reveals */
  --motion-slow: 280ms;      /* modal, side panel, toast entering */
  --motion-exit-slow: 200ms; /* modal, side panel, toast leaving */

  /* Easings */
  --ease-enter: cubic-bezier(0.2, 0, 0, 1);   /* arriving: fast start, soft landing */
  --ease-exit:  cubic-bezier(0.4, 0, 1, 1);   /* leaving */
  --ease-move:  cubic-bezier(0.4, 0, 0.2, 1); /* moving between two on-screen places */
}
```

Use `linear` only for progress bars and spinners. There is no stagger token, because nothing in the product staggers.

## Component specs

| Component | Trigger | Properties | Duration | Easing | Origin | Interrupt | Reduced motion |
|---|---|---|---|---|---|---|---|
| **Button / row hover, press** | hover, `:active` | `background-color`, `box-shadow`; press adds `scale(0.98)` | fast | enter | None. Never move the target. | Retargets | Keep color, drop scale |
| **Menu** open | click or key | `opacity` 0→1, `scale(0.97)`→1 | base | enter | `transform-origin` at the trigger | Close mid-open reverses | Opacity only, fast |
| Menu close | Esc, outside click, select | `opacity` 1→0 | fast | exit | n/a | Reopen mid-close reverses | Same |
| **Modal** open | open | Dialog: `opacity` 0→1, `translateY(8px)`→0. Scrim: `opacity` 0→1 | slow | enter | Centered, slight rise. Scrim shares the clock. | Close mid-open reverses | Opacity only, fast |
| Modal close | close, Esc, scrim | Dialog and scrim `opacity` 1→0, no translate | exit-slow | exit | n/a | Reversible | Same |
| **Side panel** open | open | Panel `translateX(100%)`→0; scrim fades in | slow | enter | Right edge | Reverses from current position | Opacity only, fast, no slide |
| Side panel close | close, Esc, scrim | Panel →100%, scrim fades out | exit-slow | exit | Back to the right edge | Reversible | Same |
| **Toast** enter | system event | `opacity` 0→1, `translateY(8px)`→0 | slow | enter | Its screen corner | n/a | Opacity only, fast |
| Toast exit | timeout, dismiss | `opacity` 1→0 | exit-slow | exit | n/a | Hover or focus pauses the timer and cancels the exit | Same |
| Toast stack reflow | a toast leaves | `translateY` on toasts below | base | move | Neighbors close the gap | Retargets | Instant |
| **Expandable row** | click, Enter, Space | Detail height (`grid-template-rows` 0fr→1fr), inner `opacity`, chevron `rotate(90deg)` | base open, fast close | enter open, exit close | Opens downward | Reverses mid-way | Instant height, chevron state kept |
| **Page navigation** | route change | New content region `opacity` 0→1 | fast | enter | None | A new navigation replaces the one in flight | Instant swap |

## Notes by component

**Menus.** Menus are the most-used overlay, so they get the smallest motion in the system: a short fade with a 3% scale. Don't add slides or item stagger. Keyboard and pointer users get the same animation.

**Modals.** Reserve modals for decisions and forms that need focus. Dialog and scrim run on the same clock. On close, the dialog fades without translating. For confirm-and-submit modals (book, cancel load, delete), show a pending state in the primary button and block double submit.

**Side panels.** Panels (load details, shipper info, filters) always slide from the right and return the same way. If a user opens a different record while a panel is open, swap the content in place with a `fast` opacity change. Don't close and reopen the panel.

**Toasts.**
- Position them bottom-right, stacked upward, with a maximum of 3 visible.
- Auto-dismiss after 5 s. Errors and toasts with an action stay until dismissed.
- Pause the timer on hover and focus.
- Use `role="status"`, or `role="alert"` for errors. The text carries the message, never the motion.

**Expandable table rows.** Tables are the core of the app, so this must never slow scanning.

```css
.row-detail {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows var(--motion-fast) var(--ease-exit);
}
.row-detail[data-open="true"] {
  grid-template-rows: 1fr;
  transition: grid-template-rows var(--motion-base) var(--ease-enter);
}
.row-detail > .inner { overflow: hidden; min-height: 0; }
```

- Put the wrapper inside a single `<td colspan>` of a detail row, because `<tr>` height can't be animated.
- "Expand all" is instant.
- Row hover is a background color only. Rows never move on hover.

**Page navigation.** Dispatchers jump between screens constantly, so changes should feel immediate.
- Keep the header and sidebar completely still.
- Render the new page right away. Don't wait on an exit animation, and don't replay the old page's exit.
- Only the main content region fades in. Skip the fade for tabs within a page.
- Start in the skeleton state on first paint. Never go blank, then skeleton, then content.
- If you use View Transitions, limit them to a crossfade of the content region, with an instant swap as the fallback.

## Loading and feedback

| Wait | Do |
|---|---|
| Under ~1 s | Nothing. Keep the UI still, but show a pressed state immediately. |
| Over ~1 s | Show inline progress in the control that started it (button label "Saving…" then "Saved", same width). Delay any loader by 200 ms, and once shown keep it at least 400 ms. |
| Known layout (tables, panels) | Use a content-shaped skeleton with no shimmer or a slow one. Keep stale data visible and dimmed during a refetch when that's safe. |
| Over ~10 s (rate quotes, bulk import) | Show steps or an estimate, plus Cancel. |

- **Success:** a check in the button or a toast. Even a booked load gets only a toast.
- **Errors:** persistent text near the problem, with an icon and color. A 4 px horizontal shake of the field (250 ms) is optional as a secondary cue. Move focus to the first error. The message must not shift layout.
- **Live changes** (status updates or new bids while the dispatcher looks elsewhere): highlight the changed cell with a background that starts strong and fades over ~1 s. Fire one pulse per batch. Don't count numbers up.
- **Optimistic updates:** only for reversible actions (status tag, assignment), with a visible rollback and a message on failure. Never for booking confirmation, payment or deletion.

## Reduced motion

Honor `prefers-reduced-motion: reduce`. Remove movement (slides, scale, shake, rotation, height animation) and keep opacity, color and focus feedback. Don't write `* { transition: none }`, because it also kills focus rings and state changes.

```css
.side-panel { transition: transform var(--motion-slow) var(--ease-enter); }

@media (prefers-reduced-motion: reduce) {
  .side-panel {
    transform: none;
    transition: opacity var(--motion-fast) linear;
  }
}
```

Handle it per component, as in the table above. In JS, read `matchMedia('(prefers-reduced-motion: reduce)')` and branch before starting any movement.

## Don'ts

- No bounce, spring overshoot or elastic easing.
- No `ease-in-out` by default. Pick enter, exit or move by direction.
- No stagger on tables, menus or lists.
- No parallax, scroll-reveals or count-ups.
- No looping animation except calm spinners and skeletons.
- Nothing in the product runs longer than 300 ms, except progress indicators.
- Don't animate `width`, `height`, `top` or `left`, except the row expand above.
- Don't disable controls or ignore input during an animation.

## Adding a new pattern

1. What is its job: where did it go, what changed, or did it work? If none, don't animate it.
2. How often will users hit it? The more often, the shorter and smaller it should be.
3. Which existing token and easing fit? If none do, ask the design team before adding a token.
4. What happens when it's interrupted, and what happens under reduced motion?

Then add a row to the component table in the same format.

---

**Choices to check:**
- I set the numbers myself from standard UI timing ranges. They're a starting point to try in the app, not measured values.
- I assumed toasts sit bottom-right and side panels come from the right. Change those if your layout differs.
- I assumed 5 s toasts and a maximum of 3 visible.
- If you already have motion tokens in code, tell me their names and I'll switch the doc to use them.
