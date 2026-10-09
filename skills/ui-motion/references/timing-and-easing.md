# Timing and easing

Load this when choosing numbers. These are starting points to test, not laws; the governing idea is as fast as it can be while still legible, and a feel test beats a table.

## Duration by size of change

| Change | Starting range |
|---|---|
| Hover and press feedback | 100 to 150 ms |
| Small local change (toggle, checkbox, small reveal, tooltip) | 150 to 250 ms |
| Medium (menu, toast, expanding panel, tab content) | 200 to 300 ms |
| Large travel or full-screen transition | 300 to 500 ms |
| Loader or deliberate demonstration | Can exceed 500 ms |

- Keep the total on any frequent path well under about 400 ms.
- Exits run about a fifth to a third shorter than entrances; people already know what is leaving.
- A complex curve (overshoot, long tail) needs a few tens of milliseconds more than a simple fade, or it reads as broken.
- Bigger distance and bigger area get more time; the same speed over a longer path means a longer duration.
- Shorter than about 100 ms often does not register as motion. That is fine for feedback you only need to feel.
- Durations on a small screen can stay the same or shrink slightly; do not scale up with the viewport.

## Easing by direction

| What is happening | Use |
|---|---|
| Arriving, appearing, entering | Ease-out: fast start, soft landing |
| Leaving, closing | Ease-in, or a quick fade |
| Moving between two on-screen positions | Ease-in-out |
| Continuous progress or an infinite loop | Linear |
| Following a finger or a thrown release | A spring or the gesture's own velocity |

Starting curves (cubic-bezier control points):

- Ease-out, gentle: `0.2, 0, 0, 1`
- Ease-out, stronger landing: `0.16, 1, 0.3, 1`
- Ease-in: `0.4, 0, 1, 1`
- Ease-in-out: `0.4, 0, 0.2, 1`

The browser's default `ease` is acceptable for small color changes and not a design decision for anything else.

Duration and easing are separate choices. The same 200 ms feels different with a linear, a soft ease-out and a springy curve; change the curve before you change the duration.

## Springs

- Use for drag release, sheets, and anything that tracks a finger; velocity carries over, so interruption is smooth.
- Product-grade defaults: near critical damping, tiny or no overshoot. A spring with visible bounce is a brand choice and rarely belongs on frequent controls.
- Specify springs as stiffness, damping and mass (or the library's bounce and duration), and cap the settle time so it matches the duration bands above.

## Stagger arithmetic

Total delay = (items - 1) x offset, and the last item still has to finish its own motion.

- Offset about 20 to 40 ms per item.
- Cap the total delay at about 200 to 300 ms; for more items, shrink the offset or stagger only the first several and let the rest arrive together.
- Do not stagger lists people act on at once or update often.
- Entrances can stagger; exits should usually go together.

Example: ten items at 30 ms offset is 270 ms of delay plus 200 ms of motion, which is already near the limit; twenty items must shrink to about 10 to 15 ms or only the first eight stagger.

## Small touches

- Anticipation (a slight move the other way first) is spice for brand moments, not controls.
- Overshoot and squash read as soft, toy-like material; keep them tiny and off hit targets.
- A move along a slight arc looks placed for something flying to a destination; drawers, sheets and anything on a rail slide straight.
