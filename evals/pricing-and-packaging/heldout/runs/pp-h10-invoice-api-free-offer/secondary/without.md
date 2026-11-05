**Recommendation: a 14-day trial with a small page cap, no card required, plus a sandbox that costs you nothing, and a paid starter plan.** Skip the forever-free tier.

**Why not the forever-free 500 pages:** the cost never stops. Every signup that stays around keeps a standing allowance, so your bill grows with your total accounts, not with new signups. Assume 2,000 signups a month and 5% of accounts stay somewhat active at 100 pages a month:

- Year 1: about 1,200 active accounts × 100 pages × $0.02 ≈ **$2,400/month**, and rising every month.
- Worst case, every account uses its full 500: $10 per account per month. That's a runway killer.

**Why the trial:** cost stops when the trial ends. Each signup has a fixed ceiling and then either pays or goes quiet. Your monthly cost is:

> new signups × average pages used during trial × $0.02

At 2,000 signups and an average of 10 pages used, that's about **$400/month**. A cap of 50 pages sets a hard ceiling of $1 per signup. I'd start with 50 pages and tune it using your real usage data.

**What I'd build:**

1. **Free sandbox endpoint.** Return canned line items for a set of sample invoices. Developers can integrate and poke around at zero cost, and most of the "poking for a day" traffic never touches your real OCR pipeline.
2. **14-day trial, 50 pages, no card.** Require email verification and rate-limit by IP and disposable-email domain. Without that, people will make multiple accounts to get more pages.
3. **Starter plan at $10 for about 300 pages.** At $10 for 500 pages you break even on processing before fees, so don't price it there. At 300 pages your processing cost is $6, leaving about $3.50 after Stripe's fees and your margin.

**Tradeoffs:**
- A card-required trial would cut abuse and drive-bys almost to zero, but it will also cut signups sharply. Given tight runway, I'd start without a card and add one if abuse shows up.
- My usage numbers (10 pages average, 5% active) are guesses. Before launch, check how many pages a typical developer actually uses in their first session. If it's much higher than 10, lower the trial cap or add the card requirement.
