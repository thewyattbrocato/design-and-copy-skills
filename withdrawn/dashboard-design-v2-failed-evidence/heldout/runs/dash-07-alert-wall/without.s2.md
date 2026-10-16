# Why "brighter red" won't fix it

## The core point

The outage was missed because 11 other tiles were also red or amber that day, so the real problem looked like the rest. That was 12 of 40 tiles, about 30% of the board. Making red brighter makes all 12 brighter, so the real outage stays just as buried.

## An analogy for him

Picture a car dashboard with 40 warning lights, where a dozen are usually lit: low washer fluid, a service reminder, a door ajar. Then the oil-pressure light comes on. Making every light brighter doesn't help the driver spot it. What helps is having few lights, with each one meaning something, and a loud alarm for the truly dangerous ones.

## What to say

> "The dashboard showed the outage. It was red for 25 minutes. The problem is that red has stopped meaning 'drop everything,' because on a normal day plenty of tiles are red or amber. On the outage day, 11 other tiles were also lit up, so the real one blended in. Brighter red makes all of them louder, including the ones that don't matter, so people will tune it out even faster. We need to make red rare and meaningful, and we need the system to tell people instead of waiting for someone to glance at a screen."

## What to do instead

1. **Put a handful of customer-impact tiles at the top.** Examples are payment success rate, checkout speed, and error rate. If those are red, customers are affected. The other ~35 tiles become supporting detail underneath.
2. **Make red mean "act now."** Review each tile's thresholds. Anything that's often red but doesn't need action should be retuned or demoted. The goal is that a red tile is unusual, and it's real when it appears.
3. **Alert people directly for serious problems.** A page or phone alert to the on-call person should fire within a minute or two. Nobody can watch a screen all day, so the 25-minute gap is really a detection-and-notification gap.
4. **Don't rely on color alone.** About 1 in 12 men are red-green colorblind. Use position, size, and labels such as "DOWN" so the critical state stands out without color.
5. **Measure it.** Track time-to-notice for incidents. The target could be under 5 minutes, which gives him a concrete number to hold the team to.

## Before you present

- **Check the 11 tiles.** My argument assumes most of them were non-urgent or chronically noisy. If some were real symptoms of the same outage, the story changes to "the dashboard worked, but nobody was alerted," which still supports points 3 and 5.
- **Bring numbers if you have them.** For example, "tiles are red or amber X% of the time on a normal day" is more persuasive than the analogy.
- **Acknowledge his instinct.** He's right that visibility matters. You can say, "You're right that it needs to stand out, and the way to get there is to make it the only thing that stands out."

I can turn this into a one-page summary or a few slides if that would help.
