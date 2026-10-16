I couldn't save this as a file because the Write tool is disabled in this session. The full section is below, so you can paste it into your docs.

---

# Motion

Motion in Tallowfield Freight explains what just happened (a panel came from the right, a row opened in place) and softens abrupt state changes. It is never decoration. Dispatchers repeat the same actions hundreds of times a day, so our motion is **quick, quiet, and predictable**.

**The rule:** use the tokens below. Don't write your own durations or easings.

## 1. Principles

1. **Fast by default.** Nothing animates longer than 300ms. If you're unsure, go shorter.
2. **Enter slower, exit faster.** Arriving UI gets a little more time to be understood. Leaving UI gets out of the way.
3. **Move from where it came from.** Menus grow from their trigger, panels slide from their edge, toasts rise from their corner.
4. **Never block work.** Content is interactive immediately, and users can click, type, or close mid-animation.
5. **Data is not animated.** Live updates to tables, statuses, ETAs, and prices change instantly. Motion is for UI chrome only.

## 2. Tokens

| Duration token | Value | Use for |
|---|---|---|
| `--motion-duration-instant` | 100ms | Hover, focus, pressed states, color changes, menu exit |
| `--motion-duration-fast` | 150ms | Menu enter, tooltips, chevron rotation, most exits, page fade-out |
| `--motion-duration-moderate` | 200ms | Modal, toast enter, row expand/collapse, page fade-in |
| `--motion-duration-slow` | 300ms | Side panel enter. This is the ceiling. |

| Easing token | Value | Use for |
|---|---|---|
| `--motion-ease-enter` | `cubic-bezier(0, 0, 0.2, 1)` | Things appearing |
| `--motion-ease-exit` | `cubic-bezier(0.4, 0, 1, 1)` | Things leaving |
| `--motion-ease-move` | `cubic-bezier(0.4, 0, 0.2, 1)` | On-screen things that resize or reposition |

Don't use bounce, spring, or elastic easings. Use `linear` only for spinners and progress bars.

```css
:root {
  --motion-duration-instant: 100ms;
  --motion-duration-fast: 150ms;
  --motion-duration-moderate: 200ms;
  --motion-duration-slow: 300ms;

  --motion-ease-enter: cubic-bezier(0, 0, 0.2, 1);
  --motion-ease-exit: cubic-bezier(0.4, 0, 1, 1);
  --motion-ease-move: cubic-bezier(0.4, 0, 0.2, 1);

  --motion-distance-small: 8px;   /* menus, modals */
  --motion-distance-medium: 16px; /* toasts */
}
```

## 3. Component recipes

Animate only `opacity` and `transform`, except where a recipe says otherwise.

| Component | Enter | Exit |
|---|---|---|
| Menu / dropdown | 150ms, enter. Fade and scale 0.98→1. | 100ms, exit. Fade only. |
| Modal | 200ms, enter. Dialog fades and moves up 8px. Scrim fades. | 150ms, exit. Fade only. |
| Toast | 200ms, enter. Fade and move up 16px. | 150ms, exit. Fade only. |
| Side panel | 300ms, enter. Slide in from right. Scrim fades. | 200ms, exit. Slide out. |
| Expandable row | 200ms, move. Height 0→auto. | 200ms, move. Height auto→0. |
| Page navigation | 200ms, enter. Content fades in. | 150ms, exit. Content fades out. |

**Menus**
- Set `transform-origin` to the trigger edge.
- Scale from 0.98 only. Anything bigger reads as a pop.
- Never wait for one menu to finish closing before opening another.

```css
.menu { transform-origin: var(--menu-origin, top left); }
.menu[data-state="open"]   { animation: menu-in var(--motion-duration-fast) var(--motion-ease-enter); }
.menu[data-state="closed"] { animation: fade-out var(--motion-duration-instant) var(--motion-ease-exit); }
@keyframes menu-in { from { opacity: 0; transform: scale(0.98); } }
@keyframes fade-out { to { opacity: 0; } }
```

**Modals**
- The scrim only fades. The dialog moves 8px and fades, with no scaling.
- Exit is fade-only and shorter, so dismissing never makes the user wait.
- Move focus into the modal on open. Don't wait for the animation.

```css
.modal[data-state="open"]   { animation: modal-in var(--motion-duration-moderate) var(--motion-ease-enter); }
.modal[data-state="closed"] { animation: fade-out var(--motion-duration-fast) var(--motion-ease-exit); }
@keyframes modal-in { from { opacity: 0; transform: translateY(var(--motion-distance-small)); } }
```

**Toasts**
- Toasts enter from the corner they're anchored to.
- When a toast leaves, the remaining toasts slide into the gap over 200ms using `--motion-ease-move`.
- All toasts use the same motion, whatever their severity.

**Side panels**
- This is the only component that uses `slow`, because it covers the most area.
- The page behind doesn't shift or scale.
- Panel content is present from the first frame. Don't stagger or animate its children.

**Expandable table rows**
- Animate height with the grid trick, so you don't have to measure content:

```css
.row-detail {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows var(--motion-duration-moderate) var(--motion-ease-move);
}
.row-detail[data-open="true"] { grid-template-rows: 1fr; }
.row-detail > .inner { overflow: hidden; }
```

- Rotate the chevron 90° over `fast` with `move`.
- Don't fade or slide the detail content. Only the height animates.
- "Expand all" and "Collapse all" skip animation. Hundreds of simultaneous height transitions are janky.
- Rows added or removed by live data don't animate.

**Page navigation**
- Only the content area changes. Header, sidebar, and other persistent chrome never animate.
- Use a fade only, with no slides or zooms.
- Don't hold the transition for data. Show the new page shell right away.
- Show skeletons only if loading exceeds about 300ms, to avoid a flash.
- Tabs within a page use no transition.

## 4. Reduced motion (required)

Honor `prefers-reduced-motion: reduce`. Remove all movement, scaling, and height animation. Keep opacity fades, shortened to 100ms. Put this in the global stylesheet once. It overrides the tokens, so components don't each need handling.

```css
@media (prefers-reduced-motion: reduce) {
  :root {
    --motion-duration-fast: 100ms;
    --motion-duration-moderate: 100ms;
    --motion-duration-slow: 100ms;
    --motion-distance-small: 0px;
    --motion-distance-medium: 0px;
  }
  .menu, .modal, .toast, .side-panel { transform: none; }
  .row-detail { transition: none; }
}
```

JS animation libraries should check `matchMedia('(prefers-reduced-motion: reduce)')` and fall back to opacity only.

## 5. Do and don't

**Do**
- Use token values for every `transition` and `animation`.
- Make animations interruptible. Closing a panel mid-open should reverse smoothly.
- Animate `transform` and `opacity`.
- Test on a low-end laptop with a large table on screen.

**Don't**
- Hard-code `ms` values or `cubic-bezier()` in components.
- Animate `width`, `height`, `top`, or `left`. The expandable row is the one exception.
- Use `ease`, `ease-in-out`, or the browser default easing.
- Add load-in animations such as staggered lists or counting-up numbers.
- Stack several animations on one interaction.
- Use motion as the only signal for something important. Errors and status changes also need text or color.

## 6. Adding or changing motion

1. Check whether an existing recipe covers it. A popover is a menu, and a drawer is a side panel.
2. If none does, use the closest tokens and propose the new recipe in design review.
3. To change a token, change it once in the tokens file so every component updates together.

---

The specific numbers are a starting point based on common practice for dense productivity tools, not values tested against your app. If something feels slow or abrupt once your engineers use it, tune the token rather than the component.

If you re-enable Write, I can save this as `motion.md` or in whatever format your docs site uses (MDX, Storybook, etc.).
