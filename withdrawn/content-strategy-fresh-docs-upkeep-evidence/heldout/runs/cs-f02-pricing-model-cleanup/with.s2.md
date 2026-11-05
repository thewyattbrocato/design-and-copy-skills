# Seat-to-usage cleanup plan

**Assumptions:** you have about 4 hours a week. I haven't seen the help center, so I don't know how many pages are affected (`[pages in scope]`). Week 1 produces that number, and weeks 2 onward may shift once you have it. Seats may still exist as a non-billing concept, such as team members or access. If so, don't do a blind find-and-replace.

**Order:** the pages where a reader could pay or decide wrongly come first. Cosmetic fixes come last.

## Week 1: Facts and inventory (4 hrs)

1. **Get one source of truth (1 hr).** Ask whoever owns pricing for a half-page fact sheet:
   - how usage is metered and billed;
   - what happens to existing customers (grandfathered, migrated, or both);
   - which old terms are retired and which are kept;
   - which settings or UI screens changed.

   Don't write any page until you have this. You'll otherwise rewrite twice.
2. **Build the list (2 hrs).** Search the help center for "seat", "per user", "per-seat", "license" and "add users", plus any plan names that changed. Use these columns:
   - ID
   - title
   - location
   - type (billing, getting started, FAQ, other)
   - what it says about seats
   - has seat screenshot? (y/n)
   - owner
   - notes
3. **Check support evidence (1 hr).** Skim recent tickets or chats for seat and billing confusion. This tells you which pages are actually hurting people. Traffic alone won't, because a quiet page can still be the wrong one.

**Output:** the list with IDs, a priority tag on each row, and a real `[pages in scope]` number.

## Week 2: Billing pages (4 hrs)

These are the worst to get wrong. Rewrite them from the fact sheet, not by patching sentences.

- Rebuild rather than annotate. A page built around seats won't work with a "now usage-based" note added to it.
- Have the pricing owner or finance check anything that states how charges work. Reading it back to yourself doesn't count.
- If a billing page walks through a task that changes the account, such as changing plans or cancelling, have someone run the steps on the current product before it ships.

## Week 3: Getting started (4 hrs)

- Fix the first-run path: setup steps, "invite your team" wording, and anything that implies a per-seat cost.
- Do the text now. If a screenshot shows the old UI and would mislead someone, flag it in the list and replace it in week 5. For incidental screenshots, don't block on them.

## Week 4: FAQ (4 hrs)

For each seat-related FAQ entry, make one call:
- **Update** it if the question still exists under usage pricing.
- **Merge** it into the new billing page if it duplicates one.
- **Retire** it if it only made sense with seats. Redirect it to the best current page.

Expect to retire or merge a fair number of these. Fewer, correct entries beat many entries with caveats. Add the questions customers actually ask about usage billing; the week 1 support skim tells you what those are.

## Weeks 5–6: Screenshots, then everything else (4 hrs each)

- **Week 5:** replace screenshots in priority order. First the ones showing seat or billing UI that no longer exists. Then the ones with misleading counts or labels. Leave incidental ones for last.
- **Week 6:** sweep the rest of the list and re-run the search from week 1 to catch what you missed. Check anything linked or translated from the changed pages. If you have translated copies, give translators the term list first so you only pay once.

## Guardrails (30 minutes, in week 6)

- **Term list:** one page stating which words are retired ("seat", etc.) and which replace them. This is also what you hand to translators.
- **Ripple rule:** ask whoever ships pricing or packaging changes to give you a heads-up before launch. You can then update pages as part of the change, so the docs don't lag a month behind next time.
- **Review date:** put "last reviewed" on billing pages and set a recheck for each pricing change.

## What I'd skip

- A full site audit. Only the pages the seat search surfaces are in scope.
- Re-shooting every screenshot. Only the ones that mislead.
- Style or tone edits while you're in the page. Every extra edit costs review time, and translation if you have it.

**To measure:** the Week 1 count decides whether the six weeks hold. If `[pages in scope]` is large, push FAQ and screenshots later and keep billing and getting started first. I'd rather you finish those two well than half-finish all four.
