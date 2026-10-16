**Go with explicit modes, but fewer than three. Select and Paint are modes. Record is a button.**

Assumptions: one trained operator on a tablet, in a dark booth. Sessions are long and rehearsal and show use are the same. Touch is the main input, with possible gloves or low light. I don't know whether painting changes the live output or only an editor and preview. That matters a lot (see the last rule).

**Why not the one always-on mode**
- A long-press versus a drag is a timing guess made by the software. Under stress or in the dark, a hesitant drag can read as a paint, or a slow press as a select. The same gesture then means two things, and the cost is a wrong look on stage.
- Paint changes data and select only looks at it. Putting both behind one touch makes the harmful action as easy to trigger as the harmless one.
- It's hard to discover and has no keyboard route. The operator can't tell by looking which action their finger is about to do.

**Why not three modes**
- Record isn't a way of touching the grid. It's a one-off act on the current state. Making it a mode adds a switch the operator can forget to leave, and a mode makes sense only for something you do repeatedly.

**Behavior rules**
1. **Select is the default and the resting state.** It never changes anything, so a stray touch is harmless. The app starts in it and returns to it after a period of inactivity or when the operator taps Done.
2. **Paint is entered deliberately and shown where the operator is looking.** Use a persistent labeled toggle, plus a tinted grid border and a banner such as "PAINT: Red 60%". Don't rely on color alone. Exiting is one large tap on the same control. Add a hardware or keyboard shortcut as an extra route.
3. **Paint sets its tool before the drag.** The color or level is chosen first and visible in the banner. A drag then only applies it, so a gesture never means two things.
4. **Every paint stroke is undoable.** Give it one large Undo button that stays on screen (not a toast that disappears) and a last-stroke redo. Nothing asks "are you sure" here, because the undo makes the action cheap to reverse.
5. **Record is a separate, labeled button that doesn't depend on the mode.** It shows what will be saved ("Record Cue 12 from current look"). Saving should be quiet and undoable. If overwriting an existing cue can't be restored, show one specific confirmation that names the cue. A new cue needs no confirmation. Keep cue versions so an overwrite can be rolled back, which is better than a confirmation.
6. **Keep large targets and a separate route for each gesture.** Selecting several lights should have a tap-to-add route as well as drag-select. Paint should have a "apply to selection" button as well as drag, so a shaky hand or a missed drag has a fallback.
7. **If paint affects live output, make that visible and stage it.** Show a Live indicator and use a preview or blind state, with an explicit Apply or Go step, so a painting mistake never reaches the stage directly. If painting only edits a preview, say so in the banner. Please confirm which one it is, because it changes how strict rules 4 and 5 need to be.

**For the team debate:** run a quick test before you commit. Have a few operators do 20 select-then-paint sequences in a dark room under time pressure, on a prototype of each design. Count the wrong-action touches. I'd expect the always-on version to lose, but that is my expectation, not a measured result.
