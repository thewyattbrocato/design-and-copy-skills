# Invoices screen: message hierarchy

**Job of the screen:** let a freelancer see and act on their invoices. The messages are secondary to that, except the one that threatens the account.

**Rank:** card declined (1), then Portuguese (2), then the N shortcut (3). Only the card message is urgent. It has a deadline, a consequence, and a required action.

## 1. Card declined: loud, top of the screen

- **Placement:** full-width banner above the page content, pinned above the invoice list. It's the only banner on the screen.
- **Style:** the only red/danger-tinted element on the screen. Use a solid tinted background with a stronger left edge or border, plus a warning icon. The icon is a second cue, so it still reads without color.
- **Copy:** keep it as written, but bold "declined" and the date "14 March" so it scans.
- **Action:** one solid primary button, **Update card**, right-aligned in the banner. It links straight to the payment form. This is the only solid primary button in the banner area.
- **Dismissal:** not dismissible. It clears when the card is fixed.
- **Accessibility:** `role="alert"` (or `role="status"` if it renders after load and you don't want it announced aggressively). Check text contrast on the tint.
- **Optional:** show a countdown ("pauses in 5 days") once the date is within about 7 days. Don't invent urgency before that.

## 2. Portuguese: quiet, once, dismissible

- **Placement:** below the invoice list header, or as a small card in the page's side area. It must not sit above the list or touch the red banner.
- **Style:** no fill and no color banner. Use neutral text on the page background with a small "New" tag. Pair it with a text link, **Try it**, that leads to the language setting. No button.
- **Dismissal:** an × button. Once dismissed, or once they've used the feature, never show it again (store this per user).
- **Rule:** show it only when the card banner is absent, or defer it until the next session. Two attention-seeking messages at once cancel each other out.

## 3. "Press N": almost invisible, in context

- **Placement:** not a banner. Put it where it's useful: as a hint next to the **New invoice** button (a small `N` keycap badge on or beside the button), plus a tooltip on hover.
- **Style:** small, muted gray text. No background, no icon, no border beyond the keycap.
- **Lifetime:** hide it permanently once the user has pressed N or created, say, 3 invoices. Don't show it on touch devices.
- **If you want a text tip:** put it in an empty state or in a help menu, not on this screen.

## Rules for the developer

- Build one message component with three variants: **critical**, **announcement**, **hint**. Don't reuse the blue banner for any of them.
- Show **at most one** top-of-page message at a time. Priority: critical, then announcement. Hints never take banner space.
- Blue stops being the default message color. Red is reserved for the critical variant, so it keeps its meaning.
- Persist dismissals per user, not per session.
- Check in grayscale: the card message should still be the obvious one, from weight, icon, and button, not only color.

**Assumptions:**
- I'm assuming the app has a settings page for language and a New invoice button on this screen.
- I didn't specify exact colors or sizes. Use your design system's danger and neutral tokens.
