# Spec: Invoices screen messages

**Check before handoff:** Today is 7 October 2026, so "pause on 14 March" is already in the past. Either the date is hardcoded and stale, or it means March 2027. The developer should compute the date from the billing record's real pause date, not from a string.

## Principle

Only one message gets the top slot, and only if it needs action. The other two move out of the banner area entirely. Right now all three share one style, so nothing ranks above anything else.

| | 1. Card declined | 2. Portuguese launch | 3. Press N tip |
|---|---|---|---|
| **Loudness** | Highest: persistent, warning color | Low: one-time, dismissable | Lowest: inline hint, no banner |
| **Where** | Top slot on Invoices, plus Settings > Billing | "What's new" menu item and a "New" badge on the invoice language picker | "N" key chip on the New Invoice button |
| **Dismissable** | No, until the card is fixed or the plan is paused | Yes, and it never returns after dismissal | Hint hides after the user presses N, or after about 5 clicks on the button without pressing N |
| **Who sees it** | All users with a failed payment | All users, once | Desktop users with a keyboard, once they've created at least one invoice |
| **Color** | Amber or red, reserved for this only | Neutral or brand accent, not warning | No banner color; a small grey key chip |

## 1. Card declined (critical)

- **Placement:** A full-width bar above the invoice list. It doesn't block the screen, because the user still needs to send invoices.
- **Copy:** "Your card ending 4417 was declined. Your plan pauses in 12 days unless you update it." Compute "12 days" from the billing record. Once fewer than 7 days remain, switch to red.
- **Action:** A primary button, "Update card," that goes straight to the billing form. Don't make the user hunt for it.
- **Persistence:** Shows on every visit until resolved. Snooze per session is acceptable; permanent dismissal is not.
- **Also:** Send an email at the failure and at 7 days out. A banner alone is easy to miss for people who only open the app to send invoices.

## 2. Portuguese launch (announcement)

- **Placement:** A "New" badge on the invoice language picker, where the feature is used, and an entry in "What's new." Don't put it on the Invoices screen.
- **Behavior:** Shows once. Clears when the user opens the picker or the What's new page.
- **Copy:** "Invoices can now be sent in Portuguese."

## 3. Press N (tip)

- **Placement:** A small "N" key chip on the New Invoice button itself. The shortcut is always discoverable there, with no banner needed.
- **Behavior:** Show the chip on desktop only. Hide the chip permanently after the user presses N. Don't show it to touch-only users.
- **No banner, no toast.** Tips should live where the action is.

## Developer notes

- Keep a single priority check for the top slot. The critical message wins. Announcements and tips never render there.
- Store dismissal and "seen" state per user per message ID, server-side, so it survives reinstalls and devices.
- Compute the pause date and days remaining server-side, with the user's time zone. Don't hardcode dates in copy.
- Give each message an ID (for example `billing_card_declined`, `announce_pt_invoices`, `tip_press_n`) so you can add, expire, and audit them without code changes.

## Open questions for you

- Does the plan actually pause on a fixed date, or on a grace period that resets when a card is updated? The copy depends on it.
- Should the Portuguese badge expire after a set time, say 30 days, even if the user never opens the picker?
