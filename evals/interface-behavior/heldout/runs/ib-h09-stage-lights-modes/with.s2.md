**Recommendation:** use neither option as proposed. Make select the default state, make paint an explicit tool, and make record a deliberate action instead of a mode. That gives two modes and one button.

**Assumptions:**
- The user is one operator on a tablet, in a dim booth, working under time pressure.
- They use the app every show and know the rig.
- Paint changes what's on stage right away. If paint only edits a preview, the rules below can be looser, so tell me.

**Why not the always-on mode (long-press = paint, drag = select)**
- It gives one surface two meanings, chosen by a timing difference. A hesitant drag or a resting finger turns into a paint, and that paint lands on live lights.
- Nothing on screen shows which gesture is about to fire, and a stressed operator will misjudge a 400 ms threshold.
- Painting is the most common bulk edit, and it would need the slower, more fragile gesture.
- Drag-to-select also conflicts with scrolling and with palm contact on a tablet.

**Why not three equal modes**
- Record isn't a way of touching the grid. It commits the current look. Treating it as a mode means the operator can be "in record" and tap lights by accident, or forget which mode they're in.

**Rules**
1. **Select is home.** When the app opens or any other tool finishes, it returns to select. Tapping lights toggles them, and a drag selects a range. Select never changes output, so it's the safe resting state.
2. **Paint is an armed tool.** The operator picks Paint from a large, labeled control. While it's active, the grid border and toolbar change visibly, not just a color tint, and the active color or level is shown beside the grid. An obvious Done control exits, and the tool also exits when it has been idle a while (I haven't picked a duration, so test it in rehearsal). Dragging while armed paints, and dragging in select mode never does.
3. **A paint stroke can be undone.** Each drag is one undo step, with a large Undo within reach and a hardware or keyboard route if the tablet has one. Because a wrong stroke is cheap to reverse, there's no "are you sure" before painting.
4. **Record is a button, not a mode.** It acts on the current look and shows what it will capture (the cue number, and whether it will overwrite an existing cue). Recording a new, empty cue needs one tap. Overwriting an existing cue needs one specific confirmation naming the cue, unless you keep versions and can restore, in which case offer Undo instead.
5. **Show state where the operator is looking.** Keep the mode name, selection count, and the live or preview status in a fixed bar next to the grid. Don't rely on color alone, since stage-dim screens and color blindness both undermine it.
6. **Everything has a non-gesture route.** Select all, clear selection, and select-by-group should be buttons. Painting a selection should work as "select, then apply", which is slower than a drag but safer when the operator's hands are busy.
7. **Keep touch targets large.** 48 lights on a tablet gives roughly 6×8 cells, so size them for a gloved or hurried finger. Don't add hover-only or long-press-only functions.

**Test before committing:** give an operator a rehearsal run with deliberate distractions (cue calls, a dropped script). Count wrong-mode paints and accidental records. If paint mistakes are still frequent, make Paint hold-to-use, where the tool is active only while a thumb stays on the button, before adding more confirmations.

**Open question:** does paint change the stage immediately, or does it edit a preview that goes live when the operator commits? If it's immediate, rule 2's visible armed state and rule 3's undo are essential. If it's a preview, you can make the whole thing less strict.
