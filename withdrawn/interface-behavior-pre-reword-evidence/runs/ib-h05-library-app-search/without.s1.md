# Navigation and search for the library app

## Diagnosis
Two problems are stacked on each other. Search is the most-used action, but it sits in a corner icon and opens an empty box. And the five tabs mix two different kinds of thing: tasks (search, holds, checkouts) and reference content (hours, events). People don't know where to start.

## Navigation

**Bottom bar: four tabs**
1. **Home**
2. **Search** (the catalog)
3. **My Library** (holds, checkouts, fines, card)
4. **Locations & Events**

Why this layout:
- **Search is a tab.** It's the main job, so it gets the most prominent spot, not a corner icon.
- **Holds and checkouts merge into My Library.** They're the same account, and they share one question: "what do I have, and what's due or ready?" Inside it, use a segmented control (Checked out / Holds) with counts on each.
- **Hours and events share a tab** because both are about "when and where can I go?" Use a segmented control: Events / Branches. Default to the user's home branch.
- **Home is a dashboard, not a menu.** It should show:
  - A search field at the top (tapping it goes to the Search tab with the keyboard open)
  - "Due soon" items, with a one-tap renew
  - "Ready for pickup" holds, with the branch and pickup-by date
  - Today's hours for the home branch
  - Two or three upcoming events
  - If the user is signed out, a sign-in prompt in place of the personal sections

If you'd rather keep five tabs, split Locations & Events back into two. Don't put Holds and Checkouts back as separate tabs, though. Badges on My Library (ready holds, items due within 3 days) cover the urgency.

Put the library card barcode one tap from anywhere, such as a button on Home and in My Library. People need it at the desk.

## Search

### Before typing (focused, empty)
- Recent searches, with a clear option
- Shortcuts: "New releases," "Popular now," "Browse by genre," "Scan a barcode/ISBN"
- Voice input button in the field

### While typing
Show suggestions after the first 2 characters, updating on each keystroke with a short debounce (about 150 ms). The list has three groups, in this order:
1. **Query completions**, such as "hallie porter," "hallie porter audiobook." Tapping one runs the search.
2. **Direct matches**: top 3 titles, authors, or series, each with a cover thumbnail, format, and availability ("Available at Main" or "2 holds"). Tapping goes straight to the item.
3. **Beyond the catalog**: matches from other areas, such as "Events: Hallie Porter trivia night" or "Branch: Harris Park Library." This lets one search box cover the whole app.

Tolerate typos and word-order variations ("halie porer" still works), and treat author names, ISBNs, and series names as first-class matches.

### Results page
- Show the result count and a **format filter row**: All, Books, eBooks, Audiobooks, DVDs. Format matters more than anything else here.
- Defaults that help: a toggle for **Available now** and a branch filter that defaults to the home branch (with an easy way to expand to all branches).
- Sort: Relevance (default), Newest, Most popular, Title.
- Each result shows the cover, title, author, format, and one clear status line, such as "Available at Main," "Due back Oct 21," or "12 holds on 4 copies." The action button is **Place hold** or **Borrow** (for digital), directly on the row.
- Filters stay visible as chips. Show which are applied, and let people remove them with one tap.

### When nothing is found
Never show a bare "No results." In this order:
1. **Say what was searched and what was applied.** "No results for 'xyzzy' with Available now + Main Branch." If filters are on, offer "Remove filters" as the first action, since they're often the cause.
2. **Try the likely fixes automatically.** If a spelling correction is plausible, show results for the corrected term: "Showing results for *hallie porter*. Search instead for 'halie porer.'" If the query is long, retry with fewer terms.
3. **Offer other formats and branches.** "Found 4 results in all branches" or "Found in eBooks."
4. **Search the rest of the app.** "No catalog matches, but 1 event matches."
5. **Give a way forward**:
   - **Suggest a purchase** or **Request via interlibrary loan**, if your system supports them
   - **Ask a librarian** (chat, call, or email)
   - Search tips (search by author, ISBN, or part of a title) as a short secondary line

Also keep a "Recent searches" list visible beneath the message, so people can get back to something that worked.

### Other cases to design for
- **Offline or slow connection:** show recent searches and cached account info, with a clear "You're offline" banner. Don't show an empty-results state when the real problem is the network.
- **Signed-out users:** they can search and browse. Prompt for sign-in only when they tap Place hold, and bring them back to the same item afterward.
- **Barcode scan:** results go straight to the item page, or to the no-results flow if the ISBN isn't in the catalog.

## Things to test
- Tab labels. "My Library" can be confused with "the library," so test it against "Account."
- Whether people find events under the combined tab. If they don't, split it.
- Task-based tests: "Find a copy of X and reserve it," "Renew what's due this week," "Find out when the nearest branch closes today." Compare time-to-complete against the current app.

I can turn this into screen-by-screen wireframe descriptions or a sitemap if you'd like.
