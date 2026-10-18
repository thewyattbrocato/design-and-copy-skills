# Recommended layout: group by channel and purpose, with masters on top

**Top level (always visible)**
1. **Push notifications** (master toggle)
2. **Email notifications** (master toggle)
3. **Quiet hours** (a row that opens a time picker, not a toggle)

**Grouped sections below**

| Section | Items | Channel controls |
|---|---|---|
| **Garden care** (the core value) | Watering reminders, Frost alerts, Harvest windows | Push, plus email if wanted |
| **Community** | Friend requests, Comments on my beds, Shared bed invites | Push, plus email if wanted |
| **Discover** | New plant suggestions, Plant-of-the-week | Push or email |
| **Email digests and news** | Weekly summary, Product news, Sale announcements | Email only |

**Key decisions**

- **Masters first, and they gate everything.** If push is off, grey out and collapse the push-only items under it, with a line like "Push is off. Turn on to choose alerts." Users shouldn't have to wonder why a toggle does nothing.
- **Quiet hours is a setting, not a notification type.** Make it a tappable row showing its current value ("10 PM – 7 AM"), and keep it near the push master since it only affects push.
- **Put time-sensitive items first.** Frost alerts and watering reminders are why people use the app, so they lead. Marketing (sale announcements, product news) goes last.
- **Consider per-row channel chips instead of 14 toggles.** If most items can be sent by both push and email, each row can show "Push · Email" chips. That's fewer rows overall, and the masters make sense as global switches.
- **Use section headers with one-line descriptions.** For example, "Garden care: timely alerts about your plants." This makes the list scannable.
- **Make defaults sensible.** Care alerts on, and marketing off (or opt-in). Most people never open this screen, so defaults matter more than the layout.
- **Add a "Pause all" or "Marketing off" shortcut at the top** if you want a quick fix for people who are overwhelmed.

**If you want to go further:** make the top level a short list of 4 rows (Garden care, Community, Discover, Email & news). Each row shows a summary like "3 on" and opens a detail screen. This is best if the list will grow. At 14 items, grouped sections on one screen are usually enough.

I can sketch this as a wireframe in HTML or SwiftUI/React code if that would help.
