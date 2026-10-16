**Pre-prompt screen**

**Headline:** Find bikes near you

**Body:** Wheelhaus uses your location to show available bikes on the map and to start your ride when you scan a bike.

**Primary button:** Continue
**Secondary button:** Not now

**Notes**

- **Nothing about storage, sharing, or retention.** The copy only states the two uses you're sure of. Avoid lines like "we never store your location" or "your data stays private" until legal signs off. Those are promises, and the screen would be wrong if the policy ends up different. When legal finishes, add one sentence plus a "Learn more" link to the privacy policy.
- **Button labels.** "Continue" fits better than "Allow" because the system dialog comes next, and users shouldn't think they've already granted permission. "Not now" is better than "Don't allow" because it doesn't read as permanent. If they tap it, let them browse the map without location and re-offer the prompt when they try to scan a bike.
- **System dialog string.** On iOS, `NSLocationWhenInUseUsageDescription` is a separate piece of copy. Suggested text: "Wheelhaus uses your location to show nearby bikes and to start your ride when you scan a bike." On Android, the system dialog has no custom text.
- **Scope.** This assumes while-using-the-app access, since both uses happen when the app is open. If you plan to ask for background location (for example, to track a ride in progress), that needs its own prompt and its own copy.

I can also draft a version with a privacy line ready to drop in once legal is done, or a shorter variant if you want to A/B test.
