Don't add both. Two loading indicators for one request is noisier, not more polished. At these latencies the bigger issue is whether you need an indicator at all.

**What I'd do**

1. **Delay the indicator by about 200-300 ms.** At 120 ms average, most lookups finish before anyone could register a loader. Showing one anyway makes the dropdown flash a loader and then swap to results, which feels slower than showing nothing. Only the slow tail (up to 600 ms) needs feedback.
2. **Once it shows, keep it up for at least about 300-400 ms.** That avoids a flicker when a response lands just after the delay.
3. **Keep the previous results visible while a new request is in flight.** Don't clear the list on each keystroke. This does more for perceived speed than either loader.
4. **Use one indicator: a small spinner at the trailing edge of the input.** I'd go with the spinner over the skeleton for these reasons:
   - A skeleton promises a shape, and you don't know how many suggestions will come back (0, 2 or 5). Swapping it for real rows causes layout jump, and an empty result looks worse.
   - The spinner doesn't change the dropdown's size, so nothing shifts when results arrive.
   - It's cheap to build and easy to keep consistent with other inputs.
5. **Add accessibility.** Put a polite live region on the status, such as "Loading suggestions", and "No matches" for empty results. Respect `prefers-reduced-motion` for the spinner.

**How to settle the design vs. engineering disagreement**

Both are right about different things. Design wants the dropdown to feel intentional while loading, and engineering wants something simple that doesn't shift. If design feels strongly, a skeleton is fine, but use a fixed number of rows (2-3) and only when the dropdown has nothing to show yet. Still don't pair it with a spinner.

If you have analytics, check the real p95 and p99 latency and how often requests exceed your delay threshold. If that's under a few percent, the delayed spinner will almost never be seen, which is what you want.
