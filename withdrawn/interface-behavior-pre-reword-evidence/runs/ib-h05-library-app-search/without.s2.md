# Navigation and search for the library app

## Core change
Search is the front door, not a corner icon. Most people come to find a book, check something they already have, or check hours. The layout should serve those three jobs directly.

## Bottom bar (five tabs)

| Tab | Contents |
|---|---|
| **Home** | Search field at the top (a real field, not an icon). Below it: items due soon, holds ready for pickup, and today's hours for the user's home branch. |
| **Search** | Same search field with browse options: new releases, popular, genres, and formats (books, eBooks, audiobooks, DVDs). |
| **My Items** | One tab with a segmented control: **Checkouts** \| **Holds** \| **Fines/Card**. It opens on whichever needs attention, such as a hold ready for pickup or something overdue. |
| **Branches** | List sorted by distance, with open/closed status and today's hours visible without tapping. Detail view has the full week, holiday closures, map, phone, and services. |
| **Events** | Calendar and list toggle, with filters for branch, age group, and date. |

Checkouts and Holds are merged into My Items because they're both "my stuff". That frees a slot so Search can be a tab. Home and Search overlap on purpose: Home is for people checking status, and Search is for people looking for something. If you want to drop one tab, merge them and keep the search field pinned at the top.

Other rules:
- Keep a persistent search field at the top of Home, Search, and Events. On Branches and My Items, tapping a search icon opens search scoped to that area.
- Show a badge on My Items for ready holds and items due within 3 days.
- Let people set a home branch once. Use it for availability, hours, and event defaults.

## Search while typing

**Before typing (field focused, empty):**
- Recent searches, each removable.
- Quick actions: scan a barcode or ISBN, voice input.
- "Popular at your branch."

**As they type (start at 2 characters, debounce about 200 ms):**
Show a grouped suggestion list, not a plain text box.
1. **Query completions**: titles, authors, and series, with typo tolerance ("halie porer" still suggests *Hallie Porter*).
2. **Top matches** with cover, author, format, and availability at the home branch ("Available now" or "3 holds").
3. **Other places it matches**: a branch name ("Eastside Branch · Open until 8") and events ("Toddler Storytime · Sat"). This is what fixes "I can't find anything", because someone typing "storytime" or "Main St" gets an answer without choosing the right tab first.

Tapping a completion goes straight to that item or a results page. Tapping the keyboard's Search key opens the full results.

**Results page:**
- Filter chips along the top: **Available now**, format, language, audience, and branch. Make "Available now at my branch" a one-tap toggle.
- Each result shows cover, title, author, format, and availability, with a **Place hold** or **Borrow now** (eBook) button on the row.
- Sort: relevance (default), newest, most popular.
- Keep filters and the query when navigating back from a detail page.

## When nothing is found

Never show a bare "No results." In order of priority:
1. **Spelling correction**: "Showing results for *Hallie Porter*. Search instead for *halie porer*."
2. **Relax filters**: if filters were on, show "No results with these filters. Remove *Available now*?" with the count that would appear.
3. **Widen scope**: "Search all branches" or "Include eBooks and audiobooks" if the scope was narrowed.
4. **Cross-search**: "No catalog matches, but we found 2 events and 1 branch matching 'quilting'."
5. **Ways forward**: "Request this title" (purchase suggestion or interlibrary loan), and "Ask a librarian" (call, chat, or email). Pre-fill the request with what they typed.
6. **Browse fallback**: popular items or genres, so the screen isn't empty.

Also handle the failure cases separately: offline and server-error messages should say so and offer retry, not claim the library has nothing.

## What to test
Run 5 or 6 task-based sessions: "find out if the library has X," "renew your book," "see when the nearest branch closes Saturday," "find a kids' event this weekend." Watch where people reach for the old corner icon or the wrong tab. Track the zero-result rate and the top zero-result queries after launch. That list tells you what to add to synonyms, the catalog, or purchase requests.
