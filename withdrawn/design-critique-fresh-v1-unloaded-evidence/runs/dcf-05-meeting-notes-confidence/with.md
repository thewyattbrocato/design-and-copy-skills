**Top finding:** the screen makes one click send unchecked model guesses to everyone on the call, and you've measured that about 1 in 5 owners are wrong. If errors are independent, which I'm assuming, the chance that at least one of the 6 owners is wrong is 1 − 0.8⁶ ≈ 74%. Most screens will therefore send at least one wrong assignment, and that goes to the whole call, not just the person who was misassigned.

I'm assuming this is high fidelity and that attendees can include people outside your team. I haven't checked contrast or sizes, because I only have your description.

## What I'd change, in order

**1. Gate the send (blocker).**
- Everything is pre-ticked, so the default path is "send it all unreviewed." The button is also the largest element on the screen and sits in the primary position.
- Make items start unreviewed. Make the button say what it does, such as "Send 5 items to 8 people", with the count updating as items are included or excluded.
- Add a confirm step that shows the recipient list, especially if anyone external was on the call.
- Items that haven't been reviewed or have low confidence shouldn't go out silently.
- This is the cheapest fix and removes the worst outcome, so do it first.

**2. Add a source for each item (high).**
- You can't verify an owner you can't trace. Today the only check is remembering the call, an hour later, across 6 items.
- Give each row a timestamp link that plays about 20 seconds, or shows the transcript lines, around where the item came up.
- Highlight who said what. That makes a wrong owner visible in about 5 seconds instead of requiring recall.
- This is the real fix for the 1-in-5 problem, because people can catch errors cheaply.

**3. Make the owner a one-tap control, and don't guess when unsure (high).**
- "Whoever spoke nearest the topic" is a weak signal. It confuses the person who raised something with the person who agreed to do it.
- Show the owner as a tappable chip with the attendee list, not a name that can only be changed through a small "Edit" link.
- When the model has no explicit commitment ("I'll do that"), show "Unassigned – pick owner" instead of a name. An empty field is cheaper than a wrong name sent to the group.
- Editing is the main job on this screen at a 20% error rate, so it shouldn't be the smallest thing in each row.

**4. Fix the checkbox and the pill (medium).**
- A ticked checkbox in a task list normally means "done". Here it seems to mean "include in the send", which a reader will misread. Use separate controls, or use an "Include" toggle with a clear label.
- "87% sure" doesn't say what it's sure of: the task, the owner, or both? It's also a grey pill, so 54% and 87% look almost the same.
- Replace the number with a state. Put low-confidence items at the top, unticked, with "Check owner" highlighted. Only show the number if you've checked that it's calibrated against your test results. People will trust it more than it deserves if it isn't.

**5. Source the summary (medium).**
- Five lines with no references can't be checked, and it sits above the part people need to act on. Link each sentence to a timestamp, or shorten it to 2–3 lines.
- This is lower priority because the summary isn't being sent out as an assignment.

## What to keep
- **The list of 6 rows.** It's scannable and has a consistent structure of task, owner and confidence.
- **Showing uncertainty at all.** The instinct is right. It just needs to drive behavior (sorting and defaults) instead of being a small label.
- **One clear primary action.** The screen has a clear end goal, so keep that. Just make it earn the click.
- **An Edit path on every row.** Keep it, but make it the main interaction.

## How to know it worked
Track the share of sent owners that get changed afterward, and the share of sends where users edited or checked at least one item first. Run the revised screen with 3–5 people on real recent calls and watch whether they catch the wrong owners before sending.
