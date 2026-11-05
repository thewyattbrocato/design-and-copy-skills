# Seat-to-usage cleanup plan (about 4 hours a week)

**The decision:** which pages to fix first, which to retire, and which to leave alone. I haven't seen your page list, so everything below is sequenced by risk. Page counts are `[pages in scope]` until Week 1 produces them.

**Assumptions to confirm:**
- Someone at Tarnwick (product or billing) can give you a one-page, authoritative description of the new model. It should cover the unit that's metered, what's included, how overage and invoices work, and what happens to existing customers on seat contracts. Every page below depends on it, so get it in Week 1.
- "Seat" doesn't always mean pricing. Pages about users, roles and permissions may still be correct, so don't find-and-replace.

## Order of work

**Week 1: Inventory and source of truth**
1. Get the pricing description above, plus a term list: the new terms, the retired terms ("seat", "per user", and so on) and one owner for the list (you).
2. Search the help center for the retired terms and related phrases (seat, license, per user, invite/add user, user limit, plan comparison). Also search for the screenshots' alt text and captions.
3. Build a simple sheet with these columns: ID, title, URL, kind (billing / getting started / FAQ / other), what it says about seats, screenshot Y/N, verdict (fix / retire / merge / leave), and notes. Don't read every page closely yet. Just tag them.
4. Sort the verdicts into the tiers below.

**Weeks 2–3: Billing pages (highest harm)**
These are the pages where a wrong answer costs the customer money or produces a support ticket. Rebuild them rather than patching. Notes stacked on a seat-based structure will confuse readers.
- Merge duplicates into one page per fact. Don't keep a copy per plan.
- Retire pages that only make sense under seats (adding or removing seats, seat limits) and redirect them to the usage page that replaces them.
- Ask whoever owns billing at Tarnwick to check these pages before they go live. If a page explains charges, they should confirm it's right.
- Add a short "pricing changed" note for customers still on a seat contract, if such customers exist. That depends on a Tarnwick answer.

**Week 4: Getting started**
This is the page every new customer reads, so seat language there causes the most confusion for the least editing effort. Remove or rewrite the seat steps. If a step only exists because of seat setup, cut the step.

**Weeks 5–6: FAQ**
- Rewrite the seat questions to match the new model, and delete the ones that no longer apply.
- Check your support team's recent tickets against the FAQ. Questions that keep coming in about billing are probably missing from it, so add them.

**Week 7 onward: Everything else and screenshots**
- Work through the long tail in the order your sheet ranks it, as time allows.
- Screenshots go last because they cost the most. First check which ones show seat UI only incidentally. Cropping or removing those is cheaper than reshooting. Reshoot only the ones where the seat UI is the point. Wait until the product's billing screens have stopped changing before you reshoot.

## Rules to keep it from coming back
- **Ripple list:** before any pricing fact changes again, list every page and screenshot that states it. The sheet from Week 1 is that list.
- **Review dates:** add a "last reviewed" date to the billing pages. Pricing is the kind of content that goes stale on a trigger, not on a calendar. Whenever Tarnwick changes pricing, review the billing pages.
- **Release checklist:** ask product to add "docs updated" to their definition of done for pricing changes. Without that, you'll be told after the fact again.

## Two things to measure
- `[pages in scope]` and the tier counts from Week 1. Once you have them, I can turn the weeks above into a real schedule instead of a sequence.
- Whether the old pricing is still live for anyone. If it is, the retired pages can't all be deleted, and some need a "legacy plan" label instead.

If you paste the page list or a URL export, I can build the Week 1 sheet and assign verdicts.
