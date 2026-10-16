I couldn't save this as a file because the Write tool is disabled in this session. The full section is below, so you can paste it into your docs.

---

# Motion

Motion in Tallowfield Freight shows **what changed and where it came from**. It is never decoration. Dispatchers use this tool all day, so every animation has to be fast enough that nobody waits on it.

**Rule of thumb:** if you can't say what the animation explains (where a menu came from, that a row opened, that a toast arrived), don't add it.

## How to use this page

1. Never write a raw `ms` value or `cubic-bezier()` in component code. Use the tokens below.
2. Find your component in [Recipes](#recipes) and copy the values.
3. If nothing fits, pick the closest recipe and ask the design team before inventing a new one.

---

## Tokens

### Durations

| Token | Value | Use for |
|---|---|---|
| `--motion-duration-instant` | 0ms | Reduced-motion fallback, bulk changes |
| `--motion-duration-fast` | 100ms | Hover, press, focus, menu exit, small state changes |
| `--motion-duration-base` | 160ms | Menu enter, chevrons, fades, most exits |
| `--motion-duration-moderate` | 240ms | Modal, side panel, toast enter, row expand |
| `--motion-duration-slow` | 360ms | Reserved. Needs design sign-off. |

Nothing in the product should run longer than `moderate` without sign-off.

### Easings

| Token | Value | Use for |
|---|---|---|
| `--motion-ease-enter` | `cubic-bezier(0.2, 0, 0, 1)` | Things appearing. Fast start, soft landing. |
| `--motion-ease-exit` | `cubic-bezier(0.4, 0, 1, 1)` | Things leaving. Gentle start, quick finish. |
| `--motion-ease-move` | `cubic-bezier(0.4, 0, 0.2, 1)` | Things already on screen that resize or move (row expand, toast stack reflow). |

Don't use `linear` (except for spinners) or the browser's default `ease`.

### CSS

```css
:root {
  --motion-duration-instant: 0ms;
  --motion-duration-fast: 100ms;
  --motion-duration-base: 160ms;
  --motion-duration-moderate: 240ms;
  --motion-duration-slow: 360ms;

  --motion-ease-enter: cubic-bezier(0.2, 0, 0, 1);
  --motion-ease-exit: cubic-bezier(0.4, 0, 1, 1);
  --motion-ease-move: cubic-bezier(0.4, 0, 0.2, 1);
}

@media (prefers-reduced-motion: reduce) {
  :root {
    --motion-duration-fast: 0ms;
    --motion-duration-base: 0ms;
    --motion-duration-moderate: 0ms;
    --motion-duration-slow: 0ms;
  }
}
```

The reduced-motion override zeroes every token, so components that use tokens get a baseline fallback automatically. See [Reduced motion](#reduced-motion) for the cases that need more.

If you need the values in JS (Framer Motion, Web Animations API), mirror them from one shared module. Don't retype them.

```ts
export const motion = {
  duration: { instant: 0, fast: 0.1, base: 0.16, moderate: 0.24, slow: 0.36 }, // seconds
  ease: {
    enter: [0.2, 0, 0, 1],
    exit: [0.4, 0, 1, 1],
    move: [0.4, 0, 0.2, 1],
  },
} as const;
```

---

## Principles

- **Exits are faster than entrances.** The user has already moved on. Exit durations are one step down from the enter (240 → 160, 160 → 100).
- **Enter with `enter`, leave with `exit`.** Easing follows direction, not component.
- **Animate `opacity` and `transform` only.** They stay smooth on a busy screen. The one exception is expandable rows (see below).
- **Start from where it came from.** Set `transform-origin` to the trigger, or slide from the edge the element lives on.
- **Small distances.** Offsets of 4–16px are enough. Full-width travel is only for side panels.
- **No stagger, no bounce, no overshoot.** Lists and tables appear all at once.
- **Don't block input.** Users can click, type, or press Esc while something is animating.
- **Never animate on data refresh.** Polling updates, new rows, and status changes don't fade or slide. If a change needs attention, use a highlight in the status color.

---

## Recipes

| Component | Enter | Exit |
|---|---|---|
| Menu / popover | `base`, `enter` | `fast`, `exit` |
| Modal | `moderate`, `enter` | `base`, `exit` |
| Toast | `moderate`, `enter` | `base`, `exit` |
| Side panel | `moderate`, `enter` | `base`, `exit` |
| Expandable row | `moderate`, `move` | `base`, `move` |
| Page navigation | `base`, `enter` | none |

### Menus and popovers

Dropdowns, action menus, select lists, and tooltips.

- **Enter:** opacity 0 → 1, `scale(0.98)` → `1`, and `translateY(-4px)` → `0` (flip the sign if it opens upward). `base`, `enter`.
- **Exit:** opacity only, 1 → 0. `fast`, `exit`.
- **Origin:** the edge nearest the trigger.
- Menu items and submenus don't animate individually.
- **Tooltips:** fade only, `fast`. Apply the open delay with a hover-intent timer, not an animation delay.

```css
.menu {
  transform-origin: var(--menu-origin, top left);
  transition:
    opacity var(--motion-duration-base) var(--motion-ease-enter),
    transform var(--motion-duration-base) var(--motion-ease-enter);
}
.menu[data-state="closed"] {
  opacity: 0;
  transform: scale(0.98) translateY(-4px);
  transition-duration: var(--motion-duration-fast);
  transition-timing-function: var(--motion-ease-exit);
}
```

### Modals

Dialogs that block the page: confirmations, create/edit forms.

- **Scrim:** opacity fade, same duration as the dialog.
- **Dialog enter:** opacity 0 → 1, `translateY(8px)` → `0`. `moderate`, `enter`. No scale.
- **Dialog exit:** opacity 1 → 0, no movement. `base`, `exit`.
- Focus moves into the dialog on open without waiting for the animation to finish.

### Toasts

- **Enter:** opacity 0 → 1, `translateY(16px)` → `0` from the bottom edge. `moderate`, `enter`.
- **Exit:** opacity 1 → 0, no movement. `base`, `exit`.
- **Stack reflow:** when a toast is dismissed, the others move into place with `moderate`, `move`.
- Auto-dismiss time is a content decision, not a motion token.
- Errors that need action must not auto-dismiss.

### Side panels

Detail drawers, filters, shipment and booking details.

- **Enter:** `translateX(100%)` → `0` from the edge the panel is anchored to. `moderate`, `enter`.
- **Exit:** reverse, `base`, `exit`.
- **Scrim** (if the panel is modal): fade, matching the panel.
- **Content behind the panel doesn't move or resize.** The panel overlays it. If the layout has to reflow to make room, switch it instantly.
- **Switching items while the panel is open** (e.g. clicking another shipment): swap the content in place with no animation. Don't close and reopen.

### Expandable table rows

This is the most-used motion in the product, so keep it light.

- **Row height:** 0 → auto, `moderate`, `move`. Collapse uses `base`, `move`.
- **Chevron:** rotate 90° with `base`, `move`.
- **Content:** fades in with `base`, `enter`, starting with the height change. On collapse, content hides immediately and the height closes.
- **"Expand all" / "Collapse all"** apply instantly (`instant`).
- **Don't animate `height` directly.** Use `grid-template-rows: 0fr → 1fr` so you don't have to measure content.
- **Virtualized tables:** if animation causes scroll jumps, fall back to instant.

```css
.row-detail {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows var(--motion-duration-base) var(--motion-ease-move);
}
.row-detail[data-open="true"] {
  grid-template-rows: 1fr;
  transition-duration: var(--motion-duration-moderate);
}
.row-detail > .inner { overflow: hidden; }
```

### Page navigation

- **Navigation chrome (top bar, sidebar) never animates.**
- **Page content:** a simple opacity fade-in, 0 → 1, `base`, `enter`. No exit animation. The old page is replaced immediately.
- **No slide, push, or shared-element transitions between routes.**
- **Loading:** show no spinner or skeleton for the first 300ms. If content arrives sooner, render it with no loading state. After 300ms, show a skeleton in place. Skeletons don't shimmer, and they fade out as content fades in (`base`).
- **Within-page changes** (tabs, filters, sort): swap content instantly.

### Small interactions

Buttons, inputs, checkboxes, toggles, row hover.

- `fast`, `enter` for color, background, border, and shadow changes.
- Press feedback: `scale(0.98)` on buttons only.
- Focus rings appear immediately (`instant`). Never delay them.

---

## Reduced motion

Respect `prefers-reduced-motion: reduce`. The token override zeroes durations, which is enough for most components. In addition:

- **Remove movement, keep meaning.** Menus, modals, toasts, and panels may still fade (a short `fast` opacity transition is fine), but without translate or scale.
- **Spinners** may keep rotating but must not be the only loading indicator. Pair them with text.
- **Expandable rows** open instantly, and the chevron flips instantly.
- **Nothing flashes** more than three times per second.

For JS-driven animation, check `window.matchMedia("(prefers-reduced-motion: reduce)")` and use the same fallbacks.

---

## Do and don't

| Do | Don't |
|---|---|
| `transition: opacity var(--motion-duration-base) var(--motion-ease-enter)` | `transition: all 0.3s ease` |
| Use `exit` easing on closing elements | Use the same easing for open and close |
| Fade a new page in once | Slide pages left and right |
| Highlight a changed table cell with color | Animate rows moving as data refreshes |
| Let users keep working during an animation | Disable the UI until an animation finishes |
| Ask for a new token if you need one | Hard-code `350ms` "just this once" |

---

## Review checklist

Before you open a PR that adds or changes motion:

- [ ] Only motion tokens are used. No raw durations or curves.
- [ ] Exit is shorter than enter.
- [ ] Only `opacity` and `transform` are animated (rows excepted).
- [ ] Works with `prefers-reduced-motion: reduce`.
- [ ] Doesn't block clicks, typing, or Esc.
- [ ] Nothing animates on background data refresh.
- [ ] You can state what the animation communicates.

---

**Notes for your team**

- The numbers are my starting proposal, not measured against your product. I picked them for a dense, repeat-use tool, so they're on the fast side. Try them in the real app for a day and adjust the five duration tokens. The recipes will follow.
- I assumed plain CSS custom properties and didn't know your stack. If you use Tailwind or a tokens pipeline (Style Dictionary, etc.), the token tables map over directly.
- If you'd like me to save this to a file in your repo, enable Write or tell me the path.
