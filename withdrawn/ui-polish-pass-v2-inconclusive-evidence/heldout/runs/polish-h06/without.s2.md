Don't add both, and don't show a loader on every keystroke either.

**Why**
- At about 120 ms, a loader appears and disappears faster than people can read it. It reads as a flicker and makes the field feel slower than it is.
- Skeleton and spinner together say "loading" twice in the same spot. That's more motion for a wait that's usually imperceptible.

**What I'd do**
1. **Show nothing for the first ~300 ms.** Under about 100 ms feels instant, and 120 ms is close enough that no feedback is needed. This covers most requests.
2. **Keep the previous results visible while the next request is in flight.** Dim them slightly if you like. This avoids empty-dropdown flashes while typing.
3. **If a request is still pending after ~300 ms, show a small spinner.** Put it in the input's trailing edge or at the top of the dropdown, not as a replacement for the list. This is your 600 ms bad-connection case.
4. **Once the spinner shows, keep it up for at least ~300–400 ms.** That way it doesn't blink on and off if the response lands just after the threshold.
5. **Handle the rest of the request lifecycle.** Cancel or ignore stale requests so slow responses don't overwrite newer ones. Show a clear "No matches, enter manually" state, and an error state with a manual-entry fallback.
6. **Cover accessibility.** Use an `aria-live="polite"` region for "Loading suggestions" and for "N suggestions available". Don't rely on the visual indicator alone.

**Spinner or skeleton?**
Go with the spinner for this case. A skeleton works when you know the shape of what's coming, like a card grid. Here the result count is unknown (0–8 rows), so skeleton rows are a guess and can cause layout shift when the real list differs. A small spinner is cheaper and more honest. If design feels strongly, skeleton rows are a reasonable swap for the delayed indicator in step 3. Just keep it to one indicator, shown only past the delay.

**Settling the disagreement**
Ship the delayed version and check your real latency distribution (p50/p95) in production. If p95 is well under 300 ms, the loader will rarely appear, which means the spinner-versus-skeleton question matters much less than it feels like it does now.
