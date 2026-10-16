I'd group the toggles by what they're about, put the two master switches at the top, and use progressive disclosure so people don't see 14 rows at once.

## Structure

**1. Delivery channels (top, always visible)**
- Push notifications (master)
- Email notifications (master)
- Quiet hours (tap to expand: start and end time, and optionally which days)

These gate everything below. When a master is off, grey out or collapse the rows that depend on it, so people see why nothing arrives.

**2. Garden care** (time-sensitive, the core value of the app)
- Watering reminders
- Frost alerts
- Harvest windows

**3. Social**
- Friend requests
- Comments on my beds
- Shared bed invites

**4. Discovery and tips**
- New plant suggestions
- Plant-of-the-week

**5. Email and marketing** (visually quietest, at the bottom)
- Weekly summary email
- Product news email
- Sale announcements

## Layout choices that reduce the overwhelm

- **Use section headers with one-line descriptions.** For example, "Garden care: alerts about your plants and weather." Headers let people scan instead of read every row.
- **Give each row a short subtitle only where the label is ambiguous.** "Harvest windows" could use "When crops are ready to pick." Skip subtitles on self-explanatory rows.
- **Split by channel only where it matters.** If people might want frost alerts by push but not email, make each row tappable to a detail screen with Push and Email checkboxes. The main screen then shows a summary like "Push, Email". This replaces what would otherwise be a doubled toggle list.
- **Collapse the low-priority groups.** Social and Discovery can start collapsed, with a summary like "3 of 3 on". Garden care stays open.
- **Set sensible defaults.** Care alerts and shared bed invites on, marketing off. Most people never open this screen, so the defaults matter more than the layout.
- **Consider a "Pause all" shortcut.** Quiet hours covers scheduled silence, but a one-tap "Pause for 1 week" is useful for people on vacation.

## Two notes

- Quiet hours and the masters are *settings*, not *notification types*. Visually separate them from the toggles, for example with a card at the top, so they don't read as one more item in the list.
- Frost alerts are the one type where a missed notification can cost someone their plants. Consider keeping them on by default even if the user turns off other push categories, or show a gentle confirmation when they turn them off.

If you share a screenshot or mockup, I can critique the specific design.
