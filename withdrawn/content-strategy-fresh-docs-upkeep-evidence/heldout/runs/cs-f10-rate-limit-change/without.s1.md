**Rate limit change checklist (60 → 100 requests/min, live Monday)**

1. **Find every instance.** Search the docs for all 23 pages that mention the old limit, including the pricing page and the two tutorials. Search for variants like "60/min", "60 requests per minute" and "sixty". Keep a list to tick off.
2. **Update the spec file first.** The API reference is generated from it, so fix the number there and regenerate. That covers the reference without hand edits.
3. **Hand-edit the remaining pages.** Everything that isn't generated is hand-written, so each of those pages needs a manual change. That includes the pricing page.
4. **Tutorials: ask Dana.** Dana in developer relations owns them. Have Dana update or approve the two tutorials.
5. **FAQ: ask the support lead.** The support lead owns the FAQ. Have them update or approve it.
6. **Batch the translation request.** The agency charges per changed string. Make all English edits first, then send the French and Japanese changes in a single batch, so strings aren't paid for twice.
7. **Time the publish for Monday.** Merge the changes so the new number goes live Monday, not before. That includes the translations, so the three languages don't disagree.
8. **Re-search after publishing.** Search again for the old number in English, French and Japanese. Confirm that none of the 23 pages still shows 60.
