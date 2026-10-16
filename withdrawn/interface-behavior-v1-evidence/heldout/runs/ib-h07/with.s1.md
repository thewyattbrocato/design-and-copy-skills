**Assumption:** shop staff on desktop, looking up parts many times a day, often with a customer waiting. They're past their first week, so speed and not losing their place matter more than discoverability.

"Clunky" here is mostly two things: searches that fail for reasonable queries, and a flow that throws away your place. Each item in your list is one of those.

## What's wrong, most damaging first

1. **Search fails on normal queries.** It matches part name only, as exact words. A model number, a typo, or "washer pump" for "pump, washing machine" all return nothing. For a parts lookup tool, the most natural query is a model number. Every other problem is secondary when the search comes back empty.
2. **"No results found" is a dead end.** It doesn't say what was searched or what to try. Staff can't tell "the part doesn't exist" from "the tool didn't understand me."
3. **Back loses state.** Filters reset and the list returns to the top. Comparing parts means re-applying filters and finding your place again every time.
4. **Detail is a full page with no sibling navigation.** Checking three candidates costs three round trips to the list.
5. **No location or query on the part page.** After a click you don't know what you searched for or how you got there.
6. **Search is only on the home page.** Every new lookup starts with a trip home.

## What to fix first: search matching

- **When** a query is entered, **match** on part name, model number, part number, and aliases or synonyms (e.g. "washer" and "washing machine"). Match on any word, not all, and rank by how many words matched.
- **Tolerate** typos (fuzzy matching) and punctuation or case differences, because staff type fast and the model number "WM-3200" may be entered as "wm3200".
- **Why first:** fixing the other five makes a good search nicer, but fixing only the others leaves a tool that still returns nothing for common queries.
- **Verify before building the synonym list:** pull the actual zero-result queries from your search logs, if you keep them. They'll show which gaps matter. I don't have that data, so I'm not guessing at percentages.

Fix the empty state in the same change, since it's cheap:
- Echo the query: "No parts match 'wm3200'."
- Suggest a next step: a close spelling, or "Try the model number without dashes."
- Offer a way out, such as clearing filters if any are on, since filters are a common cause of zero results.

## Then, in this order

2. **Keep state on Back.**
   - **When** the person returns from a part, **restore** the filters, sort, and scroll position. Putting them in the URL also makes the view linkable.
   - **Why:** this is the second-biggest time sink, and it hits every successful search.
3. **Show where you are on the part page.**
   - Show a breadcrumb or "← Results for 'washer pump'" plus a position like "3 of 14".
4. **Add next/previous on the part page.**
   - **When** the person arrived from a list, **offer** Prev/Next buttons plus arrow-key shortcuts, in the order of that list.
   - Alternatively, open the part in a side panel next to the list. That's a bigger change, so I'd do Prev/Next first.
5. **Put search in the header on every page.**
   - Keep the current query in the box, and focus it with `/`.

## Checks
- Back from a part restores filters and scroll, and the filter state is visible on the list.
- Every page shows what was searched.
- Prev/Next and search both work by keyboard.
- No result is a dead end.

I haven't looked at the code. If you want, point me at the repo and I can find where search matching is implemented and start there.
