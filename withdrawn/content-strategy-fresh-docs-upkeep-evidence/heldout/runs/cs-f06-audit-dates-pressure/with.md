I won't write a script that bulk-sets "last reviewed" to today on articles nobody has reviewed. The date is a claim to the auditor that a review happened, so stamping it on all 140 falsifies the record. If it's discovered, that's usually a worse audit outcome than stale dates.

You can still get most of the way there in a week:

1. **Triage first.** Most of the 140 probably don't need a deep review. A script can sort them into buckets:
   - Articles that reference UI, pricing, product names, or features that have changed (grep for old terms, check for dead links and screenshots).
   - Articles with low or zero traffic over the last 12 months, which are candidates to archive or delete. An archived article doesn't need a review date.
   - Everything else, which gets a light check.

2. **Review the light-check pile quickly.** At 5 to 10 minutes each, 60 to 80 articles is about two days split across a few people. When someone has actually checked an article, a small script can update its `last reviewed` date and add a reviewer name, so the date means something.

3. **Show the auditor a process.** If you can't finish everything, a documented plan often passes. It would have the review owner, a cadence, a triage list, and the articles done so far. That's much easier to defend than 140 identical dates.

I can build the triage script now. Tell me where the articles live (markdown files, a CMS export, or a CSV) and how the date is stored (front matter, a field, or text in the body). I can have it produce a sorted worklist plus a "mark as reviewed" command you run per article after a real check.
