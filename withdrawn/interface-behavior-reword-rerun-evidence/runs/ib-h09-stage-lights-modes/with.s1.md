**Recommendation: use explicit modes, but only two or three, always shown, with Record kept apart from the editing modes. Don't use the gesture-overloaded single mode.**

**Assumptions:** one trained operator, a tablet, a long session, and a dark booth where they often look away from the screen. Nobody gave me usage data, so none is cited.

**Why not long-press = paint and drag = select**
- It gives one gesture two meanings that nothing on screen tells apart. Both are touch-and-hold on the same grid. The operator has to guess which one a gesture will trigger, so a mistake happens silently.
- The cost of a mistake is lopsided. A stray select costs nothing. A stray paint changes live lights. The gesture that does damage is the one the hand is most likely to trigger by accident, such as a slow drag or a resting finger.
- A long-press delay is a timing judgment. It varies under stress, in the dark, with cold hands, or with a bumped tablet.
- Long-press and drag have no keyboard route and no visible state, so they fail the accessibility and discoverability checks.

**What the mode design should be**
1. **Select (the default and resting state).** Tapping toggles lights and dragging lasso-selects. It never changes output, so it is always safe. Returning here is the exit from everything else.
2. **Paint.** The operator enters it deliberately, picks the color or level, and then drags. Show the mode where the eyes are: a persistent colored bar or border, the active tool and value in a large label, and a big Done/Esc control. Don't rely on color alone, so include the text "PAINT".
3. **Record is an action, not a mode.** It takes the current look and writes it to a cue. Give it its own button, away from the grid. Name the target cue before writing, for example "Record to Cue 14". Overwriting an existing cue gets one specific confirmation naming the cue it replaces. A new cue number needs none.

**Rules for the paint mode**
- When a drag starts in Select, it only selects. Paint can be applied to the current selection with one tap (select, then apply), so painting by drag is optional and secondary.
- Paint is undoable at every step, with a multi-level undo button that stays on screen. Add a visible "revert to last recorded look" for show-time panic.
- Painting auto-exits to Select after a short idle period. Show the countdown only if the team wants it. This stops the "I forgot I was in paint" case.
- Show paint state on the grid itself with a preview of the values. Make the live-versus-preview distinction obvious if the grid edits live output.

**Why this beats one mode for this team**
- The three tasks have very different risk, and the interface should make that visible. Select is safe, Paint is reversible but live, and Record is committing.
- A trained operator will learn two mode switches quickly. The extra tap is cheap compared to one wrong live change.
- Keep the mode set small (two modes plus one action) so the operator isn't tracking more states than they need.

**Where the single-mode camp is right:** switching modes costs taps during fast cue sequences. To address that, allow a held two-finger or a hardware-style toggle to enter Paint temporarily, springing back to Select on release. A temporary state like that is visible by its very nature, because the finger is holding it.

**Test before committing:** have two or three real operators run a rehearsal with each design, and count wrong-state actions rather than speed. I haven't done this, so treat it as the deciding evidence if the team stays split.
