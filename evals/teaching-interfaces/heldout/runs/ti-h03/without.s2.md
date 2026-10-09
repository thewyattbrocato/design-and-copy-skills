**Recommendation: (c), the interactive setup with a live preview.**

**Why:**

1. **It matches the problem.** Users get the settings wrong, and the settings are hard to judge in the abstract. Nobody knows whether "3–5 ft" or "offshore wind under 10 knots" is a good threshold for their beach. A live preview of today's conditions turns those abstract numbers into something concrete. They can see "this would fire today" or "this would never fire" and fix it right there. The video and the carousel can only explain what the settings mean. They can't show whether a user's choices fit their spot.

2. **It teaches by doing.** Users finish with a working alert instead of having to remember what they watched. The video and carousel put a gap between learning and doing, and people forget or skip passive content. A 90-second video on first launch is especially likely to get skipped by someone who just wants to open the app.

3. **It fixes the failure directly.** The video and carousel only help if people watch or swipe and then apply what they saw. The interactive flow guides each choice as it's made, so a wrong setup is caught while the user is making it.

**Tradeoffs:**
- It costs the most to build. It needs the conditions data wired into the setup flow and some state handling. Of the three options it has the highest risk of eating the sprint.
- If the live preview is too hard to finish in time, a cut-down version still works. It would be a step-by-step flow with a simple "here's what today looks like at this spot" readout, and you could add polish later.
- I'm reasoning from how onboarding generally works, not from your data. You said you have none, so treat this as a reasoned bet, not a proven answer.

**Make the bet testable.** Before launch, define the success metric. Good candidates are the share of new users who complete a first alert and the share whose alert fires within their first week. Also track how many edit or delete that alert within a few days, because that's a signal they set it up wrong. Then you'll have data for the next sprint, whichever way this turns out.

If engineering says (c) can't be done in one sprint even in cut-down form, pick (b) over (a). A carousel is skimmable and quick to build, and users can come back to it. A video takes more effort to produce and is the easiest option to skip.
