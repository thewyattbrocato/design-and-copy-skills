# Hearthmap loading design

**Feel:** quiet and crisp. Assumptions: web, filters are used often, CSS transitions, and system reduced-motion is honored.

## Core principle

Filter changes are frequent, so the screen should stay still while they load. The list and map never go blank. The old results stay visible and are replaced in place when the new ones arrive. One wait gets one indicator. The indicator sits on the thing that was changed and on the surface that is about to change. It doesn't go in the center of the screen.

## What shows, by wait time

| Elapsed | Filter bar | List (left) | Map (right) |
|---|---|---|---|
| **0–100 ms** | The chip or control pressed shows its new state at once (selected, value applied). This is the acknowledgment. | No change. | No change. |
| **100–300 ms** | Nothing else. | Stay still. Don't show a loader. | Stay still. Pins don't change yet. |
| **300 ms–1 s** | A thin 2px indeterminate progress line appears along the bottom edge of the filter bar. It's the single loading indicator. | Old cards dim to about 60% opacity over 150 ms. They stay readable, but you can't click into them. The result count reads "Updating…". | Old pins stay put and dim slightly. No overlay. |
| **Over 1 s** | Add a text label next to the line, e.g. "Searching Capitol Hill…". | Same as above. | Same as above. |
| **Over about 8 s** | Treat as a failure (see below). | | |

Once the progress line has appeared, it stays for at least 400 ms, so it doesn't flash. Under 300 ms, the user sees only the swap.

## The swap when results arrive

- **List:** the cards crossfade from old to new over 150 ms and opacity returns to 100%. There's no stagger and no slide, because this happens on every filter change.
- **Map pins:** pins that appear fade in over 150–200 ms. Pins that leave fade out over about 120 ms. Pins that persist don't move or re-animate. This tells the user what actually changed. If the user pans or zooms during a load, don't interrupt them. Load against the new viewport and drop the stale response.
- **Count:** the count updates in place with no count-up.
- **List scroll:** reset to the top, because the results are a different set.
- **Rapid changes:** if the user changes another filter mid-load, cancel the old request and keep the indicator running. Never disable filters while loading. Debounce chip clicks by about 150 ms so quick multi-select doesn't fire many requests.

## First load or a very different area

Use skeletons only when there's nothing old to keep on screen, such as the first visit or a jump to a new city by searching.

- **List:** 4–6 card-shaped skeletons that match the real card layout (image block, two text lines). The shimmer is slow and gentle, or absent.
- **Map:** the base map tiles render immediately. Pins appear when the data arrives, with no pin placeholders. A skeleton on the first paint is the loading state, never an empty frame first.
- Don't use a spinner over the map or a full-screen scrim. These block the map for a wait that is usually under a second.

## Failure

The principle is that a failure never wipes out what the user already has. Pair every motion cue with text, because color or movement alone isn't enough.

1. **Request fails or times out (about 8 s):**
   - The progress line stops and disappears.
   - The old results un-dim and stay on screen. They no longer match the filters, so they must be marked as stale.
   - A persistent inline banner sits at the top of the list: "Couldn't update results. Showing your previous search." It has a **Retry** button. A warning icon and text carry the meaning, not just color.
   - The filter bar keeps the user's chosen filters, so a retry needs no re-entry. The control that triggered the failure gets a small dot or outline so the mismatch is visible.
   - The banner enters with a 200 ms fade, and the list reserves its space so nothing jumps.
   - The banner doesn't auto-dismiss. It clears when a retry succeeds or the user changes the filters again.
2. **Retry:** Retry puts the same progress line back on the filter bar. The banner stays until success.
3. **Partial failure, such as the list loading but the map pins failing:** update the list normally. Show a small inline note on the map: "Pins couldn't load. Retry". The list stays fully usable.
4. **Empty result (not an error):** this gets its own message in the list, "No homes match these filters", with a one-click action to clear or relax the last filter. Don't use the error style.
5. **Offline:** use the same stale banner, with text that says "You're offline".
6. **First load fails, with nothing to keep:** replace the skeletons with an empty-state panel with the message and Retry. Skeletons must not shimmer indefinitely.

## Reduced motion

Remove the crossfades, the pin fade, the shimmer and the moving progress line. Replace them with a static "Updating…" label and the dimmed list. Keep the dimming, the text, the banner and the focus rings.

## Accessibility

Announce "Updating results" and then "42 homes" through a polite live region. Announce the failure message with a polite live region too. Don't move focus on a successful update. On failure, don't force focus either. Focus stays on the filter control the user was using, and the banner is reachable in tab order.

## Spec summary

| Item | Value |
|---|---|
| Loader delay | 300 ms |
| Loader minimum visible time | 400 ms |
| Progress text threshold | 1 s |
| Failure timeout | about 8 s |
| Stale list dim | 60% opacity, 150 ms |
| List swap | 150 ms crossfade, ease-out |
| Pin enter / exit | 150–200 ms / about 120 ms |
| Banner enter | 200 ms fade, ease-out |
| Request cancel | on any new filter or viewport change |
