# Modes, touch gestures and features that act on their own

Load when a gesture or control means different things in different states, when comparing flows by effort, when designing gestures on a touch screen, or when a feature acts without being asked.

## Find the modes you did not mean to build

A mode is any hidden state that changes what an unchanged gesture does. People watch their content, not your controls, so an indicator tends to be read after the mistake, not before it.

- Audit by gesture, not by feature: list the ten most frequent gestures (tap a row, drag, Enter, Delete, type, swipe) and ask of each what state could change its effect: a selection, a chosen tool, a filter, a "bulk" switch, an input method, offline, a "viewing as" role, a toggle left on yesterday.
- Fix in this order and stop at the first that works: remove the state (act on the object directly); make it last for one use and then revert; make it held, so the hand reports it (hold a key, press and hold); only then keep a persistent mode, with an indicator at the point of attention, one control to leave, and no silent change of what a gesture means.
- Default to one-shot for tools chosen rarely. Change to persistent when the person repeats the same action many times in a row (tagging a pile, painting); then show a plain "Done" exit.
- A single/bulk switch in a toolbar is a mode: replace it with selection, where acting on what is highlighted is the whole rule and the count is visible.
- A toggle whose label flips between verbs ("Hide", "Show") is read as the state. Name the state with an adjective and show both options with the current one marked, or offer separate "Set to X" choices. Change back to a plain switch when the thing it controls is visibly on or off.
- A setting that changes what an action does later is a mode too. Add one only for a real difference in need (language, accessibility, density), not to settle a design argument.

## Order commands so nothing happens out of sight

- Default: pick the object, then the action. The object is already in attention, nothing waits in a pending command, and choosing something else cancels. Change for tools whose result is visible and undoable at once (a brush, a highlighter).
- Adding to a selection and removing from it are separate actions, not one modifier that toggles. Keep the previous selection recallable so a two-thing command (compare, merge, swap) is two selections and one action.
- Typing, paste or Delete must not rewrite content the person cannot see. If a selection can be scrolled off screen, show what will be affected or require an explicit delete.
- Selecting and dragging are different gestures; give dragging a handle so a slip does not move the item.
- Do not move things people learned by position. For a "most used" shortcut, duplicate it and leave the original. Do not switch people from beginner to expert layouts on their behalf.
- Two heavily used tools that differ in a few frequent details, in one environment, will be confused. Align the details.

## Count effort before claiming fewer steps

- To compare flows, list for each: taps or keystrokes, decisions (a point where the person must stop and think), and waits. Strike a decision that is already planned and any step that asks for what the product could infer.
- Rank the variants; the order is dependable, absolute seconds are not, and values from a mouse do not transfer to fingers.
- A longer path where each step does something beats a shorter one where a tap only reveals what could have been shown. Put the must-know value in the row.
- One wider choice beats two nested menus, unless the list is long and unordered.
- If people retry within a second, acknowledgement was too slow or duplicates are not guarded.

## Gestures on a touch screen

- Default: a gesture is a shortcut on top of a visible, labeled control, never the only route. Change to gesture-first only when a button would duplicate the content itself (swiping between photos), and keep arrows or a keyboard route.
- Essential actions use the familiar set: tap, scroll or swipe, long press, pinch and spread, double-tap to zoom. Multi-finger, shape or edge-to-edge gestures are optional extras that need teaching and a visible route.
- The system and the browser own edge swipes, pull-down, pinch zoom, link and image long-press menus and text selection. Do not override them. Keep your own swipe zones off the screen edges, and make a collision harmless (an accidental back swipe must not lose a half-finished step).
- Keep gestures hand-sized: a swipe covers the same distance on a large phone as on a small one. Targets get bigger as they get farther from the thumb's easy arc.
- Row swipes: the row follows the finger and shows the action underneath, commits past a distance on release, snaps back before it; a committed action offers Undo, and the same action is reachable from the row's menu.
- The finger hides what it touches and what lies below. Show the pressed state on the control at once, and show results (a magnified character, a confirmation, an error) above or beside the touch point, with labels above controls and content above the controls that change it.
- A first tap that previews and a second that acts is acceptable only if the preview is also reachable by focus. Otherwise nothing waits behind hover.
- Irreversible actions on touch: undo first. If none is possible, use a deliberate gesture (press and hold, slide to confirm) instead of OK and Cancel, and always keep a plain button route for people who cannot do the gesture. Keep the destructive control out of the frequent-action reach and away from Cancel; make it larger, not closer.
- If something looks like a physical object it should move like one. In a flat design, cue what moves: a cropped neighbor, a handle, a lifted state.

## Teaching a gesture that is not obvious

- Default: no tour. The visible route works from the first minute. After it has been used a handful of times (about five, a starting value), show a short moving hint on the control once, ask them to try it, and stop when they do or dismiss.
- A wrong attempt gets a response (the item springs back and the hint plays), and silence on a first visit gets a hint after several seconds.
- Change to teaching at first sight only when the gesture is the main way through the screen (a deck of cards), and keep a button beside it. Fuller treatment: `teaching-interfaces` if installed.

## When the product acts on its own

For a feature that fires without being asked (auto-sorting, alerts from a saved search, suggested replies, scheduled actions). Software that does a whole job for someone while they are away is `agent-interface-design`; use these points when it is one feature among ordinary ones.

- Show that it is armed: running or paused, the last thing it did, the next check, where the person already looks, with pause one step away. An idle feature must not look like a broken one.
- Default: bound it with limits shown at the grant (how many, for whom, up to what amount) instead of asking before every action. Change to per-action approval when a wrong action reaches other people or cannot be reversed.
- On its first mistake the person gets "not this one" (optionally for a period) and "never or always for this kind", and the second shows the rule it creates. Offer a rule after the same skip twice.
- Editing a rule shows it in plain words with a preview of three groups: newly caught, just inside, just outside.
- Keep a review list of what it did and what it passed over, doubtful first, each with its own undo.
- Do not make watchfulness the safety plan. If the person must take over, warn in stages before the limit, show one persistent view of what is wrong, what is needed and by when, and say who acts.
- Stopping needs no reason and says what happens to work already in flight.

## Checks

- A mode fix names the gesture and the state, and removes, expires or holds the state before adding a banner.
- No toggle changes its label to the opposite verb; no selection toggles through a modifier alone.
- Every gesture has a labeled control that does the same thing.
- No pressed state or result is drawn only under the finger; no hint appears before the visible route has had a chance.
- A self-acting feature shows its armed or paused state and has both a one-time and a standing correction.
