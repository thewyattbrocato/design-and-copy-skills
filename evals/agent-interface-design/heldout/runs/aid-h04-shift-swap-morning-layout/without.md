**Morning summary screen (phone, single scroll)**

**1. Header (fixed, small)**
- "Tue 28 Oct · overnight" on the left, with a refresh/last-updated time on the right.
- Under it, one status line in large text that gives the answer before any scrolling:
  - "2 need you · 9 handled" (the "2 need you" part is in the accent color).
  - If nothing is stuck: "Nothing needs you · 9 handled".
  - If it was a quiet night: "No shift changes overnight".

**2. Needs you (only appears if something is stuck)**
This is one card per stuck item, sorted by how soon the shift starts, so the most urgent is first. Each card shows:
- A top line with the location, shift, and time left: "Harbor · Fri dinner 5–11pm · in 3 days". Shifts starting today get a red tag.
- A one-line problem in plain words: "Jo can't work. 6 asked, none accepted."
- Or, for overtime: "Sam accepted, but that puts him at 44h."
- A line on what the agent already tried, such as who it asked and when. The GM shouldn't have to wonder whether to repeat it.
- Buttons sized for a thumb, chosen for the problem type:
  - **Nobody accepted:** *Ask wider* (other locations or non-opted-in staff), *Call Jo's list* (opens a list of tappable phone numbers), *Leave open*.
  - **Overtime:** *Approve OT*, *Decline & keep looking*.
- Tapping the card body (not a button) opens the detail screen.

**3. Handled (collapsed by default)**
- A single tappable header row: "Handled overnight · 9 ▸". Tapping expands it.
- Expanded, rows are grouped by location, one line each: "Maria → Dev · Sat lunch". Each row has a small check icon.
- Tapping a row opens the detail screen.
- If more than about 6 rows are showing, the list gets a location filter chip row (All, Harbor, …) at the top of the section. It's hidden when the list is short.

**4. Detail screen (reached by tapping any card or row)**
- A timeline of what the agent did: who it messaged, who replied and when, and what changed on the rota.
- A *View in rota* link.
- For handled items, an *Undo / reassign* action. For stuck items, the same buttons as the card.

**5. Footer**
- *Open full rota* and *Opt-in list* links.

**Behavior notes**
- Stuck items are always above handled ones, and there is never a chart. The GM's morning question is "do I need to do anything?", and the top block answers it.
- Once the GM acts, the card collapses to a "Done" line and moves into Handled. The header count updates.
- With 15 items, the stuck cards stay at the top, and the handled list stays collapsed, so the screen never gets long.
- Push notification (optional, outside this screen): only for stuck items whose shift is within 24 hours.
