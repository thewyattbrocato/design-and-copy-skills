# Hearthmap filter-change loading

**Feel:** quiet and crisp, like a focused productivity tool. Filters get changed often, so the loading treatment should stay light.

**Principle:** keep the old results on screen and mark them as stale. Don't blank the page or replace the list with skeletons. A filter change is a refinement of what people already see, and they often keep scanning the old results while the new ones load. One wait gets one indicator.

## By wait time

| Elapsed | Filter bar | List (left) | Map (right) |
|---|---|---|---|
| **0–100 ms** | The changed chip or control shows its active state right away. | Nothing changes. | Nothing changes. |
| **100–300 ms** | Nothing more. | Still nothing. | Still nothing. |
| **300 ms–1 s** | A 2px indeterminate progress line appears along the bottom edge of the filter bar. | Old cards dim to about 60% opacity over 150 ms. The scroll position holds, and the cards stay clickable. | Old pins stay put. The map is not dimmed. |
| **1 s+** | The line stays. A small label next to the result count replaces it with "Updating results…". | Same as above. | A small "Updating map…" pill sits at the top center of the map, only if the map is also waiting. |
| **Done** | The line and label fade out over 150 ms. | Opacity returns over 150 ms and the cards swap in place. The count updates. | Old pins fade out over 120 ms. New pins fade in over 200 ms with no stagger. |

**Why the bar:** it's the one place all three regions have in common. The control that started the action is also in the bar, so the indicator sits close to what the person did. The progress line is indeterminate because we can't know real progress.

## Rules that keep it from feeling janky

- **Nothing under 300 ms.** The common fast case (200 ms) should show no loader at all. Once the line appears, keep it for at least 400 ms so it never flashes.
- **Don't change layout.** Reserve the space for the progress line and the label. The result count should hold its width so nothing shifts.
- **Don't clear the map.** An empty map then a refill looks like a crash. Cross-fade the pins, and don't move the viewport unless the filter changes the area.
- **Keep input live.** The person can change another filter while the first request is in flight. Cancel the old request and restart the indicator. Don't disable the filters.
- **Pins use opacity only.** Don't animate pin positions or add bounce. With hundreds of pins, only opacity and transform are cheap enough.
- **A new request resets the 300 ms timer.** Rapid filter changes then show one continuous loading state.
- **Pagination or panning.** If the map is panned and only the pins reload, show only the map pill and leave the list alone.

## If it fails

A failure needs a persistent message in text. The motion only supports it.

1. **Stop the loading state.** The progress line and dimming end, and the old results return to full opacity. They stay as they were, so the person isn't left with nothing.
2. **Show an inline banner at the top of the list**, under the filter bar, with a warning icon and plain text: "Couldn't update results. Showing your previous search." Add a **Retry** button.
   - The banner pushes nothing around: reserve a slot, or overlay it at the top of the list.
   - It fades in over 200 ms with a few pixels of travel.
   - It stays until the person retries, changes a filter or dismisses it. Don't auto-dismiss it, because it carries an action.
3. **Mark the mismatch.** The filter bar shows the new filter values, but the results are from the old ones. Show the changed chip with a small warning dot until the retry succeeds. Otherwise the person could trust results that don't match the filters.
4. **Move focus** to the Retry button only if the person hasn't moved on. Announce the error to screen readers with `aria-live="polite"`.
5. **Retry** starts the same loading sequence. The banner fades out over 120 ms on success.
6. **Map only fails:** show the same banner on the map ("Couldn't load pins. Retry"), and keep the list. Don't fail the whole view for a part of it.
7. **Timeout:** at about 10 s, treat it as a failure and show the banner. Don't let the progress line run forever.
8. **Errors don't shake.** Skip the shake, because nothing here is a field the person got wrong.

## Edge cases

- **First load (no old results yet):** use skeleton cards shaped like listing cards, with a static or very slow shimmer, from the first paint. The map shows its base tiles, with the pins arriving after. Never show an empty frame before the skeleton.
- **Empty results:** this is a successful response, not an error. Show "No homes match these filters" with a "Clear filters" action, and fade the old pins out.
- **Slow connection (3s+):** nothing new is added. The label and line are enough, and the person can keep scrolling the old list.

## Reduced motion

Replace the sliding or traveling parts with opacity changes. The progress line becomes a static "Updating…" label with no moving animation. The dimming, pin fades and banner keep working since they're opacity only. Keep the focus rings.

## Specs

| Element | Trigger | Duration | Easing |
|---|---|---|---|
| Progress line | 300 ms after request, min 400 ms visible | fade 150 ms | linear loop |
| List dim | with the line | 150 ms | ease-out |
| Pins out / in | on response | 120 / 200 ms | ease-in / ease-out |
| Error banner in / out | on failure / on retry success | 200 / 120 ms | ease-out / ease-in |

Interruption: a new filter change cancels the request and restarts the timer without any reset animation.
