**Recommendation: three explicit modes (Select, Paint, Record), with a few safeguards. Don't use the gesture-overloaded always-on mode.**

**Why the always-on mode is risky for this use**
- **One gesture, two meanings.** A drag selects, but a long-press then drag paints. The difference is a timing threshold. A nervous or rushed operator, a dark booth, or a slightly slow finger will cross it by accident. The result is a color or level written across many lights during a live show.
- **Paint is destructive and Select isn't.** The two get different treatment only by a hidden timing rule, so the destructive action is the easy one to trigger by mistake.
- **No visible state.** The operator can't see what a touch will do before they make it. Under stress, "what will this do?" should be answered by the screen, not by remembering a threshold.
- **Tablet touch is imprecise.** Palm contact, a jostled tablet, and gloves or cold hands all produce stray long-presses and drags.
- **Accessibility.** Long-press timing is hard for people with tremor or slow motor response, and a fixed threshold can't suit everyone.

**Why separate modes win here**
- Each mode makes a drag mean one thing. You can see the mode, so errors are predictable and avoidable.
- You can give each mode its own look, such as a color-coded frame and a persistent label. The operator knows what the next touch will do.
- You can make the dangerous modes harder to enter or act in than the safe one.

**The cost of modes is mode errors** (acting in the wrong mode). Reduce those with these measures:
1. **Default to Select (the safe, read-only mode)** at launch and after each Paint or Record action finishes.
2. **Make the mode unmistakable.** Use a large persistent indicator, a screen-edge tint per mode, and a label, not color alone.
3. **Keep the mode switch large and fixed-position**, away from the grid so it isn't hit while working.
4. **Make Record a deliberate two-step action.** Use a confirm showing the cue name or number and what will be overwritten. Record is the one that changes saved show data.
5. **Add undo for Paint** (and a short-lived one for Record), so a mistake is recoverable in one tap.
6. **Show a live preview or "uncommitted" state in Paint** so changes are visible before they're finalized, if your lighting system allows it.
7. **Consider a "lock" or "blackout-safe" state** for show time, where Paint and Record are disabled until the operator deliberately unlocks them.

**Where the other camp has a point.** Fewer mode switches means faster work, and fast matters mid-show. If the team wants speed, keep three modes but make switching one tap. You could also let Select stay always available as a quick-look gesture inside the other modes, since it's harmless. Don't put destructive actions behind a timing-based gesture.

**One thing to validate.** Run a short test with your actual operator, in a dim room, under time pressure. Count wrong-mode and accidental-paint errors in both designs. If the modal design's errors are mostly "forgot the mode," strengthen the indicators. If the always-on design's errors are accidental paints, that confirms the decision.
