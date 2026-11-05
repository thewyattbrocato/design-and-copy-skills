# Reports and alerts

Load when designing the idle status view, deciding which messages an agent sends and how often, writing a concern notice or a morning report, or deciding how to talk about what the agent is worth. Names and numbers are invented; adapt the pattern, then hand the final wording to `ux-microcopy`.

## The status home

People who are not looking still need to be able to look. One place answers, at a glance:

- Is it running or paused (large, unmistakable)?
- When did it last act, and what was that?
- When does it next check or run?
- What is it watching, and how close is that to the limit that makes it act or stop? ("Kiln queue: 5 of 8 slots filled this week.")

Pause is on this view, one tap away. Reading it takes seconds and needs no report. An idle agent with a visible next check looks patient; the same agent with no sign of life looks dead, and people stop trusting it before anything has gone wrong.

When a run is skipped because the agent was paused, the view says so ("Paused Tuesday, so the glaze order was not placed. Order now, or leave it to Thursday's run?") with no tone of reproach.

## Five kinds of message

Each kind is a different promise to the person. Set the bar before writing any text.

| Kind | Send when | Default delivery |
|---|---|---|
| Problem | The agent cannot continue or has hit a cap, and only the person can fix it | Immediately, to the channel they use for urgent things |
| Concern | A reading is heading toward a limit and there is still time to act | Once, early enough to act, with a way to hear more often |
| Completion | Routine work was done | In the digest, not one by one |
| Suggestion | It is very likely to be worth the person's time | Rarely; the promise was "I'll handle it", so every suggestion spends some of that |
| Check-in | Nothing has happened for a while and the person has not looked | Rarely, on a schedule they set, with an easy way to stop |

Rules that follow:

- Each kind has its own off control, and a reply or tap in the message itself can set it.
- A total ceiling per day or week, above which completions fold into the digest and the rest wait. Starting values to test: one digest a day; no more than a few interruptions a week for a healthy agent. If it is interrupting more, it is wrong, not thorough.
- Success after a hard case may be credited ("Fixed the double booking for Friday on your behalf"); routine success is a line in the digest, not a ping.
- A message that only exists to prove the product is working belongs in the status home, not the inbox.
- Alerts about a physical or limited resource arrive with at least the time the person needs to act: well before the last refill, well before a disk is full.

## Writing a concern notice

Bad news should be the end of a trend the person already saw, not a shock. A concern notice is short and answers what the person would otherwise have to open the app to learn:

1. **The drift and the limit.** What is moving, how far, and which limit it is nearing. ("Clay stock is at 3 bags, below your minimum of 5.")
2. **Your options and the fork.** Anything worth doing in the meantime, and what the person will be asked to decide if the limit is passed. ("Order now, or I'll draft an order Thursday for your approval.")
3. **What I am doing.** The current response, plainly. ("Holding the glaze order until clay is sorted.")
4. **When you will hear next.** The exact condition that triggers the next message, plus a control to be updated more often.

Example: "Three days until the supplier's weekly cutoff and the studio's clay is at 3 bags (minimum 5). If it is still below 5 on Thursday at noon I'll draft an order for 12 and ask you to approve it. Until then I'm holding the glaze order. You can order now or skip this week. [Order now] [Skip this week] [Update me daily]"

Events that arrive suddenly skip the concern step and go straight to a problem message.

## The morning report (completion digest)

A total is not a report. A report lets someone check the agent in under a minute and reverse anything they disagree with.

- Lead with the counts by outcome: done, held for you, skipped, uncertain.
- List items, not just totals, ordered by doubt: the lowest-confidence actions first, each with a reason in a phrase ("filed under Packaging because the sender is the cardboard supplier") and its own reverse control.
- Include what it chose not to do and why, because misses are otherwise invisible.
- End with what needs the person, once, with the buttons.
- Collapse the routine; never tuck an exception below it.

Example opener: "Overnight: 31 done, 3 uncertain, 2 held for you, 5 skipped. The 3 uncertain are first, below." Not: "Great job staying on top of things!"

## Talking about value

Report the agent's own worth honestly, including when it is unflattering. Time saved or mistakes caught, measured, corrects the false impression that a few visible errors create; annoyance, not data, decides most switch-offs. If you cannot measure it, say nothing; do not estimate hours saved. A figure the product shows must come from something it counted ("42 items filed this month, 3 you corrected"), and `honest-claims` governs any claim in marketing.

## Sensitive moments

An automatic highlight, memory or anniversary feature can surface the worst day of someone's year. Make such features opt-in, screen for loss, illness or conflict, and let people remove or skip a period before it is celebrated.

## One voice, not many

Many agents each asking for attention is a worse product than one front agent that coordinates them. If several agents exist, one status home and one digest; each agent's name appears on its items, not on its own set of interruptions.
