**Fix search matching first.** Search is the tool's core job, and it fails on the way staff most likely look things up. Everything else here is friction. This is a dead end.

## What's wrong, in priority order

1. **Search is too literal.** It matches part name only, with exact words. Model numbers, typos, and different word order or wording ("washer pump" vs. "pump, washing machine") all return nothing. Staff often start from the appliance in front of them, so this probably fails on a large share of real lookups. They then conclude the part doesn't exist or give up on the tool, which is likely a big part of the "clunky" feeling.
2. **"No results found." is a dead end.** It compounds #1. It gives no suggestions, no hint about what was searched, and no way to loosen the query.
3. **Back loses your place.** Filters reset and the list jumps to the top. Anyone comparing several parts has to redo their work each time. This is the most irritating problem once search works.
4. **No context on the part page.** The search term and your position aren't shown, so you can't tell how you got there.
5. **No way to step to the next result.** Comparing parts means going back and forth through the list, which makes #3 hurt more.
6. **Search only exists on the home page.** Any new search means navigating home first.

## What to do first

- **Index more fields.** Search part name, model/compatibility numbers, part number, brand, aliases, and category.
- **Tokenize and match loosely.** Match words in any order, so "washer pump" finds "pump, washing machine". Handle punctuation. Add synonyms such as washer/washing machine.
- **Add typo tolerance.** Use fuzzy matching or trigram search, and rank exact matches first.
- **Improve the empty state.** Echo the query, suggest "did you mean…", and offer to clear filters or search by model number.

If you're on Postgres, `pg_trgm` plus full-text search covers most of this. Otherwise a small search engine like Meilisearch or Typesense gets there quickly.

## Next, in order

1. Put filters, query, and sort in the URL, and restore scroll position on Back. This is cheap and fixes #3 immediately.
2. Make search persistent in the header, and show a breadcrumb or "Results for 'x'" on the part page.
3. Add prev/next on the part page, using the result list kept in that URL state. A side panel or drawer instead of a full page is an alternative.

## Before you commit

I haven't seen the code or any usage data. Check the log of zero-result queries first. If model numbers and misspellings dominate, that confirms the order above. If staff mostly search clean part names, the Back-button state loss (#3) should move up to first.

If you point me at the repo, I can look at the search implementation and make the first change.
