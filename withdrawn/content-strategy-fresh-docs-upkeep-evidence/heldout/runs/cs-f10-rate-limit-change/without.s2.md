**Zephyrine rate limit change (60 → 100 req/min) – docs checklist**

- [ ] **Update the spec file first.** The API reference is generated from it, so fixing the spec there covers the reference. Regenerate and publish it.
- [ ] **Edit the hand-written pages.** The old number is on 23 pages, and the generated reference may account for some of them. Find every remaining "60" mention by searching the docs, then change it.
- [ ] **Pricing page.** Update the limit and check that any plan comparison tables still read correctly.
- [ ] **Tutorials.** Ask Dana (developer relations) to update the two tutorials, including any code samples or retry logic that assumes 60.
- [ ] **FAQ.** Ask the support lead to update their FAQ answers.
- [ ] **Batch the translation work.** The agency charges per changed string. Send French and Japanese in one batch, once the English wording is final, so you pay for each string only once.
- [ ] **Time the publish for Monday.** Merge the English changes so they go live when the change does, and schedule the translations to match or follow closely.
- [ ] **Verify after publishing.** Search the live docs in all three languages for "60 requests" or "60 per minute" and confirm that none remain.
