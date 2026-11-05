**The biggest problem is the bottom of the screen, not the owner accuracy.** Everything is pre-ticked, and one large blue button sends it to the whole call. Your own testing says each item has about a 1-in-5 chance of the wrong owner. If errors are independent (my assumption), a 6-item list has at least one wrong owner about 74% of the time (1 − 0.8⁶). So the default path publicly assigns work to the wrong person in roughly three out of four meetings. Fixing that comes first.

Assumptions: the summary also goes out with the button, and I'm judging from your description only. I haven't checked contrast, tap-target sizes or real copy.

## Fix order

**1. Make sending a reviewed act, not a default (blocker).**
- Start items unticked, or in an explicit "needs review" state.
- Label the button with a count that updates: "Send 4 items". Disable it at 0.
- A ticked box normally means "done". Here it means "include" or "approved", and the screen doesn't say which. Use different wording or a different control.
- Better still, send each person only their own items instead of broadcasting. A wrong owner then reaches one person and the true owner never hears about it, but nobody else sees a public mistake.
- The first send to a group should show who will receive it.

**2. Add a source for every item (blocker for trust).**
- Right now a person who doubts "Priya: update the pricing deck" has to recall the call from memory, or replay an hour of audio.
- Give each row a "from 23:41" link that opens the transcript lines around it, with a play button.
- This is the cheapest way to cut the wrong-owner problem in practice. It makes a 5-second check possible.
- Do the same for the summary: each sentence links to its moment in the call. An unsourced 5-line summary going to everyone is a smaller version of the same risk.

**3. Stop presenting a guessed owner as a fact (major).**
- The owner is picked by who "spoke nearest the topic". That is a weak signal, and the name looks as firm as the task text.
- Below a threshold, leave the owner blank ("Who?") rather than guess. A blank slot gets filled in. A wrong name gets sent.
- Make the owner a one-tap dropdown on the row. Don't hide the fix behind a separate edit step.
- Add a visible "Unassigned" option.

**4. Fix or remove the confidence pill (major).**
- "87% sure" is unlabeled. It could mean the task, the owner or the whole row, and the wrong-owner error is the one you know about.
- A small grey pill is easy to skip, and 54% is close to a coin flip. Nothing on screen tells the reader what to do about it.
- Check your test data. If the score doesn't predict which owners were wrong, drop the number.
- If it does predict them, replace the percentage with a state that triggers action, such as "Check owner" on low-confidence rows, sorted or highlighted at the top.

**5. Make editing proportionate (moderate).**
- If a fifth of rows need correcting, "Edit" shouldn't be a small link at the end of the row.
- Let people tap the text or the owner to edit in place. Add "Add item" and "Remove" too.
- Missed action items are invisible on this screen. Offer a way to add one, and consider showing a "Not sure about these" group for lower-confidence candidates.

## Keep

- **One owner per row, next to the task.** That is the right shape for follow-up, and it makes errors easy to spot once a source is attached.
- **Showing uncertainty at all.** The instinct is right. It needs a clearer meaning and an action attached.
- **One primary action, shown right after the call.** People remember the call best at that moment, so it's the right time to review. The single button just needs to come after review.

## Cheapest way to check this
Watch 3 to 5 people from real calls go through the screen. Count how many send without noticing a wrong owner. That number tells you how fast to ship fix 1, and fix 1 is small enough to ship first either way.
