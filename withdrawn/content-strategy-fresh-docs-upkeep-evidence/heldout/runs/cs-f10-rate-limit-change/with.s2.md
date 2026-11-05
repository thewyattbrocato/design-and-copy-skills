**Zephyrine rate limit change (60 → 100 req/min): docs checklist**

- [ ] **Find all 23 pages.** Search for every place the old limit is written (the "60 per minute" wording and any variants), and keep the list as the tracking sheet. Don't assume 23 is complete, so re-search after edits.
- [ ] **Update the API reference at the source.** It's generated from the spec file, so change the number there and regenerate. Don't hand-edit the output.
- [ ] **Update the hand-written pages.** That covers the pricing page and the rest of the 23 that aren't generated.
- [ ] **Get Dana (developer relations) to update the two tutorials**, including any code samples or retry/backoff logic that assumes 60.
- [ ] **Get the support lead to update the FAQ.**
- [ ] **Batch the translation request.** Because the agency charges per changed string, finish all English edits first and send French and Japanese as one batch, limited to the strings that actually changed. Allow lead time so the translations are ready for Monday.
- [ ] **Stage everything to publish Monday.** Don't let any page go live with 100 before the change takes effect, and keep the translated pages in sync with the English ones.
- [ ] **Verify after launch.** Re-search English, French, and Japanese for the old number and confirm nothing is left.
