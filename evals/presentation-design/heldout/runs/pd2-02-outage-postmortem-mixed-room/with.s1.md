**Plan:** 25 minutes is about 20 minutes of talk plus 5 for questions, so 9 content slides. The takeaway is that a routine config change took checkout down for 2h 40m because nothing checked it, and two engineers for one quarter close that gap. The action you want is for the execs to approve the headcount and for engineers to adopt the new change checks.

I put the verdict and ask first because the execs need them early. Engineers get the timeline and root cause in the middle, with enough detail to trust the fix. The deck doesn't follow the order the incident happened in.

## Slides

| # | Title (the claim) | On screen | Time |
|---|---|---|---|
| 1 | **One config change took checkout down for 2h 40m. Two engineers for one quarter stops it recurring.** | Big "2h 40m", with "Saturday" beneath. Speak the need, the verdict and the ask. Preview the labels by voice: what happened, why, the fix, the cost. | 2 min |
| 2 | **The outage cost us [X orders / $Y revenue] and [Z] support contacts** | Three numbers. Use real figures from finance, and leave a visible placeholder until you have them. | 1.5 min |
| 3 | **We took [A] minutes to notice and [B] to find the cause. Most of the 2h 40m was diagnosis.** | One horizontal timeline with 4–5 markers: change deployed, first failure, alert or report, cause found, fix live. Shade the long gaps. | 3 min |
| 4 | **A pool-size change in the payment service starved checkout of connections** | One diagram: checkout → payment service → pool, with the changed value circled (old → new). Only the mechanism goes here. | 3 min |
| 5 | **The change passed every step we have, because none of them test it** | Three gaps in three short lines: no validation of config values, no staged rollout, no alert on pool exhaustion. Use only gaps your review confirmed. | 2.5 min |
| 6 | **The fix closes those three gaps for every service, not only payments** | Three columns matching slide 5: validate, roll out gradually, alert early. One line each. | 3 min |
| 7 | **This failure class won't recur. Other failures still can.** | Two short lists: what the fix rules out, and what it doesn't. Being straight about the second list is what makes the first credible. | 2 min |
| 8 | **The fix costs 2 engineers for 1 quarter. One more outage like this costs [X].** | Two numbers side by side. Leave the cost of the engineers as a placeholder unless finance has a figure. | 2 min |
| 9 | **Decision needed: approve 2 engineers for Q[N]. Owner [name], first milestone [date].** | The ask, owner, date and one-line success measure. Leave this up during questions. | 1 min |

That's about 20 minutes, leaving 5 for questions.

## Backup slides (after the end, for Q&A)
- Full minute-by-minute timeline, which engineers will ask for.
- The config diff and the exact failure mechanism.
- Alternatives considered: a cheaper partial fix, and why you rejected it.
- Exposure in other services with the same pattern.
- What the engineers would otherwise be working on, which is the CFO's and VP of product's opportunity-cost question.

## Hard questions to prepare for
- **CEO:** "Can you promise this won't happen again?" Slide 7 is your answer.
- **CFO:** "Why two engineers and a full quarter? Could it be half that?" Use the alternatives backup slide.
- **VP of product:** "What does this delay?" Know the answer before Thursday.
- **Engineers:** "Why did detection take so long?" Slide 3 and the timeline backup cover it.

## If time shrinks
Cut slide 2 first and say the impact in one sentence. Then fold slide 7 into slide 6.

## Notes
- I haven't invented any numbers. Everything in brackets needs a real figure: impact, the detection and diagnosis gaps, and the cost comparison. Slides 3 and 8 depend on those figures most.
- I assumed "fix" means validation, staged rollout and alerting. If your actual proposal differs, slides 5–7 need to change, but the structure holds.
