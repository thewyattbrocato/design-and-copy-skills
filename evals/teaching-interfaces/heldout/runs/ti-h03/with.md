**Build (c), the interactive setup with a live preview of today's conditions.**

**Why (c)**
- **It's the only option where users do the task.** People learn a setting by using it. In (a) and (b) they watch or read about four settings and then have to remember them when they reach the real form. In (c) they build their first alert, so the first alert is already set up when they finish.
- **The preview shows what the settings mean.** Wind direction limit and swell height range are hard to picture in the abstract. If the preview says "with these settings, today at [beach] would [match / not match]," each choice gets immediate feedback in terms the surfer cares about. Neither the video nor the carousel can give that.
- **It fixes the problem where it happens.** You said users get the setup wrong. A guided flow that shows one setting at a time, keeps earlier choices on screen, and previews the result removes much of the confusion. The video and carousel only explain a form that stays as confusing as before.
- **(a) and (b) are weak for this audience.** A 90-second video before the product opens will mostly be skipped, and nobody can remember four settings from it. The carousel is shorter but works the same way: it's a benefits-style explainer shown before the task.

**Risk and how to contain it**
- (c) costs the most to build, and you have no data, so you can't be sure it's the best choice. I'm judging from how people learn interfaces, not from your users.
- To limit the cost, build the preview from data you already have for the beach (swell, wind, timing) and keep the flow short. A sensible version is:
  1. Pick a beach.
  2. Set the swell height range, with the preview showing today's swell.
  3. Set the wind direction limit, with the preview showing today's wind.
  4. Set the time window.
  5. Show the result: "today this alert would [fire / not fire] because [reason]."
- Offer sensible defaults per beach so nobody starts from a blank form. Mark them clearly as suggested, not as the user's own choices.
- Add a visible skip for experienced surfers, and a way to reopen the guide later.

**How to find out if it worked**
Without any data, treat this as a bet and measure it:
- Compare the share of new users who save a first alert, and who still have it active after about a week. That's a better signal than whether they finished the flow.
- Check how many edit or delete that alert in the first few days. Frequent edits suggest they set it up wrong.
- Check whether those users create a second alert on their own, without the guide.

If (c) doesn't beat your current baseline on those measures, the cheapest fallback is a lightweight version of (b), with each card sitting beside its field in the form.

**Assumption:** I'm assuming the app can already get today's conditions for a chosen beach. If it can't, (c) gets much more expensive, and that would change my answer.
