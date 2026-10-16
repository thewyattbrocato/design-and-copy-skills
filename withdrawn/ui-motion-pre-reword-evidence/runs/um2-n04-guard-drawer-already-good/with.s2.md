I changed the stylesheet in two places. The first is the likely cause of the "feels off".

**What's wrong**

1. **The close animation never plays.** `visibility: hidden` applies the moment `.open` is removed. The drawer vanishes instantly while the scrim fades out over 200 ms, so the panel seems to blink out under a lingering dim layer. That mismatch is the "off" feeling.
2. **Reduced motion is broken on open.** `.drawer.open` (outside the media query) has higher specificity than the `.drawer` override inside it. Its `transform 240ms` transition wins, so the opacity fade never runs and the drawer pops in.
3. **The scrim timing doesn't match the drawer.** The scrim takes 200 ms both ways, but the drawer's exit is 180 ms.

I left the curves and durations alone. Enter is 240 ms with an ease-out, and exit is 180 ms with an ease-in. That's already the right direction and about the right length. The drawer is a frequent action, so I kept it short and didn't add anything.

**Fixed CSS**

```css
.drawer {
  position: fixed; inset: 0 auto 0 0; width: 280px;
  transform: translateX(-100%);
  visibility: hidden;
  /* exit: accelerate away; hide only after the slide finishes */
  transition: transform 180ms cubic-bezier(0.5, 0, 0.9, 0.6),
              visibility 0s linear 180ms;
}
.drawer.open {
  transform: translateX(0);
  visibility: visible;
  /* enter: decelerate in; visible immediately */
  transition: transform 240ms cubic-bezier(0.3, 0.7, 0.2, 1),
              visibility 0s;
}

.scrim {
  position: fixed; inset: 0; background: rgb(0 0 0 / 0.4);
  opacity: 0; pointer-events: none;
  transition: opacity 180ms linear;          /* matches drawer exit */
}
.scrim.open {
  opacity: 1; pointer-events: auto;
  transition: opacity 240ms linear;          /* matches drawer enter */
}

@media (prefers-reduced-motion: reduce) {
  .drawer,
  .drawer.open { transform: none; }          /* no movement */
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

**Spec**

| | Drawer | Scrim |
|---|---|---|
| Open | 240 ms, `cubic-bezier(0.3, 0.7, 0.2, 1)`, translateX | 240 ms linear opacity |
| Close | 180 ms, `cubic-bezier(0.5, 0, 0.9, 0.6)`, then `visibility: hidden` | 180 ms linear opacity |
| Reduced motion | 120 ms opacity fade, no movement | 120 ms opacity fade |

Toggling `.open` mid-transition reverses from the current position, and nothing is disabled while it runs.

I haven't run this in a browser, so check it with a real open and close, including a quick double-toggle. Also make sure your JS moves focus into the drawer on open and back to the menu button on close. That's outside the motion work, but it matters for the same flow.
