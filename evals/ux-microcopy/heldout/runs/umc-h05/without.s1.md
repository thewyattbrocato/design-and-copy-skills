# Shiftbook copy

## 1. Coordinator's empty state (no shifts posted yet)

**Headline:** Post your first shift
**Body:** Add a shift and parents can sign up for it. You'll see who's signed up right here.
**Button:** Post a shift

## 2. Parent's empty state (no open shifts)

**Headline:** No open shifts right now
**Body:** Every shift is filled, or none have been posted yet. Check back soon.
**Optional line (if the parent hasn't enabled reminders):** Turn on notifications and we'll remind you about shifts you sign up for.

## 3. Notification permission prompt

This is the screen shown *before* the browser's own permission dialog.

**Headline:** Want a reminder before your shift?
**Body:** We'll send a notification to this device shortly before a shift you've signed up for. We won't send anything else.
**Primary button:** Turn on reminders
**Secondary button:** Not now

**If they block it (shown later, where they'd re-enable it):**
Reminders are off. You can turn them on in your browser's site settings.

Note that these are browser notifications, not email, so the copy says "notification" and "this device." Calling them email-like could confuse parents who then wait for an email that never arrives. The "We won't send anything else" line is only accurate if reminders really are the only thing you send, so cut it if that might change.

## 4. Shift just taken by someone else

**Headline:** Too slow, that shift was just taken
**Body:** Someone else signed up a moment ago. Take a look at the other open shifts.
**Button:** See open shifts

If you'd like a softer tone, use "Someone just beat you to it" as the headline. If no other shifts are open, the button should lead to the empty state in #2, which already covers that case.
