I'd leave out the bulk date change, and I won't write a script or wording for it. People read "last updated" on a legal page to decide whether they can rely on it, for example on an eviction deadline or a benefits rule. If the date says this month and nobody has checked the page, you're telling readers something false. The harm lands on your clients, and it also puts the organization's credibility and possibly its liability at risk. Google also compares the visible date against the page's actual changes, so fake freshness is unlikely to help your ranking.

You can get most of what you want honestly. Pages that have been checked can show a real "Reviewed on [date]" line, and that is a stronger trust signal than a bare date.

## The plan

**The stuck decision:** you have about 200 pages and one part-time reviewer, so you can't tell which pages are wrong, and checking them all is impossible. The fix is to review by risk instead of reviewing everything.

### Step 1: Build an inventory (this week, you)
Make a spreadsheet with one row per page and these columns:
- Page ID
- URL
- Topic
- Current "last updated" date
- Monthly visits (from analytics)
- Laws, forms, fees or deadlines cited
- Owner
- Status
- Last verified
- Next review

Pull the first five columns automatically. Fill in the rest as you triage.

### Step 2: Triage into three tiers (you and a paralegal, about 2 weeks)
- **Tier A, high risk:** deadlines, court forms and fees, eviction, benefits eligibility, anything where a wrong answer causes harm. Also include any page with high traffic.
- **Tier B:** stable legal explainers that cite statutes.
- **Tier C:** general orientation and "how to find help" pages.

Don't assume visits mean a page is correct or that low traffic means it's unimportant. Low traffic may only mean nobody can find the page.

### Step 3: Assign owners
Each page gets one paralegal as owner, with the right to flag it, edit it, or recommend retiring it. The lawyer approves only Tier A changes and any change to legal meaning. This keeps her limited time on the pages where it matters.

### Step 4: Review in this order
1. **Tier A first.** A paralegal checks each page against its source: current statute, form version, fee schedule, court rules. The paralegal marks each page "no change", "minor fix" or "needs lawyer". The lawyer batches the "needs lawyer" pages into one short session a month.
2. **Tier B next**, then Tier C last.
3. **Retire or merge** pages that duplicate others or cover things that no longer apply. Cutting pages is the fastest way to make this workload manageable. Redirect the retired URLs.
4. **Pages that can't be reviewed soon** get a visible notice such as "This page has not been reviewed since [date]. Confirm current rules with [contact] before acting." That is honest and protects readers.

### Step 5: Triggers that keep pages current
Don't rely on a calendar alone. Tie review to events:
- Legislative session ends, or new laws take effect (a paralegal checks the relevant tags).
- Court forms or fee schedules change.
- A staff member or client notices an error. Put a "Report an error" link on every page that goes to a shared inbox.
- Fixed intervals as a backstop, for example Tier A every 6 months, Tier B yearly, Tier C every 2 years. Adjust these to the hours you really have.

### Step 6: Show real dates
Only change a page's date when someone has verified it. Use this wording:

> **Reviewed by [paralegal/attorney] on [date].** Law and forms change. This is general information, not legal advice.

Have the CMS stamp the date only when a reviewer ticks a "verified" box, not on any edit. This also makes the metadata in search results truthful.

### Monthly routine (about 1 hour for you)
Look at the inventory. Check what is overdue, which flagged errors are waiting, and which law changes are pending. Then set next month's review list so it fits the hours the paralegals and lawyer actually have.

### Two things to settle
- How many hours per week can each paralegal give this? That decides how many Tier A pages you finish per month. I haven't assumed a number.
- Does your CMS let you add a custom "Reviewed" field? If you tell me what you use, I can write a script that exports the page list for the inventory and, later, adds the verified-date field to pages. I can do that without touching any existing dates.
