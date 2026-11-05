I won't help with this one. Stamping "reviewed today" on articles nobody reviewed makes the audit record false. If an auditor spot-checks a single article, or the content is wrong in a way that hurts a customer, the fake dates are worse than the old ones. Honest-but-stale is a finding. Falsified is a much bigger problem.

You can still get to a defensible state in a week, though.

**1. Triage (an hour or two)**
I can write a script that scans all 140 articles and outputs a CSV with title, last-reviewed date, last-modified date, and flags for things that usually go stale (version numbers, UI terms, pricing, links that now 404, references to removed features). That sorts the pile into:
- **Probably fine**: evergreen, no flagged content. These need a quick skim.
- **Needs real edits**: broken links, outdated UI, etc.
- **Cut**: duplicates or dead features. Archiving one removes it from audit scope.

**2. Review the real ones**
Most help articles take 2–5 minutes to skim. Split 140 across a few people and it's about a day of work. Prioritize the top 20–30 by traffic or support-ticket volume.

**3. Make the date reflect reality**
Once someone has actually checked an article, a script can bump the date and add a reviewer name. Something like: read a `reviewed.csv` of article IDs and reviewers, and update only those files. That gives you a true record and an audit trail.

**4. Go in with a plan**
If you can't finish everything, tell the auditor "X reviewed, Y archived, Z scheduled for [date], owner is [name]". Auditors generally respond well to that. It's often enough to pass.

If you tell me the format (markdown, HTML, CMS export?) and where the files live, I can write the triage script now and the date-update script for confirmed reviews.
