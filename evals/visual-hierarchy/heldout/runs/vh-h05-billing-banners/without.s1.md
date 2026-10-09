# Invoices screen: message hierarchy spec

**Principle:** loudness should match consequence and urgency. Only the card message has a deadline and a cost, so only it gets a banner. The other two are optional and shouldn't compete with it.

## 1. Card declined: loudest, top of the screen

- **Placement:** full-width banner at the very top of the Invoices screen, above the page title and invoice list. It pushes content down.
- **Style:** error/critical treatment. Red or amber-red background tint, a warning icon, and a high-contrast text colour (meet WCAG AA, 4.5:1). Don't rely on colour alone, so keep the icon.
- **Copy:** "Your card ending 4417 was declined. Your plan will pause on 14 March unless you update it." Keep it as is, but add the year if the date could be read as past or ambiguous. Generate the date from data, don't hardcode it.
- **Action:** a primary button, **"Update card"**, that goes straight to the payment form. Don't make people hunt for it.
- **Dismissal:** not dismissable. It disappears only when the card is fixed. If you must allow it, hide it for at most 24 hours, and it must come back.
- **Escalation:** from 3 days before the pause date, make it stronger. Change the copy to "Your plan pauses in 3 days" and use a solid red background with white text.
- **Accessibility:** `role="alert"` (or `aria-live="assertive"`), so screen readers announce it on load.
- **Also surface it elsewhere:** show it on any screen where the pause would hurt, such as the Send Invoice flow. That's optional but worth doing.

## 2. Portuguese invoices: quiet, dismissable, one-time

- **Placement:** below the card banner (if present) as a slim, low-contrast inline notice. Alternatives are a small "New" badge next to the language selector, or a one-time tooltip on that selector. The tooltip is best, because the message is useful at the point where people would use it.
- **Style:** neutral grey or soft blue, with a small "New" tag. No icon alarm, no bold background.
- **Copy:** "New: you can now send invoices in Portuguese." Add a text link, **"Try it"**, to the language setting.
- **Dismissal:** an "×" button. Once dismissed, never show it again, and store that per user, not per session.
- **Auto-expire:** stop showing it after about 30 days, even if not dismissed.
- **Accessibility:** `role="status"` (polite), not an alert.

## 3. Keyboard tip: quietest, never a banner

- **Placement:** not at the top. Put it in the context where it applies.
  - Show the shortcut on the "New invoice" button, for example a small `N` key hint beside the label, or in its tooltip on hover.
  - List it in a keyboard shortcuts help panel (`?`).
- **Style:** a plain `N` keycap hint in muted text. No background or banner.
- **Optional:** if you want to teach it actively, show a one-time dismissable toast or hint, but only after the person has clicked "New invoice" by mouse a few times (say 3). Stop for good once they use the shortcut.
- **Accessibility:** expose the shortcut with `aria-keyshortcuts="N"` on the button.

## Rules for the whole screen

1. **Never show more than one banner at once.** Only the card message is a banner. The others are inline or contextual.
2. **Priority order if more messages appear later:** critical (billing, data loss) > time-sensitive (expiring, action needed) > informational (new features) > tips. Only the top tier gets a banner. Everything else is dismissable and shown one at a time at most.
3. **Visual distinction:** the three messages must differ in colour, weight, and position. If they look alike again, people will ignore all of them.
4. **Persistence:** critical stays until resolved. Informational is dismissable and stays dismissed. Tips are contextual and self-retiring.
5. **Shortcut safety:** make sure the `N` shortcut doesn't fire while someone is typing in a text field.

## Summary table

| Message | Loudness | Location | Dismissable | Action |
|---|---|---|---|---|
| Card declined | High (error banner) | Top of screen | No | "Update card" button |
| Portuguese | Low (subtle notice or tooltip) | Near language selector, or slim notice below the banner | Yes, permanently | "Try it" link |
| Press N tip | Minimal (hint) | On the "New invoice" button and in the shortcuts help | Self-retiring | None |

One thing to confirm with your developer: the card state should come from live billing data, so the banner clears right after a successful update without a page reload.
