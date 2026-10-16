**Pre-prompt screen**

**Headline:** See bikes near you

**Body:** Wheelhaus uses your location to show available bikes on the map and to start your ride when you scan a bike.

**Buttons**
- Primary: **Continue** (this triggers the system dialog)
- Secondary: **Not now** (this lets people browse the map without location)

**Notes**

- **The copy only says what you've confirmed.** It names the two uses, the map and ride start, and makes no claims about storage, retention, or sharing. Avoid adding lines like "we never store your location" or "your data stays private" until legal signs off. If those claims turn out to be wrong, they could be a real liability.
- **Add a privacy link later if legal wants one.** Once the policy is settled, a small "How we use location" link under the body text is the usual spot. Anything about retention goes there, not in the headline or body.
- **Use "Continue" rather than "Allow" for the primary button.** The system dialog has its own Allow/Don't Allow choice. A pre-prompt button that says "Allow" can read as the actual permission grant, and Apple's review guidelines discourage that kind of confusion.
- **Your iOS `NSLocationWhenInUseUsageDescription` string is separate copy.** It appears inside the system dialog and has the same constraint. Something like "Wheelhaus uses your location to show nearby bikes and start rides" works without making data-handling claims. I can draft it, plus a "Location is off" fallback screen for people who tap Not now, if you want.
