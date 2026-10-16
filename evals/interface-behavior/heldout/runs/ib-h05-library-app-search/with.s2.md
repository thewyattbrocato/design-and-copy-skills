**Assumption:** The users are the general public on phones, using the app occasionally and in short sessions. Ages and tech comfort vary, and most people arrive with one job: find a book, check a due date, or see when a branch closes. Everything below is designed for that, not for power users.

## Navigation

- **Keep the bottom bar, but make Search the home tab.** The search field is a visible, full-width box at the top of the first screen, with the placeholder "Search books, movies, events…". The corner icon is the main reason people can't find anything, so remove it.
- **Tabs, left to right:** Search, My Items, Events, Branches, Card.
  - **My Items** combines Checkouts and Holds behind a two-segment control. Both are "things I have or am waiting for", and each shows a count badge. Due-soon items and holds that are ready for pickup surface on the tab badge. This gives you a tab for the library card without exceeding five.
  - **Card** shows the barcode at high brightness and holds sign-in and account settings. People need the barcode at the desk, so it is one tap away.
  - If you must keep Holds and Checkouts as separate tabs, drop Card and put the barcode at the top of My Items.
- **Show location at all times.** The active tab is highlighted with an icon and a text label. Each screen has a title. Tapping the active tab returns to that tab's top.
- **Back preserves state.** Going back from a book page returns to the same results, scroll position and filters. Tab switches keep each tab's state. Every book, event and branch has a shareable link.
- **Branch is remembered.** Ask once, in context ("Pick up at: Main Library ▾"), and reuse it for holds, hours and events. The assumption is shown next to the control and is changeable in one tap. Don't ask again.

## Search

**Scope:** One search covers the catalog, events and branches. Catalog results come first. Results are grouped under short headings: "Books & media", "Events", "Branches", and "Help" if you have FAQs. Searching "storytime" or "Eastside" should work, not just titles.

**On focus, before typing:**
- Show recent searches, each removable with an ×, and a "Clear all" control.
- Below them, show a few shortcuts into other tabs: "Renew my items", "Hours today at [my branch]", "Events this week".
- Show nothing else. Don't invent trending lists.

**While typing:**
- Suggestions appear after the first character or two. Group them by kind: titles, authors, subjects, events, branches. Label each row with its kind ("Author", "Event"), and don't rely on color or an icon alone.
- Tolerate typos, partial words and missing punctuation. Match author names in either order ("king stephen"). Match series names, and ISBNs when the input looks like one.
- Tapping a suggestion goes straight to that item or author. Pressing Search shows the full results list.
- The keyboard stays up, and the list scrolls beneath it. Don't re-render results on every keystroke. Update suggestions only, and use full results on submit.
- A barcode/ISBN scan button sits inside the field. It is a visible, labeled icon, not an unlabeled one.

**Results screen:**
- The count is always shown: "128 results for 'dune'".
- Each row shows cover, title, author, format, and availability at **my branch** ("Available now", "2 holds, est. wait [placeholder]", "Checked out, due Oct 28"). Availability on the row is the main thing people want, so it shouldn't be hidden behind a tap.
- Primary action on the row: **Place hold** or **Borrow/Download** for digital items. This is one tap, with a pickup-branch default and a toast: "Hold placed at Main Library. Undo" (about 8 seconds).
- Sort and filter live behind one **Refine** button. It holds format (book, ebook, audiobook, DVD), availability ("Available now"), branch, language, audience (kids, teen, adult) and sort ("Best match", "Newest", "Most popular").
- Active filters show as removable chips above the results. Facet options show counts, so a choice never leads to zero.
- Sort and filters persist for the session. Format and audience can be remembered between sessions, with a visible "Reset".
- Use "Load more" with a position marker, not endless scroll. People return to a spot in the list.

## When search finds nothing

Respond according to the cause:

1. **Filters caused it:** "No results for 'dune' with Available now + Large print. Remove 'Available now' (14 results)". Each filter is one tap to drop.
2. **Likely typo:** "Showing results for 'dune'. Search instead for 'dunee'". Run the corrected search automatically.
3. **Truly nothing in the catalog:**
   - Say so plainly, then offer in order: broaden the search (remove the last word, or search by author only); search **all branches** and digital collections if the current scope was narrower; **Suggest a purchase** or **Request via interlibrary loan**, whichever the system supports; and **Ask a librarian** (call, chat or email, whichever you have).
   - Keep the query visible and editable so people can fix it without retyping.
4. **Offline or error:** state that the search couldn't run, keep the query, and offer Retry. Don't show "no results", because that is a false answer.

## Other main screens

- **My Items, Checkouts:** Sort by due date, soonest first. Each row has a visible **Renew** button, plus a **Renew all** action that confirms nothing, because renewal is reversible in effect and low-risk. Show the outcome in place ("Renewed, due Nov 12") or the reason it failed ("Can't renew: another patron is waiting"). Overdue items sit at the top and are marked with text, not just color.
- **My Items, Holds:** Group into "Ready for pickup" (with pickup-by date and branch), "In transit" and "Waiting". Show position in queue only if the system supplies it. **Cancel hold** is undoable for a short time. Suspend/freeze is available from the row's menu.
- **Branches:** Open with the nearest or remembered branch first. Show "Open now, closes 8 pm" at the top of each row, with today's hours highlighted. Include holiday and special closures in the same view, not on a separate page. Actions are Call, Directions and "Set as my branch". A list/map toggle is optional.
- **Events:** Default to the next 7 days at my branch. Use a simple list grouped by day, with a calendar-jump control. Filter chips cover age group, type and branch. Registration is one tap where required, and a confirmed event shows a badge in place. "Add to calendar" is a visible action. An empty week says "No events at Main this week. Show all branches".

## Sign-in

Browsing, search and hours work without signing in. Ask for the card number and PIN only when the person places a hold or opens My Items. After sign-in, return them to the action they started and complete it. Offer biometric unlock as an opt-in, and keep sessions long on the device.

## Checks before you ship

- Test with five people who haven't seen the app: "Find a book you want and reserve it", "Renew what's due", "When does the Eastside branch close tonight?".
- Make sure every action works with screen readers and large text. Announce undo toasts through a live region and keep them on screen long enough to read.
- I have made no usage-data claims. Which tabs people use most is an unknown, so measure it after launch before you reorder anything.
