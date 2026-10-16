# Library app: navigation and search

**Assumptions:** The users are the general public, from teens to seniors, on phones, with mostly short, goal-driven sessions. Many open the app once or twice a month, so design for people who may be half-remembering how it works. Where I give numbers, they're starting values to test, not findings.

## Navigation

**Replace the five tabs with four, and put search first.**

| Tab | Contains |
|---|---|
| **Search** (home) | Search field at the top, always visible. Below it: "Ready for pickup" and "Due soon" cards, then recent searches. |
| **My Items** | Checkouts and holds in one screen, with a segmented control: *Checked out (n)* / *On hold (n)*. |
| **Branches** | Hours and location. |
| **Events** | Calendar. |

- **Search becomes a tab and a field, not a corner icon.** People come to a library app to find things, and a hidden icon is the likely cause of "can't find anything." Tapping the Search tab focuses the field. Tapping it again while on results returns to the top.
- **Merge holds and checkouts.** People think "what do I have?", not "which database table?" Put counts and a badge on the tab: pickup-ready holds and items due within 3 days (assumed threshold).
- **Home surfaces what's urgent** so most account questions are answered without any navigation: "2 holds ready at Eastside, pick up by Oct 14" and "1 item due Friday." Each card links straight to the item.
- **Always show location.** The active tab is highlighted with an icon and a label, and the screen title is visible. Back and tab-switching restore scroll position, search text, and filters. Every screen has a link, so a branch page or event can be shared.
- **Remember the user's branch.** Ask once, in context, the first time it matters: when placing a hold or opening Branches. Show it beside the control ("Pickup at: Eastside · Change"). Branches opens with "Open now / Closes at 8 pm" for that branch first, and the others are one tap away. Hours for holidays and closures should show in place, not on a separate page.
- **Sign-in only when needed.** Search, branches, and events work signed out. Prompt at "Place hold" or "My Items," and return the person to what they were doing.

## Search: before typing

On focus, show **recent searches** (removable individually, with a "Clear" option) and a few quick entry points, such as "New this week," "Available now," and "Audiobooks." Don't show an empty screen with a keyboard.

## Search: while typing

- **Suggestions start at 2 characters** (a starting value), update live, and are grouped by kind:
  - *Titles*, *Authors*, *Series/Subjects*, and *Events & Branches* (so "story time" or "Eastside" finds the right place instead of a book dead end).
  - Each group shows 2–3 rows, and the top group is whichever best matches the text.
- **Tolerate typos and variants**: "hallie porer," missing articles, and author name order ("Ravenhill, J.K." / "J.K. Ravenhill"). When the app corrects, say so: *Showing results for "hallie porter"* with a link to "Search instead for 'hallie porer'."
- **Suggestions never replace results.** Tapping a suggestion goes straight to that item or filtered list. Pressing Search on the keyboard runs the full query.
- Index what people remember: title, author, series, subject, ISBN, and format words like "large print" and "audiobook."

## Search: results

- **Each result shows what people decide on**: cover, title, author, format, and availability *at the person's branch* ("Available at Eastside" or "3 holds · est. wait [placeholder]"). Show the primary action on the row, **Place hold** or **Borrow**, so the user doesn't need the detail page to act.
- **One "Refine" button** holds sort and filters together, with active filters as removable chips and a live result count. The filters are *Format, Available now, Branch, Language, Audience (adult/teen/kids)*. Facets show counts so a choice never leads to zero. Default sort is relevance, with "Available now" one tap away. Sort and filters persist across navigation and within the session, and a visible "Reset" is always on hand.
- **Paging:** use "Load more" with a position marker instead of infinite scroll, so back-navigation returns to the same spot.
- **Placing a hold** uses the remembered pickup branch and doesn't ask for confirmation. The result is shown in place ("Hold placed · Pickup at Eastside"), with a toast offering **Undo** (cancelling a hold is harmless, but undo saves a trip into My Items). Success makes no modal.

## Search: when nothing is found

Don't show a bare "No results." In order of preference:

1. **If filters caused it:** *"No results for 'dune' with Available now + Large print."* Show the chips that did it and a one-tap **Remove 'Large print'** (the filter that most expands the results). Use the filter that unlocks the most results first.
2. **If a spelling guess is possible:** *"Did you mean 'dune messiah'?"* Tapping it runs that search.
3. **If a looser match exists:** show "Results for similar words" under a clear divider, so users don't mistake loose matches for exact ones.
4. **If the library really doesn't own it:** say so plainly, then offer the next step. Show **Suggest a purchase** and **Request from another library** (interlibrary loan) as the primary actions, if the system supports them. Include **Search events & branches for '…'** since the answer may be a program, not a book.
5. **Offline or error:** a different message from "nothing found," which says the search didn't complete and offers **Try again**. Keep the typed text and any recent results.

Never clear the search field on a failed query, since the user needs to edit it.

## Accessibility

- All tabs, chips, and suggestions have visible focus and labels (the tab icons always have text).
- Suggestions are announced as a polite live region ("5 suggestions"), and result counts are announced after filtering.
- Undo toasts stay long enough to read (the timeout is extendable) and are announced to screen readers.
- Availability is conveyed by text as well as color ("Available" / "All copies out"), and tap targets are large enough for older users.

## What to test first

1. Do people find the Search tab, and does it reduce the "can't find" complaints? (Check by asking them to find a book, their hold, and Saturday's story time.)
2. Whether merging holds and checkouts confuses anyone who thinks of them separately.
3. Which zero-result recovery gets tapped most.
