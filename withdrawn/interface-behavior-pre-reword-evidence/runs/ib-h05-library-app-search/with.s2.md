**Assumptions:** The users are the general public, from teens to seniors, on phones, often one-handed and in short sessions. Most are returning patrons who do the same few jobs (renew, check a hold, find a book). Some are first-timers, so labels stay visible. Library cards are already tied to accounts. The numbers below are starting values to test, not measured.

## Navigation

**Keep five tabs, but make them match what people come to do.**
- Tabs: **Home, Search, Holds, Checkouts, More**.
- Branch hours and Events move under Home and More. Home shows today's hours for the user's branch and the next few events, each with a "See all" link. More holds the full branch list, the events calendar, card/account and settings.
- Why: Search becomes a tab rather than a corner icon, because finding things is the main job. Holds and Checkouts are the account tasks people return for. Hours and events are lookups, not destinations people visit daily.
- The current tab is highlighted and its title is shown. Tapping the active tab returns to that tab's top level. Back returns to the same scroll position, query and filters.
- Badges sit on tabs: the count of holds ready for pickup, and the count of items due within 3 days (assumed threshold). That puts urgent state where people are already looking.
- Every screen has a shareable link (a book, an event, a branch), so notifications and email can open it directly.

## Home

- Top: a **visible search field**, not an icon. Tapping it opens the Search tab with the keyboard up.
- Below it, in order of urgency: "Ready for pickup" (holds, with the branch and the pickup-by date), "Due soon" (with a one-tap **Renew**), then "Open today" for the user's home branch, then upcoming events.
- Sections with nothing to show disappear rather than showing empty cards. Signed-out users see search, hours and events, and a single "Sign in to see your holds."
- Home branch is remembered from the last one used or chosen, shown beside hours ("Showing Eastside · Change"), and resettable.

## Search

**Before typing (on focus):**
- Show recent searches, each removable, and a "Scan a barcode/ISBN" shortcut.
- Show a few browse entries ("New books", "Audiobooks", "Kids", "Events this week") for people who don't have a title in mind.

**While typing (from the first character, results update live):**
- Suggestions are grouped by kind, so one box covers everything: **Books & media** (title, author, series), **Events**, **Branches**, **Help** (e.g. "renew," "library card"). The most likely group is first, with 2–3 rows each and a "See all" link.
- Matching tolerates typos and partial words ("hallie porer", "grayson"). It also searches what people remember: author, subject, series, narrator, and not only the title.
- Suggestions are debounced lightly (about 150–200 ms, a starting value) so the list doesn't jitter. Tapping a suggestion goes straight to that item. Pressing the keyboard's search key opens the full results.
- Each book row shows cover, title, author, format, and **availability at the user's branch** ("2 of 3 available at Eastside" or "Hold · 4 waiting"), so people don't have to open the book to learn if it's worth it.
- Show a thin loading state in the list if the network is slow, and keep the last results visible rather than blanking them.

**Full results:**
- The result count is shown, and active filters appear as removable chips.
- One **Refine** button holds both sort and filter: format (book, ebook, audiobook, DVD), availability ("Available now" / "At my branch"), language, audience (adult, teen, kids), and sort ("Best match," "Newest," "Most popular"). Filters apply live, and each option shows its count so a choice never leads to zero.
- "Available now" is the one filter worth a chip on the surface, since it's the most common need. Filters and sort are remembered across searches in the session and can be reset in one tap.
- Place a hold directly from a result or its detail page: one **Place hold** button, with the pickup branch prefilled from the last one used and shown beside the button ("Pickup: Eastside · Change"). No confirmation dialog. After placing, the button turns into "On hold · #3 in line", and an Undo toast (a few seconds, announced to screen readers) cancels it. If signed out, sign-in appears at this point and then returns the user to the same hold.

## When nothing is found

Respond according to the reason:
- **Filters caused it:** "No results with *Audiobook* + *Available now*. Remove *Available now* (24 results)." One tap relaxes the filter. Offer the most restrictive filter first.
- **Spelling:** "Showing results for *Hunger Games*. Search instead for *Hunger Gams*."
- **Genuinely not in the catalog:** Say so plainly, then offer next steps in order: related titles or authors, "Search all county branches/ebooks" if the search was scoped, **Request this title** (purchase suggestion) or **Interlibrary loan** if the library offers them (placeholder: confirm which services exist), and "Ask a librarian" with the branch phone or chat.
- **Event or branch searches that return nothing:** offer to widen the date range ("Nothing this week. Show next month") or list all branches.
- Keep the user's query in the box, editable, so a small fix is quick. Never show a bare "No results found."

## Holds and Checkouts

- **Holds:** grouped as **Ready for pickup** (first, with the pickup-by date and branch), then **Waiting** (position in line), then **Paused**. Each row has its actions visible: Pause/Resume, Change pickup branch, Cancel. Cancel is undoable with a toast, not a confirmation dialog.
- **Checkouts:** sorted by due date, with the soonest at the top and overdue items marked with text as well as color. Each row has a visible **Renew**. A "Renew all" appears when more than one item is eligible and shows the count ("Renew 3"). If an item can't be renewed (someone is waiting), say why on the row ("Can't renew: 2 people waiting") instead of failing after a tap. Results are reported in place on the row ("Renewed · due Nov 3").
- Ebooks and audiobooks sit in the same list with a format label, and "Return early" is available where the platform supports it.

## Branches and events

- **Branches (under More, and on Home):** open now/closed now is shown first ("Open until 8 pm"), with the full week on tap, and holiday closures flagged at the top. Actions: call, directions, set as my branch. Sort by distance if location is allowed; otherwise by name, with no demand for permission up front.
- **Events:** a list by date, with a filter chip row for branch, audience (kids, teens, adults) and type, remembered across visits. Week/month calendar view is a toggle, not the default, since most people scan a list. Each event has **Add to calendar** and, if registration is needed, **Register** on the card.

## Cross-cutting rules

- Everything works with a keyboard/switch control and screen reader. The tab bar, chips, and Undo toasts are focusable and announced, and the toast stays long enough to read, with an extendable time. Availability and overdue status never rely on color alone.
- Offline: show the user's last-synced holds and checkouts with a "Last updated" note. Library card barcode is always available from Home and More, offline included, since it's the thing people need at the desk.
- Sign-in is requested only when a user does something that needs an account, and is remembered on the device.

## What I'd check first

I'd test with five or six real patrons on this task list: "find a book and check it's at my branch," "see what's ready for pickup," "renew something," "find a storytime this weekend." The unknowns I've left as placeholders are which services exist (interlibrary loan, purchase requests, chat) and how your catalog system exposes branch-level availability. Live availability in suggestions depends on the latter being fast enough.
