# Order tracking screen: motion plan

**Principle:** the screen sits open for 10 to 30 minutes and changes only 3 times. Almost everything should be still. Motion is reserved for the moments a status changes, so it carries information.

## On first open

- **Nothing choreographed.** The header, status area, map placeholder, item list and button all render in their final positions at once. Don't stagger the list items, because 3 to 8 rows staggered at 50 ms each is a 150 to 400 ms delay before people see their order.
- **If data is already cached or arrives within ~300 ms:** show the content with a single 150 ms opacity fade-in on the whole screen, or no fade at all.
- **If data takes longer than ~300 ms:** show static grey skeleton blocks in the status area and list, with no shimmer. Crossfade to real content over 150 ms when it arrives. Never show a spinner over the whole screen.
- **Status area on open:** it shows the current state with the four-step indicator already filled to that point. Don't animate the indicator from zero up to the current step. That would suggest progress is happening when it isn't.
- **Map placeholder and button:** still. They never animate on load.

## When the status changes

Total sequence is about 1.5 s, and only the status area moves.

1. **Status label and text (0 to 200 ms):** crossfade the old label to the new one, with a 4 to 8 px upward slide on the incoming text. No slide on the outgoing text.
2. **Step indicator (0 to 300 ms):** the fill advances to the next step with ease-out. The new step's dot scales from 0.8 to 1 as it fills.
3. **Attention cue (200 ms to ~1.5 s):** the status area background gets a soft tint (the brand color at ~10% opacity) that fades out. It plays once and doesn't loop. This is the part that catches the eye of someone glancing back at the phone.
4. **Haptic and accessibility:** one light haptic tap if the app is in the foreground. Put the status text in an `aria-live="polite"` region so screen readers announce it.
5. **ETA or subtext:** if it changes along with the status, it swaps in the same crossfade. If the ETA changes without a status change, swap it with a 150 ms crossfade and no tint.

**Button behavior**
- "Contact courier" doesn't animate.
- Before "Out for delivery", I'd show it disabled, since there's no courier yet. At that transition, switch it to enabled with a 150 ms color change.
- On "Delivered", replace it with a quieter "Get help" or "Rate order" action, again with a simple 150 ms swap.

**Per-state notes**
- **Received → Being prepared:** the standard sequence above, nothing extra.
- **Being prepared → Out for delivery:** the standard sequence, plus the button enabling. This is the biggest change for the user, so it's worth a slightly stronger tint.
- **Out for delivery → Delivered:** the standard sequence, plus a checkmark that draws itself once over ~400 ms. After that, the screen is completely static. Dim the map placeholder to a muted state over 300 ms.

## Edge cases

- **Poll returns the same status:** do nothing. No refresh flicker, no indicator, no "updated" flash.
- **Status skips a step (for example, Received straight to Out for delivery):** jump directly to the new state with the normal sequence. Don't animate through the skipped step.
- **App returns from background with a changed status:** apply the new state instantly with no transition, then play the 1.5 s tint once so the change is noticeable.
- **Reduced motion enabled:** drop the slide, the dot scale and the checkmark draw. Keep the instant text swap plus the background tint, since color change isn't vestibular motion.
- **Network failure:** keep showing the last known status. After about 2 minutes without a successful poll, show a small static "Connection lost, retrying" line under the status. Don't animate it.

## What I'd leave out

- **Looping animations:** pulsing dots, an animated courier icon, a "breathing" status badge. They drain battery, are distracting over a 20-minute wait, and make the screen look busy when nothing is happening.
- **A fake progress bar** that creeps forward between states. It misrepresents real progress.
- **Pull-to-refresh and refresh spinners.** Polling is background work and shouldn't be visible.
- **Confetti or celebration on Delivered.** A single checkmark is enough, and the person is probably about to eat or answer the door.
- **A ticking countdown or seconds-level ETA.** Update the ETA at minute granularity, and only when the value actually changes.
- **Staggered list entrance, parallax on the map, or bouncy easing.** None of them help the user understand their order.
- **A toast or banner for each status change.** The status area already changes, so a toast would repeat it.

## Timing summary

| Element | Duration | Easing |
|---|---|---|
| Initial content fade (if any) | 150 ms | ease-out |
| Skeleton → content | 150 ms | linear |
| Status text crossfade + slide | 200 ms | ease-out |
| Step indicator fill | 300 ms | ease-out |
| Background tint | ~1.5 s | ease-out, plays once |
| Button state change | 150 ms | linear |
| Delivered checkmark draw | 400 ms | ease-in-out, plays once |

If you tell me the platform (iOS, Android or web), I can translate these into specific implementation notes. That includes the live-region and haptic APIs and the reduced-motion setting.
