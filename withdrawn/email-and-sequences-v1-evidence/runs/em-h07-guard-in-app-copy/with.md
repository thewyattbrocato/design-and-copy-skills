**1) Delay banner**

> **[Carrier name] updates are running late.** Tracking info may be out of date for up to 30 minutes.

If the banner can't name the carrier, use this:

> **Carrier updates are running late.** What you see here may be up to 30 minutes behind.

**2) Failed-refresh toast**

> Couldn't refresh. Try again.

Alternatives:
- Can't refresh right now. Try again.
- Refresh failed. Tap to retry.

**Notes**
- The banner says "up to 30 minutes" because that's the worst case. It tells people how stale the data might be, so they don't have to guess.
- Neither message blames the user or the carrier, and neither is alarming. The banner is informational, and the toast tells people the next step.
- The toast doesn't separate "no network" from "server didn't answer." On one line, "Try again" covers both. If you can detect offline, "No connection. Try again." is a good variant for that case.
- If your toast has a Retry action button, use "Couldn't refresh" as the text and put "Retry" on the button.
