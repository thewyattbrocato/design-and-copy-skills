# Navigation and search for the library app

## Diagnosis
Two things are probably causing "can't find anything":
1. **Search is hidden and generic.** A corner icon that opens a blank box gives no hint of what can be searched or how.
2. **Five tabs flatten different kinds of use.** Catalog search is the core task, but it sits on the same level as Hours and Events, which are occasional lookups. Holds and Checkouts are both "my stuff" and are probably the most frequent return visits.

## Navigation

**Bottom bar: four tabs**
1. **Home** is a search field at the top, plus a "needs attention" strip (items due soon, holds ready for pickup) and shortcuts to Events and Hours.
2. **Search** (Catalog) opens with the keyboard ready and holds recent searches.
3. **My Library** has Checkouts and Holds as two segments in one screen, with a badge on the tab for "ready to pick up" or "due in 3 days or less."
4. **More** has Branches & Hours, Events, library card (barcode), account settings, and help.

If you want to keep five tabs, split it this way: Search, Checkouts, Holds, Events, Hours, with the card barcode reachable from a persistent button. I'd still choose four, because Hours and Events are lookups, not destinations people live in. Do check your analytics or run a quick test: if Events gets heavy use, promote it to a tab and move the card into More.

**Search is a field, not an icon.** Put a visible search bar ("Search books, movies, events, branches") at the top of Home and Search. Remove the corner icon. The Search tab is the same field with the keyboard open.

**Library card barcode** should be one tap from anywhere (a card icon in the header of My Library and Home). At the desk and at self-checkout, this is the thing people need fastest.

**Branch context.** Let people set a "home branch" once. Use it for default hours, pickup location on holds, and "available at my branch" filtering.

## Search while typing

**Empty focused field (before typing):**
- Recent searches (clearable)
- A few quick filters: Available now, My branch, Books / eBooks / Audiobooks / DVDs
- Shortcuts: "Scan a barcode / ISBN" and a mic for voice input

**After 2 characters, show suggestions in grouped sections, updating on each keystroke (debounce about 150–250 ms):**
1. **Title and author completions** (top 4–5), matched by prefix and also by word anywhere in the title
2. **Other things:** a branch ("Eastside Branch hours"), an event ("Toddler Storytime"), or a page ("Renew items")
3. **"Search all for 'xyz'"** as the last row, always present

Tapping a suggestion goes straight to that item or page. Pressing Search runs the full query.

**Typo tolerance and normalization.** Ignore case, accents, and punctuation, and handle initial articles ("the heron" = "heron"). Match one or two character errors ("hallie porer"), and show the corrected results with "Showing results for *hallie porter*. Search instead for *hallie porer*."

**Results screen:**
- Each row shows a cover, title, author, format, and a **status line**: "Available at Eastside" or "3 holds on 2 copies". The action button follows the status: **Place hold** or **Hold** for unavailable titles, **Borrow / Read now** for eBooks.
- Format chips across the top (All, Books, eBooks, Audio, DVD) and a Filter button for availability, branch, language, audience (adult/teen/kids), and publication year.
- Default sort is relevance. Offer a sort by newest or by availability.
- Keep the query and filters in the field so people can edit rather than start over.

## When nothing is found

Never show a bare "No results." Escalate by cause:

1. **Likely typo or near match:** auto-correct as above, or "Did you mean…?"
2. **Filters excluded everything:** "No results with *Available now* + *Eastside*." Show the removable filter chips, and a one-tap "Clear filters" button. Show how many results there would be without them ("42 results at all branches").
3. **Truly nothing in the catalog:**
   - Say so plainly: "We couldn't find 'xyz' in our catalog."
   - Offer tips: check spelling, try fewer words, search by author only.
   - Offer **Request this title** (purchase suggestion) and **Interlibrary loan**, if the library offers them. This is the library-specific way out of a dead end.
   - Offer "Ask a librarian" (chat, phone, or email link).
4. **Search failed (offline or server error):** Different message from the empty case, with Retry. Keep the user's text. Don't say "no results" when the real problem is connectivity.

Also search events and branches in the same query so that "storytime" or "Main Street" doesn't dead-end in a catalog that doesn't contain them. Show those as a separate section below catalog results, or as a tab (Catalog | Events | Branches).

## Summary of main screens

| Screen | Key content |
|---|---|
| **Home** | Search field, needs-attention strip (due soon, ready for pickup), shortcuts to Events/Hours, card button |
| **Search** | Focused field, recents, quick filters, scan/voice, live grouped suggestions, results with status and hold action |
| **My Library** | Checkouts / Holds segments, renew and renew-all, hold position and pickup branch, tab badge |
| **More** | Branches & Hours, Events, card, account, help |

## How to check it works
Test with 5 or so people on a few tasks: "Find a book you want and put it on hold," "Renew what's due," "When does the closest branch close today?", and "Find a kids' program this weekend." Watch for hesitation at the first tap. Also review your top failed searches (zero-result queries) every month. They tell you what to fix in synonyms, spelling tolerance, or collection requests.
