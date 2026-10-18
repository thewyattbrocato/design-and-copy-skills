Reviewing the five screens together turned up several problems that per-screen review wouldn't catch.

**Must fix before launch**

1. **The progress count is inconsistent.** Screen 1 says "Step 1 of 4". Screens 2–4 say "of 5". Either the flow is 4 steps (and screen 5 is the finish) or 5, but users will notice the total jump from 4 to 5. If the final screen has no bar, "of 4" is probably the intended total, which would make the numbering 1–4 across screens 1–4. Then screens 2–4 need to be "2 of 4", "3 of 4" and "4 of 4". Whichever you choose, make all four screens match.

2. **Screen 4 says "plot", and the rest of the flow says "plant".** The footer reads "you'll need at least one plot before reminders can start." Everything else is about plants. "Plot" looks like a typo or a leftover term from an earlier garden/plot concept. Change it to "plant".

3. **Screen 4 contradicts itself on Skip.** The screen offers a "Skip" link, but the footer says you need a plant before reminders start. Then screen 5 says "Your sanctuary is ready" even if the user skipped and has nothing set up. That's a false claim, and a user who skipped will get no reminders, with no explanation of why. Options:
   - Keep Skip, but make the footer say what happens: "You can skip for now. Reminders start once you add a plant."
   - Show a different final screen for skippers, such as "You're set. Add your first plant whenever you're ready."
   - Drop Skip, if a plant really is required.

**Worth tightening**

4. **Screen 3 promises "one nudge per day", but the app is about watering, feeding and repotting on different schedules.** That's fine if it's a daily digest, but say so: "one daily reminder, only on days something needs attention." As written, users may expect a notification every day. The screen also never mentions notification permission. If you request it, this is the natural place to explain why.

5. **Voice drifts between screens.**
   - Screen 1 says "garden", screen 5 says "sanctuary", and screen 2 says "rooms" and "spaces". Pick one frame. "Garden" is already in screen 1 and fits houseplants.
   - Screen 1 says "we can take care of the rest", which promises more than the app does. It reminds you to care for plants. It doesn't care for them.
   - The Continue / Next / Done button labels are fine, but "Continue" and "Next" are inconsistent for the same action. Use one of them.

6. **Screen 2 gives no signal about selection.** It doesn't say whether it's multi-select or whether you can pick none. "Pick the rooms that have plants" implies multiple, but it's worth confirming that Next is enabled with zero chosen, or that the button states the requirement.

7. **Screen 4: "work out how thirsty it is."** This is cute, but it only covers watering, and the app also handles feeding and repotting. Something like "Fernway will work out its care schedule" is more accurate. Also check that photo and search failure states exist, since the copy has none (no match found, camera permission denied).

**Minor**

- The emoji on screen 5 is fine if it matches the brand. Check that it renders and reads well with screen readers.
- "You're all set!" paired with the "Done" button is slightly redundant but harmless.

**Suggested priority:** fix 1, 2 and 3 first, since they're factual errors or contradictions. Then 4 and 5, which affect trust and expectations. The rest can wait for a copy pass after launch.

I can draft a consistent rewrite of all five screens if you'd like. Tell me which way you want to go on the Skip question first, because the screen 4 and 5 copy depends on it.
