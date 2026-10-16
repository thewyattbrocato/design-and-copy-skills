**Fix search matching first.** It's the only item on your list where staff can't finish their task. The rest cost them time.

## What's wrong, in priority order

1. **Search fails on the queries staff actually type.**
   - It matches part name only, on exact words.
   - Staff often look up parts by model number, so that is probably their most common query, and it returns nothing.
   - "washer pump" misses "pump, washing machine", and a misspelling misses everything.
   - "No results found." gives no next step, so staff conclude the part isn't in the catalog. That is worse than the search being slow.

2. **Back loses your place.** Filters reset and the list jumps to the top. Staff compare several parts per lookup, so they re-apply filters and re-scroll on every comparison. This is likely a large part of the "clunky" feeling.

3. **Detail is a dead end.** There's no next or previous, so comparing means a round trip through the list each time. This is the same problem as #2, and fixing #2 makes it much less painful.

4. **No context on the part page.** The search term and your position aren't shown, so staff lose track of what they were looking for.

5. **Search only on the home page.** Every new lookup means going back home. It's easy to fix, so do it alongside the others.

## What I'd do

**Step 1: search (biggest win)**
- Index part name, part number, compatible model numbers and a short alias or synonym list ("washer", "washing machine"). Normalize case and punctuation.
- Match on individual words, not the exact phrase. Add typo tolerance (fuzzy match or trigram) and rank name and part-number hits above the rest.
- Replace the empty state with the query echoed back, "did you mean" suggestions, a broadened search (drop filters or words), and a way to browse by brand or category.
- Log zero-result queries. That list tells you which synonyms and fields to add next.

**Step 2: keep state**
- Put the query, filters, sort and page in the URL, and restore scroll position on Back.
- Optionally open the part in a side panel or drawer so the list never unloads.

**Step 3: navigation**
- Add a search box to the header on every page.
- On the part page, add a breadcrumb or "Results for 'washer pump'" link, plus Previous/Next within the result set.

## Caveat
I'm working from your description, not usage data. Before building, check your search logs for how many queries return zero results and how many look like model numbers. If that share is small, Step 2 may deserve to go first. I'd still bet on Step 1.
