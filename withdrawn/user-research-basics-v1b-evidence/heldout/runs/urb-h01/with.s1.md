# Plan: validate the pet-insurance add-on in two weeks

**Assumptions:** you have booking and checkout analytics, a support inbox, and a list of past customers you can email. I haven't seen any of them.

## 1. Reframe it with your VP (day 1, 30 minutes)

"Validate with customers" can mean two different things, and research can only answer one of them:

- **Is there a real problem this solves?** Do owners worry about injury or illness during a stay, and what happens today when it occurs? Conversations and existing records can answer this.
- **Will people pay for it at checkout?** Interviews and surveys can't answer this, because people overstate what they'd buy. Only a behavioral signal can, such as a fake door (below).

Agree on the result that would change the plan. For example: "If a fake door gets a take rate of [VP picks threshold], or recent incidents show owners absorbing costs they were upset about, we proceed to scoping. If neither, we don't." Have the VP choose the threshold, and don't invent one yourself.

Also flag **regulation**. Insurance is licensed. You almost certainly need a partner underwriter, and their terms (price, coverage, exclusions) will shape the product more than customer opinion. Ask legal or biz-dev now whether a partner exists. If this is really a "buy vs. partner" question, that's a third track that costs no research budget.

## 2. Mine what you already have (week 1, ~2 days of your time, no designer)

- **Support tickets and chat** for the last 12 months: injuries, vet visits, lost pets, damage, reimbursement requests, "does your guarantee cover…". Tag each one and report counts as "n of N tickets", noting that tickets only come from people who write in.
- **Current policy:** what do you already promise or cover, and what have incidents cost you?
- **Sitter side:** ask a few sitters or community managers what happens when a dog gets hurt. They see incidents you don't.
- **Analytics:** checkout drop-off, average booking value, and repeat-booking rate. Add-on price sensitivity depends on booking size.

This tells you whether the problem exists at all, and it costs nothing.

## 3. Five to eight conversations (week 1–2, 30 minutes each)

- **Who:** owners who completed a booking in the last 60 days. Aim for a mix of first-time and repeat bookers, and include anyone who had an incident. Recruit by email to past customers, offering a booking credit if you can afford one. Say who the sample leaves out: people who didn't book.
- **Who runs them:** you, not the designer. The person who designs the thing is the worst facilitator for it.
- **What to ask:** stories about the last booking, not opinions about insurance.
  - "Walk me through the last time you left your dog with someone."
  - "What was going through your mind the night before?"
  - "Has your dog ever been hurt or sick while you were away? What happened?"
  - "What did you do about vet costs or coverage, if anything?"
  - "Do you have pet insurance now? How did you pick it?"
- **Don't** mention the add-on until the end, and don't ask "would you buy this?"
- Get consent before recording. Stop when new sessions stop changing what you conclude.

## 4. Fake-door test at checkout (build week 1, run week 2)

This is the only piece that measures buying behavior, and it's where the designer's ~6 hours go.

- **Designer (~3 hrs):** one checkout mock with the add-on line, a price, and 2–3 lines of coverage copy. Use placeholder terms that are clearly labeled as such internally.
- **Engineering (~half a day, must be requested now):** show it to a share of checkout sessions. If the customer opts in, show "Coming soon, we'll email you" with no charge.
- **Be honest on the page.** Don't imply coverage exists today.
- **Read it as a lead, not a result.** With no traffic numbers I can't tell you if two weeks is enough. Pick the metric (opt-in rate among sessions that saw it) before launch, and don't stop early because it looks good.

If engineering can't spare the time, fall back to emailing recent bookers a one-question "Would you want this?" It's much weaker, so label it that way.

## 5. What you bring to the planning meeting

A one-page summary with:

1. Decision and the threshold the VP agreed to.
2. Existing evidence: ticket counts as n of N, with the bias noted.
3. Interviews: what owners did and worried about, as "3 of 7", with no percentages.
4. Fake-door result, labeled as a lead if traffic is thin.
5. What's still unknown (pricing, coverage terms, partner) and the cheapest next check.

## Schedule

| When | You | Designer (3 hrs/wk) |
|---|---|---|
| Days 1–2 | VP alignment, request eng + legal input, start ticket review | none |
| Days 3–5 | Finish tickets, send recruit email | Checkout mock |
| Week 2 | Run interviews, launch fake door | Tweak copy, nothing more |
| Days 9–10 | Write the summary | none |

**What a human has to do:** recruit and consent participants, run the sessions, get engineering to ship the fake door, and get a legal read on the insurance side. I can draft the recruit email, the interview guide, or the fake-door copy next if you want.
