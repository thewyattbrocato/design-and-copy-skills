**I'd do none of the three as written. I'd give a small one-time free allowance (about 50 to 100 pages, no card, no monthly reset) and put the $10 starter plan behind it.**

**Why not the other three**

- **500 pages a month forever:** This is the riskiest option. 500 pages costs you $10 per user per month, and it recurs. Your worst case is $20k a month if all 2,000 signups maxed out, and the cost keeps growing as free users pile up. Developers who run a side project on the free tier also tend to stay free.
- **14-day trial:** It's safer, but the time limit doesn't cap spend, because one user can push thousands of pages through in a day. It also doesn't fit your pattern, since most people try it for a day and leave. A trial clock adds nothing for them.
- **$10 plan with nothing free:** Developers want to see the extraction work on their own invoices before paying. Requiring a card up front will cut signups and conversions a lot. Also, 500 pages costs you $10, so a $10 plan has to include fewer pages (around 200 to 250) to leave any margin.

**Why a one-time allowance works**

- **Spend is capped per signup:** At 100 pages, the most any signup can cost is $2, so the worst case is about $4k a month if all 2,000 max out. Almost none will. If 90% use about 10 pages and 10% use the full 100, you spend roughly $400 a month. At 50 pages the worst case is $2k and the realistic figure is about $250.
- **It's enough to evaluate:** 50 to 100 pages is plenty to test a few real invoices. Someone who needs more than that is a likely buyer.
- **It scales with signups:** The cost depends on how many people sign up, not on how long they stay. Cost per signup is fixed, so you can model it.

**Guardrails**

- Require email verification, and consider blocking disposable domains, so people can't farm credits with repeat signups.
- Apply a rate limit to the free allowance so a script can't burn it in seconds.
- Show a "pages remaining" counter and a clear upgrade prompt when it runs low.
- Price the starter plan so it carries margin. For example, $10 for 250 pages ($5 cost) plus per-page overage.
- Track what share of free allowances get used and how many convert. If conversion is strong and spend is low, raise the allowance. If it's weak, lower it. Both are easy to change, whereas a "forever" tier is hard to take back.

I'm guessing at your usage split, so check it against your real signup data if you have it. The 10 pages per light user and 10% heavy-user shares above are my assumptions.
