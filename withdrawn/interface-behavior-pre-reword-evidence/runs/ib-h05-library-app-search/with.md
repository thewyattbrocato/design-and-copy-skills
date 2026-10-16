# Navigation and search for the library app

**Assumptions:** Patrons use phones, often one-handed, in short sessions (check a hold, find a book, check hours). Most return every few weeks. Many are older or not tech-savvy. Some are signed out or have no card yet, so the app should work without login for catalog, hours and events. Nothing here is based on usage data, so treat all numbers as starting values to test.

## Navigation

**Keep four tabs and make search the first.** The search icon in the corner is the main reason people can't find things, so search becomes a tab.

| Tab | Contents |
|---|---|
| **Search** (opens here) | Search field at the top, with browse shortcuts below it |
| **My Library** | Holds, checkouts, fines and card, in one place |
| **Hours** | Branches |
| **Events** | Calendar |

- **Why merge holds and checkouts:** Both answer "what do I have and what's due?". On My Library, a segmented control sits under a summary line such as "2 ready for pickup · 1 due Thursday". The same counts appear as a badge on the tab, so people see status without opening anything.
- **Signed-out My Library:** It shows a sign-in prompt, not an empty page. Everything else works without an account.
- **Location is always shown:** The selected tab is highlighted and labeled, and each screen has a title. Icons always carry text labels.
- **Back keeps your place:** Back returns to the same scroll position, query and filters. Every record, event and branch has a shareable link.
- **Tapping the active tab:** The first tap scrolls to top. A second tap resets that tab to its root.

## Search

**Before typing (on focus):**
- Show recent searches, each removable.
- Show a "Scan a barcode / ISBN" button.
- Below that, show browse shortcuts in plain words: "New this week", "Large print", "Audiobooks", "Kids".
- If the person is signed in and has an item ready, show a small "Ready for pickup" row.

**While typing, from the first character:**
- Show suggestions grouped by kind: **Titles**, **Authors**, **Subjects**, and **Library info** (branches, events, "renew", "library card").
- Tolerate typos and partial words. "hallie porer" should still suggest Hallie Porter.
- Match what people remember, not only titles. That means author, series, subject, and part of an ISBN.
- Search all content types together. "Storytime" returns events, "Main Library" returns the branch and its hours, and a book title returns books. Results are grouped under those same headings, so there's no need to pick the right tab first.
- Update suggestions live, and keep the previous ones on screen until new ones arrive, so the list doesn't flicker.
- Pressing search or Return opens a full results page. Tapping a suggestion goes straight to that item or filtered list.

**Results page:**
- Show the query in an editable field, so people can fix it without retyping.
- Show the result count.
- Each book result shows cover, title, author, format, and availability **at the person's chosen branch**: "Available at Eastside" or "3 holds, about N weeks" (a placeholder, since it depends on the catalog data). Availability is what people are really asking, so it shouldn't be hidden behind a tap.
- Put a **Place hold** button directly on the result, with the pickup branch prefilled from last time (see below).
- One **Refine** button holds sort and filters together: format, availability, branch, language, audience. Filters apply live. Active filters show as removable chips under the search field. Each facet shows its count, so a choice never leads to zero.
- Sort and filters are remembered across searches. The chips make this visible, and "Clear all" resets them.

**Remembered defaults:**
- Pickup branch defaults to the last one used, shown next to the Place hold button ("Pick up at Eastside · change").
- Place hold is undoable with a toast, "Hold placed · Undo", not a confirmation dialog. Holds can be cancelled, so nothing needs "Are you sure?".

## When nothing is found

Say what happened and offer a next step. Never show a bare "No results".

1. **Filters caused it:** "No results with *Large print* + *Available now*." Offer one tap to remove the most restrictive chip, with the count it would give ("Remove Available now · 14 results").
2. **Spelling:** If there's a close match, show "Showing results for *hallie porter*" and a link for the original spelling.
3. **Too specific:** Offer broader terms, such as the author alone or the first words of the title.
4. **Library doesn't own it:** Show **Suggest a purchase** and **Request from another library** (if the system offers interlibrary loan), with the query prefilled.
5. **Always:** A short line, "Ask a librarian", with the phone number and chat or email, and the branch hours.

If the search itself fails (offline or server error), say so and offer Retry. Keep the typed query and recent searches visible. Don't show "no results" for an error.

## Other screens

- **My Library:** Items due soonest are first. Overdue items are marked with text, not just color. Each row has a visible Renew or Cancel hold action. Renewing is undoable. If it's blocked, the row says why ("Another patron is waiting").
- **Hours:** Open with "Open now" and the nearest branch (ask for location permission only here, in context). Show today's hours first, with the full week on tap. Include the holiday closures. Allow a "favorite branch" that also becomes the default pickup branch.
- **Events:** Default to a list sorted by date, with a calendar-month view as an option. Filter by branch and audience (kids, teens, adults) with chips, and remember them. If there are no events, the same recovery rules apply: name the filter and offer one tap to relax it.

## Check before building

- Test the five most common tasks with people who haven't seen the app: find a book, place a hold, see what's due, check Saturday hours, find a kids' event. Watch whether they start at the Search tab.
- Review the search logs for the most frequent zero-result queries. They show which synonyms and typo fixes to add first.
- Confirm every action works with a screen reader and large text.
