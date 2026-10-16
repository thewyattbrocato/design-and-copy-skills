Here's the copy for each screen.

## 1. New coordinator, no shifts yet

**Headline:** No shifts yet
**Body:** Post your first shift and parents can sign up for it.
**Button:** Post a shift

## 2. Parent, no open shifts

**Headline:** No open shifts right now
**Body:** Every shift is covered, or none have been posted yet. Check back soon.

(Add "We'll remind you about shifts you sign up for" only if parents can get reminders before they've signed up for anything. Otherwise leave it out.)

## 3. Push notification permission prompt

This is the screen shown *before* the browser's own permission popup. Make it clear these are browser notifications, not email.

**Headline:** Want a reminder before your shift?
**Body:** We'll send a notification to this browser shortly before a shift you've signed up for. That's all we'll use it for.
**Primary button:** Yes, remind me
**Secondary button:** Not now

**If they decline or block it:**
"No problem. You can turn reminders on later in your browser settings."

Only show the browser's real popup after they tap "Yes, remind me". If they tap "Not now", you can ask again later. If they deny the browser popup itself, most browsers won't let you ask again, so the fallback message matters.

## 4. Shift just taken by someone else

**Headline:** Sorry, that shift was just taken
**Body:** Someone else signed up a moment before you. Take a look at the other open shifts.
**Button:** See open shifts

If no other shifts are open, swap the body for: "Someone else signed up a moment before you. There aren't any other open shifts right now."

Two notes:
- I wrote "browser notification" instead of "push notification" in the prompt. Parents will recognize it, and it avoids the email confusion.
- The "Not now" button keeps the prompt from feeling pushy on a first release.
