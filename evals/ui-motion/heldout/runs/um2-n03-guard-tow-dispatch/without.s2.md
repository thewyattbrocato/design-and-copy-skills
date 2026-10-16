Ask for a small set of functional animations, and push back on anything decorative. Over a 10-hour shift and about 200 assignments, a flourish that's charming the first time gets in the way by the hundredth. Constant motion in peripheral vision is also tiring, and it makes real changes harder to spot.

**Ask the designer for these**

1. **Assignment transition (about 150-200ms).** When a job is assigned, show it moving or collapsing into the driver's row. This confirms the action landed and shows where the job went. It must never block the next click.
2. **New or changed job highlight.** When a job arrives or its details change, give the row a background tint that fades over 1-2 seconds. This is the main way the board "feels alive," and it tells the dispatcher what changed.
3. **Driver status change.** When a driver goes from available to en route, or similar, flash the status chip once, then settle. It should happen once and not loop.
4. **Drag and drop feedback.** Valid drop targets should highlight, with a quick snap-back on an invalid drop. These should be near-instant.
5. **Failed action feedback.** If an assignment fails, for example because of a conflict or a sync error, show a brief cue plus a persistent inline message. The animation alone is easy to miss.

**Rules for all of them**

- Keep them under 200ms, except for the fade-outs.
- Don't shift layout. Rows must not move under the dispatcher's cursor mid-click. Insert new jobs without reflowing what they're about to click.
- Only animate state changes, never idle state.
- Limit how many run at once. If ten jobs arrive together, batch the highlights so they don't compete.
- Respect `prefers-reduced-motion`.
- Use plain easing, with no bounce or overshoot.

**Say no to these**

- Looping pulses or blinking, including on urgent jobs. Use a static color or icon that escalates with job age.
- Animated reordering of the list as jobs sort.
- Count-up numbers, success celebrations, and hover-grow effects.
- Page or panel slide transitions between views.
- Shimmer or skeleton loaders on routine refreshes.

**What to tell the owner**

A consumer app feels alive because it's delightful. A dispatch console feels alive because it's trustworthy and current. To get that, add a visible "live" or last-updated indicator and highlight changes as they come in. Then the board feels responsive, and dispatchers don't have to wonder whether it's stale.

**How to check it**

Prototype items 1-3 and watch two or three dispatchers use them for a full shift. Track time per assignment and mis-assignments before and after. If the numbers don't improve, the animations aren't earning their place.
