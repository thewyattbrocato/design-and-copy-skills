**Assumptions:** The users are the general public on phones, mostly one-handed, and many use the app only occasionally. Most come to find a title, check a hold, or check a due date or open hour. Because this is a public context, I've designed for first-time use: visible labels and no tour.

## Navigation

**Make search the front door, not an icon.**
- **Tabs:** Use four tabs: **Search** (home), **My Items**, **Branches**, **Events**.
  - My Items holds **Checkouts | Holds** as a two-way switch at the top. People think of these as "my stuff," and merging them frees a tab. If you must keep five tabs, split them back out. Every tab stays labeled with text, and the current one is highlighted.
- **Account:** Put the library card and sign-in in the top corner. Showing the barcode there is the one thing people need at the desk.
- **Search tab:** It opens with a large, visible search field at the top. Below it sit the things people come for:
  - a "Ready for pickup" or "Due soon" strip (only when it applies)
  - today's hours for the remembered branch
  - a few event highlights
- **Badges:** The My Items tab shows a count for holds ready and items due within about 3 days. The number is assumed and should be tunable.
- **Back:** Going back always returns to the same scroll position, query and filters. Every item, branch and event has a shareable link.
- **Remembered branch:** Ask for a home branch once, on first use of anything branch-specific, and infer it from location if the person allows. Show it as a chip ("Main Library ▾") where it affects results, with a one-tap change. Remember it across Search, Branches and Events.

## Search

**Before typing (on focus):**
- Show recent searches, each removable, with a "Clear all."
- Add two shortcuts: **Scan a barcode/ISBN** and **Voice**.
- If there's no history, show a few browse categories ("New books," "Audiobooks," "Kids," "Large print").

**While typing:**
- Start suggesting at 2 characters, and tolerate typos and partial words.
- Group suggestions by kind: **Titles, Authors, Subjects, Branches, Events**. A search for "storytime" or "Eastside hours" then goes straight to the right place instead of failing in a catalog-only box.
- Tapping a suggestion opens it directly. The keyboard's Search key runs the full search.
- Keep the field's focus and the keyboard up while suggestions update. Don't move the layout under the person's thumb.
- Index what people remember: title, author, series, subject, ISBN, and narrator for audiobooks, not only the title.

**Results:**
- Show the result count and active filters as removable chips.
- Each row shows cover, title, author, format, and **availability at the remembered branch**. Examples: "Available at Main," "2 holds, about 3 weeks (assumed wording)," "Available at 3 other branches."
- The primary action on each row is **Place hold** or **Borrow**. If the person isn't signed in, sign in only at that moment and then continue the action.
- One **Refine** button holds sort and filters together: format, audience, language, branch, and "available now." Filter counts update live. Facet counts keep a choice from leading to zero. Sort and filters persist across navigation and sessions, with a visible "Reset."
- **Checked-out items stay in results.** They can be held, so "available now" is a filter, never the default. Hiding them is a main cause of "I can't find it."

**When nothing is found:**
1. If filters caused it, say so: "No results for 'dune' with Large print + Spanish." Offer one tap to remove the most restrictive chip, with the count that would appear.
2. If the spelling is the problem, show "Did you mean…?" and search the corrected term automatically when the match is confident, saying that you did.
3. If the catalog really doesn't have it, say so plainly and offer the next step:
   - search all branches
   - **Suggest a purchase / request via interlibrary loan** (if the library offers them)
   - matching events or branches, if any
   - "Ask a librarian" (chat, call, or the branch phone number)

   Never show a blank screen or "0 results" alone.
4. If the search failed because of a connection problem, say that. Keep the typed query and offer Retry. Don't present it as "no results."

## My Items

- **Checkouts:** Sort by due date, soonest first. Overdue and due-soon rows differ by label and icon, not color alone. Each row has a visible **Renew** button, plus **Renew all**.
  - A renewal that fails says why ("Someone is waiting for this") and gives the next step ("Return by Oct 22").
  - Success is shown in place with the new due date, not in a popup.
- **Holds:** Put **Ready for pickup** first, with branch, pickup-by date and (if available) a locker or shelf note. Then show waiting holds with queue position.
  - Cancel and Suspend work with an undo toast, not an "Are you sure?" The toast is announced to screen readers and stays on screen long enough to read.
  - Changing the pickup branch is an inline control on the row.
- **Empty states** point to the next action: "No holds. Find something to read" opens Search.

## Branches

- Open the list sorted by **distance** (with location permission) or the remembered branch first. Each row shows **Open now / Closed, and today's hours**, so no tap is needed for the most common question.
- The detail screen has the week's hours, with holiday and special closures called out, plus an address, a map link, a call button, and the services offered.
- A branch's own events are listed in its detail screen.

## Events

- Show a date-ordered list, starting from today, filtered to the remembered branch. Use chips for **Branch, Age group, Type**, and a toggle to a month calendar. The list is the default because it's faster on a phone.
- Branch and age choices are remembered, and the chips show what's applied.
- Searching within Events filters this list, with the same zero-results behavior as above ("No events for Teens at Eastside this week. Show all branches / next week").
- **Register** and **Add to calendar** are visible buttons on the event, not buried in a detail screen.

## Quick checks

- No primary function is behind an icon-only control.
- Every filter that narrows results is visible and removable.
- Back never loses a query.
- Nothing asks for something the app could remember (branch, formats).

**Placeholders to set with your data:** the due-soon threshold (3 days is assumed), the suggestion minimum (2 characters), and which of "suggest a purchase," "interlibrary loan" and "ask a librarian" the library actually offers.
