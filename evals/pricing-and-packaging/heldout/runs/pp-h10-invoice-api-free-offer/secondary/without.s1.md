**Recommendation: a small, one-time, page-capped trial with no card, plus a zero-cost sandbox. Skip the forever-free tier, and fix the starter price.**

**Why not the forever-free tier:** The cost never stops. Every account that stays around keeps a claim on 500 pages a month, and each monthly cohort adds to it. The worst case is 2,000 signups × 500 pages × $0.02 = $20,000/month, and that grows with each cohort. A free tier is the wrong choice when runway is tight.

**Why the trial beats forever-free:** A time limit alone doesn't bound cost, so the trial also needs a page cap. Capped at 50 pages, each signup costs at most $1 total, and the spend stops when the trial ends.

**Why not zero free:** It costs nothing, but developers who can't try the product before paying mostly won't sign up. With 2,000 signups a month, you'd lose most of your adoption for a small saving.

**What I'd do:**

1. **Sandbox with sample invoices.** Let people hit the API with a few bundled sample invoices and get canned output. This serves the "poke around for a day" crowd at zero cost, and it's probably most of your evaluation traffic.
2. **One-time trial: 50 pages, 14 days, no card.** Require a verified email and one trial per org or domain to limit abuse. Set the cap so the worst case fits your budget. Max monthly trial spend = signups × pages × $0.02. At 2,000 signups and 50 pages, that's $2,000/month if everyone maxes out; most won't. Lower the cap if that's too high.
3. **Fix the $10 starter.** At $0.02 per page, 500 pages costs you $10, so the plan has zero margin before any infrastructure or payment fees. Price it at about 250 pages to get roughly 50% gross margin, or raise the price.
4. **Measure for the first 30 days:** pages per trial account (median and 90th percentile), trial-to-paid conversion, and total trial spend. If spend goes over budget, lower the cap. If the median user never uses more than 10 pages, you can probably go lower.

The numbers above assume an average of about 10 pages per poke-around signup, which is my guess. Replace it with your real distribution before committing.
