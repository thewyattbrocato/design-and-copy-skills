# Hearthmap loading states

**Principle:** a filter change updates existing content. Keep the old results and pins on screen until the new ones arrive. Don't blank anything. Show loading feedback only if the wait passes a threshold, so the 200ms case doesn't flicker.

## Timing tiers

| Elapsed | What the user sees |
|---|---|
| 0–300ms | **Nothing new** except the filter chip's applied state. Results swap in directly, with no spinner, skeleton or dimming. |
| 300ms–1s | **Light signal:** a thin progress bar and a dimmed list. |
| 1s+ | **Fuller signal:** the list shows a "Updating…" label and the map shows a pill. |
| Failure | See the failure section below. |

Tune the 300ms threshold in testing. Hold any indicator that has appeared for at least ~400ms so it doesn't flash.

## Where loading shows up

**1. Filter bar: acknowledge the input instantly (0ms).**
- The changed chip or control goes to its applied state immediately. This isn't loading, it's confirmation, so it never waits on the network.
- Below the bar, show a 2px indeterminate progress line across the full width, appearing only after 300ms. It's the single global "something is in flight" cue and takes no layout space.
- Keep the filters interactive. If the user changes another filter, cancel the in-flight request and start a new one. Never lock the bar.

**2. Results list (left): the primary loading surface.**
- **Under 1s:** keep the old cards, dim them to ~60% opacity, and disable pointer events on them. Scroll position stays put until new data arrives, then reset to top.
- **Over 1s:** the result count in the list header ("124 homes") changes to "Updating…" with a small inline spinner. Don't replace the cards with skeletons yet, because that throws away context for a wait that may be nearly over.
- **Skeletons only for the first load or a large area change** (such as a new city), where old results are irrelevant. Use 4–5 card-shaped skeletons that match the real card layout, with a gentle shimmer.
- Update the count and cards together, in one swap, to avoid layout jumps.

**3. Map (right): keep it calm and keep it usable.**
- The map stays pannable and zoomable during loading. Never overlay a blocking spinner.
- Leave the old pins in place. Don't clear them, because an empty map reads as "no results."
- After ~1s, show a small pill at the top center of the map: "Updating pins…" with a spinner. This is out of the way of the zoom controls and the pins.
- When data arrives, fade old pins out and new ones in over ~150ms. Pins that persist across both result sets stay put, so they don't flicker.
- If the user pans or zooms mid-load, cancel and re-request for the new viewport, and keep the same pill.

## Failure

Failure should be visible, local and recoverable. The user should never see an unexplained empty state.

- **Keep the last good results** in the list and on the map, restored to full opacity but marked as stale.
- **List:** a banner pinned at the top of the list: "Couldn't update results. Showing previous results." with a **Retry** button. Use a warning treatment (amber, with an icon, not color alone). Announce it to screen readers with `role="alert"`.
- **Filter bar:** the progress line stops, and the changed chip gets a small warning dot with a tooltip, "Not applied to results yet". This avoids a mismatch where the chips say one thing and the results show another.
- **Map:** the pill changes to "Pins out of date" with a retry icon. Don't use a modal or toast that covers the map.
- **Retry:** one click re-runs the request. Retry once automatically and silently for network blips, then show the banner. After repeated failures, add "Check your connection" or "Try different filters" as appropriate.
- **Timeout:** treat anything over ~10s as a failure, so the user doesn't wait indefinitely.
- **First load fails (nothing stale to show):** show a full list-pane empty state with an illustration, "We couldn't load homes," and a Retry button. The map shows its base tiles only.

## Distinguish failure from "no results"
Zero results is a successful response. Show "No homes match these filters" in the list, with a "Clear filters" action and a hint at which filter is most restrictive. The map shows no pins. This must look clearly different from the error banner.

## Accessibility
- Use `aria-busy="true"` on the list during loading.
- Announce the result count when it changes ("124 homes found") via a polite live region.
- Don't rely on the dimming alone. The spinner and label carry the meaning.
- Respect `prefers-reduced-motion` by replacing the shimmer and fades with static states.
