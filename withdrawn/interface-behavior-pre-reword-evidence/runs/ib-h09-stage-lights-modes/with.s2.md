**Go with explicit modes, but not three equal ones.** Make Select the safe default, make Paint a deliberately armed mode, and make Record an action instead of a mode.

**Assumptions (correct me if wrong):** One operator uses a tablet by touch in a dim booth. They use it often and under time pressure. Paint changes what the lights do, or what will be recorded, and Select doesn't.

**Why not the always-on gesture version**
- One gesture would mean two things depending on a hold timer. Long-press-then-drag can be misread, and a hesitant drag can become the wrong action. That is the silent double meaning the mode rules warn against.
- The two mistakes aren't equally costly. A stray select is harmless. A stray paint changes lights, possibly live. The more dangerous action shouldn't sit one slip away from the common one.
- Timing-based gestures fail with sweaty hands, gloves, a bumped tablet or panic. They also have no obvious keyboard or assistive route.
- The operator can't tell at a glance which action their next touch will do.

**Rules**
1. **Select is the default and the resting state.** Tap toggles a light, and drag selects a range. Nothing in Select mode can change output, so the operator can touch freely. Returning to Select is what you do after any other action.
2. **Paint is armed on purpose.** The operator taps a large, labeled Paint button and picks a color or level. While armed, show the mode where their eyes are: a colored frame or banner reading "PAINT: Amber 60%". Exit with one big control, and also exit automatically after an idle period. The idle length is a placeholder to test with the operator. Don't rely on color alone for the indicator. Use the label as well.
3. **Undo comes before confirmation.** Every paint stroke is one undo step, with an Undo button that stays in place. Don't add "are you sure?" to painting, because it would slow a fast operator down.
4. **Record is an action, not a mode.** It works like publish: a separate, deliberate step. Tapping it shows what will be captured and the target cue, for example "Record to Cue 12 (replaces existing)". If it would overwrite a cue, name the cue and say so. If cue overwrites can be undone or versioned, a confirmation isn't needed. If they can't, this is the one place to confirm, and the confirmation should be specific. Keep Record physically apart from the Paint controls so a paint drag can't land on it.
5. **Keep the mode set small.** Select, Paint, and Record as an action is all there is. Don't add a fourth.
6. **Support the fast path.** Allow a two-finger tap, a hardware key or a pedal to toggle Paint, if the team wants speed. It must still show the banner, so it's a shortcut to the mode and not a hidden gesture.
7. **Keep selection visible.** Selected lights get a checkmark or outline and not only a tint. Show a count ("12 of 48 selected"). Selection survives switching modes, so painting applies to what was selected.

**What the always-on camp gets right:** Mode switching costs time and people forget which mode they're in. The armed-mode banner, one-tap exit and idle timeout address that. A rehearsal test of the two designs, with the real operator timing common tasks, would settle any remaining doubt. I haven't assumed any numbers for that.
