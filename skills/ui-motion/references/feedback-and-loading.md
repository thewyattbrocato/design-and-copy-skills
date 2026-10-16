# Feedback and loading

Load this for waits, confirmations and errors. Feedback should arrive on time, be proportional, and never replace a text message.

## Timing thresholds

- About 100 ms or less feels instant; give a pressed or active state in that window.
- Up to about 300 ms the person notices the wait but keeps their flow; keep the interface still and show no loader.
- After about 300 ms show an inline loader in the control that started the action. Once shown it stays about 400 ms, so it never flashes.
- Past about 1 s, show progress with text saying what is happening. Past about 10 s, add an estimate or steps, and give long operations a cancel.

## Press and hover states

- Every tappable control gets a visible pressed state. Use a small color, shadow or about 2 to 4 percent scale change over 100 to 150 ms.
- Do not move the target out from under the pointer on hover.
- Keep focus indicators; do not animate them away.
- Hover effects are not available to touch; never hide function behind hover.

## Progress inside the control

- Put progress where the action happened: button, then an inline indicator, then a check, in the same footprint so nothing shifts.
- Keep the button's width; swap its label for the state ("Saving...", then "Saved") rather than adding a separate element.
- Do not disable other controls that do not depend on the result.

## Placeholders and skeletons

- When the layout is known, use content-shaped placeholders (skeletons) with a slow, gentle shimmer or none; they feel faster than a bare spinner.
- Keep stale content visible while new content loads when that is safe; dim it slightly and swap when ready.
- When the shape is unknown, use an indeterminate indicator that says what is happening.
- Use determinate progress only when it reflects real completion; do not fake percentages.
- Avoid several loaders on one screen; one wait gets one indicator.
- Start in the loading state on first paint; a blank or empty frame before the skeleton is a defect. The order is loading, then loaded, never empty, then loading, then loaded.
- Leaving a route must not replay the old content's exit over the incoming page, and a cross-fade must not show an empty container for a frame.
- Check the sequence with network and CPU throttled; fast hardware hides these gaps.
- Linear easing suits real progress; looping indicators move at a steady rate.

## Changes outside the person's focus

- A change away from where they look needs a stronger cue than one under the pointer: a short settling highlight (strong at once, fading over about a second) beats a flash or bounce.
- Do not make it louder each time; people learn to ignore it. On a stream of updates, rate-limit the highlight (only changes that matter, or one pulse per batch) and keep the value itself readable.
- Unprompted arrivals (a background toast or banner) use opacity and small travel; a slow start must never delay the information.

## Optimistic updates

- Show the result immediately only when the action almost always succeeds and can be rolled back.
- If it fails, restore the previous state with a short, visible reversal and a message that says what happened.
- Do not use optimistic updates for payments, deletions that cannot be undone or anything with legal weight.

## Confirmation

- Quiet confirmation for small things: a check mark, a brief highlight on the changed value, a toast.
- Toast: enter about 200 to 300 ms, exit faster, announce it to assistive technology. A plain notice stays about 4 to 8 s (longer for more text). A toast carrying an action stays at least 6 to 10 s, pauses on hover and focus, and the action stays reachable afterwards (history, trash).
- A bigger win (completed task, first success) may carry a richer, rare moment. Keep it skippable.

## Errors

- Pair any error motion with a persistent, non-motion cue: text near the problem, a color and an icon.
- A brief, small horizontal shake (a few pixels, about 200 to 400 ms) or a highlight pulse can mark the field; never a long shake of the whole page or form.
- No layout jump when the message appears; reserve its space or insert it without moving the focused field.
- No forced scroll to the top; move focus to the message or the first problem field instead.
- A drag that ends in an illegal spot may animate to the nearest legal spot when the correction is obvious; when the action could destroy data, stop and ask.
- Under reduced motion, drop the shake and keep the highlight and the text.

## Sound and vibration

Visual feedback is the default. Add sound or vibration only when eyes may be elsewhere or a physical press needs confirming, and "delight" alone is not a reason.

- Never the only channel; the same information is always visible, and both are optional with a setting that is easy to find.
- One short, distinct sound per event type (under about a second, never looped); the same chime for success and error teaches nothing.
- Never autoplay on load; honor the device's mute, silent and haptics settings and quiet contexts.
- Vibration carries almost no information: use it to confirm a press or to alert when sound is unwanted, in a few clearly different strengths at most.
- Under reduced motion, drop vibration patterns that mimic shaking.
