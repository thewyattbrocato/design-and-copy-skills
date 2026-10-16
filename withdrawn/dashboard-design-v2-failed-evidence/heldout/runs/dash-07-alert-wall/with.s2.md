Here's a way to make the case. It's built around one idea he can repeat to others.

## The one-sentence version

"The outage was red for 25 minutes, but 11 other tiles were also red or amber that day. Making red brighter makes all 12 brighter, so it doesn't help anyone tell which one matters."

## The analogy

Think of a car where the check-engine light, the low-washer-fluid light, the tire-pressure light and the door-ajar light all turn on together. Making every light brighter doesn't help. After a few weeks of this, drivers stop reacting to any of them. That's what happened on the dashboard. The outage tile was visible the whole time, but it looked like the other 11.

## Why "brighter red" won't work

1. **The problem is how many tiles are lit, not how bright they are.** On that day, 12 of about 40 tiles (roughly a third) showed a problem. If a third of the screen is always red or amber, people learn to treat red as normal.
2. **Brighter red also raises the volume on the 11 tiles that weren't the outage.** Everything gets louder together, so the real problem is no easier to pick out.
3. **The red tiles don't tell people how serious they are.** "Red" could mean a slow report or a payments outage. The tile doesn't say which, how long it's been red, or what it's affecting.
4. **Nobody is told when something new turns red.** A screen that looks the same at 2:00 and at 2:25 won't get noticed. Dashboards are passive. People have to be looking at them at the right moment.

## What to do instead

Present these in this order, most important first.

1. **Fix the thresholds.** If a third of tiles are red or amber on a normal bad day, the trigger points are set too sensitively. Re-set each one based on what's normal for that metric over recent weeks. Then red should be rare, and when it appears it means "act now." *This is the biggest fix and costs little.*
2. **Put a "needs attention" strip at the top.** It shows only what's broken, ranked by customer impact, with a plain description and a start time. For example: "Payment authorizations failing, 4.2% error rate (limit: 1%), red for 12 min." Healthy tiles collapse into one line, such as "31 of 40 normal."
3. **Make healthy tiles quiet.** Use grey or muted colors for normal. Only problems get color, and only one alert color. Then the eye goes to what's wrong without being told.
4. **Add a page or alert for the serious ones.** For the few things that mean customers can't pay, have the system notify the on-call person directly. A dashboard should be the place you look to investigate, not the thing you depend on to notice.
5. **Review it after each incident.** Ask, "Would the new setup have caught this in under 5 minutes?" Adjust from there.

## How to pitch it to a non-technical director

- **Start with his instinct.** "You're right that people missed it, and visibility is the issue."
- **Then reframe.** "The red was already visible. What was missing was a way to tell which red mattered."
- **Offer a measurable goal.** For example: "Next time, the right person knows within X minutes." I'd leave X for you and him to set. I don't know your current alerting setup or what's realistic.
- **Keep the ask small.** Step 1 (rebase thresholds) and step 2 (the attention strip) probably fit in one sprint. I haven't seen the dashboard, so please check that estimate with your team.

## Two things to verify before the meeting

- **Count the tiles.** Confirm how many were red or amber on a typical day, not just that day. If it's routinely 8 to 12, your case is much stronger because it shows the problem is chronic.
- **Check whether any alerting existed.** If the outage generated no page or notification, say so. It's the most persuasive single fact, because it shows the team was relying on someone happening to glance at a screen.

If it would help, I can turn this into a one-page summary or three slides, or sketch a before-and-after mockup of the dashboard. A visual often persuades non-technical people faster than an argument.
