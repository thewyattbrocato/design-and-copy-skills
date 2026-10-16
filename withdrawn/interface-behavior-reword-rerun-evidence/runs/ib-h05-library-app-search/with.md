**Assumptions:** Patrons use phones, often one-handed and in short visits. Most come back to the app a few times a month to check holds, renew, or look something up. A large share are older or less comfortable with apps, so labels must be visible and plain. I haven't seen any usage data, so the tab order and defaults below are starting points to check against analytics.

## Navigation

**Keep five tabs, but change what they are.** Label each with text, not just an icon. Make Search a tab, not a corner icon. Tabs: **Home, Search, My Library, Branches, Events.**

- **Home** answers "what do I need to act on?" It shows items due soon (with a Renew button), holds ready for pickup (with branch and pickup-by date), and today's hours for the user's branch. This replaces separate trips to Holds and Checkouts for most visits.
- **My Library** holds the two lists people actually mean: **Checkouts** and **Holds**, as two segments at the top of one screen. The screen remembers the last segment. Each list shows a count badge on the tab, such as "2 ready for pickup".
- **Branches** shows hours as a list, with the user's home branch first and "Open now / Closes at 8 pm" in plain words. Tapping a branch opens its address, phone, a map link, and that branch's events.
- **Events** is a list grouped by day. It has one Refine control (branch, age group, type) that remembers the last choice, with a visible chip for each active filter.
- The current tab is highlighted, and each screen has a title. Back returns to the same scroll position, filters, and search results. Every screen has a link, so a notification or email can open the exact hold or event.

**Why Search is a tab:** "can't find anything" is the main complaint, and a corner icon is easy to miss. A tab is always visible and shows the user where they are.

## Search

**On focus, before typing:** show recent searches, with a clear control. Below those, offer shortcuts to common tasks: "Search your holds", "Search your checkouts", and a scope selector (see below). The keyboard opens immediately.

**While typing**, after one or two characters:
- Show suggestions grouped by kind: **Titles, Authors, Subjects/Series, Events, Branches.** Each group shows only a few rows, with "See all" for more.
- Tolerate typos and partial words ("hallie porer" still finds Hallie Porter). Match what people remember: author, series, subject, ISBN, and words from descriptions, not just titles.
- Tapping a suggestion goes straight to that item, author, event, or branch. Pressing Search shows the full results list.
- Update suggestions on every keystroke without stealing focus or resetting scroll. Don't show a spinner for fast responses; show a slim progress indicator only if it takes noticeably long.

**Scope:** one box searches the whole catalog by default, and the scope selector sits next to it ("Catalog · My items · Events"). The app remembers the last scope and shows it beside the field. A search that matches a branch or event surfaces it in the grouped suggestions, so people don't have to guess which tab it lives on.

**Results list:**
- Each row shows cover, title, author, format, and **availability in plain words**: "Available at Main Library", "2 copies at your branch", or "Hold list: 14 waiting". The primary button on the row is the next step: **Place hold**, **Borrow** (for digital titles), or **Hold placed ✓**.
- One **Refine** button holds sort and filters together: format (book, audiobook, ebook, DVD), availability, branch, language, and audience. Active filters appear as removable chips above the list, along with the result count. Each filter option shows its count so a choice never leads to zero. Sort and filters persist for the session. Default sort is relevance, with "Available now" as one tap.
- Place hold uses the user's saved pickup branch, shown next to the button as "Pick up at Main · Change". It happens in one tap and shows a confirmation in place, plus Undo ("Hold placed. Undo") for several seconds. It's cancelable later from My Library, so no "Are you sure?" is needed.
- Use a load-more with a position marker rather than infinite scroll, so people can compare and return to where they were.

## When nothing is found

Say what happened and give a next step. Never show a blank screen or "No results".

1. **Filters caused it:** "No results with Audiobook + Available now. Remove 'Available now' (23 results)", with a one-tap button to relax each filter.
2. **Likely typo:** "Showing results for *hallie porter*. Search instead for 'hallie porer'."
3. **Truly nothing:** show "Nothing in the catalog for 'xyz'." Then offer:
   - nearby searches (the same words as author or subject, broader terms),
   - results from other scopes ("2 events match"),
   - **Suggest a purchase** or **Ask a librarian** (phone, chat, or email, with branch hours, which is a real next step for a library),
   - tips only if useful, such as "Try the author's last name".
4. **Offline or error:** say so in place, keep what they typed, and offer Retry. Recent searches still work.

## Edge cases worth deciding

- **Not signed in:** Search, Branches, and Events work without a login. Holds and My Library ask for a card number only when needed, and the app remembers the login on the device. Don't make people sign in just to look.
- **Card expired or fines block holds:** show the reason on the Place hold button's row and Home, with a way to resolve it, not a failed tap.
- **Empty states:** "No holds yet. Search the catalog" with a button to the Search tab.
- **Accessibility:** large tap targets, no meaning by color alone (availability has words), screen-reader announcement of "Hold placed" and result counts, and an optional barcode scan in the search field for people holding a book.

## What to check with real users

Test whether Home is enough for the main complaint before reordering tabs, and watch where people go first. Track searches that return zero results, since that list tells you what to fix in the catalog index and synonyms. I haven't assumed any numbers for these.
