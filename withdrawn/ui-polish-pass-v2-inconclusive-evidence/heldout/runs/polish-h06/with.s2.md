Don't add both. Pick neither as the default, and add one thing behind a delay.

**Why**

At ~120 ms average, a loader shown immediately will flash on and off. That flicker reads as slower and more jittery than showing nothing. Perceived responsiveness drops off around 100-200 ms, so your typical case is right at the edge where a loader costs more than it helps.

Both together is worse. Two loading indicators in a small dropdown is visual noise, and it doubles the flash.

**Recommendation**

1. **Show nothing for the first ~200-300 ms.** Keep the previous results (or the empty dropdown) on screen while the request is in flight. Most lookups finish inside that window and the user never sees a loading state.
2. **If it's still pending after the delay, show a skeleton of the result rows.** Skeleton fits better than a spinner here because the dropdown has a predictable shape (a few rows of text). It holds the layout, so the list doesn't jump when results arrive.
3. **Once shown, keep it visible for a minimum of ~300-400 ms.** This stops the flash for requests that finish just after the delay threshold.
4. **Use a spinner only as a fallback**, for example a small one in the input's trailing edge if you want a persistent "working" signal. It shouldn't duplicate the skeleton.

**For the 600 ms bad-connection case**

The skeleton appears at ~250 ms and is replaced at ~600 ms. That's a short, legible loading state. If you want to be safe, add a timeout/error row ("Couldn't load suggestions. Keep typing or enter your address manually"), because checkout must never block on autocomplete.

**Also worth doing**

- Announce results to screen readers with an `aria-live="polite"` region (e.g. "5 suggestions available"). Don't announce the loading state itself unless it's long.
- Cancel or ignore stale requests so a slow response for "12 Ma" doesn't overwrite results for "12 Main".
- Debounce input lightly (~100-150 ms) so you aren't firing a lookup on every keystroke.

**To settle design vs. engineering**

Both are partly right, so frame it as: design gets the skeleton, engineering gets the "don't show a spinner flash on a fast call" principle, and the delay logic is what makes either one feel good. If you want data, log how often the lookup exceeds 250 ms. If it's under a few percent, the loader is a rare edge case and shouldn't get much design effort.
