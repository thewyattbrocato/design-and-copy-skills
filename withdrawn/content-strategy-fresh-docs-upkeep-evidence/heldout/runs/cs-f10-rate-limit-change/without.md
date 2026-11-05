**Zephyrine rate limit change (60 → 100 req/min): docs checklist**

- [ ] **Find all 23 pages** that mention the old limit (60/min), including the pricing page and the two tutorials. Keep the list as the working tracker.
- [ ] **Update the API reference at the source.** It's generated from the spec file, so change the limit there and regenerate. Don't edit the generated output by hand.
- [ ] **Hand-edit the remaining pages.** Everything other than the API reference is hand-written, so each one needs a manual change to 100/min.
- [ ] **Tutorials:** ask Dana (developer relations) to review and approve the two tutorial edits.
- [ ] **FAQ:** ask the support lead to update or approve the FAQ wording.
- [ ] **Translations:** send the changed strings to the agency for French and Japanese in one batch. They charge per changed string, so finalize the English first to avoid paying for rewrites.
- [ ] **Time the publish for Monday.** The English, French, and Japanese updates should all go live with the change. If the translations aren't ready, decide beforehand whether to ship English first.
- [ ] **Re-search the docs after publishing** for "60" and "per minute" variants in all three languages, to confirm that no old number remains.
