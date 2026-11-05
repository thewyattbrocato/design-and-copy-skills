# Tarnwick docs cleanup: seats to usage-based

This plan assumes about 4 hours a week and roughly 6 weeks. I haven't seen your help center, so the time estimates are guesses until the audit gives you real page counts.

## Week 1: Audit and decisions (4h)

1. **Inventory (1.5h).** Search the help center for `seat`, `user license`, `per user`, `per-seat`, `add a user`, `invite`, `team size`, and `licenses`. Export the results to a sheet with these columns: URL, page type, seat-mentions count, has screenshots, traffic, and priority.
2. **Get the facts (1h).** Ask product or billing for a one-page source of truth. It should cover:
   - What the billing unit is now.
   - What happens to existing seat-based customers (grandfathered, migrated, or both).
   - What "users" still mean, since roles and invites probably still exist without being priced.
   - The new terms for the UI and docs.

   Don't edit anything until you have this. Otherwise you'll rewrite pages twice.
3. **Terminology map (0.5h).** Write a short old-term → new-term table, including words to avoid.
4. **Triage (1h).** Sort pages into three tiers:
   - **A: wrong and costly.** Billing, pricing, plan comparison, upgrade/downgrade, invoices.
   - **B: misleading.** Getting started, onboarding, and FAQ answers that assume seats.
   - **C: incidental.** A passing "per seat" mention or a stale screenshot.

## Week 2: Tier A text (4h)

Rewrite the billing pages first. They carry the most support-ticket and trust risk. Write the new usage-billing concepts page first (what's metered, how it's invoiced, how to view usage), then fix the other billing pages to link to it. If you have a legacy-customer path, put a short "If you're on a seat-based plan" section in one place and link to it from elsewhere.

## Week 3: Tier B text (4h)

- **Getting started (2h).** Remove seat steps such as "purchase seats" and "assign a license." Keep the user-invite flow if it still exists.
- **FAQ (2h).** Rewrite or delete the seat questions, and add the questions customers are probably asking now: "How am I charged?", "Can I set a usage cap?", and "What happened to my seats?" Your support team can tell you the real top questions.

## Week 4: Screenshots (4h)

1. List the screenshots that show seat UI. Your inventory should have flagged these.
2. Check with product on whether the UI is final. Retaking screenshots before it settles wastes your scarce hours.
3. Retake the Tier A and B screenshots in one batch, using one test account and one browser size. For the rest, crop out or blur the seat areas when you can, or remove the image.
4. Add alt text as you go.

## Week 5: Tier C and links (4h)

- Fix the incidental mentions with find-and-replace guided by your terminology map, but review each change.
- Check redirects, internal links, and anchors that pointed at deleted or renamed seat pages.
- Check search synonyms. People will still search "seats," so make sure that term surfaces the new billing pages.

## Week 6: Verify and hand off (4h)

- Re-run the Week 1 searches. Every remaining hit should be intentional, such as the legacy-plan section.
- Ask support or success to spot-check the billing pages against what customers actually ask.
- Write a short style note on the new terms so future docs don't drift back.
- Keep a changelog entry or banner if customers saw the old docs recently.

## Ways to save time

- **Interim banner (15 min, Week 1).** Add a note on the billing pages saying "Pricing changed on [date]. Some pages are being updated." This covers you while the rewrite happens.
- **Delete rather than rewrite.** Many seat-specific pages, like "How to buy more seats," can be retired and redirected.
- **Ask for help on the biggest costs.** Screenshots are usually the biggest time sink. If a designer or PM can retake them, you save most of Week 4.

If you paste or point me at the help-center export or a content folder, I can build the Week 1 inventory and triage sheet directly and give you real page counts.
