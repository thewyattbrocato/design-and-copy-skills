**Banner** (about two lines)

> **{Carrier} updates are delayed**
> Tracking info may be up to 30 minutes out of date.

If you want it as one sentence, use: "{Carrier} is running behind, so tracking info may be up to 30 minutes old."

**Toast** (one line)

> Couldn't refresh. Try again.

**Notes**
- The banner says "may be," because the feed only sometimes lags and the package may well be fine.
- "Up to 30 minutes" tells people how stale the data could be without promising a fixed delay.
- The toast leaves out "check your connection," because a failed refresh can also mean the server didn't answer, and that isn't the user's fault. If you want a hint, "Couldn't refresh. Check connection and retry." fits on most phones, but I'd keep the shorter version.
- If the carrier name might be missing or very long, use "Carrier updates are delayed" as the fallback so the headline doesn't wrap.
