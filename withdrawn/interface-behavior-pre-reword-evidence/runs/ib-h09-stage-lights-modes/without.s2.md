**Recommendation: go with explicit modes, but only two of the three should be true modes, and Record should not be a mode at all.**

**Why not the always-on gesture design**

- **Gestures collide with the core task.** On a 48-light grid, a drag meaning "select" and a long-press meaning "paint" means a slightly slow touch or a nervous hand turns a selection into a write. Select is harmless and paint is destructive, and the harmless gesture sits right next to the destructive one.
- **Nothing on screen tells the operator what the next touch will do.** With a mode, the state is visible. With gestures, it lives only in the operator's head, which is where errors happen under show pressure.
- **Dark booth, tablet, stress.** Long-press timing varies by person, by finger, and by whether their hands are cold. It's also hard to discover and hard to undo mentally.
- **Paint is itself a drag.** Making "drag = select" and "drag after long-press = paint" depend on a timing threshold is the weakest point of this design.

**Why not three equal modes**

Record is different in kind. Select and Paint change how touches on the grid are interpreted. Record doesn't touch the grid at all. It captures the current state into a cue. Making it a mode means the operator can be "in Record" while touching lights, which is a confusing state with no benefit.

**The design I'd build**

1. **Two grid modes, Select and Paint, with a persistent, unmissable indicator.** Use a large toggle, a changed border or tint on the whole grid, and a different color for Paint. Default to Select. Paint reverts to Select after a short idle period or on a lift, so the operator can't leave it armed by accident.
2. **Record is a separate action, not a mode.** Put it in its own physical area away from the grid, and require a deliberate confirm (press-and-hold, or two-step arm then confirm) that shows what will be overwritten if the cue already exists.
3. **Undo for paint.** Make it one tap and always visible. Painting is the action most likely to need it.
4. **A show-lock or "live" state.** Optionally, lock Paint and Record while a cue is running, so the riskiest actions need an explicit unlock.

**What would change my mind**

If your testing shows operators constantly switching Select and Paint every few seconds, the toggle cost becomes real. In that case, keep the modes but add a momentary hold-to-paint button (held with the other hand) instead of a timing-based long-press. That keeps the state physically visible and avoids the timing ambiguity.

I'd suggest running both camps' prototypes with a few actual operators, with a stopwatch and an error count. But if you need to decide today: explicit modes, Record separated out.
