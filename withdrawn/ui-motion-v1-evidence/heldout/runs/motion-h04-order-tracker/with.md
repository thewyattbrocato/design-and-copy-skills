**Assumptions:** this is a mobile app, people open it often, and the tone is calm and decisive. Motion uses transform and opacity only, with no overshoot and no bounce. If you already have motion tokens, swap them in.

## Core rule
Motion happens only to tell someone that something changed while they weren't watching. Nothing moves on a timer, so the screen is completely still between updates. People leave it open for 20 minutes or more, so any ambient motion would be distracting and would drain the battery.

## When it first opens
- **Everything renders at once, with no entrance animation.** There's no fade-up, no stagger and no sliding cards. People open this screen to check one thing, so it should show that thing immediately.
- **Use the last known status from cache.** The status appears already set, and the progress bar is drawn at the correct fill without animating to it.
- **If there's no cached data, show static grey placeholder blocks for the status area and the item rows.** Don't show them at all for the first ~800 ms, because most loads finish within that time and a flash of placeholders looks worse than a short blank. The placeholders don't shimmer. When real content arrives, it swaps in with a 150 ms opacity crossfade.
- **The map placeholder stays still.** When real tiles load, they crossfade over 200 ms.

## When the status changes
This is the only moment that gets real motion. It has four parts and takes about 400 ms in total:

| Element | What happens | Duration / easing |
|---|---|---|
| Progress bar | The filled segment grows to the next step (scaleX from its left edge). The new step's dot changes to the active colour. | 300 ms ease-out (dot colour 200 ms) |
| Status text | The old text fades out, then the new text fades in. There's no slide. The text block has a fixed height so nothing shifts. | 100 ms out, 150 ms in |
| Status area | A soft accent tint appears behind it and fades away. It plays once. This is the cue for someone glancing back at the phone, and it also works if they missed the motion. | 800 ms fade to transparent |
| Screen reader | The status text is an `aria-live="polite"` region. | n/a |

- **Your four states don't each need their own animation.** One transition handles all of them, which keeps it consistent.
- **A new update interrupts the current one.** If one lands mid-transition, the animation retargets from where it is.
- **Skipped states jump straight to the current one.** This happens if the app was backgrounded or an update was missed. It doesn't replay the steps in between. If the app returns from the background, apply the new state with no motion and show only the tint.

### Per state
- **Order received → Being prepared:** just the four parts above. The map stays static, showing the restaurant pin.
- **Being prepared → Out for delivery:** the courier pin appears on the map (fade plus scale from 0.9 to 1, 200 ms). The Contact courier button, if it's disabled before this point, changes colour over 150 ms. It doesn't move, resize or appear from nowhere.
- **While out for delivery:** each server update moves the courier pin to its new position over about 1 s with ease-in-out. A new update retargets the pin from wherever it is. The map camera stays put unless the pin leaves the middle ~60% of the view. In that case it pans over 400 ms.
- **Out for delivery → Delivered:** the progress bar completes and the courier pin fades out over 150 ms. A checkmark on the destination pin draws once over 300 ms. The Contact courier button settles into its inactive style with a 150 ms colour change. This is the end of the order, so the animation ends here.

## What stays still, always
- The header and restaurant name.
- The order summary list. Its 3–8 items never animate in, reorder or highlight.
- The Contact courier button's position and size. Only its colour changes, and it has a normal press state (about 100 ms) when tapped.
- The map's layout and the progress bar's shape.

## What I'd leave out
- Confetti or a celebration on delivery. It's a one-off that someone may never see, and a checkmark is enough.
- A pulsing active-step dot, an animated moving courier icon, a shimmer on placeholders, or a looping "preparing" animation. These would run for the whole wait.
- Dead-reckoned or continuously gliding courier movement between server updates. It would imply live data that you don't have.
- A "last updated 12s ago" ticker. It adds constant change for no benefit.
- Staggered list entrance, count-ups, and a page-level fade-in on open.
- A toast or banner for each status change. The status area already shows it.

## Reduced motion
- Remove the progress fill, the pin glide, the pin scale, the camera pan and the checkmark draw. These all become instant state changes.
- Keep the text crossfade, the tint fade and the colour changes. Those are opacity and colour, not movement, and they carry the information.
- Focus and press feedback stay as normal.

Optionally, add a light haptic on each status change on mobile. It reinforces the change for someone who isn't looking at the screen, and it doesn't add anything visual.
