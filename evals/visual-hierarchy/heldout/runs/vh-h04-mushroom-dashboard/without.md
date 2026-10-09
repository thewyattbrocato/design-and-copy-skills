Your co-founder is right, but "flat" understates it. The page gives every piece of information the same visual weight, so nothing signals which room needs attention. That's why Room 5 sat at 61% for six hours.

**What's wrong**

1. **State isn't the loudest thing on the card.** Normal and alarming look almost identical. The alert is a small shift in orange hue, which is easy to miss and invisible to anyone with color-vision differences. The "alert" label is 11px grey, the lowest-emphasis text on the card.
2. **Everything has equal weight.** There are 8 cards × 4 identical 28px numbers, so 32 things shout equally. Days to harvest is planning info, not a live-condition reading, but it's styled the same as humidity.
3. **The alert doesn't say what's wrong.** It doesn't say which metric, what the target is, or how long it's been out of range. A 61% reading means nothing without knowing the range is, say, 85–95%.
4. **A page is passive.** Even a well-designed page only works if someone is looking at it. It can't catch a six-hour problem on its own.

**What to change first**

Make out-of-range the dominant visual state, and make it say something specific:

- Give an alerting card a strong treatment: a saturated border or left bar, a tinted background, and an icon plus a word. Don't rely on color alone.
- Put the message on the card, e.g. "Humidity 61%, low (target 85–95%), 6 h".
- Emphasize only the offending metric. Keep the other three at normal weight.
- Quiet the healthy cards: smaller numbers, lighter weight, less contrast. Then alerts stand out by contrast rather than by shouting.
- Add a summary strip at the top ("1 room needs attention: Room 5") and sort alerting rooms first.

**Then**

- Show the target range and a small trend line or "out of range for X h" on each metric.
- Send a push alert (SMS, Slack or email) when a reading is out of range for more than N minutes. For unattended grow rooms, this matters more than any visual fix.

One thing to verify: did the page flag Room 5 at all? If 61% was outside your threshold and the card still looked normal, you have a threshold bug as well as a design problem. If it did show the orange state, that confirms the design is too subtle. I haven't seen the page or its code, so I can't tell which from here. If you share the file, I can make these changes.
