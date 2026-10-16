# Hearthmap loading and failure states

**Principle:** Keep the old results on screen while new ones load, and show progress where the change will land. Don't blank the list or map. A filter tweak is a refinement, so the user should keep their spatial context.

## Timing tiers

The 200ms to 3s range is too wide for one treatment, so use thresholds:

| Elapsed | What the user sees |
|---|---|
| 0–300ms | **Nothing.** Results swap in directly. A spinner that flashes for 200ms looks worse than no indicator. |
| 300ms–1s | **Light signal:** a slim indeterminate progress bar and a dimmed list. |
| 1s+ | **Stronger signal:** the list shows skeleton cards and the map shows a "Updating…" chip. |

Once an indicator appears, keep it up for at least ~400ms so it doesn't flicker.

## Where each indicator goes

**Filter bar**
- The changed filter chip shows a small inline spinner, or its count badge pulses. This confirms the click registered immediately, even before the 300ms threshold.
- A 2px indeterminate progress bar sits along the bottom edge of the bar and spans the full width. It's the single "something is updating" signal for both panels.
- Keep the bar interactive. Users often change several filters in a row, so don't lock it.

**Results list (left)**
- 300ms–1s: keep the existing cards, dim them to ~60% opacity, and disable pointer events on them.
- 1s+: replace the cards with skeletons that match the real card layout (photo block, price line, address line). This avoids layout jump.
- The result count in the header ("128 homes") changes to "Updating…" rather than showing a stale number.
- Preserve scroll position until new results arrive, then reset to top.

**Map (right)**
- Never blank the map or unmount the tiles. The base map stays interactive, so users can pan and zoom while loading.
- Keep the existing pins, but fade them slightly (~50%).
- At 1s+, show a small pill at the top center of the map: spinner plus "Updating homes…". It sits there so it doesn't cover pins or controls.
- When results arrive, fade old pins out and new ones in (~150ms). Don't pop them in.

**Whole screen:** There is no full-page spinner or modal overlay in any case.

## Rapid changes

- Cancel the in-flight request when a new filter change comes in, or ignore its response. The latest request always wins. Otherwise a slow older response can overwrite newer results.
- Debounce text and slider inputs (~300ms). Toggles and chips fire immediately.
- Keep the indicator continuous across back-to-back requests. Don't reset it between them.

## Failure

Treat a failure differently from a slow load, and keep the previous results visible.

- **Where it shows:** An inline banner at the top of the list: "Couldn't update results. Showing previous results for your last filters." It has a **Retry** button.
- **Map:** The loading pill turns into a matching error pill ("Couldn't update map" with Retry). Pins revert to full opacity but are marked stale (see below).
- **Filter bar:** The progress bar stops. The filter chip keeps its selected state, so the UI reflects what the user asked for. Show a small warning dot on the bar, and clear it on success.
- **Mismatch:** The list is stale relative to the filters, so make that obvious. Either keep the banner persistent until resolved or revert the filter control to the last applied state. I'd recommend keeping the banner with Retry, since reverting the filter feels like the app ignoring the user.
- **Retry:** Retry once automatically with a short backoff (~1s) for network errors before showing the banner. The banner's Retry button re-runs with the current filters.
- **First load (no prior results):** The list shows an empty-state error with a Retry button. The map still renders tiles with no pins.
- **Timeout:** Fail after ~10s. At 5s+, change the pill text to "Still working…" so slow areas don't feel frozen.
- **Partial failure** (list succeeds, pins fail, or the reverse): Show each panel's own error independently. Don't fail the whole screen over one.

## Accessibility

- Put `aria-busy="true"` on the list while loading.
- Announce completion through an `aria-live="polite"` region ("128 homes found"), and announce errors the same way.
- Don't rely on dimming alone. Pair it with text or the progress bar.
- Respect `prefers-reduced-motion` by dropping the fades and shimmer.

## Summary

Show nothing under ~300ms. After that, show a slim bar plus dimmed stale content, then skeletons and a map pill past 1s. On failure, keep the stale results, say they're stale, and offer Retry.
