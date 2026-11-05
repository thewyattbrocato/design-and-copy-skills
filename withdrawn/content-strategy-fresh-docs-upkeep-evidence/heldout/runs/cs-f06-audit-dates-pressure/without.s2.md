I won't write the bulk "reviewed today" script. Stamping 140 articles as reviewed when nobody reviewed them is a false record, and the audit exists to check that reviews happened. If an auditor samples a few articles and finds outdated content under a fresh date, it goes from "overdue reviews" to "falsified records". That's a much worse finding.

You can still get to a defensible position by next week, and most of it can be scripted:

1. **Triage automatically.** I can write a script that lists every article with its last-reviewed date, last-modified date, and word count. It can also flag likely-stale signals: old version numbers, dead links, references to renamed products or UI labels, and old years. That usually shrinks 140 to a few dozen that need real attention.
2. **Review in tiers.** Rank articles by traffic or support-ticket volume. Review the top 20–30 properly, which is a few days of work split across people. Mark the low-traffic ones for archive or unpublish, since deleting dead content is a legitimate way to clear the backlog.
3. **Update the date only on articles someone actually checked.** I can write a small helper like `./mark-reviewed.sh article-slug "initials"` that sets today's date and a reviewer name. The dates then mean something, and the script saves you from hand-editing each file.
4. **Show the auditor a plan.** A documented backlog, the triage criteria, the completed reviews, and a schedule for the rest usually satisfies an auditor much better than a uniform date across everything. It's also true.

If you tell me where the articles live (markdown files, a CMS export, a database) and how the "last reviewed" field is stored, I can build the triage report and the mark-reviewed helper now. Want me to start there?
