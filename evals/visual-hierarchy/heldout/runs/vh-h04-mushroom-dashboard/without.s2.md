**The page gives every room and every number the same visual weight, so nothing tells you where to look.** "Flat" is the right word. A dashboard exists to answer "does anything need me right now?", and yours makes you read 32 numbers to find out. The Room 5 miss is that failure, not a one-off.

**What's wrong, in order of impact**

1. **Alert state is nearly invisible.** A slightly darker orange on one of 32 identical numbers, plus an 11px grey "alert" label, is easy to miss. Grey is the color of "unimportant" and orange is close to your normal text, so the signal reads as noise. Color alone also fails for color-blind users.
2. **Nothing is ranked.** Temperature, humidity, CO2 and days-to-harvest are four equal 28px numbers. But days-to-harvest is planning information, while the other three are live conditions that can ruin a crop. A healthy room and a failing room look nearly the same.
3. **No context for the numbers.** "61%" means nothing without the target range. Is that 5 points low or 25? Is it getting worse? Nobody can tell from a single number.
4. **No time dimension.** Humidity sat at 61% for six hours. The page shows only the current value, so it can't show "out of range for 6h," and a brief blip looks the same as a sustained problem.
5. **Nothing happens outside the page.** Even a well-designed page only works if someone is looking at it. A six-hour miss is also a notification gap.

**What to change first**

Make an out-of-range room impossible to miss. It's a small change and fixes the failure you actually had:

- Give an alerting card a strong state: a thick colored border or left bar, a tinted background, and a clear badge like "Humidity LOW" in 14px or larger bold text, with an icon so it doesn't depend on color alone.
- Make the offending metric the largest thing on the card, and show only the out-of-range metrics in the alert color. Normal metrics should go quieter (smaller, grey-ish).
- Show the target range and duration right under the bad number, e.g. "61% · target 85–95% · low for 6h".
- Sort alerting rooms to the top, or at least pull them into a banner like "1 room needs attention: Room 5."

**Next, in this order**

1. **Demote the healthy state.** Calm cards, with the 28px numbers shrunk, so the alert contrast has room to work.
2. **Add a small sparkline** of the last 24h behind each live metric, with the target band shaded.
3. **Add push alerts** (SMS or Slack) when a metric is out of range for more than about 15 minutes. This is what would have caught Room 5, since nobody stares at a dashboard all day.

If you share the HTML/CSS I can make the alert-state change directly.
