**Go with explicit modes, but trim them to two plus a button.** The always-on gesture model is the riskier choice for show-time use.

**Assumptions:** one operator on a tablet, in a dark booth, under time pressure, using touch with possibly gloves or shaky hands. I'm also assuming painting changes what's on stage, or could if you're live. If you only paint blind, the stakes drop but the answer stays the same.

**Why not long-press = paint, drag = select**
- One gesture means two things depending on a timing threshold the operator can't see. A drag that starts a beat late paints over lights instead of selecting them. In a dark booth with a rushed hand, that's the exact mistake you said is costly.
- Nothing on screen says which one you're about to do, and there's no keyboard or switch route for it.
- It also gives you no safe place to rest. The operator can never touch the grid without risking a change.

**What to build**

1. **Select is the resting state, and it's read-only.**
   - A tap or drag selects lights and shows their settings. It can't change anything.
   - This is the default so that a stray touch is harmless.

2. **Paint is a deliberate mode.**
   - Enter it by tapping a Paint tool, or by holding a thumb-reachable Paint key. Hold-to-paint is the safest version, because the mode ends when the finger lifts.
   - While it's active, tint the whole grid border, show the color or level being applied, and keep a large Done button in the same spot. Don't rely on color alone. Add a text label and an icon.
   - Make every paint stroke one undo step, with an Undo button that's always visible. Painting is reversible, so don't add "are you sure" prompts.

3. **Record is not a mode or a gesture. It's a button.**
   - It always shows the target cue, for example "Record → Cue 12".
   - It does nothing to the grid, so it can't collide with select or paint.
   - If the target cue already exists, name it and what you're overwriting, for example "Overwrite Cue 12 (last saved 7:42)?". That's the one place a specific confirmation earns its keep, because a silent overwrite of a cue is what hurts mid-show.
   - If the cue is new, record immediately, show a quiet confirmation in place, and offer Undo. Keep a version history of cues so even an accepted overwrite can be recovered.

4. **Safeguards for show time**
   - Offer a lock or "show mode" that disables Paint and Record, so only Select works while cues are running.
   - Switching modes never clears the selection.
   - Every action has a touch target big enough for a gloved or hurried hand, and a keyboard or hardware-button route.

**Why this beats three equal modes:** Record isn't really a mode, so making it one adds a switch the operator has to remember. Two states (Select and Paint) plus a clearly labeled button covers all three jobs, and the most frequent one, looking, is always safe.

**Open question for your team:** does painting affect live output, or only a preview? If it's live, I'd make Paint require show mode to be off, or show an explicit "LIVE" indicator while painting. I'd test either choice with a real operator in booth lighting before settling it.
