**Anchor:** quiet and crisp, like a focused productivity tool. I'm assuming a web app where filters get changed often, so the cheapest treatment wins.

## Principles

- **Never blank the screen.** Old results and pins stay put until the new ones are ready.
- **One wait, one indicator.** The list and map load from the same request, so there is one signal, not two spinners.
- **Never disable anything.** A new filter change cancels the in-flight request and starts again.

## Success path, by wait time

| Time | Filter bar | List (left) | Map (right) |
|---|---|---|---|
| **0–100 ms** | The chip or control shows its pressed or selected state at once (100 ms). | No change. | No change. |
| **to ~300 ms** | Nothing more. | Nothing. No spinner, no dimming. When results arrive, swap them in place with a 150 ms opacity cross-fade. No stagger, no slide. | Pins swap with the same 150 ms fade. The viewport doesn't move unless the area changed. |
| **300 ms–1 s** | A 2px indeterminate bar appears along the bottom edge of the filter bar, because the filter bar started the wait. Once shown, it stays at least 400 ms so it never flashes. | Stale cards dim to about 60% opacity over 150 ms. They stay readable and scrollable. | Stale pins dim to about 60% and stay clickable. Tiles and viewport are untouched. |
| **1–3 s** | Same bar. | The result-count line changes to text such as "Updating 212 homes…". This is the only text added. | Same as above. |
| **Arrival** | Bar finishes and fades out (150 ms). | Cards go back to full opacity and cross-fade to the new set (150 ms). The scroll position resets to the top, without animation. | Old pins fade out and new pins fade in over 150 ms. If the area changed, ease the viewport over 300 ms. |

- **First load, with nothing stale to show:** the list gets content-shaped skeleton cards (about 6, no stagger, with a slow shimmer or none). They are in place on first paint, never an empty frame first. The map shows tiles with no pins, and the pins fade in.
- **The bar uses linear motion** with a steady loop. Don't fake a percentage.
- **Don't put a spinner in the filter chip.** The chip is just a toggle, and the result is elsewhere.

## Failure

Don't clear the results and don't show a full-panel error. The old results are still useful, but they no longer match the filters, so the screen has to say so in text.

1. **Bar stops and fades out (150 ms).** The dimming lifts so the old results are fully readable again.
2. **A banner appears at the top of the list.** It reads "Couldn't update results. These are from your previous filters." with a **Retry** button. It uses an error icon and color, and it persists until it's resolved or dismissed. It fades in over 200 ms and has reserved space, so the cards don't jump. Don't shake anything.
3. **The filter bar shows what's out of sync.** The changed chip gets a small warning dot, so it's clear which filter isn't applied yet.
4. **The map keeps its old pins at full opacity.** It gets no separate error, because the banner covers it.
5. **Retry puts its loader inside the button.** The label becomes "Retrying…" at the same width. If the wait is over 300 ms, the filter-bar bar runs again. If it succeeds, the banner fades out (150 ms) and the arrival sequence above plays.
6. **Changing another filter dismisses the banner.** It starts a fresh request, which follows the normal path.
7. **Zero results isn't an error.** It gets its own empty state: "No homes match. Try widening price or area."
8. **Offline** uses the same banner with different text: "You're offline." Retry becomes automatic when the connection returns.

## Reduced motion

- Remove the bar's sweep, the skeleton shimmer and the viewport easing (the map just jumps).
- Keep the dimming, the opacity swaps, the "Updating…" text and the banner. Those are state feedback, not movement.
- Show the bar as a static partial-width line, or drop it, since the text already covers the wait.

## Spec

| Moment | Trigger | Duration | Easing | Interruption |
|---|---|---|---|---|
| Pressed or selected state | Click | 100 ms | ease-out | – |
| Loader bar in | Request pending for more than 300 ms | 150 ms | ease-out | Min visible 400 ms |
| Stale dim | With the loader bar | 150 ms | ease-out | Retargets on a new request |
| Results and pins swap | Data arrives | 150 ms | ease-out in, linear out | A new request cancels the old one |
| Error banner in | Request fails | 200 ms | ease-out | Out: 150 ms |
| Viewport move | Area changed | 300 ms | ease-in-out | User pan or zoom cancels it |

All of it animates opacity and transform only, never layout.
