Here's a way to frame it for your director, plus a script you can use.

## The core message (one sentence)

**"The outage wasn't invisible because the red was too dim. It was invisible because 12 tiles were red or amber that day, and a screen where a lot of things are red can't tell you which one matters."**

## An analogy he'll get

A car where the dashboard warning lights are on most of the time. The "check engine" light comes on, you've seen it so often that you ignore it, and then the engine fails. A brighter light doesn't help. If anything it gets tuned out faster. The fix is to make the light come on only when something really needs you.

Another option is a smoke alarm that goes off every time you make toast. People take the battery out, and then it doesn't ring when there's a real fire.

## Why "brighter red" fails

1. **The problem is how many tiles are red, not how bright any one is.** On the outage day, 1 real outage was shown next to 11 other red or amber tiles. If you make red brighter, all 12 get brighter together. The real one still looks like the others.
2. **It makes the noise louder too.** Brighter red on a screen where red is common means more glare and faster fatigue. People learn to ignore it sooner.
3. **Color can't say how serious something is.** "Red" currently covers both "a minor metric drifted" and "customers can't pay." The dashboard gives the viewer no way to tell them apart.
4. **The evidence is already in your incident.** The tile was red for 25 minutes. It was visible the whole time. Nobody acted because nothing set it apart.

## What to do instead (three changes, in order)

1. **Fix the thresholds (the biggest lever).** Look at those 11 other tiles. If they are often red or amber on normal days, the trigger points are set wrong. They should be reset against what normal looks like recently, so red means "this needs someone now" and is rare. *A good test: if a quarter of tiles are red most days, the thresholds are the problem, not the team.*
2. **Put problems first and make healthy tiles quiet.** Instead of 40 equal tiles, show a short ranked "Needs attention" strip at the top. Each entry says what's wrong, against what limit, and since when (for example, "Payment success rate 91%, target 99%, 25 min"). Collapse the healthy ones into a single line like "34 of 40 within target," and drop the permanent green.
3. **Page a person for the serious few.** A dashboard only works if someone is looking at it. For the handful of tiles tied to customer-facing payment failure, send an automatic alert to the on-call person. Don't rely on someone noticing a tile.

Optionally, add a "started at" time on every alert, and show a "stale data" state so a broken feed isn't mistaken for green.

## Suggested script for the conversation

> "You're right that we need to notice problems faster. I looked at the outage day, and the tile was red the whole 25 minutes, but 11 other tiles were also red or amber, so it looked like everything else. If we make red brighter, all 12 get brighter and we're still in the same spot. What I'd propose is that we reset what counts as red so it's rare, put the few real problems at the top with how long they've been going, and send an automatic alert to on-call for payment-critical failures. That way a real outage stands out by being the only thing that's red, rather than by being a bit redder."

## Prepare for his likely pushback

- **"Can't we just do both?"** Yes, once red is rare, a stronger color is fine. It just won't solve the problem alone.
- **"Won't fewer reds hide real problems?"** The risk is the opposite. Right now real problems are hidden among false ones. Rarer red means each one gets looked at.
- **"How long will it take?"** I can't say without knowing your tooling. The threshold review is likely the fastest win, so I'd start there.

## Things I'd want to verify before the meeting

I only have the numbers you gave me. It would strengthen your case to check:
- On a typical day, how many tiles are red or amber? If it's often 8 to 12, that supports the point that thresholds are off.
- Of the 11 other tiles that day, how many were truly urgent? Probably none, or few.
- Was an alert or page sent for the outage, or did it depend on someone watching the screen?

If you can share the tile list and typical thresholds, I can help work out which to recalibrate and draft a one-page version for him.
