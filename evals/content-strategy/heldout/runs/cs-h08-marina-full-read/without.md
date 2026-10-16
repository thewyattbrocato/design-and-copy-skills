# Full-site audit plan: 280 pages in 12 weeks

**Budget:** 120 hours ÷ 280 pages is about 26 minutes per page. Reading everything fits comfortably. Estimated cost is about 20 min × 120 slip/service pages + 12 min × 160 other pages, which is about 72 hours. That leaves room for setup, owner coordination, a final report, and slippage.

## Schedule

| Week | Work | Hours |
|---|---|---|
| 1 | Setup: build the inventory, pre-fill the data columns, finalize the rubric, calibrate on 10 pages | 10 |
| 2-4 | Slip, rate and service pages (about 40/week). Send each batch to the harbormaster as you finish it | 10/wk |
| 5-6 | Events pages, in batches. Send each batch to the events coordinator | 10/wk |
| 7-9 | News, local area and staff bios (about 50/week, since these are quicker) | 10/wk |
| 10 | Re-score check (see below), resolve open owner questions, clean up the data | 10 |
| 11 | Synthesis: patterns, priority list, and a recommended action per page | 10 |
| 12 | Write the report, review it with the owners, and use any leftover time as buffer | 10 |

Doing the harbormaster's pages first gets them the most time-sensitive findings (wrong rates, stale availability) early. It also gives them weeks to answer questions while you keep going.

## Week 1 setup

1. **Build the inventory from the sitemap.** Give each page a stable ID such as `S-001` for slips or `N-014` for news.
2. **Pre-fill what you don't need to read for.** Run a crawler (Screaming Frog's free tier covers 500 URLs) and pull in analytics, then add these columns:
   - Title tag and meta description
   - Word count
   - Last-modified date
   - Status code
   - Inbound internal links
   - Last 12 months of pageviews

   This way your reading time goes to judgment, not data entry.
3. **Tag each page** with section, page type and owner (you, harbormaster or events coordinator).
4. **Calibrate.** Score 10 mixed pages, then look at your scores again a day later. Fix any rubric criteria you scored inconsistently. Write the rubric definitions on a separate sheet so you can refer to them.

## What to write down for each page

**Pre-filled in week 1 (no reading needed)**
- ID, URL, section, page type, owner
- Pageviews, last-modified date, word count, inbound links, status code

**Entered while reading**
- **Date reviewed and minutes spent.** Time spent helps you check your budget by week 3.
- **Purpose:** one line on what the page is for and who it serves.
- **Scores (1-3 each):**
  - *Accuracy/currency:* is it still true (rates, hours, names, dates, policies)?
  - *Content quality:* is it clear, complete, and well written?
  - *Usefulness:* does it serve a visitor or business goal? Is it duplicated elsewhere?
  - *Structure and findability:* headings, title, links in and out, a clear next step
  - *Technical:* broken links, images and alt text, mobile rendering, forms working
- **Issues found:** specific and short, such as "2023 rate table", "bio lists former harbor manager", or "dead link to tide chart".
- **Recommended action:** Keep, Update, Merge, Redirect or Remove.
- **Priority:** High, Medium or Low.
- **Effort:** S, M or L.
- **Needs owner confirmation:** Y/N, plus the question for them.
- **Owner response and date:** filled in later.

Define 1, 2 and 3 for each score in writing. For example, Accuracy 3 = verified current, 2 = probably current but unverified, 1 = known wrong or clearly stale. Keep the scores to five, since more than that slows you down and the scores start to blur together.

## Handling the other two owners

- You can judge clarity, structure and broken links yourself, but you can't verify rates, availability or event details. Mark those pages "Accuracy: unverified" and add a question for the owner, instead of guessing.
- Send questions in weekly batches with a filtered view of the spreadsheet (just their pages and questions). Ask for answers in a column, not by email thread.
- Old event pages are probably mostly Remove/Redirect/Archive decisions. Ask the coordinator one policy question up front, such as "keep past events for how long?", so you aren't asking about each one.

## Keeping scores consistent over 12 weeks

- Read pages of the same type together, since your scoring will stay more consistent.
- In week 10, re-read 10-15 pages from weeks 2-3 and compare to your original scores. If they drifted, re-score that section.
- Don't re-score as you go. If you change the rubric, note the date and fix earlier rows in week 10.

## Synthesis (weeks 11-12)

- Pivot by section and action: how many Keep, Update, Merge and Remove.
- Sort High priority by pageviews, so the fixes that matter most to visitors come first.
- Look for patterns, such as the same outdated boilerplate on 30 pages or three pages competing on the same topic. Those are usually the best findings for your boss.
- The report can be a one-page summary, the top 20 fixes, and the spreadsheet as an appendix.

If you want, I can draft the spreadsheet column layout with the rubric definitions written out, or the first message to the harbormaster and events coordinator.
