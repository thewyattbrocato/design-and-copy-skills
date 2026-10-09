# Recommended layout for Fernwood notifications

Group the toggles by what the user cares about, put the two master switches at the top, and keep rarely used settings out of sight.

## 1. Channel masters (top, always visible)
- **Push notifications** (master)
- **Email notifications** (master)

When a master is off, gray out and collapse the channel-specific toggles under it. This one change removes a lot of the visual noise.

## 2. Sections below, by topic

**Garden care** (the core value, so list it first)
- Watering reminders
- Frost alerts
- Harvest windows

**Social**
- Friend requests
- Comments on my beds
- Shared bed invites

**Discovery and content**
- New plant suggestions
- Plant-of-the-week

**Email digests and marketing** (email only)
- Weekly summary email
- Product news email
- Sale announcements

## 3. Quiet hours
Don't make it a toggle in the list. Make it a single row ("Quiet hours · 10 PM–7 AM >") that opens a time picker. It's a schedule, not a notification type, so it shouldn't look like the others.

## Other things to consider
- **Use section headers with short descriptions.** For example, "Garden care: timely alerts about your plants."
- **Use sensible defaults.** Garden care and shared bed invites should be on. Marketing (product news, sale announcements) should be off or opt-in.
- **Consider a push/email split per row.** Today the weekly summary and product news are email-only by nature, but watering reminders and comments could reasonably be offered on either channel. If you add per-channel control, use two small toggles or chips per row instead of separate rows. That can cut the list further.
- **Put marketing last, or behind a "Promotions & news" disclosure.** It's the least important group, and hiding it makes the screen look much shorter.
- **Mark time-sensitive alerts.** A small label on frost alerts, such as "Recommended," discourages people from turning off the one notification that can save their plants.

## Result
The screen goes from 14 identical rows to 2 masters, 4 labeled groups, and 1 drill-down row. Users can scan by topic instead of reading every label.

If you tell me your platform (React Native, SwiftUI, web), I can sketch the component structure.
