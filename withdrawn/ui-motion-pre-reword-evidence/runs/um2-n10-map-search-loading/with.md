# Hearthmap loading design

**Feel:** calm and decisive. Filtering is a frequent action, so the loading treatment should be quiet and hold the layout still.

## Principles

1. **Keep the old results on screen.** A filter change replaces content that has the same shape, so there is nothing to build from scratch. Dim the stale content slightly. Don't blank it or swap it for skeletons.
2. **One wait gets one indicator.** The wait is one event, so show one indicator, not one per region.
3. **Show nothing until the wait is long enough to notice.** The wait can be 200 ms or 3 s, and the treatment follows the timing.

## Timing tiers

| Elapsed | What the user sees |
|---|---|
| 0–100 ms | The filter chip shows its pressed or active state right away. This is input acknowledgment. It is not a loader. |
| 100–300 ms | Nothing else changes. Most fast areas finish in this window, so no loader flashes. |
| 300 ms–1 s | The results list and map pins dim to about 60% opacity over 150 ms. A 2px indeterminate line runs along the bottom edge of the filter bar. |
| 1 s+ | Same as above, plus a small "Updating…" label in the list header where the result count normally sits. |
| Done | The new content swaps in. The list and pins fade from 60% to 100% over 150 ms. The count updates. |

Once the dim and line appear, keep them for at least 400 ms so they don't flicker. For a result that lands at 350 ms, it's better to show nothing and swap the content directly.

## Where each piece lives

**Filter bar (the cause).**
- The changed chip or control shows its active state immediately. Keep every other control enabled. The user may change a second filter mid-load.
- The thin progress line sits on the bar's bottom edge. It is the single "something is happening" signal, and it's near where the user acted. Use a looping indeterminate sweep at a steady rate. Don't fake a percentage.

**Results list (left).**
- Keep the old cards at about 60% opacity, with the scroll position preserved until the swap.
- Dimmed cards stay clickable. Disabling them gains nothing and punishes someone who spotted the card they wanted.
- The count in the header changes to "Updating…" after 1 s, then to the new count ("128 homes").
- On swap, scroll the list to the top, since the old position no longer means anything.
- Don't stagger the new cards. This is a frequent path, so they appear all at once with the 150 ms fade.

**Map (right).**
- Don't dim the whole map. Panning and zooming must keep working, and a veil over the tiles looks like a break.
- Fade only the pins to about 50% and keep the base map fully visible.
- Pins cross-fade to the new set over 150 ms, with no travel and no pop-in animation, because 200+ pins moving at once is noise.
- If the viewport moves (a location filter), pan the camera first and fade the pins after it settles, so the pins don't land in the wrong place.

**Interruption.** A new filter change cancels the in-flight request and restarts the cycle from the current dimmed state. The line keeps running. Nothing resets to full opacity in between, which avoids flicker.

## Failure

Never let a failure leave the dimmed state hanging, and never silently show stale results as if they matched the filters.

**Failed request (network, 5xx, timeout):**
- Stop the progress line and restore the content to 100% opacity.
- Mark the list's stale state honestly. Put a persistent inline banner at the top of the list, not a toast: "Couldn't update results. Showing the previous search." It has a **Retry** button.
- Fade the banner in over 200 ms with about 8px of travel. No shake. Reserve space for it or insert it without shifting the card the user is looking at. Don't scroll.
- Keep the filter bar's changed chip in its selected state but add a small warning mark. The user's intent is preserved, and it's clear that the results don't reflect it.
- Retry reruns the normal loading sequence. If it works, the banner exits with a quick 120 ms fade.
- The banner needs to be announced to assistive tech (`role="status"` or `alert`), and focus stays where it was.

**Slow beyond the norm (about 8–10 s):** change the "Updating…" label to "Still working…" and add a **Cancel** link that reverts the filter. Time out around 15–20 s and show the error state.

**Partial failure (list OK, pins fail):**
- Show the new list normally and leave the old pins at 100%.
- Put a small note on the map: "Map pins didn't update. Retry". Don't fail the whole screen over half of it.

**Zero results (success, not failure):**
- Use a distinct empty state: "No homes match these filters", with a suggestion such as "Clear the last filter". Don't reuse the error banner, because empty and broken look different and mean different things.

## Spec in numbers

| Moment | Duration | Easing | Notes |
|---|---|---|---|
| Chip pressed state | 100 ms | ease-out | Immediate |
| Loader delay | 300 ms | n/a | Nothing is shown before this |
| Dim list / pins | 150 ms | ease-out | Opacity to 0.6 (list), 0.5 (pins) |
| Progress line | looping, ~1.2 s per sweep | linear | 2px tall, indeterminate |
| Minimum visible time | 400 ms | n/a | Once shown, avoid flicker |
| Content swap | 150 ms | ease-out | Opacity only, no stagger |
| Error banner in | 200 ms | ease-out | 8px upward travel and fade |
| Error banner out | 120 ms | ease-in | Fade |

All of it animates opacity and transform only.

**Reduced motion:** replace the sweeping line with a static or slowly pulsing bar, or just the "Updating…" label. Keep the dim and the opacity changes, since they aren't movement. Drop the banner's travel and keep its fade. The text, the Retry button and the warning mark carry the error either way.

## Choices I'd flag

- **Why no skeletons:** they fit a first load or a cold start, where there is no previous content. The very first search on page load should use skeleton cards, and the map should show its base tiles with no pins.
- **Why a 300 ms delay:** it keeps the fast end of your range (200 ms) from flashing. The slow end (about 3 s) is covered by the dim, the line and the label.
- **One thing to test:** throttle the network and CPU and check that the dim never runs before the old content is still on screen, and that there is no empty frame between states.
