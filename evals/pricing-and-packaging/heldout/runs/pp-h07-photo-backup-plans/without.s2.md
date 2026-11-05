# Recommended plans

Storage costs $12 per TB per month, and 1,000 searches cost $3. Storage is the main cost, so the plans are sized around it.

| | **Free** | **Personal** | **Family** | **Pro** |
|---|---|---|---|---|
| **Price/mo** | $0 | $2.99 | $9.99 | $19 |
| **Price/yr** (2 months free) | n/a | $29 | $99 | $190 |
| **Storage** | 5 GB | 100 GB | 500 GB shared | 1 TB, add more in 1 TB steps for $16/TB/mo, up to 5 TB |
| **People** | 1 | 1 | Up to 6 | 1 (extra seats optional later) |
| **AI searches/mo** | 10 | 100 | 300 pooled | 1,000 |
| **Auto backup** | ✓ | ✓ | ✓ | ✓ |
| **30-day trash** | ✓ | ✓ | ✓ | ✓ |
| **Original-quality downloads** | ✓ | ✓ | ✓ | ✓ |
| **RAW support** | n/a | ✓ | ✓ | ✓ |
| **Face grouping** | n/a | ✓ | ✓ | ✓ |
| **Shared albums** | n/a | n/a | ✓ | ✓ |
| **Client galleries and watermarks** | n/a | n/a | n/a | ✓ |
| **Lightroom plugin** | n/a | n/a | n/a | ✓ |

## Why these tiers

- **Free (5 GB):** It costs you at most about $0.09 per user per month, including searches. That's cheap acquisition for people who stay under 20 GB. When they pass 5 GB, the upgrade is only $2.99.
- **Personal (100 GB, $2.99):** This covers nearly all of your "under 20 GB" users with room to grow. A full account costs about $1.50 including searches, which is roughly a 50% margin. A typical 20 GB user costs under $0.50.
- **Family (500 GB, $9.99):** This covers your 50–300 GB range with headroom. A fully used plan costs about $7.80 ($6.00 storage and $1.80 for 300 searches), so the worst-case margin is around 22%. A typical 200 GB family costs about $3.30, a margin of roughly 65%. Pricing it as one shared plan for up to 6 people is simpler than per-seat pricing and is the main reason families will pick it over three Personal plans.
- **Pro (1 TB at $19, then $16 per extra TB):** A 2 TB photographer pays $35 and costs you about $24 in storage. A 5 TB photographer pays $83 and costs you about $60. That's a 25–30% margin at full usage, higher if they don't fill their allotment. Big-storage users are your lowest-margin customers, so the plan makes them pay in proportion to what they store.

## Where the features go

- **Everyone gets the trust features:** auto backup, trash, and original-quality downloads. Gating these would hurt the "it just works" promise.
- **The upgrade levers are face grouping, shared albums, client galleries, and the Lightroom plugin.** Each is something one specific persona values and the others don't. Photographers won't mind paying for client galleries and Lightroom. Families will pay for shared albums.
- **Search caps are what keep your costs bounded.** 1,000 searches a month costs at most $3, so Pro's cap is generous but safe. Free's 10 searches lets people try AI search without costing you much.

## Caveats to check before launch

1. **Bandwidth isn't in your numbers.** Client galleries, downloads, and RAW preview generation all cost money beyond storage. Photographers' galleries are the biggest risk, so model egress for Pro before you lock in $19.
2. **App store fees** are 15–30% on in-app purchases and would cut Personal's margin to about 35–40%. Consider steering signups to the web, or price iOS slightly higher.
3. **Redundancy and compute.** If your $0.012 per GB is for a single copy, replication adds cost. Face grouping and RAW processing also use compute. Check that the cost figure includes these.
4. **Competitive pressure on price.** Google and Dropbox sell 2 TB for about $10–12, so you can't win Pro customers on price per TB. You win on client galleries, the Lightroom plugin, and search. Say that in the marketing.
5. **Check these numbers against your beta.** Look at the real distribution of storage and searches per persona. If most photographers sit at 3–5 TB, a prepaid 2 TB or 5 TB bundle may sell better than a base plan plus add-ons.
