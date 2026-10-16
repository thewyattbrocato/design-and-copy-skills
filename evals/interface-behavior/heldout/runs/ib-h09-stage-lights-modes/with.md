**Recommendation: three explicit modes (Select, Paint, Record), with a few guardrails. Don't use the gesture-overloaded single mode.**

**Assumptions:** The operator is trained and uses the app on a tablet, touch only. They work in a dark booth, often during a live show, with little attention to spare. I haven't been given any usage data, so none is cited here.

**Why not the one-mode design**
- The one-mode design makes the same touch mean different things depending on duration and movement. A long-press is "paint" and a drag is "select". A slightly slow drag or a hesitant press will do the wrong thing, and the operator can't tell until the lights change. That is a silent double meaning, and it fails most where mistakes cost the most.
- Hands are imprecise in a dark booth and at speed, and gesture timing thresholds are hard to hit reliably under pressure.
- Paint changes live output. Select is harmless. Putting them on near-identical gestures puts a harmful action next to a harmless one.
- Neither long-press nor drag-to-select has a keyboard or non-gesture route, so accessibility gets worse.

**Why modes are acceptable here**
Modes are normally something to avoid. They are fine when each one has a visible indicator and an obvious exit, and these three do. They also match how the work actually goes: look, then change, then commit.

**Rules for the three-mode design**
1. **Mode bar:** Keep a large, labeled, always-visible three-way switch (Select | Paint | Record) in a fixed spot. Use big touch targets, a text label, and a distinct shape or icon for each mode, so color is not the only cue. The operator is already looking at the grid, so also tint the grid frame or header per mode.
2. **Default to Select:** Start in Select, and return to it after Record and after a long idle period. Select is the safe state, because a stray touch only highlights lights.
3. **Paint is the only mode that changes live output.** Show the active color or level as a swatch in the mode bar. Paint strokes should be undoable as one unit per drag, with a prominent Undo button, because undo is cheaper than confirmation mid-show.
4. **Record needs a confirmation, because it can't be undone.** If recording overwrites an existing cue, show a specific confirmation that names the cue and says what gets replaced. If cues are versioned, skip the confirmation and offer Undo instead. Make that the only confirmation in the app, so people still read it.
5. **Keep Record separate from the grid.** Make it a deliberate button in its own area, not a grid gesture. That way a touch on the grid can never record a cue.
6. **Selection persists across modes.** The operator can select lights, switch to Paint, and apply to that selection. Paint can then offer both "drag to paint" and "apply to selection", which makes the common case a tap instead of a gesture.
7. **Exit:** Tapping the active mode again, or a dedicated Done button, returns to Select. Support external keyboard shortcuts if the tablet will have one.
8. **Accessibility:** Every drag action should have a tap alternative, such as tap-to-toggle in Select and tap-to-apply in Paint. Announce mode changes to screen readers.

**Cost to accept:** Operators will sometimes forget which mode they are in. The big indicator, the tinted grid, the safe default and the single-unit undo are there to cover that. A quick test with an operator under time pressure should show whether the indicator is noticeable enough.

**What to tell the other camp:** Their concern is real. Switching modes costs time. Selection persisting across modes and tap-to-apply cut the number of switches, which gets you most of the speed of an always-on design without the ambiguous gesture.
