# Transitions and continuity

Load this for state changes, overlays and page transitions. The transition is the legend of the layout's map.

## Where things enter from and exit to

- A thing appears from where it lives and leaves toward where it goes: a bottom sheet from the bottom edge, a side panel from its side, a menu from the control that opened it.
- What leaves one way comes back the way it left, with the same duration and easing as its counterpart. If the left panel exits left, it returns from the left.
- Once the product has taught a spatial map, do not invent a new direction per screen.
- When a platform convention has already taught a different map, follow the platform.
- A scrim or backdrop fades with its panel, on the same clock.
- Anchor the origin: scale or slide from the trigger, not from the screen center, when the trigger is visible.

## Same object, same identity

- When an object persists across states, move it: a card that expands into its detail view, a row that moves to a new section, a thumbnail that grows to its full image.
- A fade-out followed by a fade-in of a different shape does not show identity.
- When the new state is a different place, not the same object, a quick crossfade or a clean cut is more honest than a fake morph.
- Neighbors close or open the gap smoothly; do not let content snap.
- Keep meaning stable in flight: do not change a control's label, icon and position in one fast move, and do not move a target someone is aiming at.

## Interruptible implementation

- Drive the state from the current value, not from a fixed keyframe list. In CSS, transitions retarget from the current computed value; keyframe animations restart, so avoid them for toggled states.
- Reverse from the current position at the current speed; a tap during an opening reverses the opening.
- Do not block clicks with `pointer-events: none` for the duration of an animation, and do not set controls to disabled while moving.
- For a drag, follow the pointer one to one and release with a spring that inherits velocity.
- For atomic commits, such as a payment or a destructive delete, finish the motion but show the pending state and prevent a double submit.
- Exiting elements stay in the document until their exit finishes; make sure they stop receiving focus and clicks once they start leaving.
- Build the start and end styles in the same layer. Do not hide the end state in the base stylesheet and rely on script to reveal it; if the animation never runs, the content is missing.

## Page and view transitions

- Prefer a short crossfade of the changed region with a shared element carried across. Keep persistent chrome (header, navigation) still.
- Use the browser's view-transition support where it exists and fall back to an instant change where it does not.
- Back navigation reverses the forward motion.
- If a page is heavy, show the new page quickly and let nothing wait on the transition.
- A transition that makes the person wait before they can read has failed, however good it looks.

## Layout and list changes

- Reordering, inserting and removing items: animate position with transform, about 200 to 300 ms, so the eye follows what moved.
- Expanding a section: animate with the platform's height or grid-row technique, or a clip and fade, rather than an unmeasured fixed height; keep it short.
- Removing an item: collapse its space after a quick fade; offer undo for destructive removal.
- Reflow at another breakpoint: opacity, color and blur survive; position paths often do not, so re-plan or drop them.
