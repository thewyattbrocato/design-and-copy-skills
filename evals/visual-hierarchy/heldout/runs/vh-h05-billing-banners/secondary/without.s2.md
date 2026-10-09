**Recommendation:** Give each message a different level of loudness and a different home. Only the card message should ever block attention. The other two should be quiet, and they should never compete with it for the same slot.

| | Card declined | Portuguese launch | Press N tip |
|---|---|---|---|
| **Level** | Urgent, persistent | Announcement, one-time | Hint, contextual |
| **Where** | Top of Invoices, plus a small badge on the account/billing menu | "What's new" entry in the menu, with a dot until seen | Inline, next to the New invoice button |
| **Visual** | Warning color with icon and a button | Plain text row, no color fill | Small muted label or tooltip |
| **Dismissal** | Not dismissible until resolved | Dismissible; shows once | Auto-retires after the user presses N once, or after about 5 sessions |
| **Blocks anything?** | No, but it's on every screen that matters | Never | Never |

**1. Card declined (urgent)**
- **Placement:** Pinned to the top of Invoices and on any screen where the plan matters (settings, billing). Add a small dot or badge on the account menu so it stays visible even when the banner is out of view.
- **Style:** Warning color (amber or red, not the info blue), warning icon, and a primary button: "Update card." Keep the copy as written.
- **Behavior:** Stays until the card is updated or the payment succeeds. Don't let it be dismissed. Optionally, email the user at 7 days and 1 day before the pause.
- **Date:** The copy says "14 March," but today is 7 October 2026. If that date is hardcoded, it's either stale or wrong. The date must come from the billing system, and the copy should change if the pause date has already passed (for example, "Your plan is paused. Update your card to restore it.").

**2. Portuguese (announcement)**
- **Placement:** A "What's new" item in the menu, with a dot until opened. Optionally, show it once in the language setting, where it's relevant.
- **Style:** Plain text, no banner, no color fill, no icon.
- **Behavior:** Dismissible. Never shown again after it's seen once or after the user dismisses it.
- **Note:** Only show the language callout to users who could use it. If the feature is a setting, the settings screen is the right place.

**3. Press N (hint)**
- **Placement:** Show the shortcut on the New invoice button itself, like "New invoice  N". This is quieter and more useful than a tip, because it stays put and needs no dismissal.
- **Behavior:** Once the user presses N, remove the label or hint for them permanently. Otherwise, retire it after about 5 sessions.
- **Style:** Muted text, no color, no icon.

**Global rules for the developer**
- Only one banner slot exists on Invoices, and it's reserved for urgent account or billing messages. Announcements and hints never use it.
- Priority, if more than one urgent message ever appears: billing and account first, then errors, then everything else.
- Track whether each message is seen, dismissed, and acted on. If the press-N hint is still showing after 30 days for most users, it's not doing its job.

**Open questions for you**
- Does the card-declined state actually block sending invoices, or only the plan? That determines whether the Invoices banner should also disable the send button.
- Is there an existing "What's new" or help menu? If not, the Portuguese item needs a home, and the simplest option is a dot on the account menu.
