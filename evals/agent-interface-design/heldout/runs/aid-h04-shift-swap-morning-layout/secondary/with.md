**Assumption:** Routine swaps run on act-and-report. The agent finds cover, offers the shift and updates the rota, and the GM sees the result after the fact. Anything stuck or involving overtime waits for the GM, and the agent never approves overtime on its own.

**Screen, top to bottom**

**1. Status line (not tappable)**
- With problems: "Overnight: 11 swaps. 9 covered. 2 need you."
- Quiet morning: "Overnight: 11 swaps. All covered. Nothing needs you."
- Small grey line below: "Last run 2:14am · Next check 6:00pm." This shows the agent is alive.

**2. Needs you (only shown when something is stuck)**
One card per stuck swap, most urgent first (earliest shift first). Each card states the shift, the problem and the deadline:
- *No cover:* "Line cook, [Location], Tue 6pm. Maria asked off. Nobody accepted after 9 offers. Cover needed by 3pm."
- *Overtime:* "Cover for Thu dinner would put Jordan at 41 hrs this week. Nobody else opted in."

Buttons on each card:
- **[Assign…]** opens the opted-in list for that shift. Each name shows hours this week, and anyone who would go into overtime is marked and can't be picked without a second tap.
- **[Approve overtime]** appears only on overtime cards. It requires an explicit tap and is never automatic.
- **[Post to all]** sends the open shift to every opted-in staff member.
- **[Hold]** leaves it open. The agent keeps trying and does not notify anyone.

**3. Done overnight (collapsed by default)**
One line: "9 covered automatically." Tap to expand. Each swap shows: "Sam → Ava, Sat 4 Nov, [Location]. Ava accepted 10:42pm."
- Each row has **[Undo]**, which reverses the rota change and tells the people involved.
- Under the list: "Undo available until 24h before the shift. Messages already sent to staff can't be recalled."

**4. Skipped (only when present)**
"1 message not acted on: 'can't do Fri maybe?' — unclear."
- **[Handle]** opens the swap request so the GM can take it.
- **[Dismiss]** closes it.

**5. Footer (always visible)**
- **[Pause swaps]**: one tap, with a visible "Paused" banner on this screen afterward.
- **[Activity log]**: the full record of every action.
- **[Limits]**: current rules, for example "Never auto-assigns overtime. Max 1 cover per shift without asking."

**Safety net:** if a stuck item is still open at a time the GM picks in Limits (for example 2pm), the agent sends one text: "[Shift] still uncovered. Open the app to decide." The GM is not relying on opening the app in time.

**Notes**
- The screen is ordered problems, then completions, then skips, so the GM's first look always lands on what needs a decision.
- Shift names and times are placeholders; I haven't set any figures such as cover windows or thresholds.
