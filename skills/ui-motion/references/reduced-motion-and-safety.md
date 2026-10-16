# Reduced motion and safety

Load this whenever motion ships. Motion is an enhancement of a state, never the state itself.

## What reduced motion means

When the system asks for reduced motion (the `prefers-reduced-motion: reduce` media query on the web, the platform setting elsewhere), honor it by default. A page-level toggle is an extra for unusually large effects, not a replacement.

Remove or replace:
- Large movement, slides across the screen, zooms and scale-ups of big areas.
- Parallax, scroll-linked movement and scroll-jacking.
- Auto-advancing or looping content, and background video that moves.
- Shakes, bounces and spins.
- Long staggers.

Keep:
- Focus indicators and every state change (pressed, selected, expanded, error).
- Opacity and color transitions, short or instant.
- Progress indicators that report real status (calm them; do not remove the information).
- Anything that is the content itself.

Replace a slide with a short fade or an instant change; the information is the same.

## Implementation

Build the effect inside the media query rather than deleting transitions globally:

```css
.panel { transition: transform 250ms var(--ease-out), opacity 250ms var(--ease-out); }
@media (prefers-reduced-motion: reduce) {
  .panel { transition: opacity 150ms linear; transform: none; }
}
```

Avoid a blanket rule that sets every `transition` and `animation` to none; it also strips focus and state feedback. If a blanket rule is the only practical fix, exempt focus and state styles. In script, read the same preference and branch before starting movement, and listen for changes.

Build the start and end styles in the same layer, so the end state shows even if the animation never runs.

## Vestibular triggers

Harm tracks how much of the screen moves, whether directions disagree (parallax, scroll that fights the finger), and how far something appears to travel at speed. Avoid large moving areas, depth zooms, spinning, and anything that moves under the pointer. Small, direct, person-triggered fades and short slides are low risk.

## Flashing, pauses and autoplay

These are external accessibility standards; check the current guideline before putting numbers into a deliverable.

- Do not flash more than three times in any second, and avoid large high-contrast flashes at any rate. Fast alternation of full-screen colors counts.
- Anything that moves, blinks or scrolls on its own for more than about five seconds, and anything that updates automatically, needs a way to pause, stop or hide it.
- Carousels and tickers need pause controls and should not advance while someone is reading, hovering or focused.
- No autoplaying sound. User-started media is a different case: give it controls, captions and a transcript where useful.

## Do not rely on motion alone

- Put the same information in text, names and live regions; screen readers do not see motion.
- Keyboard users must reach the same controls and trigger the same results.
- A mascot or highlight pointing at a field is fine only if the focus ring stays.

## Performance

- Animate transform and opacity first; they are the cheapest properties to composite. Check current paint and layout cost before animating anything else, and avoid width, height, top and left on large elements.
- Use `will-change` sparingly and only on elements about to animate, then remove it.
- Test on a slow device; people notice stutter far more than a frame counter. A beautiful curve that stutters is a bad curve.
- Steady frame pacing beats a higher rate that dips; prefer a calmer effect that holds over a rich one that stutters.
- Avoid animating very large distances; shorten the travel (start near the destination) or cross-fade instead.
- Do not load a heavy animation library for a few fades.
- If a screen feels slow, measure first: long tasks and late input response cost more than long durations.

## Motion handoff spec

For every motion, write one row:

| Motion | Trigger | Properties | Duration | Easing | Delay | Interrupt behavior | Reduced motion |
|---|---|---|---|---|---|---|---|

Keep the vocabulary small: three or four durations, three easings, one stagger value, recorded as values rather than adjectives. Name presets by role in the team's own words ("enter-overlay", "dismiss-toast"), each with its numbers and one purpose line, so squads reuse them instead of inventing their own. A video or prototype alone is not a spec; it must list the numbers too. When the system has tokens, use their names; do not invent a new set.

## Temperament as numbers

| Word | Travel | Overshoot | Duration against the baseline |
|---|---|---|---|
| Quiet | 4 to 8 px, opacity leading | none | about a fifth shorter, ease-out |
| Crisp | 8 to 16 px | none; arrives and stops | baseline |
| Lively | 12 to 24 px | up to about 5 percent, never on a hit target | about a fifth longer |

Apply one word everywhere. If the product's motion is already a mix, audit it first: list every motion, group them, and decide on one set rather than nudging dozens of near-matches.
