# Lay it out by severity, not by screen

If you walk through the app in flow order, the seat picker, the screen reader failure and the payment error get the same airtime as "colors felt dull." Sort by what happened to the user instead, and end with specific asks.

## Suggested structure (about 6 slides)

**1. Headline and bottom line (one slide)**
Something like: "Users can find and pay for tickets, but the seat picker is failing them, and it's completely unusable with a screen reader. Three things need fixes before the next release."
Include the method in one line: 5 moderated participants, task-based, last week.

**2. Fix now: users failed or got the wrong outcome**
- **Seat picker (grouped with the accessibility finding):** 4 of 5 couldn't tell which seats were available, and 2 bought the wrong deck. The screen reader participant couldn't complete selection at all. These are probably the same component, so present them as one problem with two symptoms.
- **Payment:** 1 of 5 hit a card-entry error and abandoned. Even at n=1, a hard error is worth engineering time because it may be reproducible. The ask is to check logs and reproduce it, not to redesign anything.

**3. Fix soon: missed features and lost opportunity**
- **Promo code field:** 3 of 5 didn't see it, and 1 of those said they would have used one.
- **Terminal map link:** 2 of 5 missed it, both first-time visitors. Frame it as a problem for a specific segment.

**4. Watch or deprioritize**
- **Date picker:** 1 of 5 chose the wrong month, noticed, and fixed it. The design recovered from the error, so log it and move on.
- **Home screen colors:** 2 of 5 called them "a bit dull." That's an opinion, not a behavior, so it doesn't belong in the action list.

**5. What's working**
The confirmation page was a 5 of 5. Keep this short, since it tells the team what not to touch and gives the meeting a positive note.

**6. Asks, owners, and dates**
This is the slide that gets things done. Use a table: finding, proposed action, owner, decision needed by. For example, "Design: show available and unavailable seats distinctly, with non-color cues, and make the picker screen-reader navigable. Eng: reproduce the card-entry error."

## Tips for getting people to act

- **Show counts, not percentages.** "4 of 5" is honest at this sample size, and "80%" invites someone to challenge the methodology.
- **Put a severity label on every finding** (blocker, major, minor) and define the labels once. It heads off arguments over priority.
- **Use a short quote or a screen clip for the top two issues.** Seeing someone buy the wrong deck persuades more than a bullet does.
- **Be upfront about limits.** Five people is enough to find usability problems but not to size them. Say that once, then move on.
- **Treat the accessibility failure as a blocker, not a nice-to-have.** If your company has accessibility commitments or legal exposure, say so explicitly. It's also the finding most likely to be deprioritized if you don't.
- **Send the one-page summary ahead of time** so Monday's meeting is for decisions, not first reads.

I can draft the slide text or the asks table if you'd like. If so, tell me who owns design and engineering for these areas so I can fill in the owner column.
