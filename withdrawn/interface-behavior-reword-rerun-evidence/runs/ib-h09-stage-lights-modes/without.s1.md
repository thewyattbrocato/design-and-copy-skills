**Go with explicit modes, but make it two modes plus a separate Record action, not three modes.**

**Why not the always-on gesture design**
- Long-press versus drag is a hidden distinction. The operator can't see which one they're about to trigger. In a dark booth, in a hurry, a long-press that is slightly too short or a drag that starts too slowly will do the wrong thing. This is the main show-time risk.
- The two outcomes aren't equally bad. A wrong select is harmless. A wrong paint changes 48 lights' output, possibly live.
- Touch timing varies with fatigue, cold hands, a bumped tablet, or a different operator. You can't tune a threshold that works for everyone.
- The design has no on-screen signal of what the next touch will do.

**Why modes are safer**
- Mode errors are real: the operator forgets which mode they're in. But they're visible and fixable. Gesture errors are invisible until after the damage.
- You can reduce mode errors with design:
  - Make **Select** the default and the safe resting state.
  - Make **Paint** unmistakable. Change the frame or background color and show a large persistent label, not just a small toggle highlight.
  - Have Paint auto-revert to Select after one stroke or a short idle timeout.
  - Add a one-tap **Undo** for the last paint.

**Treat Record differently**
- Record isn't a way of touching the grid. It's a commit action on the current look. Making it a mode adds a third state to track for no benefit.
- Make it a dedicated button, away from the grid and the mode toggle. Use a deliberate confirm step, such as hold-to-record or a confirm tap that shows the cue number and name. Overwriting an existing cue should need an extra confirmation.

**Where gestures still help**
- Inside Select mode, drag-to-select and tap-to-toggle are fine. They're both harmless, so ambiguity costs nothing.

**One question that could change this**
Does painting change live output, or does it go to a preview/blind state first? If it's always blind until the operator commits, the stakes drop, and a lighter design becomes more defensible. If it's live, stay with explicit modes.

Before committing, I'd run a short test with your real operator. Have them do a scripted sequence of select, paint, and record in low light, and count wrong-action errors under each design.
