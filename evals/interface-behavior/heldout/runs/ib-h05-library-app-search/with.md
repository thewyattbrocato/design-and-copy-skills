**Assumptions:** Patrons are mostly occasional, one-handed phone users in short sessions, with some regulars who check holds and due dates. Nothing here is based on usage data. The five tabs are Search (icon), Holds, Checkouts, Hours and Events.

## Navigation

- **Make search a destination.** The top-corner icon is the likely reason people can't find anything. Replace it with a persistent search field at the top of the first tab, labeled "Search books, movies, events, branches". It is always visible, never behind an icon.
- **Use four tabs, not five: Search, My Items, Branches, Events.**
  - Holds and checkouts are one "what do I have" question. Put them under My Items as a two-segment control, "Checked out (n)" and "Holds (n)", so each tab doesn't need its own badge.
  - Remember the last segment used. Open on Checked out when something is due soon.
  - Show a badge on the tab when a hold is ready or an item is due soon. Show state in the tab, not in a popup.
- **Put the library card in My Items.** Add a "Show my card" button at the top that opens the barcode full-screen. This is the most common reason to open the app at a desk. Account and settings go in a labeled secondary entry, not a tab.
- **Always show where the patron is.** Highlight the active tab and give each screen a title. Back returns to the same scroll position, query and filters. Every screen, including a result or an event, has a shareable link.
- **Remember a home branch.** Ask once, in the first search or hold, and show it beside the control ("Showing availability at Eastside · Change"). Branches opens on that branch, and Events and availability default to it.

## Search

**On focus, before typing**
- Show recent searches, each removable.
- Show the home branch's "Ready for pickup" and "Due soon" items.
- Show a few quick links such as New arrivals and Events this week, if the library supplies them.

**While typing**
- Show suggestions after the first character or two, grouped by kind:
  - Titles and authors
  - Series and subjects
  - Events
  - Branches and services
- Tolerate typos and partial words. Accept an ISBN or a barcode pasted into the same box.
- Tapping a suggestion goes straight to that item, event or branch. Pressing Search runs the full query.
- Keep the keyboard open and the list stable. Don't reorder suggestions under the thumb as more letters arrive.

**Results**
- Search all kinds of content at once. Group results as Catalog first, with "Events (2)" and "Branches (1)" as short rows below or as filter tabs. Don't make people choose a scope before searching.
- Each catalog result shows the cover, title, author, format and availability at the home branch ("Available at Eastside" or "3 holds · est. wait [placeholder from system data]"). Include a Place hold button on the row so patrons don't have to open the detail page.
- Use one "Refine" button for sort and filters. Filters:
  - Format
  - Available now
  - Branch
  - Language
  - Audience
  - Year
- Show active filters as removable chips with the result count. Show counts on filter options so a choice never leads to zero. Apply filters live. Remember the sort and filters within a session, and clear them when a new query starts.
- Use "Load more" with a position marker rather than infinite scroll, so Back lands where the patron left.

**Placing a hold**
- Use the home branch and the saved pickup branch as defaults, and show them beside the button.
- Make Place hold one tap, with an Undo toast ("Hold placed · Undo"). Cancelling is also undoable until the library processes it.

## When nothing is found

1. **Spelling.** If a likely correction exists, show "Showing results for *x*. Search instead for *y*."
2. **Filters caused it.** Name the cause: "No results with Large print + Available now. Remove Available now (14 results)". Relax in one tap.
3. **Still nothing.** Say so plainly and offer next steps that work:
   - Check other formats or branches.
   - Search by author or subject only.
   - Request that the library buy it or get it from another library, if the system supports it. Show only the routes the library actually offers.
   - Ask a librarian, with a call or chat link.
4. **Cross-type matches.** Show any event or branch matches even when the catalog has none ("1 event matches 'knitting'").
5. **Never show a bare "No results"** or clear what the patron typed. Leave the query editable.

**If search itself fails** (offline or slow): say so in place, keep the query, and offer Retry. Recent searches and My Items should still show cached data with a "Last updated" time.

## Quick checks

- Search is reachable in one tap from every tab (the top field on Search, or the tab itself).
- Nothing asks the patron what the app can remember: branch, pickup location, last segment.
- Every hold or cancel can be undone. No "Are you sure?" and no success dialogs.
- Everything works with the keyboard and screen readers. Undo toasts are announced and stay long enough to read (starting value: 6–10 seconds, extendable). Availability uses text, not only color.

**Open question:** I assumed the library can supply availability per branch, hold-queue estimates and a barcode for the card. If it can't, drop those rows rather than showing blanks.
