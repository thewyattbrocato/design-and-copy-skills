I'd skip the bulk date change, and I won't write wording or a script for it. For legal information it's a real risk to your readers:

- A "last updated" date tells a tenant or benefits applicant that someone checked the page against current law. If a page is wrong, a fresh date makes it more dangerous, because people will rely on it more.
- If someone acts on an outdated deadline or form, a false date is a liability for the organization and for the lawyer whose name is behind the content.
- Google says it doesn't want dates changed without substantive updates. A bulk edit with no real change is the kind of thing that can backfire, and it wouldn't earn the trust you're after.

You can get most of the trust benefit honestly, and it's cheaper than it sounds.

## Plan: triage by risk, then keep a rolling review

**The problem:** about 200 pages of unknown accuracy, and three people, one of whom has little spare time. You can't review everything, so the plan has to decide what gets reviewed first and what gets retired.

### 1. This week: build an inventory (you, about a day)
Make a spreadsheet with one row per page and these columns:
- ID and URL
- Topic (housing, benefits, court forms, etc.)
- Real last-edited date (from your CMS)
- Traffic over the last 12 months (pull it; I'm not assuming any numbers)
- Contains time-sensitive facts? (deadlines, dollar amounts, fees, form numbers, statute or rule citations, office addresses and phone numbers)
- Owner
- Status: `reviewed`, `needs review`, `retire`, or `merge`

### 2. Next 2–3 weeks: triage (a paralegal, with the lawyer for 30 minutes)
Sort pages into three tiers:
- **Tier 1 – high risk:** deadlines, eviction and court procedure, benefits eligibility, links to court forms. Review these first, in order of traffic.
- **Tier 2 – stable:** general rights explainers that change rarely. Review on a slower cycle.
- **Retire or merge:** duplicates, pages about repealed programs, and anything nobody can verify. Cutting pages is a legitimate way to make the site more trustworthy, and it shrinks the review workload.

### 3. Who does what
- **Paralegals (one owner per topic area):** do the first-pass check. Compare the page against the current statute, court site or agency page. Fix the obvious things such as broken links, form numbers and phone numbers. Mark the page "ready for lawyer".
- **Lawyer:** reviews only what the paralegals flag as substantive, in a short batch. Give her a one-page list with the old text, the proposed text and the source link. A fixed, small slot (say, one hour every two weeks) works better than "when she has time".
- **You:** keep the sheet, publish changes, and show the date and reviewer on each page.

### 4. Triggers and cadence
- **Event-driven:** a law change, a new court form or a fee change triggers review of every page that cites it. Add a `cites` column to the sheet so you can search for affected pages. Paralegals likely hear about changes first, so give them an easy way to flag a page.
- **Scheduled:** Tier 1 pages get a review at least every 6 months and Tier 2 every 12 months (adjust to what your staff can sustain). Add the next due date to the sheet and look at it monthly.
- **Reader feedback:** put a "Is something here out of date? Tell us" link on each page that goes to a shared inbox the paralegals check.

### 5. What to show readers (honest freshness signals)
Show a date only when a person has actually checked the page:
- **Reviewed pages:** "Reviewed [month year] by [Legal Aid Org] staff. Law current as of that date."
- **Unreviewed pages, during the cleanup:** a short notice such as: "This page hasn't been reviewed recently. Laws and forms change, so please confirm details with us or the court before acting." This is honest, and it protects readers and the organization.
- Update the date only when a review happens, not when someone edits a typo. A visible "reviewed" date on a growing share of your site is the trust signal you want.

### What gets cut or paused
- No new pages until Tier 1 is reviewed.
- Retire or merge duplicates and dead-topic pages as you find them.

### Two notes
- Assumption: your CMS lets you add a reviewed date and a banner per page, ideally in a field separate from the last-edited date. If it doesn't, tell me which platform you use. I can write a script that exports the inventory (URLs, real edit dates, cited form numbers) to seed the spreadsheet.
- Measure first: before promising a timeline, count how many pages land in Tier 1. That number sets how many weeks of paralegal time the first pass takes.
