The most likely cause is that the close animation never plays. `visibility` isn't in either `transition` list, so removing `.open` sets `visibility: hidden` on the first frame and the drawer vanishes before it can slide out. Only the open animation is visible, so closing feels abrupt.

Your curves and durations are fine: ease-out in at 240 ms, ease-in out at 180 ms. I kept them.

```css
.drawer {
  position: fixed; inset: 0 auto 0 0; width: 280px;
  transform: translateX(-100%);
  visibility: hidden;
  /* exit: accelerate away; keep visible until the slide finishes */
  transition:
    transform 180ms cubic-bezier(0.5, 0, 0.9, 0.6),
    visibility 0s linear 180ms;
}
.drawer.open {
  transform: translateX(0);
  visibility: visible;
  /* enter: decelerate in; visible immediately */
  transition:
    transform 240ms cubic-bezier(0.3, 0.7, 0.2, 1),
    visibility 0s;
}

.scrim {
  position: fixed; inset: 0; background: rgb(0 0 0 / 0.4);
  opacity: 0; pointer-events: none;
  transition: opacity 180ms cubic-bezier(0.5, 0, 0.9, 0.6);
}
.scrim.open {
  opacity: 1; pointer-events: auto;
  transition: opacity 240ms cubic-bezier(0.3, 0.7, 0.2, 1);
}

@media (prefers-reduced-motion: reduce) {
  .drawer {
    transform: none; opacity: 0;
    transition: opacity 120ms linear, visibility 0s linear 120ms;
  }
  .drawer.open {
    opacity: 1;
    transition: opacity 120ms linear, visibility 0s;
  }
  .scrim,
  .scrim.open { transition-duration: 120ms; transition-timing-function: linear; }
}
```

**What changed**
- **Visibility timing:** `visibility` now flips after the slide ends on close (180 ms delay) and immediately on open. This is the main fix. Hidden drawers still leave the tab order and accessibility tree.
- **Scrim matches the drawer:** it was 200 ms linear in both directions, so it drifted out of sync with the 240/180 ms slide. It now uses the same durations and curves.
- **Reduced motion:** the old override replaced the whole `transition` list, so the fade-out had the same instant-hide bug. It now has the same delayed-visibility fix. It still drops the movement and keeps a 120 ms fade.

**Spec**

| | Duration | Easing | Visibility |
|---|---|---|---|
| Open | 240 ms | `cubic-bezier(0.3, 0.7, 0.2, 1)` | immediate |
| Close | 180 ms | `cubic-bezier(0.5, 0, 0.9, 0.6)` | after 180 ms |
| Reduced motion | 120 ms | linear fade | same timing as above |

Toggling mid-animation reverses from the current position, because only transitions are used and nothing is disabled.

I haven't run this in a browser. Check that the close slide now shows. Two things your snippet doesn't show: the JS should toggle `aria-hidden` along with `.open`, and focus should move into the drawer on open and back to the menu button on close.
