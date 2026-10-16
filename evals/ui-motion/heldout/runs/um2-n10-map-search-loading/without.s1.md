# Hearthmap loading and failure states

**Principle:** Keep the old results on screen while new ones load, and mark them as updating. Don't blank anything. With a 200ms to 3s range, a single approach has to work at both ends. Fast loads should show nothing, and slow loads should show progress without making the screen jump.

## Timing tiers (apply to every region)

| Elapsed | Behavior |
|---|---|
| 0–300ms | No visible loading UI. Old content stays as is, so a 200ms load looks instant. |
| 300ms–1s | Subtle "updating" cues appear: a thin progress bar and a slight dim on the list. |
| 1s+ | Add explicit status text ("Updating results…"). On the list, skeleton cards replace dimmed cards only if the load exceeds about 1.5s. |
| 10s | Treat as a timeout and use the failure state. |

Once a loading cue appears, keep it for at least about 400ms so it doesn't flicker.

## By region

**Filter bar (the trigger)**
- The changed filter applies immediately and shows its new value, with no spinner on the control. The user's action has to feel acknowledged.
- A 2px indeterminate progress bar sits along the bottom edge of the filter bar. It's the single global "something is loading" signal and spans the full width above both panels.
- Controls stay enabled. If the user changes another filter mid-load, cancel the in-flight request and start a new one. Don't queue them or lock the bar.
- Give multi-select and range filters a short debounce (about 300ms) so rapid tweaks make one request.

**Results list (left)**
- **Fast:** nothing changes.
- **Slow (300ms+):** existing cards dim to about 60% opacity and the list stops accepting clicks. The result count in the header changes to "Updating…", so the old number doesn't look current.
- **Very slow (1.5s+):** replace the cards with skeletons that match the real card layout (photo block, price line, address line, stats). Use the same number of cards as the previous result, capped at about 6, to limit layout shift.
- Reset scroll to the top when new results land. Don't do it while loading.
- **Arrival:** swap in the cards with no animation or a very short fade. Update the count ("128 homes").

**Map (right)**
- Never blank or unmount the map. The user may be panning and zooming, and tiles are independent of the pin data.
- **Slow (300ms+):** old pins fade to about 50% opacity. Don't remove them yet, because that makes the map look empty.
- **Very slow:** a small pill at the top center of the map reads "Updating map…" with a spinner. It sits over the map, so it doesn't shift layout and it's easy to spot if the user is looking there instead of at the list.
- **Arrival:** old pins fade out and new ones fade in together (about 150ms). Don't animate pins one by one.
- If the user pans or zooms during a load, keep the map interactive. Don't stack a second spinner. Let the pill cover it.
- Keep the list and map in sync. Swap both at once when both responses are in. If one is ready first, hold it (up to about 500ms) rather than showing a list that disagrees with the pins.

## Failure

Failure handling should preserve the user's work and make recovery one click.

- **Keep the last good results visible**, in normal opacity but marked stale. Don't replace them with an error page.
- **Inline banner at the top of the list** (not a modal, not a toast that disappears): "Couldn't update results. Showing previous results for [old filters]." with a **Retry** button. Use a warning color plus an icon, not color alone.
- **Map:** a small matching notice in the pill position: "Map not updated · Retry". Both Retry buttons run the same request.
- **Filter bar:** the progress bar stops. The filters the user picked stay selected, and the banner makes clear they don't match what's shown. Optionally, a small dot on the filter bar indicates "not applied."
- **Retries:** retry once automatically and silently for network errors and 5xx responses (after about 1s). Show the banner only if that also fails. Cap the visible retry loop. After two manual failures, add "Check your connection or try again later."
- **Timeout (10s):** the same banner, worded "This is taking longer than expected."
- **First load with nothing to fall back on:** the full list region shows an empty-error state ("We couldn't load homes in this area" with Retry). The map still renders with its base tiles. Don't reuse the "No homes match" copy.
- **Not a failure:** zero results is a successful response. Show "No homes match these filters" with suggestions such as clearing the last filter, and empty the pins normally.

## Accessibility

- Use an `aria-live="polite"` region for status. Announce "Updating results" only when the load passes the 1s threshold, then announce "128 homes found" or the error.
- Set `aria-busy="true"` on the list while loading.
- The progress bar and skeleton pulses should respect `prefers-reduced-motion` (use a static state instead).
- Move focus to the Retry button only if the user is already interacting with the banner. Don't steal focus.

## Summary

The filter bar owns the global progress cue, the list owns its own dim-then-skeleton states, the map keeps its tiles and shows a floating pill, and failures leave the last results in place with a banner and Retry in both panels.
