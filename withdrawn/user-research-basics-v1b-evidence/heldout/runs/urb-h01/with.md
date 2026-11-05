# Plan: validating the pet-insurance add-on in two weeks

**Decision:** Do we put a paid insurance add-on in checkout, or pilot it, or drop it? The planning meeting will make that call. A wrong "build" costs months of engineering plus a partner or regulatory commitment. A wrong "drop" costs the revenue. Because the cost of a wrong "build" is high, research is warranted. It only needs to be small.

**Reframe for your VP:** "Validate with customers" shouldn't mean asking people if they'd buy it. Stated intent for add-ons is unreliable, and 20 people saying "sure" proves little. What you can learn in two weeks is:
1. Is there a real, recurring worry or incident that insurance would address?
2. How do people handle that worry today?
3. Does anyone act on an offer when it costs money?

## Week 1: use what you already have (about 3 days, no designer needed)

Pull these and read for incidents, not opinions:
- **Support tickets and chat logs** mentioning vet bills, injury, illness, escapes, lost dogs, property damage, or "who pays".
- **Dispute and refund records** for the same events.
- **Reviews and post-stay feedback** mentioning accidents or worry.
- **Any existing guarantee or protection policy.** How often is it invoked, and what did it cost?
- **Cancellations and abandoned bookings** where the reason is trust or safety.

Output: a count as "n of N tickets in [period]", with the bias stated (tickets come from people who write in). That gives you how often incidents happen and what they cost, which sets the ceiling on demand. If incidents are rare and cheap, that is a finding in itself.

## Weeks 1–2: 8–10 short conversations (30 minutes each)

You run them, not the designer. The designer of the thing is the worst facilitator of its test.

- **5–6 dog owners** who booked in the last 60 days. Include a mix of first-time and repeat bookers, and at least 1–2 who had an incident or a dispute.
- **3–4 sitters.** They are often the ones who deal with the incident, and they may be liable.
- **Recruit** through an in-app or email invite to recent bookers, with a gift credit as the incentive. Screen on "booked in the last 60 days", and don't mention insurance in the invite. Call it "how you arrange care for your dog".

**Ask about the last real time, not opinions:**
- "Tell me about the last time you left your dog with someone. What did you do before you left?"
- "Has anything gone wrong, or nearly gone wrong, while your dog was in someone else's care? What happened next? Who paid?"
- "How do you cover vet costs generally today?" (Do they already have pet insurance? That matters a lot.)
- Sitters: "Tell me about a time a dog got hurt or sick on your watch. What did you do?"

**Don't ask** "Would you buy insurance?" or "Would this be useful?" Don't mention the idea until the end. If you want a reaction, show a simple checkout mock in the last 5 minutes and ask them to talk through what they'd do at that step. Treat it as a lead, not a result.

**The designer's 6 hours:**
- ~2 hours: take notes in 3–4 sessions, so you aren't writing while you talk.
- ~3 hours: build a one-screen checkout mock, with copy and a price placeholder.
- ~1 hour: help you cluster the notes.

## Optional behavioral check (needs your VP's approval and engineering time)

A "fake door" is a checkout add-on that records interest and then says "coming soon". It tests whether people click when it costs money. I'd only do it if you have enough checkout traffic for a week to produce a meaningful count, and if your team is comfortable with that kind of test. If it doesn't fit in two weeks, say so and put it on the next-steps list.

## Two things interviews can't answer (raise these now)
- **Feasibility.** Selling insurance is regulated. You'd probably need a licensed partner or underwriter, and that determines margin and timeline. Someone should talk to legal and to one or two potential partners this week.
- **Economics.** Attach rate times price minus partner cost minus claims. You can't know these from interviews, but you can bound the incident rate from the tickets.

## What would change the plan
- **Toward building or piloting:** incidents are recurring and costly in the tickets, several owners describe unresolved "who pays" situations, few already have pet insurance, and someone acts on the offer.
- **Toward dropping:** incidents are rare, owners already have coverage or say the sitter or platform should cover it, or the partner economics don't work.
- **Toward a different product:** the worry is real but is really about trust or a platform guarantee, not a paid add-on.

## What to bring to the planning meeting
A one-page note with the incident counts (n of N, with their bias), the interview themes (say "4 of 6 owners", not percentages), what you couldn't learn, and a recommendation: build, pilot, or stop, plus the cheapest next check.

*Assumptions: you have access to support tickets and booking data, and your owners and sitters can be reached through email or in-app messages.*
*A human must recruit the participants, get their consent to record, run the sessions, and ask legal about licensing.*
