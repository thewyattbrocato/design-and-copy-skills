## Spec: Invoices screen messages

**Job of the screen:** create and send invoices. Billing and announcements support that job; they should not compete with it.

**Rank:** 1. Card declined (needs action, has a deadline). 2. Keyboard tip (helps the main task). 3. Portuguese announcement (no action needed).

| | Message | Loudness | Placement | Behavior |
|---|---|---|---|---|
| 1 | Card declined | **Loudest, one only.** Full-width bar above the invoice list, warning color (not brand blue), warning icon, bold first line, one button: "Update card". | Top of Invoices screen, above the list. Also shown on Billing and Settings. | Stays until resolved. Not dismissable. Escalates copy and color in the final 7 days before the pause date. |
| 2 | Keyboard tip "N" | **Quiet.** No banner. A key-hint chip on the "New invoice" button ("New invoice · N"). | Inline on the button it describes. | Shown only to users who haven't pressed N. Hides permanently after first use. |
| 3 | Portuguese announcement | **Quiet.** A small dismissible toast, then a dot on the "What's new" menu item. | Toast in bottom corner, once. Long-term home is the "What's new" menu. | Shows once per user. Dismiss is permanent. Dot clears when the menu is opened. |

### Rules for the developer

- **Only one banner ever shows on the Invoices screen,** and it is the billing alert when that is active. Tips and announcements never go into the banner slot.
- **Use the warning/error color for billing,** not the blue used for information. Keep blue for the announcement's icon and link only, so the two don't look alike.
- **Action buttons:** the billing bar has one button. The "New invoice" button stays the single primary action on the screen.
- **Date handling:** compute the pause date in code and show it with the year, e.g. "14 March 2027". Today is 15 October 2026, so the next 14 March is 2027, not this year. A bare "14 March" is ambiguous.
- **Persistence:** store "tip seen/used" and "announcement dismissed" per user, so they don't return on reload.

### Notes

- If the billing failure is a sudden card decline, a one-sentence message that names the card ("Your card ending 4417 was declined") plus the pause date is enough. Don't add urgency words; the layout already carries the weight.
- Copy for the billing bar should be the only text on the screen allowed to use bold. Check that with a squint test after building.
