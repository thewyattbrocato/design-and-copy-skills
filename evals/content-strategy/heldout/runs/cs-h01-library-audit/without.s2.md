# Auditing a large library website in six weeks

You don't need to read every page. Audit with data first, then read only the pages where a human decision is needed.

## Week 1: Set scope and build the inventory

**Agree on goals with your director before touching anything.** Ask what prompted the request: outdated info, too much to maintain, poor search results, or an upcoming redesign. Your criteria depend on the answer. Get it in writing, even a two-line email.

**Build an inventory spreadsheet**, one row per page. Pull the URL list from a crawler (Screaming Frog's free tier handles 500 URLs; otherwise use your CMS's export or the sitemap). Then add:

- Page title, content type (event, branch, blog, service, etc.), and owner or author if the CMS records it
- Last-modified date
- Pageviews for the past 12 months (Google Analytics or whatever you have)
- Inbound links from other pages, and search impressions if you have Search Console

Most of this is automated. Your helper can do the cleanup.

## Week 2: Triage by rule, not by reading

Sort the sheet and apply bulk rules to clear out the obvious cases:

- **Past events** (a date in the past, nothing of lasting value): archive or delete in bulk.
- **Blog posts** older than a cutoff you choose (say 3 years) with low traffic: candidates for archiving.
- **Zero or near-zero traffic and no inbound links**: candidates for removal.
- **Duplicates**: sort by title to find near-identical pages, which are common in branch content.

Hundreds of rows will resolve here. Mark each with a provisional decision: **Keep, Update, Merge, Archive, or Delete**.

## Weeks 3-4: Review what's left

The remaining pages need a human look. Split them:

- **Branch pages (11 branches)**: check each against a short checklist: hours, address, phone, staff contacts, services, accessibility info. This is the highest-stakes content, so you or a branch manager should verify it, not just your helper.
- **Core service pages** (cards, borrowing, databases, room bookings): check accuracy, broken links, and whether the policies match current ones.
- **High-traffic pages**: spot-check these first, since errors here affect the most people.

Use a simple scoring rubric (accurate? useful? findable? duplicated?) so your helper's judgments match yours. Do the first 20 pages together to calibrate.

Also run a broken-link check and an accessibility scan (WAVE or similar) on the pages you're keeping.

## Week 5: Validate and decide ownership

- Send the Delete/Archive list for **branch managers and department heads to veto**, with a deadline. Silence means approval. This protects you when someone says "wait, we needed that."
- Assign an **owner for every page you're keeping**. Pages without owners are how you got here.
- Set up redirects for anything removed that has inbound links or search traffic. Don't delete anything without a backup or archive copy.

## Week 6: Report, then act

**What to give your director (aim for 2-3 pages plus the spreadsheet):**

1. **Summary:** Total pages reviewed, and counts by decision (e.g., "640 pages: 310 archive/delete, 90 merge, 140 update, 100 keep").
2. **Key findings:** The 3-5 most important things: for example, outdated hours on four branch pages, or 200 expired event pages making up a third of the site.
3. **Method:** One paragraph on how you did it, so the numbers are credible.
4. **Recommendations:** Governance, not just cleanup: who may publish pages, a template for events and branches, an annual review date, and a rule for expiring event pages automatically.
5. **Proposed next steps and effort:** What you can finish in the next quarter, what needs more help or budget, and what you'd skip.
6. **Appendix:** The full spreadsheet.

Then start executing the quick wins (bulk archive, redirects, branch corrections) so the director sees results, not just a report.

## Pitfalls to avoid

- **Don't start deleting during the audit.** Decide first, act after approval.
- **Don't treat low traffic as proof a page is useless.** Some pages (emergency closures, niche policies) matter even if rarely viewed.
- **Cap the scope.** If you run behind, finish the high-traffic and branch pages, and report the rest as "triaged by rule, not reviewed."

If you tell me what CMS you're on and what analytics you have, I can help with the specific export steps and set up the spreadsheet columns.
