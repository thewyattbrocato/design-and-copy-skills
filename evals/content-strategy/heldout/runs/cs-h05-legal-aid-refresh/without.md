I'd leave out the bulk date change. I can help with everything else.

**Why not change the dates**
- **It misleads readers.** A "last updated" date on legal information tells people someone checked it. If a page about eviction notice periods or benefit thresholds is wrong, a fresh date makes people more likely to rely on it. For a legal aid org, that creates real harm and liability.
- **It probably won't work for Google.** Google says not to fake freshness, and it can compare the date to the page content. Pages with dates that don't match their content tend to lose trust, not gain it.

**What gets you the trust and freshness benefits honestly**

Show a real "Last reviewed by [role], [date]" on each page, and only set it when someone actually reviews the page. For pages not yet reviewed, you could show a banner like:

> *This page has not been reviewed recently. Laws change. For help with your situation, contact us at [link/phone].*

That is better for users than a false date, and it shows you're maintaining the pages.

**Plan**

1. **Inventory (you, 1–2 days).** Export every page into a spreadsheet with URL, title, topic, current "last updated" date, and monthly traffic from analytics. I can write a script to crawl the site or parse a sitemap and produce this CSV. Tell me your CMS or give me an export, and I'll write it.
2. **Triage by risk and traffic.** Score each page:
   - **High risk:** deadlines, dollar amounts, court forms, statute citations, fee waivers, benefit eligibility.
   - **Medium risk:** procedures and contact info.
   - **Low risk:** general concepts.

   Review high-traffic, high-risk pages first. Expect the top 30–40 pages to cover most of the value.
3. **Cheap automated checks (you).**
   - Run a link checker, since broken links and dead form URLs are the most common signs of staleness.
   - Search for hard-coded years, dollar figures, and statute numbers to flag pages that cite specific values.
   - Check that linked court forms still match the current versions.
4. **Split the review work so the lawyer's time goes only to legal judgment.**
   - Paralegals do a first pass using a short checklist: links work, forms are current, citations still exist, and contact info is right. They mark each page "no change," "minor edit," or "needs attorney."
   - The lawyer reviews only the flagged pages and the high-risk ones, in batches of about 5–10 per sitting.
5. **Set a cadence.** Review high-risk pages every 6 months and the rest every 12–18. Put a `next_review_date` field in the CMS or spreadsheet so overdue pages surface automatically.
6. **Subscribe to change sources.** Follow legislature session summaries, court rule updates, and agency fee or benefit announcements. When something changes, search your inventory for affected pages. This catches changes the calendar misses.
7. **Handle pages nobody can maintain.** Consolidate duplicates. For pages you can't review, either unpublish them or add the "not recently reviewed" banner. Fewer, accurate pages beat a couple hundred uncertain ones.
8. **Add a feedback channel.** A "Is this page out of date? Tell us" link gives you free error reports.

**Rough timeline:** the inventory and triage take about 2 weeks. The first 40 priority pages take 1–2 months at about 3–5 hours a week of attorney time. After that, the cadence keeps it going.

I can start on the inventory script, the paralegal checklist, or the banner and "last reviewed" wording. Which would help most? If you want the script, tell me what CMS you use (WordPress, static site, something else).
