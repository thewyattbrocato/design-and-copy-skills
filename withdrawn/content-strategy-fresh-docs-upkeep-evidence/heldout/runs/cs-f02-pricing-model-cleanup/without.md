# Seat-to-usage docs cleanup plan

I haven't seen your help center content, so the time estimates are guesses. Adjust them once you've done the inventory.

## Week 1: Facts, inventory, triage (4h)

1. **Get a source-of-truth brief (1h).** Ask product or billing for one page covering:
   - the new billing unit, its exact name, and how it's metered
   - what happens to existing customers (grandfathered, migrated, or a cutover date)
   - whether seats still exist for anything, such as user limits, permissions, or admin roles
   - invoice and billing-page changes
   - the words you should and shouldn't use

   Don't edit anything until you have this. Otherwise you'll rewrite twice.
2. **Inventory (1.5h).** Search for `seat`, `per user`, `per-seat`, `license`, `user limit`, `add users`, `upgrade plan`, and old plan names. Put every hit in a spreadsheet with these columns: URL, type (billing, onboarding, FAQ, other), traffic, severity, and has-screenshots. Pull page views and top support-ticket topics if you can.
3. **Triage (1h).** Sort every page into one of these:
   - **Wrong and costs money:** billing, pricing, invoices, upgrade or downgrade, cancellation.
   - **Wrong but confusing:** getting started, FAQ.
   - **Mentions seats incidentally:** one stray sentence or a screenshot.
   - **Still correct:** seats may still apply to user management or permissions, so don't over-purge.
4. **Stopgap (30m).** Add a short banner on the main billing pages, such as "Pricing changed to usage-based on [date]. Some articles are being updated." This keeps readers from being misled while you work.

## Week 2: Billing pages (4h)

These are the highest risk because wrong info here creates tickets, disputes, and refund requests.

- Rewrite the core billing explainer first: how usage is measured, how invoices work, and where to see usage.
- Then update invoices, payment methods, plan changes, and cancellation.
- Write the new text once and reuse it. A short glossary or snippet saves time later.
- Have billing or support skim these before you publish, since you can't verify the numbers yourself.

## Week 3: Getting started and onboarding (4h)

- Rewrite text first and leave screenshots for later. Remove steps like "choose how many seats" and replace them with the usage-based equivalent.
- Check the first-run path end to end, since new users hit these pages first.
- Where a screenshot is now wrong, cover it with a clear text description for the moment. Don't leave a misleading image up.

## Week 4: FAQ and long tail (4h)

- Rewrite or merge the FAQ entries. Many seat questions turn into "how am I charged?" and can collapse into one or two answers.
- Add a **"What changed from per-seat pricing"** FAQ for existing customers. It will probably be your most-read page.
- Work through the incidental mentions from your inventory. These are quick edits.
- Add redirects or update internal links for any pages you retitled or deleted.

## Weeks 5–6: Screenshots (about 6–8h)

- Batch them. Capture all new screenshots in one session, with the same account state, window size, and theme.
- Start with the screenshots on the billing and onboarding pages you already rewrote, then work down by traffic.
- Check for seat counts, "Add seat" buttons, and old plan names, which are easy to miss.
- Decide per image whether it needs to be replaced, cropped, or deleted. Many can go.

## Week 7: Verification (2–3h)

- Re-run your search terms and confirm the remaining hits are intentional.
- Check the site's own search results for "seat" and fix whatever ranks highly.
- Ask support to flag any tickets that still cite old docs for two weeks.
- Remove the stopgap banner.

## Shortcuts

- Talk to support early. Their ticket tags show which seat-related articles are hurting people today, so you can reorder weeks 3–4.
- Leave seat references alone in any article about user roles or permissions, unless product says seats are gone entirely.
- If the budget runs out, cut the long tail and low-traffic screenshots. Keep the billing, onboarding, and "what changed" pages.

If you can point me at the docs, whether that's a folder, an export, or a repo, I can run the inventory and build the spreadsheet so week 1 gets much shorter.
