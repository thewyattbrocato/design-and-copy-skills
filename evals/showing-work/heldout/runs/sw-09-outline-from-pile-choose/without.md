# Gridwalk offline mode: case study plan

## The story
Inspectors in the field couldn't tell what had saved and what hadn't, so a tiny grey icon was replaced with a persistent banner and per-item sync states. In testing, comprehension went from 1 of 5 to 4 of 5.

That before/after comprehension result is your strongest evidence. Build everything around it.

## Lead with (top of the page, in this order)
1. **Before/after screenshots**, side by side. The grey icon versus the banner and per-item states is visible in two seconds.
2. **The usability result (1/5 to 4/5)**, stated next to the screenshots.
3. **The problem in one sentence, grounded in a human consequence.** Use an inspector quote from your interviews, such as what happens when they don't know if their work saved. Pick the most concrete one.

A hiring manager who stops reading after the first screen should still get the problem, the change, and the outcome.

## Support (the body)
- **Interview insights.** Distill the 6 interviews into 2–3 findings that each drove a design decision. Show the finding, a short quote, and the resulting decision. Don't show the raw notes.
- **Design evolution.** Pick 6–8 frames from the 40 that show real decision points, such as v1 to v2 to v3 and what changed and why. Put a short rationale on each, including at least one idea you tried and abandoned.
- **The sync conflict challenge.** Use the engineer's comment as a short attributed quote, then explain how you designed for it (how conflicts are surfaced and resolved). This shows cross-functional work and handling of hard edge cases. It only works if your design addresses conflicts. If it doesn't, say what you did instead, and don't imply you solved it.
- **Competitor teardown.** Reduce it to one small section: what the 2 apps did, and what you borrowed or deliberately did differently. Keep it to a few lines or a single comparison graphic.
- **Test method.** Two or three sentences covering who the participants were, what task you gave them, and what "understood" meant.

## Drop
- **Most of the 40 frames.** Volume reads as an inability to edit. Link a Figma file only if you want to offer depth.
- **Raw interview notes and the full Slack thread.** Pull one quote from each.
- **Competitor detail beyond the headline takeaways.**
- **Process-for-its-own-sake narration**, like "then I did a workshop."

## Outline
1. **Title and summary.** One line on the project, your role, team, timeline, and the outcome stat.
2. **Problem.** Who the inspectors are, the situation (patchy connectivity, work that can be lost), and the before screenshot.
3. **What I learned.** Two or three insights from the interviews with quotes, and one line on the competitor gap.
4. **Design goals.** Two or three principles, such as "sync status must be visible without being looked for."
5. **Solution.** The after screenshot, annotated: banner, per-item states, and the conflict handling.
6. **Iteration.** Selected frames across the 3 versions, with what changed and why.
7. **The hard part: sync conflicts.** The engineering constraint, the tradeoff, and how you resolved it.
8. **Results.** The 1/5 to 4/5 finding and the test method.
9. **Reflection and next steps.** What you'd measure next and what you'd do differently.

## Handling the weak spots
- **n=5 and no business metrics.** Don't hide either one, and don't inflate them. Write something like: "In a small usability test (5 participants), comprehension of sync state rose from 1 to 4." Then, in next steps, name the metrics you'd track, such as support tickets about lost data, duplicate inspections, or sync-error rates. Hiring managers read a candidate who knows what the evidence does and doesn't show as more credible.
- **Attribution.** Be precise about what you owned versus what the team did, especially on the sync logic.

If you tell me your role on the project and how the design handles conflicts, I can draft the copy for sections 2, 5, and 7.
