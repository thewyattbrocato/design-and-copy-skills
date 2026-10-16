**Coordinator, no shifts posted yet**
Title: No shifts yet
Body: Post your first shift and parents can sign up for it. They'll get reminders before they're due.
Button: Post a shift

**Parent, no open shifts**
Title: No open shifts right now
Body: Every shift is taken, or none have been posted yet. Check back later. Your coordinator can post more.

**Reminder permission prompt**
Title: Get shift reminders?
Body: We'll send a notification to this device before a shift you've signed up for. You can turn this off anytime in your browser settings.
Buttons: Turn on reminders / Not now

**Shift just taken**
Title: Someone just took this shift
Body: Another parent signed up a moment ago, so it's no longer open. You haven't been signed up for it. Here are the shifts that are still open.
Button: See open shifts

Notes:
- The "Here are the shifts…" line and button assume the parent lands on the open-shifts list. If none are left, they'll see the "No open shifts right now" screen instead.
- The browser shows its own permission dialog after "Turn on reminders", and you can't change its wording. Show this screen first, and only trigger the browser dialog when they choose "Turn on reminders". If they choose "Not now", don't ask again right away.
