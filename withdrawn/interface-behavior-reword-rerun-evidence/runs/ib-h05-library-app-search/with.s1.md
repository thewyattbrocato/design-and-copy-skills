**Assumptions:** The users are the general public on phones, from teens to seniors. Most are occasional visitors, and a core group checks holds and due dates often. Many are in a hurry, such as standing in the stacks or checking whether a branch is open. I've assumed the catalog has title, author, subject, ISBN and format data, and that users sign in with a library card.

## Navigation

- **Keep five tabs, but change what they are.** The tab bar isn't the main problem. Search is hidden behind an icon, so the main job of the app looks like a side feature. Use these tabs in this order: **Search · Holds · Checkouts · Branches · Events**. Each label is text next to an icon, and the current tab is highlighted.
- **Search is the first tab and the landing screen.** A large search field sits at the top of the screen and is not an icon. Under it, show "Ready for pickup" (count) and "Due soon" (count) as tappable cards for signed-in users, then the home branch's open or closed status. People open this app mostly to check on these things, so they appear before they have to look for them.
- **Badges give state without opening anything.** Holds shows a count of items ready for pickup. Checkouts shows a count of items due soon or overdue. The badge also carries a text or icon cue, not just a color.
- **Search is also reachable from other tabs.** Holds, Checkouts and Events each have a filter field at the top for their own contents ("Filter my holds"). Branches has a field for finding a branch by name or town. These fields only search their own tab's list. A tap on a "Search catalog" link takes the user to the first tab.
- **Pick a home branch once and remember it.** Show it beside the search field ("Showing availability at Eastside, change") and keep a reset. Availability, hours and events default to that branch. Don't ask on first launch. Guess from location permission if the user has granted it, otherwise ask the first time they look at availability.
- **Back keeps position.** Back from a book returns to the same results at the same scroll position, with the same filters. Every book, branch and event has a shareable link.
- **Signed-out state.** Search, Branches and Events work without signing in. Holds and Checkouts show a sign-in prompt in place, and finishing sign-in returns the user to what they were doing, such as placing a hold.

## Search

**Before typing (on focus)**
- Show recent searches, each removable, with a "Clear" link. Below those, show browse shortcuts in plain words: "New this week," "Audiobooks," "Kids," "Large print," "Available now at my branch."
- Include a scan-barcode/ISBN button and a microphone button if the platform supports voice input. Both are labeled, not icon-only.

**While typing**
- Show suggestions after the first character or two, grouped by kind: **Titles, Authors, Subjects, Branches/Events** (a few of each, with the type labeled). Tapping a title opens it directly. Tapping an author or subject opens a filtered results list. Pressing the keyboard's search key runs the full search.
- Tolerate typos and partial words ("hallie porer" still finds Hallie Porter). Match on author, series, subject and ISBN, not only title.
- Show the search text in the field exactly as typed. Corrections appear as suggestions, or as "Showing results for…" with a "Search instead for…" link.
- Suggestions update live but never move under the user's thumb while they tap. Keep the list stable once the user starts scrolling it.

**Results**
- Each result shows cover, title, author, format, and one line of availability at the home branch: "2 of 5 available" or "All checked out, 7 holds." The hold or borrow action is on the result row, so a hold takes one tap from results.
- One **Refine** button holds sort and filters together: format, availability at my branch, language, audience (adult, teen, kids), and date published. Active filters appear as removable chips above results, with the result count.
- Facet options show counts, and options that would produce nothing are disabled or hidden, so a choice never leads to an empty list.
- Default sort is relevance. Remember the user's last sort and filter choices for the session, and offer to keep them.
- Use "Load more" with a position marker rather than endless scroll, so users can get back to where they were.

## When nothing is found

Say what was searched and why it failed. Then offer next steps, most useful first:
1. **Filters caused it:** "No results for 'dune' with Large print + Available now." Offer a one-tap button to remove the most restrictive filter, showing how many results that gives.
2. **Likely typo:** "Did you mean *Dune*?" Show a button that runs the corrected search.
3. **Wording too narrow:** Show broader matches ("Results for 'dune' in all formats"), or related authors and subjects.
4. **It isn't owned at all:** Say so plainly, and offer the library's interlibrary loan or "Suggest a purchase" request, prefilled with what the user typed. Show this only if the library offers those services. Also offer "Ask a librarian" with the branch phone number or chat link.
5. Keep the search text in the field and keep recent searches visible, so the user can edit and retry without retyping.

Never show a blank screen or a bare "No results."

## Behavior in other tabs

- **Holds:** Group by "Ready for pickup" (with the pickup branch and last pickup date), "In transit," and "Waiting" (with queue position). Cancel or freeze a hold with **Undo**, not an "Are you sure?" dialog, because a canceled hold can be restored if it's within a short window. If it can't be restored (for example, losing a queue place), say that in the one confirmation, naming the item and its queue position.
- **Checkouts:** Sort by due date, soonest first. Renew is a visible button on each row, plus "Renew all." If renewal fails, say why in place (another hold, renewal limit) and give the next step, such as the date the item can be renewed again.
- **Branches:** Open with the home branch on top and an "Open now / closes at 8 pm" status. Hours show today first, with holiday closures marked on the right date. Include call, directions and branch events links.
- **Events:** Default to the home branch, upcoming, in a date-grouped list. Filters for age group, type and branch live behind the same Refine control. Add to calendar is one tap, and registration is in place for events that need it. For a full or canceled event, say so on the row.

## Accessibility

Search, suggestions, filters and Undo must all work with a screen reader and keyboard. Announce the result count and any "no results" message in a polite live region. Undo messages stay up long enough to read, and pause on focus (starting value: about 6 to 10 seconds). Don't use color alone for availability or due-soon states. Tap targets should be large, and text should scale with the system font setting.

## Open questions I've assumed answers to

- Is the home branch known from the account? If so, skip the first-use prompt.
- Does the library offer interlibrary loan or purchase requests? The no-results step 4 depends on it.
- Are there e-books or audiobooks in a separate app (such as Libby)? If so, results should link out clearly and say where an item will open.
