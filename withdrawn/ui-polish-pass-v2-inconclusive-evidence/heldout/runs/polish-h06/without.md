Neither, and definitely not both. At ~120 ms average, most lookups finish before a loading indicator would be useful.

**Recommendation**

1. **Show nothing for the first ~200–300 ms.** Keep the previous results (or the empty dropdown) in place. Most requests finish within that window, so users never see a flash of loader. A skeleton or spinner that appears and vanishes in 100 ms reads as flicker, and it makes the lookup feel slower than it is.
2. **If the request is still pending after that delay, show one indicator.** This only matters for your 600 ms tail on bad connections. Once it appears, keep it up for a minimum of ~300–400 ms so it doesn't blink out.
3. **Pick the skeleton over the spinner.** The dropdown has a predictable shape (a few rows of text), and a skeleton shows that shape without shifting the layout when results arrive. A spinner is better for unknown-shape or non-list waits. If design and engineering still disagree, the skeleton is the better fit here, and it's an easy call to make on those grounds.
4. **Don't stack both.** Two simultaneous loading signals say "this is slow and we're nervous about it." They also double the motion and the accessibility surface, and they add code to maintain for a state most users rarely see.

**Details that matter more than which loader you pick**

- **Keep stale results while fetching.** When the user types another character, leave the old suggestions visible and dim them slightly, rather than clearing to a loader. That avoids most of the flicker.
- **Debounce input** (~100–150 ms) and **cancel or ignore out-of-order responses**. Otherwise a slow earlier request can overwrite newer results, which is a worse problem than any loader.
- **Accessibility:** use an `aria-live="polite"` region to announce "Loading suggestions" and then "N suggestions available" or "No results." Skeleton rows should be `aria-hidden`.
- **Handle failure and empty states explicitly.** On a bad connection, a timeout or error message with an option to enter the address manually matters more than the loading polish. Checkout must never be blocked by the autocomplete.
- **Respect `prefers-reduced-motion`** by using a static or very subtle skeleton shimmer.

**How to settle the design vs. engineering disagreement**

Frame it as "one indicator, delayed, skeleton-shaped." That gives design the skeleton and gives engineering the restraint they likely want. If you can, check the real latency distribution (p50, p95, p99) rather than the average, since the loader only affects the slow tail. If p95 is under ~300 ms, you may find the loader almost never shows, and that's fine.
