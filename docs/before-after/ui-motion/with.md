Here's the full updated file. I couldn't see your script, so it works without changes. A `MutationObserver` watches the text and plays the animation whenever the script updates the number, room or next-up tickets.

[...]

**What changed**

[...]

- **Motion:** The only motion plays when a patient is called. The number and room slide up and fade in over 450 ms. A soft green glow fades out over 1.4 s, which is long enough to catch someone's eye in a waiting room. The next-up cards fade in with a 40 ms stagger. Nothing loops or pulses, so the screen stays calm the rest of the time.
- **Reduced motion:** Users with `prefers-reduced-motion` get fades and the glow, with no sliding.

**What to check**
- If your script rebuilds the `.now` or `.next` elements instead of changing their text, the observer will be lost. Tell me if it does that and I'll adjust it.

[...]
