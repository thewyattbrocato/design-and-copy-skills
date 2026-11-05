**Recommendation: option B, but as a capped credit instead of a time-limited trial. Drop the forever free tier.**

Give each signup a one-time credit of 50 pages, no card required, expiring after 14 days. Put the $10 starter plan in place from day one.

**The arithmetic (assumed inputs: 2,000 signups/month, $0.02/page):**

| Option | Cost exposure | Why |
|---|---|---|
| A. 500 free pages/month forever | Up to $10/user/month, forever | Free users never leave the cost base. If 5% of signups (100/month) keep using even 100 pages/month ($2 each), the bill grows by about $200/month every month. |
| B as stated: 14-day trial, no page cap | Unbounded per signup | A developer who runs a test batch of 500 pages spends $10 in one day. |
| **B as credit: 50 pages, 14 days** | Max $1/signup; ceiling $2,000/month if every signup used all 50 | Most signups explore for a day, so expected use is far below the ceiling. Assumed realistic spend: $200–400/month. It stops at a fixed amount instead of compounding. |
| C. No free tier, $10 starter | About $0 | No cost exposure, but developers can't test on real invoices before paying, so expect fewer signups and fewer trials of the product. |

**Fix the starter price too.** 500 pages at $0.02 is $10 of cost, which is zero margin before support, payment fees, and any hosting. Either raise the starter price (e.g., around $19 for 500 pages) or cut it to about 200 pages for $10 (cost $4, gross margin around 60% before other costs; assumed, check your real per-page cost).

**If even $200–400/month is too much**, use a free sandbox endpoint that returns fixture invoices with no OCR call. It costs almost nothing, lets developers see the response shape, and you can still run option B's credit for real pages as a second step.

**Assumed:** signups are about 2,000/month, most stop within a day, and about $0.02 is your full per-page cost. Support time and payment fees are excluded and should be added to the starter margin.

**Would change if:** you see a real share of credit users converting to paid (at which point a larger credit is worth its cost), or your measured per-page cost is well below $0.02.
