**Anchor:** calm and decisive. Filtering is a frequent action, so the rule is to keep everything still and put exactly one indicator on the thing that is waiting.

## Where it shows up

- **Filter bar:** the control you just changed gets its pressed or applied state within 100 ms. This is the acknowledgment, and it isn't a loader.
- **Results list:** keep the old results visible. Don't blank the list or swap in a skeleton.
- **Single indicator:** a thin indeterminate progress bar sits on the bottom edge of the filter bar, which is the boundary between the input and what it affects. The result count in the list header ("128 homes") changes to "Updating…" as its text label.
- **Map:** pins stay where they are and nothing covers the map. It stays pannable and zoomable.

Don't put a spinner on the map and another on the list. One wait should get one indicator.

## Timeline by wait length

| Elapsed | What the user sees |
|---|---|
| 0–100 ms | Filter control shows its applied state. Nothing else changes. |
| 100–300 ms | No loader. The list and map stay still. Most responses in the 200 ms case land here and just swap. |
| ~300 ms, still pending | The progress bar fades in (150 ms, linear loop) and the list dims to ~0.6 opacity (150 ms). The count text changes to "Updating…". Once shown, the bar stays at least 400 ms so it never flashes. |
| 1–3 s | Same state, no escalation. Don't add a skeleton or a second spinner. The dimmed old results and the bar are enough. |
| Over ~10 s | Treat it as a failure (see below). |

## On success

- **List:** cross-fade to the new results over 150 ms and reset scroll to the top without animation. Don't stagger the cards.
- **Pins:** diff them. Pins that remain stay put, new pins fade in over 150 ms, and removed pins fade out over 100 ms. Don't re-drop or bounce the whole set.
- **Count:** the count updates in place with no count-up.
- **Bar and dimming:** both clear over 150 ms.
- **Zero results:** show the empty state in the list. This is a result, not an error, so it needs no error styling.

## Interruption

- If the user changes another filter mid-load, cancel the old request. The bar and dimming keep running and don't restart or flicker.
- Never disable the filters while loading.
- Ignore stale responses so an old reply can't overwrite a newer one.

## If it fails

The main risk is that the filter bar says one thing while the results show another.

- **Keep the old results and pins.** Don't blank anything. Restore full opacity and stop the bar.
- **Show a persistent inline banner at the top of the list**, not a toast, because it relates to those results. Use an icon and text, for example: "Couldn't update results. These may not match your filters. [Retry]". It appears with opacity and a few pixels of travel over 200 ms, in space reserved so the cards don't jump.
- **Mark the stale state.** The count reads "128 homes (not updated)" instead of "Updating…".
- **Keep the user's filter selection.** Don't silently revert it, because Retry needs it.
- **Don't move focus.** The user is likely still in the filter bar. Announce the banner with `role="alert"` and keep Retry reachable by keyboard.
- **Retry:** one silent automatic retry after ~1 s for network blips, before you show the banner. Retry restarts the same loading state. Changing any filter also dismisses the banner and starts a new load.
- **Timeout:** fail at about 10 s. Use the same banner with "Taking too long" wording.
- **Offline:** if the browser reports offline, say "You're offline" in the same banner.
- **Motion:** none beyond the banner's fade-in. Skip the shake because there's no field to blame.

## Reduced motion

Drop the looping bar animation and show a static bar or the "Updating…" text alone. Keep the opacity dimming and cross-fades (they're opacity only) and remove pin movement. The banner appears with no travel.

## Defaults I assumed

This is a web product UI, a frequent path, and system reduced-motion honored. Say so if the stack or the area-change behavior differs. For example, if panning the map to a new city triggers the same reload, the same pattern applies, but you could allow a skeleton on the list after 1 s because the old results would no longer be relevant.
