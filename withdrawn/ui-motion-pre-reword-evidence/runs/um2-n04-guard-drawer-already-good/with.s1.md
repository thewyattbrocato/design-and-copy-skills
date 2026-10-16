The most likely cause of the "off" feeling is that the close animation never shows. On close, `.drawer` loses `.open`, so `visibility: hidden` applies immediately and the drawer disappears. The 180ms slide-out is never seen, while the scrim fades for another 200ms. The drawer pops out and the dimming lingers behind it.

Two smaller mismatches add to it. The scrim's 200ms doesn't match either drawer duration (240ms in, 180ms out), so the two parts never settle together. The reduced-motion branch has the same bug: its 120ms fade-out is cut off by the instant `visibility` change.

```css
.drawer {
  position: fixed; inset: 0 auto 0 0; width: 280px;
  transform: translateX(-100%);
  visibility: hidden;
  /* exit: accelerate away, then hide once the slide has finished */
  transition: transform 180ms cubic-bezier(0.5, 0, 0.9, 0.6),
              visibility 0s linear 180ms;
}
.drawer.open {
  transform: translateX(0);
  visibility: visible;
  /* enter: decelerate in, visible from the first frame */
  transition: transform 240ms cubic-bezier(0.3, 0.7, 0.2, 1),
              visibility 0s;
}

.scrim {
  position: fixed; inset: 0; background: rgb(0 0 0 / 0.4);
  opacity: 0; pointer-events: none;
  transition: opacity 180ms ease-out;   /* matches drawer exit */
}
.scrim.open {
  opacity: 1; pointer-events: auto;
  transition: opacity 240ms ease-out;   /* matches drawer enter */
}

@media (prefers-reduced-motion: reduce) {
  .drawer { transform: none; opacity: 0;
            transition: opacity 120ms linear, visibility 0s linear 120ms; }
  .drawer.open { opacity: 1; transition: opacity 120ms linear, visibility 0s; }
  .scrim, .scrim.open { transition-duration: 120ms; }
}
```

**What changed**
- **Visible exit:** `visibility` now flips after the slide finishes (0s duration, delayed by the exit time). On open it flips at once. Hidden drawers still leave the tab order.
- **Synced scrim:** it uses 240ms in and 180ms out, the same as the drawer. The `ease-out` replaces `linear`, which tends to look mechanical on a large overlay.
- **Reduced motion:** it keeps the opacity fade, and the fade-out now plays before the drawer hides. Nothing slides.

**What I left alone**
- The curves and durations were already sound. The enter eases out at 240ms, the exit accelerates and is about a quarter shorter, and only `transform` and `opacity` animate.
- Clicking the scrim during the open animation reverses from the current position, because the transitions retarget. Nothing is disabled while it plays.

I haven't run this in a browser. If it still feels off, check whether your JS toggles `.open` on the drawer and scrim in the same frame. Also check whether it removes `aria-hidden` before or after the class change.
