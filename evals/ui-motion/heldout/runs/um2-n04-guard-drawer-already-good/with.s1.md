The main problem is that the drawer never visibly slides out. The curves have smaller issues too.

**What's off**
1. **The close animation is cut off.** `visibility` flips to `hidden` the moment `.open` is removed, so the drawer vanishes instantly while the 180 ms slide-out plays on an invisible element. The scrim fades but the panel pops, which is probably the "a bit off" feeling.
2. **The exit curve ends with a jolt.** `cubic-bezier(0.5, 0, 0.9, 0.6)` has a steep final segment, so the panel accelerates and then stops abruptly.
3. **The enter curve is unusual.** `(0.3, 0.7, 0.2, 1)` is valid, but the control points are oddly placed. A standard ease-out gives a cleaner deceleration.
4. **The scrim isn't synced with the drawer.** It uses 200 ms linear in both directions, while the drawer runs 240 ms in and 180 ms out.
5. **Reduced motion has a specificity gap.** `.drawer.open` outranks the media-query `.drawer` rule, so the open state keeps its transform transition and the opacity fade never applies. The drawer snaps open. The close would also still pop, because of the visibility problem above.

**Polished version**

```css
/* Quiet and crisp: enter ease-out, exit ease-in and shorter. Transform/opacity only. */
.drawer {
  position: fixed; inset: 0 auto 0 0; width: 280px;
  transform: translateX(-100%);
  visibility: hidden;
  /* exit: 200ms ease-in; visibility flips only after the slide finishes */
  transition:
    transform 200ms cubic-bezier(0.4, 0, 1, 1),
    visibility 0s linear 200ms;
}
.drawer.open {
  transform: translateX(0);
  visibility: visible;
  /* enter: 260ms ease-out; visible immediately */
  transition:
    transform 260ms cubic-bezier(0.2, 0, 0, 1),
    visibility 0s;
}

.scrim {
  position: fixed; inset: 0; background: rgb(0 0 0 / 0.4);
  opacity: 0; pointer-events: none;
  transition: opacity 200ms cubic-bezier(0.4, 0, 1, 1);
}
.scrim.open {
  opacity: 1; pointer-events: auto;
  transition: opacity 260ms cubic-bezier(0.2, 0, 0, 1);
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
  .scrim.open { transition-duration: 120ms; }
}
```

**Spec**

| Part | Trigger | Duration | Easing | Notes |
|---|---|---|---|---|
| Drawer in | add `.open` | 260 ms | `(0.2, 0, 0, 1)` | visible immediately |
| Drawer out | remove `.open` | 200 ms | `(0.4, 0, 1, 1)` | hidden after the slide ends |
| Scrim | same triggers | 260 ms in, 200 ms out | matches the drawer | no delay |
| Reduced motion | same triggers | 120 ms | linear | opacity only, no travel |

- **Interruption:** the transitions retarget from the current position, so toggling mid-motion reverses smoothly. Nothing is disabled while it runs.
- **Delayed visibility:** if the drawer is reopened mid-close, the `.open` rule's `visibility 0s` cancels the pending hide.
- **Not changed:** the 280 px width, the transform-only movement, and the reduced-motion approach (no travel, fade kept). Those were already sound.

I haven't run this in a browser. Please check the close on a real device. If your JS focuses a link on open or moves focus on close, check that it doesn't depend on the old instant `visibility` change.
