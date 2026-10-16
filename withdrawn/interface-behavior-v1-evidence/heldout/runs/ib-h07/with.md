**Assumptions (adjust if wrong):** Shop staff on a desktop or counter machine use it many times a day, often mid-conversation with a customer. They know the appliances but not the catalog's part names. A lookup is usually several parts in a row, such as checking a few candidates against a model.

## What's wrong

The clunkiness is one problem. The tool makes staff redo work and gives them no feedback. In order of damage:

1. **Search fails on how people actually ask.** Matching only exact words in the part name means a model number, a typo, or "washer pump" returns nothing. Staff think in model numbers and plain words, and the catalog uses its own wording. A failed search reads as "we don't have it" when the part probably exists. This is the biggest cause of the feeling.
2. **"No results found." is a dead end.** It doesn't say what was searched, what was tried, or what to do next.
3. **Back destroys state.** Filters clear and the list jumps to the top. Comparing candidates is the core task, and every look at a part costs the user their place. The more careful the person is, the more it hurts.
4. **No way to move between results from a part.** Each comparison takes a round trip: Back, find your place again, re-apply filters, open the next one.
5. **No location on the part page.** You can't see what you searched for or how you got there.
6. **Search only on the home page.** Every new lookup means navigating home first.

## What to fix first

**Fix 1: make search forgiving.** This is the highest-impact change, and every other fix is wasted if the search returns nothing.

- When someone searches, match across part name, model number, part number, brand, and aliases or synonyms (for example "washer" and "washing machine"). Tolerate typos and match word parts, so "pump washer" finds "pump, washing machine". Because it is a catalog lookup, rank exact model and part-number hits first.
- If it finds nothing, show what was searched ("No parts match 'wsher pmp'"). Offer the closest alternatives ("Did you mean…"), a looser retry such as dropping a word, and a way to clear the filters if any are on.
- Log searches that return nothing (queries only). This builds your synonym list from real usage. I have no figures on how often this happens today, so measure it.

**Fix 2: keep state when navigating.** This should come right after, and it may be cheap.

- When someone presses Back from a part, restore the same filters, the same sort, and the same scroll position. Put the search and filters in the URL so Back, reload, and sharing a link all work.
- Opening a part should not cost the user their place.

**Then, in order:**

3. **Part page shows context and moves between results.** Add a visible "‹ Results for 'washer pump' · 3 of 24 ›" strip. Previous and next buttons should work, with arrow keys as a shortcut, and the label should show the active filters. This is also the location display. Make Esc or the "Results" link return to the list with state intact. If the user arrived by a direct link with no list, hide the strip.
4. **Search box on every page.** Put it in the header. Keep the current query in it on the results and part pages. `/` focuses it.
5. **Optional later:** open a part in a side panel next to the list rather than a full page. That would make Fix 3 mostly unnecessary, but it is a bigger change, so try the cheaper fixes first.

## Why this order

Fix 1 removes the dead ends, since nothing else matters when the search finds nothing. Fix 2 stops the repeated loss of work. Fixes 3 and 4 reduce the number of steps per lookup. Test it by watching two or three staff do real lookups before and after. If they stop saying "clunky," it worked.

Two things I don't know: whether the catalog already stores model numbers and aliases per part (this decides how hard Fix 1 is), and how the results page is built (this decides whether Fix 2 is a small change or a rework). If you give me access to the code, I can scope both.
