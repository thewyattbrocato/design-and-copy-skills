**Go with explicit modes, but only two and with Record kept out of the paint/select mode.** The overloaded gesture is the riskier choice for a show.

*Assumptions: one trained operator, a tablet, long sessions, often in a dark booth, sometimes mid-show with little attention to spare.*

**Why not the one-mode design**
- Long-press means paint and drag means select, so the same finger movement does two different things depending on timing. The skill's rule is that no gesture should silently mean two things.
- A tentative long-press or a slightly slow drag will paint a color across live lights. Painting is the costly action here, and it is the one the timing rule makes easy to trigger by accident.
- Timing gestures degrade under stress, with cold or sweaty fingers, or when the operator is looking at the stage and not the screen.
- Neither gesture has a keyboard or accessible alternative.

**Why not three equal modes**
- Select and Paint are two views of the same grid and share a lot. Making them separate modes means the operator re-selects when switching.
- Record doesn't act on a grid gesture at all. It acts on the current look. Making it a mode adds a state to get stuck in, when it should be a deliberate action.

**What to build**
1. **Select is the default and the safe mode.** Tap toggles a light, and drag selects a range. Nothing in this mode changes output. The settings inspector shows what's selected.
2. **Paint is a separate mode, with a visible indicator.** A large labeled toggle, a colored frame around the grid, and the active color or level shown in the toolbar. Dragging paints only here. One control exits, and it's always in the same place.
3. **Paint what's selected as an alternative.** If lights are already selected, a "Apply to selection" button with a color or level picker does the same job with no drag. This gives a precise, low-risk route and covers accessibility.
4. **Record is an action, not a mode.** It's a button that's unavailable or visibly distinct while painting. Recording the wrong look is costly, so use one specific confirmation that names the cue, for example "Record as Cue 12, overwriting 'Act 2 Open'?" Confirm only when it overwrites an existing cue. A new cue number needs none.
5. **Undo for everything else.** Every paint stroke is undoable with a persistent Undo button and a longer history. Because the outcome is on live lights, undo should restore the prior levels, not just the screen state.
6. **Show-time safeguard.** Offer an optional Show lock that disables Paint and Record, so only Select and playback remain. The operator turns it on when the show starts and off to edit.
7. **Remember state.** Reopen in Select mode every time, not in whichever mode was last active, so a restart never begins in Paint.

**Why this tradeoff**
You pay one extra tap to enter Paint. That cost is small and happens in prep, while a wrongly painted look during a show is expensive and visible to the audience. Entering the mode on purpose, with a clear indicator, is the cheap way to avoid it.

**What to test before committing**
Have a few operators run a rehearsal with the Select and Paint modes and count accidental paints and mode-confusion moments. I haven't assumed any numbers. If operators say the mode toggle slows prep, the fix is a faster, more visible toggle, such as a hardware-style switch or a two-finger shortcut. Don't go back to overloading the gesture.
