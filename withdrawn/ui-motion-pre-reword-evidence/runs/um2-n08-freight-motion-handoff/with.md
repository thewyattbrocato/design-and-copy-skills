I couldn't save this to a file because the Write tool is disabled in this session. The full section is below, ready to paste into your docs.

I assumed a CSS-based web app and used "calm and decisive" as the feel. Your dispatchers use the tool all day, so frequent actions are fast and simple. If you already have tokens or a different stack, say so and I'll adjust.

---

# Motion

**Feel: calm and decisive.** Motion is short, arrives and stops, and never makes anyone wait. Things appear from where they live, leave quickly, and respond to new input at once.

Use the tokens below. Don't write your own durations or easings. If a case isn't covered, pick the closest pattern and raise it in #design.

## Rules

1. **Motion has a job.** It shows where something came from, what changed, or that an action worked. If it does none of these, don't animate it.
2. **Animate `transform` and `opacity` only.** The one exception is expandable rows. Never use `transition: all`; always list the properties.
3. **Everything is interruptible.** Use CSS transitions, not keyframes, for anything that toggles. Never disable a control or set `pointer-events: none` while something animates.
4. **Exits are faster than entrances.** Enter with ease-out and leave with ease-in.
5. **Content already on screen doesn't animate on page load.** No scroll reveals, no count-ups, no entrance animations on every navigation.
6. **Reduced motion removes movement, not feedback.** See Reduced motion.

## Tokens

```css
:root {
  /* Durations: four values, no others */
  --duration-press:  120ms; /* hover, press, menu exit */
  --duration-short:  180ms; /* menu enter, page crossfade, row collapse, toast and modal exit */
  --duration-medium: 240ms; /* modal and toast enter, row expand, side panel exit */
  --duration-long:   300ms; /* side panel enter */

  /* Easings: three curves, plus linear for progress */
  --ease-enter: cubic-bezier(0.2, 0, 0, 1);   /* things arriving */
  --ease-exit:  cubic-bezier(0.4, 0, 1, 1);   /* things leaving */
  --ease-move:  cubic-bezier(0.4, 0, 0.2, 1); /* moving between two on-screen places */

  --travel-small: 4px;  /* menus */
  --travel-large: 8px;  /* modals, toasts */
  --stagger: 30ms;      /* see below */
}
```

**Choosing a duration:** hover and press use `press`. Small local changes use `short`. Overlays and panels use `medium` or `long`. Nothing on a frequent path goes above `medium`.

**Stagger:** none of the patterns below use it. Don't stagger table rows, menu items, or anything people act on at once. For a rare moment like a first-run empty state, apply `--stagger` to at most the first 8 items.

## Patterns

| Pattern | Enter | Exit | Comes from |
|---|---|---|---|
| Menu | 180 ms, ease-enter | 120 ms, ease-exit | Its trigger |
| Modal | 240 ms, ease-enter | 180 ms, ease-exit | Slightly below its final position, with a scrim fade |
| Toast | 240 ms, ease-enter | 180 ms, ease-exit | Its screen edge |
| Side panel | 300 ms, ease-enter | 240 ms, ease-exit | Its own screen edge |
| Expandable row | 240 ms, ease-enter | 180 ms, ease-exit | In place |
| Page navigation | 180 ms crossfade | No separate exit | In place |

### Menus
*Job: show which control opened the menu.*

- **Enter:** opacity 0 to 1 and `translateY(-4px)` to 0. Set `transform-origin` to the trigger edge.
- **Exit:** opacity only.
- **Items:** no stagger. The hover highlight is a background-color change at `--duration-press`.
- **Interrupt:** closing mid-enter reverses from the current state.

```css
.menu {
  opacity: 0;
  transform: translateY(calc(var(--travel-small) * -1));
  transition: opacity var(--duration-press) var(--ease-exit),
              transform var(--duration-press) var(--ease-exit),
              display var(--duration-press) allow-discrete;
}
.menu[data-open] {
  opacity: 1;
  transform: none;
  transition: opacity var(--duration-short) var(--ease-enter),
              transform var(--duration-short) var(--ease-enter),
              display var(--duration-short) allow-discrete;
}
@starting-style {
  .menu[data-open] { opacity: 0; transform: translateY(calc(var(--travel-small) * -1)); }
}
```

All overlays use this structure. The base state is closed with the exit timing, `[data-open]` is open with the enter timing, and `@starting-style` gives the entry start. Exiting elements stay in the DOM until the exit finishes. If you use a component library with presence handling (Radix and similar), use it with these tokens.

### Modals
*Job: focus attention on the new layer.*

- **Dialog enter:** opacity 0 to 1 and `translateY(8px)` to 0, 240 ms, `--ease-enter`.
- **Scrim:** fades on the same clock and easing as the dialog.
- **Exit:** opacity only, 180 ms, `--ease-exit`.
- **No scale and no bounce.**
- **Interrupt:** Esc or the close button works immediately, even mid-enter.
- **Commits:** for actions like book, tender or cancel load, the motion finishes but the button shows its pending state and blocks double submit.

### Toasts
*Job: say something happened without taking focus.*

- **Enter:** opacity 0 to 1 and `translateY(8px)` to 0 from the stack edge, 240 ms, `--ease-enter`.
- **Exit:** opacity to 0, 180 ms, `--ease-exit`. The remaining toasts close the gap with `transform`, 180 ms, `--ease-move`; they don't snap.
- **Time on screen:**
  - Confirmations: 5 s.
  - Longer text: 8 s.
  - Toasts with an action (Undo) or an error: stay until dismissed.
- **Timer:** pauses on hover and focus.
- **Announce:** `role="status"`, or `role="alert"` for errors. Motion is never the only signal.
- **Stack:** max 3 visible. Newer toasts push older ones up; they don't replace them.

### Side panels
*Job: show the panel belongs to the edge it came from.*

- **Enter:** `translateX(100%)` to 0 for a right-side panel (mirror for left), 300 ms, `--ease-enter`.
- **Exit:** back the way it came, 240 ms, `--ease-exit`.
- **Scrim:** a modal panel's scrim fades on the same clock. A non-modal panel has no scrim.
- **Layout:** panels overlay the page. Don't animate the page's width to make room, because that reflows the whole table.
- **Interrupt:** closing mid-open reverses from the current position.

### Expandable table rows
*Job: show the detail belongs to the row above it.*

- **Structure:** the detail is a full-width row (`<td colspan>`) containing a wrapper.
- **Technique:** animate the wrapper with `grid-template-rows: 0fr` to `1fr` plus opacity. This is the one place we animate size. Keep it to one row's detail, never a large container.
- **Timing:** expand 240 ms with `--ease-enter`; collapse 180 ms with `--ease-exit`.
- **Chevron:** rotates 90° over `--duration-short` with `--ease-move`.
- **Neighbors:** rows below move with the grid animation; they don't snap.
- **Expand all:** no stagger.
- **Interrupt:** toggling mid-animation reverses from the current height.

```css
.row-detail { display: grid; grid-template-rows: 0fr; opacity: 0;
  transition: grid-template-rows var(--duration-short) var(--ease-exit),
              opacity var(--duration-short) var(--ease-exit); }
.row-detail[data-open] { grid-template-rows: 1fr; opacity: 1;
  transition: grid-template-rows var(--duration-medium) var(--ease-enter),
              opacity var(--duration-medium) var(--ease-enter); }
.row-detail > .inner { overflow: hidden; min-height: 0; }
```

### Page navigation
*Job: show the content changed, without making anyone wait.*

- **Crossfade:** only the content region crossfades, 180 ms. Header, nav and other persistent chrome stay still.
- **Direction:** no slide, so back and forward use the same crossfade.
- **Never wait:** the new page is readable immediately. Don't hold rendering or data for the transition.
- **Support:** use the View Transitions API where available and fall back to an instant swap.
- **Persistent objects:** where the same object persists (a list row that becomes the detail header), carry it with a shared `view-transition-name`. Don't fade out and fade in a lookalike.
- **Loading:** first paint is the skeleton, never an empty frame.

```css
::view-transition-old(root),
::view-transition-new(root) {
  animation-duration: var(--duration-short);
  animation-timing-function: var(--ease-enter);
}
```

## Feedback

| Moment | Spec |
|---|---|
| Hover and press | Color, shadow or a 2 to 4% scale change over 120 ms. Every clickable control has a pressed state. Never move the target out from under the pointer. |
| Focus | The focus ring is never animated away. |
| Wait under about 1 s | Show only the pressed state. No loader. |
| Button with async action | After 300 ms, swap the label for an inline spinner in the same footprint, with the width fixed. Once shown, keep it at least 400 ms. End with a check or the new label. |
| Table or page loading | Skeleton on first paint. Show it only if the wait passes 200 ms, and hold it at least 400 ms. No shimmer, or a very slow one. On refresh, keep stale data visible and dim it slightly. One wait gets one indicator. |
| Progress | Linear easing. Determinate only if it reflects real completion. |
| Commits (book, tender, cancel, delete) | Pending state on the button and no double submit. Other controls stay live. |
| Optimistic updates | Only for reversible actions, such as starring a lane. On failure, show a short reversal and a message saying what happened. Never for bookings or anything that can't be undone. |
| Live value changed outside focus | Example: a load status changes while the dispatcher looks elsewhere. The cell goes to the highlight color at once and fades out over 1 s with `--ease-enter`. Rate-limit to one highlight per batch of updates, and only for changes that matter. The value stays readable. |
| Errors | Persistent text next to the field, plus color and an icon. Focus moves to the first problem. Reserve space for the message so nothing jumps, and don't force scroll. No shake by default. |

## Reduced motion

Honor `prefers-reduced-motion: reduce`. Remove movement; keep opacity, color and focus.

| Pattern | Reduced-motion behavior |
|---|---|
| Menu | Opacity only, 120 ms |
| Modal | Opacity only, 120 ms |
| Toast | Opacity only, 120 ms; stack reflow is instant |
| Side panel | Opacity only, 150 ms, no slide |
| Expandable row | Instant open and close, including the chevron |
| Page navigation | Instant swap |
| Live-value highlight | Unchanged (it's a color change) |
| Spinners | Keep, slowed to one rotation per 2 s. They report real status. |

```css
@media (prefers-reduced-motion: reduce) {
  .menu, .modal, .toast { transform: none; transition-duration: var(--duration-press); }
  .side-panel { transform: none; transition: opacity 150ms linear; }
  .row-detail { transition: none; }
  ::view-transition-group(*), ::view-transition-old(*), ::view-transition-new(*) { animation: none; }
}
```

**Don't** use a blanket `* { transition: none !important }`. It also removes focus and state feedback. In JavaScript, read `matchMedia('(prefers-reduced-motion: reduce)')` before starting any movement and listen for changes.

## PR checklist for motion changes

- [ ] Every duration and easing is a token from this page.
- [ ] Only `transform` and `opacity` animate (or the row-expand exception). No `transition: all`.
- [ ] The exit is shorter than the enter and uses `--ease-exit`.
- [ ] Clicking or pressing Esc mid-animation works and reverses smoothly. No control is disabled while animating.
- [ ] The reduced-motion variant is implemented and checked, and focus rings still show.
- [ ] First paint is content or a skeleton, never an empty frame. Checked with network and CPU throttled.
- [ ] Nothing flashes more than 3 times per second.

## Need something new?

Don't add custom values. Post in #design with the pattern, how often people trigger it, and what question it answers for the user (where did it go, what changed, did it work). We'll map it to an existing pattern or add a row here.

---

Three decisions to confirm:
- **Four durations:** I kept them to 120, 180, 240 and 300 ms, so every pattern is one of four numbers.
- **No shake on errors:** the doc uses text, color and an icon instead. Tell me if you want a small shake added.
- **Row expand:** I made it the one exception to "transform and opacity only," because height is the point of that interaction.

If you give me the file location and enable file writes, I'll save it there.
