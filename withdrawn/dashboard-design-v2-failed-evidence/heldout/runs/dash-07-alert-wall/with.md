**The short version for your director:** the outage wasn't missed because the red wasn't bright enough. It was missed because red had stopped meaning "act now." Brighter red makes that worse.

## The argument

**1. The screen showed 12 problems and gave no way to tell which one was real.**
On the day of the outage, 12 of 40 tiles (the real one plus 11 others) were red or amber. A person looking at the screen saw a dozen alarms and no ranking. Brighter red turns all 12 up equally, so the real one is no easier to spot.

**2. Alarms that fire constantly get ignored.**
This is a well-documented human effect, not a fault in your team. If red often means "probably nothing," people learn to filter it out. Brightness doesn't fix that, and it adds visual noise that speeds up the filtering.

**3. An analogy.**
A car whose dashboard has 11 warning lights always on. Making them brighter doesn't help you notice the one that means the engine is overheating. You need fewer lights that mean something.

**4. What the outage tells us.**
The fact that 11 other tiles were red or amber on a normal day suggests the thresholds are too sensitive. Red is happening too often to be useful. I'm inferring this from your numbers. It's worth checking how often tiles are red on an ordinary day.

## What to do instead

1. **Make red rare.** Re-set each tile's threshold based on what's normal for it recently, so red means "this is unusual." The test is simple: if someone sees red, they should expect to act.
2. **Put the worst things at the top.** Add a strip showing only what is currently breaking, ranked by customer impact (for example, payments failing). Everything healthy collapses into one quiet line like "31 of 40 normal."
3. **Say what's wrong, not just a color.** "Payment success 91%, normally 99%, for 12 min" instead of a red square. Show when it started.
4. **Keep it to two levels.** One "act now" color, one "keep an eye on it." Nothing is permanently green.
5. **Make the big one actively reach people.** The most serious alerts (payments failing) should page someone. A dashboard only helps if someone is looking at it, and nobody can watch 40 tiles all day.
6. **Treat missing data as its own state.** A tile that has stopped updating shouldn't look green.

## How to say it to him

> "The 25-minute delay wasn't because red was too dim. On that day 12 of our 40 tiles were red or amber, so the real outage looked like one of many. If we make red brighter, all 12 get brighter and the real one is still hidden. The fix is to make red rare and meaningful: tune the tiles so red only shows when something is really wrong, put the most serious problem at the top, and have the worst alerts notify someone directly. That way, when something is red, people know it matters."

If he wants a number to anchor on, a good goal is: "On a normal day, we should see almost no red. If we see it, we act."

**Two things worth doing before the meeting:**
- Pull the last month of tile history and count how many tiles were red or amber on a typical day. If it's routinely 5 to 10, that backs up the argument.
- Check whether the outage tile had a paging alert. If not, that's your clearest "what we change" item.

I can draft a one-slide version or sketch the new layout if that would help.
