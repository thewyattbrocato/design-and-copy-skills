I won't write a script that stamps "reviewed today" on articles nobody reviewed. An auditor would read that date as a claim that a review happened, so it would be falsified compliance evidence. If it came out later, it would likely be a bigger problem than two-year-old dates, and it would put you personally on the hook.

You have a week, and 140 articles is a manageable review if you triage. I can help with that:

1. **Inventory script.** It pulls each article's title, last-reviewed date, last-modified date, and word count into a CSV, sorted by staleness. That gives you an honest picture of what you have.
2. **Triage by risk.** Most help centers have maybe 20 to 30 high-traffic or high-risk articles, such as billing, security, account access, and anything with UI screenshots. Those get a real review first.
3. **Fast review for the rest.** A checklist takes about 5 minutes per article: do the links work, do the steps match the current product, is the screenshot or terminology outdated. I can write a link checker and a script that flags mentions of old product names or deprecated features, so you only read the articles that need it.
4. **Date updates tied to real reviews.** A small script sets the `last reviewed` date and a reviewer name, but only for the article IDs you list as reviewed. The dates stay truthful, and the work is quick.
5. **A plan for the rest.** For whatever you don't get to, a short remediation plan ("remaining N articles scheduled for review by X, owner Y") usually satisfies auditors better than a spotless-looking record.

Tell me where the articles live (markdown files, a CMS export, or something else) and what the date field looks like. I'll start with the inventory script and the link checker.
