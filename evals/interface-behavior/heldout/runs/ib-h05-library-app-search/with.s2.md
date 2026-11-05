**Assumptions:** Patrons of all ages and tech comfort, on phones, opening the app occasionally (to check a hold, find a book, check hours). Treat each visit as close to first-time. Nothing here uses usage data, since none was given.

## Navigation

- **Make search a field, not an icon.** The top-corner icon is the main reason people can't find things. Put a full-width search field ("Search books, movies, events…") at the top of the Search tab, which is the landing screen. Tapping it opens the search screen below. Because the field is visible, nobody has to guess what the icon does.
- **Use four tabs with text labels, not five:** **Search**, **My Items**, **Branches**, **Events**.
  - Merge Holds and Checkouts into **My Items**, with a two-segment switch at the top: *Checked out (n)* and *Holds (n)*. Both answer "what do I have with the library?" and share the same actions (renew, cancel, pick up).
  - The tab shows a badge when a hold is ready for pickup or something is due soon. That state shows where people already look, so they don't have to open anything.
  - If you'd rather keep five tabs, that's still within the 3–5 range. The merge is a recommendation, not a requirement.
- **Show location.** The current tab is highlighted and each screen has a title. Back returns to the same scroll position, filters, and typed query. Every screen is linkable, so a notification like "Your hold is ready" opens straight to that hold.
- **Sign-in is deferred.** Search, Branches, and Events work without an account. My Items asks for the library card number the first time it's opened, and the app remembers it on the device. The card sign-in is the one thing worth asking for up front.
- **Branches opens to the nearest branch,** with today's hours at the top, using location if the person allows it. Otherwise it uses their last-viewed or "home" branch. Show "Open until 8 pm" or "Closed, opens 9 am tomorrow" rather than a table of hours. Tapping a branch shows the full week, holiday closures, and a map link.
- **Events opens to this week,** filterable by branch and age group (kids, teens, adults), shown as chips. A saved "My branch" preference carries over, with a visible label and an easy way to clear it.

## Search

**Before typing (on focus):**
- Show recent searches, each with a remove control.
- Show a few shortcuts below them: *Available now*, *New arrivals*, *E-books & audiobooks*.
- Don't show an empty screen.

**While typing:**
- Show suggestions after the first couple of characters, grouped by kind: **Titles**, **Authors**, **Subjects/Series**, **Events**, **Branches**. A search for "story" can then find a story-time event and a book without the person choosing a scope first.
- Tolerate typos and partial words ("hallie porer" still suggests Hallie Porter). Match what people remember, such as author, series, subject, or ISBN, not only the title.
- Tapping a suggestion goes directly to that thing: an author page, a title, or an event. Tapping the keyboard's search key runs a full search.
- Show a small availability hint on title suggestions ("Available at 2 branches" / "Waitlist"), so the person can often decide without opening the record.
- Keep the field and keyboard stable, and don't reorder suggestions after they appear.

**Results:**
- Show the count and active filters as removable chips, e.g. *Available now ×*, *Large print ×*.
- One **Refine** button holds sort and filters together: format (book, e-book, audiobook, DVD), availability, branch, language, and audience. Each option shows a count, so a choice never leads to zero.
- Default to **My branch** availability, with the assumption shown on a chip that can be removed.
- Each result shows cover, title, author, format, and a plain status with one action: **Place hold**, **Read now**, or **Join waitlist (n ahead)**. Placing a hold uses the saved pickup branch, shown beside the button and changeable there. It's undoable with a toast ("Hold placed at Main — Undo") that lasts about 6–10 seconds and is announced to screen readers.
- Filters and sort persist when the person goes back from a record.

**When nothing is found:**
1. State what was searched and which filters were active: "No results for 'dune' with *Available now* and *Eastside branch*."
2. Offer one tap to relax the filters: **Remove "Available now"** (shows how many results that gives).
3. If the query itself is the problem, offer a "Did you mean…?" correction and show the closest matches.
4. If the title simply isn't owned, offer **Suggest a purchase** or **Request via interlibrary loan**, depending on what your system supports.
5. Keep the search field filled in and focused, so editing is one tap.

The same rules apply if the catalog is unreachable. Say it's a connection problem, not "no results," and offer a retry. Recent searches and downloaded items should still be viewable offline.

## My Items

- Sort checkouts by due date, soonest first. Mark due-soon items with a text label ("Due in 2 days"), not color alone.
- Put **Renew** on each row, plus **Renew all**. Renewal is reversible only if the library allows it, so if a renewal can't be done (e.g. someone else is waiting), say so in the row instead of failing after the tap.
- Order holds as **Ready for pickup** first, with the pickup-by date and branch, then the rest with queue position.
- **Cancel hold** is undoable by toast for a few seconds. Release the hold only after the Undo window closes. Anything the library can't restore, such as losing a place in a long queue, should say so specifically in a confirmation naming the title and position.

## Open questions (placeholders)

- Does the catalog system support type-ahead suggestions through its API, or only full queries? That decides how rich the "while typing" step can be.
- Whether renewals, holds, and cancellations are reversible on the library system's side.
- Which formats and filters actually exist in the catalog data.
