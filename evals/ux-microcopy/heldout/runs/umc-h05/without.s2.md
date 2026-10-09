**Headline**
Find bikes near you

**Body**
Wheelhaus uses your location to show available bikes on the map and to start your ride when you scan a bike.

**Buttons**
- Primary: **Continue** (this triggers the system dialog)
- Secondary: **Not now**

**Notes**

- **The copy only says what you've confirmed.** It covers the two uses you listed and makes no claim about storage, retention, or sharing. Avoid lines like "we never store your location" or "only used while you ride" until legal signs off. If they land on something, add one line and a "Learn more" link to the privacy policy.
- **Keep the primary label neutral.** "Continue" fits because the system dialog still follows. "Allow" or "Enable location" can read as if the choice is already made, and users then get confused when a second prompt appears.
- **Use "Not now" for the secondary button, not "Don't allow".** It doesn't burn your one system prompt. iOS only shows the system dialog once, so if the user taps "Not now" you can ask again later, for example when they open the map or tap Scan. Make sure the map still works without location, for example by letting them pan or search.
- **Check the permission scope.** The copy assumes you'll request "While Using the App" permission. If you also need background location, for example to track a ride in progress, the copy needs to say so, and that is another thing legal will want to review.
- **Match your Info.plist string.** Make `NSLocationWhenInUseUsageDescription` consistent with this copy. For example: "Wheelhaus uses your location to show bikes near you and to start your ride when you scan a bike."

If you'd like a warmer or shorter variant, I can write one.
