# Invoices screen: message hierarchy

**The job of the screen:** help the user work on invoices. Only one of the three messages can cost them money, so only that one should interrupt.

## Ranking

| Rank | Message | Loudness | Placement |
|---|---|---|---|
| 1 | Card declined | Loud | Full-width banner at the top of the content area, above the invoice list |
| 2 | Portuguese invoices | Quiet | Small dismissible note inside the page, below the primary content, or in a "What's new" entry |
| 3 | Press N tip | Nearly invisible | Inline hint next to the "New invoice" button |

Only one banner shows at a time. If the card message is present, the Portuguese note is suppressed.

## 1. Card declined (the only banner)

- **Style:** a solid warning or error treatment. Use a tinted red or amber background with a stronger left edge or border, and a warning icon. Use the icon as a second cue, so the message still reads in grayscale and for colorblind users.
- **Placement:** top of the content area, full width, pushing the list down. It stays there until the card is fixed. Do not make it dismissible. A "Remind me later" option is acceptable, but it must return on the next visit.
- **Copy:** lead with the consequence and the date, and make the action a button.
  - Text: **"Your card ending 4417 was declined. Your plan will pause on 14 March."**
  - Button: **"Update card"**. This is the one solid primary button on the screen, so "New invoice" must not compete with it. Make "New invoice" a secondary style while this banner is up, or accept that two primaries share the screen briefly.
- **Escalation:** it can get louder as 14 March approaches (for example, red in the last 3 days, amber before that). The date is the real driver, so state the date in the text rather than only changing colors.

## 2. Portuguese invoices (announcement)

- **Style:** no colored background. Use plain text with a small "New" label, a text link ("Try it"), and a close (×) button.
- **Placement:** not at the top. Put it below the invoice list, or in a quiet strip above the list only when no warning is showing. Better still, show it only when the user opens the language setting or creates an invoice, where it's relevant.
- **Behavior:** it's dismissed permanently on the first × click, and it's never shown again. It is also hidden whenever the card banner is present.

## 3. "Press N" tip

- **Style:** not a banner at all. Show it as muted helper text, or as a small keyboard-key badge "N" beside the "New invoice" button.
- **Placement:** attached to the control it describes.
- **Behavior:** hide it permanently after the user presses N once or creates their first few invoices. Do not show it on mobile or touch devices, where it doesn't apply.

## Rules for your developer

1. Add a `severity` to each message: `critical`, `info`, `hint`. Each severity has one visual style, used the same way everywhere.
2. Only `critical` messages may appear as full-width banners. Only one banner shows at a time.
3. `critical` messages are not permanently dismissible. `info` and `hint` messages are, and the dismissal is stored per user.
4. Priority when several apply: critical, then info, then hint. Show only the highest-ranked message in the top area.
5. Blue is no longer the default for every message. Reserve it for `info` only, and keep it quiet.

## Why this works

Three identical banners compete, so people tune out all of them. Making one loud and the other two quiet means the card warning stands out, and the others still exist without getting in the way. The loud treatment is only meaningful if it's rare.

**Assumptions:**
- Your "Update card" flow is reachable in one click from the banner.
- If your app has no "What's new" area, the quiet note under the list is enough for the Portuguese message.
