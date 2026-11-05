**Verdict: not ready to ship.** Each screen works on its own. The problems are between screens. The flow ends by telling the user they're "all set," but screen 4 says reminders can't start yet. The progress bar also changes its total partway through.

**Findings, ranked**

1. **Blocker: Screen 4's footer contradicts screens 4 and 5.** "You'll need at least one plot before reminders can start" is the only mention of this requirement. "Skip" sits as an equal option, and screen 5 says "Your sanctuary is ready." A user who skips, or who misses the small footer, finishes onboarding with reminders silently off. Fix: decide the minimum needed to start reminders. Then either make that step required, or have screen 5 state the real state ("Add a plant to start your reminders") and have Skip lead there.

2. **Major: "Plot" is never defined.** Screen 2 asks for rooms and mentions "spaces." Screen 4 introduces "plot" for the first time, as a requirement. Users can't tell whether a plot is a room, a pot, or a location. Fix: use "room" throughout, since it matches the screen 2 chips. If plots are a separate concept, collect them explicitly on screen 2 with a reason.

3. **Major: The progress total changes.** The bar reads Step 1 of 4, then 2 of 5, 3 of 5, 4 of 5. This shows on every screen, so it reaches every user. Fix: use one total of 5. Screen 1 counts as step 1, or it gets no label, like screen 5.

4. **Major: Five words describe one place.** Garden (screen 1), rooms and spaces (2), plot (4), and sanctuary (5) all refer to where plants live. Fix: keep "room" as the noun. "Garden" and "sanctuary" can stay as brand flavor in the welcome and completion copy, but not as nouns the user has to map to data.

5. **Major: Screen 2 doesn't say whether a selection is required.** If Next works with no chips selected, the plot problem from finding 1 comes back. Not checked: whether Next is disabled when empty. Either way, the copy should state the rule, for example "Pick at least one room." Also unstated: whether multiple selection is intended.

6. **Major, unverified: Screen 3 doesn't prepare the user for the notification permission prompt.** Reminders need OS notification permission. The copy doesn't say when that prompt appears. If it appears cold, many users will deny it. Fix: add one line on screen 3, such as "Allow notifications so we can send it," or move the request to a point where its purpose is clear. Not checked: when the app actually requests permission.

7. **Minor: Screen 1 doesn't say what Fernway does.** A newcomer can name the next action (Continue) but not the offer. The three jobs (water, feed, repot) appear in neither the title nor the body. Suggested body: "Get reminders to water, feed and repot your plants."

8. **Minor: Screen 4 promises something vague.** "Fernway will work out how thirsty it is" doesn't say what the user gets. Suggested: "Fernway will set a watering schedule for it."

9. **Minor: Forward button labels are inconsistent.** Continue (screen 1), Next (screens 2 and 3), Done (screen 5). Pick one forward verb for the middle screens. Continue fits best.

10. **Taste: "Time to get growing 🌱" and "sanctuary."** The tone is fine if the rest of the copy matches it. Once findings 4 and 7 are fixed, this is a preference, not a problem.

**What works and should stay**
- One decision per screen. Nothing asks the user two things at once.
- The time picker has a default (8:00 AM), so Next is never blocked on that screen.
- Screen 3 says "one nudge per day." That sets a clear expectation about notification volume.
- Screen 4 offers Skip, so a user without a plant handy isn't trapped. (Finding 1 is about what Skip leads to, not the option itself.)
- Screen 5 has one action.

**Fix order**
1. Decide the minimum needed to start reminders, then make screens 2, 4 and 5 agree on it (finding 1).
2. Use one term for the location and one progress total (findings 2–4).
3. State the selection rule on screen 2 (finding 5).
4. Add notification context on screen 3 (finding 6).
5. Tighten the screen 1 value line, the screen 4 promise, and the button labels (findings 7–9).

**Not checked:** layout, contrast, tap target sizes, and actual behavior. That covers whether Next is enabled with no chips selected, whether Skip really leaves reminders off, and when the OS permission prompt appears. Those need the build or screenshots.
