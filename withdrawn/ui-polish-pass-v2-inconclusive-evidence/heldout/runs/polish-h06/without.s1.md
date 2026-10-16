Don't add both. Two loading indicators for one wait is noisy, and at your latencies the bigger risk is flicker, not a missing loader.

**What I'd do**

1. **Show nothing for the first ~250-300 ms.** At 120 ms average, most lookups finish before a loader would help. A skeleton or spinner that flashes for 100 ms reads as jank and is slower-feeling than no indicator.
2. **Keep the previous results on screen while the next lookup runs.** As the user types, the list updates in place. This removes most of the need for a loader.
3. **If the lookup passes the threshold, show one indicator.** This only happens in your 600 ms tail.
   - **Skeleton rows** fit if the dropdown is empty, such as on the first keystroke. They reserve the right height, so the list doesn't jump.
   - **A small spinner in the input's trailing edge** fits if stale results are already showing. A skeleton would replace useful content with placeholders.
4. **Once an indicator appears, keep it up for at least ~300-400 ms.** This prevents it from flashing on and off.

**On the disagreement**

Design and engineering are each right about a different state: skeleton for the empty dropdown, spinner for refreshing existing results. If you want one rule to give both sides, use that split. If you want the simplest version, use a skeleton only when the dropdown is empty and show nothing otherwise.

**Other things to check**

- Announce loading and result counts to screen readers, for example with an `aria-live="polite"` region. A visual loader doesn't help them.
- Cancel or ignore stale responses so a slow earlier request can't overwrite newer results.
- Test on throttled network, since the 600 ms case is where the delay and minimum-display timings matter.

The 250 ms delay and 300-400 ms minimum are starting points. Tune them by watching the real latency distribution rather than the average.
