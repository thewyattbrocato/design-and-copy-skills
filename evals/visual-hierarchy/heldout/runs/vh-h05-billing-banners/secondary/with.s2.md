## Spec: Invoices screen messages

**Job of the screen:** make and track invoices. The payment problem is the only message that can cost the user something, so it gets the one top slot. Everything else stays out of the way of the list.

| Level | Message | Treatment | Location | Dismiss | Lifetime |
|---|---|---|---|---|---|
| 1, Action needed | Card declined / plan pause | Full-width strip above the list. Warning tone (amber or red, not brand blue), warning icon, the words "Action needed", one button: "Update card" | Top of the Invoices content, above the list | No dismiss | Stays until the card is fixed or the plan is no longer at risk |
| 2, Announcement | Portuguese invoices | Neutral surface (light gray, no accent color), small dot on a "What's new" item in the header, plus a one-time inline note in the Send dialog where the language choice is made | Header, and the Send dialog | Close button; the note shows until the user has opened it once | Up to one week, then only in What's new |
| 3, Hint | Press N for a new invoice | No banner. A small "N" keycap beside the New invoice button, always visible | Next to the New invoice button | Never needed | Permanent, very quiet |

**Rules for the developer:**
- Only one strip ever shows at the top. If Level 1 is active, nothing else appears above the list.
- The "Update card" button is the only solid button in its strip. The New invoice button stays the screen's primary action.
- Each level keeps its own cue, so it still reads in grayscale: the icon and words for Level 1, the dot for Level 2, the keycap for Level 3.
- Level 1 is only shown when the payment problem is active. Do not reuse the strip for other notices.

**Notes:**
- **The date needs checking before this ships.** The payment copy says the plan pauses on 14 March, but today is 7 October 2026. Either that date has already passed, which would make the warning wrong, or it means March 2027. Add the year and confirm it with whoever owns billing. If the deadline is real, the strip can get stronger wording in the last week before it.
- **I assumed the card problem is account-level.** It probably belongs on every screen, not only Invoices, so the strip should live in the app shell. I designed it for Invoices as you asked.
