**Recommendation: use explicit modes, but make them hard to get wrong. Don't use the long-press/drag overload.**

**Assumptions (not confirmed):** The operator is trained and uses the app for hours at a time. They hold a tablet in a dark booth, often glancing at it and sometimes in a hurry. Wrong touches happen, and they cost a lot during a show.

**Why not the always-on mode**
- One gesture would mean different things depending on timing. A drag that starts a little too early or late selects when the operator meant to paint, or paints when they meant to select.
- Long-press timing is a bad fit for a dark booth, gloves, a bumped tablet, or a hurried operator.
- A mistaken paint changes live lighting. A mistaken select changes nothing. The two failures are not equally costly, and this design makes the worse one easy to trigger.
- Long-press and drag have no keyboard route and are hard to discover. They also rely on motor precision that varies between operators.

**Why modes work here.** Modes are usually a risk when they're invisible. These three are visible and reflect a real difference in what the operator is doing. Two of them are safe and one is dangerous.

**Behavior spec**

1. **Three modes: Select, Paint, Record.** Show them as a persistent, large, labeled bar that stays in the same place. This lets the operator see the mode at a glance.
2. **Select is the default and the safe home.** On launch, and after any other action finishes, return to Select. A drag in Select only chooses lights and never changes output.
3. **Make the current mode obvious.** Give each mode a label and a distinct tint or border around the grid, plus an icon. Don't rely on color alone, so it works for color-blind operators and in dim light.
4. **Paint changes output, so make it deliberate.** Entering Paint should take one clear tap on the mode control. While in Paint, the color or level being applied shows on screen. Each paint stroke is one undo step, with a big Undo button always visible. Use no confirmation dialogs, because undo covers the mistake.
5. **Record is the one real confirmation.** Overwriting an existing cue can't be restored easily, so show a single, specific confirm: "Overwrite Cue 12 'Act 2 Open'?" Recording to an empty cue number needs no confirmation. Also keep a short history of overwritten cues so even that is recoverable.
6. **Exit modes in one touch.** A large "Done" or Select button leaves Paint. An optional timeout back to Select is probably unwise during a show, because it could change behavior unexpectedly. Test this with operators.
7. **Keep the selection when switching modes.** The operator selects lights in Select, switches to Paint, and applies the color to that selection. Losing the selection on a mode switch would make the modes feel punishing.
8. **Provide non-drag routes.** Allow tap-to-toggle, "select row," "select all," and "invert." Paint should offer "apply to selection" with one tap, not only dragging. This helps accessibility and gives a fallback when dragging is imprecise.
9. **Guard against accidental touches.** Place the mode bar away from the grid edge where palms rest. Make Record and its confirmation targets large with space around them.

**Compromise for the always-on camp.** Their goal is speed, and that's legitimate. You can serve it without overloading the gesture. Use fast, one-tap mode switching, optionally with a hardware or on-screen shortcut. Another option is a "hold to paint" button that paints only while held and snaps back to Select on release.

**Validate with a test.** Have two or three real operators run a rehearsal with each design, and count wrong-mode actions. I haven't measured this, so treat the recommendation as a design judgment and not data.
