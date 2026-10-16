**Anchor:** calm and decisive, like a quiet productivity tool. The core rule is to keep the old results on screen while new ones load, and never blank the map or list.

## Principles
- **One wait, one indicator.** A filter change triggers one fetch, so it gets one loading signal. The list, map and filter bar don't each show their own.
- **Stale content stays visible.** Users keep their spatial context, and the map doesn't flash to blank.
- **Acknowledge the input instantly.** The filter chip gets its active or applied state within 100 ms, whatever the network does.
- **Don't flash a loader.** Anything under about 300 ms should look like a plain swap.

## Loading, by how long it takes

| Elapsed | List (left) | Map (right) | Filter bar (top) |
|---|---|---|---|
| **0–150 ms** | Unchanged | Unchanged | Chip shows its applied state immediately (100–150 ms color change). This is the only feedback. |
| **150–300 ms** | Unchanged | Unchanged | Unchanged. If results arrive in this window, they swap in with no loader (see below). |
| **300 ms–1 s** | Existing cards dim to about 60% opacity (150 ms ease-out). Cards stay readable and scrollable. | Existing pins stay. The map stays fully interactive. | A 2 px indeterminate bar along the bottom edge of the filter bar starts, linear and steady. |
| **1–3 s** | Same dimmed cards. The result count in the list header changes to "Updating…". | Same pins. A small "Updating results…" pill appears at the top of the map. | The progress bar continues. |

- **Why the filter bar.** It's the thing that caused the wait, so progress lives there (cause and effect). The bar is thin, so it doesn't add a second heavy loader.
- **Pill on the map.** The pill is optional. It's the one place to say what's happening when the list is off-screen on a narrow layout. Keep it to one line, and fade it in and out over about 150 ms.
- **Once shown, stay.** The bar and pill stay visible for at least 300–500 ms, so a result that lands just after they appear doesn't produce a flicker.
- **No skeletons for filter changes.** The layout is already known and content is already there. Replacing cards with grey blocks would make a 1-second wait feel worse. Use skeletons only for the first load of a new area, when nothing is on screen.

## When results arrive
- **List:** the cards fade back to full opacity and swap content in one 150–200 ms opacity change. Don't stagger. Don't animate card positions. Reset scroll to the top, without animating the scroll.
- **Map pins:** pins that stay don't move. New pins fade in over about 150–200 ms, and removed pins fade out over about 120 ms. Don't drop or bounce them, because this happens on every filter change.
- **Map viewport:** if the filter changes the bounds, ease the camera with the map's own pan/zoom (about 300–400 ms). Otherwise leave it alone.
- **Count:** update the count in the list header to the real number. No count-up.

## If the user acts while loading
- **Another filter change:** cancel the in-flight request and restart. Controls are never disabled, and the bar keeps running without restarting its animation.
- **Panning or zooming the map:** it works as normal. Pan changes are a separate fetch, and the same single indicator covers both.
- **Hovering or clicking a card or pin:** this works on the stale content. If the item no longer exists when results land, clear the selection quietly.

## When it fails
Failure needs a persistent text message, not just motion.

- **Keep the last good results.** Cards return to full opacity and the pins stay. The screen is still usable, but now stale, so say so.
- **Stop the progress bar.** It disappears in 150 ms.
- **Inline banner at the top of the list** (not a toast, because it must persist and carry an action): an icon, "Couldn't update results. Showing your previous search." and a **Retry** button. It's inserted in space reserved above the list, so the cards don't jump. It fades in over about 200 ms.
- **The failed filter chip** gets a small error marker, so the mismatch between chips and results is visible. Don't silently revert the chip, because that would hide what happened.
- **Optional secondary cue:** a short, small highlight pulse on the banner. No shake, because nothing here is a field the user mistyped.
- **Retry** re-enters the normal loading sequence. The banner stays until the new results land, then fades out over about 150 ms.
- **Timeout:** at around 10 s with no response, treat it as a failure with the same banner. Offer **Retry** and let the user cancel.
- **Focus:** don't steal focus. Announce the banner to screen readers with `role="status"`, or `role="alert"` for errors.

**Empty result is not a failure.** Zero matches gets its own message in the list ("No homes match these filters", with a "Clear filters" action). The map shows no pins and stays at its current view.

## Spec

| Element | Trigger | Duration | Easing |
|---|---|---|---|
| Chip applied state | Click | 100–150 ms | ease-out |
| Progress bar appears | Wait > 300 ms | Instant start | Linear, looping |
| List dim | Wait > 300 ms | 150 ms | ease-out |
| Results swap | Data arrives | 150–200 ms | ease-out |
| Pin enter / exit | Data arrives | 150–200 ms / 120 ms | ease-out / ease-in |
| Error banner in / out | Failure / retry succeeds | 200 ms / 150 ms | ease-out / ease-in |
| Minimum loader display | Once shown | 300–500 ms | n/a |

Only opacity and transform animate. The progress bar translates on the compositor.

## Reduced motion
Replace the sliding progress bar with a static "Updating…" label in the same spot. Keep the dim, the opacity swaps, the banner and the focus rings. Skip animated camera moves and snap the viewport instead.

## Two choices for you
1. **Dim level.** I suggested 60% opacity. Go lighter, around 75%, if the list contrast ratio becomes a problem.
2. **Map pill vs. no pill.** If the layout is always side by side and the filter bar is always visible, drop the pill and rely on the filter bar progress and list header. Keep it on mobile, where the map and list are separate views.
