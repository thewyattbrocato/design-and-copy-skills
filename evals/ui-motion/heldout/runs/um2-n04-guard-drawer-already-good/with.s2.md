The most likely cause of the "off" feeling is that the drawer never visibly closes. `visibility: hidden` isn't transitioned, so it flips the moment `.open` is removed, and the 180 ms slide-out is cut off. The drawer vanishes while the scrim fades out slowly behind it. Opening works fine, so it feels lopsided. The reduced-motion fade-out has the same bug.

I found two smaller problems:
- **Scrim timing:** the scrim uses 200 ms linear in both directions, so it doesn't match the drawer's 240 ms open and 180 ms close.
- **Exit curve:** the exit curve ends at high speed (`0.9, 0.6`), which reads as a slam.

```css
.drawer {
  position: fixed; inset: 0 auto 0 0; width: 280px;
  transform: translateX(-100%);
  visibility: hidden;
  /* exit: accelerate away, then hide only after the slide finishes */
  transition:
    transform 180ms cubic-bezier(0.4, 0, 1, 1),
    visibility 0s linear 180ms;
}
.drawer.open {
  transform: translateX(0);
  visibility: visible;
  /* enter: decelerate in, become visible immediately */
  transition:
    transform 240ms cubic-bezier(0.3, 0.7, 0.2, 1),
    visibility 0s;
}

.scrim {
  position: fixed; inset: 0; background: rgb(0 0 0 / 0.4);
  opacity: 0; pointer-events: none;
  transition: opacity 180ms ease-in;
}
.scrim.open {
  opacity: 1; pointer-events: auto;
  transition: opacity 240ms ease-out;
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
  .scrim, .scrim.open { transition-duration: 120ms; }
}
```

**Spec**

| | Drawer | Scrim |
|---|---|---|
| Open | 240 ms, your original ease-out, visible at once | 240 ms ease-out |
| Close | 180 ms, ease-in (`0.4, 0, 1, 1`), hidden after 180 ms | 180 ms ease-in |
| Reduced motion | 120 ms opacity fade, no travel | 120 ms |

**What I kept**
- The 240 ms open and its ease-out curve, since the drawer decelerates into place.
- The shorter exit.
- The transform and opacity animation.
- The reduced-motion approach of removing travel but keeping a fade.

**Interruption:** reopening mid-close works. `visibility` becomes visible immediately and the transform reverses from wherever it is. Nothing is disabled during the motion.

I haven't run this in a browser. Please check close, and a quick open-then-close, on the real page.
