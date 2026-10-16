# Why "brighter red" won't fix it

## The core argument

**Brightness wasn't the problem. Red had stopped meaning anything.**

On the day of the outage, 12 of the 40 tiles (30%) were red or amber. If a third of the board is always in some warning state, people learn to tune it out, and the one tile that matters looks like the others. Making red brighter makes all 12 brighter, so the noise gets louder and the signal stays buried.

## An analogy he'll recognize

Picture a car with 40 warning lights, and 11 of them are always on. You'd stop looking at the dashboard. Making the engine light brighter doesn't help, because you've already learned the lights don't tell you anything. The fix is to turn off the false alarms so the real one stands out.

A smoke alarm that chirps every day works the same way. People take the battery out.

## A second problem: a dashboard only works if someone is looking

Even a perfect dashboard can't help if nobody is watching it at that moment. A 25-minute delay suggests that was part of what happened. Important problems should come to us, by paging or calling the on-call person, instead of waiting for someone to glance at a screen.

## What we should do instead

1. **Cut the board down to what customers feel.** Keep a handful of top-level tiles, such as payment success rate, payment speed, and error rate. The other ~35 tiles become supporting detail for diagnosing a problem, not things people monitor.
2. **Make red mean "act now."** Go through the tiles that were red or amber that day. Either fix the cause, change the threshold, or remove the tile. If a tile is red and nobody needs to do anything, it's hurting us.
3. **Automatically alert a person for the critical few.** A serious problem should page the on-call engineer within minutes, whether or not anyone is looking at the screen.
4. **Measure detection time.** Track how long it takes from "something broke" to "someone is working on it." Last month it was 25 minutes. Set a target (for example, under 5) and report on it.

## A short version to say out loud

> "Last month the problem was on screen for 25 minutes and nobody reacted. That wasn't because the red wasn't bright enough. It's because 11 other tiles were also red or amber that day, so red looks normal. If we brighten it, everything gets brighter and we're back where we started. What fixes it is fewer tiles, red that always means 'act now,' and an automatic page to the on-call engineer when a customer-facing tile goes red. That should bring detection from 25 minutes to a few."

## Before the conversation

- **Find out what the 11 other tiles were.** If they were side effects of the outage, you can say "the board lit up everywhere and gave no hint of where the problem started." If they were unrelated chronic noise, you can say "this is the everyday state of the board." Both support your case, but you should know which one you're telling.
- **Bring a number for the cost.** Even a rough estimate of failed payments or revenue lost during those 25 minutes will land better than any analogy.
- **Acknowledge his instinct.** "Making the important thing more visible is the right goal" is true. You're only saying that brightness can't do it when everything else is shouting too.

I can turn this into a one-page summary or a few slides, or draft a mock "before and after" of the dashboard, if you'd like.
