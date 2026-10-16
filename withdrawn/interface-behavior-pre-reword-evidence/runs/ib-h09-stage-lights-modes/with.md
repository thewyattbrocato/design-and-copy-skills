**Go with explicit modes, but make Record an action rather than a third mode.** Select and Paint are two visible tools, and Record is a deliberate, undoable button.

**Assumptions (correct me if wrong):** One operator uses a tablet in a dim booth during live shows. They are trained and use the app often. Paint can change what's on stage. Record writes to a cue that may already exist.

**Why not the always-on gesture model**
- Long-press means paint and drag means select, so one hand movement does two different things with no visible state. A slightly slow drag or a hesitant press in the dark silently does the wrong thing. That is the failure you can't afford at show time.
- Paint changes live lights, so a misread gesture shows up on stage.
- It is hard to see and hard to learn under pressure. Nothing on screen tells the operator which gesture they're about to perform.
- Dragging to select is also what a finger does when it slips, and long-press is what a resting hand does.

**Why not three modes**
- Record isn't a way of touching the grid. It acts on the current look. Making it a mode means the operator can be stuck in it, or leave it armed, which is the worst show-time state.

**Rules**
1. **Select and Paint are a two-way switch, always visible.** Use large labeled buttons at a fixed position, with the active one filled and the grid border or tint changing too. Don't rely on color alone. Select is the default on launch and after Record.
2. **In each mode, the drag does one thing.** In Select, tapping toggles lights and dragging adds a range. In Paint, dragging applies the current color or level. Because the meaning never changes within a mode, the operator doesn't need to time gestures.
3. **Show the paint value next to the Paint switch.** For example, show a swatch and the level. That way the operator can see what the next drag will do before touching anything.
4. **Paint is undoable.** Add a large Undo button and keep a short history. One drag is one undo step. Paint on a selection is allowed, and the selection stays visible afterward.
5. **Record is a button, not a mode.** It acts on the current look and shows what it will write, for example "Record to Cue 12". If that cue already exists, it asks for an explicit, specific confirmation naming the cue ("Replace Cue 12 'Act 2 open'?") because overwriting may not be recoverable. Recording to a new cue number needs no confirmation and can be undone. Don't make it a toggle that stays armed.
6. **Provide a one-tap exit.** A "Done" or "Clear selection" control returns to Select with nothing selected. Hardware Esc does the same if a keyboard is attached.
7. **Add a lock for show time.** An optional "Lock grid" state stops accidental touches while the operator is on something else. It is visible and has one control to unlock.
8. **Offer a small shortcut, not a gesture overload.** If speed matters, let a two-finger tap or an on-screen modifier temporarily switch tools, and show that state while it's held. The default path stays the visible switch.

**Assumed, not measured:** I haven't seen how your operators work. Before you commit, run a quick test with the real operator. Have them run a rehearsal using each design and count the accidental paints.

Whichever camp loses should know the trade-off. You give up a bit of speed (one extra tap to switch tools), and in return the operator always knows what a touch will do.
