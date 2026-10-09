## Recommendation

Give each message a different severity, placement, and lifetime. The problem is that all three use the same blue banner, so the card warning looks like the Portuguese announcement.

| | Card declined | Portuguese launch | Press N tip |
|---|---|---|---|
| **Loudness** | Highest: warning color, persistent | Low: informational, one-time | Lowest: contextual hint |
| **Placement** | Top of every screen until fixed, plus email | Settings/language picker, with a "new" dot in the menu | Next to the "New invoice" button |
| **Dismissal** | Not dismissable. Can snooze for a day. Clears when the payment is fixed. | Dismiss or auto-expire after first view or about 7 days | Dismiss permanently, or auto-retire after the user presses N once or after about 10 sessions |
| **Color** | Amber or red, with a warning icon | Neutral or blue, no icon | Neutral, shown as a keyboard hint badge |

### 1. Card declined (critical)

- **Placement:** A full-width inline alert at the top of the app shell, shown on all screens, not just Invoices. Send an email too, since someone who has ignored in-app banners may still read email.
- **Content:** Keep the message, add a primary button ("Update payment method") and a countdown or date.
- **Behavior:** No X button. Only "Remind me tomorrow" as a snooze. Remove the alert when the payment method is fixed or the plan is no longer at risk.
- **Copy issue:** It says "14 March," but today is 7 October 2026, so that date has already passed. Confirm whether it means March 2027 and show the year, or whether the copy is stale. Pull the date from billing data rather than hardcoding it.

### 2. Portuguese launch (informational)

- **Placement:** Don't show it on the Invoices screen. Show a small "New" dot on the Settings or account menu, and the language picker shows "Português (new)."
- **Behavior:** Show a one-time toast on first login after release, then auto-dismiss. Keep it in a "What's new" changelog entry.
- **Copy:** "Invoices can now be sent in Portuguese. Change it in Settings → Language."

### 3. Press N (tip)

- **Placement:** Show a `N` keyboard badge on the "New invoice" button, with a tooltip on hover. This puts the tip where the action is.
- **Behavior:** Show the badge only to users who haven't used N. Hide it permanently after the first use or after about 10 sessions. Don't show it again.
- **Dev note:** Ignore the N key when focus is in a text field, so it doesn't fire while someone types an invoice.

### Rules for the developer

- Only one banner slot at the top, reserved for critical account alerts. Informational and tip messages never use it.
- Reserve blue for informational content. Use amber or red only for things that need action.
- Each message gets a stored state (dismissed, snoozed, seen count) so it doesn't come back once handled.
- If more than one critical alert exists, show the most urgent one. Use a stack only for critical alerts.
