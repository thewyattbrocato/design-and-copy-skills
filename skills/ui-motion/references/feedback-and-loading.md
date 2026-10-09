# Feedback and loading

Load this for waits, confirmations and errors. Feedback should arrive on time, be proportional, and never replace a text message.

## Timing thresholds

- About 100 ms or less feels instant; give a pressed or active state in that window.
- Between about 100 ms and 1 s, the person notices the wait but keeps their flow; keep the interface still and do not show a loader.
- Past about 1 s, show progress. Past about 10 s, show progress with an estimate or steps, and give long operations a cancel.
- Loaders appear after a short delay (about 150 to 300 ms) and, once shown, stay at least a short moment (about 300 to 500 ms) to avoid a flash. If a result is likely to come back almost at once, show nothing.

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
- Linear easing suits real progress; looping indicators move at a steady rate.

## Optimistic updates

- Show the result immediately only when the action almost always succeeds and can be rolled back.
- If it fails, restore the previous state with a short, visible reversal and a message that says what happened.
- Do not use optimistic updates for payments, deletions that cannot be undone or anything with legal weight.

## Confirmation

- Quiet confirmation for small things: a check mark, a brief highlight on the changed value, a toast.
- Toast: enter about 200 to 300 ms, stay about 4 to 8 s (longer for more text, indefinite when it carries an action or an error), exit faster. Pause the timer on hover and focus, and announce it to assistive technology.
- A bigger win (completed task, first success) may carry a richer, rare moment. Keep it skippable.

## Errors

- Pair any error motion with a persistent, non-motion cue: text near the problem, a color and an icon.
- A brief, small horizontal shake (a few pixels, about 200 to 400 ms) or a highlight pulse can mark the field; never a long shake of the whole page or form.
- No layout jump when the message appears; reserve its space or insert it without moving the focused field.
- No forced scroll to the top; move focus to the message or the first problem field instead.
- A drag that ends in an illegal spot may animate to the nearest legal spot when the correction is obvious; when the action could destroy data, stop and ask.
- Under reduced motion, drop the shake and keep the highlight and the text.
