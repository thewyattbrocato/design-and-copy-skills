**Assumptions:** The users are the public, on phones. Some open the app once a month and some daily. Most come to do one job: find a book, check a hold, or see when a branch closes. Many are logged in, but browsing the catalog shouldn't require it.

## Navigation

**Keep the bottom bar, but change what's in it.** Five tabs is the upper limit, and the tabs are the wrong ones. Catalog search is the main job and currently sits behind a corner icon.

| Tab | Contains |
|---|---|
| **Home** | Search bar at the top, then a "needs attention" strip: items due soon, holds ready for pickup. Below that is today's hours for the user's branch and the next few events. |
| **Search** | Catalog search. Tapping it opens the search field with the keyboard up. |
| **My Items** | Checkouts and Holds, shown as two segments on one screen. |
| **Branches** | Hours, address, and a map. |
| **Events** | Calendar and list. |

- **Why Home exists:** it answers the usual question, "what do I need to do?", without a tap. Counts show as badges on My Items: "2 due in 3 days" and "1 ready."
- **Why Holds and Checkouts are merged:** people think of both as "my stuff," and they are two views of the same account. This frees up a slot.
- **Location is always visible.** The active tab is highlighted and has a text label. Every screen has a title.
- **Back preserves state.** Returning from a book page keeps the scroll position, query, and filters. Every book, event, and branch has a shareable link.
- **The search bar on Home is a real field, not an icon.** Tapping it jumps to the Search tab. Drop the corner icon, because two entry points to one function is clutter.

## Search

**Before typing (on focus):**
- Show recent searches, each with a remove button.
- Show shortcuts such as "Available now," "New this month," and "Browse by genre." The staff can curate these.
- Show the barcode or ISBN scan button. It sits inside the field.

**While typing:**
- Update suggestions on each keystroke, grouped by kind:
  - **Titles and authors:** with cover thumbnails.
  - **Events:** such as "Toddler story time."
  - **Branches:** such as "Eastside branch."
  - **Help pages:** such as "Renew a book."
- Tolerate typos and partial words. "Hallie porer" should still find the book.
- Match what people remember: author, series, subject, and part of a title. Don't match only the exact title.
- Pressing search shows full results. Each result shows format, availability, and the nearest branch with a copy. It shows "Available at Eastside" or "12 holds, about N weeks" (the wait estimate should come from your system's data).
- Format (book, ebook, audiobook, DVD) is the most-used filter, so put it as chips directly under the search bar.

**Results screen:**
- Show the result count and active filters as removable chips.
- One "Refine" button holds sort and filter together. It uses plain labels: "Available now," "Newest first," "At my branch."
- Filters show counts, so no choice leads to zero.
- Remember the user's home branch and preferred format. Show "At: Eastside · Change" so the assumption is visible and easy to reset.
- Use a load-more button with position kept on return, not endless scrolling. People compare results and come back to them.
- Place Hold is a single tap. It uses the home branch as the pickup location by default and shows "Pickup at Eastside · Change." It shows a toast with Undo ("Hold placed · Undo") because canceling a hold is cheap. If the user isn't logged in, ask them to sign in then, and resume the hold afterward.

## When nothing is found

Say what happened and give a next step. Never show a blank screen.

1. **Filters caused it.** "No results for 'dune' with Audiobook + Eastside." Offer one tap: "Remove Eastside filter (14 results)."
2. **Likely typo.** "Showing results for 'dune.' Search instead for 'dunne'?" Auto-correct only when one match is clearly stronger.
3. **Really nothing.** "We don't have 'xyz.'" Then show:
   - Related results (similar subjects or authors) if there are any.
   - **Suggest a purchase** or **Request from another library** (interlibrary loan), if the system supports either. Prefill it with the search text.
   - **Ask a librarian**: a link to chat, phone, or the branch.
4. **No connection.** Say that, show recent searches and the user's cached items, and retry automatically.

## Other main screens

- **My Items:**
  - Sort by due date, soonest first.
  - Each row shows a status in text and an icon, not color alone: "Due in 2 days," "Ready for pickup until Fri."
  - Renew is a visible button on each row, with a "Renew all" action. It shows "Renewed, due Nov 17" with Undo if the system allows. When an item can't be renewed, say why ("Another patron is waiting") and offer the next step.
  - Pickup holds sit at the top, since they're time-limited.
- **Branches:** put the user's home branch first, with "Open until 8 pm" and a "Closes soon" label. Include a "Open now" filter. Show holiday closures right in the hours, not on a separate page.
- **Events:** default to a list for the next two weeks, with a calendar toggle. Filters are for age group and branch, and they persist. Add to calendar is one tap.

## Accessibility

- Every function reachable by keyboard and screen reader, with visible focus.
- Toasts announced politely and left up long enough to read.
- Availability and due status never rely on color alone.
- Suggestions announce their count ("5 suggestions").

I haven't tested any of this with your users. Before finalizing, check it with a few patrons: ask them to find a specific book, place a hold, and find Saturday hours. Watch where they hesitate.
