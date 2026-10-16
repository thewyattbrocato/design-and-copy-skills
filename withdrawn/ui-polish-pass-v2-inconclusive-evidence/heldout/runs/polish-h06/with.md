Don't add both. Pick neither as the default, and add one conditionally.

**Why**

- At about 120 ms, a loader of any kind is a net negative. Responses under roughly 100–200 ms read as instant. A skeleton or spinner that appears and vanishes in that window shows up as a flash, which looks worse than no loader.
- Both together is redundant. They say the same thing ("loading") twice, which adds visual noise in a small dropdown and doubles the layout shifts and accessibility announcements.
- The slow case is the only one that needs help, and it's the 600 ms tail.

**What I'd do**

1. **Delay the loading indicator by about 200 ms.** If results arrive before that, the user never sees a loader. Only the slow connections get feedback.
2. **Once it shows, give it a minimum display time of about 300–400 ms.** This prevents it from flickering off a moment after it appears.
3. **Keep the previous results on screen while the new query is in flight.** Don't blank the dropdown on every keystroke. This does more for perceived speed than any loader.
4. **Use a skeleton, not a spinner, for the delayed state.** Autocomplete results are a list of known shape (rows of address text). A skeleton holds the dropdown's height steady and avoids a jump when results land. A spinner in an empty box is the weaker fit here. If engineering wants a spinner for a technical reason, a tiny inline one in the input's trailing edge is the usual compromise, but use it instead of the skeleton, not alongside it.
5. **Cover the other states:**
   - Announce loading and result counts with `aria-live="polite"` (and `aria-busy` on the listbox).
   - Handle empty results ("No matches").
   - Handle errors with a retry.
   - Cancel or ignore stale responses so a slow earlier request can't overwrite a newer one.

**To settle the design vs. engineering disagreement**

Both are right about the slow case and both are wrong to optimize for it as the default. Frame it as "no loader for the fast path, skeleton after a 200 ms delay." That gives design their skeleton and gives engineering a simple, low-cost implementation. Then check your real latency distribution. If the p95 is near 600 ms, tune the delay. If most users never hit 200 ms, you've avoided shipping a loader nobody sees.
