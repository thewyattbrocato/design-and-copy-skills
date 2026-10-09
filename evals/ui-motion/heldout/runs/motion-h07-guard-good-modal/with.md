This motion is already good, so I wouldn't retune it before you ship.

**What's working**
- **Timing:** The enter is 200ms and the exit is 120ms, so the exit is about 40% shorter. The overlay's 160ms fade sits in the right range for a modal.
- **Easing:** `cubic-bezier(.2, .8, .2, 1)` decelerates on the way in, and the exit is just a quick fade. That matches how each direction should feel.
- **Travel:** 8px and `scale(.98)` is small enough to feel calm and decisive, with no overshoot or bounce.
- **Performance:** Only `transform` and `opacity` animate, and nothing uses `transition: all`.
- **Interruption:** Because these are CSS transitions, toggling `.open` mid-animation reverses from the current state. Nothing is disabled while it plays.
- **Reduced motion:** You drop the movement and keep a linear opacity fade. The button still gets its background-color feedback. That's the right behavior, not "delete all transitions".

**Optional polish (none of these block shipping)**
1. **Keyboard focus can reach the closed modal.** `opacity: 0` and `pointer-events: none` don't take the contents out of the tab order or the accessibility tree. Add `visibility: hidden` to the closed overlay. Delay it on close so the fade still plays:
   ```css
   .modal-overlay { visibility: hidden; transition: opacity 160ms ease-out, visibility 0s linear 160ms; }
   .modal-overlay.open { visibility: visible; transition-delay: 0s; }
   ```
   Alternatively, set `inert` on the overlay while it's closed. You'll still need to move focus into the modal on open and restore it on close, if you haven't already.
2. **The button's press release snaps.** `.confirm-btn` only transitions `background-color`, so the `scale(.98)` applies and releases instantly. The instant press is fine. If you want a softer release, use `transition: background-color 120ms ease-out, transform 120ms ease-out`.

The values are fine if you ship as is. The `visibility` fix is the only one I'd call worth doing, and it's about accessibility rather than motion.
