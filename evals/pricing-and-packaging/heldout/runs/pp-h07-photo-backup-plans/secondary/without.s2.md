## Recommended plans

| Plan | Price (monthly / annual) | Storage | Who it's for |
|---|---|---|---|
| **Free** | $0 | 5 GB | Trial and acquisition |
| **Plus** | $2.99 / $29.99 | 100 GB | Casual phone shooters |
| **Family** | $9.99 / $99 | 500 GB pooled, up to 6 members | Shared families |
| **Pro 1 TB** | $24.99 / $249 | 1 TB | Working photographers, starting out |
| **Pro 5 TB** | $99.99 / $999 | 5 TB | Heavy RAW shooters |

**What goes in each:**

- **Free:** auto backup, 30-day trash, basic search (about 20 AI searches/month).
- **Plus:** everything in Free, plus face grouping, shared albums, original-quality downloads, and AI search (200/month).
- **Family:** everything in Plus, plus a shared family library, 6 members, and pooled AI search (300/month).
- **Pro 1 TB and Pro 5 TB:** everything in Plus, plus RAW support, client galleries with watermarks, the Lightroom plugin, and higher AI search quotas (1,000 and 3,000/month).
- **Add-on for Pro:** +1 TB for $19.99/month. This covers the middle of the 1–5 TB range without a separate 3 TB plan.
- **30-day trash** is on every tier. It's a trust feature, and you shouldn't gate it.
- **RAW support** is on every tier, but RAW files count against storage, so the Pro plans are where the quota matters.

## Margin check

Storage at $0.012/GB is about $12.29/TB/month, so a flat price under roughly $20/TB squeezes margin. These are worst-case numbers, assuming a user fills the storage quota and uses the full AI search allowance:

| Plan | Max cost/month | Margin at full use |
|---|---|---|
| Free | $0.12 | n/a (acquisition) |
| Plus | $1.80 | ~40% |
| Family | $6.90 | ~31% |
| Pro 1 TB | $15.29 | ~39% |
| Pro 5 TB | $70.44 | ~30% |

Most users won't hit the cap, so real margins will be higher than these.

## Caveats before launch

- **Downloads cost bandwidth.** Original-quality downloads of RAW libraries can cost more in egress than storage does. Check your provider's egress price, and consider a fair-use download limit on Pro.
- **Payment fees.** Stripe-style processing takes about 3%. If you sell through the App Store or Google Play, they take 15–30%, which changes every margin above. Price with that in mind.
- **Your $0.012/GB may be a blended rate.** Confirm whether it includes redundancy, request costs, and cold-storage tiering. Hot storage list prices are often higher.
- **Usage assumptions are guesses.** The search quotas and the 100 GB Plus cap are my proposals. Check the beta data for actual search frequency and storage distribution before you lock them in. If photographers search far more than 3,000 times a month, the Pro quotas need to change.
- **Over-quota behavior.** Pause uploads when a user hits quota. Don't delete anything. Deleting originals is the fastest way to lose trust.
