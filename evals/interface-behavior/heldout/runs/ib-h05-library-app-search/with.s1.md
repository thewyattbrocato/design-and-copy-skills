**Assumptions:** The users are the general public, from teens to seniors. They're on phones, use the app occasionally (a few times a month), and often have one errand in mind, like "is this book in?", "when is my hold ready?" or "when does Eastside close?". So I've designed for first-time clarity. Please correct me if the five tabs aren't what I've guessed.

## Navigation

- **Keep five tabs, but make them match the errands.** Use Search (home), Checkouts, Holds, Branches and Events. Every tab has a text label and the current tab is highlighted. The bar stays visible on every top-level screen.
  - *Why:* Five peer destinations fit a tab bar. The "can't find anything" problem is mostly the search entry, not the tab count.
- **Show state on the tabs.** Checkouts gets a badge when something is due within a few days (assumed 3, adjustable). Holds gets a badge with the number ready for pickup. The badge is a number, not just a color.
  - *Why:* The two most common questions get answered without opening anything.
- **Search is the top of the home screen, not an icon.** Put a full-width field labeled "Search books, movies, and more" at the top of the Search tab. Put a barcode/ISBN scan button inside the field.
  - *Why:* A corner icon hides the main feature of the app.
- **Search is reachable from every other tab.** Tapping the Search tab while already on it focuses the field. On Checkouts, Holds, Branches and Events, a pull-down or a visible field at the top searches within that tab (for example, filtering your own checkouts by title).
- **Back preserves place.** Going back from a book's detail page returns to the same results, scroll position and filters. Every book, branch and event has a shareable link.
- **Remember the home branch.** Ask once, in context, the first time availability matters ("Which branch is yours?"). Show it beside the results, for example "Showing availability at Eastside · Change". It is stored per device, with a reset in the account screen.

## Search: before typing

On focus, before any typing, show:
- Recent searches, each with a remove control.
- Quick shortcuts: "Available now at Eastside," "New this month," "Audiobooks," "Kids."

## Search: while typing

- **Start suggesting after 2 characters.** Update live and keep the keyboard and scroll position stable.
- **Group suggestions by kind**, with a small label for each group:
  - Titles
  - Authors
  - Subjects/series
  - Your items (matches in your holds and checkouts)
  - Branches and Events (matches such as "story time" or "Eastside")
- **Be tolerant.** Handle typos, missing punctuation, partial titles and author-first names. Also match what people remember: author, series, subject, narrator, ISBN, and the exact phrase "large print".
- **Tapping a suggestion goes straight to that thing.** A title opens the book, an author opens that author's results, and a branch opens its hours. Pressing Search/Return runs the full query.

## Search: results

- **Each row shows what people came for.** Cover, title, author, format, and availability at the home branch ("2 of 3 available at Eastside" or "Hold queue: 4"). A **Place hold** or **Hold** button sits on the row, so most holds need no detail page.
- **Placing a hold does not need a confirmation dialog.** Do the action, change the button to "On hold · #5 in line", and offer **Undo** in a toast. Use the same pattern when canceling a hold.
  - *Why:* Holds are cancelable, so a dialog would only slow people down.
- **One "Refine" button** holds sort and filter together. Filters: format, available now, branch, language, audience, and year. Active filters show as removable chips above the results, with the result count. Choices show counts, so no choice leads to zero.
- **Keep sort and filter across screens**, and reset them with one "Clear all" control.
- **Use "Load more" or paging with a position marker** rather than endless scrolling. People compare items and need to return to a place.

## Search: when nothing is found

Say what happened and give a next step. Pick the first that applies:

1. **A filter caused it.** "No results with Available now + Large print." Offer one tap to remove the most restrictive filter, with the new count.
2. **Probable typo.** "Did you mean *Hamilton*?" and show those results below, not behind another tap.
3. **Only other branches have it.** "Not at Eastside. 3 copies at other branches." Offer to place a hold with pickup at Eastside.
4. **The library doesn't own it.** Say so plainly and offer **Request this title** (purchase suggestion or interlibrary loan, whatever the system supports). Pre-fill the form from the search text.
5. **Matches elsewhere in the app.** Show "0 books, but 2 events match 'knitting'" with links to them.

Never show a blank screen or "No results" on its own.

## The other screens

- **Checkouts:** Sort by due date, soonest first. Each row has the due date and a visible **Renew** button. Renewing is reversible only in the sense that nothing is lost, so just do it and show the new due date in the row. If renewal is blocked (someone is waiting, or renewal limit hit), say that in the row, in words, instead of a failure dialog.
- **Holds:** Group by "Ready for pickup" (with pickup-by date and branch), then "In line" (with position). Cancel is a visible row action with Undo.
- **Branches:** Open with "Open now" at the top, starting from the home branch, then nearby branches sorted by distance if location is allowed (ask in context, and work without it). Show today's hours first, with a status like "Open until 8 pm", then a link to the full week and any holiday exceptions.
- **Events:** Default to "This week" at the user's home branch. Provide a list view (not just a month grid), and filters for age group, branch and type. Show these as chips with counts. Add to Calendar is one tap, and Register/Cancel use the Undo pattern when registration is not limited. If an event is full, say so and offer a waitlist.

## Open questions and placeholders

- Due-soon badge threshold: 3 days is an assumption.
- Whether the system supports interlibrary loan or purchase requests: shapes the "not owned" fallback.
- Whether holds can be placed for pickup at any branch: shapes the "other branches" fallback.

## Accessibility

- All actions are reachable by screen reader and keyboard, with visible focus.
- Undo toasts are announced politely and stay long enough to read (around 6 to 10 seconds, extendable).
- Availability and badges use text, not just color.
- Suggestion groups are announced with their labels and result counts.
