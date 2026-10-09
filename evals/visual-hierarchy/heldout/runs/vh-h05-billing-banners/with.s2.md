# Invoices screen: message hierarchy spec

**Job of the screen:** let a freelancer see and act on their invoices. The three messages are interruptions, so rank them by the cost of ignoring them. A declined card pauses the plan. The Portuguese feature is optional news. The shortcut is a nice-to-have.

## Ranking

| # | Message | Level | Loudness |
|---|---|---|---|
| 1 | Card declined | Primary | Loud, the only loud thing on the screen |
| 2 | Portuguese invoices | Secondary | Quiet, dismissible |
| 3 | Press N tip | Tertiary | Nearly silent, not a banner |

## 1. Card declined: persistent banner at the top

- **Position:** full-width banner above the invoice list, below the page header. It is the first thing under the title.
- **Color:** the only red or amber surface on the screen. Use a tinted fill with a solid left border or icon, not a saturated block. The color needs a second cue: a warning icon plus the words in the text.
- **Copy:** lead with the consequence and put the date in bold: "**Your plan pauses on 14 March.** Your card ending 4417 was declined." Say what to do in the button label rather than a generic "Fix".
- **Action:** one solid primary button, "Update card", which goes straight to the payment method form. This is the only solid button in the banner area.
- **Dismissal:** none. It goes away when the card is fixed. A "Remind me later" link is optional, but if you add one, the banner must come back in the 3 days before 14 March.
- **Escalation (optional):** within about 3 days of the pause date, strengthen it: solid fill, or repeat it in the app header.

## 2. Portuguese invoices: quiet, dismissible notice

- **Position:** below the declined-card banner, or in the page header area if the card banner isn't showing. Never above the card banner.
- **Style:** neutral. Use a gray or very light surface, or no fill at all, with a hairline border. Don't use blue fill. Small text, with a "New" label in a modest weight.
- **Copy:** "New: you can now send invoices in Portuguese." plus a text link, "Choose a language" (to wherever the setting lives).
- **Action:** text link only, no button.
- **Dismissal:** an × button. Once dismissed, never show it again. Optionally auto-hide it after about 30 days.
- **Rule:** if the card banner is showing, hide this notice entirely and show it on a later visit. Two stacked banners dilute the one that matters. If you won't suppress it, keep it to a single line.

## 3. "Press N" tip: not a banner

- **Position:** inline hint, not at the top. Put it where it's relevant: next to or under the "New invoice" button, as a tooltip on hover, or as a small muted line in the page footer. If you want it as a passing hint, use a subtle hint chip on the button itself (a small "N" keycap shown inside or beside it).
- **Style:** small muted text with the key shown as a keycap: "Tip: press <kbd>N</kbd> to start a new invoice."
- **Dismissal:** show it a few times, or until the user uses the shortcut once, then stop. No × is needed.
- **Never** show it at the same time as messages 1 or 2.

## Rules for your developer

1. **One message at a time at the top of the page.** Use a priority queue: billing problem > new feature > tip. Show only the highest-priority message that applies. The tip lives outside this queue.
2. **One loud color on the screen.** Red/amber is reserved for things that cost the user money or access. Blue banners for informational messages go away.
3. **Persistence follows urgency.** The billing banner can't be dismissed. The feature notice is dismissible and stays dismissed (store the flag per user). The tip retires itself.
4. **Accessibility:** give the billing banner `role="alert"` (or `role="status"` if it's present on page load), and make sure the color is paired with an icon and text. The other two are not announced as alerts.
5. **Check:** squint at the screen. You should see the red banner and nothing else competing. In grayscale, it should still stand apart thanks to its icon, bold date, and the only solid button.

## Assumptions

- You have no existing design system. If you do, use its warning, neutral, and hint tokens in place of the colors described here.
- I haven't seen your app or code. This is a spec from your description, so tell me if the screen has constraints (for example, a fixed header) that change where things go.
