# Seat-to-usage cleanup plan (about 4 hrs/week)

I haven't looked at your help center, so the time estimates assume a few dozen to a couple hundred articles. Adjust after the audit in Week 1.

## Before you start (1 hour, can overlap with Week 1)
Get these answers from product or billing. Everything else depends on them.
1. **Approved vocabulary.** What are the billable unit, the plan names, and the term for "seat" now (if "user" still exists as a non-billing concept)?
2. **Are any customers still on seats?** This includes grandfathered, annual-contract, and enterprise customers. If so, you'll need to keep some seat content and label it "legacy" instead of deleting it.
3. **Source of truth.** Who confirms billing details, such as overage, invoicing, and how to see usage? Get a named reviewer.
4. **Dates.** When did the change take effect, and when does the legacy plan end, if it does?

## Week 1: Audit and stopgap (4 hrs)
- **Inventory (about 2 hrs).** Search the help center, and your source files if you have them, for `seat`, `per user`, `per-seat`, `license`, `add user`, `user limit`, `invite`, and `billing`. Put each hit in a spreadsheet with these columns: URL, topic, type (billing, onboarding, FAQ, other), seat-reference count, has screenshots (Y/N), traffic, priority, status.
- **Add a stopgap banner (about 30 min).** Put a short notice on the billing hub and the top billing articles: "Tarnwick now uses usage-based pricing. Some articles are being updated." Link it to the new pricing explainer, or to the pricing page if the explainer isn't written yet.
- **Rank by risk (about 1.5 hrs).** Sort by traffic and by how likely a wrong answer is to cost money or create tickets. Pull the top support-ticket topics too, since those show where confusion is happening.

## Week 2: Write the new billing foundation (4 hrs)
Write one canonical "How usage-based billing works" article first. Later articles can link to it instead of re-explaining, which saves you time throughout.
- Cover what's billed, how usage is counted, where to see it, invoice timing, and what changed from seats.
- Have your reviewer sign off before you build on it.

## Weeks 3–4: Billing pages (about 8 hrs)
These carry the most risk, because a wrong answer here means billing disputes.
- Rewrite pricing, plans, invoices, upgrade/downgrade, and cancellation pages.
- Remove "add or remove seats" procedures. Replace them with usage monitoring and limits or alerts, if those exist.
- Where legacy customers remain, add a short "On a legacy seat plan?" section.
- Log any screenshots that need replacing, but don't redo them yet.

## Weeks 5–6: Getting started and onboarding (about 8 hrs)
- Reword any "seats included" and "invite your team" framing. Inviting people probably still exists, but it no longer affects cost.
- Update step-by-step flows to match the current UI.
- Check that the quickstart doesn't send new users to a seat-purchase step that no longer exists.

## Week 7: FAQ and roles/permissions (4 hrs)
- Rewrite or merge the seat-related FAQs. Many will collapse into a link to the canonical article.
- Check admin and permissions pages. "Seats" and "roles" often get mixed together there.

## Week 8: Long tail and redirects (4 hrs)
- Handle the remaining low-traffic hits from the inventory.
- Retire the articles that no longer apply, and set up redirects instead of deleting them.
- Re-run the keyword searches to confirm nothing was missed.

## Weeks 9–10: Screenshots (about 6–8 hrs)
Do these last, because UI changes while the text work is going on and you'd end up redoing them.
- Replace only the screenshots that show seat UI, pricing, or billing.
- Where you can, blur or crop to the relevant area so future UI changes break fewer images.
- Retake lower-priority ones on a best-effort basis.

## Ongoing
- Keep a short style note with the approved terms so new articles don't bring "seat" back.
- Ask support to flag any ticket that cites outdated docs, and treat those as top priority.

**Total: about 10 weeks at 4 hrs/week.** If you can only cover the high-risk content, finishing Weeks 1–6 (about 6 weeks) removes most of the customer-facing damage.

If you point me at the docs directory or an export of the help center, I can run the Week 1 inventory for you and give you the spreadsheet.
