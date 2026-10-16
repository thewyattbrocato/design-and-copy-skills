**Go with explicit modes, but only two: Select and Paint. Make Record a separate button, not a mode.**

Assumed: one trained operator, a tablet in a dim booth, sessions of a few hours, with live show-time use where a wrong change can reach the stage.

**Why not the always-on, gesture-based option**
- It gives the same grid two meanings, depending on whether the finger lingers or moves. The operator can't see which one they'll get until it happens.
- A hesitation before a drag, a slightly slow press, a shaky hand or a bumped tablet all turn "look at settings" into "change 12 lights." Painting is the costly action, and this design puts it one timing slip away.
- The operator learns it by feel, and it breaks down under pressure or in the dark.

**Why not three modes**
- Record isn't a grid gesture. It captures whatever the look currently is. Making it a mode adds a state to forget and a way to be "in Record" when you meant to be painting.

**Rules**
- **Select is the default and the safe state.** The app starts in Select, so taps and drags only look and never change anything.
- **Show the mode where the eyes are.** Use a large, persistent two-segment switch next to the grid, with the active mode labeled in text. Also change the grid's frame or tint, not just a color, so it reads in the dark and for color-blind users.
- **Paint shows its tool.** The chosen color or level appears in the mode bar, so the operator sees what a drag will do before they do it.
- **One tap exits Paint.** The Select segment is always visible. No hidden gesture is needed.
- **Each paint stroke is one undo step.** Put a large Undo button beside the mode switch. This matters more than any confirmation, because a confirmation before every stroke would slow the operator down.
- **Record is its own button, away from the grid.**
  - A new cue needs no confirmation, but it can be undone.
  - Overwriting an existing cue gets one specific confirmation that names the cue, for example "Replace Cue 12 'Act 2 sunset'?" This is the one case where nothing can restore the old look, unless you add cue version history. If you do add it, you can drop the confirmation.
- **Keep long-press free.** Use it for nothing, or for a secondary action like "select this light only." Never use it to change what a drag means.

**Open question for the team:** is painting live, or does it go to a preview that the operator then commits? If a preview exists, most of the risk disappears and Paint can be looser. If painting is live, treat everything above as required.

**Test before committing:** run a rehearsal in a dark booth with the operator. Count accidental changes and mode errors for each design. That will settle the argument better than opinion.
