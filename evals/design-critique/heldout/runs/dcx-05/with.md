**The flow contradicts itself in three places, and none of them show up when you review one screen at a time. Fix the Skip path and the progress count before launch.**

**Blockers and majors**

1. **Skip contradicts the rest of the flow (Major, screen 4 to 5).**
   - Screen 4 offers "Skip". The footer says reminders can't start without a plant. Screen 3 has just had the user choose a reminder time.
   - A user who skips gets "You're all set! Your sanctuary is ready" on screen 5, but nothing will ever remind them. Reminders are the whole product, so this is a silent failure of the core promise.
   - Fix: either drop Skip, or keep it and show a different screen 5 for that path. For example: "You're in. Add a plant whenever you're ready. Reminders start once you do." with the button "Add a plant".
   - Also move the warning out of the footer. It currently sits below the buttons, where it's easy to miss, and it only appears after the user has been offered an escape.

2. **The progress count changes mid-flow (Major, all 4 numbered screens).**
   - Screen 1 says "Step 1 of 4". Screens 2–4 say "of 5". The user sees the total grow right after they commit.
   - Even with "of 5" throughout, the fifth step would be screen 5, which has no progress bar. That leaves the count at 4 steps plus a finish.
   - Fix: use "of 4" on all four, and keep the final screen outside the count. Better still, derive the total from the step list so it can't drift.

**Moderate**

3. **Vocabulary drift (Moderate, 4 screens).**
   - The same thing is called "garden" (1), "spaces" and "rooms" (2), "plot" (4) and "sanctuary" (5).
   - "Plot" is the worst of these. It's the only word in the flow that means a plant, and it's in the one warning that matters. A user could read it as a garden bed or a room, and "Add your first plant" is on the same screen.
   - Fix: say "plant" wherever you mean a plant. Pick one word for a room (screen 2 uses both "rooms" and "spaces"). Keep "garden" or "sanctuary" as a brand flourish in one place at most.

4. **The room answers go nowhere (Moderate, screens 2 and 4).**
   - Screen 2 asks which rooms have plants. Screen 4 adds a plant with no room assignment.
   - If the answer isn't used, cut the question. If it is used (grouping, light assumptions), screen 4 should ask which room the plant is in. Right now the user does work that has no visible payoff.

5. **Notification permission isn't in the copy (Moderate, screen 3).**
   - Screen 3 sets a daily notification time. If the OS permission prompt is missing or comes at launch, the reminder will never arrive.
   - Fix: trigger it from screen 3's "Next", with a line of context. Confirm that a denial is handled.

**Minor**

6. **Button labels (Minor).** Screen 1 says "Continue" and screens 2–3 say "Next". Pick one. On screen 4, say which of "Take photo" and "Search by name" is the primary action. As written they read as equals.
7. **Filler and ambiguity (Minor).** "Choose a time that suits you" adds nothing. In "work out how thirsty it is", "it" has no clear referent. Try "how often it needs water".

**Keep**
- The question-style titles on screens 2 and 3. They say what to do without instructions.
- "You can add more spaces later" and "one nudge per day". They lower the stakes and set expectations on notification volume.
- Offering both photo and search on screen 4, so users aren't forced into one input method.

**Assumptions and gaps:** I'm judging copy only. I haven't checked layout, contrast, touch targets or whether screen 2 requires a selection. If Skip does lead to a different end screen, tell me and I'll re-rate finding 1.
