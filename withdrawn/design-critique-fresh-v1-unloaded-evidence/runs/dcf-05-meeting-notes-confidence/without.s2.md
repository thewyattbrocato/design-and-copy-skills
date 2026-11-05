**Short version:** the screen asks for trust, gives no way to check, and then publishes the result to everyone. With a 20% owner error rate across 6 items, about 74% of screens (1 − 0.8⁶) will contain at least one wrong owner. A wrong owner means a public, mistaken assignment, not just a typo. I'm working from your description, not the live screen.

## Order of changes

**1. Stop the damage at the send step (do first, it's cheap)**
- Untick the checkboxes by default. A pre-ticked box means "approved" when nobody has reviewed anything. Make ticking the act of confirming.
- Replace "Send to everyone on the call" with something that shows what will go out, such as "Send 4 confirmed items to 7 people". Disable it, or make it secondary, until at least one item is confirmed.
- Consider a different default audience. The meeting organizer, or each person receiving only their own items, limits how far a wrong owner spreads.
- Show a preview before the send. Check whether "everyone on the call" includes external guests who shouldn't get it.

**2. Add provenance to every item (biggest trust fix)**
- Give each row a "Source" link that opens the transcript snippet around that moment, with a timestamp and audio playback.
- Highlight who said what. For owner errors, this is how a user confirms or corrects in about 3 seconds.
- Without this, users either rubber-stamp everything or distrust all of it. Both are bad.

**3. Treat owner as the uncertain field it is**
- "Who spoke nearest the topic" is a weak proxy for who committed to the task. Prefer explicit signals ("I'll take that", "can you do X?" followed by "sure").
- Where there's no explicit commitment, show the owner as "Suggested: Priya" or leave it blank. An empty owner is much better than a confidently wrong one.
- Make the owner an inline tap-to-change control, not something buried behind a small "Edit" link. Owner is your most frequent correction, so it should be the easiest one to make.

**4. Fix the confidence pill**
- It's ambiguous. It could mean confidence in the task, the owner, or the wording. Put confidence on the owner specifically, since that's where you fail.
- Grey, small, and numeric ("87% sure") gets ignored. It's also probably miscalibrated. Check whether "87%" really means 87% right on your test data.
- Use it to change behavior, not decorate. Low-confidence items should be visually flagged and sorted to the top for review, and never pre-selected. A 54% item shouldn't look like the same kind of row as an 87% one.

**5. Source the summary**
- Link each summary sentence to its moment in the call, or cut the summary to what you can link. It's lower priority because people can skim it, but an unsourced paragraph that gets sent out carries the same risk.

**6. Close the loop (after the above)**
- Log every owner edit as a labeled error. It's free evaluation data, and it tells you whether the 1-in-5 rate is falling.
- Improve the owner-assignment method itself. Better UI makes errors cheaper, but fewer errors is the real fix.

## Why this order
Steps 1–3 make a wrong owner something the user catches before it ships. Step 4 helps them know where to look. Steps 5–6 improve quality and measurement. If you can only do one thing this sprint, untick the boxes and change the send button.

One thing worth testing: how often users fix wrong owners today, as opposed to sending as-is. If they rarely edit, that's a stronger argument for steps 1 and 2 than the 20% figure alone.
