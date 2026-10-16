**Recommendation: go with explicit modes, but only two or three of them, each clearly visible. Don't use the always-on gesture scheme.**

**Assumptions:** The user is a volunteer or part-time operator on a tablet. They work in a dim booth, under time pressure, and are often glancing rather than reading. They use it for a few hours per show. I've assumed touch only, with no keyboard.

**Why not the always-on scheme**

The always-on scheme makes one gesture mean two things, and the difference is invisible. Long-press means paint and drag means select. Two failure cases would show up at show time:
- A hesitant drag, or a long-press that isn't held quite long enough, does the wrong thing. A wrong paint changes the lights on stage. A wrong select only highlights the wrong lights.
- A wet or shaky finger, or a tablet in a dark booth, makes timing-based gestures unreliable. Long-press thresholds are also hard to get right for every operator.
- Nothing on screen tells the operator which action they are about to trigger.

Paint changes live output, so it is the dangerous action. It should never be the result of a gesture that is easy to trigger by accident.

**What to build instead**

1. **Three modes, always labeled and shown where the eyes are.**
   - The modes are **Select**, **Paint** and **Record**.
   - Use a large segmented control with text labels, not icons.
   - Tint the grid frame or header per mode, and don't rely on color alone for the cue.
   - Keep it one tap to switch.
   - Select is the default on launch, and the app returns to Select after a Record.
   - The reason is that Select is read-only and harmless, so a stray touch there costs nothing.

2. **Make drag mean one thing per mode.**
   - In Select, tap toggles a light and drag selects a range.
   - In Paint, drag applies the chosen color or level. The paint value should be visible in a swatch next to the mode control.
   - Don't use long-press for anything critical.

3. **Make Paint recoverable.**
   - Each paint stroke is one undo step, with a large persistent Undo button, not a short-lived toast.
   - Show the lights that were touched during the stroke.
   - Decide with your team whether paint affects live stage output or only a preview/blind state. If it can be blind until the operator commits, that removes most of the show-time risk. I'd lean toward that if your console supports it.

4. **Make Record the one deliberate step.**
   - Record is a mode, or at least a separate button, and is never reachable by gesture.
   - It names the target in the control, for example "Record to Cue 12".
   - If it would overwrite an existing cue, say so in the control and require one specific confirmation naming the cue. Overwriting is the case where a confirmation earns its place. For a new cue, record silently and offer Undo.
   - Keep previous cue versions recoverable, so even an overwrite can be rolled back.

5. **Avoid accidental mode changes.**
   - Keep the mode switch away from the grid edge, where palms rest.
   - Switching modes never changes the selection, so the operator doesn't lose work.
   - Keep the selection when switching from Select to Paint, so "select these, then paint them" is a natural flow. Drag-paint also remains available for freehand work.

**What the always-on camp gets right**

Fewer mode switches is a real benefit, and it is worth honoring in the design:
- Select → Paint with the selection kept means the common workflow is one tap.
- If testing shows operators constantly toggling between Select and Paint, consider merging those two and leaving Record separate. Don't merge them by gesture, though. A single "Edit" mode with explicit "paint selected" actions would be safer.

**Check this before committing**

Run a short test with the real operator in booth lighting. Time how long it takes to switch modes, and check whether anyone ever paints when they meant to select. Treat any wrong-mode event as a design bug, not a training problem. I haven't seen usage data, so this recommendation rests on the risk reasoning above, not on measurements.

**Open question that would change the design:** does painting change live output immediately, or can it be staged first? If it's live, make Undo even more prominent and consider a short hold-to-confirm on the Paint mode switch.
