**Assumption:** Shop staff on a desktop or counter terminal look up parts all day, often with a customer waiting. They're past the first week and want speed, not guidance. No usage data was provided, so I've ranked by how much each problem costs per lookup, not by measured frequency.

## What's wrong

"Clunky" is really six separate problems. Two of them cause most of it.

1. **Search can't find parts.** Name-only exact-word matching fails on model numbers, typos, and word order ("washer pump" vs "pump, washing machine"). People search by model number or by whatever they call the part, so a miss is the normal case. Each miss costs a retry, and staff learn to distrust the tool.
2. **Back wipes your place.** Filters reset and the scroll position is lost. Comparing parts is the main job, so this repeats the work on every comparison.
3. **The empty state is a dead end.** "No results found." doesn't say what was searched, what was assumed, or what to try next. That's most damaging when #1 is the cause.
4. **No way to step through results.** Looking at three candidate parts costs three round trips to the list.
5. **No location or context on the part page.** The query and the path back disappear.
6. **Search only on the home page.** Every new lookup means navigating home first.

## Fix first: search matching, with a better empty state

When someone types a query, match across part name, model number, part number, and aliases. Tolerate typos and ignore word order and punctuation. Rank exact model and part-number hits first.

I'd put this first because it's the root cause. Items 2, 4, 5 and 6 only make a working flow smoother, and none of them matters if the search returns nothing. Staff will feel it immediately.

Pair it with the empty state, since it covers the cases matching still misses:
- Echo the query: "Nothing for 'wsher pmp'."
- Say what was tried and offer the nearest alternatives: "Did you mean *washer pump*?"
- If filters are active, say so and offer one control to clear them. This often explains an empty list.
- Offer a next step, such as searching by model number or browsing by brand.

## Fix second: keep state across Back

When someone opens a part and returns, restore the filters and scroll position. Put the query and filters in the URL so Back, reload, and sharing a link all work. This is cheap and removes the next most frequent annoyance.

## Then, in order

3. **Search box in the header on every page**, prefilled with the current query. This also fixes #5, because the page now shows what you searched for.
4. **Context on the part page:** a breadcrumb back to "Results for 'washer pump' (14)" and the active filters.
5. **Next and previous within the results**, with a position indicator ("3 of 14") and arrow-key shortcuts. Better still, open the part in a side panel next to the list so the list stays in place. Do this after #2 and #4, since it builds on both.

## Before building

- Pull the actual zero-result queries from the search logs, if you keep them. That shows whether model numbers, typos, or synonyms dominate, and it tells you what to index first. I haven't assumed any numbers.
- Check whether parts have aliases or cross-reference data. If they don't, "washer pump" vs "pump, washing machine" needs a synonym list. That's a data task and could take longer than the matching change.

I haven't looked at any code. If you share the repo, I can look at how search is built and propose the specific change.
