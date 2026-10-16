The most likely cause of the "off" feeling is that the drawer never animates out. `visibility` isn't in either `transition` list, so when `.open` is removed, `visibility: hidden` applies on the first frame. The panel vanishes while the scrim fades behind it. Opening works, closing is a pop. The reduced-motion fade has the same problem, because the 120ms opacity fade is cut off on close.

I haven't run this in a browser. The diagnosis comes from reading the CSS.

Other smaller mismatches:
- **Durations:** the drawer opens in 240ms and closes in 180ms, while the scrim uses 200ms both ways, so the two never finish together.
- **Scrim easing:** `linear` fades look mechanical next to the eased drawer.
- **Exit curve:** `cubic-bezier(0.5, 0, 0.9, 0.6)` starts slowly, which feels laggy right after a tap, and it ends mid-flight.

Here's a revised version:

```css
.drawer {
  position: fixed; inset: 0 auto 0 0; width: 280px;
  transform: translateX(-100%);
  visibility: hidden;
  /* exit: quick, accelerates away; hide only after the slide finishes */
  transition:
    transform 200ms cubic-bezier(0.4, 0, 1, 1),
    visibility 0s linear 200ms;
}
.drawer.open {
  transform: translateX(0);
  visibility: visible;
  /* enter: decelerates into place; become visible immediately */
  transition:
    transform 240ms cubic-bezier(0.2, 0.8, 0.2, 1),
    visibility 0s;
}

.scrim {
  position: fixed; inset: 0; background: rgb(0 0 0 / 0.4);
  opacity: 0; pointer-events: none;
  transition: opacity 200ms cubic-bezier(0.4, 0, 1, 1);
}
.scrim.open {
  opacity: 1; pointer-events: auto;
  transition: opacity 240ms cubic-bezier(0.2, 0.8, 0.2, 1);
}

@media (prefers-reduced-motion: reduce) {
  .drawer,
  .drawer.open { transform: none; }
  .drawer {
    opacity: 0;
    transition: opacity 120ms linear, visibility 0s linear 120ms;
  }
  .drawer.open {
    opacity: 1;
    transition: opacity 120ms linear, visibility 0s;
  }
  .scrim,
  .scrim.open { transition-duration: 120ms; }
}
```

What changed:
1. **Exit is visible:** `visibility` flips after the slide ends (delayed on close, immediate on open), so the drawer slides out.
2. **Scrim matches the drawer:** it now has the same duration and easing in each direction, so they start and land together.
3. **Easing:** enter is a clean ease-out, and exit is a shorter ease-in so it leaves briskly.
4. **Reduced motion:** the fade now works on close too. I also made `.drawer.open` set `transform: none` explicitly, because the normal `.open` rule would otherwise win on specificity and bring the slide back.

If you want more depth, a `box-shadow` on `.drawer` that fades in with `.open` would help the panel separate from the scrim. I left it out since it's a visual change beyond the motion.
