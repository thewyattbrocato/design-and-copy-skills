**I recommend a capped trial: a one-time allowance of about 100 pages, usable within 14 days, with a hard stop and no card required. After that, users move to the paid starter plan.** I wouldn't do the forever-free tier, and I wouldn't launch with nothing free.

| Option | Cost per signup | Monthly cost at 2,000 signups |
|---|---|---|
| Free 500 pages/month, forever | Up to $10 per month, every month | Up to $20,000 per month if all use it fully. Usage also builds up, since free users never leave. |
| Trial capped at 100 pages | Up to $2, once | Up to $4,000. About $800 if the average signup uses 20 pages (assumed). |
| No free offer, $10 plan | $0 | $0, but developers rarely pay before testing an API, so I'd expect very few signups to convert. |

- **Free forever:** A fully used free tier costs you $10 per user per month, which is the whole starter price. It also doesn't fit your signups, because most developers leave after a day. You'd pay for the heavy users and get no conversion from the rest.
- **Capped trial:** 100 pages is enough to run real invoices through the API and judge accuracy. Your worst case is fixed at $4,000 per month, and you can set a monthly spend cap on top of that.
- **Nothing free:** Developers evaluating an API want to test it on their own invoices first, so I'd expect a $10 paywall to cut signups sharply. This is a judgment call, not something I measured.

**Fix the starter plan.** At $10, you can't include 500 pages.
- 500 pages costs you $10 to process, and a payment fee takes about $0.59 on top (assumed card-processor rates). That leaves you losing money on every customer.
- Include about 250 pages for $10. Your cost is $5 and your margin is about $4.40 per customer per month. Treat $10 as a floor and test higher, such as $15–25 for 250–500 pages. I don't have any evidence yet of what your buyers will pay.
- Charge per page beyond the included amount, at a rate clearly above 2 cents.

**Break-even on the trial:**
- At $0.40 of trial cost per signup and $4.40 of monthly margin, the trial pays for itself in the first month only if about 9% of signups convert.
- If paying customers stay about six months (assumed), you only need about 1.5% to convert, which is about 30 customers per 2,000 signups.
- Track this number from the first month. It decides whether the trial stays, shrinks to 50 pages, or goes up.

**Assumed:** The average trial user processes about 20 pages. Payment fees are about 2.9% plus $0.30. Paying customers stay about six months. Your 2 cents per page covers processing only, and I haven't included support.

**Would change if:**
- Real usage per signup is much higher than 20 pages. Then lower the cap.
- Conversion after a month or two is below about 1.5%. Then the problem is the product or the price, not the trial.
- A few larger buyers show up wanting thousands of pages a month. Then add a higher tier for them, and keep the starter plan as is.
