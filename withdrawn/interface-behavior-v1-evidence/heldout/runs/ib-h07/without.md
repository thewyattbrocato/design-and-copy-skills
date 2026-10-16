**Fix search first.** It's the only item on your list where staff fail to get the part. The rest slow them down.

## What's wrong, by severity

1. **Search fails on how people actually look things up.** It matches part name only, on exact words. Staff in a shop will search by model number, by the appliance and part in their own words ("washer pump"), and with typos. All of those return nothing. The "No results found." page then leaves them stuck, with no suggestion and no way to browse.
2. **Navigation loses state.** Filters reset and the scroll position jumps to the top when you press Back. Comparing parts means re-applying brand and price filters and finding your place again every time. This is probably most of the "clunky" feeling, because it happens on every lookup.
3. **No way to step through results.** Part detail is a dead end. Comparing three candidates means list, part, back, part, back.
4. **No context on the part page.** It doesn't show the query, the filters, or the position in the results (for example "3 of 12"). Combined with #2 and #3, people lose their place.
5. **Search only exists on the home page.** Every new search means navigating home first. This is minor, but it's cheap to fix with a search box in the header.

## What I'd do first

- **Search matching:**
  - Match on model number, part number, and aliases or synonyms, not just the name.
  - Tokenize and match words in any order, so "washer pump" finds "pump, washing machine".
  - Add typo tolerance and stemming ("washer" and "washing").
  - Rank name and part-number hits above loose matches.
- **The zero-results page:** show "did you mean…", the closest matches, and a link to browse by brand or category. It should never be a dead end.

Before building, pull the last few weeks of search queries and look at the ones that returned zero results. That shows which of model numbers, synonyms, or typos dominate, so you know what to build first. It also gives you a test set to check the fix against.

## Second

Keep filters, sort, and scroll position in the URL, or restore them on Back. Add the context bar to the part page at the same time (query, filters, "3 of 12", prev/next). Those two changes are closely related and fix items 2 through 4 together.

I haven't seen the codebase or any usage data, so this ranking comes from your description. If the logs show most searches already succeed, the state-loss fix could move up. If you point me at the repo, I can look at how search is implemented and scope the change.
