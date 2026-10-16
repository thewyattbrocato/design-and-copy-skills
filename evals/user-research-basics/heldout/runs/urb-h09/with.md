**Structure: lead with the decision, rank by severity × task centrality, and give every item an owner-sized next step.**

**Slide 1: Headline (one sentence)**
"In a 5-person test, people could not reliably complete the core task of choosing seats and paying. Seat selection is the top fix. It blocked a screen reader user entirely and led two people to buy the wrong deck."

**Slide 2: Priority table**

| # | Issue | Task | Hit | Severity | What happened |
|---|---|---|---|---|---|
| 1 | Seat picker: availability unclear | Choose seats | 4 of 5 | Blocks (2 bought the wrong deck) | Couldn't tell which seats were free |
| 2 | Seat picker with a screen reader | Choose seats | 1 of 1 screen reader user | Blocks | Couldn't complete selection |
| 3 | Card entry error | Pay | 1 of 5 | Blocks (abandoned) | Error on card entry |
| 4 | Promo code field missed | Pay | 3 of 5 | Slows or costs revenue | 1 of those 3 said they'd have used a code |
| 5 | Terminal map link missed | Find the terminal | 2 of 5 (both first-time visitors) | Slows | Didn't see the link |
| 6 | Date picker | Choose date | 1 of 5 | Annoys | Picked the wrong month, noticed, fixed it |
| 7 | Home screen colors | n/a | 2 of 5 | Opinion, not a finding | Called them "a bit dull" |

Order by severity first, then by how central the task is. Seats and payment come before anything peripheral.

**Slide 3: What worked**
All 5 of 5 found their ticket on the confirmation page. Say so briefly. It shows the team what to protect, and it makes the problems look like a measured result and not a complaint list.

**Then one slide per top 3–4 issues**
Each gets a screenshot or short clip, a one-line description of what happened, the n of N, and a proposed owner and next step. Clips of the two wrong-deck purchases will persuade more than any table.

**Slide: Decisions needed Monday**
Ask for specific commitments, for example:
- Assign an owner for the seat picker redesign, covering availability states and screen reader support.
- Investigate the card entry error. The test doesn't say whether it's a bug or a usability problem, so engineering should check logs before anyone redesigns it.
- Agree to retest with new participants after the fixes.

**Framing choices**
- **Use "4 of 5," not "80%."** With 5 people, percentages overstate certainty. Say plainly that this is a small qualitative test. It shows where people get stuck, not how often it happens.
- **Treat the screen reader result as its own item.** It's one person, but a complete failure on a core task is serious regardless of sample size. Don't fold it into the 4 of 5. These are probably related problems, but the test doesn't show that.
- **Flag single-person items as leads.** That covers the payment error and the date picker. Check analytics or error logs for the payment error before investing.
- **Don't draw conclusions from the first-time-visitor pattern on the map link.** Both misses were first-timers, which is worth noting. But 2 people is a hint, not a segment finding.
- **Keep the color comments as a footnote.** Two people calling the colors "a bit dull" is a preference, not a usability problem. Putting it on the main list would dilute the real issues.
- **Keep findings and solutions separate.** The findings slides say what happened. Proposed fixes go in the "Decisions" slide so people can disagree with a fix without disputing the finding.

**Caveats to state on a closing slide:** the sample was 5 people, and I don't know how they were recruited. Say who the sample leaves out, such as repeat riders. Name what's still unknown (for example, whether the card error is reproducible) and the cheapest next check.

If you share the screenshots or clips you have, I can draft the slide text.
