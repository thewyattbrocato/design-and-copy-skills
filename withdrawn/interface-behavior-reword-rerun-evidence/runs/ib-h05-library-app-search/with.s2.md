# Navigation and search spec: county library app

**Assumption:** Most users are patrons on a phone, in short sessions. They are usually in one of two moments: "find a book or check on my stuff" and "when does the branch close." They are often one-handed, and some are older or less familiar with apps. I'm designing for the tenth use, with labels visible and nothing hidden. The numbers below are starting values, not measured.

## Navigation

**Keep five tabs, but make them match what people come to do.** Five is the upper limit for a tab bar, and these destinations are all peers. The problem is more likely the search entry point and the tab contents.

| Tab | Contents |
|---|---|
| **Search** (first, opens by default) | Search field at the top of the screen, always visible. Below it, before typing: recent searches, then browse shortcuts (New arrivals, Audiobooks, Kids, Staff picks). |
| **Holds** | Ready for pickup first, then waiting, with queue position. |
| **Checkouts** | Sorted by due date, soonest first. Each item has a Renew button. |
| **Branches** | My branch first, with open or closed right now, today's hours, and a map. |
| **Events** | Filtered to my branch by default. |

- **Replace the corner icon with a real search field on the Search tab.** An icon opening a blank box is why people can't find things. A visible field says what the tab is for.
- **Show badges on tabs when something needs attention.** Examples are "2 ready for pickup" on Holds and "1 due tomorrow" on Checkouts. This answers the most common question without opening anything.
- **Show a compact search field at the top of Holds, Checkouts, and Events once the list is longer than a few items.** It filters that list only.
- **Remember "my branch"** and use it as the default for hours, events, and pickup. Ask once at first run, show it on screen, and let people change it in one tap. Don't make them re-pick it on every screen.
- **Keep location visible.** Highlight the active tab and give each screen a title. Pressing back or switching tabs returns to the same scroll position, query, and filters. Tapping the active tab scrolls to the top, and tapping it again clears the search.
- **Keep sign-in out of the way.** Hours, events, and catalog search work without signing in. Holds and Checkouts ask for sign-in in place, with a short line saying why, and then return the person to where they were.

## Search while typing

- **On focus, before typing:** show recent searches, each with a remove control. Show nothing invented, such as trending items, unless the library has real data.
- **While typing, from the first character,** show suggestions grouped by kind:
  - **Titles, authors, and series**, tolerant of typos and partial words ("halie portr" still finds Hallie Porter).
  - **Subjects and formats**, such as "Large print" or "Audiobook."
  - **Other tabs:** "Branch: Eastside" and "Event: Toddler story time." This lets one search box reach all five areas, so people don't have to guess which tab holds what.
  - **Items I already have.** If a title is in my Holds or Checkouts, show that status on the suggestion.
- **Index what people remember,** not only the title. That means author, series, subject, ISBN, and words from the description.
- **Pressing Search** opens full results. The query stays in the field and is editable.

## Results

- **Each result shows:** cover, title, author, format, and availability in plain words ("Available at Main", "3 holds, about [N] weeks"). Don't force people to open a record to learn whether they can get it.
- **One primary action per result:** "Place hold" or "Borrow now" (for digital). It's visible on the row, not hidden in a long-press.
- **Placing a hold** uses the remembered pickup branch, shown beside the button ("Pickup: Eastside · Change"). It happens in one tap, with a short confirmation in place and an Undo (cancel hold) for at least 6 to 10 seconds. No "are you sure" dialog.
- **One "Refine" control** holds sort and filters together: format, availability, branch, language, audience (adult, teen, kids). Show active filters as removable chips with the result count. Filter options show counts, so a choice never leads to zero.
- **Default to "Available now" off.** Many people want to place holds, so hiding unavailable items surprises them. Make it one tap to turn on.
- **Keep sort and filters** across navigation within the session.

## When nothing is found

Say what was searched, then work in this order:

1. **If filters caused it:** "No results for 'dune' with Audiobook + Eastside." Offer one tap to remove each filter, or "Clear all," and show the count each would give.
2. **If it's likely a typo:** show "Did you mean *Dune*?" and run that search.
3. **If the title isn't in the catalog:** show similar titles or the same author, then a clear route to **"Suggest a purchase"** or **"Request from another library"** (interlibrary loan), if the system offers those. Check that it does before including them.
4. **Always offer a human route:** "Ask a librarian," linking to the branch phone or chat.
5. **Never leave a blank screen** or a bare "No results."

If the search can't run (offline or server error), say so plainly, keep the typed query, and offer Retry. Don't show it as "no results." While offline, Holds, Checkouts, and Branch hours show the last-loaded data, labeled with when it was updated.

## Accessibility

- All controls are reachable by screen reader and keyboard, with visible focus.
- Announce suggestion counts and result counts in a polite live region ("12 results").
- Show availability and status as text, not color alone.
- Make touch targets large, and respect system text size.

## Checks to run with real users

- Give people five tasks: find a book and place a hold, see what's due, check Saturday hours, find a kids' event, renew an item. Watch where they hesitate.
- Review the library's actual "no results" search logs. They will show whether the problem is typos, missing titles, or users searching for non-catalog things like events and hours.
