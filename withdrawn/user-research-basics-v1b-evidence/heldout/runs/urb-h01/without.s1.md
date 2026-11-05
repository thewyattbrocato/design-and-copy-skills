# Recommended plan: validate the pet-insurance add-on in two weeks

**Reframe "validate" first.** In two weeks with no budget, you can't prove the add-on will succeed. You can find out whether there's a real reason to believe it will, and what it would take to find out for sure. Tell your VP that now, and propose that the planning meeting decide whether to run a real test, not whether to build the product.

## Before talking to anyone (days 1–3, about 0 designer hours)

Your own data may answer half the questions:

- **Incident rate.** Pull support tickets and claims from the last 12 months for vet visits, injuries, escapes, property damage, and refund disputes. If incidents are rare or already handled by an existing guarantee or sitter policy, the need is weak. If they're frequent and costly, that's your strongest argument.
- **Booking economics.** Look at the average booking value and the checkout drop-off by step. A $12 add-on on a $40 booking is a different bet than on a $300 holiday stay. Check for segments, such as multi-night stays, puppies, seniors, and first-time bookers.
- **What you already cover.** Check whether you have a platform guarantee or sitter liability coverage. "Insurance" may overlap with it or contradict it.

## Talk to customers (days 3–10, about 5–6 designer hours)

- Talk to **8–10 people who booked in the last 30 days**, plus **3–4 sitters**. Email them or use an in-app prompt, and offer a small credit if you can. Keep calls to 15 minutes.
- Ask about **past behavior, not hypotheticals**:
  - "Tell me about the last time something went wrong with a sitter or your dog while you were away."
  - "What did you do? What did it cost?"
  - "Do you have pet insurance now? Why or why not?"
  - "What did you worry about before booking?"
- Don't ask "Would you buy this?" People say yes and then don't.
- Include some people who have pet insurance and some who don't. Their reasons for buying or skipping it will tell you who the add-on is for.
- Sitters matter because they'll see the add-on too, and they may worry it implies they're risky. They also know where incidents actually happen.

## Run a cheap behavioral test (days 5–12, about 1–2 designer hours)

A **fake-door test** is the best use of your designer's time. Add a simple opt-in line at checkout, for example "Add pet protection for $X." Clicking it shows "Coming soon, want us to notify you?" Run it on a slice of traffic and measure:

- Click rate
- Whether checkout completion drops for the group that sees it

Even a few hundred sessions gives a rough signal. Check with legal first. Make the add-on clearly non-binding, and don't charge anyone or imply coverage exists. If you can't ship it in time, a post-booking email with a link is a weaker fallback.

## Check feasibility in parallel (about 2 hours of your time)

Insurance is regulated, and you almost certainly can't underwrite it yourself. Take a look at embedded-insurance partners, since several sell pet coverage through APIs. Get a rough sense of:

- Who would underwrite it and handle licensing
- The likely price and your revenue share
- The claims experience, since a bad claims process would hurt your brand

If you can't find a partner, the idea is dead regardless of demand.

## What to bring to the planning meeting

A one-pager with:

1. **Incident data:** how often it happens and what it costs.
2. **Customer findings:** the top themes, with quotes.
3. **Fake-door numbers:** click rate and any checkout impact, with honest caveats on sample size.
4. **Feasibility:** partner options and the rough economics.
5. **A recommendation:** go, no-go, or run a larger pilot, with the specific thing you'd test next.

## Time budget

Your designer's roughly 6 hours should go to the interview guide and recruiting copy (1 hr), the fake-door design (1–2 hrs), and sitting in on or synthesizing interviews (3 hrs). If it's tight, drop sitter interviews before you drop the fake-door test. Behavioral data is worth more than more conversations.

## Two traps to avoid

- **Confirmation bias.** The VP wants this to work. Decide before you start what result would make you say no, such as incident rates being negligible or a measurable checkout drop with low interest. Write it down and share it with the VP.
- **Over-reading small numbers.** Ten interviews tell you about reasons and risks, not market size. Say so in the readout.

I can draft the interview guide, the fake-door copy, or the one-pager template if you'd like.
