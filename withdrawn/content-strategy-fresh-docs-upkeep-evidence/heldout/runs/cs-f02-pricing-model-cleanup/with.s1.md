**Stuck decision:** fix. A fact changed and nobody has listed every page that states it. Everything below is ordered by how much harm a wrong page does, not by where it sits in the help center.

## The plan, in order (about 4 hours a week)

**Week 1: fact sheet and inventory**
1. **Fact sheet (1h).** Get one page from whoever owns pricing at Tarnwick: what is billed now, how it's invoiced, what happens to existing customers, the effective date, and which words are approved and retired (for example "seat"). Every later edit checks against it. If you can't get it, nothing downstream is safe.
2. **Inventory (2h).** Export the help center and build a sheet with these columns: ID, URL, page type, mentions seats (Y/N), screenshot shows seats or pricing (Y/N), moves money or changes access (Y/N), owner, action (rewrite, patch, merge or retire), priority. Search on "seat", "per user", "license", and "add or invite users".
   - Some user-management pages will still be correct, because adding a user may no longer affect billing. Judge each page against the fact sheet, not by keyword.
3. **Stopgap (1h).** Put a short notice on the billing pages saying pricing changed on [date] and some pages are being updated. Then readers aren't misled while you work.

**Weeks 2–3: pages where a wrong answer costs money or access**
4. **Billing, plans, invoices, upgrade/downgrade/cancel.** Rebuild these rather than patching, since seat logic is probably in their structure. Someone must run every step on the current product before they ship. Reading the page through doesn't count. Anything unrun ships marked unverified.
5. **Pricing FAQ.** Start with the questions support actually gets about the change.

**Weeks 4–5: onboarding**
6. **Getting started.** Rebuild wherever the flow assumes buying or assigning seats. Patch where it only mentions them in passing.

**Then, as hours allow**
7. **Admin and user-management pages.** Patch the wording about seat limits and billing.
8. **Remaining FAQs.** Merge duplicates and retire anything about the old model. Don't update a page just to keep it.
9. **Screenshots.** Pages from steps 4–6 get new screenshots with their rewrite. Do the rest last. Where a shot only incidentally shows a seat count, crop it or leave it.

**Ongoing, from week 1**
- **Ripple list.** Keep it on the inventory sheet. For anything outside the help center that states the old model (in-app text, emails, API docs, the marketing site), note the owner and tell them. You can't fix those yourself.
- **Docs are part of done.** Ask Tarnwick's product and pricing owners to treat the docs change as part of any pricing change shipping.

## Cut and decide
- Retire old per-seat pages instead of rewriting them.
- Keep a legacy page only if some customers are still billed per seat. In that case, keep one page with the differing lines marked, not a copy.
- Don't polish pages that merely mention seats in passing until steps 4–6 are done.

## Notes
- **Assumption that changes the plan:** I assumed nobody is still on per-seat billing. If some customers are, billing pages need that split, and step 4 gets bigger.
- **To measure:** the number of weeks depends on `[pages in scope]` from the inventory. After week 1 you'll know, so re-cut the schedule then.
